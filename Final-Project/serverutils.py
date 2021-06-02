import http.client
import json
import socketserver
import termcolor
import http.server
import jinja2
from urllib.parse import urlparse, parse_qs
import pathlib

dict_genes = {"FRAT1": "ENSG00000165879",
    "ADA":  "ENSG00000196839",
    "FXN":  "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"}


def print_colored(message, color):
    from termcolor import cprint, colored
    print(colored(message,color))


def take_out_space(word):
    return word.replace(" ", "_")


def read_template_html_file(filename):
    return jinja2.Template(pathlib.Path(filename).read_text())


def obtain_dict(ENDPOINT):
    SERVER = "rest.ensembl.org"
    PARAMS = "?content-type=application/json"
    print(f"\nURl: {SERVER + ENDPOINT + PARAMS}")
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", ENDPOINT + PARAMS)
    r = conn.getresponse()
    print(f"Response received!: {r.status} {r.reason}\n")
    data = r.read().decode("utf-8")
    dict_data = json.loads(data)
    return dict_data


def list_species(data_dict, limit):
    number_species = len(data_dict["species"])
    species_list = []
    try:
        for n in range(0, int(limit)):
            try:
                species_list.append(data_dict["species"][n]["display_name"])
            except KeyError:
                pass
            except IndexError:
                break
        context = {"limit": limit, "list_species": species_list, "number_species": number_species}
        content = read_template_html_file("html/list_species.html").render(context=context)
    except ValueError:
        content = read_template_html_file("html/error.html").render()
    return content


def list_chrom(data_dict, specie):
    try:
        context = {"specie": specie, "karyotype": data_dict["karyotype"]}
        content = read_template_html_file("html/karyotype.html").render(context=context)
    except KeyError:
        content = read_template_html_file("html/error.html").render()
    return content


def list_len(data_dict, specie, chromo):
    try:
        chromo_len = data_dict["length"]
        context = {"specie": specie, "chromo": chromo, "chromo_len": chromo_len}
        content = read_template_html_file("html/chromosomeLength.html").render(context=context)
    except KeyError:
        content = read_template_html_file("html/error.html").render()
    return content


def seq_gene(data_dict, gene_id, gene_name):
    try:
        seq = data_dict["seq"]
        context = {"seq": seq, "gene_id": gene_id, "gene_name": gene_name}
        content = read_template_html_file("html/geneSeq.html").render(context=context)
    except KeyError:
        content = read_template_html_file("html/error.html").render()
    return content


def info_gene(data_dict, gene_id, gene_name):
    try:
        chrom_name = data_dict["desc"].split(":")[2]
        start = data_dict["desc"].split(":")[3]
        end = data_dict["desc"].split(":")[4]
        seq_len = int(data_dict["desc"].split(":")[4])-int(data_dict["desc"].split(":")[3]) + 1
        context = {"seq_len": seq_len, "gene_id": gene_id, "gene_name": gene_name,
                   "chro_name": chrom_name, "start": start, "end": end}
        content = read_template_html_file("html/geneInfo.html").render(context=context)
    except KeyError:
        content = read_template_html_file("html/error.html").render()
    return content


def calc_gene(data_dict, gene_id, gene_name):
    try:
        seq1 = Seq(data_dict["seq"])
        seq_len = seq1.len()
        seq_count = seq1.count()
        seq_per = seq1.percentage_base(seq1.count_bases(), seq_len)
        context = {"seq_per": seq_per, "gene_id": gene_id, "seq_len": seq_len, "seq_count": seq_count, "gene_name": gene_name}
        content = read_template_html_file("html/geneCalc.html").render(context=context)
    except KeyError:
        content = read_template_html_file("html/error.html").render()
    return content



class Seq:
    NULL_SEQUENCE = "NULL"
    INVALID_SEQUENCE = "ERROR"

    def __init__(self, str_bases=NULL_SEQUENCE):
        if str_bases == Seq.NULL_SEQUENCE:
            print("NULL seq created")
            self.str_bases = str_bases
        elif Seq.is_valid_seq2(str_bases):
            self.str_bases = str_bases
            print("New sequence created!")
        else:
            self.str_bases = Seq.INVALID_SEQUENCE
            print("INCORRECT Sequence detected.")

    @staticmethod
    def is_valid_seq2(str_bases):
        for i in str_bases:
            if i != "A" and i != "C" and i != "G" and i != "T":
                return False
        return True

    def __str__(self):
        return self.str_bases

    def len(self):
        if self.str_bases == Seq.NULL_SEQUENCE or self.str_bases == Seq.INVALID_SEQUENCE:
            return 0
        else:
            return len(self.str_bases)


    def count_bases(self):
        a, c, g, t = 0, 0, 0, 0
        if not (self.str_bases == Seq.NULL_SEQUENCE) and not (self.str_bases == Seq.INVALID_SEQUENCE):
            for ch in self.str_bases:
                if ch == "A":
                    a += 1
                elif ch == "T":
                    t += 1
                elif ch == "G":
                    g += 1
                elif ch == "C":
                    c += 1
        return a, c, g, t

    def count(self):
        a, c, g, t = self.count_bases()
        return {"A" : a, "C": c , "G" : g, "T" : t}

    def percentage_base(self, count_bases, seq_len):
        a = str(round(count_bases[0] / seq_len*100, 2)) + "%"
        c = str(round(count_bases[1] / seq_len * 100, 2)) + "%"
        g = str(round(count_bases[2] / seq_len * 100, 2)) + "%"
        t = str(round(count_bases[3] / seq_len * 100, 2)) + "%"
        return {"A": a, "C": c, "G": g, "T": t}
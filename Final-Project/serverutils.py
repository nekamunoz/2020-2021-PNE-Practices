import http.client
import json
import socketserver
import termcolor
import http.server
import jinja2
from urllib.parse import urlparse, parse_qs
import pathlib


def print_colored(message, color):
    from termcolor import cprint, colored
    print(colored(message,color))


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


def seq_gene(data_dict, id):
    try:
        seq = data_dict["seq"]
        context = {"seq": seq, "gene_id": id}
        content = read_template_html_file("html/geneSeq.html").render(context=context)
    except KeyError:
        content = read_template_html_file("html/error.html").render()
    return content


def info_gene(data_dict, id):
    pass


def calc_gene(data_dict, id):
    try:
        seq1 = Seq(data_dict["seq"])
        seq_len = seq1.len()
        seq_count = seq1.count()
        context = {"seq": seq1, "gene_id": id, "seq_len": seq_len, "seq_count": seq_count}
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
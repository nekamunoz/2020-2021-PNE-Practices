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


def get_json(data_dict):
    return json.dumps(data_dict)


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


def index(context, arguments):
    context["dict_genes"] = dict_genes
    if "json" in arguments.keys() and arguments["json"][0] == "1":
        contents = get_json({"index":"""-BASIC level\n1) Species list\n2) Species karyotype\n3) Chromosome length
        \n-INTERMEDIATE level\n4) Gene sequence \n5) Gene information\n6) Gene calculations\n"""})
        content_type = 'application/json'
    else:
        contents = read_template_html_file("./html/indx.html").render(context=context)
        content_type = 'text/html'
    return contents, content_type


def list_species(arguments, data_dict):
    try:
        limit = arguments["limit"][0]
    except KeyError:
        limit = len(data_dict["species"])
    species_list = []
    try:
        for n in range(0, int(limit)):
            try:
                species_list.append(data_dict["species"][n]["display_name"])
            except KeyError:
                pass
            except IndexError:
                break
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents = get_json({"limit": limit, "list_species": species_list, "number_species": len(data_dict["species"])})
            content_type = 'application/json'
        else:
            context = {"limit": limit, "list_species": species_list, "number_species": len(data_dict["species"])}
            contents = read_template_html_file("html/list_species.html").render(context=context)
            content_type = 'text/html'
    except ValueError:
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents, content_type = get_json({"ERROR": "Incorrect limit."}), 'application/json'
        else:
            contents, content_type = read_template_html_file("html/error.html").render(), 'text/html'
    return contents, content_type


def list_chrom(arguments):
    try:
        specie = take_out_space(arguments["specie"][0])
        data_dict = obtain_dict("/info/assembly/" + specie)
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents = get_json({"specie": specie, "karyotype": data_dict["karyotype"]})
            content_type = 'application/json'

        else:
            context = {"specie": specie, "karyotype": data_dict["karyotype"]}
            contents = read_template_html_file("html/karyotype.html").render(context=context)
            content_type = 'text/html'
    except KeyError:
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents, content_type = get_json({"ERROR": "Incorrect karyotype."}), 'application/json'
        else:
            contents, content_type = read_template_html_file("html/error.html").render(), 'text/html'
    return contents, content_type


def list_len(arguments):
    try:
        specie = take_out_space(arguments["specie"][0])
        chromo = arguments["chromo"][0]
        data_dict = obtain_dict("/info/assembly/" + specie + "/" + chromo)
        chromo_len = data_dict["length"]
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents = get_json({"specie": specie, "chromo": chromo, "chromo_len": chromo_len})
            content_type = 'application/json'
        else:
            context = {"specie": specie, "chromo": chromo, "chromo_len": chromo_len}
            contents = read_template_html_file("html/chromosomeLength.html").render(context=context)
            content_type = 'text/html'
    except KeyError:
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents, content_type = get_json({"ERROR": "Incorrect specie or chromosome."}), 'application/json'
        else:
            contents, content_type = read_template_html_file("html/error.html").render(), 'text/html'
    return contents, content_type


def gene(arguments, path_name):
    try:
        gene_name = arguments["gene"][0]
        gene_id = dict_genes[gene_name]
        gene_seq = obtain_dict("/sequence/id/" + gene_id)
        if path_name == "/geneSeq":
            contents, content_type = seq_gene(arguments, gene_seq, gene_id, gene_name)
        elif path_name == "/geneInfo":
            contents, content_type = info_gene(arguments, gene_seq, gene_id, gene_name)
        elif path_name == "/geneCalc":
            contents, content_type = calc_gene(arguments, gene_seq, gene_id, gene_name)
    except KeyError:
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents, content_type = get_json({"ERROR": "Incorrect gene."}), 'application/json'
        else:
            contents, content_type = read_template_html_file("html/error.html").render(), 'text/html'
    return contents, content_type


def seq_gene(arguments, data_dict, gene_id, gene_name):
    try:
        context = {"seq": data_dict["seq"], "gene_id": gene_id, "gene_name": gene_name}
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents, content_type = get_json(context), 'application/json'
        else:
            contents, content_type = read_template_html_file("html/geneSeq.html").render(context=context), 'text/html'
    except KeyError:
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents, content_type = get_json({"ERROR": "error"}), 'application/json'
        else:
            contents, content_type = read_template_html_file("html/error.html").render(), 'text/html'
    return contents, content_type


def info_gene(arguments, data_dict, gene_id, gene_name):
    try:
        chro_name = data_dict["desc"].split(":")[2]
        start = data_dict["desc"].split(":")[3]
        end = data_dict["desc"].split(":")[4]
        seq_len = int(data_dict["desc"].split(":")[4])-int(data_dict["desc"].split(":")[3]) + 1
        context = {"seq_len": seq_len, "gene_id": gene_id, "gene_name": gene_name,
                   "chro_name": chro_name, "start": start, "end": end}
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents, content_type = get_json(context), 'application/json'
        else:
            contents, content_type = read_template_html_file("html/geneInfo.html").render(context=context), 'text/html'
    except KeyError:
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents, content_type = get_json({"ERROR": "error"}), 'application/json'
        else:
            contents, content_type = read_template_html_file("html/error.html").render(), 'text/html'
    return contents, content_type


def calc_gene(arguments, data_dict, gene_id, gene_name):
    try:
        seq1 = Seq(data_dict["seq"])
        seq_per = seq1.percentage_base(seq1.count_bases(), seq1.len())
        context = {"seq_per": seq_per, "gene_id": gene_id, "seq_len": seq1.len(),
                   "seq_count": seq1.count(), "gene_name": gene_name}
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents, content_type = get_json(context), 'application/json'
        else:
            contents, content_type = read_template_html_file("html/geneCalc.html").render(context=context), 'text/html'
    except KeyError:
        if "json" in arguments.keys() and arguments["json"][0] == "1":
            contents, content_type = get_json({"ERROR": "error"}), 'application/json'
        else:
            contents, content_type = read_template_html_file("html/error.html").render(), 'text/html'
    return contents, content_type



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
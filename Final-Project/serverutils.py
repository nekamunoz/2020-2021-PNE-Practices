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


def obtain_data(ENDPOINT):
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
    for n in range(0, int(limit)):
        try:
            species_list.append(data_dict["species"][n]["display_name"])
        except KeyError:
            pass
        except IndexError:
            break
    context = {"limit": limit, "list_species": species_list, "number_species": number_species}
    content = read_template_html_file("html/list_species.html").render(context=context)
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
        chromo_len = data_dict["top_level_region"][int(chromo)]["length"]
        context = {"specie": specie, "chromo": chromo, "chromo_len": chromo_len}
        content = read_template_html_file("html/chromosomeLength.html").render(context=context)
    except KeyError:
        content = read_template_html_file("html/error.html").render()
    return content



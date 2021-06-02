import json
from termcolor import cprint


def get_connection(conn, path_name, argument, val1, val2):
    try:
        if path_name == "/":
            conn.request("GET", "/?json=1")
        elif path_name == "/chromosomeLength":
            conn.request("GET", path_name + "?specie=" + val1 + "&chromo=" + val2 + "&json=1")
        else:
            conn.request("GET", path_name + "?" + argument + "=" + val1 + "&json=1")
    except ConnectionRefusedError:
        cprint("ERROR! Cannot connect to the Server", 'red')
        exit()


def get_response(conn):
    r = conn.getresponse()
    response = r.read().decode("utf-8")
    data = json.loads(response)
    return data


def print_index(data):
    cprint(data["index"], 'yellow')


def print_list_species(data):
    if "ERROR" in data.keys():
        cprint("ERROR: Incorrect limit", "red")
    else:
        cprint("The total number of species in the ensembl is:", 'blue', end=" ")
        print(data["number_species"])
        cprint("The limit you have selected is:", 'blue', end=" ")
        print(data["limit"])
        cprint("The names of the species are: ", 'blue')
        for n in data["list_species"]:
            print(" - " + n)


def print_karyotype(data):
    if "ERROR" in data.keys():
        cprint("ERROR: Incorrect karyotype.", "red")
    else:
        cprint("Karyotype of the: ", 'blue', end=" ")
        print(data["specie"])
        cprint("The names of the chromosomes are:", 'blue')
        for n in data["karyotype"]:
            print(" - " + n)


def print_chromolen(data):
    if "ERROR" in data.keys():
        cprint("ERROR: Incorrect specie or chromosome.", "red")
    else:
        cprint("Specie: ", 'blue', end=" ")
        print(data["specie"])
        cprint("Chromosome: ", 'blue', end=" ")
        print(data["chromo"])
        cprint("Length:", 'blue', end=" ")
        print(data["chromo_len"])


def print_gene_seq(data):
    if "ERROR" in data.keys():
        cprint("ERROR: Incorrect gene.", "red")
    else:
        cprint("Sequence of the gene ", 'blue', end=" ")
        print(data["gene_name"])
        cprint("Ensembl ID: ", 'blue', end=" ")
        print(data["gene_id"])
        cprint("The sequence is:", 'blue', end=" ")
        print(data["seq"])

def print_gene_info(data):
    if "ERROR" in data.keys():
        cprint("ERROR: Incorrect gene.", "red")
    else:
        cprint("Information of the gene ", 'blue', end=" ")
        print(data["gene_name"])
        cprint("Ensembl ID: ", 'blue', end=" ")
        print(data["gene_id"])
        cprint("Chromosome name: ", 'blue', end=" ")
        print(data["chro_name"])
        cprint("Start: ", 'blue', end=" ")
        print(data["start"])
        cprint("End: ", 'blue', end=" ")
        print(data["end"])
        cprint("Length: ", 'blue', end=" ")
        print(data["seq_len"])


def print_gene_calc(data):
    if "ERROR" in data.keys():
        cprint("ERROR: Incorrect gene.", "red")
    else:
        cprint("Calculation of the gene ", 'blue', end=" ")
        print(data["gene_name"])
        cprint("Ensembl ID: ", 'blue', end=" ")
        print(data["gene_id"])
        cprint("Total length: ", 'blue', end=" ")
        print(data["seq_len"])
        cprint("Percentage bases:  ", 'blue')
        for key, value in data["seq_per"].items():
            print(" - " + key + ":" + str(value))
        cprint("Count bases: ", 'blue')
        for key, value in data["seq_count"].items():
            print(" - " + key + ": " + str(value))
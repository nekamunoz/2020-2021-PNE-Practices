import http.client
import json
from termcolor import cprint
import termcolor
import clientutils as cu

PORT = 8080
SERVER = 'localhost'
list_func = ["/", "/listSpecies", "/karyotype", "/chromosomeLength", "/geneSeq", "/geneInfo", "/geneCalc"]


cprint("ADVANCED Level Services")
cprint(f"\nConnecting to server: {SERVER}:{PORT}\n", 'red')
conn = http.client.HTTPConnection(SERVER, PORT)

for path_name in list_func:
    if path_name == "/":
        cprint("------------------ INDEX ---------------------", 'yellow')
        cu.get_connection(conn, path_name, argument=None, val1=None, val2=None)
        cu.print_index(cu.get_response(conn))
    elif path_name == "/listSpecies":
        cprint("\n---> ListSpecies endpoint", 'yellow', end=" ")
        argument, v1, v2 = "limit", "", "2"
        cprint("\n------Test 1-----")
        cu.get_connection(conn, path_name, argument=argument, val1=v1, val2=None)
        cu.print_list_species(cu.get_response(conn))
        cprint("\n------Test 2-----")
        cu.get_connection(conn, path_name, argument=argument, val1=v2, val2=None)
        cu.print_list_species(cu.get_response(conn))
    elif path_name == "/karyotype":
        cprint("\n---> Karyotype endpoint", 'yellow', end=" ")
        argument, v1, v2, v3 = "specie", "", "homo_sapiens", "cat"
        cprint("\n------Test 1-----")
        cu.get_connection(conn, path_name, argument=argument, val1=v1, val2=None)
        cu.print_karyotype(cu.get_response(conn))
        cprint("\n------Test 2-----")
        cu.get_connection(conn, path_name, argument=argument, val1=v2, val2=None)
        cu.print_karyotype(cu.get_response(conn))
        cprint("\n------Test 3-----")
        cu.get_connection(conn, path_name, argument=argument, val1=v3, val2=None)
        cu.print_karyotype(cu.get_response(conn))
    elif path_name == "chromosomeLength":
        cprint("\n---> ChromosomeLength endpoint", 'yellow', end=" ")
        v1, v2, v3, v4, v5 = "human", "X", "", "cat", "5"
        cprint("\n------Test 1-----")
        cu.get_connection(conn, path_name, argument=None, val1=v1, val2=v2)
        cu.print_chromolen(cu.get_response(conn))
        cprint("\n------Test 2-----")
        cu.get_connection(conn, path_name, argument=None, val1=v3, val2=v2)
        cu.print_chromolen(cu.get_response(conn))
        cprint("\n------Test 3-----")
        cu.get_connection(conn, path_name, argument=None, val1=v1, val2=v3)
        cu.print_chromolen(cu.get_response(conn))
        cprint("\n------Test 4-----")
        cu.get_connection(conn, path_name, argument=None, val1=v4, val2=v5)
        cu.print_chromolen(cu.get_response(conn))
    elif path_name.startswith("/gene"):
        argument, v1, v2 = "gene", "FRAT1", ""
        cprint("\n---> " + path_name.replace("/", "") + "endpoint", 'yellow', end=" ")
        if path_name == "/geneSeq":
            cprint("\n------Test 1-----")
            cu.get_connection(conn, path_name, argument=argument, val1=v1, val2=None)
            cu.print_gene_seq(cu.get_response(conn))
            cprint("\n------Test 2-----")
            cu.get_connection(conn, path_name, argument=argument, val1=v2, val2=None)
            cu.print_gene_seq(cu.get_response(conn))
        elif path_name == "/geneInfo":
            cprint("\n------Test 1-----")
            cu.get_connection(conn, path_name, argument=argument, val1=v1, val2=None)
            cu.print_gene_info(cu.get_response(conn))
            cprint("\n------Test 2-----")
            cu.get_connection(conn, path_name, argument=argument, val1=v2, val2=None)
            cu.print_gene_info(cu.get_response(conn))
        elif path_name == "/geneCalc":
            cprint("\n------Test 1-----")
            cu.get_connection(conn, path_name, argument=argument, val1=v1, val2=None)
            cu.print_gene_calc(cu.get_response(conn))
            cprint("\n------Test 2-----")
            cu.get_connection(conn, path_name, argument=argument, val1=v2, val2=None)
            cu.print_gene_calc(cu.get_response(conn))
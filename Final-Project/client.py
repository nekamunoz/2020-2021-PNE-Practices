import http.client
import json
from termcolor import cprint
import termcolor
import clientutils as cu

PORT = 8080
SERVER = 'localhost'
url_request = "/?json=1"   #CHANGE THE URL HERE
path_name = url_request.split("?")[0]

if "json=1" in url_request:
    cprint(f"\nURL requested: {url_request}", 'red')
    cprint(f"\nConnecting to server: {SERVER}:{PORT}\n", 'red')
    conn = http.client.HTTPConnection(SERVER, PORT)
    try:
        conn.request("GET", url_request)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r = conn.getresponse()
    cprint(f"Response received!: {r.status} {r.reason}\n", 'red')
    response = r.read().decode("utf-8")
    data = json.loads(response)

    if path_name == "/":
        cprint("\n----- INDEX ----", 'yellow')
        cu.print_index(data)

    elif path_name == "/listSpecies":
        cprint("\n---- ListSpecies ----", 'yellow')

    elif path_name == "/karyotype":
        cprint("\n---- Karyotype ----", 'yellow')

    elif path_name == "chromosomeLength":
        cprint("\n---- ChromosomeLength ----", 'yellow')

    elif path_name == "/geneSeq":
        cprint("\n---- GeneSeq ----", 'yellow')

    elif path_name == "/geneInfo":
        cprint("\n---- GeneInfo ----", 'yellow')

    elif path_name == "/geneCalc":
        cprint("\n---- GeneCalc ----", 'yellow')

else:
    print("No connection established between the client and the server was requested.")










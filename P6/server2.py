import socketserver
import termcolor
import pathlib
import http.server
from urllib.parse import urlparse, parse_qs
import jinja2
import server_utils2 as su


PORT = 9090
HTML_ASSETS = "./html/"
LIST_SEQUENCE = ["ATTCGATGTGCTAGTCGATGCTGTGTACGTCAGTCAGTCGAT", "CAGTAGATGACGAGCGATGAGCAACCGCATCGAT", "ACGATATAGGAGATATGAGGACACACAATGAGATACA",
     "CAGTACAGATAGAGACATAGATATCACTATACAAAAAAAAAAGTTGAGTA", "CGATACGCAGACTATCGACTAGATATA"]
LIST_GENES = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5" ]
LIST_FUNC = ["Info", "Comp", "Rev"]
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        termcolor.cprint(self.path, 'blue')
        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested:", path_name)
        print("Parameters:", arguments)

        context = {}
        if path_name == "/":
            context["n_sequences"] = len(LIST_SEQUENCE)
            context["name_genes"] = LIST_GENES
            context["operations"] = LIST_FUNC
            contents = su.read_template_html_file("./html/index.html").render(context=context)
        elif path_name == "/ping":
            contents = su.read_template_html_file("html/ping.html").render()
        elif path_name == "/get":
            number_sequence = arguments["sequence"][0]
            contents = su.get(LIST_SEQUENCE, number_sequence)
        elif path_name == "/gene":
            gene = arguments["gene"][0]
            contents = su.gene(gene)
        elif path_name == "/operation":
            try:
                sequence = arguments["sequence"][0]
                operation_name = arguments["calculation"][0]
                contents = su.operation(sequence, operation_name)
            except KeyError:
                contents = su.read_template_html_file("./html/ERROR.html").render()
        else:
            contents = su.read_template_html_file("./html/ERROR.html").render()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())
        return

Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
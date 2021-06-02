import http.client
import json
import socketserver
import termcolor
import http.server
import jinja2
from urllib.parse import urlparse, parse_qs
import copyserverutils as su
import clientutils as cu
import pathlib

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        o = urlparse(self.path)
        path_name = o.path
        arguments = parse_qs(o.query)
        print("Resource requested:", path_name)
        print("Parameters:", arguments)
        context = {}
        if path_name == "/":
            contents, content_type = su.index(context, arguments)
        elif path_name == "/listSpecies":
            dict_species = su.obtain_dict("/info/species")
            contents, context_type = su.list_species(arguments, dict_species)
        elif path_name == "/karyotype":
            contents, content_type = su.list_chrom(arguments)
        elif path_name == "/chromosomeLength":
            contents, content_type = su.list_len(arguments)
        elif path_name.startswith("/gene"):
            contents, content_type = su.gene(arguments, path_name)
        else:
            if "json" in arguments.keys() and arguments["json"][0] == "1":
                contents, content_type = cu.get_json({"ERROR": "error"}), 'application/json'
            else:
                contents, content_type = su.read_template_html_file("html/error.html").render(), 'text/html'
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
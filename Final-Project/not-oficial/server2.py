import socketserver
import http.server
from urllib.parse import urlparse, parse_qs
import serverutils2 as su

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
            context["dict_genes"] = su.dict_genes
            contents = su.read_template_html_file("../html/indx.html").render(context=context)
        elif path_name == "/listSpecies":
            dict_species = su.obtain_dict("/info/species")
            try:
                limit = arguments["limit"][0]
            except KeyError:
                limit = len(dict_species["species"])
            contents = su.list_species(dict_species, limit)
        elif path_name == "/karyotype":
            try:
                specie = su.take_out_space(arguments["specie"][0])
                dict_chrom = su.obtain_dict("/info/assembly/" + specie)
                contents = su.list_chrom(dict_chrom, specie)
            except KeyError:
                contents = su.read_template_html_file("../html/error.html").render()
        elif path_name == "/chromosomeLength":
            try:
                specie = su.take_out_space(arguments["specie"][0])
                chromo = arguments["chromo"][0]
                dict_len = su.obtain_dict("/info/assembly/" + specie + "/" + chromo)
                contents = su.list_len(dict_len, specie, chromo)
            except KeyError:
                contents = su.read_template_html_file("../html/error.html").render()
        elif path_name.startswith("/gene"):
            try:
                gene_name = arguments["gene"][0]
                gene_id = su.dict_genes[gene_name]
                gene_seq = su.obtain_dict("/sequence/id/" + gene_id)
                if path_name == "/geneSeq":
                    contents = su.seq_gene(gene_seq, gene_id, gene_name)
                elif path_name == "/geneInfo":
                    contents = su.info_gene(gene_seq, gene_id, gene_name)
                elif path_name == "/geneCalc":
                    contents = su.calc_gene(gene_seq, gene_id, gene_name)
            except KeyError:
                contents = su.read_template_html_file("../html/error.html").render()
        else:
            contents = su.read_template_html_file("../html/error.html").render()
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
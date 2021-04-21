import socketserver
import termcolor
import pathlib
import http.server
from urllib.parse import urlparse, parse_qs


PORT = 8080
HTML_ASSETS = "./html/"


def read_html_file(filename):
    return pathlib.Path(filename).read_text()


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/info" or self.path == "/index.html" or self.path == "/":
            contents = read_html_file(HTML_ASSETS + "index.html")
        elif "/info/" in self.path:
            try:
                contents = read_html_file(HTML_ASSETS + str(self.path) + ".html")
            except FileNotFoundError:
                contents = read_html_file(HTML_ASSETS + "ERROR.html")
        else:
            contents = read_html_file(HTML_ASSETS + "ERROR.html")

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
        print("Stoped by the user")
        httpd.server_close()
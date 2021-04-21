import http.server
import socketserver
import termcolor
import pathlib


PORT = 8080
HTML_ASSETS = "./html/"


def read_html_file(filename):
    return pathlib.Path(filename).read_text()


socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        termcolor.cprint(self.requestline, 'green')
        if self.path == "/" or self.path == "/index.html":
            contents = read_html_file(HTML_ASSETS + "index.html")
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
        print("Stopped by the user")
        httpd.server_close()
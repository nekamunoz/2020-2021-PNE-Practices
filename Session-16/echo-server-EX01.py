import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')  #request line
        contents = Path('form-1.html').read_text()   # Open form1.html and read the index from the file

        self.send_response(200)  # -- Status line: OK!  # Generating the response message
        self.send_header('Content-Type', 'text/html')   # Define the content-type header:
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers() # The header is finished
        self.wfile.write(str.encode(contents))   # Send the response message
        return


Handler = TestHandler  # -- Set the new handler
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
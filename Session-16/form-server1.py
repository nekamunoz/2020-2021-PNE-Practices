import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import urlparse, parse_qs

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')  # request line
        if self.path == "/":
            contents = Path('form-1.html').read_text()
        elif self.path.startswith("/echo"):
            message = parse_qs(urlparse(self.path).query["msg"][0])
            print("The message is: ", message)
            contents = Path('template.html').read_text().format(message)
        else:
            contents = Path('ERROR.html').read_text()

        self.send_response(200)  # -- Status line: OK!, Generating the response message
        self.send_header('Content-Type', 'text/html')   # Define the content-type header:
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers() # The header is finished

        # Send the response message
        self.wfile.write(str.encode(contents))

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
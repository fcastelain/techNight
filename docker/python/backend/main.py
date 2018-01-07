from http.server import BaseHTTPRequestHandler, HTTPServer

hostport = 8081
hostname = "0.0.0.0"

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        if self.path == "/add":
            message = "add 1 to iterator"
        elif self.path == "/remove":
            message = "remove 1 to iterator"
        else:
            message = "Wrong ULR"

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        return


def run():
    print('starting server...')

    # Server settings
    server_address = (hostname, hostport)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()

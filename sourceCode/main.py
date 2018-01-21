from http.server import BaseHTTPRequestHandler, HTTPServer

hostport = 8081
ostname = "0.0.0.0"

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        # infunction of the path change the action
        if self.path == "/add":
            self.send_response(200)
            message = "{ \"action\": \"ADD\", \"value\": 0 }"
        elif self.path == "/remove":
            self.send_response(200)
            message = "{ \"action\": \"REMOVE\", \"value\": 0}"
        else:
            self.send_response(404)
            message = "{ \"code\": 1, \"message\": \"wrong url\" }"

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

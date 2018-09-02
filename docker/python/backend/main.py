from http.server import BaseHTTPRequestHandler, HTTPServer
import configparser

# Get the good properties
config = configparser.ConfigParser()
config.read('properties/INT.properties')

hostport = config['ServerSection']['listen.port']
hostname = config['ServerSection']['listen.host']

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):

        if self.path == "/add":
            # Send response status code
            self.send_response(200)
            message = "{ \"action\": \"ADD\", \"value\": 1 }"
        elif self.path == "/remove":
            # Send response status code
            self.send_response(200)
            message = "{ \"action\": \"REMOVE\", \"value\": 1 }"
        else:
            # Send response status code
            self.send_response(404)
            message = "{ \"code\": 1, \"message\": \"wrong URL\" }"

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        return


def run():
    print('starting server...')

    # Server settings
    server_address = (hostname, int(hostport))
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()

run()

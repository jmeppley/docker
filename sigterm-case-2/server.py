#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
import signal, sys

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.wfile.write(bytes("Hello world!", "utf8"))

if __name__ == '__main__':
    def MySigtermHandler(signum, frame):
        print("Shutting down server via SIGTERM")
        httpd.socket.close()
        sys.exit(0)

    def MySigintHandler(signum, frame):
        print("Shutting down server via SIGINT")
        httpd.socket.close()
        sys.exit(0)

    signal.signal(signal.SIGTERM, MySigtermHandler)
    signal.signal(signal.SIGINT, MySigintHandler)

    print("starting server...")
    httpd = HTTPServer(('', 8000), MyHTTPRequestHandler)
    print('running server...')
    httpd.serve_forever()

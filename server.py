#!/usr/bin/env python

# Requires urllib: pip3 install urllib3

from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        print(self.rfile.read(length).decode('utf-8'))
        self.send_response(200)
        self.send_header('Content-Type','text/html')
        self.end_headers()
        self.wfile.write(bytes("", "utf8"))
        return
        
def run():
    print('Starting skjeng-speedbox-httpserver on port 8080')
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('Server is running, waiting for POST')
    httpd.serve_forever()

run()

#!/usr/bin/env python3
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys

BIND_HOST = 'localhost'
PORT = 8008

class EchoServer(BaseHTTPRequestHandler):
    def do_GET(self):
        content = 'Ola IFSP'
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content.encode())

        print(self.headers)
        print(content)

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--IP', '-ip', help='IP, Default: '+BIND_HOST, type= str, default=BIND_HOST)
    parser.add_argument('--PORT', '-p', help='Port, Default: '+str(PORT), type= int, default= PORT)

    args = parser.parse_args()

    return args

if __name__ == '__main__':
    args = arguments()
    print(f'Listening on http://{BIND_HOST}:{PORT}\n')
    httpd = HTTPServer((BIND_HOST, PORT), EchoServer)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.shutdown()
        print("Ctrl C - Stopping proxy")
        sys.exit(1)
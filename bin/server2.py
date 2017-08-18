#!/usr/bin/env python3
# modify to ad dcommand line arguments for PORT IP address and directory

import http.server
import socketserver
import os

PORT = 8000

web_dir = os.path.join(os.path.dirname(__file__), '../')
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
#httpd.serve_forever()

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()

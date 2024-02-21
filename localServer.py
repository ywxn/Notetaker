# Host a local server, using index.html, located in the root directory.

import http.server
import socketserver

def host():
    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


# Run this file in the terminal, and go to http://localhost:8000/ in your browser.
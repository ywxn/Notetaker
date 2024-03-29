from waitress import serve
from notetaker import app
import sys

def host(port):
    print(f"Starting server at http://localhost:{port}")
    serve(app, port=port)

if __name__ == "__main__":
    #get argument from command line
    port = int(sys.argv[1])
    host(port)
from http.server import SimpleHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import requests


# Allow server to handle multiple clients in threads
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


# Handle HTTP GET requests
class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"Hello world!")


if __name__ == "__main__":
    server = ThreadedHTTPServer(("localhost", 8080), RequestHandler)
    try:
        print("Server started on port 8080")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped")
        server.server_close()

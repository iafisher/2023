from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request as {self.path}")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Response received!")


def main():
    print("Starting the HTTP server")
    http_server = HTTPServer(("", 8080), Handler)
    http_server.serve_forever()


if __name__ == "__main__":
    main()

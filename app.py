from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 8000

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = "Really advanced, but also not an advanced Git Docker App\nStatus: healthy - U66520657\n"

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body.encode())))
        self.end_headers()

        self.wfile.write(body.encode())

    def log_message(self, format, *args):
        print(format % args, flush=True)


if __name__ == "__main__":
    print(f"Application listening on port {PORT}", flush=True)
    server = HTTPServer((HOST, PORT), AppHandler)
    server.serve_forever()

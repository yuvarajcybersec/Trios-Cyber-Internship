from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

LOG_FILE = "logs/local-web-access.log"


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            status = 200
        elif self.path == "/index.html":
            status = 200
        elif self.path == "/login":
            status = 200
        elif self.path == "/admin":
            status = 403
        elif self.path == "/missing":
            status = 404
        else:
            status = 404

        self.send_response(status)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(
            f"<html><body><h1>Status {status}</h1></body></html>".encode()
        )

        timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S")
        client_ip = self.client_address[0]
        user_agent = self.headers.get("User-Agent", "-")

        log_entry = (
            f'{client_ip} - - [{timestamp}] '
            f'"GET {self.path} HTTP/1.1" {status} '
            f'"-" "{user_agent}"\n'
        )

        with open(LOG_FILE, "a") as log:
            log.write(log_entry)

        print(log_entry, end="")


server = HTTPServer(("127.0.0.1", 8080), RequestHandler)

print("Local test server running on http://127.0.0.1:8080")
print("Press Ctrl+C to stop.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    server.server_close()

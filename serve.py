#!/usr/bin/env python3
import http.server
import socketserver
import socket
import os

PORT = 8085
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and disable aggressive caching for dev testing
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == '__main__':
    local_ip = get_local_ip()
    print("=" * 60)
    print("🚀 Money Manager Multi-Device Server Running!")
    print(f"💻 Mac Desktop URL:  http://localhost:{PORT}")
    print(f"📱 Mobile Phone URL: http://{local_ip}:{PORT}")
    print("=" * 60)
    print("👉 ဖုန်း Safari / Chrome တွင် အထက်ပါ Mobile URL ကို ရိုက်ထည့်ပါ")
    print("   သို့မဟုတ် Camera ဖြင့် QR Code ကို Scan ဖတ်ပါ")
    print("=" * 60)

    with ThreadedHTTPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

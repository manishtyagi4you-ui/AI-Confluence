import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    os.chdir(DIRECTORY)
    # Allow port reuse if recently stopped
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print("=" * 58)
        print("🚀 AI Confluence 2026 — Local Web Server Started")
        print(f"🔗 URL: {url}")
        print("💡 Press Ctrl+C in your terminal to stop the server.")
        print("=" * 58)
        
        # Open in default browser
        webbrowser.open(url)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server... Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    start_server()

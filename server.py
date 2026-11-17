from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import os
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="/app/public", **kwargs)
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()
    def log_message(self, fmt, *args):
        print(fmt % args)
ThreadingHTTPServer(("0.0.0.0", 8000), Handler).serve_forever()

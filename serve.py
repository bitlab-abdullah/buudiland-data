#!/usr/bin/env python3
"""
Development server with CORS support for Open SDG data site.
"""

import http.server
import socketserver
import os
import sys
from urllib.parse import urlparse

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Access-Control-Max-Age', '86400')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def serve_site(port=8000, directory='_site'):
    """Serve the built site with CORS headers."""
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found.")
        print("Please run 'python scripts/build_data.py' first to build the site.")
        sys.exit(1)
    
    os.chdir(directory)
    
    with socketserver.TCPServer(("", port), CORSHTTPRequestHandler) as httpd:
        print(f"Serving at http://localhost:{port}")
        print(f"Directory: {os.path.abspath('.')}")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Development server with CORS support')
    parser.add_argument('--port', '-p', type=int, default=8000, 
                       help='Port to serve on (default: 8000)')
    parser.add_argument('--dir', '-d', default='_site',
                       help='Directory to serve (default: _site)')
    
    args = parser.parse_args()
    serve_site(args.port, args.dir)
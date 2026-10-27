#!/usr/bin/env python3
"""Serve only the app's static folder on the local network."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import subprocess
import sys
import time
import urllib.request

class AppHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()
    def list_directory(self, path):
        self.send_error(404, 'Not found')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=4173)
    parser.add_argument('--bind', default='0.0.0.0')
    parser.add_argument('--background', action='store_true')
    args = parser.parse_args()
    if args.background:
        root = Path(__file__).resolve().parent
        try:
            with urllib.request.urlopen(f'http://127.0.0.1:{args.port}/', timeout=2) as response:
                if b'Duolingo codex' in response.read(10000):
                    print('Duolingo codex is already running.', flush=True)
                    sys.exit(0)
        except OSError:
            pass
        with (root / 'server.log').open('a') as log:
            child = subprocess.Popen([sys.executable, str(root / 'server.py'), '--bind', args.bind, '--port', str(args.port)], cwd=root, stdin=subprocess.DEVNULL, stdout=log, stderr=log, start_new_session=True)
        (root / 'server.pid').write_text(str(child.pid))
        for attempt in range(30):
            try:
                with urllib.request.urlopen(f'http://127.0.0.1:{args.port}/', timeout=1) as response:
                    if response.status == 200:
                        print(f'Duolingo codex is running in the background (PID {child.pid}).', flush=True)
                        sys.exit(0)
            except OSError:
                time.sleep(0.1)
        print('Could not start the server. Check server.log.', file=sys.stderr)
        sys.exit(1)
    handler = partial(AppHandler, directory=str(Path(__file__).resolve().parent / 'dist'))
    print(f'Business app ready on port {args.port}. Keep this process running.', flush=True)
    print('This computer: http://127.0.0.1:' + str(args.port), flush=True)
    with ThreadingHTTPServer((args.bind, args.port), handler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass

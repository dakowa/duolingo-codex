#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
echo 'Open http://127.0.0.1:4173 in Chrome on this computer.'
echo 'On another device, use this computer’s Wi-Fi IP address with :4173.'
echo 'Keep this computer awake. The app runs in the background.'
exec python3 server.py --background

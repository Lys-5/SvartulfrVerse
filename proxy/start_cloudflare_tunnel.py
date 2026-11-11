import subprocess
import re
import time
import requests
import pathlib
import sys
import os

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRATCH = ROOT / 'scratch'
PROXY_DIR = ROOT / 'proxy'
CLOUDFLARED_PATH = r"C:\Program Files (x86)\cloudflared\cloudflared.exe"
TOKEN_FILE = SCRATCH / 'wyvern_token.txt'
REFRESH_FILE = SCRATCH / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
PROVIDER_ID = '_BkFy28ggAtq9K7cwk2mfR'

def get_refreshed_token():
    rt = REFRESH_FILE.read_text(encoding='utf-8').strip()
    url = f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}'
    resp = requests.post(url, data={'grant_type': 'refresh_token', 'refresh_token': rt})
    if resp.status_code == 200:
        token = resp.json()['id_token']
        TOKEN_FILE.write_text(token, encoding='utf-8')
        return token
    else:
        # Fallback to existing token
        return TOKEN_FILE.read_text(encoding='utf-8').strip()

def update_wyvern_provider(tunnel_url):
    token = get_refreshed_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    api_url = f"{tunnel_url}/v1"
    url = f"https://app.wyvern.chat/api/providers/{PROVIDER_ID}"
    resp = requests.put(url, headers=headers, json={'api_url': api_url}, timeout=15)
    if resp.status_code == 200:
        print(f"✅ Successfully updated Wyvern Provider '{PROVIDER_ID}' to: {api_url}", flush=True)
        return True
    else:
        print(f"❌ Failed to update Wyvern Provider: HTTP {resp.status_code}: {resp.text[:200]}", flush=True)
        return False

def main():
    print(f"=== Starting Cloudflare Tunnel for Proxy on 127.0.0.1:5005 ===", flush=True)
    if not os.path.exists(CLOUDFLARED_PATH):
        print(f"Error: cloudflared not found at {CLOUDFLARED_PATH}", flush=True)
        sys.exit(1)

    cmd = [CLOUDFLARED_PATH, "tunnel", "--url", "http://127.0.0.1:5005"]
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        encoding='utf-8',
        errors='replace'
    )

    tunnel_url = None
    url_pattern = re.compile(r'https://[a-zA-Z0-9-]+\.trycloudflare\.com')

    # Monitor output for tunnel URL
    for line in iter(process.stdout.readline, ''):
        print(line, end='', flush=True)
        if not tunnel_url:
            match = url_pattern.search(line)
            if match:
                tunnel_url = match.group(0)
                print(f"\n🎉 DISCOVERED TUNNEL URL: {tunnel_url}", flush=True)
                update_wyvern_provider(tunnel_url)

    process.wait()

if __name__ == '__main__':
    main()

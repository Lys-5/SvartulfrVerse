import json
import urllib.request
import urllib.parse
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
RT_PATH = ROOT / 'scratch' / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'

def refresh():
    rt = RT_PATH.read_text(encoding='utf-8').strip()
    url = f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}'
    data = urllib.parse.urlencode({'grant_type': 'refresh_token', 'refresh_token': rt}).encode()
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode())
        token = res['id_token']
        WT_PATH.write_text(token, encoding='utf-8')
        print("Token refreshed successfully, len:", len(token))
        return token

if __name__ == '__main__':
    refresh()

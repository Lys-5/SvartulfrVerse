import urllib.request
import json

try:
    with urllib.request.urlopen('http://127.0.0.1:9222/json') as resp:
        tabs = json.loads(resp.read().decode())
        print(f"Chrome DevTools responsive! Open targets: {len(tabs)}")
        for t in tabs:
            print(f"  Target: {t.get('title')} | URL: {t.get('url')} | Type: {t.get('type')}")
            if 'webSocketDebuggerUrl' in t:
                print(f"    WS: {t.get('webSocketDebuggerUrl')}")
except Exception as e:
    print(f"Error connecting to DevTools: {e}")

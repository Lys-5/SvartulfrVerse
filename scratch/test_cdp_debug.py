import os
import json
import websocket

active_port_file = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort")
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port = lines[0]
    ws_path = lines[1]

ws_url = f"ws://127.0.0.1:{port}{ws_path}"
print("Connecting to:", ws_url)

try:
    ws = websocket.create_connection(ws_url, suppress_origin=True, timeout=3)
    print("Connected successfully!")
    req = {"id": 1, "method": "Target.getTargets"}
    ws.send(json.dumps(req))
    print("Sent Target.getTargets, waiting for recv...")
    res = json.loads(ws.recv())
    print("Received response!")
    targets = res.get('result', {}).get('targetInfos', [])
    for t in targets:
        print(f"- Type: {t.get('type')}, Title: {t.get('title')}, URL: {t.get('url')}")
    ws.close()
except Exception as e:
    print("Error:", type(e), e)

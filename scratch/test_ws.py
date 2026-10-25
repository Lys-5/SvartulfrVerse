import os
import json
import websocket

devtools_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "DevToolsActivePort")
with open(devtools_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
port = lines[0]
ws_path = lines[1]
ws_url = f"ws://127.0.0.1:{port}{ws_path}"
print(f"Connecting to: {ws_url}")

try:
    # suppress origin
    ws = websocket.create_connection(ws_url, timeout=3, suppress_origin=True)
    ws.send(json.dumps({"id": 1, "method": "Target.getTargets"}))
    resp = ws.recv()
    print("Received response!")
    data = json.loads(resp)
    targets = data.get("result", {}).get("targetInfos", [])
    for t in targets:
        if t.get("type") == "page":
            print(f"PAGE: {t.get('title')} | {t.get('url')}")
    ws.close()
except Exception as e:
    print(f"Error: {e}")

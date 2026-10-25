import os
import json
import websocket

devtools_path = os.path.join(os.environ["LOCALAPPDATA"], "Google", "Chrome", "User Data", "DevToolsActivePort")
with open(devtools_path, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]
port = lines[0]
ws_path = lines[1]
ws_url = f"ws://127.0.0.1:{port}{ws_path}"

try:
    ws = websocket.create_connection(ws_url, timeout=3, origin="chrome-devtools://devtools")
    print("Handshake succeeded!")
    ws.send(json.dumps({"id": 1, "method": "Target.getTargets"}))
    resp = ws.recv()
    print("Response:", resp[:200])
    ws.close()
except Exception as e:
    print("Error:", e)

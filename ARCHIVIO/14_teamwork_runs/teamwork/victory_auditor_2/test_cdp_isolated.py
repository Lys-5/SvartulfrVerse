import os
import json
import websocket

active_port_file = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort")
print("DevToolsActivePort path:", active_port_file)
if os.path.exists(active_port_file):
    with open(active_port_file, "r") as f:
        lines = f.read().splitlines()
        port = lines[0]
        ws_path = lines[1]
    ws_url = f"ws://127.0.0.1:{port}{ws_path}"
    print("Connecting to ws_url:", ws_url)
    try:
        ws = websocket.create_connection(ws_url, suppress_origin=True, timeout=10)
        print("Connected!")
        ws.send(json.dumps({"id": 1, "method": "Target.getTargets"}))
        res = json.loads(ws.recv())
        targets = res.get("result", {}).get("targetInfos", [])
        print(f"Found {len(targets)} targets:")
        for t in targets:
            print(f"  - [{t.get('type')}] {t.get('title')} ({t.get('url')})")
        ws.close()
        print("Closed cleanly.")
    except Exception as e:
        print("CDP Error:", e)
else:
    print("DevToolsActivePort not found")

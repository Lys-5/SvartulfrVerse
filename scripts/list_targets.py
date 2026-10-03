import os
import json
import websocket

def get_browser_ws():
    active_port_file = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort")
    with open(active_port_file, 'r') as f:
        lines = f.read().splitlines()
        port = lines[0]
        ws_path = lines[1]
    return f"ws://127.0.0.1:{port}{ws_path}"

def main():
    ws_url = get_browser_ws()
    ws = websocket.create_connection(ws_url, suppress_origin=True)
    
    req = {"id": 1, "method": "Target.getTargets"}
    ws.send(json.dumps(req))
    res = json.loads(ws.recv())
    
    for t in res.get('result', {}).get('targetInfos', []):
        print(f"Type: {t['type']}, URL: {t['url']}")
        
    ws.close()

if __name__ == '__main__':
    main()

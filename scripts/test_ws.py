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
    print("Connecting to:", ws_url)
    
    # Suppress the Origin header or provide a dummy one
    ws = websocket.create_connection(ws_url, suppress_origin=True)
    
    # Get targets
    req = {
        "id": 1,
        "method": "Target.getTargets"
    }
    ws.send(json.dumps(req))
    res = json.loads(ws.recv())
    
    page_target = None
    for t in res.get('result', {}).get('targetInfos', []):
        if t['type'] == 'page':
            page_target = t
            break
            
    if not page_target:
        print("No page target found")
        return
        
    print("Found page:", page_target['targetId'])
    
    # Attach to the page target
    req = {
        "id": 2,
        "method": "Target.attachToTarget",
        "params": {
            "targetId": page_target['targetId'],
            "flatten": True
        }
    }
    ws.send(json.dumps(req))
    
    session_id = None
    while True:
        r = json.loads(ws.recv())
        if r.get('id') == 2:
            session_id = r['result']['sessionId']
            break
            
    print("Attached, session:", session_id)
    
    js = """
    (async () => {
        let res = await fetch('https://janitorai.com/characters/df0ec5c5-1356-40c8-89f1-3b70b8cff244_character-andrew-andy-campbell');
        let html = await res.text();
        let match = html.match(/window\\._storeState_\\s*=\\s*JSON\\.parse\\((.*)\\);/);
        if (match) {
            let jsonStr = JSON.parse(match[1]);
            let data = JSON.parse(jsonStr);
            return Object.keys(data).join(", ") + " | char: " + (data.character ? Object.keys(data.character).join(",") : "no");
        }
        return "No match";
    })()
    """
    
    req = {
        "id": 3,
        "sessionId": session_id,
        "method": "Runtime.evaluate",
        "params": {
            "expression": js,
            "awaitPromise": True,
            "returnByValue": True
        }
    }
    ws.send(json.dumps(req))
    
    while True:
        r = json.loads(ws.recv())
        if r.get('id') == 3:
            print("Result:", r)
            break
            
    ws.close()

if __name__ == '__main__':
    main()

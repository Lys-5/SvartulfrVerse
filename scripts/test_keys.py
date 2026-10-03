import os
import json
import time
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
    
    msg_id = 1
    def send_cmd(method, params=None, session_id=None):
        nonlocal msg_id
        req = {"id": msg_id, "method": method}
        if params: req["params"] = params
        if session_id: req["sessionId"] = session_id
        ws.send(json.dumps(req))
        mid = msg_id
        msg_id += 1
        return mid

    def wait_for_result(target_id):
        while True:
            r = json.loads(ws.recv())
            if r.get('id') == target_id:
                return r.get('result')

    mid = send_cmd("Target.createTarget", {"url": "https://janitorai.com/characters/df0ec5c5-1356-40c8-89f1-3b70b8cff244_character-andrew-andy-campbell"})
    target_id = wait_for_result(mid)['targetId']
    
    mid = send_cmd("Target.attachToTarget", {"targetId": target_id, "flatten": True})
    session_id = wait_for_result(mid)['sessionId']
    
    print("Waiting 10s for load...")
    time.sleep(10)
    
    js = """
    (() => {
        let text = "";
        for (let s of document.querySelectorAll('script')) {
            if (s.textContent.includes('personality')) {
                text = s.textContent.substring(0, 150);
                break;
            }
        }
        return text;
    })()
    """
    mid = send_cmd("Runtime.evaluate", {"expression": js, "returnByValue": True}, session_id=session_id)
    res = wait_for_result(mid)
    
    print("Result:", res.get('result', {}).get('value'))
        
    send_cmd("Target.closeTarget", {"targetId": target_id})
    ws.close()

if __name__ == '__main__':
    main()

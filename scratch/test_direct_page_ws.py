import websocket
import json
import os

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port = lines[0]
    ws_path = lines[1]

ws = websocket.create_connection(f'ws://127.0.0.1:{port}{ws_path}')
ws.send(json.dumps({'id': 1, 'method': 'Target.getTargets'}))
targets = json.loads(ws.recv())['result']['targetInfos']
ws.close()

for t in targets:
    if 'lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC' in t.get('url', ''):
        target_id = t['targetId']
        print(f"Found target: {target_id}")
        page_ws_url = f'ws://127.0.0.1:{port}/devtools/page/{target_id}'
        pws = websocket.create_connection(page_ws_url)
        pws.send(json.dumps({'id': 100, 'method': 'Runtime.evaluate', 'params': {'expression': 'document.title', 'returnByValue': True}}))
        res = json.loads(pws.recv())
        print('Page evaluation result:', res)
        pws.close()
        break

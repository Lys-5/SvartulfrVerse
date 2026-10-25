import websocket
import json
import os

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port = lines[0]
    ws_path = lines[1]

ws = websocket.create_connection(f'ws://127.0.0.1:{port}{ws_path}')

# Find target
ws.send(json.dumps({'id': 1, 'method': 'Target.getTargets'}))
res = json.loads(ws.recv())
target = next(t for t in res['result']['targetInfos'] if 'lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC' in t.get('url', ''))

# Attach
ws.send(json.dumps({'id': 2, 'method': 'Target.attachToTarget', 'params': {'targetId': target['targetId'], 'flatten': True}}))
res = json.loads(ws.recv())
sess_id = res['result']['sessionId']

js = """
(() => {
    let selects = Array.from(document.querySelectorAll('select'));
    return selects.map(s => ({
        name: s.name,
        id: s.id,
        currentValue: s.value,
        options: Array.from(s.options).map(o => ({ value: o.value, text: o.text }))
    }));
})()
"""

ws.send(json.dumps({'id': 3, 'sessionId': sess_id, 'method': 'Runtime.evaluate', 'params': {'expression': js, 'returnByValue': True}}))

while True:
    msg = json.loads(ws.recv())
    if msg.get('id') == 3:
        print(json.dumps(msg['result']['result']['value'], indent=2))
        break

ws.close()

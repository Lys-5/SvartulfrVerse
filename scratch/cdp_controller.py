import websocket
import json
import time

class ChromeCDP:
    def __init__(self):
        import os
        active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
        with open(active_port_file, 'r') as f:
            lines = f.read().splitlines()
            port = lines[0]
            ws_path = lines[1]
        self.browser_ws_url = f'ws://127.0.0.1:{port}{ws_path}'
        self.browser_ws = websocket.create_connection(self.browser_ws_url)
        self.msg_id = 1

    def send_browser(self, method, params=None):
        mid = self.msg_id
        self.msg_id += 1
        payload = {'id': mid, 'method': method}
        if params:
            payload['params'] = params
        self.browser_ws.send(json.dumps(payload))
        while True:
            resp = json.loads(self.browser_ws.recv())
            if resp.get('id') == mid:
                return resp.get('result', {})

    def get_targets(self):
        res = self.send_browser('Target.getTargets')
        return res.get('targetInfos', [])

    def attach_to_page(self, target_id):
        res = self.send_browser('Target.attachToTarget', {'targetId': target_id, 'flatten': True})
        session_id = res.get('sessionId')
        return session_id

    def evaluate_in_session(self, session_id, expression, await_promise=True):
        mid = self.msg_id
        self.msg_id += 1
        payload = {
            'id': mid,
            'sessionId': session_id,
            'method': 'Runtime.evaluate',
            'params': {
                'expression': expression,
                'returnByValue': True,
                'awaitPromise': await_promise
            }
        }
        self.browser_ws.send(json.dumps(payload))
        while True:
            resp = json.loads(self.browser_ws.recv())
            if resp.get('id') == mid:
                if 'error' in resp:
                    raise Exception(resp['error'])
                result = resp.get('result', {}).get('result', {})
                if 'value' in result:
                    return result['value']
                return result

    def close(self):
        self.browser_ws.close()

if __name__ == '__main__':
    cdp = ChromeCDP()
    targets = cdp.get_targets()
    print(f"Found {len(targets)} targets:")
    lorebook_target = None
    for t in targets:
        if t.get('type') == 'page':
            print(f"  [{t['targetId']}] {t.get('title')} -> {t.get('url')}")
            if 'lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC' in t.get('url', ''):
                lorebook_target = t
    if lorebook_target:
        print(f"\nTargeting Lorebook page: {lorebook_target['targetId']}")
        sess = cdp.attach_to_page(lorebook_target['targetId'])
        title = cdp.evaluate_in_session(sess, "document.title")
        print("Page title from session:", title)
    cdp.close()

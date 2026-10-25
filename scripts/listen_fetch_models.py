import os
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    requests = []
    responses = []
    
    def on_req(req):
        if 'model' in req.url or 'navy' in req.url or 'provider' in req.url:
            requests.append({'url': req.url, 'method': req.method})
            
    def on_res(res):
        if 'model' in res.url or 'navy' in res.url or 'provider' in res.url:
            try:
                responses.append({'url': res.url, 'status': res.status, 'text': res.text()[:500]})
            except:
                responses.append({'url': res.url, 'status': res.status})

    page.on('request', on_req)
    page.on('response', on_res)
    
    btn = page.locator('button:has-text("Fetch Models")').first
    btn.click()
    page.wait_for_timeout(3000)
    
    print("Requests:", json.dumps(requests, indent=2))
    print("Responses:", json.dumps(responses, indent=2))

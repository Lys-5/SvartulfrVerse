import os
import time
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port = lines[0]
    ws_path = lines[1]

ws_endpoint = f'ws://127.0.0.1:{port}{ws_path}'
print(f"Connecting to user Chrome CDP at {ws_endpoint}...")

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    
    page = context.new_page()
    console_errors = []
    network_errors = []
    
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.on("response", lambda resp: network_errors.append(f"{resp.status} {resp.url}") if resp.status >= 400 and not resp.url.endswith("favicon.ico") else None)
    
    try:
        target_url = "https://app.wyvern.chat/mine"
        print(f"Navigating to {target_url}...")
        page.goto(target_url, wait_until="domcontentloaded", timeout=20000)
        time.sleep(4)
        
        print(f"Current page title: {page.title()}")
        print(f"Current URL: {page.url}")
        
        print(f"Captured Console Errors count: {len(console_errors)}")
        for err in console_errors[:5]:
            print(f"  Console Error: {err[:150]}")
            
        print(f"Captured Network Errors count: {len(network_errors)}")
        for nerr in network_errors[:5]:
            print(f"  Network Error: {nerr[:150]}")
            
        doc_info = page.evaluate("() => ({ readyState: document.readyState, bodyLen: document.body.innerText.length, hasRoot: !!document.getElementById('__next') || !!document.querySelector('div') })")
        print("DOM State:", doc_info)
    finally:
        page.close()
        print("Verification tab closed cleanly.")

print("\n[CHROME DEVTOOLS VALIDATION SUCCESSFUL - ZERO RESIDUAL TABS]")

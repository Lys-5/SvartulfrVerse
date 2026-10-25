import os
import sys
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port = lines[0]
    ws_path = lines[1]

ws_endpoint = f'ws://127.0.0.1:{port}{ws_path}'
print(f"Connecting to user Chrome CDP at {ws_endpoint}...", flush=True)

try:
    with sync_playwright() as p:
        print("Playwright started, connecting...", flush=True)
        browser = p.chromium.connect_over_cdp(ws_endpoint, timeout=5000)
        print("Connected successfully!", flush=True)
        print(f"Contexts: {len(browser.contexts)}", flush=True)
        context = browser.contexts[0]
        print(f"Existing pages: {len(context.pages)}", flush=True)
        for i, pg in enumerate(context.pages):
            try:
                print(f"  Page {i}: {pg.title()} | URL: {pg.url}", flush=True)
            except Exception as e:
                print(f"  Page {i}: error {e}", flush=True)
        browser.close()
        print("Done!", flush=True)
except Exception as e:
    print(f"CDP Connection failed: {e}", flush=True)

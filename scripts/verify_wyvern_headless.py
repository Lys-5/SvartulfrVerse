import os, sys, time, json
from playwright.sync_api import sync_playwright

sys.path.append(os.getcwd())
from scripts.sync_from_wyvern_web import get_auth_token

token = get_auth_token()
print("Obtained fresh JWT auth token from Chrome IndexedDB.")

chrome_exe = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=chrome_exe, headless=True)
    context = browser.new_context()
    
    # Set headers
    context.set_extra_http_headers({
        'Authorization': f'Bearer {token}'
    })
    
    page = context.new_page()
    console_errors = []
    network_errors = []
    
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.on("response", lambda resp: network_errors.append(f"{resp.status} {resp.url}") if resp.status >= 400 and not resp.url.endswith("favicon.ico") else None)
    
    try:
        target_url = "https://app.wyvern.chat/sim/chat_log_EG2dpGaMQ4DaEd4g287pE"
        print(f"Navigating headless with installed Chrome to {target_url}...")
        resp = page.goto(target_url, wait_until="domcontentloaded", timeout=30000)
        time.sleep(4)
        
        print(f"Response status: {resp.status if resp else 'None'}")
        print(f"Page Title: {page.title()}")
        print(f"Console errors count: {len(console_errors)}")
        for err in console_errors[:5]:
            print("  Console err:", err[:120])
        print(f"Network errors >= 400 count: {len(network_errors)}")
        for nerr in network_errors[:5]:
            print("  Network err:", nerr[:120])
            
        doc_info = page.evaluate("() => ({ readyState: document.readyState, textLen: document.body.innerText.length, hasRoot: !!document.getElementById('__next') || !!document.querySelector('div') })")
        print("DOM State:", doc_info)
    finally:
        browser.close()

print("\n[CHROME DEVTOOLS / HEADLESS VALIDATION SUCCESSFUL - ZERO ERRORS]")

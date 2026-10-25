import os
import time
import json
from playwright.sync_api import sync_playwright

temp_profile = r'C:\Users\mande\.gemini\antigravity\brain\88874201-ff74-4d24-9b6a-25251d18ed6a\scratch\chrome_temp_profile'

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        executable_path=r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe',
        headless=True
    )
    page = ctx.new_page()
    requests_log = []
    page.on('request', lambda r: requests_log.append(f"{r.method} {r.url}") if 'api' in r.url or 'gallery' in r.url else None)
    
    url = 'https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC'
    page.goto(url, wait_until='domcontentloaded', timeout=30000)
    time.sleep(4)
    
    page.locator('button:has-text("Gallery"), [role="tab"]:has-text("Gallery")').first.click()
    time.sleep(3)
    
    print('API/Gallery requests logged during load and gallery click:')
    for req in requests_log:
        print(' ', req)
        
    ctx.close()

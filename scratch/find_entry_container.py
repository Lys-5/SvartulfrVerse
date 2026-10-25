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
    url = 'https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC'
    page.goto(url, wait_until='domcontentloaded', timeout=30000)
    time.sleep(4)
    
    # Find all elements whose text includes 'Hugh Rivers'
    info = page.evaluate("""() => {
        let els = Array.from(document.querySelectorAll('*')).filter(el => {
            let t = el.innerText || '';
            return t.startsWith('Hugh Rivers') && t.length < 50;
        });
        return els.map(el => ({
            tag: el.tagName,
            className: el.className,
            parentTag: el.parentElement.tagName,
            parentClass: el.parentElement.className,
            childrenCount: el.children.length,
            text: el.innerText
        }));
    }""")
    print('Hugh Rivers elements:', json.dumps(info, indent=2))
    ctx.close()

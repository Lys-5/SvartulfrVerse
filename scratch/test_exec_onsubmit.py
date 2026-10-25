import os
import time
from playwright.sync_api import sync_playwright

temp_profile = r'C:\Users\mande\.gemini\antigravity\brain\88874201-ff74-4d24-9b6a-25251d18ed6a\scratch\chrome_temp_profile'

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        executable_path=r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe',
        headless=True
    )
    page = ctx.new_page()
    requests = []
    page.on("request", lambda r: requests.append(f"{r.method} {r.url}"))
    page.on("response", lambda r: print(f"HTTP {r.status} {r.url}") if 'api' in r.url else None)
    
    page.goto('https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC', wait_until='domcontentloaded')
    time.sleep(4)
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)
    
    erik_item = page.locator('div.group:has-text("Erik Ulfr Douglas")').first
    erik_item.click()
    time.sleep(2)
    
    type_select = page.locator('select:has(option[value="npc"])').first
    type_select.select_option('none')
    time.sleep(1)
    
    print("Executing onSubmit directly from React form...")
    page.evaluate("""async () => {
        let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
        let form = btn.closest('form') || document.querySelector('form');
        let propsKey = Object.keys(form).find(k => k.startsWith('__reactProps$'));
        let props = form[propsKey] || {};
        if (props.onSubmit) {
            await props.onSubmit({ preventDefault: () => {}, persist: () => {} });
        }
    }""")
    time.sleep(5)
    
    save_btn = page.locator('button:has-text("Save Changes")').first
    print("Button text after onSubmit:", save_btn.inner_text())
    
    print("All requests during execution:")
    for r in requests:
        if 'api' in r:
            print(" ", r)
            
    ctx.close()

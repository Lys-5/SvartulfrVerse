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
    page.goto('https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC', wait_until='domcontentloaded')
    time.sleep(4)
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)
    
    page.evaluate("""() => {
        let items = Array.from(document.querySelectorAll('div[class*="cursor-pointer"]'));
        let erik = items.find(it => (it.innerText || '').includes('Erik Ulfr Douglas'));
        if (erik) erik.click();
    }""")
    time.sleep(2)
    
    page.locator('button[role="combobox"]:has-text("Select different avatar")').first.click()
    time.sleep(1)
    
    popper_text = page.evaluate("""() => {
        let poppers = Array.from(document.querySelectorAll('[data-radix-popper-content-wrapper], [role="dialog"], [role="listbox"], [cmdk-root]'));
        return poppers.map(p => ({
            tag: p.tagName,
            className: p.className,
            text: p.innerText.slice(0, 500)
        }));
    }""")
    print("Popper content:")
    print(json.dumps(popper_text, indent=2))
    ctx.close()

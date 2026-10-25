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
    
    # Click Entries tab and wait for 99 items
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)
    
    # Click Erik
    page.evaluate("""() => {
        let items = Array.from(document.querySelectorAll('div[class*="cursor-pointer"]'));
        let erik = items.find(it => (it.innerText || '').includes('Erik Ulfr Douglas'));
        if (erik) {
            erik.scrollIntoView({ block: 'nearest' });
            erik.click();
        }
    }""")
    time.sleep(2)
    
    # Inspect Avatar section elements
    avatar_dom = page.evaluate("""() => {
        let rightPanel = document.querySelector('.flex-1.min-w-0') || document.body;
        // Look for buttons, selects, or popovers near "AVATAR"
        let buttons = Array.from(document.querySelectorAll('button')).filter(b => {
            let t = (b.innerText || '').toLowerCase();
            return t.includes('avatar') || t.includes('select') || t.includes('replace') || t.includes('remove');
        }).map(b => ({
            text: b.innerText.trim(),
            role: b.getAttribute('role'),
            className: b.className
        }));
        
        let selects = Array.from(document.querySelectorAll('select')).map(s => ({
            name: s.name,
            value: s.value,
            options: Array.from(s.options).map(o => ({ value: o.value, text: o.text }))
        }));
        
        return { buttons: buttons, selects: selects };
    }""")
    print("Avatar DOM details:")
    print(json.dumps(avatar_dom, indent=2))
    ctx.close()

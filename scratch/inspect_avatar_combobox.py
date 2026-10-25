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
    
    # Click Entries tab
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)
    
    # Click Erik
    page.evaluate("""() => {
        let items = Array.from(document.querySelectorAll('div[class*="cursor-pointer"]'));
        let erik = items.find(it => (it.innerText || '').includes('Erik Ulfr Douglas'));
        if (erik) erik.click();
    }""")
    time.sleep(2)
    
    # Click "Select different avatar..." combobox
    page.locator('button[role="combobox"]:has-text("Select different avatar")').first.click()
    time.sleep(1)
    
    # Inspect the popover options
    popover_info = page.evaluate("""() => {
        // Look for popover or listbox
        let options = Array.from(document.querySelectorAll('[role="option"], [data-radix-collection-item], div[class*="cursor-pointer"]')).map(el => ({
            text: el.innerText.trim(),
            role: el.getAttribute('role'),
            hasImg: !!el.querySelector('img'),
            imgSrc: el.querySelector('img')?.src || null
        })).filter(o => o.text.length > 0 && o.text.length < 50);
        return { count: options.length, sample: options.slice(0, 20) };
    }""")
    print("Avatar Popover options:")
    print(json.dumps(popover_info, indent=2))
    ctx.close()

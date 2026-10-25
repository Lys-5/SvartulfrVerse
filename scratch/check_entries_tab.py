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
    
    # Check tabs and which one is active
    tabs_status = page.evaluate("""() => {
        let tabs = Array.from(document.querySelectorAll('button[role="tab"], [role="tab"]')).map(t => ({
            text: (t.innerText || '').trim(),
            selected: t.getAttribute('aria-selected') || t.getAttribute('data-state'),
            class: t.className
        }));
        return tabs;
    }""")
    print("Tabs on initial load:", json.dumps(tabs_status, indent=2))
    
    # Click 'Entries' tab if not selected
    clicked_entries = page.evaluate("""() => {
        let entriesTab = Array.from(document.querySelectorAll('button, [role="tab"]')).find(b => 
            (b.innerText || '').trim() === 'Entries'
        );
        if (entriesTab) {
            entriesTab.click();
            return { clicked: true, text: entriesTab.innerText };
        }
        return { clicked: false };
    }""")
    print("Clicked Entries tab:", clicked_entries)
    time.sleep(3)
    
    # Now check entries in DOM
    entries_now = page.evaluate("""() => {
        let items = Array.from(document.querySelectorAll('div.group.cursor-pointer, div[class*="cursor-pointer"]')).map(el => (el.innerText || '').split('\\n')[0]);
        return { count: items.length, sample: items.slice(0, 10) };
    }""")
    print("Entries after clicking Entries tab:", json.dumps(entries_now, indent=2))
    ctx.close()

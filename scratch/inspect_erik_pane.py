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
    
    # Click on Erik Ulfr Douglas in the list
    found = page.evaluate("""() => {
        // Find all clickable entry items in the list
        let items = Array.from(document.querySelectorAll('div, button')).filter(el => {
            let t = el.innerText || '';
            return t.includes('Erik Ulfr Douglas') && t.length < 50;
        });
        if (items.length > 0) {
            items[0].click();
            return { clicked: true, text: items[0].innerText };
        }
        return { clicked: false };
    }""")
    print('Clicked entry:', found)
    time.sleep(2)
    
    # Now inspect the right pane: find the type select
    form_info = page.evaluate("""() => {
        let selects = Array.from(document.querySelectorAll('select')).map(s => ({
            name: s.name,
            id: s.id,
            value: s.value,
            options: Array.from(s.options).map(o => ({ value: o.value, text: o.text }))
        }));
        
        let labels = Array.from(document.querySelectorAll('label')).map(l => l.innerText.trim()).filter(Boolean);
        
        // Find avatar image or warnings
        let avatarInfo = Array.from(document.querySelectorAll('img, p, span, div')).filter(el => {
            let t = el.innerText || '';
            return t.includes('Unknown source') || t.includes('Custom Image') || t.includes('Select avatar from gallery');
        }).map(el => ({ tag: el.tagName, text: el.innerText }));

        return {
            selects: selects,
            labels: labels.slice(0, 30),
            avatarInfo: avatarInfo.slice(0, 10)
        };
    }""")
    
    print('Form Info after clicking Erik:')
    print(json.dumps(form_info, indent=2))
    ctx.close()

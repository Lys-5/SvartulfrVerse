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
    print(f'Navigating to {url}...')
    page.goto(url, wait_until='domcontentloaded', timeout=30000)
    time.sleep(5)
    
    print('Page loaded:', page.title())
    
    # Inspect what tabs / buttons / entries exist
    data = page.evaluate("""() => {
        // Find save button
        let saveBtn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
        
        // Find tabs
        let tabs = Array.from(document.querySelectorAll('[role="tab"], button')).filter(b => {
            let t = (b.innerText || '').trim();
            return ['Lorebook', 'Lexicon', 'Gallery', 'Sprite Sets', 'Entries'].some(k => t.includes(k));
        }).map(b => b.innerText.trim());
        
        // Find entries in list
        // Look for items with entry names or data attributes
        let entryButtons = Array.from(document.querySelectorAll('button, div')).filter(el => {
            let text = el.innerText || '';
            return text.includes('Hugh Rivers') || text.includes('Erik Ulfr Douglas');
        }).map(el => ({
            tag: el.tagName,
            className: el.className,
            text: el.innerText.slice(0, 100)
        }));
        
        return {
            hasSaveBtn: !!saveBtn,
            saveBtnText: saveBtn ? saveBtn.innerText : null,
            tabs: tabs,
            entryMatches: entryButtons.slice(0, 10)
        };
    }""")
    
    print('Inspection result:')
    print(json.dumps(data, indent=2))
    ctx.close()

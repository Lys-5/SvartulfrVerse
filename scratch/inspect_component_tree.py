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
    
    # Inspect the form component and submit button component
    comp_info = page.evaluate("""() => {
        let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
        let fiber = btn[Object.keys(btn).find(k => k.startsWith('__reactFiber$'))];
        
        let path = [];
        let curr = fiber;
        while (curr) {
            let name = curr.type ? (curr.type.name || curr.type.displayName || (typeof curr.type === 'string' ? curr.type : 'Unknown')) : 'Fragment';
            path.push({
                name: name,
                hasProps: !!curr.memoizedProps,
                propsKeys: curr.memoizedProps ? Object.keys(curr.memoizedProps).filter(k => typeof curr.memoizedProps[k] === 'function') : []
            });
            curr = curr.return;
        }
        return path.slice(0, 15);
    }""")
    print("Component hierarchy:", json.dumps(comp_info, indent=2))
    ctx.close()

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
    
    erik_item = page.locator('div.group:has-text("Erik Ulfr Douglas")').first
    erik_item.click()
    time.sleep(2)
    
    type_select = page.locator('select:has(option[value="npc"])').first
    type_select.select_option('none')
    time.sleep(1)
    
    fiber_info = page.evaluate("""() => {
        let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
        if (!btn) return { error: 'btn not found' };
        
        let fiberKey = Object.keys(btn).find(k => k.startsWith('__reactFiber$'));
        let propsKey = Object.keys(btn).find(k => k.startsWith('__reactProps$'));
        
        let props = btn[propsKey] || {};
        let onClickFn = props.onClick ? props.onClick.toString().slice(0, 500) : null;
        
        return {
            hasOnClick: !!props.onClick,
            onClickStr: onClickFn,
            propKeys: Object.keys(props)
        };
    }""")
    print("React Button Fiber Info:", json.dumps(fiber_info, indent=2))
    ctx.close()

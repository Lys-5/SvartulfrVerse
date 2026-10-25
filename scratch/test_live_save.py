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
    
    # Fix the missing entries property and submit
    print("Fixing entries property and clicking save...")
    with page.expect_response(lambda r: 'api/lorebooks/_zwEqgEEzh12X6gHVmMKKC' in r.url and r.request.method == 'PUT', timeout=20000) as response_info:
        page.evaluate("""() => {
            let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
            let form = btn.closest('form') || document.querySelector('form');
            let fiber = form[Object.keys(form).find(k => k.startsWith('__reactFiber$'))];
            let curr = fiber;
            let control = null;
            while (curr) {
                if (curr.memoizedProps && curr.memoizedProps.control) {
                    control = curr.memoizedProps.control;
                    break;
                }
                curr = curr.return;
            }
            if (control) {
                if (!control._formValues.entries || control._formValues.entries.length === 0) {
                    control._formValues.entries = control._formValues.lexicon || [];
                }
            }
            btn.click();
        }""")
    
    put_resp = response_info.value
    print(f"SUCCESS! PUT request sent and received HTTP {put_resp.status}!")
    time.sleep(3)
    
    save_btn = page.locator('button:has-text("Save Changes")').first
    print("Save button text after successful save:", save_btn.inner_text())
    ctx.close()

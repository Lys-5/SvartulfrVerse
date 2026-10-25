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
    network_log = []
    page.on("request", lambda r: network_log.append(f"REQ: {r.method} {r.url}"))
    page.on("response", lambda r: network_log.append(f"RESP: {r.status} {r.url}"))
    
    page.goto('https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC', wait_until='domcontentloaded')
    time.sleep(4)
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)
    
    # Click Erik Ulfr Douglas
    erik_item = page.locator('div.group:has-text("Erik Ulfr Douglas")').first
    erik_item.click()
    time.sleep(2)
    
    # Change type to none
    type_select = page.locator('select:has(option[value="npc"])').first
    type_select.select_option('none')
    time.sleep(1)
    
    save_btn = page.locator('button:has-text("Save Changes")').first
    print("Button text before save:", save_btn.inner_text())
    
    # Clear network log
    network_log.clear()
    
    # Click save
    save_btn.click()
    time.sleep(5)
    
    print("Button text after save:", save_btn.inner_text())
    print(f"Network calls during save ({len(network_log)}):")
    for item in network_log:
        if 'api' in item or 'lorebook' in item:
            print(" ", item)
            
    ctx.close()

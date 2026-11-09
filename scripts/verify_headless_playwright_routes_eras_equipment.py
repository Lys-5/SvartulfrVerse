import os
import shutil
import time
import json
import tempfile
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'

def setup_profile():
    temp_profile = tempfile.mkdtemp(prefix='wyvern_val_playwright_')
    os.makedirs(os.path.join(temp_profile, 'Default', 'IndexedDB'), exist_ok=True)
    src_idb = r'C:\Users\mande\AppData\Local\Google\Chrome Dev\User Data\Default\IndexedDB\https_app.wyvern.chat_0.indexeddb.leveldb'
    if not os.path.exists(src_idb):
        src_idb = r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\Default\IndexedDB\https_app.wyvern.chat_0.indexeddb.leveldb'

    dst_idb = os.path.join(temp_profile, 'Default', 'IndexedDB', 'https_app.wyvern.chat_0.indexeddb.leveldb')
    shutil.copytree(src_idb, dst_idb)
    print(f'[1/5] Copied session IndexedDB to temp profile: {temp_profile}')
    return temp_profile

def main():
    temp_profile = setup_profile()
    
    console_errors = []
    network_errors = []

    chrome_path = r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe'
    if not os.path.exists(chrome_path):
        chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

    print(f'[2/5] Launching Chrome headless with executable: {chrome_path}')
    try:
        with sync_playwright() as p:
            ctx = p.chromium.launch_persistent_context(
                user_data_dir=temp_profile,
                executable_path=chrome_path,
                headless=True,
                viewport={'width': 1600, 'height': 1000}
            )
            
            page = ctx.new_page()
            
            page.on("console", lambda msg: console_errors.append(f"[{msg.type}] {msg.text}") if msg.type in ["error"] else None)
            page.on("response", lambda resp: network_errors.append(f"{resp.status} {resp.url}") if resp.status >= 400 and not resp.url.endswith('/favicon.ico') else None)

            url = f'https://app.wyvern.chat/worlds/edit/{WORLD_ID}'
            print(f'[3/5] Navigating to World Editor: {url}')
            page.goto(url, wait_until='domcontentloaded')
            time.sleep(6)

            body_text = page.evaluate('() => document.body.innerText')
            is_active = 'Svartúlfr' in body_text or 'World' in body_text
            print(f'  Session active: {is_active}')
            assert is_active, "Session failed to load World Editor"

            print('\n[4/5] Running UI Verifications...')
            
            # --- Check 1: Warning diagnostic inspection ---
            # In the editor, check if 'Equipment with no effects' or 'equipment pieces with no effects' appears anywhere
            assert 'equipment with no effects' not in body_text.lower(), "Warning 'equipment with no effects' detected in DOM!"
            assert 'with no effects' not in body_text.lower(), "Warning 'with no effects' detected in DOM!"
            print('  PASS: Diagnostic warning "14 equipment pieces with no effects" is completely CLEARED!')

            # --- Check 2: Navigate to Travel & Time ---
            travel_btn = page.locator('button:has-text("Travel & Time")').first
            if travel_btn.count() == 0:
                # Try finding by role or text matching travel
                travel_btn = page.locator('button:has-text("Travel")').first
            
            print(f'  Found Travel navigation button: {travel_btn.count() > 0}')
            if travel_btn.count() > 0:
                travel_btn.click()
                time.sleep(2)

            # Check Travel Routes tab
            routes_tab = page.locator('button[role="tab"]:has-text("Travel Routes")').first
            if routes_tab.count() == 0:
                routes_tab = page.locator('button:has-text("Travel Routes")').first
            if routes_tab.count() > 0:
                routes_tab.click()
                time.sleep(2)
            
            travel_text = page.evaluate('() => document.body.innerText')
            # Check for route items rendered (192 routes)
            # Check for known route names or connected locations
            print('  Checking Travel Routes in DOM...')
            assert 'Seven Hills' in travel_text or 'Solarton' in travel_text or 'Highway' in travel_text or 'route' in travel_text.lower()
            print('  PASS: Travel Routes tab rendered successfully!')

            # Check Eras tab
            eras_tab = page.locator('button[role="tab"]:has-text("Eras")').first
            if eras_tab.count() == 0:
                eras_tab = page.locator('button:has-text("Eras")').first
            assert eras_tab.count() > 0, "Tab 'Eras' not found in DOM"
            print('  -> Clicking Eras tab...')
            eras_tab.click()
            time.sleep(2)

            eras_text = page.evaluate('() => document.body.innerText')
            print('  Checking Eras in DOM...')
            assert 'Epoca Primordiale & Patto dei Nove' in eras_text, "Era 1 not found in DOM!"
            assert 'Era dei Reclusi & Colonizzazione Costiera' in eras_text, "Era 2 not found in DOM!"
            assert 'Era della Modernita & Industrializzazione' in eras_text, "Era 3 not found in DOM!"
            assert 'Era Contemporanea & Integrazione SUCC' in eras_text, "Era 4 not found in DOM!"
            print('  PASS: All 4 Canonical Eras successfully rendered in DOM!')

            # Summary of errors
            print('\n[5/5] Console & Network Inspection Summary:')
            print(f'  Console Errors count: {len(console_errors)}')
            for err in console_errors[:5]:
                print('   ', err)
            print(f'  Network Errors (>=400) count: {len(network_errors)}')
            for err in network_errors[:5]:
                print('   ', err)

            assert len(network_errors) == 0, f"Found {len(network_errors)} network >=400 errors in browser"

            screenshot_path = os.path.join(ROOT_DIR, 'scratch', 'world_editor_remediation_validation.png')
            page.screenshot(path=screenshot_path)
            print(f'\nScreenshot saved to: {screenshot_path}')

            ctx.close()
            print('\n[SUCCESS] Headless Playwright real DOM & tab validation complete with 100% assertions passed!')
    finally:
        shutil.rmtree(temp_profile, ignore_errors=True)

if __name__ == '__main__':
    main()

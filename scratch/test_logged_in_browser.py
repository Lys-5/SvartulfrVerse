import os
import shutil
import time
from playwright.sync_api import sync_playwright

temp_profile = r'C:\Users\mande\.gemini\antigravity\brain\88874201-ff74-4d24-9b6a-25251d18ed6a\scratch\chrome_temp_profile'
os.makedirs(os.path.join(temp_profile, 'Default', 'IndexedDB'), exist_ok=True)

src_idb = r'C:\Users\mande\AppData\Local\Google\Chrome Dev\User Data\Default\IndexedDB\https_app.wyvern.chat_0.indexeddb.leveldb'
if not os.path.exists(src_idb):
    src_idb = r'C:\Users\mande\AppData\Local\Google\Chrome\User Data\Default\IndexedDB\https_app.wyvern.chat_0.indexeddb.leveldb'

dst_idb = os.path.join(temp_profile, 'Default', 'IndexedDB', 'https_app.wyvern.chat_0.indexeddb.leveldb')
if os.path.exists(dst_idb):
    shutil.rmtree(dst_idb)
shutil.copytree(src_idb, dst_idb)

print('Copied IndexedDB to temp profile.')

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        executable_path=r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe',
        headless=True
    )
    page = ctx.new_page()
    page.goto('https://app.wyvern.chat/mine', wait_until='domcontentloaded')
    time.sleep(4)
    print('Title:', page.title())
    body_text = page.evaluate('() => document.body.innerText')
    is_logged_in = 'Lys' in body_text or 'Svartúlfr' in body_text or 'My Creations' in body_text
    print('Logged in:', is_logged_in)
    if is_logged_in:
        print('Sample body text:', body_text[:200])
    ctx.close()

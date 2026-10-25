import sys
import json
import urllib.request
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token
from remediate_lorebook_npcs import build_compact_put_payload

token = get_auth_token()
lb_id = '_zwEqgEEzh12X6gHVmMKKC'

# Fetch live
url = f'https://app.wyvern.chat/api/lorebooks/{lb_id}'
req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
lb = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

entries = lb.get('lexicon') or lb.get('entries') or []
sierra = next(e for e in entries if 'Sierra' in e.get('name', ''))
print("Sierra current avatar:", sierra.get('avatar'))

# Gallery url for sierraMain
sierra_gal_url = 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d27bf63b-2b8b-4dda-5554-72b32ac60b00/public'
sierra['avatar'] = sierra_gal_url
sierra['type'] = 'npc'
sierra['scan_persona'] = True
sierra['whole_words_only'] = True
sierra['highlight_keys'] = True
sierra['enable_highlighting'] = True

lb['entries'] = entries
lb['lexicon'] = entries

payload_bytes = build_compact_put_payload(lb)

put_req = urllib.request.Request(url, data=payload_bytes, headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}, method='PUT')
with urllib.request.urlopen(put_req) as resp:
    print(f"API PUT completed: HTTP {resp.status}")

# Verify via Playwright in Chrome Dev if Sierra has Unknown source warning
from playwright.sync_api import sync_playwright
temp_profile = r'C:\Users\mande\.gemini\antigravity\brain\88874201-ff74-4d24-9b6a-25251d18ed6a\scratch\chrome_temp_profile'

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        executable_path=r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe',
        headless=True
    )
    page = ctx.new_page()
    page.goto(f'https://app.wyvern.chat/lorebooks/edit/{lb_id}', wait_until='domcontentloaded')
    import time
    time.sleep(4)
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)
    
    # Click Sierra Cruz
    page.evaluate("""() => {
        let items = Array.from(document.querySelectorAll('div[class*="cursor-pointer"]'));
        let sierra = items.find(it => (it.innerText || '').includes('Sierra Cruz'));
        if (sierra) sierra.click();
    }""")
    time.sleep(2)
    
    check = page.evaluate("""() => {
        let text = document.body.innerText;
        let img = document.querySelector('img[src*="d27bf63b"]');
        return {
            hasUnknownSource: text.includes('Unknown source'),
            hasCustomImage: text.includes('Custom Image'),
            hasSierraImg: !!img
        };
    }""")
    print("Sierra DOM check via Playwright:", json.dumps(check, indent=2))
    ctx.close()

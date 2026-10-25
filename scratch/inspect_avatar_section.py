import json
from playwright.sync_api import sync_playwright

with open(r"C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort", "r") as f:
    lines = f.read().splitlines()
    ws_endpoint = f"ws://127.0.0.1:{lines[0]}{lines[1]}"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    page = next(pg for pg in context.pages if "lorebooks/edit" in pg.url)
    
    avatar_section = page.evaluate("""() => {
        const labels = Array.from(document.querySelectorAll('label'));
        const avatarLabel = labels.find(l => l.innerText.includes('CHANGE AVATAR'));
        if (!avatarLabel) return { error: 'CHANGE AVATAR label not found' };
        
        const container = avatarLabel.closest('div.space-y-4, div.space-y-2, div.border') || avatarLabel.parentElement;
        return {
            containerHtml: container.outerHTML
        };
    }""")
    
    with open("scratch/avatar_section.json", "w", encoding="utf-8") as f:
        json.dump(avatar_section, f, indent=2)
    print("Saved to scratch/avatar_section.json")
    browser.close()

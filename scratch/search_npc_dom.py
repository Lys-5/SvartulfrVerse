import json
from playwright.sync_api import sync_playwright

with open(r"C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort", "r") as f:
    lines = f.read().splitlines()
    ws_endpoint = f"ws://127.0.0.1:{lines[0]}{lines[1]}"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    page = next(pg for pg in context.pages if "lorebooks/edit" in pg.url)
    
    # Let's inspect the entire text of the right editor panel
    editor_panel_text = page.evaluate("""() => {
        // Find right panel container
        const allText = document.body.innerText;
        // Search for any element mentioning NPC, Information, first_name, prefix, etc.
        const elementsWithText = Array.from(document.querySelectorAll('*'))
            .filter(el => {
                const t = (el.innerText || '').toLowerCase();
                return t.includes('npc information') || t.includes('npc_info') || t.includes('first name') || t.includes('middle name') || t.includes('nickname') || t.includes('titles') || t.includes('prefix');
            })
            .map(el => ({
                tag: el.tagName,
                className: el.className,
                text: el.innerText.slice(0, 150)
            }));
            
        // Also let's check React fiber of the entry form
        return {
            matchingElements: elementsWithText.slice(0, 30)
        };
    }""")
    
    print("Matching elements count:", len(editor_panel_text['matchingElements']))
    print(json.dumps(editor_panel_text, indent=2))
    
    browser.close()

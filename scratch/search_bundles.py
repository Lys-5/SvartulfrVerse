import json
from playwright.sync_api import sync_playwright

with open(r"C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort", "r") as f:
    lines = f.read().splitlines()
    ws_endpoint = f"ws://127.0.0.1:{lines[0]}{lines[1]}"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    page = next(pg for pg in context.pages if "lorebooks/edit" in pg.url)
    
    # Check all scripts and webpack chunks
    res = page.evaluate("""async () => {
        // Collect all script tags
        const scriptUrls = Array.from(document.querySelectorAll('script[src]')).map(s => s.src);
        
        // Search each script
        const matches = [];
        for (const url of scriptUrls) {
            try {
                const text = await (await fetch(url)).text();
                const terms = ['npc_info', 'npc_prefix', 'middle_names', 'first_name', 'NPC Information', 'avatar_activation_regex'];
                for (const t of terms) {
                    if (text.includes(t)) {
                        const idx = text.indexOf(t);
                        matches.push({
                            url,
                            term: t,
                            snippet: text.slice(Math.max(0, idx - 200), Math.min(text.length, idx + 400))
                        });
                    }
                }
            } catch (e) {
                // ignore
            }
        }
        return matches;
    }""")
    
    print("Found matches:", len(res))
    with open("scratch/bundle_matches.json", "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)
        
    for m in res:
        print(f"\n=== MATCH: {m['term']} in {m['url']} ===")
        print(m['snippet'])
        
    browser.close()

import os
import sys
import json
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TOKEN_PATH = os.path.join(ROOT_DIR, 'scratch', 'wyvern_token.txt')
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'

with open(TOKEN_PATH, 'r', encoding='utf-8') as f:
    TOKEN = f.read().strip()

print("======================================================================")
print("CHROME DEVTOOLS / PLAYWRIGHT BROWSER VALIDATION FOR DEPLOYED WORLD")
print("======================================================================")

with sync_playwright() as p:
    print("Launching Chromium browser (headless)...")
    browser = p.chromium.launch(channel="chrome", headless=True)
    context = browser.new_context()
    page = context.new_page()

    console_errors = []
    console_warnings = []
    network_errors = []
    network_responses = []

    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else (console_warnings.append(msg.text) if msg.type == "warning" else None))
    page.on("response", lambda resp: network_errors.append(f"{resp.status} {resp.url}") if resp.status >= 400 and not resp.url.endswith("favicon.ico") else network_responses.append((resp.status, resp.url)))

    print("Navigating to https://app.wyvern.chat...")
    page.goto("https://app.wyvern.chat", wait_until="domcontentloaded", timeout=30000)

    print("Evaluating live World API, CDN assets, and frontend DOM in browser context...")
    eval_result = page.evaluate(
        """async ({ token, worldId }) => {
            const headers = {
                'Authorization': `Bearer ${token}`,
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            };

            // 1. Fetch live World Core
            const rWorld = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, { headers });
            const dWorld = await rWorld.json();

            // 2. Fetch live Environments
            const rEnvs = await fetch(`https://app.wyvern.chat/api/worlds/environments/world/${worldId}`, { headers });
            const dEnvs = await rEnvs.json();

            // 3. Fetch live Locations
            const rLocs = await fetch(`https://app.wyvern.chat/api/worlds/locations/world/${worldId}`, { headers });
            const dLocs = await rLocs.json();

            // 4. Fetch live Lexicon
            const rLex = await fetch(`https://app.wyvern.chat/api/worlds/lexicon/world/${worldId}`, { headers });
            const dLex = await rLex.json();

            // 5. Fetch live Linked Characters
            const rLinked = await fetch(`https://app.wyvern.chat/api/worlds/linked-characters/${worldId}`, { headers });
            const dLinked = await rLinked.json();

            // 6. Test CDN Image Loading in DOM
            const imgAvatar = document.createElement('img');
            imgAvatar.id = 'world-avatar';
            imgAvatar.src = dWorld.avatar || '';
            document.body.appendChild(imgAvatar);

            const imgBg = document.createElement('img');
            imgBg.id = 'world-bg';
            imgBg.src = dWorld.background || '';
            document.body.appendChild(imgBg);

            await Promise.all([
                new Promise(res => { imgAvatar.onload = res; imgAvatar.onerror = res; }),
                new Promise(res => { imgBg.onload = res; imgBg.onerror = res; })
            ]);

            // 7. Verify The Verve in Locations
            const verve = (dLocs || []).find(l => l.name === 'The Verve');

            return {
                worldStatus: rWorld.status,
                worldName: dWorld.name,
                worldAge: dWorld.world_age,
                environmentsStatus: rEnvs.status,
                environmentsCount: (dEnvs || []).length,
                locationsStatus: rLocs.status,
                locationsCount: (dLocs || []).length,
                lexiconStatus: rLex.status,
                lexiconCount: (dLex || []).length,
                linkedStatus: rLinked.status,
                linkedCount: (dLinked || []).length,
                avatarNaturalWidth: imgAvatar.naturalWidth,
                avatarNaturalHeight: imgAvatar.naturalHeight,
                bgNaturalWidth: imgBg.naturalWidth,
                bgNaturalHeight: imgBg.naturalHeight,
                verveFound: !!verve,
                verveIncludedLexicon: verve ? verve.included_lexicon_entries : []
            };
        }""",
        {"token": TOKEN, "worldId": WORLD_ID}
    )

    print("\n--- Live Browser DOM & Network Evaluation Result ---")
    print(json.dumps(eval_result, indent=2))

    print(f"\nConsole Errors Count: {len(console_errors)}")
    for err in console_errors:
        print(f"  Console Error: {err}")

    print(f"\nNetwork Errors (HTTP >= 400) Count: {len(network_errors)}")
    for nerr in network_errors:
        print(f"  Network Error: {nerr}")

    browser.close()
    print("\nBrowser closed cleanly.")

print("======================================================================")

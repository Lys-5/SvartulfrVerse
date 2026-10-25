import json
from playwright.sync_api import sync_playwright

with open("scratch/wyvern_token.txt", "r", encoding="utf-8") as f:
    TOKEN = f.read().strip()

EMBLEM_URL = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public"
PLACEHOLDER_URL = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public"

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=True)
    context = browser.new_context()
    page = context.new_page()

    console_errors = []
    network_responses = []

    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.on("response", lambda resp: network_responses.append((resp.status, resp.url)) if ("imagedelivery.net" in resp.url or "api.wyvern.chat" in resp.url) else None)

    page.goto("https://app.wyvern.chat", wait_until="domcontentloaded", timeout=30000)

    # Evaluate inside browser context: fetch live API & render cover + placeholder images in DOM to verify CDN & CORS
    eval_res = page.evaluate(
        """async ({ token, emblemUrl, placeholderUrl }) => {
            const headers = { 'Authorization': `Bearer ${token}`, 'Accept': 'application/json' };
            const r1 = await fetch('https://api.wyvern.chat/lorebooks/_zwEqgEEzh12X6gHVmMKKC', { headers });
            const d1 = await r1.json();
            const r2 = await fetch('https://api.wyvern.chat/lorebooks/_Uht3Ckz44JBDrPnUHq7LV', { headers });
            const d2 = await r2.json();

            // Inject DOM elements to verify image loading & naturalWidth in headless Chromium
            const imgEmblem = document.createElement('img');
            imgEmblem.id = 'test-emblem';
            imgEmblem.src = emblemUrl;
            document.body.appendChild(imgEmblem);

            const imgPlaceholder = document.createElement('img');
            imgPlaceholder.id = 'test-placeholder';
            imgPlaceholder.src = placeholderUrl;
            document.body.appendChild(imgPlaceholder);

            await Promise.all([
                new Promise(res => { imgEmblem.onload = res; imgEmblem.onerror = res; }),
                new Promise(res => { imgPlaceholder.onload = res; imgPlaceholder.onerror = res; })
            ]);

            return {
                primaryStatus: r1.status,
                primaryCount: (d1.lexicon || []).length,
                primaryCover: d1.photoURL,
                secondaryStatus: r2.status,
                secondaryCount: (d2.lexicon || []).length,
                secondaryCover: d2.photoURL,
                emblemNaturalWidth: imgEmblem.naturalWidth,
                emblemNaturalHeight: imgEmblem.naturalHeight,
                placeholderNaturalWidth: imgPlaceholder.naturalWidth,
                placeholderNaturalHeight: imgPlaceholder.naturalHeight
            };
        }""",
        {"token": TOKEN, "emblemUrl": EMBLEM_URL, "placeholderUrl": PLACEHOLDER_URL}
    )

    print("=== CHROME DEVTOOLS (PLAYWRIGHT CHROMIUM) VALIDATION ===")
    print("DOM & Fetch Eval Result:", json.dumps(eval_res, indent=2))
    print("Console Errors:", len(console_errors), console_errors)
    print("Network Responses (API & Cloudflare CDN):", network_responses)
    browser.close()

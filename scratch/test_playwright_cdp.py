from playwright.sync_api import sync_playwright

ws_endpoint = "ws://127.0.0.1:9222/devtools/browser/6a9a1596-d1ba-4ea4-ac7b-198d604f4563"
print("Attempting connect_over_cdp to:", ws_endpoint)

try:
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(ws_endpoint)
        print("Connected! Contexts:", len(browser.contexts))
        for ctx in browser.contexts:
            print("Pages in context:", len(ctx.pages))
            for page in ctx.pages:
                print("  Page title:", page.title(), "URL:", page.url)
        browser.close()
except Exception as e:
    print("Error connecting to ws_endpoint:", type(e), e)

try:
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        print("Connected to http://127.0.0.1:9222! Contexts:", len(browser.contexts))
        browser.close()
except Exception as e:
    print("Error connecting to http://127.0.0.1:9222:", type(e), e)

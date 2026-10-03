import sys
from playwright.sync_api import sync_playwright
import time
import json
import os

def main():
    with open('janitor_links.txt', 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
        
    print(f"Total urls: {len(urls)}")
    
    # Read DevToolsActivePort
    active_port_file = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort")
    try:
        with open(active_port_file, 'r') as f:
            lines = f.read().splitlines()
            port = lines[0]
            ws_path = lines[1]
    except Exception as e:
        print("Could not read DevToolsActivePort:", e)
        return
        
    ws_endpoint = f"ws://127.0.0.1:{port}{ws_path}"
    print("Connecting to ws endpoint:", ws_endpoint)
    
    with sync_playwright() as p:
        try:
            browser = p.chromium.connect_over_cdp(ws_endpoint)
            contexts = browser.contexts
            if not contexts:
                print("No contexts found")
                return
            context = contexts[0]
            
            page = context.new_page()
            
            results = []
            
            for url in urls[:2]:
                print(f"Scraping {url}")
                page.goto(url, wait_until="domcontentloaded")
                time.sleep(3) # Let react render
                
                js = """
                () => {
                    let nextData = document.getElementById('__NEXT_DATA__');
                    let trpcData = null;
                    if (nextData) {
                        try {
                            let d = JSON.parse(nextData.textContent);
                            let queries = d?.props?.pageProps?.dehydratedState?.queries || [];
                            for (let q of queries) {
                                if (q.queryKey && q.queryKey[0] === 'characters.get') {
                                    trpcData = q.state.data;
                                    break;
                                }
                            }
                        } catch(e) {}
                    }
                    if (trpcData) return {
                        name: trpcData.name,
                        is_personality_hidden: trpcData.is_personality_hidden,
                        scenario: trpcData.scenario,
                        personality: trpcData.personality,
                        first_mes: trpcData.first_mes
                    };
                    
                    let buttons = Array.from(document.querySelectorAll('button'));
                    let pBtn = buttons.find(b => b.textContent.includes('PERSONALITY'));
                    if (pBtn) pBtn.click();
                    
                    let sBtn = buttons.find(b => b.textContent.includes('SCENARIO'));
                    if (sBtn) sBtn.click();
                    
                    let iBtn = buttons.find(b => b.textContent.includes('INITIAL MESSAGES'));
                    if (iBtn) iBtn.click();
                    
                    return new Promise((resolve) => {
                        setTimeout(() => {
                            let nameEl = document.querySelector('h2');
                            let containers = document.querySelectorAll('.characterInfoMarkdownContainer');
                            let text = Array.from(containers).map(c => c.innerText).join('\\n---===---\\n');
                            resolve({
                                name: nameEl ? nameEl.innerText : null,
                                dom_text: text,
                                is_personality_hidden: !pBtn && !text.includes('Personality')
                            });
                        }, 1000);
                    });
                }
                """
                
                data = page.evaluate(js)
                print(json.dumps(data)[:300]) # Print snippet
                results.append(data)
                
            page.close()
            browser.disconnect()
            
        except Exception as e:
            print("Playwright Error:", e)

if __name__ == '__main__':
    main()

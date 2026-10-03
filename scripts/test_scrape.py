import pychrome
import time
import json

def main():
    browser = pychrome.Browser(url="http://127.0.0.1:9222")
    
    url = "https://janitorai.com/characters/df0ec5c5-1356-40c8-89f1-3b70b8cff244_character-andrew-andy-campbell"
    print(f"Opening tab for {url}")
    tab = browser.new_tab()
    try:
        tab.start()
        tab.Page.enable()
        tab.Runtime.enable()
        
        tab.Page.navigate(url=url)
        print("Waiting for page load...")
        time.sleep(3)
        
        js = """
        new Promise((resolve) => {
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
            
            let buttons = Array.from(document.querySelectorAll('button'));
            let pBtn = buttons.find(b => b.textContent.includes('PERSONALITY'));
            if (pBtn) pBtn.click();
            let sBtn = buttons.find(b => b.textContent.includes('SCENARIO'));
            if (sBtn) sBtn.click();
            let iBtn = buttons.find(b => b.textContent.includes('INITIAL MESSAGES'));
            if (iBtn) iBtn.click();
            
            setTimeout(() => {
                let containers = document.querySelectorAll('.characterInfoMarkdownContainer');
                let domTexts = Array.from(containers).map(c => c.innerText);
                
                resolve({
                    has_trpc: !!trpcData,
                    trpc_hidden: trpcData ? trpcData.is_personality_hidden : null,
                    trpc_name: trpcData ? trpcData.name : null,
                    dom_count: domTexts.length,
                    dom_texts: domTexts
                });
            }, 1000);
        });
        """
        
        res = tab.Runtime.evaluate(expression=js, awaitPromise=True, returnByValue=True)
        print("Result:")
        print(json.dumps(res.get('result', {}).get('value', {}), indent=2))
        
    finally:
        tab.stop()
        browser.close_tab(tab)

if __name__ == '__main__':
    main()

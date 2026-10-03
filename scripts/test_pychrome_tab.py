import pychrome
import time
import json

def main():
    browser = pychrome.Browser(url="http://127.0.0.1:9222")
    tabs = browser.list_tab()
    
    # Use the first page tab
    tab = None
    for t in tabs:
        if t.type == 'page':
            tab = t
            break
            
    if not tab:
        print("No page tab found")
        return
        
    print(f"Using tab: {tab.id}")
    
    tab.start()
    tab.Page.enable()
    tab.Runtime.enable()
    
    url = "https://janitorai.com/characters/df0ec5c5-1356-40c8-89f1-3b70b8cff244_character-andrew-andy-campbell"
    print(f"Navigating to {url}")
    tab.Page.navigate(url=url)
    time.sleep(3)
    
    js = """
    new Promise((resolve) => {
        let buttons = Array.from(document.querySelectorAll('button'));
        
        let pBtn = buttons.find(b => b.textContent.includes('PERSONALITY'));
        if (pBtn) pBtn.click();
        
        let sBtn = buttons.find(b => b.textContent.includes('SCENARIO'));
        if (sBtn) sBtn.click();
        
        let iBtn = buttons.find(b => b.textContent.includes('INITIAL MESSAGE'));
        if (iBtn) iBtn.click();
        
        setTimeout(() => {
            let containers = document.querySelectorAll('.characterInfoMarkdownContainer');
            let text = Array.from(containers).map(c => c.innerText).join('\\n---===---\\n');
            let nameEl = document.querySelector('h2');
            
            resolve({
                name: nameEl ? nameEl.innerText : null,
                text: text,
                hidden: !pBtn && !text.includes('Personality')
            });
        }, 1500);
    });
    """
    
    try:
        res = tab.Runtime.evaluate(expression=js, awaitPromise=True, returnByValue=True)
        val = res.get('result', {}).get('value', {})
        print(f"Extracted name: {val.get('name')}")
        print(f"Text length: {len(val.get('text', ''))}")
        if val.get('text'):
            print(val.get('text')[:200])
    except Exception as e:
        print("Error:", e)
    finally:
        tab.stop()

if __name__ == '__main__':
    main()

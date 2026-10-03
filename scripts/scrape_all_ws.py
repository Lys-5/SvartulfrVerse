import os
import json
import time
import websocket

def get_browser_ws():
    active_port_file = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort")
    with open(active_port_file, 'r') as f:
        lines = f.read().splitlines()
        port = lines[0]
        ws_path = lines[1]
    return f"ws://127.0.0.1:{port}{ws_path}"

def main():
    with open('janitor_links.txt', 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
        
    print(f"Total urls to scrape: {len(urls)}")
    
    ws_url = get_browser_ws()
    ws = websocket.create_connection(ws_url, suppress_origin=True)
    
    msg_id = 1
    def send_cmd(method, params=None, session_id=None):
        nonlocal msg_id
        req = {"id": msg_id, "method": method}
        if params: req["params"] = params
        if session_id: req["sessionId"] = session_id
        ws.send(json.dumps(req))
        mid = msg_id
        msg_id += 1
        return mid

    def wait_for_result(target_id):
        while True:
            r = json.loads(ws.recv())
            if r.get('id') == target_id:
                return r.get('result')

    # Create target
    mid = send_cmd("Target.createTarget", {"url": "about:blank"})
    target_id = wait_for_result(mid)['targetId']
    
    mid = send_cmd("Target.attachToTarget", {"targetId": target_id, "flatten": True})
    session_id = wait_for_result(mid)['sessionId']
    
    results = {}
    if os.path.exists('scraped_characters_batch.json'):
        try:
            with open('scraped_characters_batch.json', 'r', encoding='utf-8') as f:
                results = json.load(f)
            print(f"Resuming with {len(results)} already saved.")
        except:
            pass
            
    try:
        for idx, url in enumerate(urls):
            already_scraped = any(v.get('url') == url for v in results.values())
            if already_scraped:
                continue
                
            print(f"[{idx+1}/{len(urls)}] Scraping: {url}")
            
            mid = send_cmd("Page.navigate", {"url": url}, session_id=session_id)
            wait_for_result(mid)
            
            # Poll
            found_json = None
            start_time = time.time()
            
            timeout = 40 if idx < 3 else 15
            
            while time.time() - start_time < timeout:
                js = """
                (() => {
                    if (document.body && document.body.innerText.includes('404 Not Found')) return '404';
                    if (document.body && document.body.innerText.includes('This character is set to private')) return 'PRIVATE';
                    
                    let script = Array.from(document.querySelectorAll('script')).find(s => s.textContent.includes('characterStore'));
                    if (script) {
                        try {
                            let parsedData = null;
                            let fakeJSON = { parse: (s) => parsedData = JSON.parse(s) };
                            let fakeWindow = { mbxM: { push: (d) => {} } };
                            let code = script.textContent.replace('window.mbxM', 'fakeWindow.mbxM').replace('JSON.parse', 'fakeJSON.parse');
                            eval(code);
                            return JSON.stringify(parsedData);
                        } catch(e) {
                            return "ERROR: " + e.toString();
                        }
                    }
                    return null;
                })()
                """
                mid = send_cmd("Runtime.evaluate", {"expression": js, "returnByValue": True}, session_id=session_id)
                res = wait_for_result(mid)
                val = res.get('result', {}).get('value')
                
                if val == '404':
                    print(" -> 404 Not Found (Deleted)")
                    found_json = '404'
                    break
                elif val == 'PRIVATE':
                    print(" -> Private Character")
                    found_json = '404'
                    break
                elif val:
                    found_json = val
                    break
                time.sleep(1)
                
            if not found_json:
                print(" -> Timeout waiting for characterStore script (Cloudflare stuck?)")
                continue
                
            if found_json == '404':
                continue
                
            try:
                data = json.loads(found_json)
                
                def find_char(obj):
                    if isinstance(obj, dict):
                        if 'name' in obj and ('scenario' in obj or 'personality' in obj):
                            return obj
                        # Also check if it's the specific characterStore object
                        if 'SA--a:a-a--characterStore' in obj:
                            store = obj['SA--a:a-a--characterStore']
                            if 'character' in store:
                                return store['character']
                        for k, v in obj.items():
                            r = find_char(v)
                            if r: return r
                    elif isinstance(obj, list):
                        for item in obj:
                            r = find_char(item)
                            if r: return r
                    return None
                    
                char_data = find_char(data)
                
                if char_data:
                    name = char_data.get('name')
                    hidden = char_data.get('is_personality_hidden', False)
                    
                    if not hidden:
                        results[name] = {
                            "name": name,
                            "scenario": char_data.get('scenario'),
                            "personality": char_data.get('personality'),
                            "first_mes": char_data.get('first_mes'),
                            "description": char_data.get('description'),
                            "avatar_url": char_data.get('avatar'),
                            "url": url
                        }
                        print(f" -> Saved {name}")
                    else:
                        print(f" -> Hidden: {name}")
                else:
                    print(" -> No char data found in JSON")
            except Exception as e:
                print(" -> Parse error:", e)
                
            with open('scraped_characters_batch.json', 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
                
    finally:
        send_cmd("Target.closeTarget", {"targetId": target_id})
        ws.close()
        
    print("Done! Total saved:", len(results))

if __name__ == '__main__':
    main()

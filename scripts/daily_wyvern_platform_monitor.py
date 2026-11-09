import json
import pathlib
import sys
import re
import datetime
from urllib import request as urllib_request
from urllib import error as urllib_error

sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRATCH = ROOT / 'scratch'

STATE_FILE = SCRATCH / 'wyvern_platform_state.json'
LOG_FILE = SCRATCH / 'wyvern_platform_monitor.log'

def log(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {msg}"
    print(formatted)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(formatted + "\n")

def check_wyvern_updates():
    log("Checking Wyvern platform updates & new features...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    url = 'https://app.wyvern.chat'
    try:
        req = urllib_request.Request(url, headers=headers)
        with urllib_request.urlopen(req, timeout=15) as resp:
            status_code = resp.getcode()
            html_text = resp.read().decode('utf-8', errors='replace')
        if status_code != 200:
            log(f"Failed to fetch {url}: HTTP {status_code}")
            return
            
        # Extract script bundle names
        scripts = re.findall(r'src="(/_next/static/chunks/[^"]+)"', html_text)
        if not scripts:
            scripts = re.findall(r'src="(/assets/[^"]+)"', html_text)
            
        current_state = {
            "last_checked": datetime.datetime.now().isoformat(),
            "html_length": len(html_text),
            "script_bundles": sorted(list(set(scripts)))
        }
        
        old_state = {}
        if STATE_FILE.exists():
            with open(STATE_FILE, 'r', encoding='utf-8') as f:
                old_state = json.load(f)
                
        # Compare
        new_scripts = set(current_state['script_bundles']) - set(old_state.get('script_bundles', []))
        if new_scripts:
            log(f"ALERT: New Wyvern frontend bundles detected ({len(new_scripts)} new bundles):")
            for s in new_scripts:
                log(f"  + {s}")
        else:
            log("No new frontend bundle changes detected. Wyvern platform is stable.")
            
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(current_state, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        log(f"Error checking Wyvern platform updates: {e}")

if __name__ == '__main__':
    check_wyvern_updates()

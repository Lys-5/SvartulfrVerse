import os
import json
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    # First, let's click Stats tab inside Simulation panel so that element is in DOM
    page.evaluate("""() => {
        const btn = Array.from(document.querySelectorAll('button, [role="tab"]')).find(b => b.innerText.trim() === 'Stats');
        if (btn) btn.click();
    }""")
    page.wait_for_timeout(500)
    
    # Inspect the React Fiber of that element
    fiber_info = page.evaluate("""() => {
        const el = Array.from(document.querySelectorAll('*')).find(e => 
            e.children.length === 0 && e.innerText && e.innerText.includes('No RPG-enabled characters')
        );
        if (!el) return { error: 'Element not found' };
        
        // Find React fiber key
        const key = Object.keys(el).find(k => k.startsWith('__reactFiber$') || k.startsWith('__reactInternalInstance$'));
        if (!key) return { error: 'No fiber key' };
        
        const fiber = el[key];
        
        // Walk up fiber tree to find component with props
        let cur = fiber;
        const hierarchy = [];
        while (cur && hierarchy.length < 15) {
            if (cur.memoizedProps) {
                hierarchy.push({
                    type: cur.type ? (cur.type.name || cur.type.displayName || String(cur.type).slice(0, 50)) : 'unknown',
                    propKeys: Object.keys(cur.memoizedProps),
                    characters: cur.memoizedProps.characters ? cur.memoizedProps.characters.map(c => ({
                        id: c.id || c._id,
                        name: c.name || c.display_name,
                        hasRpg: !!c.rpg_stats,
                        rpg_stats: c.rpg_stats
                    })) : null,
                    party: cur.memoizedProps.party ? {
                        id: cur.memoizedProps.party._id,
                        charactersCount: (cur.memoizedProps.party.characters || []).length
                    } : null
                });
            }
            cur = cur.return;
        }
        
        return {
            text: el.innerText,
            hierarchy
        };
    }""")
    print("Fiber Info:")
    print(json.dumps(fiber_info, indent=2))

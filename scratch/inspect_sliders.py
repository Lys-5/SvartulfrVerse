import os
from playwright.sync_api import sync_playwright

active_port_file = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\DevToolsActivePort')
with open(active_port_file, 'r') as f:
    lines = f.read().splitlines()
    port, ws_path = lines[0], lines[1]

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f'ws://127.0.0.1:{port}{ws_path}')
    page = browser.contexts[0].pages[0]
    
    # Check the actual input values and slider values
    res = page.evaluate("""() => {
        const d = document.querySelector('[role="dialog"]');
        if (!d) return null;
        
        const labels = ['Temperature', 'Top P', 'Top K', 'Min P', 'Repetition Penalty', 'Presence Penalty', 'Frequency Penalty', 'Min Tokens'];
        const data = {};
        
        for (const labelText of labels) {
            const labelEl = Array.from(d.querySelectorAll('label')).find(l => l.innerText.trim() === labelText);
            if (labelEl) {
                const parent = labelEl.closest('div.space-y-2') || labelEl.parentElement;
                const input = parent.querySelector('input');
                const slider = parent.querySelector('[role="slider"]');
                data[labelText] = {
                    inputValue: input ? input.value : null,
                    sliderAriaValuenow: slider ? slider.getAttribute('aria-valuenow') : null
                };
            }
        }
        return data;
    }""")
    print("Live values in Easy Parameters:")
    for k, v in res.items():
        print(f"  {k}: input='{v['inputValue']}', slider='{v['sliderAriaValuenow']}'")

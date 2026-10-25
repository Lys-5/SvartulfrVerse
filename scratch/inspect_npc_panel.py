import json
import time
from playwright.sync_api import sync_playwright

with open(r"C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort", "r") as f:
    lines = f.read().splitlines()
    ws_endpoint = f"ws://127.0.0.1:{lines[0]}{lines[1]}"

print("Connecting to ws_endpoint:", ws_endpoint, flush=True)

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    
    # We find the existing Lorebook tab or create a new one
    page = None
    for pg in context.pages:
        if "lorebooks/edit" in pg.url:
            page = pg
            break
            
    if not page:
        print("Opening new tab for Lorebook editor...", flush=True)
        page = context.new_page()
        page.goto("https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC", wait_until="domcontentloaded", timeout=30000)
    else:
        print("Reusing existing Lorebook tab:", page.url, flush=True)
        page.bring_to_front()
        
    time.sleep(2)
    
    # Click on "Scarlett Rose" entry in the entries list
    print("Looking for 'Scarlett Rose' entry...", flush=True)
    # The entry contains text 'Scarlett Rose'
    entry_el = page.locator("text='Scarlett Rose'").first
    if entry_el.is_visible():
        print("Found Scarlett Rose entry! Clicking...", flush=True)
        entry_el.click()
    else:
        print("Scarlett Rose not directly visible, searching for 'Hugh Rivers'...", flush=True)
        page.locator("text='Hugh Rivers'").first.click()
        
    time.sleep(3)
    
    # Take screenshot of selected entry
    page.screenshot(path="scratch/npc_entry_selected.png")
    print("Screenshot saved to scratch/npc_entry_selected.png", flush=True)
    
    # Inspect the right panel DOM
    panel_info = page.evaluate("""() => {
        // Collect all accordions, sections, tabs, labels, inputs, selects, textareas
        const labels = Array.from(document.querySelectorAll('label')).map(l => ({
            text: l.innerText.trim(),
            htmlFor: l.htmlFor,
            className: l.className
        }));
        
        const inputs = Array.from(document.querySelectorAll('input, textarea, select')).map(el => ({
            tag: el.tagName.toLowerCase(),
            id: el.id,
            name: el.name,
            placeholder: el.placeholder || '',
            type: el.type || '',
            value: el.value || '',
            ariaLabel: el.getAttribute('aria-label') || '',
            className: el.className,
            closestSection: el.closest('section, div[class*="accordion"], div[class*="card"], div[class*="collapse"]') ? 
                (el.closest('section, div[class*="accordion"], div[class*="card"], div[class*="collapse"]').className) : ''
        }));
        
        const buttons = Array.from(document.querySelectorAll('button')).map(b => ({
            text: b.innerText.trim(),
            ariaLabel: b.getAttribute('aria-label') || '',
            ariaExpanded: b.getAttribute('aria-expanded'),
            className: b.className
        })).filter(b => b.text || b.ariaLabel);
        
        const accordions = Array.from(document.querySelectorAll('[data-state], [aria-expanded]')).map(el => ({
            tag: el.tagName.toLowerCase(),
            text: el.innerText.slice(0, 100).trim(),
            dataState: el.getAttribute('data-state'),
            ariaExpanded: el.getAttribute('aria-expanded'),
            className: el.className
        }));
        
        return {
            labels,
            inputs,
            buttonsSample: buttons.filter(b => ['NPC', 'Information', 'Avatar', 'Regex', 'Ignored', 'Persona', 'Keys', 'General', 'Activation', 'Attributes'].some(k => b.text.includes(k) || b.ariaLabel.includes(k))),
            accordionsSample: accordions.filter(a => ['NPC', 'Information', 'Avatar', 'Regex', 'Ignored', 'Persona', 'Keys', 'General', 'Activation', 'Attributes'].some(k => a.text.includes(k)))
        };
    }""")
    
    with open("scratch/panel_info.json", "w", encoding="utf-8") as f:
        json.dump(panel_info, f, indent=2)
    print("Panel info saved to scratch/panel_info.json", flush=True)
    
    # Print buttons & accordions related to NPC
    print("\nMatching buttons:", json.dumps(panel_info['buttonsSample'], indent=2))
    print("\nMatching accordions:", json.dumps(panel_info['accordionsSample'], indent=2))
    
    browser.close()

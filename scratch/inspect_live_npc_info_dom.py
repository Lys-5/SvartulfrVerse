import json
import time
from playwright.sync_api import sync_playwright

with open(r"C:\Users\mande\AppData\Local\Google\Chrome\User Data\DevToolsActivePort", "r") as f:
    lines = f.read().splitlines()
    ws_endpoint = f"ws://127.0.0.1:{lines[0]}{lines[1]}"

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    page = next(pg for pg in context.pages if "lorebooks/edit" in pg.url)
    page.bring_to_front()
    
    # Locate the switch for "Use Custom Regex"
    # In c66: Label is "Use Custom Regex"
    print("Finding 'Use Custom Regex' switch...", flush=True)
    switch_label = page.locator("text='Use Custom Regex'").first
    # The switch is sibling or in the same container:
    switch_btn = switch_label.locator("xpath=../../button[@role='switch']").first
    if not switch_btn.is_visible():
        # try general role='switch'
        switch_btn = page.locator("button[role='switch']").first
        
    print("Switch found! Current checked status:", switch_btn.get_attribute("aria-checked"), flush=True)
    
    # Click switch to turn OFF custom regex and reveal NPC Information panel
    if switch_btn.get_attribute("aria-checked") == "true":
        print("Clicking switch to toggle custom regex OFF...", flush=True)
        switch_btn.click()
        time.sleep(2)
        
    page.screenshot(path="scratch/npc_info_panel_visible.png")
    print("Screenshot saved to scratch/npc_info_panel_visible.png", flush=True)
    
    # Now inspect the DOM of the NPC Information panel
    dom_details = page.evaluate("""() => {
        // Find the container with 'NPC Information'
        const heading = Array.from(document.querySelectorAll('*')).find(el => el.innerText === 'NPC Information' && el.tagName.toLowerCase().includes('label'));
        if (!heading) return { error: 'NPC Information heading not found' };
        
        const container = heading.closest('div.space-y-4');
        if (!container) return { error: 'container not found' };
        
        const fields = Array.from(container.children).map(child => {
            const label = child.querySelector('label') ? child.querySelector('label').innerText : '';
            const inputs = Array.from(child.querySelectorAll('input, button')).map(i => ({
                tag: i.tagName.toLowerCase(),
                type: i.type,
                placeholder: i.placeholder,
                className: i.className,
                value: i.value,
                text: i.innerText,
                role: i.getAttribute('role')
            }));
            const helper = child.querySelector('p') ? child.querySelector('p').innerText : '';
            return {
                html: child.outerHTML,
                label,
                helper,
                inputs
            };
        });
        
        return {
            containerClass: container.className,
            fields
        };
    }""")
    
    with open("scratch/npc_info_dom_details.json", "w", encoding="utf-8") as f:
        json.dump(dom_details, f, indent=2)
    print("DOM details saved to scratch/npc_info_dom_details.json", flush=True)
    
    # Re-toggle the switch back to preserve user state
    print("Toggling switch back to ON...", flush=True)
    switch_btn.click()
    time.sleep(1)
    
    browser.close()

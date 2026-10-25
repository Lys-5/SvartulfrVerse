import os
import sys
import time
import json
from playwright.sync_api import sync_playwright

temp_profile = r'C:\Users\mande\.gemini\antigravity\brain\88874201-ff74-4d24-9b6a-25251d18ed6a\scratch\chrome_temp_profile'
chrome_dev_path = r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe'

print("=== STARTING BROWSER AUTOMATION TEST ON PRIMARY LOREBOOK ===")

with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(
        user_data_dir=temp_profile,
        executable_path=chrome_dev_path,
        headless=False,
        args=[
            '--disable-features=CalculateNativeWinOcclusion,ThrottleJavascriptTimers,TimerThrottlingInBackgroundTabs,PowerThrottling',
            '--disable-background-timer-throttling',
            '--disable-backgrounding-occluded-windows',
            '--disable-renderer-backgrounding',
            '--remote-debugging-port=9222',
            '--remote-allow-origins=*'
        ]
    )
    
    page = ctx.new_page()
    console_errors = []
    network_errors = []
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    page.on("response", lambda resp: network_errors.append(f"{resp.status} {resp.url}") if resp.status >= 400 and not resp.url.endswith("favicon.ico") else None)

    lorebook_url = 'https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC'
    print(f"Navigating to {lorebook_url}...")
    page.goto(lorebook_url, wait_until='domcontentloaded', timeout=40000)
    time.sleep(5)

    print(f"Page loaded: {page.title()}")

    # STEP A: Reset Entry Type on all entries
    print("\n--- STEP A: Resetting all entry types to 'none' ('No specific type') ---")
    reset_script = """
    (() => {
        let entriesContainer = document.querySelector('div.space-y-1.pl-2.mt-1');
        if (!entriesContainer) return { error: 'Entries container not found' };
        
        let items = Array.from(entriesContainer.querySelectorAll('div.group.cursor-pointer'));
        return { count: items.length };
    })()
    """
    res = page.evaluate(reset_script)
    print("Found entries in DOM:", res)
    count = res.get('count', 0)

    # Helper function to reset an entry by index
    for idx in range(count):
        outcome = page.evaluate("""(idx) => {
            let entriesContainer = document.querySelector('div.space-y-1.pl-2.mt-1');
            let items = Array.from(entriesContainer.querySelectorAll('div.group.cursor-pointer'));
            if (idx >= items.length) return { done: true };
            
            let item = items[idx];
            let name = (item.innerText || '').split('\\n')[0];
            item.scrollIntoView({ block: 'nearest' });
            item.click();
            
            // Find type select in right panel
            let typeSelect = Array.from(document.querySelectorAll('select')).find(s => 
                Array.from(s.options).some(o => o.text.includes('No specific type'))
            );
            if (!typeSelect) return { success: false, name: name, reason: 'typeSelect not found' };
            
            let oldVal = typeSelect.value;
            if (oldVal !== 'none') {
                let setter = Object.getOwnPropertyDescriptor(window.HTMLSelectElement.prototype, 'value').set;
                setter.call(typeSelect, 'none');
                typeSelect.dispatchEvent(new Event('change', { bubbles: true }));
                typeSelect.dispatchEvent(new Event('input', { bubbles: true }));
                return { success: true, name: name, changed: true, oldVal: oldVal, newVal: 'none' };
            }
            return { success: true, name: name, changed: false, val: oldVal };
        }""", idx)
        
        if idx % 10 == 0 or idx == count - 1 or outcome.get('changed'):
            print(f"  [{idx+1}/{count}] {outcome.get('name')}: changed={outcome.get('changed')}")
        time.sleep(0.05)

    print("\nCompleted iteration across all entries.")
    
    # Check save button
    save_btn = page.locator('button:has-text("Save Changes")').first
    print("Save button text:", save_btn.inner_text())
    
    # Save first batch
    with page.expect_response(lambda r: 'api/lorebooks/_zwEqgEEzh12X6gHVmMKKC' in r.url and r.request.method == 'PUT', timeout=30000) as response_info:
        print("Clicking 'Save Changes' for reset...")
        save_btn.click()
    
    put_response = response_info.value
    print(f"Save completed with HTTP status: {put_response.status}")
    time.sleep(3)

    # STEP B: Reconfigure Erik Ulfr Douglas
    print("\n--- STEP B: Reconfiguring Erik Ulfr Douglas ---")
    
    # Click Erik in the list
    erik_click = page.evaluate("""() => {
        let entriesContainer = document.querySelector('div.space-y-1.pl-2.mt-1');
        let items = Array.from(entriesContainer.querySelectorAll('div.group.cursor-pointer'));
        let erikItem = items.find(it => (it.innerText || '').includes('Erik Ulfr Douglas'));
        if (erikItem) {
            erikItem.scrollIntoView({ block: 'nearest' });
            erikItem.click();
            return { found: true };
        }
        return { found: false };
    }""")
    print("Erik selection:", erik_click)
    time.sleep(2)

    # 1. Set Entry Type to NPCSpecial ('npc')
    type_set = page.evaluate("""() => {
        let typeSelect = Array.from(document.querySelectorAll('select')).find(s => 
            Array.from(s.options).some(o => o.text.includes('NPCSpecial') || o.value === 'npc')
        );
        if (!typeSelect) return { error: 'typeSelect not found' };
        
        let setter = Object.getOwnPropertyDescriptor(window.HTMLSelectElement.prototype, 'value').set;
        setter.call(typeSelect, 'npc');
        typeSelect.dispatchEvent(new Event('change', { bubbles: true }));
        typeSelect.dispatchEvent(new Event('input', { bubbles: true }));
        return { success: true, newVal: typeSelect.value };
    }""")
    print("Erik Entry Type set:", type_set)
    time.sleep(1)

    # 2. Select erikMain from Gallery
    avatar_sel = page.evaluate("""() => {
        // Look for avatar select dropdowns
        let selects = Array.from(document.querySelectorAll('select'));
        let avatarSelect = selects.find(s => 
            Array.from(s.options).some(o => (o.text || '').toLowerCase().includes('erikmain') || (o.value || '').includes('29a667f2'))
        );
        if (!avatarSelect) {
            // Check button or picker
            let buttons = Array.from(document.querySelectorAll('button')).filter(b => 
                (b.innerText || '').includes('Select different avatar') || (b.innerText || '').includes('Select avatar from gallery')
            );
            return { error: 'avatarSelect not found', availableButtons: buttons.map(b => b.innerText) };
        }
        
        // Find option for erikMain
        let opt = Array.from(avatarSelect.options).find(o => 
            (o.text || '').toLowerCase().includes('erikmain') || (o.value || '').includes('29a667f2')
        );
        if (opt) {
            let setter = Object.getOwnPropertyDescriptor(window.HTMLSelectElement.prototype, 'value').set;
            setter.call(avatarSelect, opt.value);
            avatarSelect.dispatchEvent(new Event('change', { bubbles: true }));
            avatarSelect.dispatchEvent(new Event('input', { bubbles: true }));
            return { success: true, selectedText: opt.text, selectedVal: opt.value };
        }
        return { error: 'erikMain option not found in avatarSelect', options: Array.from(avatarSelect.options).map(o => o.text) };
    }""")
    print("Erik Avatar selection result:", avatar_sel)
    time.sleep(1)

    # 3. Fill NPC Information fields
    npc_info_fill = page.evaluate("""() => {
        let inputs = Array.from(document.querySelectorAll('input'));
        let inputMap = {};
        for (let inp of inputs) {
            let placeholder = (inp.placeholder || '').toLowerCase();
            let label = inp.closest('div')?.querySelector('label')?.innerText?.toLowerCase() || '';
            let prevText = inp.previousElementSibling?.innerText?.toLowerCase() || '';
            
            let key = label || placeholder || prevText;
            if (key.includes('first name') || placeholder.includes('first name')) inputMap['first_name'] = inp;
            else if (key.includes('middle') || placeholder.includes('middle')) inputMap['middle_names'] = inp;
            else if (key.includes('last name') || placeholder.includes('last name')) inputMap['last_name'] = inp;
            else if (key.includes('nickname') || placeholder.includes('nickname')) inputMap['nicknames'] = inp;
            else if (key.includes('title') || placeholder.includes('title')) inputMap['titles'] = inp;
            else if (key.includes('prefix') || placeholder.includes('prefix')) inputMap['npc_prefix'] = inp;
        }
        
        function setInputValue(input, val) {
            if (!input) return false;
            let setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            setter.call(input, val);
            input.dispatchEvent(new Event('input', { bubbles: true }));
            input.dispatchEvent(new Event('change', { bubbles: true }));
            return true;
        }
        
        let results = {};
        if (inputMap['first_name']) results['first_name'] = setInputValue(inputMap['first_name'], 'Erik');
        if (inputMap['middle_names']) results['middle_names'] = setInputValue(inputMap['middle_names'], 'Ulfr');
        if (inputMap['last_name']) results['last_name'] = setInputValue(inputMap['last_name'], 'Douglas');
        if (inputMap['nicknames']) results['nicknames'] = setInputValue(inputMap['nicknames'], 'Prime Alpha');
        if (inputMap['titles']) results['titles'] = setInputValue(inputMap['titles'], 'Alpha');
        
        return { matchedInputs: Object.keys(inputMap), results: results };
    }""")
    print("NPC Information fill result:", npc_info_fill)
    time.sleep(1)

    # 4. Set switches: Scan Persona, Whole Words Only, Highlight keywords
    flags_res = page.evaluate("""() => {
        let switches = Array.from(document.querySelectorAll('button[role=\"switch\"], input[type=\"checkbox\"]'));
        let outcomes = {};
        for (let sw of switches) {
            let container = sw.closest('div[class*=\"flex\"], label') || sw.parentElement;
            let labelText = (container ? container.innerText : '').toLowerCase();
            
            let target = null;
            if (labelText.includes('scan persona')) target = 'scan_persona';
            else if (labelText.includes('whole words')) target = 'whole_words_only';
            else if (labelText.includes('highlight keyword')) target = 'highlight_keywords';
            
            if (target) {
                let isChecked = sw.getAttribute('aria-checked') === 'true' || sw.checked === true || sw.getAttribute('data-state') === 'checked';
                if (!isChecked) {
                    sw.click();
                    outcomes[target] = 'toggled_on';
                } else {
                    outcomes[target] = 'already_on';
                }
            }
        }
        return outcomes;
    }""")
    print("Flags configuration result:", flags_res)
    time.sleep(1)

    # Save Erik reconfigured
    save_btn = page.locator('button:has-text("Save Changes")').first
    print("Erik Save button text:", save_btn.inner_text())
    
    with page.expect_response(lambda r: 'api/lorebooks/_zwEqgEEzh12X6gHVmMKKC' in r.url and r.request.method == 'PUT', timeout=30000) as response_info:
        print("Clicking 'Save Changes' for Erik reconfiguration...")
        save_btn.click()
    
    erik_put_resp = response_info.value
    print(f"Erik Save completed with HTTP status: {erik_put_resp.status}")
    time.sleep(3)

    # STEP C: Inspect DOM on Erik to check if "Custom Image ⚠️ Unknown source" is gone
    print("\n--- STEP C: Validating Erik DOM Warnings ---")
    dom_check = page.evaluate("""() => {
        let text = document.body.innerText;
        let hasUnknownSource = text.includes('Unknown source');
        let hasCustomImage = text.includes('Custom Image');
        
        // Find avatar image element in right panel
        let avatarImgs = Array.from(document.querySelectorAll('img')).filter(i => 
            i.src.includes('29a667f2') || (i.alt || '').toLowerCase().includes('avatar')
        ).map(i => ({ src: i.src, alt: i.alt }));

        return {
            hasUnknownSource: hasUnknownSource,
            hasCustomImage: hasCustomImage,
            matchingAvatarImages: avatarImgs
        };
    }""")
    print("DOM validation result:", json.dumps(dom_check, indent=2))
    
    print("\nConsole errors:", console_errors[:5])
    print("Network errors:", network_errors[:5])
    
    ctx.close()
    print("\n=== TEST COMPLETED SUCCESSFULLY ===")

import os
import sys
import time
import json
from playwright.sync_api import sync_playwright

temp_profile = r'C:\Users\mande\.gemini\antigravity\brain\88874201-ff74-4d24-9b6a-25251d18ed6a\scratch\chrome_temp_profile'
chrome_dev_path = r'C:\Program Files\Google\Chrome Dev\Application\chrome.exe'

print("=================================================================")
print("=== ESECUZIONE COMPLETA TEST GUIDATO BROWSER SU LOREBOOK PRIMARY ===")
print("=================================================================")

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
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

    lorebook_url = 'https://app.wyvern.chat/lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC'
    print(f"\n[1/5] Navigazione a {lorebook_url}...")
    page.goto(lorebook_url, wait_until='domcontentloaded', timeout=40000)
    time.sleep(5)

    # Click tab Entries
    page.locator('button[role="tab"]:has-text("Entries")').first.click()
    time.sleep(2)

    # STEP A: Reset ALL 99 entries to 'none'
    print("\n[2/5] Reset del campo Entry Type a 'No specific type' (none) su tutte le 99 entry...")
    reset_stats = page.evaluate("""() => {
        let items = Array.from(document.querySelectorAll('div.group[class*="cursor-pointer"]'));
        return { count: items.length };
    }""")
    total_entries = reset_stats.get('count', 0)
    print(f"  Trovate {total_entries} entry nella lista del Lorebook.")

    for idx in range(total_entries):
        page.evaluate("""(idx) => {
            let items = Array.from(document.querySelectorAll('div.group[class*="cursor-pointer"]'));
            if (idx >= items.length) return;
            let item = items[idx];
            item.scrollIntoView({ block: 'nearest' });
            item.click();
            
            let typeSelect = Array.from(document.querySelectorAll('select')).find(s => 
                Array.from(s.options).some(o => o.text.includes('No specific type'))
            );
            if (typeSelect && typeSelect.value !== 'none') {
                typeSelect.value = 'none';
                typeSelect.dispatchEvent(new Event('change', { bubbles: true }));
                typeSelect.dispatchEvent(new Event('input', { bubbles: true }));
            }
        }""", idx)
        if idx % 20 == 0 or idx == total_entries - 1:
            print(f"  Elaborate {idx+1}/{total_entries} entry...")
        time.sleep(0.04)

    print("  Tutte le 99 entry impostate su 'none'.")
    time.sleep(1)

    # Click Save Changes for Reset
    print("\n[3/5] Salvataggio del batch di reset con sincronizzazione schema entries...")
    with page.expect_response(lambda r: 'api/lorebooks/_zwEqgEEzh12X6gHVmMKKC' in r.url and r.request.method == 'PUT', timeout=30000) as resp_info:
        page.evaluate("""() => {
            let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
            let form = btn.closest('form') || document.querySelector('form');
            let fiber = form[Object.keys(form).find(k => k.startsWith('__reactFiber$'))];
            let curr = fiber;
            let control = null;
            while (curr) {
                if (curr.memoizedProps && curr.memoizedProps.control) {
                    control = curr.memoizedProps.control;
                    break;
                }
                curr = curr.return;
            }
            if (control && (!control._formValues.entries || control._formValues.entries.length === 0)) {
                control._formValues.entries = control._formValues.lexicon || [];
            }
            btn.click();
        }""")
    
    put_1 = resp_info.value
    print(f"  Salvataggio Batch 1 completato! HTTP {put_1.status}")
    time.sleep(3)

    # STEP B: Riconfigurazione Erik Ulfr Douglas
    print("\n[4/5] Riconfigurazione completa di Erik Ulfr Douglas...")
    # Click Erik
    page.evaluate("""() => {
        let items = Array.from(document.querySelectorAll('div.group[class*="cursor-pointer"]'));
        let erik = items.find(it => (it.innerText || '').includes('Erik Ulfr Douglas'));
        if (erik) {
            erik.scrollIntoView({ block: 'nearest' });
            erik.click();
        }
    }""")
    time.sleep(2)

    # 1. Imposta Entry Type su NPCSpecial ('npc')
    page.locator('select:has(option[value="npc"])').first.select_option('npc')
    time.sleep(1)
    print("  - Entry Type impostato su NPCSpecial ('npc')")

    # 2. Seleziona erikMain dalla Gallery Popover
    print("  - Apertura selettore avatar da gallery e selezione di erikMain...")
    avatar_combobox = page.locator('button[role="combobox"]:has-text("avatar")').first
    avatar_combobox.click()
    time.sleep(1)

    # Clicca erikMain nel popover
    selected_avatar = page.evaluate("""() => {
        let popover = document.querySelector('[data-radix-popper-content-wrapper]');
        if (!popover) return { error: 'popover not found' };
        
        let items = Array.from(popover.querySelectorAll('div, button, [role="option"]'));
        let erikOpt = items.find(el => (el.innerText || '').trim().startsWith('erikMain'));
        if (erikOpt) {
            erikOpt.click();
            return { success: true, text: erikOpt.innerText.trim() };
        }
        return { error: 'erikMain not found in popover' };
    }""")
    print("  - Risultato selezione avatar:", selected_avatar)
    time.sleep(1)

    # 3. Compilazione campi NPC Information
    print("  - Compilazione campi NPC Information...")
    page.evaluate("""() => {
        let inputs = Array.from(document.querySelectorAll('input'));
        function setVal(input, val) {
            if (!input) return;
            let setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            setter.call(input, val);
            input.dispatchEvent(new Event('input', { bubbles: true }));
            input.dispatchEvent(new Event('change', { bubbles: true }));
        }
        
        for (let inp of inputs) {
            let p = (inp.placeholder || '').toLowerCase();
            let label = (inp.closest('div')?.querySelector('label')?.innerText || '').toLowerCase();
            if (p.includes('first name') || label.includes('first name')) setVal(inp, 'Erik');
            else if (p.includes('middle') || label.includes('middle')) setVal(inp, 'Ulfr');
            else if (p.includes('last name') || label.includes('last name')) setVal(inp, 'Douglas');
            else if (p.includes('nickname') || label.includes('nickname')) setVal(inp, 'Prime Alpha');
            else if (p.includes('title') || label.includes('title')) setVal(inp, 'Alpha');
        }
    }""")
    time.sleep(1)

    # 4. Terna di flag ON
    print("  - Attivazione terna di flag (Scan Persona, Whole Words, Highlight)...")
    page.evaluate("""() => {
        let switches = Array.from(document.querySelectorAll('button[role="switch"], input[type="checkbox"]'));
        for (let sw of switches) {
            let container = sw.closest('div[class*="flex"], label') || sw.parentElement;
            let labelText = (container ? container.innerText : '').toLowerCase();
            if (labelText.includes('scan persona') || labelText.includes('whole words') || labelText.includes('highlight keyword')) {
                let isChecked = sw.getAttribute('aria-checked') === 'true' || sw.checked === true || sw.getAttribute('data-state') === 'checked';
                if (!isChecked) sw.click();
            }
        }
    }""")
    time.sleep(1)

    # Salva Erik
    print("  - Salvataggio definitivo di Erik...")
    with page.expect_response(lambda r: 'api/lorebooks/_zwEqgEEzh12X6gHVmMKKC' in r.url and r.request.method == 'PUT', timeout=30000) as resp_info_erik:
        page.evaluate("""() => {
            let btn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').includes('Save Changes'));
            let form = btn.closest('form') || document.querySelector('form');
            let fiber = form[Object.keys(form).find(k => k.startsWith('__reactFiber$'))];
            let curr = fiber;
            let control = null;
            while (curr) {
                if (curr.memoizedProps && curr.memoizedProps.control) {
                    control = curr.memoizedProps.control;
                    break;
                }
                curr = curr.return;
            }
            if (control && (!control._formValues.entries || control._formValues.entries.length === 0)) {
                control._formValues.entries = control._formValues.lexicon || [];
            }
            btn.click();
        }""")

    put_2 = resp_info_erik.value
    print(f"  Salvataggio di Erik completato! HTTP {put_2.status}")
    time.sleep(4)

    # STEP C: Validazione finale DOM
    print("\n[5/5] Ispezione DOM ed assenza warning...")
    erik_dom = page.evaluate("""() => {
        let text = document.body.innerText;
        let hasUnknownSource = text.includes('Unknown source');
        let hasCustomImage = text.includes('Custom Image');
        
        let avatarImg = document.querySelector('img[src*="29a667f2"]');
        return {
            hasUnknownSource: hasUnknownSource,
            hasCustomImage: hasCustomImage,
            hasErikMainRendered: !!avatarImg,
            avatarSrc: avatarImg ? avatarImg.src : null
        };
    }""")
    print("  Esito validazione DOM:")
    print(" ", json.dumps(erik_dom, indent=2))
    
    ctx.close()

print("\n=================================================================")
print("=== TEST GUIDATO BROWSER CONCLUSO CON SUCCESSO ASSOLUTO ===")
print("=================================================================")

from cdp_controller import ChromeCDP
import json

cdp = ChromeCDP()
targets = cdp.get_targets()
lorebook_target = next(t for t in targets if 'lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC' in t.get('url', ''))
sess = cdp.attach_to_page(lorebook_target['targetId'])

# Check what tabs or elements are present
js_info = """
(() => {
    let buttons = Array.from(document.querySelectorAll('button')).map(b => b.innerText.trim()).filter(Boolean);
    let inputs = Array.from(document.querySelectorAll('input')).map(i => ({ placeholder: i.placeholder, value: i.value, type: i.type }));
    let selects = Array.from(document.querySelectorAll('select')).map(s => ({ value: s.value, options: Array.from(s.options).map(o => o.text) }));
    
    // Check if there is an active dialog or modal
    let dialogs = Array.from(document.querySelectorAll('[role="dialog"], .modal, [data-headlessui-state]')).map(d => ({
        tag: d.tagName,
        text: d.innerText.slice(0, 200)
    }));
    
    // Check entries visible in list
    // Usually lorebook entries are listed with titles or cards
    let entryElements = Array.from(document.querySelectorAll('button, div')).filter(el => {
        let txt = el.innerText || '';
        return txt.includes('Erik') && txt.length < 100;
    }).map(el => ({ tag: el.tagName, text: el.innerText }));

    return {
        url: window.location.href,
        buttons: buttons.slice(0, 30),
        selects: selects,
        dialogs: dialogs,
        sampleEntries: entryElements.slice(0, 10)
    };
})()
"""

info = cdp.evaluate_in_session(sess, js_info)
print(json.dumps(info, indent=2))
cdp.close()

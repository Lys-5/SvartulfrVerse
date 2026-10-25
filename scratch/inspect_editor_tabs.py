from cdp_controller import ChromeCDP
import json

cdp = ChromeCDP()
targets = cdp.get_targets()
lorebook_target = next(t for t in targets if 'lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC' in t.get('url', ''))
sess = cdp.attach_to_page(lorebook_target['targetId'])

js_tabs = """
(() => {
    let tabs = Array.from(document.querySelectorAll('[role="tab"], [role="tablist"] *')).map(t => ({
        tag: t.tagName,
        text: (t.innerText || '').trim(),
        role: t.getAttribute('role'),
        selected: t.getAttribute('aria-selected')
    })).filter(t => t.text.length > 0 && t.text.length < 50);

    let entrySearch = Array.from(document.querySelectorAll('input')).filter(i => 
        (i.placeholder || '').toLowerCase().includes('search') || (i.placeholder || '').toLowerCase().includes('filter')
    ).map(i => ({ placeholder: i.placeholder, value: i.value }));

    let allButtons = Array.from(document.querySelectorAll('button')).map(b => (b.innerText || '').trim());
    
    return {
        tabs: tabs,
        entrySearch: entrySearch,
        totalButtons: allButtons.length,
        someButtons: allButtons.filter(b => b.length > 0 && b.length < 30).slice(0, 40)
    };
})()
"""

info = cdp.evaluate_in_session(sess, js_tabs)
print(json.dumps(info, indent=2))
cdp.close()

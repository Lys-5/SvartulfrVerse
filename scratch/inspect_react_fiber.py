from cdp_controller import ChromeCDP
import json

cdp = ChromeCDP()
targets = cdp.get_targets()
lorebook_target = next(t for t in targets if 'lorebooks/edit/_zwEqgEEzh12X6gHVmMKKC' in t.get('url', ''))
sess = cdp.attach_to_page(lorebook_target['targetId'])

js_inspect_react = """
(() => {
    // Helper to find React fiber
    function getFiber(dom) {
        for (let key in dom) {
            if (key.startsWith('__reactFiber$') || key.startsWith('__reactInternalInstance$')) {
                return dom[key];
            }
        }
        return null;
    }

    // Search for container with lorebook state or entries
    let main = document.querySelector('main') || document.body;
    let fiber = getFiber(main);
    
    // Let's inspect window.__NEXT_DATA__ or similar
    let nextData = window.__NEXT_DATA__ ? {
        page: window.__NEXT_DATA__.page,
        query: window.__NEXT_DATA__.query,
        buildId: window.__NEXT_DATA__.buildId
    } : null;

    // Check how entries are represented in the DOM list
    // Let's find all entries in the sidebar / entry list
    let entryItems = Array.from(document.querySelectorAll('div, li, button')).filter(el => {
        let txt = el.innerText || '';
        return (txt.includes('Erik Ulfr Douglas') || txt.includes('Hugh Rivers')) && el.children.length < 5;
    }).map(el => ({
        tag: el.tagName,
        className: el.className,
        text: el.innerText.slice(0, 50)
    }));

    return {
        nextData: nextData,
        sampleFoundEntries: entryItems.slice(0, 5)
    };
})()
"""

info = cdp.evaluate_in_session(sess, js_inspect_react)
print(json.dumps(info, indent=2))
cdp.close()

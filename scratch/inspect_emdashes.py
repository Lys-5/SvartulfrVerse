import json

with open('FINAL/Svartulfr_Master_Scenario.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k in ['name', 'display_description', 'scenario', 'startup_script']:
    val = data.get(k, '')
    if '\u2014' in val:
        print(f"Top-level key {k} has {val.count(chr(8212))} em-dashes")

for idx, g in enumerate(data.get('greetings', [])):
    gname = g.get('name', '')
    if '\u2014' in gname:
        print(f"Greeting [{idx}] name has em-dash: {gname}")
    for p in g.get('linked_personas', []):
        for pk in ['name', 'title', 'comment']:
            pv = p.get(pk, '')
            if '\u2014' in pv:
                print(f"Greeting [{idx}] persona {p.get('name')} field {pk} has em-dash: {pv}")
    for m_idx, m in enumerate(g.get('messages', [])):
        m_txt = m.get('content', '') or m.get('message', '') or ''
        if '\u2014' in m_txt:
            print(f"Greeting [{idx}] message [{m_idx}] content has {m_txt.count(chr(8212))} em-dashes")

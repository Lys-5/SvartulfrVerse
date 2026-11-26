import json

fpath = 'FINAL/Svartulfr_Master_Scenario.json'
with open(fpath, 'r', encoding='utf-8') as f:
    data = json.load(f)

greetings = data.get('greetings', [])
out = [f"Total greetings in Master Scenario: {len(greetings)}\n"]

for i, g in enumerate(greetings):
    gid = g.get('id')
    name = g.get('name')
    desc = g.get('description')
    lpi = g.get('linked_persona_ids')
    lp = g.get('linked_personas')
    msgs = g.get('messages', [])
    content = g.get('content', '')
    
    out.append(f"--- Greeting {i} ---")
    out.append(f"ID: {gid}")
    out.append(f"Name: {name}")
    out.append(f"Description: {desc}")
    out.append(f"Current linked_persona_ids: {lpi}")
    out.append(f"Current linked_personas count: {len(lp) if isinstance(lp, list) else 'None'}")
    if isinstance(lp, list) and lp:
        out.append(f"Current linked_personas names: {[p.get('name') for p in lp]}")
    out.append(f"Messages count: {len(msgs)}")
    if msgs:
        out.append(f"Msg 0 speaker_slot: {msgs[0].get('speaker_slot')}")
        out.append(f"Msg 0 content preview: {msgs[0].get('content', '')[:140]}...")
    out.append(f"Greeting content preview: {content[:140]}...\n")

with open('.agents/teamwork/explorer_scenarios_15lb_1/master_greetings_dump.txt', 'w', encoding='utf-8') as f_out:
    f_out.write('\n'.join(out))

print("Dumped successfully.")

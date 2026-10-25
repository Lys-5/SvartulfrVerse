import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
scen = json.loads((ROOT / 'scratch' / 'live_scenario_rev16.json').read_text(encoding='utf-8'))

out = []
for i, g in enumerate(scen.get('greetings', []), 1):
    out.append("=" * 80)
    out.append(f"GREETING #{i:02d} | id={g.get('id')}")
    out.append(f"NAME: {g.get('name')}")
    out.append(f"DESC: {g.get('description')}")
    out.append(f"SLOT: {g.get('speaker_slot')}")
    out.append(f"PERSONAS: {g.get('linked_persona_ids')}")
    out.append(f"ROOT CONTENT:\n{g.get('content')}")
    msgs = g.get('messages', [])
    out.append(f"\nMESSAGES ({len(msgs)}):")
    for mi, m in enumerate(msgs):
        out.append(f"--- msg[{mi}] id={m.get('id')} | slot={m.get('speaker_slot')} ---")
        out.append(m.get('content', ''))

(ROOT / 'scratch' / 'live_rev16_full_greetings.txt').write_text('\n'.join(out), encoding='utf-8')
print("Wrote scratch/live_rev16_full_greetings.txt")

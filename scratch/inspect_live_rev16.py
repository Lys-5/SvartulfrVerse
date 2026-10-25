import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
scen = json.loads((ROOT / 'scratch' / 'live_scenario_rev16.json').read_text(encoding='utf-8'))

lines = []
lines.append(f"Top level keys: {list(scen.keys())}")
lines.append("=== SLOTS ===")
slots_key = 'character_slots' if 'character_slots' in scen else 'slots'
lines.append(f"Slots field name: {slots_key}")
for i, s in enumerate(scen.get(slots_key, []), 1):
    lines.append(f"{i:02d}. key={s.get('key')} | label={s.get('label')} | pool={[p.get('character_id') for p in s.get('pool', [])]}")

lines.append("\n=== LOREBOOKS ===")
lines.append(str(scen.get('lorebook_ids')))

lines.append("\n=== GREETINGS ===")
for i, g in enumerate(scen.get('greetings', []), 1):
    lines.append(f"\n--- {i:02d}. id={g.get('id')} ---")
    lines.append(f"  name: {g.get('name')}")
    lines.append(f"  description: {g.get('description')}")
    lines.append(f"  speaker_slot: {g.get('speaker_slot')}")
    lines.append(f"  linked_persona_ids: {g.get('linked_persona_ids')}")
    msgs = g.get('messages', [])
    lines.append(f"  messages count: {len(msgs)} | slots: {[m.get('speaker_slot') for m in msgs]}")
    lines.append(f"  content preview: {g.get('content', '')[:200]!r}")
    for mi, m in enumerate(msgs):
        lines.append(f"    msg[{mi}] id={m.get('id')} slot={m.get('speaker_slot')}: {m.get('content', '')[:150]!r}")

(ROOT / 'scratch' / 'live_rev16_summary.txt').write_text('\n'.join(lines), encoding='utf-8')
print("Wrote scratch/live_rev16_summary.txt")

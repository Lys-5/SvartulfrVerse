import json
import pathlib

MY_DIR = pathlib.Path(__file__).parent
live_dump = json.loads((MY_DIR / 'live_scenarios_dump.json').read_text(encoding='utf-8'))

alyssa_live = live_dump['char_scenario_CKgwq246DyCj1NNTBV9rt']

print("=== ALYSSA LIVE (rev 10) GREETINGS ===")
for idx, g in enumerate(alyssa_live.get('greetings', [])):
    print(f"\nGreeting [{idx}]: id={g.get('id')}, name={g.get('name')}, speaker_slot={g.get('speaker_slot')}")
    print(f"  Description: {g.get('description')}")
    print(f"  Messages ({len(g.get('messages', []))}):")
    for midx, m in enumerate(g.get('messages', [])):
        print(f"    m[{midx}] id={m.get('id')}, speaker_slot={m.get('speaker_slot')}, len={len(m.get('content', ''))}")
        print(f"      content snippet: {m.get('content', '')[:100]}...")

print("\n=== ALYSSA LIVE SLOTS ===")
for s in alyssa_live.get('slots', []):
    print(f"  Slot: key={s.get('key')}, label={s.get('label')}, unavail={s.get('unavailable_count')}, pool={s.get('pool')}")

print("\n=== JASPER LIVE (rev 4) GREETINGS ===")
jasper_live = live_dump['char_scenario_Kq4mJEBH83j7Q7DdVfFnF']
for idx, g in enumerate(jasper_live.get('greetings', [])):
    print(f"\nGreeting [{idx}]: id={g.get('id')}, name={g.get('name')}, speaker_slot={g.get('speaker_slot')}")
    print(f"  Description: {g.get('description')}")
    print(f"  Messages ({len(g.get('messages', []))}):")
    for midx, m in enumerate(g.get('messages', [])):
        print(f"    m[{midx}] id={m.get('id')}, speaker_slot={m.get('speaker_slot')}, len={len(m.get('content', ''))}")
        print(f"      content snippet: {m.get('content', '')[:100]}...")

print("\n=== JASPER LIVE SLOTS ===")
for s in jasper_live.get('slots', []):
    print(f"  Slot: key={s.get('key')}, label={s.get('label')}, unavail={s.get('unavailable_count')}, pool={s.get('pool')}")

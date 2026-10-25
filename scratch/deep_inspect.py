import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

with open(ROOT / 'scratch' / 'raw_live_characters_m1_review.json', encoding='utf-8') as f:
    chars = json.load(f)

print(f"Loaded {len(chars)} characters from live response dump.\n")

for c in chars:
    name = c.get('display_name')
    wid = c.get('world_id')
    bdate = c.get('birthdate')
    tl = c.get('start_timeline_position')
    avatar = c.get('avatar')
    rpg = c.get('rpg_stats') or {}
    keys = c.get('keys')
    whole_words = c.get('whole_words_only')
    is_global = c.get('is_global')
    summary = c.get('summary')
    long_summary = c.get('long_summary')
    final_inst = c.get('final_instructions')
    
    print(f"=== {name} ({c.get('_id')}) ===")
    print(f"  world_id: {wid}")
    print(f"  birthdate == start_timeline_position: {bdate == tl} ({bdate})")
    print(f"  avatar: {avatar}")
    print(f"  keys: {keys}")
    print(f"  whole_words_only: {whole_words}, is_global: {is_global}")
    print(f"  rpg: enabled={rpg.get('enabled')}, level={rpg.get('level')}")
    print(f"  base_stats: {rpg.get('base_stats')}")
    print(f"  summary: {summary[:80]}...")
    print(f"  long_summary len: {len(long_summary) if long_summary else 0}")
    print(f"  final_instructions: {final_inst}\n")

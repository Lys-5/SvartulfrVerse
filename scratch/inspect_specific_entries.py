import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

lb1 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_I.json').read_text(encoding='utf-8'))
lb2 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_II.json').read_text(encoding='utf-8'))

print("=== LOREBOOK I ENTRIES ===")
for eid in ['HxdpzBtgY_wSx5ZpIDzGK', 'WTVBwGkRovmXZKfrjYKBw', 'pyWwstSbY5IYYvNn-4-hf', 'lb1_nine_firstborn_pantheon']:
    e = next((x for x in lb1['lexicon'] if x.get('entry_id') == eid), None)
    if e:
        print(f"\n--- {e['name']} ({eid}) ---")
        print(e['content'][:1500])

print("\n=== LOREBOOK II ENTRIES ===")
for eid in ['nbeEd2cvkA5PLke6svWez', 'qCmzi5J5o-ocZcFJWyovq', 'K7t7KMDSBtyjB90gz0pWf', 'iaKAUBJ3qDchReuK2WnEE', '21rz_Jv-VaddKBNMya2tf']:
    e = next((x for x in lb2['lexicon'] if x.get('entry_id') == eid), None)
    if e:
        print(f"\n--- {e['name']} ({eid}) ---")
        print(e['content'][:1500])

import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
lb1 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_I.json').read_text(encoding='utf-8'))
for eid in ['HxdpzBtgY_wSx5ZpIDzGK', 'WTVBwGkRovmXZKfrjYKBw', 'pyWwstSbY5IYYvNn-4-hf', 'lb1_nine_firstborn_pantheon']:
    e = next(x for x in lb1['lexicon'] if x.get('entry_id') == eid)
    print('==================================================')
    print(f"ENTRY: {e['name']} ({eid})")
    print('==================================================')
    print(e['content'])

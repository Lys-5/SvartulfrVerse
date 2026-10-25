import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

lb1 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_I.json').read_text(encoding='utf-8'))
lb2 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_II.json').read_text(encoding='utf-8'))

terms = [
    'Living Sagas',
    'LSE History Timeline',
    'La Guerra di Fenris',
    'LSE Blood Classification',
    'House Genealogies Summary',
    'Zefir',
    'Ut Berg',
    'Firstborn: Wulfnic',
    '1005 AD',
    '823 AD',
    '827 AD',
    'pre-827',
]

for name, lb in [('LB1', lb1), ('LB2', lb2)]:
    for idx, e in enumerate(lb['lexicon']):
        title = e.get('comment', '') or e.get('name', '')
        c = e.get('content', '')
        matches = []
        for t in terms:
            if t.lower() in title.lower() or t.lower() in c.lower():
                matches.append(t)
        if matches:
            print(f"{name} [{idx}] id={e.get('entry_id')} name=\"{e.get('name')}\" comment=\"{title}\" matches={matches}")

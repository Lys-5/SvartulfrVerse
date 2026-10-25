import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
lb2 = json.loads((ROOT / 'FINAL' / 'Svartulfr_Lorebook_II.json').read_text(encoding='utf-8'))
for eid in ['nbeEd2cvkA5PLke6svWez', 'qCmzi5J5o-ocZcFJWyovq', 'K7t7KMDSBtyjB90gz0pWf']:
    e = next(x for x in lb2['lexicon'] if x.get('entry_id') == eid)
    print('==================================================')
    print(f"ENTRY: {e['name']} ({eid})")
    print('==================================================')
    print(e['content'])

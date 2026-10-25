import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

# 1. Update Lorebook I
for p in [ROOT / 'FINAL' / 'Svartulfr_Lorebook_I.json', ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_Lorebook_I.json']:
    data = json.loads(p.read_text(encoding='utf-8'))
    updated = False
    for e in data['lexicon']:
        if e.get('entry_id') == 'HxdpzBtgY_wSx5ZpIDzGK':
            target_str = "nell'827 d.C."
            assert target_str in e['content'], f"{target_str} not found in {p}"
            e['content'] = e['content'].replace(target_str, "nell'824 d.C.")
            updated = True
            break
    assert updated, f'Entry HxdpzBtgY_wSx5ZpIDzGK not found in {p}'
    data['entries'] = [dict(e) for e in data['lexicon']]
    assert data['entries'] == data['lexicon']
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Updated {p} successfully!')

# 2. Update Lorebook II
for p in [ROOT / 'FINAL' / 'Svartulfr_Lorebook_II.json', ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_Lorebook_II.json']:
    data = json.loads(p.read_text(encoding='utf-8'))
    
    # Entry 51: nbeEd2cvkA5PLke6svWez
    e51 = next((e for e in data['lexicon'] if e.get('entry_id') == 'nbeEd2cvkA5PLke6svWez'), None)
    assert e51 is not None and 'Born circa 827 AD in Iceland' in e51['content']
    e51['content'] = e51['content'].replace('Born circa 827 AD in Iceland', 'Born circa 824 AD in Iceland')
    
    # Entry 80: qCmzi5J5o-ocZcFJWyovq
    e80 = next((e for e in data['lexicon'] if e.get('entry_id') == 'qCmzi5J5o-ocZcFJWyovq'), None)
    assert e80 is not None and '(born circa 827 AD, Iceland)' in e80['content']
    e80['content'] = e80['content'].replace('(born circa 827 AD, Iceland)', '(born circa 824 AD, Iceland)')
    
    # Entry 91: ffB2cSM0T_5MYbddXlzNf
    e91 = next((e for e in data['lexicon'] if e.get('entry_id') == 'ffB2cSM0T_5MYbddXlzNf'), None)
    assert e91 is not None and "Wulfnic nacque nell'827 d.C." in e91['content']
    e91['content'] = e91['content'].replace("Wulfnic nacque nell'827 d.C.", "Wulfnic nacque nell'824 d.C.")
    assert 'Nel 2026, Wulfnic ha circa 1199 anni.' in e91['content']
    e91['content'] = e91['content'].replace('Nel 2026, Wulfnic ha circa 1199 anni.', 'Nel 2024, Wulfnic compie 1200 anni.')
    
    # Entry 93: 21rz_Jv-VaddKBNMya2tf
    e93 = next((e for e in data['lexicon'] if e.get('entry_id') == '21rz_Jv-VaddKBNMya2tf'), None)
    assert e93 is not None and 'Alpha of Alphas. Born circa 827 AD.' in e93['content']
    e93['content'] = e93['content'].replace('Alpha of Alphas. Born circa 827 AD.', 'Alpha of Alphas. Born circa 824 AD.')
    
    data['entries'] = [dict(e) for e in data['lexicon']]
    assert data['entries'] == data['lexicon']
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f'Updated {p} successfully!')

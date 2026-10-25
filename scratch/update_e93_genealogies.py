import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

for folder in ['FINAL', 'lorebooks/optimized']:
    p = ROOT / folder / 'Svartulfr_Lorebook_II.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    e_gene = next(e for e in d['lexicon'] if e.get('entry_id') == '21rz_Jv-VaddKBNMya2tf')
    gene_c = e_gene['content']
    
    if "Born circa 824 AD." in gene_c:
        gene_c = gene_c.replace(
            "Born circa 824 AD.",
            "Born December 21, 824 AD; turned at 40 in 864 AD."
        )
    elif "Born December 21, 824 AD." not in gene_c:
        gene_c = gene_c.replace(
            "Wulfnic Bloodmoon: Divine Blood (Firstborn), Primordial Enigma. Silver-white hair (originally blond), ice-blue eyes. The First Fang, Alpha of Alphas.",
            "Wulfnic Bloodmoon: Divine Blood (Firstborn), Primordial Enigma. Silver-white hair (originally blond), ice-blue eyes. The First Fang, Alpha of Alphas. Born December 21, 824 AD; turned at 40 in 864 AD."
        )
    assert '—' not in gene_c and '*' not in gene_c
    e_gene['content'] = gene_c
    
    # Invariant
    d['entries'] = [dict(e) for e in d['lexicon']]
    assert d['entries'] == d['lexicon']
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Updated {p}")

import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'

prim = json.loads((FINAL_DIR / 'Svartulfr_NPC_Primary.json').read_text(encoding='utf-8'))['lexicon']
sec = json.loads((FINAL_DIR / 'Svartulfr_NPC_Secondary.json').read_text(encoding='utf-8'))['lexicon']

dups = ['Zaire Ziisis', 'Xaiden Nershatar', 'Lestat Oreven', 'Caien Vaelion', 'Aeril Royen', 'Ashton Crowley', 'Amerian de Vian', 'Goran', 'Kian', 'Radek']

print("=== CONFRONTO CONTENUTI DUPLICATI NPC PRIMARY vs SECONDARY ===")
for dname in dups:
    p_e = next((e for e in prim if e.get('name', '').lower() == dname.lower()), None)
    s_e = next((e for e in sec if e.get('name', '').lower() == dname.lower()), None)
    
    p_len = len(p_e.get('content', '')) if p_e else 0
    s_len = len(s_e.get('content', '')) if s_e else 0
    p_av = bool(p_e.get('avatar')) if p_e else False
    s_av = bool(s_e.get('avatar')) if s_e else False
    
    print(f"\n{dname}:")
    print(f"  Primary:   length={p_len}, avatar={p_av}, regex={bool(p_e.get('avatar_activation_regex'))}")
    print(f"  Secondary: length={s_len}, avatar={s_av}, regex={bool(s_e.get('avatar_activation_regex'))}")

import json
import pathlib
import re
from collections import Counter

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'

LOREBOOKS = [
    ('Svartulfr_Lorebook_I.json', 'Lorebook I (LSE, Core, Runes, Houses)'),
    ('Svartulfr_Lorebook_II.json', 'Lorebook II (DDM, Economy, Items, Contracts)'),
    ('Svartulfr_Lorebook_III.json', 'Lorebook III (SUCC & Underworld)'),
    ('Svartulfr_Location.json', 'Location (Structured Locations)'),
    ('Svartulfr_NPC_Primary.json', 'NPC Primary (Main NPCs & Family)'),
    ('Svartulfr_NPC_Secondary.json', 'NPC Secondary (Secondary & Tertiary NPCs)'),
]

report = []

def log(msg=""):
    print(msg)
    report.append(msg)

log("================================================================================")
log("       AUDIT COMPLETO INTEGRITÀ DATI E COMPLETEZZA DEI 6 LOREBOOK STANDALONE    ")
log("================================================================================\n")

total_entries_all = 0
global_issues = []

for fname, title in LOREBOOKS:
    fpath = FINAL_DIR / fname
    if not fpath.exists():
        log(f"FILE NON TROVATO: {fname}")
        continue
        
    data = json.loads(fpath.read_text(encoding='utf-8'))
    entries = data.get('lexicon') or data.get('entries') or []
    total_entries_all += len(entries)
    
    log(f"--- {fname} | {title} ---")
    log(f"  Totale Voci: {len(entries)}")
    log(f"  Metadati Top-Level: name='{data.get('name')}', token_budget={data.get('token_budget')}, scan_depth={data.get('scan_depth')}")
    
    types_counter = Counter()
    missing_name = []
    missing_content = []
    empty_keys_not_constant = []
    has_age_macro = []
    has_em_dash = []
    has_npc_fields = []
    npc_missing_regex = []
    npc_missing_avatar = []
    npc_missing_info = []
    broad_keys_found = []
    
    BROAD_SET = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega', 'beta'}

    for idx, e in enumerate(entries):
        name = e.get('name', '').strip()
        etype = e.get('type')
        types_counter[str(etype)] += 1
        content = e.get('content', '')
        keys = e.get('keys', [])
        clean_keys = [k.strip() for k in keys if k and k.strip()]
        constant = e.get('constant', False)
        
        # 1. Name check
        if not name:
            missing_name.append(idx)
            
        # 2. Content check
        if not content.strip():
            missing_content.append((idx, name))
            
        # 3. Keys check: non-constant with no keys can never trigger
        if not clean_keys and not constant:
            empty_keys_not_constant.append((idx, name))
            
        # 4. Macros
        if '{{age}}' in content:
            has_age_macro.append((idx, name))
            
        # 5. Em-dash check
        if '—' in content or '—' in name:
            has_em_dash.append((idx, name))
            
        # 6. Broad keys on NPCs
        if etype == 'npc':
            overlap = set(k.lower() for k in clean_keys).intersection(BROAD_SET)
            if overlap:
                broad_keys_found.append((idx, name, list(overlap)))
                
        # 7. NPC Specific fields
        if etype == 'npc':
            if not e.get('avatar_activation_regex'):
                npc_missing_regex.append((idx, name))
            if not e.get('avatar') or 'placeholder' in e.get('avatar', '').lower():
                npc_missing_avatar.append((idx, name))
            if not e.get('npc_info'):
                npc_missing_info.append((idx, name))
        else:
            # Check if non-NPC has NPC fields populated
            if e.get('npc_info') or e.get('avatar_activation_regex'):
                has_npc_fields.append((idx, name, etype))

    log("  Distribuzione Entry Type:")
    for t, cnt in types_counter.most_common():
        log(f"    - '{t}': {cnt}")
        
    log("  Verifiche Integrità:")
    log(f"    * Voci senza nome: {len(missing_name)}")
    log(f"    * Voci con content vuoto: {len(missing_content)}")
    log(f"    * Voci senza keys e NON constant (inattive): {len(empty_keys_not_constant)}")
    log(f"    * Voci con macro {{{{age}}}} residua: {len(has_age_macro)}")
    log(f"    * Voci con em-dash ('—'): {len(has_em_dash)}")
    
    if etype == 'npc' or 'NPC' in fname:
        log(f"    * NPC senza avatar_activation_regex: {len(npc_missing_regex)}")
        log(f"    * NPC senza avatar reale/placeholder: {len(npc_missing_avatar)}")
        log(f"    * NPC senza npc_info strutturato: {len(npc_missing_info)}")
        log(f"    * NPC con BROAD_KEYS generiche: {len(broad_keys_found)}")
        if broad_keys_found:
            for b in broad_keys_found[:5]:
                log(f"       -> [{b[0]}] {b[1]}: broad keys {b[2]}")
    else:
        log(f"    * Voci non-NPC con campi NPC spuri: {len(has_npc_fields)}")
        if has_npc_fields:
            for h in has_npc_fields[:5]:
                log(f"       -> [{h[0]}] {h[1]} (type={h[2]})")
                
    if empty_keys_not_constant:
        for ek in empty_keys_not_constant[:5]:
            log(f"       -> ATTENZIONE INATTIVA: [{ek[0]}] {ek[1]}")
    if has_age_macro:
        for ha in has_age_macro[:5]:
            log(f"       -> MACRO AGE RESIDUA: [{ha[0]}] {ha[1]}")
            
    log("\n" + "-"*60 + "\n")

log(f"TOTALE COMPLESSIVO VOCI SUI 6 LOREBOOK: {total_entries_all}")

# Save report to scratch
(ROOT / 'scratch' / 'lorebooks_integrity_report.txt').write_text("\n".join(report), encoding='utf-8')
log("Report salvato in scratch/lorebooks_integrity_report.txt")

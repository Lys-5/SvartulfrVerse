import json
import re
from collections import Counter

prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))

p_lex = prim.get('lexicon', [])
s_lex = sec.get('lexicon', [])

print(f"Total entries: Primary={len(p_lex)}, Secondary={len(s_lex)}, Total={len(p_lex)+len(s_lex)}")

# -------------------------------------------------------------
# 1. Standard JED+ layout across all 310 entries
# -------------------------------------------------------------
# - Check how many entries currently begin with a bracket block `[...]`.
# - Check section headers: uppercase `BACKSTORY:`, `FAMILY & PACK:` or `CLAN AND COMPANY:`, `VOICE & BEHAVIOR:`, thematic closure.
# - Identify entries with non-standard headers (e.g. `VOICE & PERSONALITY:` or lowercase headers).

def analyze_headers(entries, label):
    bracket_starts = 0
    non_bracket = []
    
    backstory_count = 0
    family_pack_count = 0
    clan_company_count = 0
    voice_behavior_count = 0
    thematic_closure_count = 0
    
    non_standard_headers = []
    all_headers = Counter()
    entries_missing_sections = []
    
    for idx, e in enumerate(entries):
        eid = e.get('entry_id', f'idx_{idx}')
        name = e.get('name', 'UNKNOWN')
        content = e.get('content', '')
        lines = content.strip().split('\n')
        
        # Check bracket start
        if content.strip().startswith('['):
            bracket_starts += 1
        else:
            non_bracket.append((eid, name, content.strip()[:80]))
            
        # Detect headers in the text
        # Regex to find uppercase or mixed case headers like "HEADER:"
        found_headers = []
        for line in lines:
            line_str = line.strip()
            # If line is bracket block or inside one, skip
            if line_str.startswith('[') and line_str.endswith(']'):
                # thematic closure could be like [THE WEIGHT HE CARRIES] or [CORE TRAGEDY] or bracket block
                # if it contains semicolons, it's attribute block; if not, could be thematic closure
                if ';' not in line_str and len(line_str) < 60:
                    found_headers.append(line_str)
                continue
            
            # match lines ending with colon or starting with title:
            m = re.match(r'^([A-Za-z0-9\s&/\-\'\"_]+):(?:\s*(.*))?$', line_str)
            if m:
                h = m.group(1).strip()
                # filter out false positives: lines inside dialogues, or simple timestamp/time, or attribute keys
                if len(h) <= 40 and not any(k in h.upper() for k in ['NAME', 'SPECIES', 'AGE', 'ROLE', 'GENDER', 'HEIGHT', 'BUILD', 'AFFILIATION', 'OCCUPATION', 'STATUS']):
                    found_headers.append(h + ':')
                    all_headers[h.upper() + ':'] += 1
                    
                    # check non-standard
                    # standard: BACKSTORY:, FAMILY & PACK:, CLAN AND COMPANY:, VOICE & BEHAVIOR:
                    if 'VOICE' in h.upper() and h != 'VOICE & BEHAVIOR':
                        non_standard_headers.append((eid, name, h + ':', line_str[:60]))
                    elif any(c.islower() for c in h) and not h.startswith('http'):
                        non_standard_headers.append((eid, name, h + ':', line_str[:60]))

        # Count canonical
        has_bs = any('BACKSTORY:' in h for h in found_headers) or 'BACKSTORY:' in content
        has_fp = any('FAMILY & PACK:' in h for h in found_headers) or 'FAMILY & PACK:' in content
        has_cc = any(x in content for x in ['CLAN AND COMPANY:', 'CLAN & COMPANY:', 'CLAN AND PACK:', 'FAMILY & CLAN:'])
        has_vb = any('VOICE & BEHAVIOR:' in h for h in found_headers) or 'VOICE & BEHAVIOR:' in content
        
        # Thematic closure check:
        # Check last 3 non-empty lines for bracketed title or uppercase section like [CORE TRAGEDY], [THE WEIGHT HE CARRIES], [PERSONAL STRUGGLE], etc.
        thematic = False
        for l in reversed(lines[-5:]):
            l_s = l.strip()
            if l_s.startswith('[') and l_s.endswith(']') and ';' not in l_s:
                thematic = True
                break
            # Or uppercase header like CORE TRAGEDY: or THE SECRET HE CARRIES:
            m_th = re.match(r'^([A-Z0-9\s&/\-]+):', l_s)
            if m_th:
                th_name = m_th.group(1).strip()
                if any(kw in th_name for kw in ['TRAGEDY', 'WEIGHT', 'SECRET', 'CONFLICT', 'STRUGGLE', 'AMBITION', 'LEGACY', 'DRIVE', 'BURDEN', 'VULNERABILITY', 'CORE', 'SHADOW', 'TENSION']):
                    thematic = True
                    break
        
        if has_bs: backstory_count += 1
        if has_fp: family_pack_count += 1
        if has_cc: clan_company_count += 1
        if has_vb: voice_behavior_count += 1
        if thematic: thematic_closure_count += 1
        
        # Track missing
        missing = []
        if not has_bs: missing.append("BACKSTORY")
        if not (has_fp or has_cc): missing.append("FAMILY & PACK / CLAN AND COMPANY")
        if not has_vb: missing.append("VOICE & BEHAVIOR")
        if not thematic: missing.append("THEMATIC CLOSURE")
        if missing:
            entries_missing_sections.append((eid, name, missing))

    print(f"\n--- {label} Header Analysis ---")
    print(f"Starts with bracket '[': {bracket_starts}/{len(entries)}")
    print(f"Non-bracket entries: {len(non_bracket)}")
    print(f"BACKSTORY: {backstory_count}/{len(entries)}")
    print(f"FAMILY & PACK: {family_pack_count}/{len(entries)}")
    print(f"CLAN AND COMPANY (or variant): {clan_company_count}/{len(entries)}")
    print(f"FAMILY/PACK/CLAN total: {family_pack_count + clan_company_count}/{len(entries)}")
    print(f"VOICE & BEHAVIOR: {voice_behavior_count}/{len(entries)}")
    print(f"Thematic closure: {thematic_closure_count}/{len(entries)}")
    print(f"Non-standard headers flagged ({len(non_standard_headers)}):")
    for x in non_standard_headers[:15]:
        print(f"  {x[0]} ({x[1]}): {x[2]} -> {x[3]}")
    print(f"Top 15 headers in {label}:")
    for h, c in all_headers.most_common(15):
        print(f"  {h}: {c}")

analyze_headers(p_lex, "Primary Lorebook")
analyze_headers(s_lex, "Secondary Lorebook")

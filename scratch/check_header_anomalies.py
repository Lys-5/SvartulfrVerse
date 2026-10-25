import json
import re

prim = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
sec = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))

p_lex = prim.get('lexicon', [])
s_lex = sec.get('lexicon', [])

print("=== CHECKING ALL 310 ENTRIES FOR NON-STANDARD HEADERS ===")

# Standard headers per JED+:
# 1. Bracket block: [...]
# 2. BACKSTORY:
# 3. FAMILY & PACK: (or CLAN AND COMPANY:)
# 4. VOICE & BEHAVIOR:
# 5. Thematic closure (e.g. [THE WEIGHT HE CARRIES] or THE SECRET HE CARRIES: or similar)

def check_entry(origin, idx, e):
    eid = e.get('entry_id', f'idx_{idx}')
    name = e.get('name', 'UNKNOWN')
    content = e.get('content', '')
    
    # 1. Bracket start
    stripped = content.strip()
    starts_bracket = stripped.startswith('[')
    
    # 2. Find all headers (lines starting with uppercase word(s) ending with colon, or bracketed theme)
    lines = stripped.split('\n')
    headers = []
    has_lowercase_header = []
    voice_header = None
    
    for l in lines:
        ls = l.strip()
        # skip initial bracket block
        if ls.startswith('[') and ';' in ls:
            continue
        
        # Check bracketed header like [CORE TRAGEDY]
        if ls.startswith('[') and ls.endswith(']') and ';' not in ls:
            headers.append(ls)
            continue
            
        m = re.match(r'^([A-Za-z0-9\s&/\-\'\"_]+):(?:\s*(.*))?$', ls)
        if m:
            h = m.group(1).strip()
            # filter out sub-items, dialogue lines or list items
            if len(h) <= 45 and not h.startswith('-') and not h.startswith('*'):
                headers.append(h + ':')
                if any(c.islower() for c in h) and not h.startswith('http'):
                    has_lowercase_header.append(h + ':')
                if 'VOICE' in h.upper() or 'PERSONALITY' in h.upper():
                    voice_header = h + ':'

    has_bs = 'BACKSTORY:' in headers or 'BACKSTORY:' in content
    has_fp = 'FAMILY & PACK:' in headers or 'FAMILY & PACK:' in content
    has_cc = 'CLAN AND COMPANY:' in headers or 'CLAN AND COMPANY:' in content or 'CLAN & COMPANY:' in content
    has_vb = 'VOICE & BEHAVIOR:' in headers or 'VOICE & BEHAVIOR:' in content
    
    return {
        'origin': origin,
        'id': eid,
        'name': name,
        'starts_bracket': starts_bracket,
        'headers': headers,
        'has_bs': has_bs,
        'has_fp': has_fp,
        'has_cc': has_cc,
        'has_vb': has_vb,
        'voice_header': voice_header,
        'has_lowercase_header': has_lowercase_header,
        'content_len': len(content)
    }

all_checked = []
for idx, e in enumerate(p_lex):
    all_checked.append(check_entry("Primary", idx, e))
for idx, e in enumerate(s_lex):
    all_checked.append(check_entry("Secondary", idx, e))

print(f"Total entries analyzed: {len(all_checked)}")

# Let's find all entries where voice_header is not 'VOICE & BEHAVIOR:'
voice_anomalies = []
for c in all_checked:
    vh = c['voice_header']
    if vh and vh != 'VOICE & BEHAVIOR:':
        voice_anomalies.append((c['origin'], c['id'], c['name'], vh))
    elif not vh and not c['has_vb']:
        voice_anomalies.append((c['origin'], c['id'], c['name'], "NO_VOICE_OR_PERSONALITY"))

print(f"\nTotal voice/personality anomalies: {len(voice_anomalies)}")
for origin, eid, name, vh in voice_anomalies:
    print(f"  [{origin}] {eid} ({name}): {vh}")

# Let's find all entries where has_lowercase_header is not empty
lowercase_entries = []
for c in all_checked:
    if c['has_lowercase_header']:
        lowercase_entries.append((c['origin'], c['id'], c['name'], c['has_lowercase_header']))

print(f"\nEntries with lowercase headers: {len(lowercase_entries)}")
for origin, eid, name, lh in lowercase_entries[:20]:
    print(f"  [{origin}] {eid} ({name}): {lh}")

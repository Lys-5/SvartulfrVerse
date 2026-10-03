import json
import re

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
chars = d.get('world_characters', [])

def parse_name(dn, fn, ln):
    # If last_name is already present and first_name has no spaces, fine
    if ln and ' ' not in fn:
        return fn, ln, []

    raw = fn if fn else dn
    titles = []
    nicknames = []

    # Strip prefixes like "Professor", "Dr.", "Coach", "Lord", "GREED -", etc.
    if raw.startswith("Lord "):
        titles.append("Lord")
        raw = raw[5:].strip()
    elif raw.startswith("Dr. "):
        titles.append("Dr.")
        raw = raw[4:].strip()
    elif raw.startswith("Professor "):
        titles.append("Professor")
        raw = raw[10:].strip()
    elif raw.startswith("Coach "):
        titles.append("Coach")
        raw = raw[6:].strip()
    elif re.match(r'^(GREED|GLUTTONY|ENVY|WRATH|PRIDE|LUST|SLOTH)\s*-\s*', raw):
        m = re.match(r'^(GREED|GLUTTONY|ENVY|WRATH|PRIDE|LUST|SLOTH)\s*-\s*(.*)', raw)
        titles.append(m.group(1))
        raw = m.group(2).strip()

    # Extract quotes like "Riki", "Sully", "Danny", "Rory"
    quote_match = re.search(r'["\']([^"\']+)["\']', raw)
    if quote_match:
        nicknames.append(quote_match.group(1))
        raw = re.sub(r'\s*["\'][^"\']+["\']\s*', ' ', raw).strip()

    parts = raw.split()
    if len(parts) == 0:
        return fn, ln, titles
    elif len(parts) == 1:
        new_fn = parts[0]
        new_ln = ""
    elif len(parts) == 2:
        new_fn = parts[0]
        new_ln = parts[1]
    elif len(parts) == 3:
        if parts[2] in ('Jr.', 'Sr.', 'III', 'IV', 'II'):
            new_fn = parts[0]
            new_ln = f"{parts[1]} {parts[2]}"
        elif parts[1] in ('Sanchez', 'van', 'de', 'von', 'la', 'del', 'da'):
            new_fn = parts[0]
            new_ln = f"{parts[1]} {parts[2]}"
        elif len(parts[1]) == 2 and parts[1].endswith('.'): # e.g. Iordan R. Vess
            new_fn = f"{parts[0]} {parts[1]}"
            new_ln = parts[2]
        else:
            new_fn = parts[0]
            new_ln = f"{parts[1]} {parts[2]}"
    else:
        new_fn = parts[0]
        new_ln = " ".join(parts[1:])

    return new_fn, new_ln, titles, nicknames

proposals = []
for c in chars:
    cid = c['id']
    dn = (c.get('display_name') or '').strip()
    fn = (c.get('first_name') or '').strip()
    ln = (c.get('last_name') or '').strip()

    if (' ' in fn and not ln) or (not fn and dn):
        res = parse_name(dn, fn, ln)
        new_fn, new_ln = res[0], res[1]
        titles = res[2] if len(res) > 2 else []
        nicks = res[3] if len(res) > 3 else []
        proposals.append((cid, dn, fn, new_fn, new_ln, titles, nicks))

print(f"Total proposals to fix: {len(proposals)}")
for cid, dn, old_fn, new_fn, new_ln, titles, nicks in proposals:
    t_str = f" | Add Titles: {titles}" if titles else ""
    n_str = f" | Add Nicks: {nicks}" if nicks else ""
    print(f"[{cid}] \"{dn}\" -> FIRST: \"{new_fn}\" | LAST: \"{new_ln}\"{t_str}{n_str}")

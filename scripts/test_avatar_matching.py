import json
import re

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
chars = d['world_characters']

gallery_titles = [
    "Kaladin", "zeera", "yael", "wulfnic", "wren", "warg", "thrakgor", "thomas", 
    "tate", "sully", "stanley", "stan", "santiago", "roland", "rev", "radek", 
    "oberon", "noah", "nixara", "nikolai", "malachia", "mac", "logan", "loewe", 
    "kian", "jasper", "jasmin", "janice", "iordan", "hank", "griven", "Goran", 
    "finn", "fenris-full", "fade", "eris", "erik", "edric", "dullahan", "dominic", 
    "danny", "chase", "brak", "barkley", "ballantine", "bailey", "aries", 
    "ariadne", "alyssa", "alistar", "alicia"
]

print(f"Total titles to match: {len(gallery_titles)}")

for gt in gallery_titles:
    gt_lower = gt.lower()
    matches = []
    for c in chars:
        cid = c['id']
        dn = c['display_name']
        fn = (c.get('first_name') or '').lower()
        ln = (c.get('last_name') or '').lower()
        nicks = [n.lower() for n in (c.get('nicknames') or [])]
        keys = [k.lower() for k in (c.get('keys') or [])]
        
        # Check matching
        matched = False
        if gt_lower == fn or gt_lower == ln:
            matched = True
        elif gt_lower in nicks:
            matched = True
        elif gt_lower in dn.lower().split():
            matched = True
        elif any(gt_lower == k for k in keys):
            matched = True
        elif gt_lower == 'warg' and 'varg' in fn:
            matched = True
        elif gt_lower == 'fenris-full' and 'fenris' in fn:
            matched = True
        elif gt_lower == 'dullahan' and ('dullahan' in dn.lower() or 'mithers' in dn.lower() or 'dullahan' in [k.lower() for k in keys]):
            matched = True
        elif gt_lower == 'thomas' and 'tomas' in fn:
            matched = True
        elif gt_lower == 'nikolai' and 'nikolaj' in fn:
            matched = True
        elif gt_lower == 'ballantine' and 'ballantine' in ln:
            matched = True
        elif gt_lower == 'aries' and 'aries' in ln:
            matched = True
        elif gt_lower == 'finn' and 'finnegan' in fn:
            matched = True
        elif gt_lower == 'alistar' and 'alastair' in fn or 'alistar' in fn or 'alister' in fn:
            matched = True
            
        if matched:
            matches.append((cid, dn, c.get('avatar')))
            
    print(f"\nTitle: '{gt}' -> {len(matches)} matches:")
    for cid, dn, curr_av in matches:
        print(f"   [{cid}] {dn} (Current avatar: {'YES' if curr_av else 'NONE'})")

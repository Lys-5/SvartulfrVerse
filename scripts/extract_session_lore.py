import json
import os
from collections import defaultdict

fpath = r'd:\SvartulfrVerse\drive\Modern-Fantasy-lorebook-export.json'
with open(fpath, 'r', encoding='utf-8') as f:
    drive_data = json.load(f)

entries = drive_data.get('entries', {})

print(f"Loaded {len(entries)} entries from Modern-Fantasy-lorebook-export.json")

# Let's inspect Team Ukiyo, DMHA, characters, locations, items, etc.
terms = ['ukiyo', 'radek', 'kian', 'goran', 'barrow', 'marek', 'dmha', 'kobal', 'ortus', 'rifugio', 'mckay', 'ironhorn', 'cylinder', 'echo core', 'sr3s', 'dimora', 'zaire', 'ershatar', 'vian', 'bryson', 'yael', 'zeera', 'wren']

matches = defaultdict(list)
for k, e in entries.items():
    comment = e.get('comment', '').strip()
    content = e.get('content', '').strip()
    keys = [x.lower() for x in e.get('key', [])]
    full_text = (comment + ' ' + ' '.join(keys) + ' ' + content).lower()
    
    for term in terms:
        if term in full_text:
            matches[term].append({
                'comment': comment,
                'keys': e.get('key', []),
                'content': content
            })

for term, items in sorted(matches.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"Term '{term:12}': {len(items):3} entries")

# Let's write a structured markdown file with all extracted details
with open('scratch/session_lore_extracted.md', 'w', encoding='utf-8') as out:
    out.write("# Session Lore Extraction: Guild, Party, NPCs, Locations, Items & Concepts\n\n")
    
    # 1. Characters & Party
    out.write("## 1. Characters & Party (Team Ukiyo & Guild Contacts)\n\n")
    char_terms = ['ukiyo', 'radek', 'kian', 'goran', 'barrow', 'marek', 'kobal', 'vargus', 'wren', 'zaire', 'amerian', 'xaiden', 'bryson']
    seen_comments = set()
    for ct in char_terms:
        out.write(f"### Tag: {ct.upper()}\n\n")
        for item in matches[ct]:
            if item['comment'] not in seen_comments:
                seen_comments.add(item['comment'])
                out.write(f"#### {item['comment']}\n")
                out.write(f"**Keys:** {', '.join(item['keys'])}\n\n")
                out.write(f"{item['content']}\n\n---\n\n")

    # 2. Locations
    out.write("## 2. Locations (Bases, Facilities, Clinics, Shops, Districts)\n\n")
    loc_terms = ['ortus', 'rifugio', 'dimora', 'mckay', 'ironhorn', 'cable district', 'black vault', 'dungeon', 'safe zone']
    for lt in loc_terms:
        out.write(f"### Location Keyword: {lt.upper()}\n\n")
        for k, e in entries.items():
            comment = e.get('comment', '').strip()
            content = e.get('content', '').strip()
            if lt in comment.lower() or lt in content.lower():
                if comment not in seen_comments:
                    seen_comments.add(comment)
                    out.write(f"#### {comment}\n")
                    out.write(f"**Keys:** {', '.join(e.get('key', []))}\n\n")
                    out.write(f"{content}\n\n---\n\n")

    # 3. Items & Artifacts
    out.write("## 3. Items & Artifacts (Gear, Weapons, Tech, Cylinders, Cores)\n\n")
    item_terms = ['cylinder', 'echo core', 'sr3s', 'medallion', 'refuge key', 'porsche', 'amulet', 'katana', 'dagger']
    for it in item_terms:
        out.write(f"### Item Keyword: {it.upper()}\n\n")
        for k, e in entries.items():
            comment = e.get('comment', '').strip()
            content = e.get('content', '').strip()
            if it in comment.lower() or it in content.lower():
                if comment not in seen_comments:
                    seen_comments.add(comment)
                    out.write(f"#### {comment}\n")
                    out.write(f"**Keys:** {', '.join(e.get('key', []))}\n\n")
                    out.write(f"{content}\n\n---\n\n")

    # 4. DMHA, Guild Rules, Contracts, & Concepts
    out.write("## 4. DMHA, Guild Mechanics, Contracts & Concepts\n\n")
    for k, e in entries.items():
        comment = e.get('comment', '').strip()
        content = e.get('content', '').strip()
        if any(w in comment.lower() or w in content.lower() for w in ['dmha', 'gilda', 'guild', 'contract', 'pact', 'loot', 'concierge']):
            if comment not in seen_comments:
                seen_comments.add(comment)
                out.write(f"#### {comment}\n")
                out.write(f"**Keys:** {', '.join(e.get('key', []))}\n\n")
                out.write(f"{content}\n\n---\n\n")

print("Detailed extraction saved to scratch/session_lore_extracted.md")

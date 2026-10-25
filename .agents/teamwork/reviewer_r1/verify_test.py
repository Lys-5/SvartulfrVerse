import re

req_sources = [
    ("Sopakco Sauce Docs", "https://sopakcosauce.gitbook.io/sopakcosauce-docs", "Canonical"),
    ("Wyvern Svart\u00falfr World Editor", "https://app.wyvern.chat/worlds/edit/_CgYT8fHXpDC4crjmegQF7", "Canonical"),
    ("io's Modern Fantasy Universe Hub", "https://io-modernfantasy.uwu.ai/", "Canonical"),
    ("Mackenzie \"Mac\" Sanchez-Rogers", "https://janitorai.com/characters/1d1ef070-934d-4c11-90e2-b7fb9a4649c4_character-mackenzie-mac-sanchez-rogers", "Canonical"),
    ("Elite Warrior Tsalu Haoitan", "https://janitorai.com/characters/1e685f63-024f-40f0-a892-a57535760b49_character-elite-warrior-tsalu-haoitan", "Canonical"),
    ("Don't Look at Me", "https://janitorai.com/characters/1ff24d14-3dfd-4795-9d49-986eeee711de_character-dont-look-at-me", "Community"),
    ("Neon Purr", "https://janitorai.com/characters/d67a12e8-a1be-4ec4-95e1-ada90263fee4_character-neon-purr-%F0%9F%87%A6%F0%9F%87%BA", "Canonical"),
    ("The Omega Breeding Facility", "https://janitorai.com/characters/c6a9088f-8b82-402c-8070-8afe22a2781e_character-the-omega-breeding-facility", "Community")
]

with open('knowledge/Lore_Worldbuilding/EXTERNAL_RESOURCES_INDEX.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract section 3.10
sec_match = re.search(r'## 3\.10 RPG & TTRPG Mechanics \(D20 / S\.P\.E\.C\.I\.A\.L\.\)(.*?)(?=\n---|# 4|\Z)', content, re.DOTALL)
if not sec_match:
    print('FAIL: Section 3.10 not found')
    exit(1)

sec_text = sec_match.group(1)

for name, url, auth in req_sources:
    if f'`{url}`' not in sec_text:
        print(f'FAIL: URL {url} not found in 3.10')
    else:
        print(f'PASS URL: {url}')

lines = [l.strip() for l in sec_text.strip().split('\n') if l.strip().startswith('|') and not l.strip().startswith('| Resource') and not l.strip().startswith('|---')]
print(f'Count of rows in 3.10: {len(lines)}')
assert len(lines) == 8, f"Expected 8 rows, got {len(lines)}"

# Check authorities
canonical_count = sum(1 for l in lines if '✅ Canonical' in l)
community_count = sum(1 for l in lines if '🔵 Community' in l)
print(f'Canonical count: {canonical_count}, Community count: {community_count}')
assert canonical_count == 6, f"Expected 6 canonical, got {canonical_count}"
assert community_count == 2, f"Expected 2 community, got {community_count}"

# Check Section 2 table
sec2_match = re.search(r'# 2\. RESOURCE STATISTICS.*?\n\| Category \|.*?\n\|(.*?)(?=\n---|# 3|\Z)', content, re.DOTALL)
sec2_text = sec2_match.group(1)
print("Section 2 content:")
print(sec2_text)
assert '| RPG & TTRPG Mechanics (D20 / S.P.E.C.I.A.L.) | 8 | 6 | 2 | 0 |' in sec2_text
assert '| **TOTAL** | **77** | **27** | **50** | **0** |' in sec2_text

print("ALL ASSERTS PASSED!")

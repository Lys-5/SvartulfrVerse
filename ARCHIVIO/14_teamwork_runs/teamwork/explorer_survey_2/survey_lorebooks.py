import json

lorebooks = {
    'Lore_I': 'FINAL/Svartulfr_Lorebook_I.json',
    'Lore_II': 'FINAL/Svartulfr_Lorebook_II.json',
    'Lore_III': 'FINAL/Svartulfr_Lorebook_III.json',
    'Location': 'lorebooks/optimized/Svartulfr_Location.json',
    'NPC_Primary': 'FINAL/Svartulfr_NPC_Primary.json',
    'NPC_Secondary': 'FINAL/Svartulfr_NPC_Secondary.json'
}

search_terms = [
    'brugge', 'revazhael', 'crystall', 'cristall', 'cylinder', 'cilindr',
    'abyss', 'abiss', 'void', 'vuoto', 'necroman', 'narghaton', 'kaladin',
    'warg', 'adelin', 'barkley', 'santiago', 'bailey', 'roxy', 'grave mistake',
    'alyssa', 'jasper'
]

results = []
for lb_name, path in lorebooks.items():
    with open(path, 'r', encoding='utf-8') as f:
        d = json.load(f)
    entries = d.get('entries', [])
    for idx, e in enumerate(entries):
        name = e.get('name', '')
        keys = e.get('keys', [])
        content = e.get('content', '')
        text_to_search = (name + ' ' + ' '.join(keys) + ' ' + content).lower()
        matched = [term for term in search_terms if term in text_to_search]
        if matched:
            results.append((lb_name, idx, e.get('entry_id') or e.get('id'), name, e.get('type'), matched, keys[:3]))

with open('e:/repository/SvartulfrVerse/.agents/teamwork/explorer_survey_2/lorebook_search_results.txt', 'w', encoding='utf-8') as out:
    out.write(f'Total matched entries: {len(results)}\n')
    for r in results:
        out.write(f'[{r[0]}] #{r[1]} id={r[2]} name="{r[3]}" type={r[4]} matches={r[5]} keys={r[6]}\n')

print(f'Wrote {len(results)} matches to lorebook_search_results.txt')

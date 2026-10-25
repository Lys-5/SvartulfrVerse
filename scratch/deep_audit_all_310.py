import json, re

for path in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    lex = data['lexicon']
    print(f'================ {path} ({len(lex)} entries) ================')
    double_dots = 0
    double_quotes = 0
    they_singular_verb = 0
    jan1_births = 0
    truncated_traits = 0
    missing_4blocks = 0
    for e in lex:
        c = e['content']
        if '..' in c and '...' not in c.replace('..', ''):
            # check actual '..' not '...'
            if re.search(r'(?<!\.)\.\.(?!\.)', c):
                double_dots += 1
        if '""' in c:
            double_quotes += 1
        if re.search(r'\bthey\s+(withdraws|is|has|wants|needs|keeps|avoids|tends|struggles|hides|speaks|carries|prefers|acts|gets|makes|takes|feels|looks|seems)\b', c, re.I):
            they_singular_verb += 1
        if 'January 1,' in c or '1 January' in c:
            jan1_births += 1
        for line in c.splitlines():
            if line.startswith('- ') and not line.strip().endswith(('.', ')', ']', '"')):
                truncated_traits += 1
                break
        has_b = 'BACKSTORY:' in c
        has_f = ('FAMILY & PACK:' in c) or ('CLAN AND COMPANY:' in c)
        has_v = 'VOICE & BEHAVIOR:' in c
        if not (has_b and has_f and has_v):
            missing_4blocks += 1
    print(f'  Double dots (..): {double_dots}')
    print(f'  Double quotes (""): {double_quotes}')
    print(f'  "they <singular verb>" grammar bugs: {they_singular_verb}')
    print(f'  Born January 1: {jan1_births}')
    print(f'  Truncated trait lines: {truncated_traits}')
    print(f'  Missing canonical 4-block headers: {missing_4blocks}')

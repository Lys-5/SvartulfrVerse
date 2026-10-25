import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'

scen = json.loads((FINAL / 'Svartulfr_Master_Scenario.json').read_text(encoding='utf-8'))

print("=== MASTER SCENARIO PROMPT ===")
print(scen['scenario'])
print("\n=== CHECKING ALL 29 GREETINGS ===")

english_words = re.compile(r'\b(the|and|with|from|into|behind|through|across|while|his|her|their|you|your|they|were|was|had|have|would|could|should)\b', re.I)
ascii_accents = re.compile(r"\b[a-zA-Z]+(?:piu|perche|poiche|anziche|affinche|cosi|gia|puo|pero|cio|li|la|ne|se|te|me|caffe|universita|citta|realta|verita|liberta|attivita|capacita|possibilita|difficolta|qualita|quantita|novita| opportunita|curiosita|eternita|umanita|autorita|identita|comunita|responsabilita|velocita|oscurita|volonta|falo|papa)'", re.I)

valid_slots = {s['key'] for s in scen['slots']}

for idx, g in enumerate(scen['greetings'], 1):
    name = g.get('name', '')
    desc = g.get('description', '')
    content = g.get('content', '')
    s_slot = g.get('speaker_slot')
    l_pids = g.get('linked_persona_ids', [])
    msgs = g.get('messages', [])
    
    issues = []
    if not name.startswith(f"{idx:02d}. "):
        issues.append(f"name does not start with {idx:02d}. : {name}")
    if '*' in name or '*' in desc or '*' in content:
        issues.append("asterisk in name/desc/content")
    if '—' in name or '—' in desc or '—' in content:
        issues.append("em-dash in name/desc/content")
    if not msgs:
        issues.append("empty messages[]")
    else:
        if content != msgs[0].get('content'):
            issues.append("content != messages[0].content")
        if s_slot != msgs[0].get('speaker_slot'):
            issues.append(f"speaker_slot ({s_slot}) != messages[0].speaker_slot ({msgs[0].get('speaker_slot')})")
        for m_i, m in enumerate(msgs):
            ms = m.get('speaker_slot')
            mc = m.get('content', '')
            if ms is not None and ms not in valid_slots:
                issues.append(f"msg[{m_i}] invalid speaker_slot: {ms}")
            if '*' in mc:
                issues.append(f"msg[{m_i}] has '*'")
            if '—' in mc:
                issues.append(f"msg[{m_i}] has '—'")
            # check ascii accents
            acc_hits = ascii_accents.findall(mc)
            if acc_hits:
                issues.append(f"msg[{m_i}] ascii accents: {acc_hits}")
            # check English sentences (more than 4 common English words in a single message)
            eng_hits = english_words.findall(mc)
            # Filter out known proper nouns/titles like "The Verve", "The Docks", "The Sinners", "The Deep Ward", "The Drowned Bell", "You Belong With Me"
            cleaned_mc = re.sub(r'(The Verve|The Docks|The Sinners|The Deep Ward|The Drowned Bell|The Five Cocketeers|The Pack|You Belong With Me|Into the Mystic|The Other Side)', '', mc)
            eng_hits2 = [w for w in english_words.findall(cleaned_mc) if w.lower() not in ('and',)]
            if len(eng_hits2) >= 3:
                issues.append(f"msg[{m_i}] possible English words: {eng_hits2}")
            # Check anti-ventriloquism: does {{user}} speak or have quotes attributed?
            if re.search(r'\{\{user\}\}[^.\n]{0,30}"', mc) or re.search(r'"[^"]*"[^.\n]{0,30}\{\{user\}\}', mc):
                issues.append(f"msg[{m_i}] possible {{user}} dialogue adjacent to quotes")
    # Check POV vs linked_persona_ids
    if '[FemPOV]' in name and l_pids != ['persona_1786335754946']:
        issues.append(f"[FemPOV] has wrong linked_persona_ids: {l_pids}")
    elif '[MalePOV]' in name and l_pids != ['1792155173728']:
        issues.append(f"[MalePOV] has wrong linked_persona_ids: {l_pids}")
    elif '[FemPOV]' not in name and '[MalePOV]' not in name and l_pids != []:
        issues.append(f"Dual POV has non-empty linked_persona_ids: {l_pids}")

    msg_slots = [m.get('speaker_slot') for m in msgs]
    print(f"[{idx:02d}] {name} | pids={l_pids} | msg_slots={msg_slots} | issues={issues}")

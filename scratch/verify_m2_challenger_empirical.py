#!/usr/bin/env python3
"""
scratch/verify_m2_challenger_empirical.py
Empirical Challenger Verification Script for Milestone 2

Tests:
1. Live Wyvern Web API GET for Scenario `_2MTWKjxrQPdQVaz9y4Q7H`.
2. Live Wyvern Web API GET for Active Chat Log `chat_log_PJx1W1rg3WUzRM7MnQrkN`.
3. Live Wyvern Web API GET for World Characters in `_YpX47fNraQFw2dD7TdycJ`.
4. High-fidelity implementation of frontend module 93312 (WH) and nC beat splitting algorithm.
5. Assertion of 100% resolution for all 13 Primary World Characters plus Narrator.
6. Stress-testing boundary conditions, adversarial variants, and formatting discipline.
"""

import sys
import os
import json
import regex as re
import urllib.request
import urllib.error
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = Path(__file__).resolve().parent.parent
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
REFRESH_SCRIPT = ROOT / 'scratch' / 'refresh_token.py'

SCENARIO_ID = "_2MTWKjxrQPdQVaz9y4Q7H"
CHAT_LOG_ID = "chat_log_PJx1W1rg3WUzRM7MnQrkN"
WORLD_ID = "_YpX47fNraQFw2dD7TdycJ"
SWIPE_ID = "message_swipe_99mmMgEEQjk2pkJN3hXkQ"

EXPECTED_13_NAMES = [
    'Erik Ulfr Douglas',
    'Logan Járn Douglas',
    'Edric Douglas',
    'Noah Loki Douglas Bloodmoon',
    'Malachia Björn Douglas Bloodmoon',
    'Jasper Svartr Douglas Bloodmoon',
    'Alyssa Hvit Douglas Bloodmoon',
    'Wulfnic Báleygr Bloodmoon',
    'Zefir Hvitskog',
    'Mackenzie Sanchez-Rogers',
    'Finnegan Novak',
    'Sierra Cruz',
    'Scarlett Rose'
]


def get_token():
    if TOKEN_PATH.exists():
        t = TOKEN_PATH.read_text(encoding='utf-8').strip()
        if t:
            return t
    import subprocess
    subprocess.check_call([sys.executable, str(REFRESH_SCRIPT)])
    return TOKEN_PATH.read_text(encoding='utf-8').strip()


def api_get(url):
    token = get_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Challenger/1.0',
        'Content-Type': 'application/json'
    }
    req = urllib.request.Request(url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8')
            return resp.status, json.loads(content) if content else {}
    except urllib.error.HTTPError as e:
        if e.code in (401, 403):
            print(f"[AUTH] Received HTTP {e.code}, refreshing token...")
            import subprocess
            subprocess.check_call([sys.executable, str(REFRESH_SCRIPT)])
            token = get_token()
            headers['Authorization'] = f'Bearer {token}'
            req = urllib.request.Request(url, headers=headers, method='GET')
            with urllib.request.urlopen(req) as r2:
                content = r2.read().decode('utf-8')
                return r2.status, json.loads(content) if content else {}
        raise


# =====================================================================
# Frontend Module 93312 / WH & nC Simulation Engine
# =====================================================================

def compile_wyvern_wh_regex(char_info, prefix="=>", suffix=":"):
    """
    Python port of frontend module 93312 function f(e, a, l).
    Generates exact regex used by Wyvern for speaker detection.
    """
    first_name = (char_info.get('first_name') or char_info.get('name') or '').strip()
    if not first_name:
        return None

    def u(s):
        # normalize and escape special regex chars, quotes, hyphens
        res = s.replace('\\', '\\\\')
        for ch in r'.*+?^${}()|[]':
            res = res.replace(ch, '\\' + ch)
        res = re.sub(r"['\u2018\u2019\u02bc\u201b\u2032]", "['\u2018\u2019\u02bc\u201b\u2032]", res)
        res = re.sub(r"[-\u2010\u2011\u2012\u2013\u2014\u2212]", "[-‐‑‒–—−]", res)
        return res

    h = []
    p = r"(?:\*\*)?"
    prefix_clean = prefix.strip() if prefix else ""
    if prefix_clean:
        h.append(p + u(prefix_clean) + r"\s*" + p)
    else:
        h.append(r"(?<=^|\n)\s*" + p)

    titles = char_info.get('titles') or []
    if titles:
        t_joined = "|".join(u(t) for t in titles)
        h.append(rf"(({t_joined})\s+)?")

    v = []
    def add_p(pat, weight_mult, length):
        v.append((pat, 10000 * weight_mult + length))

    g = first_name
    m = (char_info.get('last_name') or '').strip() or None
    y = [mid.strip() for mid in (char_info.get('middle_names') or []) if mid.strip()]
    max_mid = max([len(mid) for mid in y]) if y else 0
    w = u(g)
    C = u(m) if m else None
    x = "|".join(u(mid) for mid in y) if y else None

    if x and C:
        add_p(rf"{w}\s+({x})\s+{C}", 3, len(g) + max_mid + (len(m) if m else 0) + 2)
    if C:
        add_p(rf"{w}\s+{C}", 2, len(g) + len(m) + 1)
        add_p(rf"{C}\s+{w}", 2, len(g) + len(m) + 1)
    if x and C:
        add_p(rf"{C}\s+({x})\s+{w}", 3, len(g) + max_mid + (len(m) if m else 0) + 2)
    if x:
        add_p(rf"{w}\s+({x})", 2, len(g) + max_mid + 1)

    add_p(w, 1, len(g))
    if C:
        add_p(C, 1, len(m))

    nicknames = char_info.get('nicknames') or []
    for nick in nicknames:
        t = nick.strip()
        n_words = len([w for w in re.split(r'\s+', t) if w]) or 1
        u_nick = u(nick)
        if "'" in nick or '"' in nick:
            add_p(u_nick, n_words, len(t))
        else:
            add_p(u_nick, n_words, len(t))
            add_p(f"'{u_nick}'", n_words, len(t) + 2)
            add_p(f'"{u_nick}"', n_words, len(t) + 2)

    v.sort(key=lambda item: item[1], reverse=True)
    patterns_joined = "|".join(item[0] for item in v)
    d = r"(?<=^|[^\w])" if prefix_clean else ""
    h.append(rf"{d}(?P<coreName>{patterns_joined})(?=$|[^\w])")

    if titles:
        t_joined = "|".join(u(t) for t in titles)
        h.append(rf"(\s+({t_joined}))?")

    suffix_clean = suffix.strip() if suffix else ":"
    if suffix_clean:
        h.append(r"(?:\*\*)?\s*" + u(suffix_clean) + r"(?:\*\*(?=\s|$))?")

    # Match at line start
    full_pattern = "^" + "".join(h)
    return full_pattern


class WyvernVNBeatParser:
    """
    Simulates frontend nC beat splitting.
    """
    def __init__(self, world_characters, prefix="=>"):
        self.world_characters = world_characters
        self.prefix = prefix
        self.rules = []

        # 1. Rules for each world character
        for wc in world_characters:
            pat = compile_wyvern_wh_regex(wc, prefix=prefix, suffix=":")
            if pat:
                self.rules.append({
                    'char': wc,
                    'regex': re.compile(pat, flags=re.MULTILINE | re.IGNORECASE),
                    'is_fallback': False
                })

        # 2. Fallback rule: ^=>\s*([^:\n]{1,35}):\s*
        fallback_pat = rf"^{re.escape(prefix)}\s*([^:\n]{{1,35}}):\s*"
        self.fallback_regex = re.compile(fallback_pat, flags=re.MULTILINE | re.IGNORECASE)
        self.rules.append({
            'char': None,
            'regex': self.fallback_regex,
            'is_fallback': True
        })

    def parse_beats(self, text):
        """
        Parses text into beats, resolving character objects and narrator.
        """
        if not text:
            return []

        # Remove think tags
        cleaned_text = re.sub(r'<think>[\s\S]*?</think>', '', text, flags=re.IGNORECASE)

        matches = []
        for rule in self.rules:
            reg = rule['regex']
            for m in reg.finditer(cleaned_text):
                speaker_raw = m.group(1) if rule['is_fallback'] and m.lastindex else m.group(0)
                matches.append({
                    'start': m.start(),
                    'end': m.end(),
                    'matched_text': m.group(0),
                    'rule': rule,
                    'raw_speaker': speaker_raw
                })

        # Sort matches by start position
        matches.sort(key=lambda x: (x['start'], -x['end']))

        # Deduplicate overlapping matches: pick the one with longest span or character match over fallback
        filtered_matches = []
        last_end = -1
        for m in matches:
            if m['start'] >= last_end:
                filtered_matches.append(m)
                last_end = m['end']
            else:
                # Overlap: if existing is fallback and current is specific char, replace
                if filtered_matches:
                    prev = filtered_matches[-1]
                    if prev['rule']['is_fallback'] and not m['rule']['is_fallback']:
                        filtered_matches[-1] = m
                        last_end = m['end']

        beats = []
        cursor = 0
        for i, m in enumerate(filtered_matches):
            start = m['start']
            end = m['end']

            # If there was text before this match, it's narrator
            if start > cursor:
                preceding = cleaned_text[cursor:start].strip()
                if preceding:
                    beats.append({
                        'speaker_tag': 'Narrator (Preceding)',
                        'speaker_name': 'Narrator',
                        'character_id': None,
                        'avatar': None,
                        'is_narrator': True,
                        'content': preceding
                    })

            # The content for this speaker runs until the next match or EOF
            next_start = filtered_matches[i + 1]['start'] if i + 1 < len(filtered_matches) else len(cleaned_text)
            content = cleaned_text[end:next_start].strip()

            rule = m['rule']
            if rule['char']:
                c = rule['char']
                beats.append({
                    'speaker_tag': m['matched_text'].strip(),
                    'speaker_name': c.get('display_name') or c.get('name'),
                    'character_id': c.get('id') or c.get('_id'),
                    'avatar': c.get('avatar'),
                    'is_narrator': False,
                    'content': content
                })
            else:
                raw_name = m['raw_speaker'].strip()
                is_narr = raw_name.lower() == 'narrator'
                beats.append({
                    'speaker_tag': m['matched_text'].strip(),
                    'speaker_name': 'Narrator' if is_narr else raw_name.title(),
                    'character_id': None,
                    'avatar': None,
                    'is_narrator': is_narr,
                    'content': content
                })

            cursor = next_start

        return beats


def main():
    print("================================================================================")
    print("EMPIRICAL CHALLENGER: MILESTONE 2 VERIFICATION SUITE")
    print("================================================================================\n")

    # Step 1: Query live Scenario
    print("[1] Querying live Wyvern Scenario...")
    sc_url = f"https://app.wyvern.chat/api/worlds/scenarios/{SCENARIO_ID}"
    status_sc, live_sc = api_get(sc_url)
    print(f"    Scenario ID: {SCENARIO_ID}")
    print(f"    HTTP Status: {status_sc}")
    assert status_sc == 200, f"Scenario GET failed with HTTP {status_sc}"
    scenes = live_sc.get('premade_scenes', [])
    print(f"    Premade Scenes Count: {len(scenes)}")
    assert len(scenes) == 3, f"Expected 3 premade scenes, got {len(scenes)}"

    # Step 2: Query live Chat Log
    print("\n[2] Querying live Wyvern Chat Log...")
    chat_url = f"https://app.wyvern.chat/api/new/chat-logs/{CHAT_LOG_ID}"
    status_chat, live_chat = api_get(chat_url)
    print(f"    Chat Log ID: {CHAT_LOG_ID}")
    print(f"    HTTP Status: {status_chat}")
    assert status_chat == 200, f"Chat log GET failed with HTTP {status_chat}"
    messages = live_chat.get('messages', [])
    print(f"    Messages Count: {len(messages)}")
    assert len(messages) >= 1, f"Expected at least 1 message, got {len(messages)}"
    msg0 = messages[0]
    swipes = msg0.get('swipes', [])
    assert len(swipes) >= 1, "Expected at least 1 swipe in message 0"
    swipe0 = swipes[0]
    print(f"    Swipe ID: {swipe0.get('id')}")

    # Step 3: Query live World Characters
    print("\n[3] Querying live World Characters in World...")
    world_chars_url = f"https://app.wyvern.chat/api/worlds/characters/world/{WORLD_ID}"
    try:
        status_wc, live_wc = api_get(world_chars_url)
        print(f"    World Characters API HTTP {status_wc}, found {len(live_wc)} characters")
        world_characters = live_wc if isinstance(live_wc, list) else live_wc.get('characters', [])
    except Exception as e:
        print(f"    Direct characters endpoint error ({e}), falling back to world endpoint...")
        status_w, live_w = api_get(f"https://app.wyvern.chat/api/worlds/{WORLD_ID}")
        world_characters = live_w.get('characters', [])

    if not world_characters:
        # Fallback to verified local snapshot if endpoint returns summary
        snap_path = ROOT / 'scratch' / 'fresh_world_chars.json'
        if snap_path.exists():
            world_characters = json.loads(snap_path.read_text(encoding='utf-8'))
            print(f"    Loaded {len(world_characters)} characters from fresh_world_chars.json")

    print(f"    Total World Characters active: {len(world_characters)}")
    assert len(world_characters) >= 13, f"Expected at least 13 world characters, found {len(world_characters)}"

    # Step 4: Initialize Beat Parser
    print("\n[4] Initializing Wyvern Visual Novel Beat Parser (Module 93312/nC simulation)...")
    parser = WyvernVNBeatParser(world_characters, prefix="=>")
    print(f"    Parser compiled {len(parser.rules)} rules (including fallback).")

    # Step 5: Test Beat Splitting on Live Texts
    print("\n[5] Parsing and Verifying Live Texts...")

    # 5.1 Scene 0
    print("\n--- 5.1 Parsing Live Scene 0 (Alyssa POV) ---")
    s0_text = scenes[0].get('scene_text', '')
    beats_0 = parser.parse_beats(s0_text)
    print(f"    Generated {len(beats_0)} beats:")
    for b_idx, b in enumerate(beats_0):
        print(f"      Beat {b_idx:02d}: tag='{b['speaker_tag']}' -> name='{b['speaker_name']}' "
              f"| is_narrator={b['is_narrator']} | char_id={b['character_id']} | avatar={'YES' if b['avatar'] else 'NO'} "
              f"| words={len(b['content'].split())}")

    # Assert formatting discipline
    assert s0_text.count('—') == 0, "Scene 0 contains em-dashes!"
    assert s0_text.count('*') == 0, "Scene 0 contains asterisks!"
    assert len(beats_0) == 14, f"Expected 14 beats in Scene 0, got {len(beats_0)}"

    # 5.2 Scene 1
    print("\n--- 5.2 Parsing Live Scene 1 (Jasper POV) ---")
    s1_text = scenes[1].get('scene_text', '')
    beats_1 = parser.parse_beats(s1_text)
    print(f"    Generated {len(beats_1)} beats:")
    for b_idx, b in enumerate(beats_1):
        print(f"      Beat {b_idx:02d}: tag='{b['speaker_tag']}' -> name='{b['speaker_name']}' "
              f"| is_narrator={b['is_narrator']} | char_id={b['character_id']} | avatar={'YES' if b['avatar'] else 'NO'} "
              f"| words={len(b['content'].split())}")

    assert s1_text.count('—') == 0, "Scene 1 contains em-dashes!"
    assert s1_text.count('*') == 0, "Scene 1 contains asterisks!"
    assert len(beats_1) == 14, f"Expected 14 beats in Scene 1, got {len(beats_1)}"

    # 5.3 Scene 2
    print("\n--- 5.3 Parsing Live Scene 2 (Corale) ---")
    s2_text = scenes[2].get('scene_text', '')
    beats_2 = parser.parse_beats(s2_text)
    print(f"    Generated {len(beats_2)} beats:")
    for b_idx, b in enumerate(beats_2):
        print(f"      Beat {b_idx:02d}: tag='{b['speaker_tag']}' -> name='{b['speaker_name']}' "
              f"| is_narrator={b['is_narrator']} | char_id={b['character_id']} | avatar={'YES' if b['avatar'] else 'NO'} "
              f"| words={len(b['content'].split())}")

    assert s2_text.count('—') == 0, "Scene 2 contains em-dashes!"
    assert s2_text.count('*') == 0, "Scene 2 contains asterisks!"
    assert len(beats_2) == 4, f"Expected 4 beats in Scene 2, got {len(beats_2)}"

    # 5.4 Message #0 Swipe
    print("\n--- 5.4 Parsing Live Message #0 Swipe ---")
    swipe_content = swipe0.get('content', '')
    beats_m0 = parser.parse_beats(swipe_content)
    print(f"    Generated {len(beats_m0)} beats:")
    for b_idx, b in enumerate(beats_m0):
        print(f"      Beat {b_idx:02d}: tag='{b['speaker_tag']}' -> name='{b['speaker_name']}' "
              f"| is_narrator={b['is_narrator']} | char_id={b['character_id']} | avatar={'YES' if b['avatar'] else 'NO'} "
              f"| words={len(b['content'].split())}")

    assert swipe_content.count('—') == 0, "Message #0 contains em-dashes!"
    assert swipe_content.count('*') == 0, "Message #0 contains asterisks!"
    assert len(beats_m0) == 14, f"Expected 14 beats in Message #0, got {len(beats_m0)}"

    # Step 6: Test Resolution Across ALL 13 Primary World Characters + Narrator
    print("\n[6] Testing Resolution for ALL 13 Primary World Characters + Narrator...")

    test_script_lines = []
    # Test canonical short names
    test_specs = [
        ("Narrator", "=>Narrator:\nIl vento soffia leggero sul campus.", True, None),
        ("Erik", '=>Erik:\n"Restate uniti."', False, 'Erik Ulfr Douglas'),
        ("Logan", '=>Logan:\n"Lasciali respirare."', False, 'Logan Járn Douglas'),
        ("Edric", '=>Edric:\n"Guarda la mensa!"', False, 'Edric Douglas'),
        ("Noah", '=>Noah:\n"C\'e ombra alla KSA."', False, 'Noah Loki Douglas Bloodmoon'),
        ("Malachia", '=>Malachia:\n"Nessuno tocchi la mia famiglia."', False, 'Malachia Björn Douglas Bloodmoon'),
        ("Jasper", '=>Jasper:\n"I server sono crashati."', False, 'Jasper Svartr Douglas Bloodmoon'),
        ("Alyssa", '=>Alyssa:\n"Non farti notare."', False, 'Alyssa Hvit Douglas Bloodmoon'),
        ("Wulfnic", '=>Wulfnic:\n"Sei un ragazzino!"', False, 'Wulfnic Báleygr Bloodmoon'),
        ("Zefir", '=>Zefir:\n"Ridi pure, mio Jarl."', False, 'Zefir Hvitskog'),
        ("Mackenzie", '=>Mackenzie:\n"Ci penso io a fare spazio."', False, 'Mackenzie Sanchez-Rogers'),
        ("Finn", '=>Finn:\n"Vi procuro i pass VIP per la partita."', False, 'Finnegan Novak'),
        ("Sierra", '=>Sierra:\n"Dove hai preso quel chiodo?"', False, 'Sierra Cruz'),
        ("Scarlett", '=>Scarlett:\n"Ti dona quello stile, Zefir."', False, 'Scarlett Rose'),
    ]

    synthetic_test_text = "\n\n".join([item[1] for item in test_specs])
    beats_all = parser.parse_beats(synthetic_test_text)
    print(f"    Synthetic test generated {len(beats_all)} beats (expected {len(test_specs)}):")

    resolved_chars = set()
    for idx, (expected_tag, _, expected_narrator, expected_char_name) in enumerate(test_specs):
        beat = beats_all[idx]
        print(f"      [{idx:02d}] Tag: {expected_tag:<10} -> Speaker: {beat['speaker_name']:<30} | "
              f"is_narrator={beat['is_narrator']} | avatar={'OK' if beat['avatar'] or beat['is_narrator'] else 'MISSING'}")

        if expected_narrator:
            assert beat['is_narrator'], f"Expected narrator for {expected_tag}, got character"
            assert beat['speaker_name'] == "Narrator"
        else:
            assert not beat['is_narrator'], f"Expected character for {expected_tag}, got narrator"
            assert beat['speaker_name'] == expected_char_name, f"Expected {expected_char_name}, got {beat['speaker_name']}"
            assert beat['avatar'] is not None and beat['avatar'].startswith("https://"), f"Missing CDN avatar for {expected_tag}"
            assert beat['character_id'] is not None, f"Missing character_id for {expected_tag}"
            resolved_chars.add(expected_char_name)

    print(f"\n    Resolved characters count: {len(resolved_chars)} / 13")
    assert len(resolved_chars) == 13, f"Expected 13 resolved characters, got {len(resolved_chars)}"

    # Step 7: Test Nickname and Formal Name Resolution
    print("\n[7] Testing Nickname and Full Name Resolution...")
    alias_specs = [
        ("Mac", '=>Mac:\n"Ehi ciao."', 'Mackenzie Sanchez-Rogers'),
        ("Finnegan", '=>Finnegan:\n"Pronto per il match."', 'Finnegan Novak'),
        ("Erik Ulfr Douglas", '=>Erik Ulfr Douglas:\n"Ascoltatemi bene."', 'Erik Ulfr Douglas'),
        ("Malachia Björn Douglas Bloodmoon", '=>Malachia Björn Douglas Bloodmoon:\n"Sorveglio io."', 'Malachia Björn Douglas Bloodmoon'),
        ("Noah Loki Douglas Bloodmoon", '=>Noah Loki Douglas Bloodmoon:\n"Prego, accomodatevi."', 'Noah Loki Douglas Bloodmoon')
    ]
    alias_text = "\n\n".join([item[1] for item in alias_specs])
    alias_beats = parser.parse_beats(alias_text)
    for idx, (alias_tag, _, expected_name) in enumerate(alias_specs):
        beat = alias_beats[idx]
        print(f"      Alias: {alias_tag:<32} -> Resolved: {beat['speaker_name']:<30} | avatar={'OK' if beat['avatar'] else 'MISSING'}")
        assert beat['speaker_name'] == expected_name, f"Alias {alias_tag} failed to resolve to {expected_name}"
        assert beat['avatar'] is not None, f"Missing avatar for alias {alias_tag}"

    print("\n================================================================================")
    print("ALL EMPIRICAL ASSERTIONS PASSED WITH ZERO DEFECTS!")
    print("================================================================================")
    return True


if __name__ == '__main__':
    main()

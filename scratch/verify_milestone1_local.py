import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
OPT_DIR = ROOT / 'lorebooks' / 'optimized'

DCC_PLACEHOLDER = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/99d10d9b-611c-45b7-566a-79c3ed2e9800/public"
OLD_FALLBACK = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public"
HOUSE_EMBLEM_COVER = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public"
BROAD_KEYS = {'solarton', 'succ', 'blackwood', 'vampire', 'werewolf', 'college', 'student', 'alpha', 'omega'}

CORE_PRIMARY = {
    'C-JisFj8qA1tsFEqZKevk': ('Erik Ulfr Douglas', 22775, '_QPea6g4Q1QfeYCVHCLMPR', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/61648731-7c96-454d-95e5-e27aa69d8c00/public'),
    'jDuJtzirlEZC3K_ArIufh': ('Malachia Björn Douglas Bloodmoon', 18520, '_RDfz7XzTpM23LpPALVXHM', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/d77a20fc-49da-4f35-a311-1539ef698d00/public'),
    'H2JX-NkHRiJ2FzoekC5ZZ': ('Noah Loki Douglas Bloodmoon', 10398, '_zFLUjV8aVxQRAfQxGcAcY', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/968cc93e-879d-4aab-94b7-3838f94a9e00/public'),
    'tAcrWLtWSDGf3xJJRwUOM': ('Logan Járn Douglas', 13735, '_T8Ywcr9FEqNf9JxbK6eHP', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/0b5a932b-0a3b-4e0b-8257-49f18fedae00/public'),
    'HhuMluMmIIENUei3bX6ed': ('Wulfnic Báleygr Bloodmoon', 14530, '_HEQQbbRFwKdG8QE2Fh1z1', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/683beb87-8091-4b5a-e6fd-8acb0a159500/public'),
    'BXi3sENAVYB8OKF80Q9Su': ('Mackenzie Sanchez-Rogers', 9618, '_zn24784jfcchQ7EwCyAnm', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/87f28fb6-557f-4eaf-9c7c-0cddfbe5c300/public')
}

CORE_SECONDARY = {
    'h-ttmlgJYeRXqyDvQjSX7': ('Edric Douglas', 7240, '_TbRM3EdxDjHFgqztTbCpL', 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/ed348ea6-c40c-461c-f90e-d09e742c3400/public')
}

def verify():
    errors = []
    
    # 1. Load files
    with open(FINAL_DIR / 'Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
        prim = json.load(f)
    with open(FINAL_DIR / 'Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
        sec = json.load(f)
        
    with open(OPT_DIR / 'Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
        opt_prim = json.load(f)
    with open(OPT_DIR / 'Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
        opt_sec = json.load(f)

    print("=== 1. Checking Top-Level Metadata ===")
    if prim.get('photoURL') != HOUSE_EMBLEM_COVER:
        errors.append(f"Primary photoURL mismatch: {prim.get('photoURL')}")
    if sec.get('photoURL') != HOUSE_EMBLEM_COVER:
        errors.append(f"Secondary photoURL mismatch: {sec.get('photoURL')}")
    if prim.get('token_budget') != 7500:
        errors.append(f"Primary token_budget mismatch: {prim.get('token_budget')} (expected 7500)")
    if sec.get('token_budget') != 5000:
        errors.append(f"Secondary token_budget mismatch: {sec.get('token_budget')} (expected 5000)")

    print(f"Primary token_budget={prim.get('token_budget')}, photoURL={prim.get('photoURL')}")
    print(f"Secondary token_budget={sec.get('token_budget')}, photoURL={sec.get('photoURL')}")

    print("\n=== 2. Checking Entries vs Lexicon Parity ===")
    if len(prim['entries']) != 99 or len(prim['lexicon']) != 99:
        errors.append(f"Primary entry counts mismatch: entries={len(prim['entries'])}, lexicon={len(prim['lexicon'])}")
    if len(sec['entries']) != 211 or len(sec['lexicon']) != 211:
        errors.append(f"Secondary entry counts mismatch: entries={len(sec['entries'])}, lexicon={len(sec['lexicon'])}")

    # Check mirror parity
    if prim != opt_prim:
        errors.append("FINAL/Svartulfr_NPC_Primary.json != lorebooks/optimized/Svartulfr_NPC_Primary.json")
    if sec != opt_sec:
        errors.append("FINAL/Svartulfr_NPC_Secondary.json != lorebooks/optimized/Svartulfr_NPC_Secondary.json")

    print(f"Primary parity verified: 99/99, Secondary parity verified: 211/211. Mirror files identical: {prim == opt_prim and sec == opt_sec}")

    all_entries = []
    for label, lb in [('Primary', prim), ('Secondary', sec)]:
        for arr_name in ['entries', 'lexicon']:
            for idx, e in enumerate(lb[arr_name]):
                all_entries.append((label, arr_name, idx, e))

    print(f"\n=== 3. Auditing 310 Entries (across both entries and lexicon) ===")
    bracket_starts = 0
    non_bracket_starts = []
    em_dash_count = 0
    asterisk_count = 0
    age_macro_count = 0
    broad_key_count = 0
    recursion_not_true = 0
    dcc_placeholder_count = 0
    custom_portrait_count = 0
    old_fallback_count = 0
    invalid_avatar_count = 0
    voice_and_behavior_count = 0

    # We evaluate unique entries across lexicon
    unique_entries = prim['lexicon'] + sec['lexicon']
    print(f"Total unique entries to audit: {len(unique_entries)}")

    for e in unique_entries:
        content = e.get('content', '')
        eid = e.get('entry_id')
        name = e.get('name')
        
        # Bracket start
        if content.strip().startswith('['):
            bracket_starts += 1
        else:
            non_bracket_starts.append((eid, name, content[:50]))
            
        # Em-dashes
        if '\u2014' in content:
            em_dash_count += 1
        # Asterisks
        if '*' in content:
            asterisk_count += 1
        # Age macros
        if '{{age' in content.lower():
            age_macro_count += 1
            
        # Broad trigger keys
        keys = e.get('keys', [])
        for k in keys:
            if k.lower().strip() in BROAD_KEYS:
                broad_key_count += 1
                errors.append(f"Entry {name} ({eid}) has broad trigger key: {k}")
                
        # Exclude from recursion
        if e.get('exclude_from_recursion') is not True:
            recursion_not_true += 1
            
        # Voice and behavior
        if 'VOICE AND BEHAVIOR:' in content:
            voice_and_behavior_count += 1
            errors.append(f"Entry {name} ({eid}) has unnormalized 'VOICE AND BEHAVIOR:'")

        # Avatars
        av = e.get('avatar', '')
        if not av or not av.startswith('https://'):
            invalid_avatar_count += 1
        if av == DCC_PLACEHOLDER:
            dcc_placeholder_count += 1
        elif av == OLD_FALLBACK:
            old_fallback_count += 1
        else:
            custom_portrait_count += 1

    print(f"Bracket starts: {bracket_starts} / 310 (non-bracket: {len(non_bracket_starts)})")
    print(f"Em-dashes: {em_dash_count}")
    print(f"Asterisks: {asterisk_count}")
    print(f"Age macros: {age_macro_count}")
    print(f"Broad keys in trigger keys: {broad_key_count}")
    print(f"Entries without exclude_from_recursion=True: {recursion_not_true}")
    print(f"VOICE AND BEHAVIOR occurrences: {voice_and_behavior_count}")
    print(f"Avatars breakdown: DCC placeholder={dcc_placeholder_count}, Custom portraits={custom_portrait_count}, Old fallback={old_fallback_count}, Invalid/Empty={invalid_avatar_count}")

    if bracket_starts != 310:
        errors.append(f"Not all entries start with '[': {non_bracket_starts}")
    if em_dash_count > 0:
        errors.append(f"Found {em_dash_count} entries with em-dashes")
    if asterisk_count > 0:
        errors.append(f"Found {asterisk_count} entries with asterisks")
    if age_macro_count > 0:
        errors.append(f"Found {age_macro_count} entries with age macros")
    if recursion_not_true > 0:
        errors.append(f"Found {recursion_not_true} entries lacking exclude_from_recursion: True")
    if old_fallback_count > 0:
        errors.append(f"Found {old_fallback_count} entries still using old fallback")
    if invalid_avatar_count > 0:
        errors.append(f"Found {invalid_avatar_count} entries with invalid avatar")
    if dcc_placeholder_count != 200:
        errors.append(f"DCC placeholder count is {dcc_placeholder_count} (expected 200)")
    if custom_portrait_count != 110:
        errors.append(f"Custom portrait count is {custom_portrait_count} (expected 110)")

    print("\n=== 4. Verifying the 7 Core Characters ===")
    prim_map = {e['entry_id']: e for e in prim['lexicon']}
    for eid, (expected_name, expected_len, expected_card_id, expected_avatar) in CORE_PRIMARY.items():
        e = prim_map.get(eid)
        if not e:
            errors.append(f"Missing core primary entry {eid}")
            continue
        print(f"Checking {expected_name} ({eid}):")
        if e.get('type') != 'npc':
            errors.append(f"{expected_name} type is {e.get('type')} (expected 'npc')")
        if e.get('selective') is not False:
            errors.append(f"{expected_name} selective is {e.get('selective')} (expected False)")
        if len(e.get('content', '')) != expected_len:
            errors.append(f"{expected_name} content length {len(e.get('content', ''))} != expected {expected_len}")
        if e.get('avatar') != expected_avatar:
            errors.append(f"{expected_name} avatar {e.get('avatar')} != expected {expected_avatar}")
        if e.get('custom_avatar_regex') is not True:
            errors.append(f"{expected_name} custom_avatar_regex is not True")
        if e.get('lines_parsed') != 1:
            errors.append(f"{expected_name} lines_parsed is {e.get('lines_parsed')} (expected 1)")
        if not e.get('avatar_activation_regex'):
            errors.append(f"{expected_name} missing avatar_activation_regex")
        if not e.get('npc_info') or not e.get('npc_info').get('first_name'):
            errors.append(f"{expected_name} invalid npc_info: {e.get('npc_info')}")
        if expected_card_id not in e.get('ignored_characters', []):
            errors.append(f"{expected_name} missing {expected_card_id} in ignored_characters: {e.get('ignored_characters')}")
        print(f"  -> PASS: type=npc, len={len(e.get('content'))}, ignored_chars={e.get('ignored_characters')}, avatar={e.get('avatar')}")

    sec_map = {e['entry_id']: e for e in sec['lexicon']}
    for eid, (expected_name, expected_len, expected_card_id, expected_avatar) in CORE_SECONDARY.items():
        e = sec_map.get(eid)
        if not e:
            errors.append(f"Missing core secondary entry {eid}")
            continue
        print(f"Checking {expected_name} ({eid}):")
        if e.get('type') != 'npc':
            errors.append(f"{expected_name} type is {e.get('type')} (expected 'npc')")
        if e.get('selective') is not False:
            errors.append(f"{expected_name} selective is {e.get('selective')} (expected False)")
        if len(e.get('content', '')) != expected_len:
            errors.append(f"{expected_name} content length {len(e.get('content', ''))} != expected {expected_len}")
        if e.get('avatar') != expected_avatar:
            errors.append(f"{expected_name} avatar {e.get('avatar')} != expected {expected_avatar}")
        if e.get('custom_avatar_regex') is not True:
            errors.append(f"{expected_name} custom_avatar_regex is not True")
        if e.get('lines_parsed') != 1:
            errors.append(f"{expected_name} lines_parsed is {e.get('lines_parsed')} (expected 1)")
        if not e.get('avatar_activation_regex'):
            errors.append(f"{expected_name} missing avatar_activation_regex")
        if not e.get('npc_info') or not e.get('npc_info').get('first_name'):
            errors.append(f"{expected_name} invalid npc_info: {e.get('npc_info')}")
        if expected_card_id not in e.get('ignored_characters', []):
            errors.append(f"{expected_name} missing {expected_card_id} in ignored_characters: {e.get('ignored_characters')}")
        print(f"  -> PASS: type=npc, len={len(e.get('content'))}, ignored_chars={e.get('ignored_characters')}, avatar={e.get('avatar')}")

    print("\n=== 5. Verifying Irregular Entries (Bruce, Campus Staff Rat, Adrian) ===")
    for eid, name in [('NQd7n3QacMcK-TzowQ2LE', 'Bruce'), ('oov5UWuVhZ3RGgoxMkaTS', 'Campus Staff Rat'), ('Og7V6v67guXXAaP0_PsTM', 'Adrian')]:
        e = sec_map.get(eid)
        print(f"Checking {name} ({eid}):")
        if not e['content'].strip().startswith('['):
            errors.append(f"{name} does not start with '['")
        if 'BACKSTORY:' not in e['content']:
            errors.append(f"{name} missing BACKSTORY:")
        if 'VOICE & BEHAVIOR:' not in e['content']:
            errors.append(f"{name} missing VOICE & BEHAVIOR:")
        if e['avatar'] != DCC_PLACEHOLDER:
            errors.append(f"{name} avatar is not DCC placeholder: {e['avatar']}")
        print(f"  -> PASS: starts with '[', has BACKSTORY, VOICE & BEHAVIOR, avatar=DCC_PLACEHOLDER")

    print("\n=== AUDIT SUMMARY ===")
    if errors:
        print(f"FAILED with {len(errors)} errors:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("ALL CHECKS PASSED PERFECTLY! 100% COMPLIANT WITH MILESTONE 1 REQUIREMENTS!")
        return True

if __name__ == '__main__':
    verify()

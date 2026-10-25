import json
import urllib.request
import urllib.error
import re
import pathlib
import sys

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN_PATH = ROOT / 'scratch' / 'wyvern_token.txt'

def fetch_lorebook(lid):
    token = TOKEN_PATH.read_text(encoding='utf-8').strip()
    url = f"https://app.wyvern.chat/api/lorebooks/{lid}"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "Milestone2Challenger/1.0"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            body = resp.read()
            data = json.loads(body.decode('utf-8'))
            return status, data
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8', errors='replace')
    except Exception as e:
        return 500, str(e)

def run_challenge():
    results = {
        "primary": {},
        "secondary": {},
        "errors": [],
        "verdict": "PENDING"
    }
    
    print("=== CHALLENGER M2: QUERYING LIVE WYVERN API ===")
    
    # 1. Fetch Primary
    p_status, p_data = fetch_lorebook("_zwEqgEEzh12X6gHVmMKKC")
    print(f"Primary Status: {p_status}")
    if p_status != 200:
        results["errors"].append(f"Primary HTTP {p_status}: {p_data}")
        results["verdict"] = "REQUEST_CHANGES"
        print(f"FAILED to fetch Primary: {p_status}")
        return results

    # 2. Fetch Secondary
    s_status, s_data = fetch_lorebook("_Uht3Ckz44JBDrPnUHq7LV")
    print(f"Secondary Status: {s_status}")
    if s_status != 200:
        results["errors"].append(f"Secondary HTTP {s_status}: {s_data}")
        results["verdict"] = "REQUEST_CHANGES"
        print(f"FAILED to fetch Secondary: {s_status}")
        return results

    print("\n=== VERIFYING PRIMARY LOREBOOK ===")
    p_lex = p_data.get("lexicon", [])
    p_ent = p_data.get("entries", [])
    print(f"Primary Lexicon count: {len(p_lex)}")
    print(f"Primary Entries count: {len(p_ent)}")
    
    if len(p_lex) != 99:
        results["errors"].append(f"Primary live lexicon count mismatch: expected 99, got {len(p_lex)}")
    if len(p_ent) != 99:
        results["errors"].append(f"Primary live entries count mismatch: expected 99, got {len(p_ent)}")
        
    p_parity = (json.dumps(p_lex, sort_keys=True) == json.dumps(p_ent, sort_keys=True))
    print(f"Primary Entries == Lexicon parity: {p_parity}")
    if not p_parity:
        results["errors"].append("Primary live entries != lexicon parity failed")
        
    p_root_gallery = "gallery" in p_data and isinstance(p_data["gallery"], list)
    p_root_gallery_count = "gallery_count" in p_data and isinstance(p_data["gallery_count"], int)
    p_root_highlight = p_data.get("enableEntryHighlighting") is True
    print(f"Primary root gallery: {p_root_gallery}, gallery_count: {p_root_gallery_count}, enableEntryHighlighting: {p_root_highlight}")
    if not (p_root_gallery and p_root_gallery_count):
        results["errors"].append("Primary root missing gallery or gallery_count")
    if not p_root_highlight:
        results["errors"].append("Primary root missing enableEntryHighlighting: true")

    # Inspect Primary Entries
    p_scan_persona_count = 0
    p_whole_words_count = 0
    p_highlight_count = 0
    p_valid_npc_info_count = 0
    p_valid_avatars_count = 0
    p_dup_surnames = []
    
    # Track specific expected characters in Primary
    p_chars_to_check = {
        "Erik Cornelius Ulfr Douglas": False,
        "Malachia Björn Douglas Bloodmoon": False,
        "Noah Loki Douglas Bloodmoon": False,
        "Jasper Svartr Douglas Bloodmoon": False,
        "Alyssa Hvit Douglas Bloodmoon": False,
        "Logan Dominic Járn Douglas": False,
        "Nixara Hvit Bloodmoon": False,
        "Wulfnic Báleygr Bloodmoon": False,
        "Dominic Wayne Rogers": False,
        "Roland Mark Vickers": False,
        "Marcus Iron Thornfield": False,
        "Kaladin Blackwolf Nargathon": False,
        "Iordan R. Vess": False,
    }
    
    for idx, e in enumerate(p_lex):
        name = e.get("name", f"entry_{idx}")
        # Toggles
        if e.get("scan_persona") is True:
            p_scan_persona_count += 1
        if e.get("whole_words_only") is True:
            p_whole_words_count += 1
        if e.get("highlight_keys") is True or e.get("enable_highlighting") is True:
            p_highlight_count += 1
            
        # Avatar
        av = e.get("avatar", "")
        if av and av.startswith("https://"):
            p_valid_avatars_count += 1
            
        # NPC info
        info = e.get("npc_info")
        if isinstance(info, dict):
            required_keys = {"first_name", "middle_names", "last_name", "nicknames", "titles", "npc_prefix"}
            if required_keys.issubset(info.keys()) and isinstance(info["middle_names"], list):
                p_valid_npc_info_count += 1
                
                # Check specific target characters
                for target_full_name in p_chars_to_check:
                    fn = info.get("first_name", "")
                    mn = info.get("middle_names", [])
                    ln = info.get("last_name", "")
                    full = " ".join([fn] + mn + ([ln] if ln else [])).strip()
                    if full == target_full_name or name == target_full_name:
                        p_chars_to_check[target_full_name] = True
                        if not mn:
                            results["errors"].append(f"Primary character {target_full_name} has empty middle_names!")
                            
        # Regex duplicate surname check
        reg = e.get("avatar_activation_regex", "")
        # Look for e.g. "Rivers Rivers", "Rogers Rogers"
        dups = re.findall(r'\b([A-Za-z]+)\s+\1\b', reg)
        if dups:
            p_dup_surnames.append((name, dups))

    print(f"Primary scan_persona: {p_scan_persona_count}/99")
    print(f"Primary whole_words_only: {p_whole_words_count}/99")
    print(f"Primary highlighting: {p_highlight_count}/99")
    print(f"Primary valid npc_info: {p_valid_npc_info_count}/99")
    print(f"Primary valid avatars: {p_valid_avatars_count}/99")
    print(f"Primary duplicate surnames in regex: {len(p_dup_surnames)}")
    
    if p_scan_persona_count != 99:
        results["errors"].append(f"Primary scan_persona not 100%: {p_scan_persona_count}/99")
    if p_whole_words_count != 99:
        results["errors"].append(f"Primary whole_words_only not 100%: {p_whole_words_count}/99")
    if p_highlight_count != 99:
        results["errors"].append(f"Primary highlighting not 100%: {p_highlight_count}/99")
    if p_valid_npc_info_count != 99:
        results["errors"].append(f"Primary valid npc_info not 100%: {p_valid_npc_info_count}/99")
    if p_valid_avatars_count != 99:
        results["errors"].append(f"Primary valid avatars not 100%: {p_valid_avatars_count}/99")
    if p_dup_surnames:
        results["errors"].append(f"Primary duplicate surnames found: {p_dup_surnames}")
        
    for char_name, found in p_chars_to_check.items():
        if not found:
            results["errors"].append(f"Primary expected character not matched: {char_name}")
            
    print("\n=== VERIFYING SECONDARY LOREBOOK ===")
    s_lex = s_data.get("lexicon", [])
    s_ent = s_data.get("entries", [])
    print(f"Secondary Lexicon count: {len(s_lex)}")
    print(f"Secondary Entries count: {len(s_ent)}")
    
    if len(s_lex) != 211:
        results["errors"].append(f"Secondary live lexicon count mismatch: expected 211, got {len(s_lex)}")
    if len(s_ent) != 211:
        results["errors"].append(f"Secondary live entries count mismatch: expected 211, got {len(s_ent)}")
        
    s_parity = (json.dumps(s_lex, sort_keys=True) == json.dumps(s_ent, sort_keys=True))
    print(f"Secondary Entries == Lexicon parity: {s_parity}")
    if not s_parity:
        results["errors"].append("Secondary live entries != lexicon parity failed")

    s_root_gallery = "gallery" in s_data and isinstance(s_data["gallery"], list)
    s_root_gallery_count = "gallery_count" in s_data and isinstance(s_data["gallery_count"], int)
    s_root_highlight = s_data.get("enableEntryHighlighting") is True
    print(f"Secondary root gallery: {s_root_gallery}, gallery_count: {s_root_gallery_count}, enableEntryHighlighting: {s_root_highlight}")
    if not (s_root_gallery and s_root_gallery_count):
        results["errors"].append("Secondary root missing gallery or gallery_count")
    if not s_root_highlight:
        results["errors"].append("Secondary root missing enableEntryHighlighting: true")

    # Inspect Secondary Entries
    s_scan_persona_count = 0
    s_whole_words_count = 0
    s_highlight_count = 0
    s_valid_npc_info_count = 0
    s_valid_avatars_count = 0
    s_dup_surnames = []
    
    finn_found = False
    jasper_rowan_found = False
    alistair_ambrose_found = False
    luisa_sanchez_found = False
    camp_mystic_middle_names_count = 0
    
    for idx, e in enumerate(s_lex):
        name = e.get("name", f"entry_{idx}")
        # Toggles
        if e.get("scan_persona") is True:
            s_scan_persona_count += 1
        if e.get("whole_words_only") is True:
            s_whole_words_count += 1
        if e.get("highlight_keys") is True or e.get("enable_highlighting") is True:
            s_highlight_count += 1
            
        # Avatar
        av = e.get("avatar", "")
        if av and av.startswith("https://"):
            s_valid_avatars_count += 1
            
        # Check Finn the Satyr and Jasper Rowan
        keys_str = " ".join(e.get("keys", [])) + " " + name
        if "Finn the Satyr" in keys_str or "Satyr" in keys_str or "Finn" in name:
            if "Satyr" in keys_str:
                finn_found = True
                print(f"Found Finn the Satyr: name='{name}', keys={e.get('keys')}, id={e.get('id')}")
        if "Jasper Rowan" in keys_str or "Rowan" in name:
            jasper_rowan_found = True
            print(f"Found Jasper Rowan: name='{name}', keys={e.get('keys')}, id={e.get('id')}")

        # NPC info
        info = e.get("npc_info")
        if isinstance(info, dict):
            required_keys = {"first_name", "middle_names", "last_name", "nicknames", "titles", "npc_prefix"}
            if required_keys.issubset(info.keys()) and isinstance(info["middle_names"], list):
                s_valid_npc_info_count += 1
                
                fn = info.get("first_name", "")
                mn = info.get("middle_names", [])
                ln = info.get("last_name", "")
                
                if fn == "Alistair" and ln == "DeVille":
                    if "Ambrose" in mn:
                        alistair_ambrose_found = True
                    else:
                        results["errors"].append("Alistair DeVille missing 'Ambrose' in middle_names")
                        
                if fn == "Luisa" and ln == "Rogers":
                    if "Sanchez" in mn:
                        luisa_sanchez_found = True
                    else:
                        results["errors"].append("Luisa Rogers missing 'Sanchez' in middle_names")
                        
                if mn:
                    camp_mystic_middle_names_count += 1

        # Regex duplicate surname check
        reg = e.get("avatar_activation_regex", "")
        dups = re.findall(r'\b([A-Za-z]+)\s+\1\b', reg)
        if dups:
            s_dup_surnames.append((name, dups))

    print(f"Secondary scan_persona: {s_scan_persona_count}/211")
    print(f"Secondary whole_words_only: {s_whole_words_count}/211")
    print(f"Secondary highlighting: {s_highlight_count}/211")
    print(f"Secondary valid npc_info: {s_valid_npc_info_count}/211")
    print(f"Secondary valid avatars: {s_valid_avatars_count}/211")
    print(f"Secondary duplicate surnames in regex: {len(s_dup_surnames)}")
    print(f"Finn the Satyr found: {finn_found}")
    print(f"Jasper Rowan found: {jasper_rowan_found}")
    print(f"Alistair Ambrose DeVille found: {alistair_ambrose_found}")
    print(f"Luisa Sanchez Rogers found: {luisa_sanchez_found}")
    print(f"Total entries with non-empty middle_names in Secondary: {camp_mystic_middle_names_count}")
    
    if not finn_found:
        results["errors"].append("Finn the Satyr not found in live Secondary lorebook")
    if not jasper_rowan_found:
        results["errors"].append("Jasper Rowan not found in live Secondary lorebook")
    if not alistair_ambrose_found:
        results["errors"].append("Alistair Ambrose DeVille middle name 'Ambrose' not verified")
    if not luisa_sanchez_found:
        results["errors"].append("Luisa Sanchez Rogers middle name 'Sanchez' not verified")
        
    if s_scan_persona_count != 211:
        results["errors"].append(f"Secondary scan_persona not 100%: {s_scan_persona_count}/211")
    if s_whole_words_count != 211:
        results["errors"].append(f"Secondary whole_words_only not 100%: {s_whole_words_count}/211")
    if s_highlight_count != 211:
        results["errors"].append(f"Secondary highlighting not 100%: {s_highlight_count}/211")
    if s_valid_npc_info_count != 211:
        results["errors"].append(f"Secondary valid npc_info not 100%: {s_valid_npc_info_count}/211")
    if s_valid_avatars_count != 211:
        results["errors"].append(f"Secondary valid avatars not 100%: {s_valid_avatars_count}/211")
    if s_dup_surnames:
        results["errors"].append(f"Secondary duplicate surnames found: {s_dup_surnames}")
        
    if not results["errors"]:
        results["verdict"] = "APPROVE"
    else:
        results["verdict"] = "REQUEST_CHANGES"
        
    print(f"\nFINAL VERDICT: {results['verdict']}")
    if results["errors"]:
        print("ERRORS ENCOUNTERED:")
        for err in results["errors"]:
            print(f"  - {err}")
            
    # Write summary to scratch/m2_live_adversarial_result.json
    out_path = ROOT / 'scratch' / 'm2_live_adversarial_result.json'
    out_path.write_text(json.dumps(results, indent=2), encoding='utf-8')
    print(f"Detailed results written to {out_path}")
    return results

if __name__ == '__main__':
    run_challenge()

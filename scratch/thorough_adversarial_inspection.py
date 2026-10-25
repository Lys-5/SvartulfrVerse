import json
import urllib.request
import re
import pathlib

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
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read().decode('utf-8'))

def inspect():
    print("=" * 70)
    print("THOROUGH ADVERSARIAL INSPECTION OF LIVE WYVERN LOREBOOKS")
    print("=" * 70)

    # 1. PRIMARY LOREBOOK
    p_status, p_data = fetch_lorebook("_zwEqgEEzh12X6gHVmMKKC")
    assert p_status == 200, f"Primary status not 200: {p_status}"
    p_lex = p_data.get("lexicon", [])
    print(f"Primary Live Lexicon Count: {len(p_lex)}")
    assert len(p_lex) == 99, f"Expected 99, got {len(p_lex)}"

    # Check key figures in Primary
    target_primary = {
        "Erik Ulfr Douglas": {
            "first_name": "Erik",
            "middle_names": ["Cornelius", "Ulfr"],
            "last_name": "Douglas",
            "titles": ["Alpha", "Lord"],
            "ignored_characters": ["_QPea6g4Q1QfeYCVHCLMPR"]
        },
        "Malachia Björn Douglas Bloodmoon": {
            "first_name": "Malachia",
            "middle_names": ["Björn"],
            "last_name": "Douglas Bloodmoon",
            "titles": ["Alpha"],
            "ignored_characters": ["_RDfz7XzTpM23LpPALVXHM"]
        },
        "Noah Loki Douglas Bloodmoon": {
            "first_name": "Noah",
            "middle_names": ["Loki"],
            "last_name": "Douglas Bloodmoon",
            "titles": [],
            "ignored_characters": ["_zFLUjV8aVxQRAfQxGcAcY"]
        },
        "Jasper Svartr Douglas Bloodmoon": {
            "first_name": "Jasper",
            "middle_names": ["Svartr"],
            "last_name": "Douglas Bloodmoon",
            "titles": [],
            "ignored_characters": ["_t4J9aQNJM36cUKAP4wB4U"],
            "ignored_personas": ["1792155173728"],
            "selective": True,
            "secondary_keys": ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]
        },
        "Alyssa Hvit Douglas Bloodmoon": {
            "first_name": "Alyssa",
            "middle_names": ["Hvit"],
            "last_name": "Douglas Bloodmoon",
            "titles": [],
            "ignored_characters": ["_6exg3yPfe2eCDK4hTftkh"],
            "ignored_personas": ["persona_1786335754946"],
            "selective": True,
            "secondary_keys": ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]
        },
        "Logan Járn Douglas": {
            "first_name": "Logan",
            "middle_names": ["Dominic", "Járn"],
            "last_name": "Douglas",
            "titles": [],
            "ignored_characters": ["_T8Ywcr9FEqNf9JxbK6eHP"]
        },
        "Wulfnic Báleygr Bloodmoon": {
            "first_name": "Wulfnic",
            "middle_names": ["Báleygr"],
            "last_name": "Bloodmoon",
            "titles": ["Jarl", "Alpha"],
            "ignored_characters": ["_HEQQbbRFwKdG8QE2Fh1z1"]
        },
        "Nixara Hvit Bloodmoon": {
            "first_name": "Nixara",
            "middle_names": ["Hvit"],
            "last_name": "Bloodmoon",
            "titles": []
        },
        "Dominic Rogers": {
            "first_name": "Dominic",
            "middle_names": ["Wayne"],
            "last_name": "Rogers",
            "titles": ["Mr."]
        },
        "Roland Vickers": {
            "first_name": "Roland",
            "middle_names": ["Mark"],
            "last_name": "Vickers",
            "titles": []
        },
        "Marcus Thornfield": {
            "first_name": "Marcus",
            "middle_names": ["Iron"],
            "last_name": "Thornfield",
            "titles": []
        },
        "Kaladin Nargathon": {
            "first_name": "Kaladin",
            "middle_names": ["Blackwolf"],
            "last_name": "Nargathon",
            "titles": ["Commander"]
        },
        "Iordan R. Vess": {
            "first_name": "Iordan",
            "middle_names": ["R."],
            "last_name": "Vess",
            "titles": ["Alpha"]
        }
    }

    found_primary = {}
    p_scan_count = 0
    p_whole_count = 0
    p_highlight_count = 0
    p_avatar_count = 0

    for e in p_lex:
        name = e.get("name", "")
        if e.get("scan_persona") is True:
            p_scan_count += 1
        if e.get("whole_words_only") is True:
            p_whole_count += 1
        if e.get("highlight_keys") is True and e.get("enable_highlighting") is True:
            p_highlight_count += 1
        if e.get("avatar", "").startswith("https://"):
            p_avatar_count += 1

        info = e.get("npc_info", {})
        for tgt, exp in target_primary.items():
            if name == tgt or (info.get("first_name") == exp["first_name"] and (not exp.get("last_name") or exp.get("last_name") in name or info.get("last_name") == exp.get("last_name"))):
                # Extra check to avoid false matches
                if exp["first_name"] == "Marcus" and "Thornfield" not in name:
                    continue
                found_primary[tgt] = e
                # Check middle names
                assert info.get("middle_names") == exp["middle_names"], f"{tgt}: expected mn {exp['middle_names']}, got {info.get('middle_names')}"
                # Check titles
                for t in exp.get("titles", []):
                    assert t in info.get("titles", []), f"{tgt}: expected title {t} in {info.get('titles')}"
                # Check ignored_characters
                if "ignored_characters" in exp:
                    assert e.get("ignored_characters") == exp["ignored_characters"], f"{tgt}: ignored_chars mismatch"
                # Check ignored_personas
                if "ignored_personas" in exp:
                    assert e.get("ignored_personas") == exp["ignored_personas"], f"{tgt}: ignored_personas mismatch"
                if "selective" in exp:
                    assert e.get("selective") == exp["selective"], f"{tgt}: selective mismatch"
                if "secondary_keys" in exp:
                    assert e.get("secondary_keys") == exp["secondary_keys"], f"{tgt}: secondary_keys mismatch"

    print(f"Primary Target Match: {len(found_primary)}/{len(target_primary)} verified!")
    print(f"Primary scan_persona == True: {p_scan_count}/99")
    print(f"Primary whole_words_only == True: {p_whole_words_count if 'p_whole_words_count' in locals() else p_whole_count}/99")
    print(f"Primary highlight toggles == True: {p_highlight_count}/99")
    print(f"Primary avatars valid HTTPS: {p_avatar_count}/99")

    assert p_scan_count == 99
    assert p_whole_count == 99
    assert p_highlight_count == 99
    assert p_avatar_count == 99
    assert len(found_primary) == len(target_primary)

    # 2. SECONDARY LOREBOOK
    print("\n" + "-" * 70)
    s_status, s_data = fetch_lorebook("_Uht3Ckz44JBDrPnUHq7LV")
    assert s_status == 200, f"Secondary status not 200: {s_status}"
    s_lex = s_data.get("lexicon", [])
    print(f"Secondary Live Lexicon Count: {len(s_lex)}")
    assert len(s_lex) == 211, f"Expected 211, got {len(s_lex)}"

    s_scan_count = 0
    s_whole_count = 0
    s_highlight_count = 0
    s_avatar_count = 0
    s_middle_names_count = 0

    finn_entry = None
    jasper_rowan_entry = None
    alistair_entry = None
    luisa_entry = None
    edric_entry = None

    for e in s_lex:
        name = e.get("name", "")
        if e.get("scan_persona") is True:
            s_scan_count += 1
        if e.get("whole_words_only") is True:
            s_whole_count += 1
        if e.get("highlight_keys") is True and e.get("enable_highlighting") is True:
            s_highlight_count += 1
        if e.get("avatar", "").startswith("https://"):
            s_avatar_count += 1

        info = e.get("npc_info", {})
        mn = info.get("middle_names", [])
        if mn:
            s_middle_names_count += 1

        if name == "Finn the Satyr":
            finn_entry = e
        elif name == "Jasper Rowan":
            jasper_rowan_entry = e
        elif info.get("first_name") == "Alistair" and info.get("last_name") == "DeVille":
            alistair_entry = e
        elif info.get("first_name") == "Luisa" and info.get("last_name") == "Rogers":
            luisa_entry = e
        elif "Edric Douglas" in name:
            edric_entry = e

    print(f"Secondary scan_persona == True: {s_scan_count}/211")
    print(f"Secondary whole_words_only == True: {s_whole_count}/211")
    print(f"Secondary highlight toggles == True: {s_highlight_count}/211")
    print(f"Secondary avatars valid HTTPS: {s_avatar_count}/211")
    print(f"Secondary entries with middle_names: {s_middle_names_count}/211")

    assert s_scan_count == 211
    assert s_whole_count == 211
    assert s_highlight_count == 211
    assert s_avatar_count == 211
    assert s_middle_names_count == 102

    # Verify Finn the Satyr
    assert finn_entry is not None, "Finn the Satyr must be present in Secondary"
    print(f"\nFinn the Satyr details: name='{finn_entry.get('name')}', avatar='{finn_entry.get('avatar')}'")
    f_info = finn_entry.get("npc_info", {})
    assert f_info.get("first_name") == "Finn", f"Finn first_name: {f_info.get('first_name')}"
    assert finn_entry.get("scan_persona") is True
    assert finn_entry.get("whole_words_only") is True
    assert finn_entry.get("highlight_keys") is True

    # Verify Jasper Rowan
    assert jasper_rowan_entry is not None, "Jasper Rowan must be present in Secondary"
    print(f"Jasper Rowan details: name='{jasper_rowan_entry.get('name')}', avatar='{jasper_rowan_entry.get('avatar')}'")
    jr_info = jasper_rowan_entry.get("npc_info", {})
    assert jr_info.get("first_name") == "Jasper", f"Jasper Rowan first_name: {jr_info.get('first_name')}"
    assert jr_info.get("middle_names") == ["Finn"], f"Jasper Rowan middle_names: {jr_info.get('middle_names')}"
    assert jr_info.get("last_name") == "Rowan", f"Jasper Rowan last_name: {jr_info.get('last_name')}"
    assert "Camp Mystic Camper" in jr_info.get("titles", []), f"Jasper Rowan titles: {jr_info.get('titles')}"
    assert jasper_rowan_entry.get("scan_persona") is True
    assert jasper_rowan_entry.get("whole_words_only") is True
    assert jasper_rowan_entry.get("highlight_keys") is True

    # Verify Alistair Ambrose DeVille
    assert alistair_entry is not None, "Alistair Ambrose DeVille must be present in Secondary"
    a_info = alistair_entry.get("npc_info", {})
    assert a_info.get("middle_names") == ["Ambrose"], f"Alistair middle_names: {a_info.get('middle_names')}"
    print(f"Alistair Ambrose DeVille verified: {a_info}")

    # Verify Luisa Sanchez Rogers
    assert luisa_entry is not None, "Luisa Sanchez Rogers must be present in Secondary"
    l_info = luisa_entry.get("npc_info", {})
    assert l_info.get("middle_names") == ["Sanchez"], f"Luisa middle_names: {l_info.get('middle_names')}"
    print(f"Luisa Sanchez Rogers verified: {l_info}")

    # Verify Edric Douglas anti-collision
    assert edric_entry is not None, "Edric Douglas must be present in Secondary"
    assert edric_entry.get("ignored_characters") == ["_TbRM3EdxDjHFgqztTbCpL"], f"Edric ignored_characters: {edric_entry.get('ignored_characters')}"
    print(f"Edric Douglas anti-collision verified: {edric_entry.get('ignored_characters')}")

    print("\n" + "=" * 70)
    print("ALL ADVERSARIAL ASSERTIONS PASSED WITH ZERO ERRORS!")
    print("=" * 70)

if __name__ == '__main__':
    inspect()

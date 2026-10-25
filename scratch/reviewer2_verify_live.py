import json
import urllib.request
import pathlib
import sys

ROOT = pathlib.Path(r"e:\repository\SvartulfrVerse")
token = (ROOT / "scratch" / "wyvern_token.txt").read_text("utf-8").strip()

scen_ids = [
    ("char_scenario_8GtdBd6dU7tPF481ekrKe", "Camp Mystic", 8, 4),
    ("char_scenario_664yrxUXYwNUUJfyf7da7", "SUCC Alyssa", 8, 6),
    ("char_scenario_Mfxz4Ym8QaECU6MjfmWG3", "SUCC Jasper", 8, 5),
    ("char_scenario_kw42g8J3NjBfKf7QW8zAG", "Villa Douglas", 7, 5),
    ("char_scenario_WdajqL3eJtT3GydxhDRT4", "DMHA Dungeons", 9, 4),
    ("char_scenario_MdbWc4gXbDqXHKrXY7YFx", "Underworld Sindacato", 6, 4),
]

expected_lbs = [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_Uht3Ckz44JBDrPnUHq7LV",
]

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}

print("=== REVIEWER 2 INDEPENDENT LIVE WYVERN VERIFICATION ===")
for sid, label, exp_slots, exp_greetings in scen_ids:
    url = f"https://app.wyvern.chat/api/character-scenarios/{sid}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 200, f"HTTP {resp.status} on {sid}"
        raw_bytes = resp.read()
        raw_text = raw_bytes.decode("utf-8")
        data = json.loads(raw_text)

        vis = data.get("visibility")
        slots = data.get("slots", [])
        greetings = data.get("greetings", [])
        lbs = data.get("lorebook_ids", [])
        name = data.get("name")
        rating = data.get("rating")
        scenario_text = data.get("scenario", "")

        print(f"\n[SCENARIO {sid}] '{name}' ({label})")
        print(f"  HTTP Status: {resp.status} OK")
        print(f"  Visibility: '{vis}'")
        assert vis == "private", f"{sid}: visibility is '{vis}', expected 'private'"

        print(f"  Rating: '{rating}'")
        assert rating == "explicit", f"{sid}: rating is '{rating}', expected 'explicit'"

        print(f"  Slots Count: {len(slots)} (expected {exp_slots})")
        assert len(slots) == exp_slots, f"{sid}: slots {len(slots)} != {exp_slots}"

        print(f"  Greetings Count: {len(greetings)} (expected {exp_greetings})")
        assert len(greetings) == exp_greetings, f"{sid}: greetings {len(greetings)} != {exp_greetings}"

        print(f"  Lorebook IDs Count: {len(lbs)} (expected 6)")
        assert lbs == expected_lbs, f"{sid}: lorebooks mismatch {lbs}"

        # Check unavailable_count on each slot
        slot_keys = []
        for s in slots:
            k = s.get("key")
            slot_keys.append(k)
            unav = s.get("unavailable_count", 0)
            assert unav == 0, f"{sid}: slot {k} unavailable_count={unav}"
        print(f"  Slot Keys ({len(slot_keys)}): {', '.join(slot_keys)}")
        print(f"  All slots have unavailable_count == 0: PASS")

        # Check em dashes in raw text
        assert "\u2014" not in raw_text, f"{sid} contains em-dash (\\u2014)!"
        assert "\u2013" not in raw_text, f"{sid} contains en-dash (\\u2013)!"
        print("  Em-dashes / en-dashes: NONE (PASS)")

        # Check greeting message parity
        for g_idx, g in enumerate(greetings):
            gid = g.get("id")
            msgs = g.get("messages", [])
            assert len(msgs) >= 1, f"{sid}: greeting {gid} has no messages"
            assert g.get("content") == msgs[0].get("content"), f"{sid}: greeting {gid} content mismatch with messages[0]"
            assert g.get("speaker_slot") == msgs[0].get("speaker_slot"), f"{sid}: greeting {gid} speaker_slot mismatch with messages[0]"
            for m in msgs:
                assert m.get("speaker_slot") in slot_keys, f"{sid}: msg speaker_slot '{m.get('speaker_slot')}' not in slots"
        print(f"  Greeting Parity & Speaker Slot checks: PASS ({len(greetings)} greetings verified)")

print("\nALL 6 LIVE SCENARIOS FULLY VERIFIED ON WYVERN WEB API WITH 100% SUCCESS!")

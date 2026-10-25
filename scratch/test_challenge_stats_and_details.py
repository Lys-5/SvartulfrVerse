"""
Detailed Character and Invariant Metric Scanner for Svartulfr Verse Character Scenarios
Challenger 1 Empirical Verification
"""

import os
import re
import json
from pathlib import Path

SCENARIOS_DIR = Path(r"e:\repository\SvartulfrVerse\FINAL\scenarios")

EXPECTED_FILES = [
    "Svartulfr_Scenario_Camp_Mystic.json",
    "Svartulfr_Scenario_DMHA_Dungeons.json",
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json",
    "Svartulfr_Scenario_SUCC_Route_Jasper.json",
    "Svartulfr_Scenario_Underworld_Sindacato.json",
    "Svartulfr_Scenario_Villa_Douglas.json",
]

EXPECTED_SLOT_COUNTS = {
    "Svartulfr_Scenario_Camp_Mystic.json": 8,
    "Svartulfr_Scenario_DMHA_Dungeons.json": 9,
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json": 8,
    "Svartulfr_Scenario_SUCC_Route_Jasper.json": 8,
    "Svartulfr_Scenario_Underworld_Sindacato.json": 6,
    "Svartulfr_Scenario_Villa_Douglas.json": 7,
}

EXPECTED_GREETING_COUNTS = {
    "Svartulfr_Scenario_Camp_Mystic.json": 4,
    "Svartulfr_Scenario_DMHA_Dungeons.json": 4,
    "Svartulfr_Scenario_SUCC_Route_Alyssa.json": 6,
    "Svartulfr_Scenario_SUCC_Route_Jasper.json": 5,
    "Svartulfr_Scenario_Underworld_Sindacato.json": 4,
    "Svartulfr_Scenario_Villa_Douglas.json": 5,
}

EXPECTED_LOREBOOK_IDS = [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_Uht3Ckz44JBDrPnUHq7LV",
]

def main():
    report = {
        "files_analyzed": len(EXPECTED_FILES),
        "per_file_metrics": {},
        "total_characters_scanned": 0,
        "total_bytes_scanned": 0,
        "total_lines_scanned": 0,
        "total_slots": 0,
        "total_greetings": 0,
        "total_messages": 0,
        "smart_quote_scan": {},
        "overall_status": "PASS"
    }

    for fname in EXPECTED_FILES:
        fpath = SCENARIOS_DIR / fname
        with open(fpath, "rb") as f:
            raw_bytes = f.read()
        raw_text = raw_bytes.decode("utf-8")
        data = json.loads(raw_text)

        char_count = len(raw_text)
        byte_count = len(raw_bytes)
        line_count = len(raw_text.splitlines())

        report["total_characters_scanned"] += char_count
        report["total_bytes_scanned"] += byte_count
        report["total_lines_scanned"] += line_count

        slots = data.get("slots", [])
        greetings = data.get("greetings", [])
        lorebook_ids = data.get("lorebook_ids", [])
        visibility = data.get("visibility")

        msg_count = sum(len(g.get("messages", [])) for g in greetings)
        report["total_slots"] += len(slots)
        report["total_greetings"] += len(greetings)
        report["total_messages"] += msg_count

        # Check smart quotes
        smart_quotes = {
            "left_double": raw_text.count("\u201c"),
            "right_double": raw_text.count("\u201d"),
            "left_single": raw_text.count("\u2018"),
            "right_single": raw_text.count("\u2019"),
        }
        report["smart_quote_scan"][fname] = smart_quotes

        # Verify expected counts
        exp_slots = EXPECTED_SLOT_COUNTS[fname]
        exp_greetings = EXPECTED_GREETING_COUNTS[fname]

        slot_match = (len(slots) == exp_slots)
        greeting_match = (len(greetings) == exp_greetings)
        lb_match = (set(lorebook_ids) == set(EXPECTED_LOREBOOK_IDS) and len(lorebook_ids) == 6)
        vis_match = (visibility == "private")

        report["per_file_metrics"][fname] = {
            "name": data.get("name"),
            "scenario_id": data.get("id"),
            "visibility": visibility,
            "visibility_ok": vis_match,
            "char_count": char_count,
            "byte_count": byte_count,
            "line_count": line_count,
            "slots_count": len(slots),
            "expected_slots": exp_slots,
            "slots_ok": slot_match,
            "greetings_count": len(greetings),
            "expected_greetings": exp_greetings,
            "greetings_ok": greeting_match,
            "messages_count": msg_count,
            "lorebook_ids": lorebook_ids,
            "lorebook_ids_ok": lb_match,
            "em_dashes_found": raw_text.count("\u2014"),
            "en_dashes_found": raw_text.count("\u2013")
        }

        if not (slot_match and greeting_match and lb_match and vis_match):
            report["overall_status"] = "FAIL"

    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()

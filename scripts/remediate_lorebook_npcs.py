#!/usr/bin/env python3
"""
scripts/remediate_lorebook_npcs.py

Milestone 2 (R2) Automated Mass Remediation and Live Deployment Tool:
1. Remediates FINAL/Svartulfr_NPC_Primary.json (99 entries):
   - Injects root gallery properties (gallery: [], gallery_count: 0)
   - Populates npc_info with {first_name, middle_names, last_name, nicknames, titles, npc_prefix}
   - Fixes the 10 legacy duplicate surname regexes
   - Preserves 13 ignored_characters, 2 ignored_personas on Alyssa and Jasper
   - Enforces selective: true on Alyssa and Jasper with Dossier secondary_keys; selective: false on remaining 97
2. Remediates FINAL/Svartulfr_NPC_Secondary.json (211 entries):
   - Ensures root gallery (gallery: [], gallery_count: 0)
   - Populates npc_info with 102 middle_names, 110 titles, and clean nicknames
   - Fixes the 10 legacy duplicate surname regexes (+ Jet Thompson)
   - Cleans umbrella keywords (Ariadne Cirillo, Brittany Willow, Damien Bishop secondary_keys)
   - Preserves ignored_characters on Edric Douglas, enforces selective: false across all 211 entries
3. Enforces 100% byte-for-byte entries == lexicon parity across FINAL/ and lorebooks/optimized/
4. Validates local files against scripts/verify_npc_schema_contract.py (asserting 0 defects)
5. Deploys updated lorebooks live to Wyvern API via authenticated PUT requests
6. Verifies live deployment state via GET requests (confirming 99 and 211 entries)
"""

import argparse
import copy
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from scripts.verify_npc_schema_contract import (
    validate_npc_info_schema,
    validate_avatar_gallery_contract,
    validate_anti_collision_contract,
    validate_entries_lexicon_parity,
    detect_duplicate_surnames,
    CANONICAL_BROAD_KEYS,
    audit_file,
)
from scratch.refresh_token import refresh as refresh_wyvern_token

PRIMARY_LOREBOOK_ID = "_zwEqgEEzh12X6gHVmMKKC"
SECONDARY_LOREBOOK_ID = "_Uht3Ckz44JBDrPnUHq7LV"

PRIMARY_BUDGET = 7500
SECONDARY_BUDGET = 5000
OFFICIAL_COVER = "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1e5124b4-f7d0-46cf-fad9-7ecfc801d100/public"

PRIMARY_FINAL_PATH = ROOT_DIR / "FINAL" / "Svartulfr_NPC_Primary.json"
SECONDARY_FINAL_PATH = ROOT_DIR / "FINAL" / "Svartulfr_NPC_Secondary.json"
PRIMARY_OPT_PATH = ROOT_DIR / "lorebooks" / "optimized" / "Svartulfr_NPC_Primary.json"
SECONDARY_OPT_PATH = ROOT_DIR / "lorebooks" / "optimized" / "Svartulfr_NPC_Secondary.json"


# ==============================================================================
# 1. Authoritative Primary NPC Catalog (99 Entries)
# ==============================================================================

PRIMARY_NPC_CATALOG = [
    # 00
    {"index": 0, "name": "Hugh Rivers", "first_name": "Hugh", "middle_names": [], "last_name": "Rivers", "titles": ["Alpha"], "nicknames": ["The Mountain Sovereign"], "npc_prefix": ""},
    {"index": 1, "name": "Liam O’Connor", "first_name": "Liam", "middle_names": [], "last_name": "O'Connor", "titles": [], "nicknames": ["Liam"], "npc_prefix": ""},
    {"index": 2, "name": "Bessie May", "first_name": "Bessie", "middle_names": [], "last_name": "May", "titles": [], "nicknames": ["Bessie"], "npc_prefix": ""},
    {"index": 3, "name": "Neve", "first_name": "Neve", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["The Archivist"], "npc_prefix": ""},
    {"index": 4, "name": "Jaelyn", "first_name": "Jaelyn", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["Jae"], "npc_prefix": ""},
    {"index": 5, "name": "Marek", "first_name": "Marek", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["The Iron Hammer", "Blue Devil", "Blue Oni"], "npc_prefix": ""},
    {"index": 6, "name": "Kian", "first_name": "Kian", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["The Ghost Feather", "Shadow Scout"], "npc_prefix": ""},
    {"index": 7, "name": "Goran", "first_name": "Goran", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["The Iron Ram", "Team Ukiyo Tank"], "npc_prefix": ""},
    {"index": 8, "name": "Radek", "first_name": "Radek", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["The Tactician", "Squad Leader"], "npc_prefix": ""},
    {"index": 9, "name": "Echo", "first_name": "Echo", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["E.C.H.O.", "familiar", "Jasper AI", "cyber familiar"], "npc_prefix": ""},
    # 10
    {"index": 10, "name": "Dominic Rogers", "first_name": "Dominic", "middle_names": ["Wayne"], "last_name": "Rogers", "titles": ["Mr."], "nicknames": ["Dom", "Bailey's Dad"], "npc_prefix": ""},
    {"index": 11, "name": "Roman Blackwood", "first_name": "Roman", "middle_names": [], "last_name": "Blackwood", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 12, "name": "Eric", "first_name": "Eric", "middle_names": [], "last_name": "", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 13, "name": "Javier Reyes", "first_name": "Javier", "middle_names": [], "last_name": "Reyes", "titles": [], "nicknames": ["Javi"], "npc_prefix": ""},
    {"index": 14, "name": "Raymond", "first_name": "Raymond", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["Ray"], "npc_prefix": ""},
    {"index": 15, "name": "Dean", "first_name": "Dean", "middle_names": [], "last_name": "", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 16, "name": "Bryson", "first_name": "Bryson", "middle_names": [], "last_name": "", "titles": ["Chief"], "nicknames": ["Chief Researcher", "MF Inc."], "npc_prefix": ""},
    {"index": 17, "name": "Scarlett Rose", "first_name": "Scarlett", "middle_names": [], "last_name": "Rose", "titles": [], "nicknames": ["Red"], "npc_prefix": ""},
    {"index": 18, "name": "Sierra Cruz", "first_name": "Sierra", "middle_names": [], "last_name": "Cruz", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 19, "name": "Varg Darkfire", "first_name": "Varg", "middle_names": [], "last_name": "Darkfire", "titles": [], "nicknames": ["The Patriarch", "The Old King", "Il Patriarca", "Vecchio Re"], "npc_prefix": ""},
    # 20
    {"index": 20, "name": "Karshin Darkfire", "first_name": "Karshin", "middle_names": [], "last_name": "Darkfire", "titles": ["Chief"], "nicknames": ["The Mastiff", "Chief of Security for HSK Consulting", "Il Mastino"], "npc_prefix": ""},
    {"index": 21, "name": "Boros Darkfire", "first_name": "Boros", "middle_names": [], "last_name": "Darkfire", "titles": [], "nicknames": ["The Bastion", "Logistics Director of HSK Consulting", "Il Bastione"], "npc_prefix": ""},
    {"index": 22, "name": "Aras Darkfire", "first_name": "Aras", "middle_names": [], "last_name": "Darkfire", "titles": [], "nicknames": ["The Whisper", "HR Director of HSK Consulting", "Il Sussurro"], "npc_prefix": ""},
    {"index": 23, "name": "Kolya Varenkov", "first_name": "Kolya", "middle_names": [], "last_name": "Varenkov", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 24, "name": "Russell 'Russ' Sinclair", "first_name": "Russell", "middle_names": [], "last_name": "Sinclair", "titles": [], "nicknames": ["Russ"], "npc_prefix": ""},
    {"index": 25, "name": "Daniel \"Danny\" Boone", "first_name": "Daniel", "middle_names": [], "last_name": "Boone", "titles": [], "nicknames": ["Danny"], "npc_prefix": ""},
    {"index": 26, "name": "Marlowe Voss", "first_name": "Marlowe", "middle_names": [], "last_name": "Voss", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 27, "name": "Cassian Aralas", "first_name": "Cassian", "middle_names": [], "last_name": "Aralas", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 28, "name": "Harrison Black", "first_name": "Harrison", "middle_names": [], "last_name": "Black", "titles": ["Councilman"], "nicknames": ["Harry"], "npc_prefix": ""},
    {"index": 29, "name": "Zero", "first_name": "Zero", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["Wrath"], "npc_prefix": ""},
    # 30
    {"index": 30, "name": "Zefir Hvitskog", "first_name": "Zefir", "middle_names": [], "last_name": "Hvitskog", "titles": [], "nicknames": ["White Ghost", "Firstborn"], "npc_prefix": ""},
    {"index": 31, "name": "Zeera Darkfire", "first_name": "Zeera", "middle_names": [], "last_name": "Darkfire", "titles": [], "nicknames": ["CEO of HSK Consulting", "Demonic Representative", "Horned Skull Clan Leader"], "npc_prefix": ""},
    {"index": 32, "name": "Wulfnic Báleygr Bloodmoon", "first_name": "Wulfnic", "middle_names": ["Báleygr"], "last_name": "Bloodmoon", "titles": ["Jarl", "Alpha"], "nicknames": ["The First Tusk", "Primo Zanna", "The Ancient", "Alpha of Alphas"], "npc_prefix": ""},
    {"index": 33, "name": "Vito Marino", "first_name": "Vito", "middle_names": [], "last_name": "Marino", "titles": [], "nicknames": ["Scar", "Ironworks Syndicate"], "npc_prefix": ""},
    {"index": 34, "name": "Viola Carter", "first_name": "Viola", "middle_names": [], "last_name": "Carter", "titles": [], "nicknames": ["Via"], "npc_prefix": ""},
    {"index": 35, "name": "Vincent Campbell", "first_name": "Vincent", "middle_names": [], "last_name": "Campbell", "titles": [], "nicknames": ["Vince", "Vi", "Ace"], "npc_prefix": ""},
    {"index": 36, "name": "Ut Berg", "first_name": "Ut", "middle_names": [], "last_name": "Berg", "titles": [], "nicknames": ["The Mountain", "Út Fjallit", "Firstborn"], "npc_prefix": ""},
    {"index": 37, "name": "Tomas Matthews", "first_name": "Tomas", "middle_names": [], "last_name": "Matthews", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 38, "name": "Tate", "first_name": "Tate", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["Subject 36"], "npc_prefix": ""},
    {"index": 39, "name": "Sullivan \"Sully\" Jones", "first_name": "Sullivan", "middle_names": [], "last_name": "Jones", "titles": [], "nicknames": ["Sully"], "npc_prefix": ""},
    # 40
    {"index": 40, "name": "Stanley Davies Sr.", "first_name": "Stanley", "middle_names": [], "last_name": "Davies", "titles": ["Mr."], "nicknames": ["Stanley Davies Sr."], "npc_prefix": ""},
    {"index": 41, "name": "Stanley Davies Jr.", "first_name": "Stanley", "middle_names": [], "last_name": "Davies", "titles": [], "nicknames": ["Stan", "Stanley Davies Jr."], "npc_prefix": ""},
    {"index": 42, "name": "Santiago Herrera", "first_name": "Santiago", "middle_names": [], "last_name": "Herrera", "titles": [], "nicknames": ["Santi", "Tank"], "npc_prefix": ""},
    {"index": 43, "name": "Ruaraidh \"Rory\" Ballantine", "first_name": "Ruaraidh", "middle_names": [], "last_name": "Ballantine", "titles": [], "nicknames": ["Rory"], "npc_prefix": ""},
    {"index": 44, "name": "Roland Vickers", "first_name": "Roland", "middle_names": ["Mark"], "last_name": "Vickers", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 45, "name": "Professor Loewe", "first_name": "Richard", "middle_names": [], "last_name": "Loewe", "titles": ["Professor"], "nicknames": ["Loewe"], "npc_prefix": ""},
    {"index": 46, "name": "Oskar", "first_name": "Oskar", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["Ozzie", "Squidface"], "npc_prefix": ""},
    {"index": 47, "name": "Noah Loki Douglas Bloodmoon", "first_name": "Noah", "middle_names": ["Loki"], "last_name": "Douglas Bloodmoon", "titles": [], "nicknames": ["The Grey Eminence", "Golden Boy"], "npc_prefix": ""},
    {"index": 48, "name": "Nixara Hvit Bloodmoon", "first_name": "Nixara", "middle_names": ["Hvit"], "last_name": "Bloodmoon", "titles": [], "nicknames": ["White Moon", "Pack Mom", "Whitemoon"], "npc_prefix": ""},
    {"index": 49, "name": "Nikolaj Jökull", "first_name": "Nikolaj", "middle_names": [], "last_name": "Jökull", "titles": [], "nicknames": ["Jokull", "eel", "marksman"], "npc_prefix": ""},
    # 50
    {"index": 50, "name": "Naomi Black", "first_name": "Naomi", "middle_names": [], "last_name": "Black", "titles": [], "nicknames": ["Uptown North"], "npc_prefix": ""},
    {"index": 51, "name": "Marcus Thornfield", "first_name": "Marcus", "middle_names": ["Iron"], "last_name": "Thornfield", "titles": [], "nicknames": ["Field Lead Marcus"], "npc_prefix": ""},
    {"index": 52, "name": "Marcus O'Connor", "first_name": "Marcus", "middle_names": [], "last_name": "O'Connor", "titles": [], "nicknames": ["Mark", "Oldtown"], "npc_prefix": ""},
    {"index": 53, "name": "Malachia Björn Douglas Bloodmoon", "first_name": "Malachia", "middle_names": ["Björn"], "last_name": "Douglas Bloodmoon", "titles": ["Alpha"], "nicknames": ["The Berserker", "Ghost", "The King"], "npc_prefix": ""},
    {"index": 54, "name": "Magnus Douglas III", "first_name": "Magnus", "middle_names": [], "last_name": "Douglas", "titles": ["III", "Sir"], "nicknames": ["Patriarch Magnus"], "npc_prefix": ""},
    {"index": 55, "name": "Mackenzie Sanchez-Rogers", "first_name": "Mackenzie", "middle_names": [], "last_name": "Sanchez-Rogers", "titles": [], "nicknames": ["Mac"], "npc_prefix": ""},
    {"index": 56, "name": "Lord Cornelius Douglas", "first_name": "Cornelius", "middle_names": [], "last_name": "Douglas", "titles": ["Lord"], "nicknames": [], "npc_prefix": ""},
    {"index": 57, "name": "Logan Járn Douglas", "first_name": "Logan", "middle_names": ["Dominic", "Járn"], "last_name": "Douglas", "titles": [], "nicknames": ["Uncle Logan", "The Peacemaker"], "npc_prefix": ""},
    {"index": 58, "name": "Kaladin Nargathon", "first_name": "Kaladin", "middle_names": ["Blackwolf"], "last_name": "Nargathon", "titles": ["Commander"], "nicknames": ["Kal", "Subject Zero"], "npc_prefix": ""},
    {"index": 59, "name": "Jean-Luc Virtuoso", "first_name": "Jean-Luc", "middle_names": [], "last_name": "Virtuoso", "titles": [], "nicknames": ["Jean", "The Maestro"], "npc_prefix": ""},
    # 60
    {"index": 60, "name": "Jasper Svartr Douglas Bloodmoon", "first_name": "Jasper", "middle_names": ["Svartr"], "last_name": "Douglas Bloodmoon", "titles": [], "nicknames": ["DJ Frequency", "Shadow Wolf", "Jasp"], "npc_prefix": ""},
    {"index": 61, "name": "Jasmin Thompson", "first_name": "Jasmin", "middle_names": [], "last_name": "Thompson", "titles": [], "nicknames": ["Jas"], "npc_prefix": ""},
    {"index": 62, "name": "Jared Thompson", "first_name": "Jared", "middle_names": [], "last_name": "Thompson", "titles": [], "nicknames": ["J-Man", "The Golden Bull"], "npc_prefix": ""},
    {"index": 63, "name": "Janice Thompson", "first_name": "Janice", "middle_names": [], "last_name": "Thompson", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 64, "name": "Isobel Blackwater", "first_name": "Isobel", "middle_names": [], "last_name": "Blackwater", "titles": [], "nicknames": ["Dockside"], "npc_prefix": ""},
    {"index": 65, "name": "Iordan R. Vess", "first_name": "Iordan", "middle_names": ["R."], "last_name": "Vess", "titles": ["Alpha"], "nicknames": ["Io"], "npc_prefix": ""},
    {"index": 66, "name": "Helena Weiss", "first_name": "Helena", "middle_names": [], "last_name": "Weiss", "titles": ["Professor"], "nicknames": ["Arcadia"], "npc_prefix": ""},
    {"index": 67, "name": "Harper Aries", "first_name": "Harper", "middle_names": [], "last_name": "Aries", "titles": [], "nicknames": ["Harp"], "npc_prefix": ""},
    {"index": 68, "name": "Harlan Beaumont", "first_name": "Harlan", "middle_names": [], "last_name": "Beaumont", "titles": [], "nicknames": ["Huck"], "npc_prefix": ""},
    {"index": 69, "name": "Hank Thompson", "first_name": "Hank", "middle_names": [], "last_name": "Thompson", "titles": ["Coach"], "nicknames": [], "npc_prefix": ""},
    # 70
    {"index": 70, "name": "GREED - Roxie", "first_name": "Roxie", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["Greed", "Rox"], "npc_prefix": ""},
    {"index": 71, "name": "GLUTTONY - Kevin", "first_name": "Kevin", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["Gluttony"], "npc_prefix": ""},
    {"index": 72, "name": "Finnegan Novak", "first_name": "Finnegan", "middle_names": [], "last_name": "Novak", "titles": [], "nicknames": ["Finn"], "npc_prefix": ""},
    {"index": 73, "name": "Federico \"Riki\" Savini", "first_name": "Federico", "middle_names": [], "last_name": "Savini", "titles": [], "nicknames": ["Riki"], "npc_prefix": ""},
    {"index": 74, "name": "Fade Greymoor", "first_name": "Mihaela", "middle_names": [], "last_name": "Greymoor", "titles": [], "nicknames": ["Fade"], "npc_prefix": ""},
    {"index": 75, "name": "Eris Davies", "first_name": "Eris", "middle_names": [], "last_name": "Davies", "titles": ["Mrs.", "Ms."], "nicknames": ["Stan's Mom"], "npc_prefix": ""},
    {"index": 76, "name": "Erik Ulfr Douglas", "first_name": "Erik", "middle_names": ["Cornelius", "Ulfr"], "last_name": "Douglas", "titles": ["Alpha", "Lord"], "nicknames": ["The Prime Alpha", "The Patriarch"], "npc_prefix": ""},
    {"index": 77, "name": "Elizabeth Duskwood", "first_name": "Elizabeth", "middle_names": [], "last_name": "Duskwood", "titles": ["Lady"], "nicknames": ["Nonna"], "npc_prefix": ""},
    {"index": 78, "name": "Eclipse Noir", "first_name": "Eclipse", "middle_names": [], "last_name": "Noir", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 79, "name": "ENVY - Siobhan", "first_name": "Siobhan", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["Envy"], "npc_prefix": ""},
    # 80
    {"index": 80, "name": "Dullahan", "first_name": "Dullahan", "middle_names": [], "last_name": "", "titles": ["Coach"], "nicknames": ["Coach D", "Dully"], "npc_prefix": ""},
    {"index": 81, "name": "Dr. Arthur Sinclair", "first_name": "Arthur", "middle_names": [], "last_name": "Sinclair", "titles": ["Dr."], "nicknames": ["Sloth", "The Alchemist"], "npc_prefix": ""},
    {"index": 82, "name": "Dominic Chen", "first_name": "Dominic", "middle_names": [], "last_name": "Chen", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 83, "name": "Darius Vale", "first_name": "Darius", "middle_names": [], "last_name": "Vale", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 84, "name": "Dante", "first_name": "Dante", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["Lust"], "npc_prefix": ""},
    {"index": 85, "name": "Chase Anderson", "first_name": "Chase", "middle_names": [], "last_name": "Anderson", "titles": [], "nicknames": ["Goldie"], "npc_prefix": ""},
    {"index": 86, "name": "Cass Harrow", "first_name": "Cass", "middle_names": [], "last_name": "Harrow", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 87, "name": "Casey Williams", "first_name": "Casey", "middle_names": [], "last_name": "Williams", "titles": [], "nicknames": ["Case"], "npc_prefix": ""},
    {"index": 88, "name": "Brak Ironfist", "first_name": "Brak", "middle_names": [], "last_name": "Ironfist", "titles": [], "nicknames": ["Orc Representative"], "npc_prefix": ""},
    {"index": 89, "name": "Bianca Rossi", "first_name": "Bianca", "middle_names": [], "last_name": "Rossi", "titles": [], "nicknames": ["Bia"], "npc_prefix": ""},
    # 90
    {"index": 90, "name": "Barrow", "first_name": "Barrow", "middle_names": [], "last_name": "", "titles": [], "nicknames": ["The Horns"], "npc_prefix": ""},
    {"index": 91, "name": "Barkley Rover", "first_name": "Barkley", "middle_names": [], "last_name": "Rover", "titles": ["Coach"], "nicknames": ["Barks", "Coach B"], "npc_prefix": ""},
    {"index": 92, "name": "Bailey Rogers", "first_name": "Bailey", "middle_names": [], "last_name": "Rogers", "titles": [], "nicknames": ["Red"], "npc_prefix": ""},
    {"index": 93, "name": "Aurora Night", "first_name": "Aurora", "middle_names": [], "last_name": "Night", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 94, "name": "Archer Wolfwood", "first_name": "Archer", "middle_names": [], "last_name": "Wolfwood", "titles": ["Chancellor"], "nicknames": ["Rettore"], "npc_prefix": ""},
    {"index": 95, "name": "Angelo Moreno", "first_name": "Angelo", "middle_names": [], "last_name": "Moreno", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 96, "name": "Andrew Campbell", "first_name": "Andrew", "middle_names": [], "last_name": "Campbell", "titles": [], "nicknames": ["Andy"], "npc_prefix": ""},
    {"index": 97, "name": "Abel Vilas ", "first_name": "Abel", "middle_names": [], "last_name": "Vilas", "titles": [], "nicknames": [], "npc_prefix": ""},
    {"index": 98, "name": "Alyssa Hvit Douglas Bloodmoon", "first_name": "Alyssa", "middle_names": ["Hvit"], "last_name": "Douglas Bloodmoon", "titles": [], "nicknames": ["White Moon", "Lyssa", "The Anchor"], "npc_prefix": ""},
]


# ==============================================================================
# 2. Curated Clean Regex Patterns for Defective Entries
# ==============================================================================

CLEAN_PRIMARY_REGEXES = {
    0: r"(?:^|\n)\s*(?:Hugh\ Rivers|Alpha\ Rivers|The\ Mountain\ Sovereign|Hugh)\s*:",
    10: r"(?:^|\n)\s*(?:Dominic\ Rogers|Dom\ Rogers|Dom|Mr\.\ Rogers|Dominic)\s*:",
    25: r'(?:^|\n)\s*(?:Daniel\ "Danny"\ Boone|Daniel\ Boone|Danny\ Boone|Danny|Boone|Daniel)\s*:',
    28: r"(?:^|\n)\s*(?:Harrison\ Black|Harry\ Black|Harry|Councilman\ Black|Harrison)\s*:",
    52: r"(?:^|\n)\s*(?:Marcus\ O'Connor|Mark\ O'Connor|Oldtown|Marcus)\s*:",
    66: r"(?:^|\n)\s*(?:Helena\ Weiss|Professor\ Weiss|Arcadia|Helena)\s*:",
    68: r"(?:^|\n)\s*(?:Harlan\ Beaumont|Huck\ Beaumont|Huck|Harlan)\s*:",
    73: r'(?:^|\n)\s*(?:Federico\ "Riki"\ Savini|Federico\ Savini|Riki\ Savini|Riki|Federico)\s*:',
    75: r"(?:^|\n)\s*(?:Eris\ Davies|Stan's\ Mom|ms\ davies|Mrs\.\ Davies|Eris)\s*:",
    77: r"(?:^|\n)\s*(?:Elizabeth\ Duskwood|Lady\ Duskwood|nonna|Elizabeth)\s*:",
}

CLEAN_SECONDARY_REGEXES = {
    0: r"(?:^|\n)\s*(?:Jet\ Thompson|Hank's\ son|Edric's\ friend|Jet)\s*:",
    2: r"(?:^|\n)\s*(?:Alicia\ Virtuoso|Mrs\.\ Virtuoso|Mrs\ Virtuoso|Jean\-Luc's\ wife|Alicia)\s*:",
    4: r"(?:^|\n)\s*(?:Ariadne\ Cirillo|Nurse\ Cirillo|Ari|Ariadne)\s*:",
    5: r"(?:^|\n)\s*(?:Luisa\ Sanchez\ Rogers|Luisa\ Rogers|Mac's\ older\ sister|Sanchez\ Rogers|Luisa)\s*:",
    6: r"(?:^|\n)\s*(?:Alistair\ Ambrose\ DeVille|Alistair\ DeVille|The\ Collector|Mr\.\ DeVille|Alistair)\s*:",
    8: r"(?:^|\n)\s*(?:Damien\ Bishop|The\ Hellhound\ Detective|Private\ Detective|Bishop|Damien)\s*:",
    17: r"(?:^|\n)\s*(?:Adelin\ Coso|Coach\ Coso|Adelin)\s*:",
    21: r"(?:^|\n)\s*(?:Professor\ Marit\ Christiansen|Professor\ Marit|Professor\ Christiansen|Marit\ Christiansen|Marit)\s*:",
    22: r"(?:^|\n)\s*(?:Professor\ Mollusk\ Moreau|Professor\ Mollusk|Professor\ Moreau|Mollusk\ Moreau|Mollusk)\s*:",
    39: r"(?:^|\n)\s*(?:Campus\ Staff\ Rat|Campus\ Rat|Rodent\ Campus\ Worker|Campus)\s*:",
    62: r"(?:^|\n)\s*(?:Graham\ Purcell|Major\ Purcell|Grizzly|Graham)\s*:",
}


# ==============================================================================
# 3. Remediation Functions
# ==============================================================================

def remediate_primary_lorebook(data: Dict[str, Any]) -> Dict[str, Any]:
    """Remediates FINAL/Svartulfr_NPC_Primary.json in-place."""
    # 1. Root Gallery & Metadata
    data["gallery"] = data.get("gallery", [])
    data["gallery_count"] = len(data["gallery"])
    data["token_budget"] = PRIMARY_BUDGET
    data["photoURL"] = OFFICIAL_COVER
    data["enableEntryHighlighting"] = True

    lexicon = data.get("lexicon", [])
    assert len(lexicon) == 99, f"Expected 99 entries in Primary, got {len(lexicon)}"

    for idx, e in enumerate(lexicon):
        spec = PRIMARY_NPC_CATALOG[idx]
        assert idx == spec["index"], f"Index mismatch: {idx} vs {spec['index']}"

        # 2. Populate npc_info
        e["npc_info"] = {
            "first_name": spec["first_name"],
            "middle_names": copy.deepcopy(spec["middle_names"]),
            "last_name": spec["last_name"] if spec["last_name"] else None,
            "nicknames": copy.deepcopy(spec["nicknames"]),
            "titles": copy.deepcopy(spec["titles"]),
            "npc_prefix": spec["npc_prefix"],
        }

        # 3. Regex Duplicate Surname Fix
        if idx in CLEAN_PRIMARY_REGEXES:
            e["avatar_activation_regex"] = CLEAN_PRIMARY_REGEXES[idx]
        e["custom_avatar_regex"] = True
        e["lines_parsed"] = 1

        # 4. Anti-Collision Rules
        # Alyssa & Jasper: selective: true with Dossier keys
        if idx in (60, 98):  # Jasper (60), Alyssa (98)
            e["selective"] = True
            e["secondary_keys"] = ["Dossier", "Scheda", "Archivio", "Database", "Profilo"]
            e["key_logic"] = "AND_ANY"
        else:
            e["selective"] = False
            e["secondary_keys"] = []

        # Ensure no broad umbrella keywords in keys
        e["keys"] = [k for k in e.get("keys", []) if isinstance(k, str) and k.strip().lower() not in CANONICAL_BROAD_KEYS]

        # 5. Sentinel Directive Toggles: Scan Persona, Whole Words Only, Highlighting
        e["scan_persona"] = True
        e["whole_words_only"] = True
        e["highlight_keys"] = True
        e["enable_highlighting"] = True
        ext = e.get("extensions") if isinstance(e.get("extensions"), dict) else {}
        ext["highlight_keys"] = True
        e["extensions"] = ext

    # 6. Mirror lexicon to entries byte-for-byte
    data["entries"] = copy.deepcopy(data["lexicon"])
    return data


def remediate_secondary_lorebook(data: Dict[str, Any]) -> Dict[str, Any]:
    """Remediates FINAL/Svartulfr_NPC_Secondary.json in-place."""
    # 1. Root Gallery & Metadata
    data["gallery"] = data.get("gallery", [])
    data["gallery_count"] = len(data["gallery"])
    data["token_budget"] = SECONDARY_BUDGET
    data["photoURL"] = OFFICIAL_COVER
    data["enableEntryHighlighting"] = True

    lexicon = data.get("lexicon", [])
    assert len(lexicon) == 211, f"Expected 211 entries in Secondary, got {len(lexicon)}"

    for idx, e in enumerate(lexicon):
        info = e.get("npc_info", {})
        fn = info.get("first_name", e.get("name", "").split()[0])
        ln = info.get("last_name", "")
        nicks = copy.deepcopy(info.get("nicknames", []))
        titles = copy.deepcopy(info.get("titles", []))
        mid_names: List[str] = []

        # 2. Extract Middle Names (102 entries)
        if 111 <= idx <= 210:
            # Camp Mystic campers (111-190) and counselors (191-210)
            three_tokens = [k for k in e.get("keys", []) if len(k.split()) == 3]
            if three_tokens:
                mid_names = [three_tokens[0].split()[1]]
        elif idx == 5:  # Luisa Sanchez Rogers
            mid_names = ["Sanchez"]
            ln = "Rogers"
        elif idx == 6:  # Alistair Ambrose DeVille
            mid_names = ["Ambrose"]
            ln = "DeVille"

        # 3. Nickname & Keyword Sanitation
        if idx == 4:  # Ariadne Cirillo
            nicks = ["Ari", "Nurse Cirillo"]
        elif idx == 7:  # Cato
            nicks = ["The Gator", "Guard Dog"]
        elif idx == 8:  # Damien Bishop
            nicks = ["The Hellhound Detective", "Private Detective"]
            # Purge 'demon' from secondary_keys
            e["secondary_keys"] = [k for k in e.get("secondary_keys", []) if k.strip().lower() != "demon"]
        elif idx == 9:  # Everett Rottmore
            nicks = ["The Mortician", "The Fixer", "Bone Mask"]
        elif idx == 10:  # Vasile Ionescu
            nicks = ["The Jailer", "The Trapper"]
        elif idx == 18:  # Brittany Willow
            nicks = ["Malachia super-fan"]
        elif idx == 39:  # Campus Staff Rat
            nicks = ["Rodent Campus Worker"]
        elif idx == 40:  # Adrian
            nicks = ["Adrian the Baker"]
        elif idx == 80:  # Professor Dryden Kiwetin
            nicks = ["Wîhtikow"]
        elif idx == 88:  # Siebren Dijkstra
            nicks = []

        # Filter out any accidental broad umbrella keys
        nicks = [n for n in nicks if isinstance(n, str) and n.strip().lower() not in CANONICAL_BROAD_KEYS]
        e["keys"] = [k for k in e.get("keys", []) if isinstance(k, str) and k.strip().lower() not in CANONICAL_BROAD_KEYS]
        if "secondary_keys" in e and isinstance(e["secondary_keys"], list):
            e["secondary_keys"] = [k for k in e["secondary_keys"] if isinstance(k, str) and k.strip().lower() not in CANONICAL_BROAD_KEYS]

        # 4. Populate npc_info
        e["npc_info"] = {
            "first_name": str(fn).strip(),
            "middle_names": [str(m).strip() for m in mid_names if str(m).strip()],
            "last_name": str(ln).strip() if ln else None,
            "nicknames": nicks,
            "titles": titles,
            "npc_prefix": "",
        }

        # 5. Regex Duplicate Surname Fix
        if idx in CLEAN_SECONDARY_REGEXES:
            e["avatar_activation_regex"] = CLEAN_SECONDARY_REGEXES[idx]
        e["custom_avatar_regex"] = True
        e["lines_parsed"] = 1

        # 6. Anti-Collision Rules: all 211 selective: false
        e["selective"] = False

        # 7. Sentinel Directive Toggles: Scan Persona, Whole Words Only, Highlighting
        e["scan_persona"] = True
        e["whole_words_only"] = True
        e["highlight_keys"] = True
        e["enable_highlighting"] = True
        ext = e.get("extensions") if isinstance(e.get("extensions"), dict) else {}
        ext["highlight_keys"] = True
        e["extensions"] = ext

    # 8. Mirror lexicon to entries byte-for-byte
    data["entries"] = copy.deepcopy(data["lexicon"])
    return data


# ==============================================================================
# 4. Validation Suite
# ==============================================================================

def validate_remediated_lorebooks(prim: Dict[str, Any], sec: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Runs authoritative contract verifiers across both in-memory lorebook dictionaries."""
    errors = []

    # 1. Root Gallery Checks
    ok_g_p, errs_g_p = validate_avatar_gallery_contract(lorebook_root=prim)
    if not ok_g_p:
        errors.extend([f"Primary Root Gallery: {e}" for e in errs_g_p])

    ok_g_s, errs_g_s = validate_avatar_gallery_contract(lorebook_root=sec)
    if not ok_g_s:
        errors.extend([f"Secondary Root Gallery: {e}" for e in errs_g_s])

    # 2. Parity Checks
    ok_p_p, errs_p_p = validate_entries_lexicon_parity(prim)
    if not ok_p_p:
        errors.extend([f"Primary Parity: {e}" for e in errs_p_p])

    ok_p_s, errs_p_s = validate_entries_lexicon_parity(sec)
    if not ok_p_s:
        errors.extend([f"Secondary Parity: {e}" for e in errs_p_s])

    # 3. Primary Entries Check
    prim_lex = prim.get("lexicon", [])
    if len(prim_lex) != 99:
        errors.append(f"Primary lexicon length ({len(prim_lex)}) != 99")

    for idx, e in enumerate(prim_lex):
        name = e.get("name", f"Entry_{idx}")
        # Avatar
        ok_a, errs_a = validate_avatar_gallery_contract(entry=e)
        if not ok_a:
            errors.append(f"Primary [{idx}] {name} Avatar: {'; '.join(errs_a)}")
        # npc_info
        info = e.get("npc_info")
        ok_n, errs_n = validate_npc_info_schema(info)
        if not ok_n:
            errors.append(f"Primary [{idx}] {name} npc_info: {'; '.join(errs_n)}")
        # Duplicate surnames in regex
        regex = e.get("avatar_activation_regex", "")
        ln = info.get("last_name") if isinstance(info, dict) else None
        dupes = detect_duplicate_surnames(regex, ln)
        if dupes:
            errors.append(f"Primary [{idx}] {name} Duplicate Surname: {dupes}")
        # Anti-collision
        ok_ac, errs_ac = validate_anti_collision_contract(e)
        if not ok_ac:
            errors.append(f"Primary [{idx}] {name} Anti-Collision: {'; '.join(errs_ac)}")

    # 4. Secondary Entries Check
    sec_lex = sec.get("lexicon", [])
    if len(sec_lex) != 211:
        errors.append(f"Secondary lexicon length ({len(sec_lex)}) != 211")

    for idx, e in enumerate(sec_lex):
        name = e.get("name", f"Entry_{idx}")
        # Avatar
        ok_a, errs_a = validate_avatar_gallery_contract(entry=e)
        if not ok_a:
            errors.append(f"Secondary [{idx}] {name} Avatar: {'; '.join(errs_a)}")
        # npc_info
        info = e.get("npc_info")
        ok_n, errs_n = validate_npc_info_schema(info)
        if not ok_n:
            errors.append(f"Secondary [{idx}] {name} npc_info: {'; '.join(errs_n)}")
        # Duplicate surnames in regex
        regex = e.get("avatar_activation_regex", "")
        ln = info.get("last_name") if isinstance(info, dict) else None
        dupes = detect_duplicate_surnames(regex, ln)
        if dupes:
            errors.append(f"Secondary [{idx}] {name} Duplicate Surname: {dupes}")
        # Anti-collision
        ok_ac, errs_ac = validate_anti_collision_contract(e)
        if not ok_ac:
            errors.append(f"Secondary [{idx}] {name} Anti-Collision: {'; '.join(errs_ac)}")

    return len(errors) == 0, errors


# ==============================================================================
# 5. File Persistence
# ==============================================================================

def save_remediated_files(prim: Dict[str, Any], sec: Dict[str, Any]):
    """Saves remediated lorebooks to FINAL/ and mirrors identically to lorebooks/optimized/."""
    for path in [PRIMARY_FINAL_PATH, PRIMARY_OPT_PATH]:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(prim, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"  [SAVED] {path.relative_to(ROOT_DIR)} ({path.stat().st_size:,} bytes)")

    for path in [SECONDARY_FINAL_PATH, SECONDARY_OPT_PATH]:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(sec, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"  [SAVED] {path.relative_to(ROOT_DIR)} ({path.stat().st_size:,} bytes)")


# ==============================================================================
# 6. Live Wyvern Web API Deployment
# ==============================================================================

def build_compact_put_payload(data: Dict[str, Any]) -> bytes:
    # Omit provenance metadata from entries in PUT payload to guarantee body size stays under 1MB Next.js / Cloudflare limit
    clean_lexicon = []
    for e in data.get("lexicon", []):
        ec = dict(e)
        ec.pop("provenance", None)
        clean_lexicon.append(ec)

    compact = {
        "name": data.get("name"),
        "description": data.get("description", ""),
        "photoURL": data.get("photoURL"),
        "token_budget": data.get("token_budget"),
        "visibility": data.get("visibility", "private"),
        "rating": data.get("rating", "explicit"),
        "scan_depth": data.get("scan_depth", 5),
        "recursive_scanning": data.get("recursive_scanning", True),
        "enableEntryHighlighting": data.get("enableEntryHighlighting", True),
        "gallery": data.get("gallery", []),
        "gallery_count": len(data.get("gallery", [])),
        "lexicon": clean_lexicon,
    }
    return json.dumps(compact, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def deploy_live_lorebooks(prim: Dict[str, Any], sec: Dict[str, Any]) -> bool:
    """Executes authenticated PUT requests and GET verifications for both lorebooks."""
    print("\n" + "=" * 70)
    print("EXECUTING LIVE WYVERN WEB API DEPLOYMENT")
    print("=" * 70)

    token = refresh_wyvern_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json",
    }

    # 1. Deploy Primary Lorebook
    prim_bytes = build_compact_put_payload(prim)
    print(f"\n[Deploying Primary Lorebook: {PRIMARY_LOREBOOK_ID}]")
    print(f"  Payload size: {len(prim_bytes):,} bytes ({len(prim['lexicon'])} entries)")
    url_prim = f"https://app.wyvern.chat/api/lorebooks/{PRIMARY_LOREBOOK_ID}"
    req_prim = urllib.request.Request(url_prim, data=prim_bytes, headers=headers, method="PUT")

    try:
        with urllib.request.urlopen(req_prim, timeout=90) as resp:
            print(f"  [SUCCESS] Primary Lorebook PUT returned HTTP {resp.status} {resp.reason}")
    except urllib.error.HTTPError as e:
        print(f"  [FAILED] Primary Lorebook PUT failed: HTTP {e.code} {e.reason}")
        print(e.read().decode("utf-8", errors="replace"))
        return False

    # Pacing delay between calls
    print("  Pacing delay: waiting 2.5 seconds...")
    time.sleep(2.5)

    # 2. Deploy Secondary Lorebook
    sec_bytes = build_compact_put_payload(sec)
    print(f"\n[Deploying Secondary Lorebook: {SECONDARY_LOREBOOK_ID}]")
    print(f"  Payload size: {len(sec_bytes):,} bytes ({len(sec['lexicon'])} entries)")
    url_sec = f"https://app.wyvern.chat/api/lorebooks/{SECONDARY_LOREBOOK_ID}"
    req_sec = urllib.request.Request(url_sec, data=sec_bytes, headers=headers, method="PUT")

    try:
        with urllib.request.urlopen(req_sec, timeout=90) as resp:
            print(f"  [SUCCESS] Secondary Lorebook PUT returned HTTP {resp.status} {resp.reason}")
    except urllib.error.HTTPError as e:
        print(f"  [FAILED] Secondary Lorebook PUT failed: HTTP {e.code} {e.reason}")
        print(e.read().decode("utf-8", errors="replace"))
        return False

    # Pacing delay before verification
    print("  Pacing delay: waiting 2.5 seconds before verification...")
    time.sleep(2.5)

    # 3. Post-Deployment Verification GET
    print("\n[Verifying Live Lorebooks via GET API]")
    get_req_prim = urllib.request.Request(url_prim, headers=headers, method="GET")
    with urllib.request.urlopen(get_req_prim, timeout=60) as resp:
        live_prim = json.loads(resp.read().decode("utf-8"))
        live_p_count = len(live_prim.get("lexicon", []))
        print(f"  Primary: HTTP {resp.status}, Name: '{live_prim.get('name')}', Live Entries: {live_p_count}, Budget: {live_prim.get('token_budget')}")
        assert live_p_count == 99, f"Expected 99 live entries in Primary, got {live_p_count}"

    get_req_sec = urllib.request.Request(url_sec, headers=headers, method="GET")
    with urllib.request.urlopen(get_req_sec, timeout=60) as resp:
        live_sec = json.loads(resp.read().decode("utf-8"))
        live_s_count = len(live_sec.get("lexicon", []))
        print(f"  Secondary: HTTP {resp.status}, Name: '{live_sec.get('name')}', Live Entries: {live_s_count}, Budget: {live_sec.get('token_budget')}")
        assert live_s_count == 211, f"Expected 211 live entries in Secondary, got {live_s_count}"

    print("\n[LIVE DEPLOYMENT & VERIFICATION 100% SUCCESSFUL]")
    return True


# ==============================================================================
# 7. Main Runner
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Milestone 2 (R2) Lorebook NPC Remediation & Live Deployment")
    parser.add_argument("--dry-run", action="store_true", help="Perform in-memory remediation and contract validation without saving")
    parser.add_argument("--apply", action="store_true", help="Remediate and save to FINAL/ and lorebooks/optimized/")
    parser.add_argument("--deploy", action="store_true", help="Deploy remediated lorebooks live via Wyvern Web API")
    parser.add_argument("--all", action="store_true", help="Execute complete pipeline: remediate, save, validate, and deploy")
    args = parser.parse_args()

    # Default to --all if no specific flag given
    if not (args.dry_run or args.apply or args.deploy or args.all):
        args.all = True

    should_save = args.apply or args.all
    should_deploy = args.deploy or args.all

    print("=" * 70)
    print("STARTING MILESTONE 2 (R2) LOREBOOK NPC REMEDIATION PIPELINE")
    print("=" * 70)

    # 1. Load Source Files
    print("\n[Loading Local Lorebook Source Files]")
    with open(PRIMARY_FINAL_PATH, "r", encoding="utf-8") as f:
        prim_data = json.load(f)
    print(f"  Loaded Primary: {PRIMARY_FINAL_PATH.name} ({len(prim_data.get('lexicon', []))} entries)")

    with open(SECONDARY_FINAL_PATH, "r", encoding="utf-8") as f:
        sec_data = json.load(f)
    print(f"  Loaded Secondary: {SECONDARY_FINAL_PATH.name} ({len(sec_data.get('lexicon', []))} entries)")

    # 2. Execute Remediation
    print("\n[Executing Remediation Logic]")
    prim_remed = remediate_primary_lorebook(prim_data)
    print("  [OK] Primary Lorebook remediated (99 entries).")

    sec_remed = remediate_secondary_lorebook(sec_data)
    print("  [OK] Secondary Lorebook remediated (211 entries).")

    # 3. Contract Pre-Save Validation
    print("\n[Executing Strict Contract Verification]")
    valid, errors = validate_remediated_lorebooks(prim_remed, sec_remed)
    if not valid:
        print(f"\n[FATAL] Remediation failed contract verification ({len(errors)} defects):")
        for err in errors[:20]:
            print(f"  - {err}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors.")
        sys.exit(1)

    print("  [PASS] 0 contract defects found across all 310 entries!")
    print("  [PASS] Root gallery valid on both lorebooks.")
    print("  [PASS] Entries == Lexicon byte-for-byte parity verified.")
    print("  [PASS] 0 duplicate surname regex defects detected.")
    print("  [PASS] 0 umbrella keyword violations found.")

    # 4. Save to Disk
    if should_save:
        print("\n[Persisting Remediated Files to Disk]")
        save_remediated_files(prim_remed, sec_remed)
    else:
        print("\n[DRY RUN] Skipping file persistence.")

    # 5. Live Deployment
    if should_deploy:
        success = deploy_live_lorebooks(prim_remed, sec_remed)
        if not success:
            print("\n[FATAL] Live deployment failed.")
            sys.exit(1)

    print("\n" + "=" * 70)
    print("MILESTONE 2 (R2) REMEDIATION PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()

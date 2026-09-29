import os
import re
import json
import sys
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')

EP = datetime(827, 12, 21, 0, 0, 0, tzinfo=timezone.utc)

def d_to_h(y, m, d, h=0):
    dt = datetime(y, m, d, h, 0, 0, tzinfo=timezone.utc)
    return int((dt - EP).total_seconds() // 3600)

def h_to_d(hours):
    dt = EP + timedelta(hours=hours)
    return dt.strftime('%Y-%m-%d')

with open('scratch/g2_canonical_list.json', encoding='utf-8') as f:
    g2_list = json.load(f)

with open('exports/Svartulfr_Export.json', encoding='utf-8') as f:
    world = json.load(f)
chars_by_id = {c['id']: c for c in world['world_characters']}

# Load all claude docs
doc_dir = 'docs/claude_project_docs'
docs = {}
for fname in os.listdir(doc_dir):
    with open(os.path.join(doc_dir, fname), encoding='utf-8', errors='ignore') as f:
        docs[fname] = f.read()

# Known explicit dates from dedicated completion docs and verified canon
# Format: (year, month, day)
known_dates = {
    # Main / Family / Council / Representatives
    "Eithne Dal'Kereth": (1945, 9, 21), # Existing 9799056
    "Yael": (1998, 7, 24), # Existing 10261128
    "Bryson": (1966, 3, 1), # Existing 9977496
    "Mackenzie Sanchez-Rogers": (1999, 10, 5), # Existing 10270512
    "Jared Thompson": (2001, 11, 3), # Existing 10287000
    
    # SUCC Students & Class of 2024
    "Vincent Campbell": (2000, 8, 8), # August 8, 2000 -> 10279080
    "Andrew Campbell": (2002, 3, 7), # March 7, 2002 -> 10292904
    "Tomas Matthews": (2003, 4, 2), # April 2, 2003 -> 10302288
    "Santiago Herrera": (2002, 10, 12), # October 12, 2002 -> 10298160
    "Sierra": (2005, 9, 8), # September 8, 2005 -> 10323648 (18yo, turns 19 Sept 2024)
    "Scarlett Rose": (2005, 11, 18), # November 18, 2005 -> 10325352 (18yo)
    "Brittany Willow": (2004, 8, 2), # August 2, 2004 -> 10313976 (20yo)
    "Chase Anderson": (2003, 8, 11), # August 11, 2003 -> 10305432 (20yo, turns 21 Aug 2024)
    "Bailey Rogers": (2003, 5, 18), # Incubus student, 20yo -> 10303416
    "Ariadne Cirillo": (2002, 6, 14), # "reads about 22", nurse/student -> 10295280
    "Finnegan Novak": (2002, 11, 25), # SUCC Bears hockey, 21yo -> 10299216
    "Casey Williams": (1996, 7, 19), # 27 anni, falco -> 10243536
    "Stanley Davies Jr.": (2002, 9, 14), # 21 anni -> 10297488
    "Janice Thompson": (2003, 2, 15), # 21 anni, Mu Omega Omega, cheerleader -> 10301184
    "Iordan R. Vess": (1996, 11, 20), # 27 anni, Delta werewolf -> 10246512
    "Tate": (2001, 4, 18), # Dog demihuman lab survivor, 22/23yo -> 10285632
    "Nikolaj Jökull": (1995, 12, 8), # 28 anni, eel demihuman lab survivor -> 10238160
    "Oskar": (2003, 1, 20), # early twenties, hivemind lab survivor -> 10300560
    "Kolya Varenkov": (2000, 4, 14), # 24 anni, vampire -> 10276056
    "Fade Greymoor": (1999, 10, 14), # 24 anni, Grave Mistake -> 10271904
    "Roland Vickers": (2000, 6, 14), # 23 anni, Grave Mistake -> 10277520
    "Viola Carter": (2001, 9, 30), # 22 anni, Grave Mistake -> 10289616
    "Venera Dolce": (2000, 11, 3), # 23 anni, cheerleader -> 10281168

    # The Five Cocketeers (Solarton_FiveCocketeers_2026-09-15.md)
    "Dean": (2002, 11, 3), # 21 anni -> 10298688
    "Russ Sinclair": (2002, 8, 14), # 21 anni -> 10296744
    "Javier Reyes": (2001, 12, 5), # 22 anni -> 10291176
    "Eric": (2003, 9, 27), # 20 anni -> 10306560
    "Raymond": (2001, 10, 30), # 22 anni -> 10290312

    # Staff SUCC
    "Barkley Rover": (1992, 3, 12), # 32 anni -> 10205376
    "Coach Mithers": (1978, 8, 4), # Manticore coach, August 4 -> 10086240 (45yo)
    "Adelin Coso": (1975, 5, 9), # Abominable snowman, May 9 -> 10057872 (48yo, looks 30)
    "Professor Loewe": (1971, 7, 22), # 52 anni -> 10024560
    "Professor Marit Christiansen": (1995, 1, 15), # appears mid/late 20s, ancient -> 10230288
    "Professor Mollusk Moreau": (1968, 6, 11), # 55 anni -> 9997176
    "Hideo Reid": (1967, 11, 14), # 56 anni -> 9992136

    # Thompson & Davies Family / Alumni
    "Hank Thompson": (1973, 8, 19), # 50 anni -> 10042464
    "Jasmin Thompson": (1975, 10, 24), # 48 anni -> 10061904
    "Stanley Davies Sr.": (1974, 4, 16), # 50 anni -> 10048248
    "Eris Davies": (1980, 5, 12), # 43 anni -> 10101792
    "Allegra Lumsden": (1973, 11, 28), # 50 anni -> 10044888
    "Luisa Sanchez Rogers": (1938, 7, 14), # 85 anni -> 9735408
    "Dominic Rogers": (1973, 11, 3), # 50 anni -> 10044312

    # Blackwood District Alphas & Concilio (Import_Plan_AllContent.md & Concilio docs)
    "Vito Marino": (1901, 3, 22), # Pureblood, born 1901 -> 9408336 (or 1974-03-22 -> 10047648)
    "Bianca Rossi": (1989, 7, 8), # 1989-07-08 -> 10182312
    "Cass Harrow": (1979, 4, 15), # 1979-04-15 -> 10092360
    "Dominic Chen": (1986, 9, 9), # 1986-09-09 -> 10157520
    "Eclipse Noir": (2000, 6, 21), # 2000-06-21 -> 10277688
    "Isobel Blackwater": (1969, 11, 10), # 1969-11-10 -> 10009584
    "Federico \"Riki\" Savini": (1959, 10, 3), # 1959-10-03 -> 9921432
    "Naomi Black": (1982, 6, 18), # co-leader Uptown North, ~41yo -> 10120176
    "Darius Vale": (1978, 11, 14), # Uptown South, 45 anni -> 10088688
    "Marcus O'Connor": (1905, 5, 12), # Oldtown Pureblood, born 1905 -> 9444648
    "Helena Weiss": (1970, 9, 23), # Arcadia leader, 53yo -> 10017216
    "Aurora Night": (1984, 8, 16), # Bluemoon North -> 10139424
    "Harrison Black": (1978, 10, 14), # 45 anni -> 10087944
    "Abel Vilas": (1993, 9, 2), # 30 anni -> 10218312
    "Cassian Aralas": (1711, 6, 15), # 312 anni -> 7744920
    "Marlowe Voss": (1943, 3, 12), # 81 anni -> 9776184
    "Zeera": (1989, 10, 24), # 34 anni -> 10184904
    "Brak Ironfist": (1976, 8, 17), # 47 anni -> 10068792
    "Barrow": (1981, 11, 9), # 42 anni -> 10114872
    "Harlan Beaumont": (1975, 6, 12), # Huck Beaumont, 48 anni -> 10058688

    # Los Angeles & The Sinners & Ballantine
    "Jean-Luc Virtuoso": (1985, 4, 22), # 38 anni -> 10145400
    "Alicia Virtuoso": (1988, 5, 14), # ~35 anni -> 10172232
    "Zero": (1999, 3, 7), # 24 anni -> 10266624
    "Dr. Arthur Sinclair": (1959, 8, 14), # 64 anni -> 9920232
    "Dante": (1420, 6, 18), # centuries old incubus -> 5193912
    "Daniel \"Danny\" Boone": (1999, 7, 19), # 24 anni -> 10269840
    "Sullivan \"Sully\" Jones": (1968, 3, 2), # 55 anni -> 9994680
    "Harper Aries": (2003, 5, 11), # 20 anni -> 10303248
    "Ruaraidh \"Rory\" Ballantine": (1977, 2, 15), # 46 anni -> 10073376
    "GREED - Roxie": (1996, 4, 18), # 27 anni -> 10241352
    "GLUTTONY - Kevin": (2001, 8, 22), # 22 anni -> 10288632
    "ENVY - Siobhan": (1910, 10, 14), # century-old vampire -> 9492168

    # Immortals & Ancients
    "Archer Wolfwood": (1846, 5, 14), # 1846-05-14 -> 8928648
    "Angelo Moreno": (1484, 6, 10), # 1484-06-10 -> 5755080
    "Dullahan": (1724, 4, 11), # 1724-04-11 -> 7857288
    "Rev": (1795, 5, 6), # Greater Incubus, May 6 -> 8480376
    "Roman Blackwood": (2000, 8, 25), # 23 anni -> 10279488
}

print(f"Total mapped characters: {len(known_dates)}")
missing = [c['name'] for c in g2_list if c['name'] not in known_dates]
print(f"Missing from map: {len(missing)}")
for m in missing:
    print(f" - {m}")

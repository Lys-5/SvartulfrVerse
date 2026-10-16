# -*- coding: utf-8 -*-
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

species_list = json.load(open(os.path.join(ROOT, "scratch", "rpg_species_catalog.json"), encoding="utf-8"))
occs_list = json.load(open(os.path.join(ROOT, "scratch", "rpg_occupations_catalog.json"), encoding="utf-8"))
traits_list = json.load(open(os.path.join(ROOT, "scratch", "rpg_traits_catalog.json"), encoding="utf-8"))

species_map = {s["id"]: s for s in species_list}
occs_map = {o["id"]: o for o in occs_list}
traits_map = {t["id"]: t for t in traits_list}

# Ensure the 5 updated traits from update_missing_trait_modifiers.js + Pack Leader have their exact modifiers
extra_trait_mods = {
    "_NL4ANGp2gjKtbAgRTFxbD": {
        "name": "Apex Predator Divine Core",
        "description": "Consacrato dal Dio Lupo Fenris. Immunita biologica totale, sensi onnidirezionali e aura che proietta la supremazia fisica e carismatica dei Firstborn.",
        "stat_modifiers": {"strength": 3, "endurance": 3, "perception": 2, "charisma": 2},
    },
    "_L2xQk9j8RnMKUgGnCVWRR": {
        "name": "Berserker Internal Furnace",
        "description": "Metabolismo ipertermico a consumo di ferro. La forza e la rigenerazione scalano in modo colossale in battaglia a scapito di un consumo metabolico e di ferro accelerato.",
        "stat_modifiers": {"strength": 3, "endurance": 3, "agility": 1, "intelligence": -1},
    },
    "_kUV13hFp2R2a4aYEXq3c4": {
        "name": "Familiar Soulbound Synergy",
        "description": "Legame simbiotico profondo con un compagno animale sovrannaturale, con condivisione di percezione sensoriale e risonanza aurica.",
        "stat_modifiers": {"perception": 2, "intelligence": 2, "charisma": 1},
    },
    "_C8XXTwLd1mmF33EkQMUyD": {
        "name": "Puppeteer Mana Strings",
        "description": "Capacita di tessere fili di mana invisibili per controllare burattini, simulacri o guidare traiettorie con precisione millimetrica.",
        "stat_modifiers": {"agility": 2, "intelligence": 2, "perception": 1, "strength": -1},
    },
    "_AQ6Qy4KHMDgFWKPHDJeqb": {
        "name": "Technomantic Data Resonance",
        "description": "Capacita di percepire il flusso di bit e la fibra ottica come tessuto eterico vivo, canalizzando incantesimi attraverso circuiti elettronici e reti digitali.",
        "stat_modifiers": {"intelligence": 3, "perception": 2, "strength": -1},
    },
}

for tid, tdata in extra_trait_mods.items():
    if tid in traits_map:
        if not traits_map[tid].get("stat_modifiers"):
            traits_map[tid]["stat_modifiers"] = tdata["stat_modifiers"]
    else:
        traits_map[tid] = {"id": tid, **tdata}

# Check if any trait in traits_map has empty stat_modifiers
for tid, t in traits_map.items():
    if not t.get("stat_modifiers"):
        print("Trait without modifiers:", tid, t.get("name"))

# Build name -> trait map as well (for Alyssa whose traits were listed by name in sync_alyssa_traits.js)
trait_by_name = {t["name"].lower(): t for t in traits_map.values()}

STAT_KEYS = ["strength", "perception", "endurance", "charisma", "intelligence", "agility", "luck"]
STAT_ABBR = {
    "strength": "STR",
    "perception": "PER",
    "endurance": "END",
    "charisma": "CHA",
    "intelligence": "INT",
    "agility": "AGI",
    "luck": "LCK",
}

# All 22 characters (10 Batch 1 + 8 Batch 2 + Alyssa + Edric + Marek + Dullahan)
CHARACTERS_RPG = [
    {
        "key": "alyssa",
        "name": "Alyssa Hvit Douglas Bloodmoon",
        "lbSearch": "{{user}} Hvit Douglas Bloodmoon",
        "level": 3,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_zdew8qxchkMDcJf6Ge39t", # Pre-Med / Healer
        "speciesName": "Werewolf (Founding Bloodline & Pureblood Dominant Omega)",
        "occupationName": "Novice Healing Mage, Pre-Med Healer",
        "className": "Guild Support (Healer/Mage)",
        "base_stats": {"strength": 8, "perception": 9, "endurance": 10, "charisma": 8, "intelligence": 11, "agility": 15, "luck": 20},
        "traitIds": [
            "_4nTUFT2tfNAjdTKXHfgUc", # Night Stalker
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_8YMa2gRKXFMBrWYzx2jqD", # Founding Bloodline
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_DMMAzBKW3b8wPd9rq6TWp", # The White Moon (Omega)
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
            "_LNe6dhHnxx7BCfXeMERzc", # Eternal Optimist
            "_QT6N7KhahqwqkJVaMXhY9", # Pre-Med / Healer
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_VrgTBJR3aEyW3FBD1zLkR", # Dungeon Veteran
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_hgNaenaG3qkHjaHgJFreB", # Dominant Omega
            "_kUV13hFp2R2a4aYEXq3c4", # Familiar Soulbound Synergy
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_pxQ16JrPDh2H6qAQKgKyx", # Nerdy / Bookworm
            "_wBMRG63aH2rTYeW4BaeXp", # Submissive Omega
        ],
    },
    {
        "key": "jasper",
        "name": "Jasper Svartr Douglas Bloodmoon",
        "lbSearch": "Jasper",
        "level": 3,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_3mrK4LGktdtUHGbf6CWNp",
        "speciesName": "Werewolf (Founding Bloodline & Pureblood Beta)",
        "occupationName": "Technomancer / Cyber-Mage",
        "className": "Guild Infiltrator & Black-Market Info-Broker",
        "base_stats": {"strength": 8, "perception": 14, "endurance": 10, "charisma": 8, "intelligence": 18, "agility": 13, "luck": 10},
        "traitIds": [
            "_aReYAkFDzYfFHwBWqQbyU", # LSE Beta Biology
            "_8YMa2gRKXFMBrWYzx2jqD", # Founding Bloodline
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_AQ6Qy4KHMDgFWKPHDJeqb", # Technomantic Data Resonance
            "_F3Y6PeGWJKq2rk7HKGr9y", # Tech Savvy
            "_CKqQUUkAh31KTLDkVK96E", # Mastermind
            "_kUV13hFp2R2a4aYEXq3c4", # Familiar Soulbound Synergy
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
            "_VrgTBJR3aEyW3FBD1zLkR", # Dungeon Veteran
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
        ],
    },
    {
        "key": "malachia",
        "name": "Malachia Björn Douglas Bloodmoon",
        "lbSearch": "Malachia",
        "level": 4,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_d7mHQJKnQqQNzwdwnqMdM",
        "speciesName": "Werewolf (Founding Bloodline & Pureblood Alpha)",
        "occupationName": "Guild Berserker (Vanguard)",
        "className": "Guild Frontline TANK / Vanguard",
        "base_stats": {"strength": 18, "perception": 10, "endurance": 17, "charisma": 8, "intelligence": 8, "agility": 12, "luck": 8},
        "traitIds": [
            "_jyDzgjNM8BmbrNC3AxcfB", # Dominant Alpha
            "_MRxrtF9paJmcB13fAnE9g", # Alpha Command
            "_yQj1axBPPjLBp79cCD3JG", # Ascended Enigma
            "_DgLQ22bMWpBnP3nnUK7nf", # Apex Core Resonance
            "_mJezfhzrdYDq8k7GWaGzm", # Pack Leader
            "_8YMa2gRKXFMBrWYzx2jqD", # Founding Bloodline
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_L2xQk9j8RnMKUgGnCVWRR", # Berserker Internal Furnace
            "_YbYKU6fNwTJgP6x4DPhDT", # Feral Blood
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_ycHNkaW9aEjTxppUe6Wtg", # Knight in Sour Armor
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
            "_VrgTBJR3aEyW3FBD1zLkR", # Dungeon Veteran
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
        ],
    },
    {
        "key": "noah",
        "name": "Noah Loki Douglas Bloodmoon",
        "lbSearch": "Noah",
        "level": 4,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_mG8DVrPTq8JdL8B2meJRY",
        "speciesName": "Werewolf (Founding Bloodline & Pureblood Delta)",
        "occupationName": "Right Hand (Advisor/Peacekeeper)",
        "className": "Pack PR Shield & Strategic Grey Eminence",
        "base_stats": {"strength": 9, "perception": 12, "endurance": 10, "charisma": 18, "intelligence": 14, "agility": 10, "luck": 8},
        "traitIds": [
            "_f8kfz4eJLh6br4fgGXyc6", # LSE Delta Biology
            "_8YMa2gRKXFMBrWYzx2jqD", # Founding Bloodline
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_CKqQUUkAh31KTLDkVK96E", # Mastermind
            "_gHdqdc2R8U9GLBxmBLcUV", # Trickster Mentor
            "_LNe6dhHnxx7BCfXeMERzc", # Eternal Optimist
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
            "_VrgTBJR3aEyW3FBD1zLkR", # Dungeon Veteran
        ],
    },
    {
        "key": "erik",
        "name": "Erik Ulfr Douglas",
        "lbSearch": "Erik",
        "level": 9,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_AAc7xBcAEttBdFmWTjBTg",
        "speciesName": "Werewolf (Pureblood Prime Alpha)",
        "occupationName": "Pack Leader",
        "className": "Prime Alpha & CEO of DCC",
        "base_stats": {"strength": 15, "perception": 12, "endurance": 15, "charisma": 15, "intelligence": 8, "agility": 8, "luck": 8},
        "traitIds": [
            "_mJezfhzrdYDq8k7GWaGzm", # Pack Leader
            "_jyDzgjNM8BmbrNC3AxcfB", # Dominant Alpha
            "_MRxrtF9paJmcB13fAnE9g", # Alpha Command
            "_DgLQ22bMWpBnP3nnUK7nf", # Apex Core Resonance
            "_CKqQUUkAh31KTLDkVK96E", # Mastermind
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_ycHNkaW9aEjTxppUe6Wtg", # Knight in Sour Armor
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
            "_VrgTBJR3aEyW3FBD1zLkR", # Dungeon Veteran
        ],
    },
    {
        "key": "logan",
        "name": "Logan Dominic Járn Douglas",
        "lbSearch": "Logan",
        "level": 9,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_mG8DVrPTq8JdL8B2meJRY",
        "speciesName": "Werewolf (Pureblood Beta)",
        "occupationName": "Right Hand (Advisor/Peacekeeper)",
        "className": "Erik's Right Hand & DCC Black Market Commander",
        "base_stats": {"strength": 16, "perception": 13, "endurance": 16, "charisma": 8, "intelligence": 9, "agility": 11, "luck": 8},
        "traitIds": [
            "_aReYAkFDzYfFHwBWqQbyU", # LSE Beta Biology
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_YbYKU6fNwTJgP6x4DPhDT", # Feral Blood
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_ycHNkaW9aEjTxppUe6Wtg", # Knight in Sour Armor
            "_URpa2cwkJQgVYt9j966JW", # Rebel Heart / Underground
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
            "_VrgTBJR3aEyW3FBD1zLkR", # Dungeon Veteran
        ],
    },
    {
        "key": "wulfnic",
        "name": "Wulfnic Báleygr Bloodmoon",
        "lbSearch": "Wulfnic",
        "level": 99,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_b8KfUNHq4z3bFw6jKkmzf",
        "speciesName": "Werewolf (Divine Blood Firstborn Primordial)",
        "occupationName": "Firstborn Apex Sovereign",
        "className": "Alpha of Alphas & Omniscient Jarl of California",
        "base_stats": {"strength": 16, "perception": 12, "endurance": 16, "charisma": 13, "intelligence": 8, "agility": 8, "luck": 8},
        "traitIds": [
            "_HwqVPTYtptM1Cwz1aCaaJ", # Primordial Enigma
            "_jyDzgjNM8BmbrNC3AxcfB", # Dominant Alpha
            "_MRxrtF9paJmcB13fAnE9g", # Alpha Command
            "_1QQ982MmT1fzehNRxq4WU", # Divine Blood (Firstborn)
            "_NL4ANGp2gjKtbAgRTFxbD", # Apex Predator Divine Core
            "_8YMa2gRKXFMBrWYzx2jqD", # Founding Bloodline
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_L2xQk9j8RnMKUgGnCVWRR", # Berserker Internal Furnace
            "_YbYKU6fNwTJgP6x4DPhDT", # Feral Blood
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
        ],
    },
    {
        "key": "edric",
        "name": "Edric Douglas",
        "lbSearch": "Edric Douglas",
        "level": 1,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_fgTDn33yV6eE9HEmm3qec",
        "speciesName": "Werewolf (Pureblood Pre-Presentation Gamma)",
        "occupationName": "Student / Pack Pup",
        "className": "Junior Pack Pup & Aspiring Vanguard",
        "base_stats": {"strength": 14, "perception": 12, "endurance": 15, "charisma": 10, "intelligence": 10, "agility": 10, "luck": 10},
        "traitIds": [
            "_B8TxmbNBqgwRVAem6qAUr", # Pre-First Shift (Gamma)
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
        ],
    },
    {
        "key": "elizabeth",
        "name": "Elizabeth Duskwood",
        "lbSearch": "Elizabeth",
        "level": 14,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_UqPTxeWDKkGT9R8bpM9U2",
        "speciesName": "Werewolf (Pureblood Dominant Omega)",
        "occupationName": "Leader's Mate / Pack Mom",
        "className": "Pack Mom Reggente & DCC Medical Director",
        "base_stats": {"strength": 8, "perception": 12, "endurance": 12, "charisma": 17, "intelligence": 16, "agility": 8, "luck": 8},
        "traitIds": [
            "_hgNaenaG3qkHjaHgJFreB", # Dominant Omega
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_QT6N7KhahqwqkJVaMXhY9", # Pre-Med / Healer
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_pxQ16JrPDh2H6qAQKgKyx", # Nerdy / Bookworm
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
        ],
    },
    {
        "key": "magnus",
        "name": "Magnus Douglas III",
        "lbSearch": "Magnus",
        "level": 99,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_e8MAN4PAq111hqe91UhCY",
        "speciesName": "Werewolf (Pureblood Alpha Patriarch)",
        "occupationName": "Patriarch / Coven Leader",
        "className": "Ancestral Pack Elder & Dynastic Sovereign",
        "base_stats": {"strength": 11, "perception": 12, "endurance": 12, "charisma": 16, "intelligence": 14, "agility": 8, "luck": 8},
        "traitIds": [
            "_jyDzgjNM8BmbrNC3AxcfB", # Dominant Alpha
            "_MRxrtF9paJmcB13fAnE9g", # Alpha Command
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
            "_CKqQUUkAh31KTLDkVK96E", # Mastermind
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
        ],
    },
    {
        "key": "cornelius",
        "name": "Lord Cornelius Douglas",
        "lbSearch": "Cornelius",
        "level": 99,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_YngWPBkwzfxfd6MbjhQAj",
        "speciesName": "Werewolf (Pureblood Alpha Founder)",
        "occupationName": "House Head (Lord/Patriarch)",
        "className": "Blackwood Colony Governor & House Founder",
        "base_stats": {"strength": 13, "perception": 12, "endurance": 13, "charisma": 16, "intelligence": 11, "agility": 8, "luck": 8},
        "traitIds": [
            "_jyDzgjNM8BmbrNC3AxcfB", # Dominant Alpha
            "_MRxrtF9paJmcB13fAnE9g", # Alpha Command
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
            "_DgLQ22bMWpBnP3nnUK7nf", # Apex Core Resonance
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
        ],
    },
    {
        "key": "nixara",
        "name": "Nixara Hvit Bloodmoon",
        "lbSearch": "Nixara",
        "level": 99,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_UqPTxeWDKkGT9R8bpM9U2",
        "speciesName": "Werewolf (Founding Bloodline White Moon Omega)",
        "occupationName": "Leader's Mate / Pack Mom",
        "className": "Ancestral Pack Mom & The White Moon of Seven Hills",
        "base_stats": {"strength": 8, "perception": 14, "endurance": 12, "charisma": 18, "intelligence": 13, "agility": 8, "luck": 8},
        "traitIds": [
            "_DMMAzBKW3b8wPd9rq6TWp", # The White Moon (Omega)
            "_hgNaenaG3qkHjaHgJFreB", # Dominant Omega
            "_8YMa2gRKXFMBrWYzx2jqD", # Founding Bloodline
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_LNe6dhHnxx7BCfXeMERzc", # Eternal Optimist
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
        ],
    },
    {
        "key": "echo",
        "name": "Echo",
        "lbSearch": "Echo",
        "level": 3,
        "speciesId": "_92MghbhEBRkmnzJCDBAR7",
        "occupationId": "_3mrK4LGktdtUHGbf6CWNp",
        "speciesName": "Macchina & Sintetico (Cyber-Entity Familiar)",
        "occupationName": "Technomancer / Cyber-Mage",
        "className": "Jasper's Technomantic Cyber-Familiar",
        "base_stats": {"strength": 8, "perception": 16, "endurance": 8, "charisma": 8, "intelligence": 20, "agility": 13, "luck": 8},
        "traitIds": [
            "_hF64363acKFAJCc77xXjE", # Cyber-Augmented
            "_F3Y6PeGWJKq2rk7HKGr9y", # Tech Savvy
            "_AQ6Qy4KHMDgFWKPHDJeqb", # Technomantic Data Resonance
            "_kUV13hFp2R2a4aYEXq3c4", # Familiar Soulbound Synergy
            "_CKqQUUkAh31KTLDkVK96E", # Mastermind
            "_4nTUFT2tfNAjdTKXHfgUc", # Night Stalker
            "_pxQ16JrPDh2H6qAQKgKyx", # Nerdy / Bookworm
        ],
    },
    {
        "key": "zefir",
        "name": "Zefir Hvitskog",
        "lbSearch": "Zefir",
        "level": 99,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_yCNjpDEBrLGbMK73CrBzR",
        "speciesName": "Werewolf (Divine Blood Firstborn Primordial)",
        "occupationName": "Scout",
        "className": "Primordial Shadow Scout & Snow-Wolf Sovereign",
        "base_stats": {"strength": 12, "perception": 18, "endurance": 14, "charisma": 8, "intelligence": 11, "agility": 10, "luck": 8},
        "traitIds": [
            "_HwqVPTYtptM1Cwz1aCaaJ", # Primordial Enigma
            "_1QQ982MmT1fzehNRxq4WU", # Divine Blood (Firstborn)
            "_8YMa2gRKXFMBrWYzx2jqD", # Founding Bloodline
            "_jyDzgjNM8BmbrNC3AxcfB", # Dominant Alpha
            "_MRxrtF9paJmcB13fAnE9g", # Alpha Command
            "_NL4ANGp2gjKtbAgRTFxbD", # Apex Predator Divine Core
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_4nTUFT2tfNAjdTKXHfgUc", # Night Stalker
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
        ],
    },
    {
        "key": "ut",
        "name": "Ut Berg",
        "lbSearch": "Ut",
        "level": 99,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_fgTDn33yV6eE9HEmm3qec",
        "speciesName": "Werewolf (Divine Blood Firstborn Primordial)",
        "occupationName": "Guild Tank",
        "className": "Primordial Mountain Titan & Vanguard Breaker",
        "base_stats": {"strength": 18, "perception": 10, "endurance": 18, "charisma": 11, "intelligence": 8, "agility": 8, "luck": 8},
        "traitIds": [
            "_HwqVPTYtptM1Cwz1aCaaJ", # Primordial Enigma
            "_1QQ982MmT1fzehNRxq4WU", # Divine Blood (Firstborn)
            "_8YMa2gRKXFMBrWYzx2jqD", # Founding Bloodline
            "_jyDzgjNM8BmbrNC3AxcfB", # Dominant Alpha
            "_MRxrtF9paJmcB13fAnE9g", # Alpha Command
            "_NL4ANGp2gjKtbAgRTFxbD", # Apex Predator Divine Core
            "_L2xQk9j8RnMKUgGnCVWRR", # Berserker Internal Furnace
            "_YbYKU6fNwTJgP6x4DPhDT", # Feral Blood
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
        ],
    },
    {
        "key": "kaladin",
        "name": "Major Kaladin Blackwolf Nargathon",
        "lbSearch": "Kaladin",
        "level": 6,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_12YM878yc9tkLC32Lfdhx",
        "speciesName": "Werewolf (Modified / Lab Lineage)",
        "occupationName": "DCC Security / PMC",
        "className": "DCC Security Division Commander & Subject Zero",
        "base_stats": {"strength": 15, "perception": 14, "endurance": 15, "charisma": 11, "intelligence": 10, "agility": 8, "luck": 8},
        "traitIds": [
            "_jyDzgjNM8BmbrNC3AxcfB", # Dominant Alpha
            "_MRxrtF9paJmcB13fAnE9g", # Alpha Command
            "_YT36NBpQWKPTwqwRNeGzp", # Modified / Lab Lineage
            "_7a2b7jHqJ7MdbNXQCxG34", # S.R.F. Veteran
            "_VrgTBJR3aEyW3FBD1zLkR", # Dungeon Veteran
            "_ycHNkaW9aEjTxppUe6Wtg", # Knight in Sour Armor
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
            "_F3Y6PeGWJKq2rk7HKGr9y", # Tech Savvy
        ],
    },
    {
        "key": "archer",
        "name": "Archer Wolfwood",
        "lbSearch": "Archer",
        "level": 34,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_12YM878yc9tkLC32Lfdhx",
        "speciesName": "Werewolf (Pureblood Lineage)",
        "occupationName": "DCC Security / PMC",
        "className": "Wolfwood House Head & Senior DCC Security Liaison",
        "base_stats": {"strength": 12, "perception": 14, "endurance": 12, "charisma": 15, "intelligence": 12, "agility": 8, "luck": 8},
        "traitIds": [
            "_jyDzgjNM8BmbrNC3AxcfB", # Dominant Alpha
            "_MRxrtF9paJmcB13fAnE9g", # Alpha Command
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
            "_CKqQUUkAh31KTLDkVK96E", # Mastermind
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
        ],
    },
    {
        "key": "mackenzie",
        "name": "Mackenzie Sanchez-Rogers",
        "lbSearch": "Mackenzie",
        "level": 4,
        "speciesId": "_wyAYU2Mn7AkQ1hVej7PdW",
        "occupationId": "_R3MA2NAW1yXtXDT4KkqqN",
        "speciesName": "Werewolf (Pureblood Rogers & Common Sanchez)",
        "occupationName": "Street Scrapper / Rogue",
        "className": "Underground Street Fighter & Protective Brawler",
        "base_stats": {"strength": 14, "perception": 12, "endurance": 14, "charisma": 11, "intelligence": 8, "agility": 14, "luck": 8},
        "traitIds": [
            "_jyDzgjNM8BmbrNC3AxcfB", # Dominant Alpha
            "_MRxrtF9paJmcB13fAnE9g", # Alpha Command
            "_an1zbcGY7MYWA2qHeCzba", # Pureblood Lineage
            "_fYMTrnz7V4Vd7DECCxLMm", # Common Lupine Blood
            "_URpa2cwkJQgVYt9j966JW", # Rebel Heart / Underground
            "_YbYKU6fNwTJgP6x4DPhDT", # Feral Blood
            "_VrgTBJR3aEyW3FBD1zLkR", # Dungeon Veteran
            "_VVnrtkB9fn9gr1zMwFRyM", # Lupine Senses
            "_8B9wFbE8xag2a2dWTVE9b", # Partial Shift Mastery
            "_nKtryaNUjK1edMnBNjL9K", # Regenerative Factor
            "_EG7K3mQqJhgaUr7KkYxJR", # Silver Allergy
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
        ],
    },
    {
        "key": "finnegan",
        "name": "Finnegan Novak",
        "lbSearch": "Finn",
        "level": 3,
        "speciesId": "_pf9FRybEA1Y7naxw7TDQE",
        "occupationId": "_GwQBtq3JX8MGjF6QYpVkg",
        "speciesName": "Demi-umano (Arctic Wolf Kemonomimi)",
        "occupationName": "Pro Athlete / Fighter",
        "className": "SUCC Bears Left Wing (Varsity Hockey Athlete)",
        "base_stats": {"strength": 12, "perception": 12, "endurance": 14, "charisma": 11, "intelligence": 9, "agility": 15, "luck": 8},
        "traitIds": [
            "_8AYDaJ2xJaP7Vhe26M1jA", # Gentle Giant
            "_URpa2cwkJQgVYt9j966JW", # Rebel Heart / Underground
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_ycHNkaW9aEjTxppUe6Wtg", # Knight in Sour Armor
            "_LNe6dhHnxx7BCfXeMERzc", # Eternal Optimist
            "_F3Y6PeGWJKq2rk7HKGr9y", # Tech Savvy
        ],
    },
    {
        "key": "zeera",
        "name": "Zeera Darkfire",
        "lbSearch": "Zeera",
        "level": 6,
        "speciesId": "_FQJetrfXHAA4TyachJqwU",
        "occupationId": "_eFTUaaMbVTByeDbbM9cLP",
        "speciesName": "Demone & Infernale (High Infernal Bloodline)",
        "occupationName": "Diplomat",
        "className": "Horned Skull Clan Leader & CEO of HSK Consulting",
        "base_stats": {"strength": 10, "perception": 12, "endurance": 12, "charisma": 17, "intelligence": 14, "agility": 8, "luck": 8},
        "traitIds": [
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_JLKHrB9AFqkb1BhT6G3tj", # Old Money / Aristocrat
            "_CKqQUUkAh31KTLDkVK96E", # Mastermind
            "_4nTUFT2tfNAjdTKXHfgUc", # Night Stalker
            "_VrgTBJR3aEyW3FBD1zLkR", # Dungeon Veteran
            "_C8XXTwLd1mmF33EkQMUyD", # Puppeteer Mana Strings
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
        ],
    },
    {
        "key": "jared",
        "name": "Jared Thompson",
        "lbSearch": "Jared",
        "level": 3,
        "speciesId": "_nUm9xyCztM9UR8HktQneq",
        "occupationId": "_GwQBtq3JX8MGjF6QYpVkg",
        "speciesName": "Minotauro & Centauro (Half-Minotaur Hybrid)",
        "occupationName": "Pro Athlete / Fighter",
        "className": "SUCC Bulls Starting Quarterback & Beta Rho Omega Frat",
        "base_stats": {"strength": 16, "perception": 10, "endurance": 16, "charisma": 14, "intelligence": 8, "agility": 9, "luck": 8},
        "traitIds": [
            "_8AYDaJ2xJaP7Vhe26M1jA", # Gentle Giant
            "_URpa2cwkJQgVYt9j966JW", # Rebel Heart / Underground
            "_LNe6dhHnxx7BCfXeMERzc", # Eternal Optimist
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_CBcWYUneXXPwpyEq2Mjcm", # Ancient Heritage
            "_YbYKU6fNwTJgP6x4DPhDT", # Feral Blood
        ],
    },
    {
        "key": "marek",
        "name": "Marek",
        "lbSearch": "Marek",
        "level": 7,
        "speciesId": "_y1Cc1bJ6d2D3HzFyymDRB",
        "occupationId": "_AceqGK7cL6QkAKdPF9kCT",
        "speciesName": "Orco & Oni (Blue Oni)",
        "occupationName": "Mechanic / Custom Builder",
        "className": "Ironhorn Nomads MC President & Heavy Chopper Builder",
        "base_stats": {"strength": 16, "perception": 12, "endurance": 15, "charisma": 11, "intelligence": 9, "agility": 11, "luck": 7},
        "traitIds": [
            "_8AYDaJ2xJaP7Vhe26M1jA", # Gentle Giant
            "_URpa2cwkJQgVYt9j966JW", # Rebel Heart / Underground
            "_VrgTBJR3aEyW3FBD1zLkR", # Dungeon Veteran
            "_AMT6xk8rnrT9E9Vx8mhdq", # The Weight He Carries
            "_ycHNkaW9aEjTxppUe6Wtg", # Knight in Sour Armor
        ],
    },
    {
        "key": "echo",
        "name": "Echo (E.C.H.O.)",
        "lbSearch": "E.C.H.O.",
        "level": 3,
        "speciesId": "_92MghbhEBRkmnzJCDBAR7",
        "occupationId": "_3mrK4LGktdtUHGbf6CWNp",
        "speciesName": "Macchina & Sintetico (Cyber-Entity Familiar)",
        "occupationName": "Technomancer / Cyber-Mage",
        "className": "Jasper's Technomantic Cyber-Familiar",
        "base_stats": {"strength": 8, "perception": 16, "endurance": 8, "charisma": 8, "intelligence": 20, "agility": 13, "luck": 8},
        "traitIds": [
            "_hF64363acKFAJCc77xXjE", # Cyber-Augmented
            "_F3Y6PeGWJKq2rk7HKGr9y", # Tech Savvy
            "_AQ6Qy4KHMDgFWKPHDJeqb", # Technomantic Data Resonance
            "_kUV13hFp2R2a4aYEXq3c4", # Familiar Soulbound Synergy
            "_CKqQUUkAh31KTLDkVK96E", # Mastermind
            "_4nTUFT2tfNAjdTKXHfgUc", # Night Stalker
            "_pxQ16JrPDh2H6qAQKgKyx", # Nerdy / Bookworm
        ],
    },
]

def compute_final_stats(c):
    final = dict(c["base_stats"])
    sp = species_map.get(c["speciesId"], {})
    oc = occs_map.get(c["occupationId"], {})
    for k, v in sp.get("stat_modifiers", {}).items():
        if k in final:
            final[k] += v
    for k, v in oc.get("stat_modifiers", {}).items():
        if k in final:
            final[k] += v
    for tid in c["traitIds"]:
        tr = traits_map.get(tid, {})
        for k, v in tr.get("stat_modifiers", {}).items():
            if k in final:
                final[k] += v
    return final

def format_mod_str(mods):
    if not mods:
        return ""
    parts = []
    for k in STAT_KEYS:
        if k in mods and mods[k] != 0:
            sign = "+" if mods[k] > 0 else ""
            parts.append(f"{STAT_ABBR[k]} {sign}{mods[k]}")
    return f" ({', '.join(parts)})" if parts else ""

def build_rpg_block(c):
    final = compute_final_stats(c)
    sp = species_map.get(c["speciesId"], {})
    oc = occs_map.get(c["occupationId"], {})
    sp_mod_str = format_mod_str(sp.get("stat_modifiers", {}))
    oc_mod_str = format_mod_str(oc.get("stat_modifiers", {}))
    stats_str = "; ".join(f"{STAT_ABBR[k]} {final[k]}" for k in STAT_KEYS)
    lines = [
        "RPG STATS & TRAITS:",
        f"[LEVEL: {c['level']}; SPECIES: {c['speciesName']}{sp_mod_str}; OCCUPATION: {c['occupationName']}{oc_mod_str}; CLASS: {c['className']}]",
        f"[STATS: {stats_str}]",
        "TRAITS:",
    ]
    for tid in c["traitIds"]:
        tr = traits_map.get(tid, {})
        t_name = tr.get("name", tid)
        t_desc = tr.get("description", "").replace("—", ", ")
        t_mod = format_mod_str(tr.get("stat_modifiers", {}))
        lines.append(f"- {t_name}{t_mod}: {t_desc}")
    return "\n".join(lines), final

if __name__ == "__main__":
    out = {}
    for c in CHARACTERS_RPG:
        block, final = build_rpg_block(c)
        out[c["key"]] = {**c, "final_stats": final, "rpg_block": block}
        print(f"{c['name']:36} | Base sum={sum(c['base_stats'].values())} | Final={final} (sum={sum(final.values())})")
    with open(os.path.join(ROOT, "scratch", "computed_final_rpg_stats.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

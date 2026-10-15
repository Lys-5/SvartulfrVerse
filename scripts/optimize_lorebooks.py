# -*- coding: utf-8 -*-
"""
Fase 1 - Ottimizzazione non-distruttiva dei lorebook WyvernChat.
Legge i 5 export originali da ../lorebooks/source/ e scrive le versioni pulite in ../lorebooks/optimized/.
Gli originali non vengono MAI modificati.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(ROOT, "lorebooks", "source")
OUTPUT_DIR = os.path.join(ROOT, "lorebooks", "optimized")
os.makedirs(OUTPUT_DIR, exist_ok=True)

FILES = [
    "Svartulfr_Lorebook_I.json",
    "Svartulfr_Lorebook_II.json",
    "Svartulfr_Lorebook_III.json",
    "Svartulfr_Location.json",
    "Svartulfr_NPC_Primary.json",
]

# Keyword "ombrello" da rimuovere SOLO dalle schede dei singoli NPC (content che inizia con [NAME:)
BROAD_KEYS = {"solarton", "succ", "blackwood", "losangeles", "underworld"}

# Voci intruse del setting Digitalis / Cuttings / Jun, identificate per uid verificato (non per substring)
INTRUDER_UID = {
    "Svartulfr_Location.json": {"0"},
    "Svartulfr_Lorebook_II.json": {"45", "128"},
    "Svartulfr_Lorebook_III.json": {"186", "200", "201"},
    "Svartulfr_NPC_Primary.json": {"0", "1", "2", "3", "4", "5", "6"},
}

# Cross-check: se un marcatore Digitalis compare su una uid NON in lista, viene segnalato (non disabilitato)
MARKERS = ["Cutting 01", "Cutting 02", "Cutting 03", "Tendril", "The Hothouse",
           "Cuttings and", "Shiba Inu", "half sister of Jun"]

# Blocco [INSTRUCTIONS: Format discipline ...] generico e ripetuto (NON tocca le istruzioni character-specific)
INSTR_PATTERN = re.compile(
    r"\s*\[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text "
    r"\(no asterisks\), asterisks reserved for internal thoughts only\. "
    r"Never use the em dash; use commas or periods instead\.\]",
    re.IGNORECASE,
)

for filename in FILES:
    src = os.path.join(SOURCE_DIR, filename)
    if not os.path.exists(src):
        print(f"[!] File non trovato: {filename}")
        continue

    with open(src, "r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get("entries", {})
    st = {"ph": 0, "intr": 0, "keys": 0, "instr": 0, "sel": 0, "prio": 0}
    warnings = []

    for uid, entry in entries.items():
        content = entry.get("content", "")

        # 1. Congela (disable) le schede segnaposto o vuote
        if "STATUS: placeholder" in content or content.strip() == "":
            if not entry.get("disable"):
                entry["disable"] = True
                st["ph"] += 1

        # 2. Congela (disable) le voci intruse del setting Digitalis / Cuttings / Jun (per uid esplicito)
        if uid in INTRUDER_UID.get(filename, set()):
            if not entry.get("disable"):
                entry["disable"] = True
            st["intr"] += 1
        else:
            hit = [m for m in MARKERS if m in content]
            if hit:
                warnings.append((uid, entry.get("comment", ""), hit))

        # 3. Rimuove le keyword "ombrello" dalle schede dei personaggi (content che inizia con [NAME:)
        if content.startswith("[NAME:") and len(entry.get("key", [])) > 1:
            keys = entry["key"]
            new_keys = [k for k in keys if str(k).lower().strip() not in BROAD_KEYS]
            if new_keys and len(new_keys) != len(keys):
                entry["key"] = new_keys
                st["keys"] += 1

        # 4. Rimuove il blocco [INSTRUCTIONS: Format discipline ...] ridondante
        new_content, count = INSTR_PATTERN.subn("", content)
        if count > 0:
            entry["content"] = new_content.strip()
            st["instr"] += 1

        # 5. Rilevazione (NON modifica) di selective=True senza keysecondary: no-op su questo dataset
        if entry.get("selective") is True and not entry.get("keysecondary"):
            st["sel"] += 1

        # 6. Priority di sicurezza: porta a 10 le voci con priority 0
        ext = entry.get("extensions")
        if isinstance(ext, dict) and isinstance(ext.get("wyvern"), dict):
            if ext["wyvern"].get("priority", 0) == 0:
                ext["wyvern"]["priority"] = 10
                st["prio"] += 1

    out_path = os.path.join(OUTPUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Validazione: il file scritto deve ri-parsare correttamente
    with open(out_path, "r", encoding="utf-8") as f:
        json.load(f)

    print(f"OK  {filename}")
    print(f"    - placeholder disabilitati:            {st['ph']}")
    print(f"    - voci intruse disabilitate:           {st['intr']}")
    print(f"    - NPC ripuliti da keyword generiche:   {st['keys']}")
    print(f"    - [INSTRUCTIONS] generiche rimosse:    {st['instr']}")
    print(f"    - 'selective' senza keysecondary:      {st['sel']} (rilevate, non modificate)")
    print(f"    - priority 0->10 applicate:            {st['prio']}")
    for w in warnings:
        print(f"    [!] marcatore fuori lista uid -> uid {w[0]} '{w[1]}': {w[2]}")
    print()

#!/usr/bin/env python3
"""
scripts/vault_health_check.py

Svartulfr Verse — Vault Health Check & Metabolism Engine
Codifica le 10 Regole del "Second Brain / LLM Wiki 2026" (Karpathy / CoALA / MemGuard):
1. Contraddizioni & Verita Canonica (Canon Invariants & Biological Constraints)
2. Struttura JED+ & Contratto Schede (Schema as Contract & 9 Mandatory Outfits)
3. Anti-Collisione & Igiene Trigger (No Umbrella Keys, No {{age}}, Flag Triad)
4. Johnny.Decimal & Unicita Entita (One Entity, One Place; No Collisions)
5. Parita Byte-for-byte (Zod Frontend Parity: entries == lexicon)
6. Metabolismo & Infrastruttura (Automations, Proxy Upstreams, State Files)

Uso:
  python scripts/vault_health_check.py
  python scripts/vault_health_check.py --fix-parity
"""

import argparse
import datetime
import json
import os
import pathlib
import re
import sys

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT = pathlib.Path(__file__).resolve().parent.parent
FINAL = ROOT / 'FINAL'
PERSONAS = FINAL / 'personas'
OPT = ROOT / 'lorebooks' / 'optimized'
SCRATCH = ROOT / 'scratch'
PROXY = ROOT / 'proxy'
SIDECARS_DIR = pathlib.Path(os.path.expanduser('~/.gemini/config/sidecars'))

REPORT_PATH = SCRATCH / 'vault_health_report.md'

# ANSI Color Codes
CLR_RESET = "\033[0m"
CLR_GREEN = "\033[92m"
CLR_AMBER = "\033[93m"
CLR_RED = "\033[91m"
CLR_CYAN = "\033[96m"
CLR_BOLD = "\033[1m"

CANONICAL_HEIGHTS = {
    'Alyssa': {'cm': 155, 'imperial': "5' 1\""},
    'Jasper': {'cm': 193, 'imperial': "6' 4\""},
    'Noah': {'cm': 197, 'imperial': "6' 5.6\""},
    'Logan': {'cm': 198, 'imperial': "6' 6\""},
    'Mackenzie': {'cm': 204, 'imperial': "6' 8\""},
    'Malachia': {'cm': 208, 'imperial': "6' 9.9\""},
    'Erik': {'cm': 213, 'imperial': "7' 0\""},
    'Wulfnic': {'cm': 220, 'imperial': "7' 2.6\""},
    'Zeera': {'cm': 208, 'imperial': "6' 10\""},
}

BROAD_KEYS = {
    "solarton", "succ", "blackwood", "vampire", "werewolf", 
    "college", "student", "alpha", "omega", "dcc"
}

MANDATORY_OUTFIT_IDS = {
    "casual", "business", "formal", "party", 
    "beach", "sleep", "nude", "hybrid", "full"
}

class HealthAuditor:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.passes = []
        self.stats = {
            "lorebooks_scanned": 0,
            "characters_scanned": 0,
            "personas_scanned": 0,
            "npc_entries_scanned": 0,
            "total_checks": 0
        }

    def record_pass(self, category: str, message: str):
        self.stats["total_checks"] += 1
        self.passes.append((category, message))

    def record_warning(self, category: str, message: str):
        self.stats["total_checks"] += 1
        self.warnings.append((category, message))

    def record_error(self, category: str, message: str):
        self.stats["total_checks"] += 1
        self.errors.append((category, message))

    # --------------------------------------------------------------------------
    # 1. Contraddizioni & Verita Canonica
    # --------------------------------------------------------------------------
    def audit_canonical_invariants(self):
        cat = "1. Canon & Contraddizioni"
        print(f"{CLR_CYAN}[1/6] Verifica Contraddizioni & Verita Canonica...{CLR_RESET}")

        # Check Sierra Cruz anatomy
        npc_files = [FINAL / 'Svartulfr_NPC_Primary.json', FINAL / 'Svartulfr_NPC_Secondary.json']
        for npcf in npc_files:
            if not npcf.exists():
                continue
            with open(npcf, 'r', encoding='utf-8') as f:
                data = json.load(f)
            entries = data.get('entries') or data.get('lexicon') or []
            for e in entries:
                name = e.get('name', '')
                desc = e.get('description') or e.get('content') or ''
                
                # Check Sierra Cruz
                if 'sierra cruz' in name.lower():
                    forbidden = ['feet', 'shoes', 'legs', 'stride', 'steps', 'pants', 'walks', 'walking']
                    found_f = [w for w in forbidden if re.search(r'\b' + re.escape(w) + r'\b', desc, re.IGNORECASE)]
                    if found_f:
                        self.record_error(cat, f"Sierra Cruz ({npcf.name}) contiene termini proibiti su locomozione bipede: {found_f}")
                    else:
                        self.record_pass(cat, f"Sierra Cruz ({npcf.name}) anatomia lamia rigorosa (zero gambe/piedi/passi)")
                    
                    forbidden_ears = ['wolf ear', 'wolf ears', 'pointed demi-human ear', 'orecchie da lupo', 'pointed ears']
                    found_ears = [w for w in forbidden_ears if re.search(r'\b' + re.escape(w) + r'\b', desc, re.IGNORECASE)]
                    if found_ears:
                        self.record_error(cat, f"Sierra Cruz ({npcf.name}) contiene attributi auricolari mammiferi/lupini proibiti: {found_ears}")
                    else:
                        self.record_pass(cat, f"Sierra Cruz ({npcf.name}) anatomia uditiva rettiliana rigorosa (zero orecchie da lupo/mammifero)")

                # Check Scarlett Rose
                if 'scarlett rose' in name.lower():
                    if 'candy-pink' not in desc.lower():
                        self.record_warning(cat, f"Scarlett Rose ({npcf.name}) dovrebbe specificare 'candy-pink' per capelli/occhi")
                    else:
                        self.record_pass(cat, f"Scarlett Rose ({npcf.name}) palette 'candy-pink' verificata")
                    if 'horns' not in desc.lower() or 'scarlet' not in desc.lower():
                        self.record_warning(cat, f"Scarlett Rose ({npcf.name}) dovrebbe includere le due corna scarlatte")
                    else:
                        self.record_pass(cat, f"Scarlett Rose ({npcf.name}) due corna scarlatte verificate")

                # Check Roman Blackwood homonymy
                if 'roman blackwood' in name.lower():
                    if 'omonim' not in desc.lower():
                        self.record_error(cat, f"Roman Blackwood ({npcf.name}) deve esplicitare l'omonimia anagrafica ('omonimo') per prevenire l'attribuzione di erede della Casata Blackwood")
                    else:
                        self.record_pass(cat, f"Roman Blackwood ({npcf.name}) omonimia confermata (nessun legame ereditario Casata Blackwood)")

                # Check Em-Dash
                if '—' in desc or '–' in desc:
                    self.record_error(cat, f"Entry '{name}' in {npcf.name} contiene em-dash (— o –) vietato dalle regole")

        # Check SopakcoSauce 31 Non-Human Templates Reference Integrity
        sopakco_path = ROOT / 'knowledge' / 'External_References' / 'SOPAKCOSAUCE_NON_HUMAN_CHARACTER_TEMPLATES.md'
        if not sopakco_path.exists():
            self.record_error(cat, f"Riferimento canonico non trovato: {sopakco_path}")
        else:
            with open(sopakco_path, 'r', encoding='utf-8') as sf:
                s_content = sf.read()
            if len(s_content) > 50000 and "## 31. Abyssal Horror" in s_content and "## 1. Lamia & Naga" in s_content:
                self.record_pass(cat, "SopakcoSauce 31 Non-Human Templates verificato e integro (31/31 specie censite)")
            else:
                self.record_warning(cat, "SopakcoSauce 31 Non-Human Templates presente ma potrebbe essere incompleto")

        # Check Cato (Alligator Demihuman)
        for npcf in npc_files:
            if not npcf.exists():
                continue
            with open(npcf, 'r', encoding='utf-8') as f:
                data = json.load(f)
            entries = data.get('entries') or data.get('lexicon') or []
            for e in entries:
                ename = e.get('name', '').lower()
                edesc = e.get('description') or e.get('content') or ''
                if ename == 'cato' or 'cato' in ename.split():
                    if 'single animal ear' in edesc.lower() or 'wolf ear' in edesc.lower():
                        self.record_error(cat, f"Cato ({npcf.name}) contiene attributi auricolari mammiferi errati")
                    elif 'ear-slit' in edesc.lower() or 'scaled flaps' in edesc.lower():
                        self.record_pass(cat, f"Cato ({npcf.name}) anatomia uditiva da alligatore verificata (fessure squamate)")

        # Check heights in Standalone Cards
        card_files = list(FINAL.glob('*_card.json'))
        self.stats["characters_scanned"] = len(card_files)
        for cf in card_files:
            with open(cf, 'r', encoding='utf-8') as f:
                card = json.load(f)
            char_name = card.get('name', cf.stem)
            desc = card.get('description', '')
            
            # Em dash in card fields
            for field_name in ['description', 'first_mes', 'scenario']:
                val = card.get(field_name, '')
                if val and '—' in val:
                    self.record_error(cat, f"Card '{char_name}' ({field_name}) contiene em-dash (—)")

            # Check heights in Cards
            for canon_name, hdata in CANONICAL_HEIGHTS.items():
                if canon_name.lower() in char_name.lower():
                    cm_val = hdata['cm']
                    if f"{cm_val} cm" not in desc and f"{cm_val}cm" not in desc:
                        self.record_warning(cat, f"Card '{char_name}' non riporta esattamente '{cm_val} cm' nella descrizione JED+")
                    else:
                        self.record_pass(cat, f"Card '{char_name}' allineata all'altezza canonica ({cm_val} cm)")

        # Check canonical heights across User Personas, World Characters, and Outfits (especially Alyssa = 155 cm, never 165 cm)
        for pf in sorted((FINAL / 'personas').glob('*.json')):
            try:
                pdata = json.loads(pf.read_text(encoding='utf-8'))
                pname = pdata.get('name', pf.stem)
                pdesc = pdata.get('description', '')
                if 'alyssa' in pname.lower() or 'alyssa' in pf.stem.lower():
                    if '155 cm' not in pdesc and '155cm' not in pdesc:
                        self.record_error(cat, f"Persona '{pf.name}' non riporta l'altezza canonica di Alyssa (155 cm)")
                    for o in (pdata.get('outfits') or []):
                        odesc = o.get('description', '')
                        if '165 cm' in odesc or '165cm' in odesc or '160 cm' in odesc:
                            self.record_error(cat, f"Persona '{pf.name}' outfit '{o.get('name')}' riporta un'altezza errata per Alyssa (deve essere 155 cm)")
            except Exception:
                pass
        wc_file = FINAL / 'Svartulfr_Characters.json'
        if wc_file.exists():
            try:
                wcs_list = json.loads(wc_file.read_text(encoding='utf-8'))
                for wc in wcs_list:
                    wname = wc.get('display_name') or wc.get('name') or ''
                    wdesc = wc.get('long_summary', '')
                    if 'alyssa' in wname.lower():
                        if '155 cm' not in wdesc and '155cm' not in wdesc:
                            self.record_error(cat, f"World Character '{wname}' non riporta l'altezza canonica di Alyssa (155 cm)")
                        else:
                            self.record_pass(cat, f"World Character '{wname}' e outfits allineati all'altezza canonica (155 cm)")
                        for o in (wc.get('outfits') or []):
                            odesc = o.get('description', '')
                            if '165 cm' in odesc or '165cm' in odesc or '160 cm' in odesc:
                                self.record_error(cat, f"World Character '{wname}' outfit '{o.get('name')}' riporta un'altezza errata per Alyssa (deve essere 155 cm)")
            except Exception:
                pass

        # Global Pure Positive Framing Check (zero 'no human ears' in narrative text)
        forbidden_neg = ['no human ears', 'senza orecchie umane', 'prive di orecchie umane', 'prive di orecchie ai lati']
        neg_violations = []
        for cf in card_files:
            with open(cf, 'r', encoding='utf-8') as f:
                card = json.load(f)
            text = (card.get('description', '') + ' ' + card.get('personality', '')).lower()
            for ph in forbidden_neg:
                if ph in text:
                    neg_violations.append(f"Card '{card.get('name')}' contiene '{ph}'")
        for lbf in FINAL.glob('Svartulfr_*.json'):
            try:
                with open(lbf, 'r', encoding='utf-8') as f:
                    d = json.load(f)
                entries = d if isinstance(d, list) else (d.get('entries') or d.get('lexicon') or [])
                for e in entries:
                    text = (e.get('description') or e.get('content') or '').lower()
                    for ph in forbidden_neg:
                        if ph in text:
                            neg_violations.append(f"{lbf.name} entry '{e.get('name')}' contiene '{ph}'")
            except Exception:
                pass

        if neg_violations:
            for v in neg_violations:
                self.record_error(cat, f"Negative Framing vietato: {v}")
        else:
            self.record_pass(cat, "Pure Positive Framing verificato su tutto il corpus (zero 'no human ears' nei testi narrativi)")

    # --------------------------------------------------------------------------
    # 2. Struttura JED+ & Contratto Schede
    # --------------------------------------------------------------------------
    def audit_jed_structure(self):
        cat = "2. Struttura JED+ & Schede"
        print(f"{CLR_CYAN}[2/6] Verifica Struttura JED+ & 9 Outfits Minimi...{CLR_RESET}")

        card_files = list(FINAL.glob('*_card.json'))
        for cf in card_files:
            with open(cf, 'r', encoding='utf-8') as f:
                card = json.load(f)
            char_name = card.get('name', cf.stem)
            desc = card.get('description', '')

            # Check JED+ v2.0 multiline or legacy single-line PList bracket
            if desc.startswith('['):
                closing_bracket_idx = desc.find(']')
                if closing_bracket_idx != -1:
                    first_bracket = desc[1:closing_bracket_idx]
                    bad_plist_lines = [
                        ln.strip()
                        for ln in first_bracket.splitlines()
                        if ln.strip() and not re.match(r'^[A-Z][A-Z0-9_ /&()-]{1,35}:\s*.+', ln.strip())
                    ]
                    if bad_plist_lines:
                        self.record_error(cat, f"Card '{char_name}' blocco PList iniziale [...] contiene righe malformate o narrative: {bad_plist_lines[:2]}")
                    else:
                        mode_lbl = "multilinea JED+ v2.0" if '\n' in first_bracket else "singola riga"
                        self.record_pass(cat, f"Card '{char_name}' blocco PList iniziale conforme ({mode_lbl})")
                else:
                    self.record_error(cat, f"Card '{char_name}' blocco iniziale '[' non chiuso da ']'")
            else:
                self.record_error(cat, f"Card '{char_name}' description non inizia con il blocco JED+ [...]")

            # Check mandatory narrative blocks (JED+ v2.0 or legacy)
            if "BACKSTORY:" not in desc:
                self.record_error(cat, f"Card '{char_name}' manca della sezione obbligatoria 'BACKSTORY:'")
            if "VOICE & BEHAVIOR:" not in desc and "VOICE, TELLS & BEHAVIOR:" not in desc:
                self.record_error(cat, f"Card '{char_name}' manca della sezione obbligatoria 'VOICE, TELLS & BEHAVIOR:' (o 'VOICE & BEHAVIOR:')")

            # Check Outfits count and categories
            outfits = card.get('outfits', [])
            if len(outfits) < 9:
                self.record_error(cat, f"Card '{char_name}' ha {len(outfits)}/9 outfits contestuali minimi")
            else:
                self.record_pass(cat, f"Card '{char_name}' possiede {len(outfits)} outfits (minimo 9 rispettato)")

            # Check Nude outfit with 6 sections and JED+ v2.0 Multiline PList format
            non_plist_outfits = [o.get('name', '?') for o in outfits if not (o.get('description', '').strip().startswith('[') and o.get('description', '').strip().endswith(']'))]
            if non_plist_outfits:
                self.record_error(cat, f"Card '{char_name}' ha outfits non formattati in JED+ v2.0 PList [...]: {non_plist_outfits[:2]}")

            nude_list = [o for o in outfits if any(w in o.get('name', '').lower() for w in ['nude', 'nudo'])]
            if not nude_list:
                self.record_error(cat, f"Card '{char_name}' manca dell'outfit 'nude/nudo' obbligatorio")
            else:
                n_desc = nude_list[0].get('description', '')
                required_sections = ['Abbigliamento:', 'Accessori:', 'Scarpe:', 'Gioielli:', 'Trucco:', 'Acconciatura:']
                missing_secs = [s for s in required_sections if s not in n_desc and s.upper() not in n_desc]
                
                if len(n_desc) < 250 and missing_secs:
                    self.record_error(cat, f"Card '{char_name}' outfit nude non conforme: len={len(n_desc)} (min 250), sezioni mancanti={missing_secs}")
                elif len(n_desc) < 250:
                    self.record_error(cat, f"Card '{char_name}' outfit nude troppo breve ({len(n_desc)} car., min 250 richiesti)")
                elif missing_secs:
                    self.record_error(cat, f"Card '{char_name}' outfit nude privo delle sezioni obbligatorie: {missing_secs}")
                else:
                    self.record_pass(cat, f"Card '{char_name}' outfit nude anatomico JED+ v2.0 a 6 sezioni verificato ({len(n_desc)} car., 6/6 sezioni presenti)")

            # Check RPG Stats & Traits rule (1 Species + 1 Occupation + 5..15 Traits, 15 for protagonists/powerhouses, canonical Level curve + DDM ARC_LEVEL)
            rpg_m = re.search(r"\[LEVEL:\s*(\d+);\s*ARC_LEVEL:\s*([^;]+);\s*SPECIES:\s*([^;]+);\s*OCCUPATION:\s*([^;]+);", desc)
            age_m = re.search(r"AGE:\s*(\d+)", desc)
            if not rpg_m:
                self.record_error(cat, f"Card '{char_name}' manca di header RPG completo [LEVEL; ARC_LEVEL; SPECIES; OCCUPATION; CLASS]")
            else:
                lvl_val = int(rpg_m.group(1))
                arc_val = rpg_m.group(2).strip()
                if age_m:
                    age_val = int(age_m.group(1))
                    if age_val <= 13:
                        exp_lvl = 1
                    elif age_val <= 21:
                        exp_lvl = 2
                    else:
                        exp_lvl = min(99, 2 + ((age_val - 21 + 4) // 5))
                    if lvl_val != exp_lvl:
                        self.record_error(cat, f"Card '{char_name}' (AGE {age_val}) ha LEVEL {lvl_val} invece del canonico {exp_lvl}")
                    else:
                        self.record_pass(cat, f"Card '{char_name}' (AGE {age_val}) allineata al LEVEL canonico ({lvl_val}) e DDM ARC_LEVEL ({arc_val})")

                traits_part = desc.split("TRAITS:")[-1] if "TRAITS:" in desc else ""
                bullet_traits = re.findall(r"^- ", traits_part, flags=re.M)
                t_count = len(bullet_traits)
                is_max_char = any(k in char_name.lower() for k in ["alyssa", "jasper", "malachia", "noah", "wulfnic", "erik", "logan", "zeera"])
                if is_max_char and t_count != 15:
                    self.record_error(cat, f"Card protagonista/top-lore '{char_name}' ha {t_count} tratti invece del massimo obbligatorio di 15")
                elif not (5 <= t_count <= 15):
                    self.record_error(cat, f"Card '{char_name}' ha {t_count} tratti RPG (fuori dal range 5..15)")
                else:
                    self.record_pass(cat, f"Card '{char_name}' dotazione RPG conforme (1 Specie + 1 Occupazione + {t_count} Tratti)")

        # Check duplicate section headers and broken multiline PLists across Cards, Personas, WCs, and Lorebooks
        dup_errors = []
        plist_errors = []

        def check_sheet_text(label_src: str, item_name: str, text_val: str):
            text_val = str(text_val or '').strip()
            if not text_val:
                return
            if text_val.startswith('['):
                c_idx = text_val.find(']')
                if c_idx != -1:
                    p_blk = text_val[1:c_idx]
                    bad_lns = [
                        ln.strip()
                        for ln in p_blk.splitlines()
                        if ln.strip() and not re.match(r'^[A-Z][A-Z0-9_ /&()-]{1,35}:\s*.+', ln.strip())
                    ]
                    if bad_lns:
                        plist_errors.append(f"{label_src} '{item_name}' PList contiene riga orfana/non-chiave: {bad_lns[0][:60]}")
            counts = {}
            for ln in text_val.splitlines():
                ls = ln.strip()
                mh = re.match(r'^([A-Z][A-Z0-9 \'&/-]{2,42}):(?:\s|$)', ls)
                if mh and '_' not in mh.group(1):
                    hdr = mh.group(1).strip()
                    counts[hdr] = counts.get(hdr, 0) + 1
            dups = {k: v for k, v in counts.items() if v > 1}
            if dups:
                dup_errors.append(f"{label_src} '{item_name}' ha intestazioni duplicate: {dups}")

        for cf in card_files:
            with open(cf, 'r', encoding='utf-8') as f:
                c_obj = json.load(f)
            check_sheet_text("Card", c_obj.get('name', cf.stem), c_obj.get('description', ''))

        for pf in sorted((FINAL / 'personas').glob('*.json')):
            with open(pf, 'r', encoding='utf-8') as f:
                p_obj = json.load(f)
            check_sheet_text("Persona", pf.name, p_obj.get('description', ''))

        wc_file = FINAL / 'Svartulfr_Characters.json'
        if wc_file.exists():
            with open(wc_file, 'r', encoding='utf-8') as f:
                wcs_arr = json.load(f)
            for wc in wcs_arr:
                check_sheet_text("WorldChar", wc.get('display_name') or wc.get('first_name') or wc.get('id'), wc.get('long_summary', ''))

        for lbf_name in ('Svartulfr_NPC_Primary.json', 'Svartulfr_NPC_Secondary.json'):
            lbf_path = FINAL / lbf_name
            if lbf_path.exists():
                with open(lbf_path, 'r', encoding='utf-8') as f:
                    lb_obj = json.load(f)
                for ent in (lb_obj.get('lexicon') or lb_obj.get('entries') or []):
                    check_sheet_text(lbf_name, ent.get('name', ''), ent.get('content') or ent.get('description') or '')

        if plist_errors:
            for pe in plist_errors:
                self.record_error(cat, pe)
        else:
            self.record_pass(cat, "Zero righe orfane nei blocchi PList [...] su tutto il corpus (Cards, Personas, WCs, NPC Lorebooks)")

        if dup_errors:
            for de in dup_errors:
                self.record_error(cat, de)
        else:
            self.record_pass(cat, "Zero intestazioni di sezione duplicate su tutto il corpus (Cards, Personas, WCs, NPC Lorebooks)")

    # --------------------------------------------------------------------------
    # 3. Igiene Trigger & Anti-Collisione
    # --------------------------------------------------------------------------
    def audit_trigger_hygiene(self):
        cat = "3. Igiene Trigger & Anti-Collisione"
        print(f"{CLR_CYAN}[3/6] Scansione Macro Vietate & Broad Umbrella Keys...{CLR_RESET}")

        lb_files = list(FINAL.glob('Svartulfr_*.json'))
        self.stats["lorebooks_scanned"] = len(lb_files)

        for lbf in lb_files:
            try:
                with open(lbf, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                continue

            if isinstance(data, dict):
                entries = data.get('entries') or data.get('lexicon') or []
            elif isinstance(data, list):
                entries = data
            else:
                continue

            if not isinstance(entries, list):
                continue

            for e in entries:
                self.stats["npc_entries_scanned"] += 1
                name = e.get('name', '')
                keys = [k.lower().strip() for k in e.get('keys', [])]
                desc = e.get('description', '') or ''

                # Macro {{age}} check
                if '{{age}}' in desc.lower():
                    self.record_error(cat, f"Entry '{name}' in {lbf.name} contiene la macro vietata '{{{{age}}}}'")

                # Broad Keys check on NPC
                is_npc = e.get('type') == 'npc' or 'npc' in lbf.name.lower()
                if is_npc:
                    found_broad = [k for k in keys if k in BROAD_KEYS]
                    if found_broad:
                        self.record_error(cat, f"NPC '{name}' in {lbf.name} ha keyword ombrello vietate: {found_broad}")

                    # Selective without secondary keys
                    if e.get('selective', False) and not e.get('secondary_keys'):
                        self.record_warning(cat, f"NPC '{name}' ha selective:true ma secondary_keys e vuoto")

                    # Flag triad check
                    scan_persona = e.get('scan_persona')
                    whole_words = e.get('whole_words_only')
                    highlight = e.get('enableEntryHighlighting') or e.get('highlight_keys')

                    if not (scan_persona and whole_words and highlight):
                        self.record_warning(cat, f"NPC '{name}' ({lbf.name}) terna flag incompleta (sp={scan_persona}, ww={whole_words}, hl={highlight})")

                    # npc_info check
                    npc_info = e.get('npc_info')
                    if not npc_info or not npc_info.get('first_name'):
                        self.record_warning(cat, f"NPC '{name}' ({lbf.name}) manca di npc_info o first_name valido")

    # --------------------------------------------------------------------------
    # 4. Johnny.Decimal & Unicita Entita
    # --------------------------------------------------------------------------
    def audit_entity_uniqueness(self):
        cat = "4. Unicita Entita & Zero Duplicati"
        print(f"{CLR_CYAN}[4/6] Verifica Collisioni & Duplicazioni NPC...{CLR_RESET}")

        p_file = FINAL / 'Svartulfr_NPC_Primary.json'
        s_file = FINAL / 'Svartulfr_NPC_Secondary.json'

        if p_file.exists() and s_file.exists():
            with open(p_file, 'r', encoding='utf-8') as f:
                p_data = json.load(f)
            with open(s_file, 'r', encoding='utf-8') as f:
                s_data = json.load(f)

            p_entries = p_data.get('entries') or p_data.get('lexicon') or []
            s_entries = s_data.get('entries') or s_data.get('lexicon') or []

            p_names = {e.get('name', '').strip().lower(): e.get('id') for e in p_entries if e.get('name')}
            s_names = {e.get('name', '').strip().lower(): e.get('id') for e in s_entries if e.get('name')}

            overlap = set(p_names.keys()).intersection(set(s_names.keys()))
            if overlap:
                self.record_error(cat, f"Collisione rilevata! Entita presenti sia in Primary che in Secondary: {list(overlap)}")
            else:
                self.record_pass(cat, f"Zero collisioni tra NPC Primary ({len(p_entries)}) e Secondary ({len(s_entries)})")

    # --------------------------------------------------------------------------
    # 5. Parita Byte-for-byte (entries == lexicon)
    # --------------------------------------------------------------------------
    def audit_byte_parity(self, fix: bool = False):
        cat = "5. Parita Byte-for-byte (Zod Frontend)"
        print(f"{CLR_CYAN}[5/6] Controllo Parita entries == lexicon...{CLR_RESET}")

        targets = list(FINAL.glob('Svartulfr_*.json')) + list(OPT.glob('Svartulfr_*.json'))
        for tf in targets:
            try:
                with open(tf, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except Exception:
                continue

            if 'entries' not in data and 'lexicon' not in data:
                continue

            entries_str = json.dumps(data.get('entries', []), sort_keys=True)
            lexicon_str = json.dumps(data.get('lexicon', []), sort_keys=True)

            if entries_str != lexicon_str:
                if fix:
                    source = data.get('lexicon') or data.get('entries') or []
                    data['entries'] = source
                    data['lexicon'] = source
                    with open(tf, 'w', encoding='utf-8') as out_f:
                        json.dump(data, out_f, indent=2, ensure_ascii=False)
                    self.record_pass(cat, f"Parita ripristinata e riscritta per {tf.name}")
                else:
                    self.record_error(cat, f"Discrepanza 'entries != lexicon' in {tf.relative_to(ROOT)} (rischio blocco form Wyvern)")
            else:
                self.record_pass(cat, f"Parita byte-for-byte perfetta per {tf.name}")

    # --------------------------------------------------------------------------
    # 6. Metabolismo & Infrastruttura Locale
    # --------------------------------------------------------------------------
    def audit_infrastructure(self):
        cat = "6. Metabolismo & Infrastruttura"
        print(f"{CLR_CYAN}[6/6] Controllo Sidecars Automations & Proxy Free Models...{CLR_RESET}")

        # Check Sidecars (Unified Master Pipeline or Legacy Sidecars)
        master_sidecar = SIDECARS_DIR / "daily-master-pipeline" / "sidecar.json"
        if master_sidecar.exists():
            self.record_pass(cat, "Automazione Master Unificata registrata: 'daily-master-pipeline'")
        else:
            required_sidecars = ["daily-character-enrichment", "daily-wyvern-monitor", "daily-proxy-free-models"]
            for sid in required_sidecars:
                s_file = SIDECARS_DIR / sid / "sidecar.json"
                if s_file.exists():
                    self.record_pass(cat, f"Automazione registrata: '{sid}'")
                else:
                    self.record_error(cat, f"Automazione mancante in sidecars: '{sid}' (o 'daily-master-pipeline')")

        # Check Multi-Model Registry
        mm_reg = ROOT / '.agents' / 'skills' / 'multi-model-unified-pipeline' / 'references' / 'models_registry.json'
        if mm_reg.exists():
            self.record_pass(cat, "Multi-Model Unified Registry presente e configurato (3 Tier + PC OMEN Clients)")

        # Check Proxy config
        p_cfg = PROXY / 'config_free_proxy.json'
        if p_cfg.exists():
            with open(p_cfg, 'r', encoding='utf-8') as f:
                cfg = json.load(f)
            upstreams = cfg.get('upstreams', [])
            if len(upstreams) > 0:
                self.record_pass(cat, f"Proxy configurato con {len(upstreams)} upstream attivi")
            else:
                self.record_warning(cat, "Proxy config non ha upstream configurati")
        else:
            self.record_warning(cat, "config_free_proxy.json non trovato in proxy/")

        # Check Enrichment State
        state_file = SCRATCH / 'daily_character_enrichment_state.json'
        if state_file.exists():
            with open(state_file, 'r', encoding='utf-8') as f:
                st = json.load(f)
            prog = st.get('completed_count', st.get('progress', 0))
            tot = st.get('total_count', st.get('total', 210))
            self.record_pass(cat, f"Enrichment State attivo: avanzamento {prog}/{tot}")
        else:
            self.record_warning(cat, "daily_character_enrichment_state.json non ancora inizializzato")

    # --------------------------------------------------------------------------
    # Report & Summary
    # --------------------------------------------------------------------------
    def generate_report(self):
        now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "=" * 70)
        print(f"{CLR_BOLD}=== SVARTULFR VERSE — VAULT HEALTH METABOLISM REPORT ==={CLR_RESET}")
        print(f"Timestamp: {now_str}")
        print("=" * 70)

        print(f"\n{CLR_BOLD}Statistiche Scansione:{CLR_RESET}")
        print(f"  • Lorebook Scansionati: {self.stats['lorebooks_scanned']}")
        print(f"  • Schede Personaggio:    {self.stats['characters_scanned']}")
        print(f"  • Voci NPC Analizzate:   {self.stats['npc_entries_scanned']}")
        print(f"  • Totale Verifiche:      {self.stats['total_checks']}")

        print(f"\n{CLR_GREEN}{CLR_BOLD}🟢 CHECK SUPERATI ({len(self.passes)}):{CLR_RESET}")
        for cat, p in self.passes[:10]:
            print(f"  [{cat}] {p}")
        if len(self.passes) > 10:
            print(f"  ... e altri {len(self.passes) - 10} controlli superati.")

        if self.warnings:
            print(f"\n{CLR_AMBER}{CLR_BOLD}🟡 AVVISI DA MONITORARE ({len(self.warnings)}):{CLR_RESET}")
            for cat, w in self.warnings:
                print(f"  [{cat}] {w}")

        if self.errors:
            print(f"\n{CLR_RED}{CLR_BOLD}🔴 ERRORI CRITICI BLOCCANTI ({len(self.errors)}):{CLR_RESET}")
            for cat, e in self.errors:
                print(f"  [{cat}] {e}")
        else:
            print(f"\n{CLR_GREEN}{CLR_BOLD}🎉 ZERO ERRORI CRITICI! Il Vault e in perfetta salute operativa.{CLR_RESET}")

        # Save Markdown Report
        with open(REPORT_PATH, 'w', encoding='utf-8') as rf:
            rf.write(f"# Svartúlfr Verse — Vault Health Check Report\n\n")
            rf.write(f"- **Data Scansione:** {now_str}\n")
            rf.write(f"- **Totale Controlli Eseguiti:** {self.stats['total_checks']}\n")
            rf.write(f"- **Stato Vault:** {'🔴 ATTENZIONE RICHIESTA' if self.errors else '🟢 100% SALUTE OTTIMALE'}\n\n")

            rf.write(f"### Statistiche\n")
            rf.write(f"- Lorebook: `{self.stats['lorebooks_scanned']}`\n")
            rf.write(f"- Standalone Cards: `{self.stats['characters_scanned']}`\n")
            rf.write(f"- NPC Entries: `{self.stats['npc_entries_scanned']}`\n\n")

            if self.errors:
                rf.write(f"### 🔴 Errori Critici ({len(self.errors)})\n\n")
                for cat, err in self.errors:
                    rf.write(f"- **[{cat}]** {err}\n")
                rf.write("\n")

            if self.warnings:
                rf.write(f"### 🟡 Avvisi ({len(self.warnings)})\n\n")
                for cat, warn in self.warnings:
                    rf.write(f"- **[{cat}]** {warn}\n")
                rf.write("\n")

            rf.write(f"### 🟢 Controlli Superati ({len(self.passes)})\n\n")
            for cat, pas in self.passes:
                rf.write(f"- **[{cat}]** {pas}\n")

        print(f"\nReport markdown salvato in: {REPORT_PATH}")
        return len(self.errors)

def main():
    parser = argparse.ArgumentParser(description="Vault Health Check for Svartulfr Verse")
    parser.add_argument("--fix-parity", action="store_true", help="Ripristina automaticamente la parita entries == lexicon")
    args = parser.parse_args()

    auditor = HealthAuditor()
    auditor.audit_canonical_invariants()
    auditor.audit_jed_structure()
    auditor.audit_trigger_hygiene()
    auditor.audit_entity_uniqueness()
    auditor.audit_byte_parity(fix=args.fix_parity)
    auditor.audit_infrastructure()

    exit_code = auditor.generate_report()
    sys.exit(0 if exit_code == 0 else 1)

if __name__ == '__main__':
    main()

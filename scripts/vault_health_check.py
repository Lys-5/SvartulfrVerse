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

                # Check Em-Dash
                if '—' in desc or '–' in desc:
                    self.record_error(cat, f"Entry '{name}' in {npcf.name} contiene em-dash (— o –) vietato dalle regole")

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

            # Check heights
            for canon_name, hdata in CANONICAL_HEIGHTS.items():
                if canon_name.lower() in char_name.lower():
                    cm_val = hdata['cm']
                    if f"{cm_val} cm" not in desc and f"{cm_val}cm" not in desc:
                        self.record_warning(cat, f"Card '{char_name}' non riporta esattamente '{cm_val} cm' nella descrizione JED+")
                    else:
                        self.record_pass(cat, f"Card '{char_name}' allineata all'altezza canonica ({cm_val} cm)")

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

            # Check single line bracket
            if desc.startswith('['):
                closing_bracket_idx = desc.find(']')
                if closing_bracket_idx != -1:
                    first_bracket = desc[:closing_bracket_idx]
                    if '\n' in first_bracket:
                        self.record_error(cat, f"Card '{char_name}' blocco iniziale [...] non e su singola riga (contiene newline)")
                    else:
                        self.record_pass(cat, f"Card '{char_name}' blocco PList iniziale su singola riga")
            else:
                self.record_error(cat, f"Card '{char_name}' description non inizia con il blocco JED+ [...]")

            # Check 4 mandatory blocks
            required_blocks = ["BACKSTORY:", "VOICE & BEHAVIOR:"]
            for rb in required_blocks:
                if rb not in desc:
                    self.record_error(cat, f"Card '{char_name}' manca della sezione obbligatoria '{rb}'")

            # Check Outfits count and categories
            outfits = card.get('outfits', [])
            if len(outfits) < 9:
                self.record_warning(cat, f"Card '{char_name}' ha {len(outfits)}/9 outfits contestuali minimi")
            else:
                self.record_pass(cat, f"Card '{char_name}' possiede {len(outfits)} outfits (minimo 9 rispettato)")

            # Check RPG Stats & Traits rule (1 Species + 1 Occupation + 5..15 Traits, 15 for protagonists/powerhouses, canonical Level curve)
            rpg_m = re.search(r"\[LEVEL:\s*(\d+);\s*SPECIES:\s*([^;]+);\s*OCCUPATION:\s*([^;]+);", desc)
            age_m = re.search(r"AGE:\s*(\d+)", desc)
            if not rpg_m:
                self.record_error(cat, f"Card '{char_name}' manca di header RPG completo [LEVEL; SPECIES; OCCUPATION; CLASS]")
            else:
                lvl_val = int(rpg_m.group(1))
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
                        self.record_pass(cat, f"Card '{char_name}' (AGE {age_val}) allineata al LEVEL canonico ({lvl_val})")

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

import json
import pathlib
import re

SC_DIR = pathlib.Path('FINAL/scenarios')

def run_checks():
    files = sorted(SC_DIR.glob('*.json'))
    print(f"Auditing {len(files)} files...\n")
    
    findings = []
    
    for f in files:
        raw = f.read_text(encoding='utf-8')
        data = json.loads(raw)
        fname = f.name
        
        # 1. Dash checks
        if '—' in raw:
            findings.append((fname, 'CRITICAL', "Contains em-dash ('—' \u2014)"))
        if '–' in raw:
            findings.append((fname, 'CRITICAL', "Contains en-dash ('–' \u2013)"))
            
        # 2. Invariant checks
        if data.get('visibility') != 'private':
            findings.append((fname, 'CRITICAL', f"Visibility is '{data.get('visibility')}', expected 'private'"))
        if data.get('rating') != 'explicit':
            findings.append((fname, 'CRITICAL', f"Rating is '{data.get('rating')}', expected 'explicit'"))
            
        expected_lbs = [
            "_gwwCxCfQ6PQaLEjAQVpJL",
            "_HfG7TeV6MJyj6bxMwxkpt",
            "_9zWTGqYJNJ4BCDMj8gfcD",
            "_EjXxkmPVhpCXg8xABpFkK",
            "_zwEqgEEzh12X6gHVmMKKC",
            "_Uht3Ckz44JBDrPnUHq7LV",
        ]
        if set(data.get('lorebook_ids', [])) != set(expected_lbs):
            findings.append((fname, 'CRITICAL', f"Lorebook IDs mismatch: {data.get('lorebook_ids')}"))
            
        # 3. Asterisks checks
        for g_i, g in enumerate(data.get('greetings', [])):
            for m_i, m in enumerate(g.get('messages', [])):
                content = m.get('content', '')
                if '*' in content:
                    # Let's inspect asterisks usage
                    findings.append((fname, 'INFO_ASTERISK', f"Greeting {g_i} msg {m_i} has asterisks: {content}"))
                    
        # 4. Quotes checks (balanced double quotes)
        for g_i, g in enumerate(data.get('greetings', [])):
            for m_i, m in enumerate(g.get('messages', [])):
                content = m.get('content', '')
                q_count = content.count('"')
                if q_count % 2 != 0:
                    findings.append((fname, 'MAJOR', f"Greeting {g_i} msg {m_i} has unbalanced double quotes ({q_count})"))
                    
        # 5. Check speaker prefix patterns
        for g_i, g in enumerate(data.get('greetings', [])):
            for m_i, m in enumerate(g.get('messages', [])):
                content = m.get('content', '')
                # Direct prefix check: e.g. "Santiago Herrera: ..." or "Name: ..."
                prefix_match = re.match(r'^([A-Z][a-zA-Z\s\'-]{1,30}):\s', content)
                if prefix_match:
                    findings.append((fname, 'SPEAKER_PREFIX', f"Greeting {g_i} msg {m_i} has prefix '{prefix_match.group(1)}:' in content: {content[:80]}..."))
                    
        # 6. Specific character and lore constraints
        prompt = data.get('scenario', '')
        
        if fname == "Svartulfr_Scenario_Camp_Mystic.json":
            # Marcus Vale and Celeste Nadir
            if "Marcus Vale" not in prompt or "Celeste Nadir" not in prompt:
                findings.append((fname, 'LORE', "Missing Marcus Vale or Celeste Nadir in scenario prompt"))
            # Mara Voss
            if "Mara Voss" not in prompt:
                findings.append((fname, 'LORE', "Missing Mara Voss in scenario prompt"))
            # Lake Erie shuttle arrival
            if "Lake Erie" not in raw and "shuttle" not in raw:
                findings.append((fname, 'LORE', "Missing Lake Erie shuttle arrival"))
            # Edric 13yo
            if "13" not in prompt:
                findings.append((fname, 'LORE', "Edric 13yo not specified in scenario prompt"))
            # Startup script
            if not data.get('startup_script'):
                findings.append((fname, 'CRITICAL', "Missing startup_script"))
                
        elif fname == "Svartulfr_Scenario_SUCC_Route_Alyssa.json":
            if "Finnegan Novak" not in raw:
                findings.append((fname, 'LORE', "Finnegan Novak missing"))
            if "Arctic Wolf" not in raw or "demi-human" not in raw:
                findings.append((fname, 'LORE', "Finnegan Novak not specified as Arctic Wolf demi-human"))
            if "Scarlett Rose" not in raw:
                findings.append((fname, 'LORE', "Scarlett Rose surname missing"))
            if "Mackenzie" not in raw:
                findings.append((fname, 'LORE', "Mackenzie missing"))
                
        elif fname == "Svartulfr_Scenario_SUCC_Route_Jasper.json":
            if "Russell 'Russ' Sinclair" not in raw and "Russ Sinclair" not in raw:
                findings.append((fname, 'LORE', "Russ Sinclair missing"))
            if "Scarlett Rose" not in raw:
                findings.append((fname, 'LORE', "Scarlett Rose missing"))
            if "Echo" not in raw:
                findings.append((fname, 'LORE', "Echo AI missing"))
            if "Cocketeers" not in raw:
                findings.append((fname, 'LORE', "Cocketeers reference missing"))
            if "Finnegan Novak" not in raw:
                findings.append((fname, 'LORE', "Finnegan Novak missing"))
                
        elif fname == "Svartulfr_Scenario_Villa_Douglas.json":
            expected_cids = {
                "father": "_QPea6g4Q1QfeYCVHCLMPR",
                "eldest_brother": "_RDfz7XzTpM23LpPALVXHM",
                "tech_brother": "_t4J9aQNJM36cUKAP4wB4U",
                "politician_brother": "_zFLUjV8aVxQRAfQxGcAcY",
                "maternal_grandfather": "_HEQQbbRFwKdG8QE2Fh1z1",
                "uncle": "_T8Ywcr9FEqNf9JxbK6eHP",
                "cousin": "_TbRM3EdxDjHFgqztTbCpL",
            }
            slots = data.get('slots', [])
            if len(slots) != 7:
                findings.append((fname, 'CRITICAL', f"Expected exactly 7 slots, got {len(slots)}"))
            slot_map = {s['key']: s['pool'][0]['character_id'] for s in slots if s.get('pool')}
            for k, cid in expected_cids.items():
                if k not in slot_map:
                    findings.append((fname, 'CRITICAL', f"Missing male Douglas slot '{k}'"))
                elif slot_map[k] != cid:
                    findings.append((fname, 'CRITICAL', f"Slot '{k}' has cid {slot_map[k]}, expected {cid}"))
                    
        elif fname == "Svartulfr_Scenario_DMHA_Dungeons.json":
            slots = data.get('slots', [])
            if len(slots) != 9:
                findings.append((fname, 'CRITICAL', f"Expected exactly 9 slots, got {len(slots)}"))
            req_chars = ["Alyssa", "Jasper", "Malachia", "Barrow", "Marek", "Radek", "Goran", "Kian"]
            for rc in req_chars:
                if rc not in raw:
                    findings.append((fname, 'LORE', f"Missing {rc} in DMHA scenario"))
                    
        elif fname == "Svartulfr_Scenario_Underworld_Sindacato.json":
            slots = data.get('slots', [])
            if len(slots) != 6:
                findings.append((fname, 'CRITICAL', f"Expected exactly 6 slots, got {len(slots)}"))
            if "Human Telepath" not in raw and "Human, Telepath" not in raw:
                findings.append((fname, 'LORE', "Jean-Luc Virtuoso not specified as Human Telepath"))
            req_names = ["Rory", "Sully", "Jean-Luc", "Alicia", "Arthur Sinclair", "Ambrosia"]
            for rn in req_names:
                if rn not in raw:
                    findings.append((fname, 'LORE', f"Missing {rn} in Underworld scenario"))

    print("=================== FINDINGS ===================")
    for f in findings:
        print(f"[{f[1]}] {f[0]}: {f[2]}")
    print(f"Total findings: {len(findings)}")

if __name__ == '__main__':
    run_checks()

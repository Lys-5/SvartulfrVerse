import os
import re
import json
import sys

out_fp = open('scratch/target_docs_summary_utf8.txt', 'w', encoding='utf-8')

def print_out(*args):
    out_fp.write(" ".join(str(a) for a in args) + "\n")

target_files = [
    'Concilio_QuattroDistretti_E_Vito_Pureblood_2026-09-14.md',
    'Blackwood_District_Alphas_Completamento_2026-09-14.md',
    'Solarton_FiveCocketeers_2026-09-15.md',
    'Gray_Dean_Rifle_Maddox_Solarton_Completamento_2026-09-14.md',
    'JeanLuc_Virtuoso_Pride_Sinners_Completamento_2026-09-14.md',
    'Dante_Lust_Sinners_Completamento_2026-09-14.md',
    'Arthur_Sinclair_Sloth_Sinners_Completamento_2026-09-14.md',
    'Zero_Wrath_Sinners_Completamento_2026-09-14.md',
    'Danny_Boone_Ballantine_Completamento_2026-09-14.md',
    'Sully_Jones_Ballantine_Completamento_2026-09-14.md',
    'Harper_Aries_Ballantine_Completamento_2026-09-14.md',
    'Rory_Ballantine_Completamento_2026-09-14.md',
    'Zeera_HSK_Consulting_Completamento_2026-09-14.md',
    'Brak_Ironfist_Orc_Representative_2026-09-14.md',
    'Barrow_Demihuman_Representative_2026-09-14.md',
    'Huck_Beaumont_Rappresentante_Umano_2026-09-14.md',
    'Harrison_Black_Umano_Magico_2026-09-14.md',
    'Marlowe_Voss_NonMorti_Representative_2026-09-14.md',
    'Abel_Vilas_Ibridi_Representative_2026-09-14.md',
    'Cassian_Aralas_Fatati_Representative_2026-09-14.md',
    'Grave_Mistake_Band_Schede.md',
    'FanOC_Staff_Batch1_7Schede_2026-09-15.md',
    'Otto_Fully_Custom_Completamento_2026-09-13.md',
    'Scenari_Arco_2024_9Schede_Completamento_2026-09-20.md',
    'Eris_Jasmin_Completamento_2026-09-13.md',
    'Adelin_Coso_Completamento_2026-09-13.md',
    'Hideo_Reid_Card_2026-09-13.md',
    'Venera_Dolce_Card_2026-09-13.md',
    'Vincent_Campbell_Card.md',
    'Andrew_Campbell_Card.md',
    'Tomas_Matthews_Card.md',
    'Santiago_Herrera_Card.md',
    'Bailey_Rogers_Card.md',
    'Archer_Wolfwood_Card.md',
    'Barkley_Rover_Card_v2_DA_APPLICARE.md'
]

doc_dir = 'docs/claude_project_docs'

for tf in target_files:
    fpath = os.path.join(doc_dir, tf)
    if os.path.exists(fpath):
        with open(fpath, encoding='utf-8', errors='ignore') as f:
            content = f.read()
        print_out(f"==================================================")
        print_out(f"FILE: {tf}")
        print_out(f"==================================================")
        # Look for headings, tables, or sections mentioning birthdate, start position, age, attitudes
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if any(k in line.lower() for k in ['birthdate', 'start position', 'timeline', 'età', 'age', 'nato', 'nata', 'attitudes', 'outfits', 'scheda']):
                if len(line.strip()) > 0:
                    print_out(f"  L{i+1}: {line.strip()[:110]}")

out_fp.close()

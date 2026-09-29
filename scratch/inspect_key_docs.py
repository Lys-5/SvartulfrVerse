import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('drive/claude_export/extracted/projects/projects/01a03cfa-cebb-74ef-be69-f24d0ae96ed0.json', encoding='utf-8') as f:
    claude_proj = json.load(f)

docs = {d['filename']: d['content'] for d in claude_proj.get('docs', [])}

target_docs = [
    'claude/NPC_Import_Rules_1to1.md',
    'claude/Outfit_Census.md',
    'claude/Attitudes_Audit_2026-09-03.md',
    'claude/Audit_Schede_2026-09-03.md',
    'claude/Grave_Mistake_Band_Schede.md',
    'claude/Solarton_FiveCocketeers_2026-09-15.md',
    'claude/FanOC_Staff_Batch1_7Schede_2026-09-15.md',
    'claude/Concilio_QuattroDistretti_E_Vito_Pureblood_2026-09-14.md',
    'claude/Blackwood_District_Alphas_Completamento_2026-09-14.md',
    'claude/Audit_Blackwood_Family_Pack_Concilio_2026-09-14.md',
    'claude/Thompson_Family_Reference.md',
    'claude/Tate_And_The_Lab_Survivors.md',
    'claude/Huck_Beaumont_Rappresentante_Umano_2026-09-14.md',
    'claude/Harrison_Black_Umano_Magico_2026-09-14.md',
    'claude/Marlowe_Voss_NonMorti_Representative_2026-09-14.md',
    'claude/Abel_Vilas_Ibridi_Representative_2026-09-14.md'
]

for td in target_docs:
    if td in docs:
        print(f"=== {td} ({len(docs[td])} bytes) ===")
        # Print first 20 lines
        lines = docs[td].split('\n')
        for l in lines[:25]:
            print("  ", l)
    else:
        print(f"MISSING: {td}")

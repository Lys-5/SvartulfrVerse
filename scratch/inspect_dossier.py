import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/g2_dossier.json', encoding='utf-8') as f:
    dossier = json.load(f)

for d in dossier:
    name = d['name']
    bdf = d['bday_field']
    cur_bd = str(d['current_birthdate'])
    ages = d['found_ages']
    bdays = d['found_bdays']
    sp = d['species'][:25]
    print(f"{name:30s} | bday_f: {bdf:20s} | cur_bd: {cur_bd:10s} | ages: {str(ages):30s} | bdays: {str(bdays)}")

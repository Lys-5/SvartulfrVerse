import json

with open('FINAL/Svartulfr_Lorebook_III.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

target_names = [
    'Demografia e Popolazione Studentesca SUCC',
    'Corsi di Laurea e Facoltà SUCC',
    'SUCC Bulls (Squadra Football Americano)',
    'SUCC Bears (Squadra Hockey su Ghiaccio)',
    'Programmi Sportivi Universitari SUCC',
    'Campus SUCC - Luoghi e Strutture Principali'
]

for e in d['entries']:
    name = e.get('name', '')
    if any(t in name for t in target_names):
        print(f"=== {name} (id: {e.get('id')}) ===")
        print(f"Keys: {e.get('keys')}")
        print(f"Content:\n{e.get('content')}\n")

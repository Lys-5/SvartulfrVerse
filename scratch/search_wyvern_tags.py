import pathlib

tags = pathlib.Path('scratch/clean_tags_list.txt').read_text(encoding='utf-8').splitlines()

def find_tags(query):
    return [t for t in tags if query.lower() in t.lower()]

print("Species tags:")
for q in ['wolf', 'were', 'demon', 'succubus', 'monster', 'naga', 'snake', 'bull', 'minotaur', 'oni', 'human', 'fae', 'vampire']:
    m = find_tags(q)
    if m:
        print(f"  {q}: {m}")

print("\nOccupation tags:")
for q in ['student', 'artist', 'biker', 'mechanic', 'bodyguard', 'military', 'soldier', 'boss', 'executive', 'ceo', 'musician', 'doctor', 'nurse']:
    m = find_tags(q)
    if m:
        print(f"  {q}: {m}")

print("\nGeneral / Archetype:")
for q in ['fantasy', 'supernatural', 'modern', 'original', 'alpha', 'omega', 'beta', 'jed', 'romance', 'college', 'school', 'urban']:
    m = find_tags(q)
    if m:
        print(f"  {q}: {m}")

import json
import re

SCRAPED_FILE = r'D:\SvartulfrVerse\ARCHIVIO\01_Drafts\Character_Cards_V1\Scraped_Characters.md'

WYVERN_CHARS = [
  "Boros Darkfire", "Karshin Darkfire", "Aras Darkfire", "Varg Darkfire", "Ren",
  "Nicole O'Connor", "Marek", "Kian", "Goran", "Radek", "Eithne Dal'Kereth",
  "Yael", "Bryson", "Fenris", "Zero", "Zefir Hvitskog", "Zeera Darkfire",
  "Wulfnic Bloodmoon", "Vito Marino", "Viola Carter", "Vincent Campbell",
  "Ut Berg", "Tomas Matthews", "Tate", "Sullivan \"Sully\" Jones",
  "Stanley Davies Sr.", "Stanley Davies Jr.", "Sierra", "Scarlett Rose",
  "Santiago Herrera", "Russ Sinclair", "Ruaraidh \"Rory\" Ballantine",
  "Roman Blackwood", "Roland Vickers", "Rev", "Raymond",
  "Professor Mollusk Moreau", "Professor Marit Christiansen",
  "Professor Loewe", "Oskar", "Noah Douglas Bloodmoon", "Nixara Bloodmoon",
  "Nikolaj Jökull", "Naomi Black", "Marlowe Voss", "Marcus Thornfield",
  "Marcus O'Connor", "Malachia Douglas Bloodmoon", "Magnus Douglas III",
  "Mackenzie Sanchez-Rogers", "Luisa Sanchez Rogers", "Lord Cornelius Douglas",
  "Logan Douglas", "Kolya Varenkov", "Kaladin Nargathon", "Jean-Luc Virtuoso",
  "Javier Reyes", "Jasper Douglas Bloodmoon", "Jasmin Thompson",
  "Jared Thompson", "Janice Thompson", "Isobel Blackwater", "Iordan R. Vess",
  "Hideo Reid", "Helena Weiss", "Harrison Black", "Harper Aries",
  "Harlan Beaumont", "Hank Thompson", "GREED - Roxie", "GLUTTONY - Kevin",
  "Finnegan Novak", "Federico \"Riki\" Savini", "Fade Greymoor", "Eris Davies",
  "Erik Douglas", "Eric", "Elizabeth Duskwood", "Edric Douglas", "Eclipse Noir",
  "ENVY - Siobhan", "Dullahan", "Dr. Arthur Sinclair", "Dominic Rogers",
  "Dominic Chen", "Dean", "Darius Vale", "Dante", "Daniel \"Danny\" Boone",
  "Coach Mithers", "Chase Anderson", "Cassian Aralas", "Cass Harrow",
  "Casey Williams", "Brittany Willow", "Brak Ironfist", "Bianca Rossi",
  "Barrow", "Barkley Rover", "Bailey Rogers", "Aurora Night", "Ariadne Cirillo",
  "Archer Wolfwood", "Angelo Moreno", "Andrew Campbell",
  "Alyssa Douglas Bloodmoon", "Allegra Lumsden", "Alicia Virtuoso",
  "Adelin Coso", "Abel Vilas "
]

def load_scraped_names():
    with open(SCRAPED_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    names = []
    for line in content.split('\n'):
        if line.startswith('## '):
            names.append(line.replace('## ', '').strip())
    return names

def normalize(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9]', '', name)
    return name

def main():
    scraped = load_scraped_names()
    wyvern_norm = {normalize(n): n for n in WYVERN_CHARS}
    
    matches = []
    missing = []
    
    for s in scraped:
        norm = normalize(s)
        matched = False
        for w_norm, w_orig in wyvern_norm.items():
            if norm in w_norm or w_norm in norm:
                matches.append((s, w_orig))
                matched = True
                break
        if not matched:
            missing.append(s)
            
    print("### ALREADY IN WYVERN (To Merge)")
    for s, w in matches:
        print(f"- {s} (Matches: {w})")
        
    print("\n### NEW CHARACTERS (To Create Ex Novo)")
    for s in missing:
        print(f"- {s}")

if __name__ == '__main__':
    main()

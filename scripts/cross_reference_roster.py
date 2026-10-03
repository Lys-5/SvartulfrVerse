import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    world_data = json.load(f)

world_characters = { (c.get('name') or c.get('display_name') or '').lower(): c for c in world_data['world_characters'] }
world_lexicon = { (l.get('name') or '').lower(): l for l in world_data['world_lexicon_entries'] }

roster_31 = [
    ("Abel Vilas", "Sea dragon", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/b98d6546.jpg?v=2881d07e"),
    ("Adrian Locke", "Werewolf", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/08c5a9fa.jpg?v=2881d07e"),
    ("Alistair DeVille", "Human", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/b308459d.jpg?v=2881d07e"),
    ("Angui", "Swamp thing", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/c22bee08.jpg?v=2881d07e"),
    ("Arthur Grey", "Rabbit demi", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/93ef6885.jpg?v=2881d07e"),
    ("Atlas Teague", "Werewolf", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/9eba5831.jpg?v=2881d07e"),
    ("Cato", "Alligator demi", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/54231706.jpg?v=2881d07e"),
    ("Cyrus Camden", "Rabbit demi", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/a9af2e2f.jpg?v=2881d07e"),
    ("Damien Bishop", "Demon", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/03d6f9f0.jpg?v=2881d07e"),
    ("Emil", "Fallen angel", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/c9f7c97d.jpg?v=2881d07e"),
    ("Everett Rottmore", "Cursed", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/22a98739.jpg?v=2881d07e"),
    ("Emlyn Danes", "Harpy", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/b821e71d.jpg?v=2881d07e"),
    ("Garrett Locke", "Vampire", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/308b0b41.jpg?v=2881d07e"),
    ("Gianni Luciano", "Manticore", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/9b0d6c39.jpg?v=2881d07e"),
    ("Graham Purcell", "Bear demi", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/06308116.jpg?v=2881d07e"),
    ("Ilya Volkov", "Werewolf", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/4cdc036e.jpg?v=2881d07e"),
    ("Julian Bieri", "Unicorn demi", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/8a25da51.jpg?v=2881d07e"),
    ("Kade Leavis", "Werewolf", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/b06e3112.jpg?v=2881d07e"),
    ("Kai Monroe", "Incubus", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/dbfc955d.jpg?v=2881d07e"),
    ("Levi Graham", "Ram demi", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/e1c09189.jpg?v=2881d07e"),
    ("Miles Airhardt", "Werewolf", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/d78ac878.jpg?v=2881d07e"),
    ("Milo Grayson", "Werewolf", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/fc4661f3.jpg?v=2881d07e"),
    ("Nic Lucero", "Goat demi/Demon", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/3f6a55d2.jpg?v=2881d07e"),
    ("Park Jae-Sung", "Lizard demi", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/b3642974.jpg?v=2881d07e"),
    ("Rafael Callaway", "Werewolf", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/299f561a.jpg?v=2881d07e"),
    ("Rhett Moore", "Dove demi", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/650ea6f4.jpg?v=2881d07e"),
    ("Jayce Collins", "Crow demi", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/650ea6f4.jpg?v=2881d07e"),
    ("Romeo Gray Dean", "Werewolf", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/d72ec552.jpg?v=2881d07e"),
    ("Ruaraidh Ballantine", "Dragon demi", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/7ba6a268.jpg?v=2881d07e"),
    ("Sullivan Jones", "Fixer/Human", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/368fb9c7.jpg?v=2881d07e"),
    ("Vale Roberts", "Centaur", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/b98d086b.jpg?v=2881d07e"),
    ("Vasile Ionescu", "Hunter", "https://io-modernfantasy.uwu.ai/assets/images/gallery03/424fe3ff.jpg?v=2881d07e")
]

print("=== STATO DETTAGLIATO DEI 32 PERSONAGGI DI IO-MODERNFANTASY NEL WORLD ===")
for name, sp, avatar in roster_31:
    first_name = name.split()[0].lower()
    
    match_c = None
    for k, c in world_characters.items():
        if first_name in k:
            match_c = c
            break
            
    match_l = None
    for k, l in world_lexicon.items():
        if first_name in k:
            match_l = l
            break
            
    if match_c:
        c_name = match_c.get('name') or match_c.get('display_name')
        print(f"[OK CHARACTER] {name:20} -> {c_name} (ID: {match_c['id']}) | Has Avatar: {bool(match_c.get('avatar'))}")
    elif match_l:
        l_name = match_l.get('name') or match_l.get('title')
        print(f"[OK LEXICON]   {name:20} -> {l_name} (ID: {match_l['id']}) | Has Avatar: {bool(match_l.get('avatar'))}")
    else:
        print(f"[MANCANTE]     {name:20} -> DA CREARE! (Specie: {sp})")

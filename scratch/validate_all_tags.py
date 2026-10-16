import json
import pathlib

valid_tags = set(json.loads(pathlib.Path('scratch/wyvern_clean_tags.json').read_text(encoding='utf-8')))

all_card_tags = {
  'Alyssa': ["JED", "Third Person", "AnyPOV", "Female", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Omega", "Student", "Fluff"],
  'Erik': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Alpha", "CEO"],
  'Jasper': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Beta", "Musician", "Student"],
  'Noah': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Student"],
  'Malachia': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Alpha", "Bodyguard", "Athlete"],
  'Logan': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Beta", "Mechanic"],
  'Edric': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Student"],
  'Wulfnic': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Historical", "Supernatural", "Original", "Werewolf", "Mythology"],
  'Elizabeth': ["JED", "Third Person", "AnyPOV", "Female", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Omega", "Doctor"],
  'Magnus': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Historical", "Supernatural", "Original", "Werewolf", "Royalty"],
  'Kaladin': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Alpha", "Military", "Bodyguard"],
  'Zeera': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Demon", "CEO"],
  'Jared': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Minotaur", "Demihuman", "Student", "Athlete", "Himbo"],
  'Mac': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Musician", "Artist"],
  'Marek': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Monster", "Demihuman"],
  'Russ': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Human", "Student", "Artist"],
  'Neon': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Demihuman", "Musician", "Cyberpunk"],
  'Scarlett': ["JED", "Third Person", "AnyPOV", "Female", "Fantasy", "Modern", "Supernatural", "Original", "Succubus (Incubus)", "Demihuman", "Student"],
  'Sierra': ["JED", "Third Person", "AnyPOV", "Female", "Fantasy", "Modern", "Supernatural", "Original", "Naga", "Demihuman", "Student", "Monster"],
  'Stan': ["JED", "Third Person", "AnyPOV", "Male", "Fantasy", "Modern", "Supernatural", "Original", "Werewolf", "Alpha", "Student", "Artist"]
}

has_err = False
for char, tlist in all_card_tags.items():
    bad = [t for t in tlist if t not in valid_tags]
    if bad:
        print(f"ERROR: {char} has invalid tags: {bad}")
        has_err = True

if not has_err:
    print("ALL 20 CHARACTER TAG SETS ARE 100% VALID!")

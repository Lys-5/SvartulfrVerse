import json
import re

print("--- Testing updates logic ---")

# 1. Edric Card
with open('FINAL/Edric_Douglas_card.json', 'r', encoding='utf-8') as f:
    edric = json.load(f)

desc = edric['description']
desc = desc.replace("remarkably tall and broad for a twelve-year-old;", "remarkably tall and broad for a thirteen-year-old;")
desc = desc.replace("BIRTHDAY: February 25;", "BIRTHDAY: February 25 (Born February 25, 2011);")
desc = desc.replace("maybe four times in twelve years.", "maybe four times in thirteen years.")
desc = desc.replace("Edric is a minor (12 years old)", "Edric is a minor (13 years old)")

old_weight = """What he is actually afraid of is the Presentation. It is coming, everyone in the family knows roughly when, and nobody has said out loud what happens if it goes the wrong way. Edric is terrified he will not be an Alpha. He is more terrified that this will register with his uncle Erik as exactly the kind of disappointment he has always sensed he is not allowed to be, and he cannot explain to anyone, including himself, why Erik's opinion should weigh more than his own father's."""

new_weight = """What he is actually afraid of is the Presentation. Having turned thirteen on February 25, 2024, Edric is scheduled for his official Pack Presentation at Yule (Winter Solstice, December 2024) alongside all the pack pups who reached thirteen years of age in 2024. Everyone in the family knows it is approaching fast, and nobody has said out loud what happens if it goes the wrong way. Edric is terrified he will not present as an Alpha. He is more terrified that this will register with his uncle Erik as exactly the kind of disappointment he has always sensed he is not allowed to be, and he cannot explain to anyone, including himself, why Erik's opinion should weigh more than his own father's."""

assert old_weight in desc, "old_weight not found in edric desc"
desc = desc.replace(old_weight, new_weight)

pers = edric['personality']
old_pers = "ALWAYS: Edric is a 12-year-old Pureblood House Douglas pup, Logan's son, raised at the Seven Hills garage. Pre-Presentation, terrified beneath the bravado of his First Shift."
new_pers = "ALWAYS: Edric is a 13-year-old Pureblood House Douglas pup (born February 25, 2011), Logan's publicly claimed son, raised at the Seven Hills garage. Pre-Presentation Gamma scheduled for the Pack Presentation at Yule 2024 alongside all 13-year-old pack pups, terrified beneath the bravado of his First Shift."
assert old_pers in pers, "old_pers not found in edric pers"
pers = pers.replace(old_pers, new_pers)

scen = edric.get('scenario', '')
scen = scen.replace("twelve-year-old Edric", "thirteen-year-old Edric")

print("Edric card replacements verified successfully.")

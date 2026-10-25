import json, glob

primary = json.load(open('FINAL/Svartulfr_NPC_Primary.json', encoding='utf-8'))
secondary = json.load(open('FINAL/Svartulfr_NPC_Secondary.json', encoding='utf-8'))

print("Primary NPC entries count:", len(primary.get('lexicon', [])))
print("Secondary NPC entries count:", len(secondary.get('lexicon', [])))

# Let's check card files in FINAL
cards = glob.glob('FINAL/*_card.json')
print("\nLocal card files in FINAL/:")
for c in cards:
    data = json.load(open(c, encoding='utf-8'))
    print(f"  {c}: id={data.get('id')} name={data.get('name')}")

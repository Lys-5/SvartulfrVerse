import json

data = json.load(open('FINAL/Svartulfr_Location.json', encoding='utf-8'))['lexicon']

e0 = data[0]
print("=== ENTRY 0: LOCATION SAMPLE ===")
print("Name:", e0.get('name'))
print("Type:", e0.get('type'))
print("Keys:", e0.get('keys'))
print("Content snippet (first 400 chars):")
print(e0.get('content', '')[:400])

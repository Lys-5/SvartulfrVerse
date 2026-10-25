import json

data = json.load(open('FINAL/Svartulfr_Master_Scenario.json', encoding='utf-8'))
for i, g in enumerate(data.get('greetings', [])):
    print(f"{i+1}. {g.get('name')}")

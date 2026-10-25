import json

path = 'FINAL/Svartulfr_Master_Scenario.json'
data = json.load(open(path, encoding='utf-8'))
old_str = '- {{user}} and {{scenarioChar "twin"}} are the 19-year-old Douglas-Bloodmoon twins (Alyssa Hvit, Dominant Omega Pre-Med Healer, and Jasper Svartr, Beta Technomancer & DJ Frequency), starting their freshman year at SUCC.'
new_str = '- {{user}} and {{scenarioChar "twin"}} are the 19-year-old Douglas-Bloodmoon twins: Alyssa Hvit (the White Moon, Dominant Omega Pre-Med Healer carrying her dimensional pochette) and Jasper Svartr (the Solar Shadow, Beta Tecnomancer, Cyber-Rogue & DJ Frequency), starting their freshman year at SUCC.'

if old_str in data['scenario']:
    data['scenario'] = data['scenario'].replace(old_str, new_str)
    json.dump(data, open(path, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
    print('Updated scenario prompt in FINAL/Svartulfr_Master_Scenario.json')
else:
    print('old_str not found!')

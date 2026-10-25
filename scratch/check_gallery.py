import json

for lb_path in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
    with open(lb_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print('===', lb_path, '===')
    for k in data.keys():
        if any(term in k.lower() for term in ['image', 'gallery', 'media', 'asset']):
            print('Key found:', k, type(data[k]))
            if isinstance(data[k], list) and len(data[k]) > 0:
                print('   first item:', data[k][0])

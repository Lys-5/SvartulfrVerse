import json

for cid in ['_93Rrpm1bDdytjzBqAp99P', '_nbEC7qk3NgU1LDfpQN9BW', '_9AycMJGa4fjy6pn6kgxGj']:
    with open(f'scratch/kakihara_{cid}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("="*60)
    print("CID:", cid)
    print("NAME:", data.get('name'))
    print("SCENARIO:\n", data.get('scenario'))
    print("FIRST_MES:\n", (data.get('first_mes') or '')[:1200].encode('ascii', errors='replace').decode('ascii'))

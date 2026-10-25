import json

def inspect_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("="*60)
    print(f"FILE: {fpath}")
    print(f"ID: {data.get('id')}")
    print(f"NAME: {data.get('name')}")
    print(f"TAGLINE: {data.get('tagline')}")
    print(f"FIRST_MES (length {len(data.get('first_mes') or '')}):")
    print((data.get('first_mes') or '')[:500])
    print("\nSCENARIO:")
    print((data.get('scenario') or '')[:600])
    greetings = data.get('greetings', [])
    print(f"\nGREETINGS COUNT: {len(greetings)}")
    for i, g in enumerate(greetings):
        gname = g.get('name') or g.get('title') or 'No title'
        print(f"  {i+1}. {gname} (text len {len(g.get('content') or g.get('text') or '')})")

inspect_file('scratch/kakihara__93Rrpm1bDdytjzBqAp99P.json')
inspect_file('scratch/kakihara__nbEC7qk3NgU1LDfpQN9BW.json')
inspect_file('scratch/kakihara__9AycMJGa4fjy6pn6kgxGj.json')
inspect_file('scratch/campmystic_full_card.json')

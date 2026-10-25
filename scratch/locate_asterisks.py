import json
import pathlib

for f in sorted(pathlib.Path('FINAL/scenarios').glob('*.json')):
    text = f.read_text(encoding='utf-8')
    data = json.loads(text)
    print(f"\n=== {f.name} ===")
    for k, v in data.items():
        if isinstance(v, str) and '*' in v:
            print(f"  Field '{k}' contains *:")
            for line in v.split('\n'):
                if '*' in line:
                    print(f"    {line}")
    for s in data.get('slots', []):
        for sk, sv in s.items():
            if isinstance(sv, str) and '*' in sv:
                print(f"  Slot '{s.get('key')}' field '{sk}' contains *: {sv}")
    for g_i, g in enumerate(data.get('greetings', [])):
        if '*' in g.get('name', ''):
            print(f"  Greeting {g_i} name contains *: {g.get('name')}")
        if '*' in g.get('description', ''):
            print(f"  Greeting {g_i} desc contains *: {g.get('description')}")
        for m_i, m in enumerate(g.get('messages', [])):
            if '*' in m.get('content', ''):
                print(f"  Greeting {g_i} msg {m_i} content contains *: {m.get('content')}")

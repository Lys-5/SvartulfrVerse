import json
import pathlib
import re

SC_DIR = pathlib.Path('FINAL/scenarios')

def inspect_all():
    files = sorted(SC_DIR.glob('*.json'))
    print(f"Total scenario files: {len(files)}")
    
    for f in files:
        print(f"\n==========================================")
        print(f"FILE: {f.name}")
        print(f"==========================================")
        data = json.loads(f.read_text(encoding='utf-8'))
        
        # Metadata
        print(f"Name: {data.get('name')}")
        print(f"Display description: {data.get('display_description')}")
        print(f"Visibility: {data.get('visibility')}")
        print(f"Rating: {data.get('rating')}")
        print(f"Lorebook IDs: {data.get('lorebook_ids')}")
        
        # Slots
        slots = data.get('slots', [])
        print(f"Slots ({len(slots)}):")
        for s in slots:
            pool_chars = [c.get('character_id') for c in s.get('pool', [])]
            print(f"  - Key: {s.get('key'):<25} Label: {s.get('label'):<35} unavail: {s.get('unavailable_count')} pool: {pool_chars}")
            
        # Startup script
        script = data.get('startup_script')
        if script:
            print(f"Startup Script present ({len(script)} chars)")
            print(f"Preview: {script[:150]}...")
        else:
            print("Startup Script: None")
            
        # Scenario text
        sc_text = data.get('scenario', '')
        print(f"Scenario Prompt length: {len(sc_text)} chars")
        
        # Greetings
        greetings = data.get('greetings', [])
        print(f"Greetings ({len(greetings)}):")
        for g_idx, g in enumerate(greetings):
            msgs = g.get('messages', [])
            print(f"  [{g_idx}] Name: {g.get('name')} | Speaker: {g.get('speaker_slot')} | Messages: {len(msgs)}")
            for m_idx, m in enumerate(msgs):
                c = m.get('content', '')
                print(f"      msg[{m_idx}] slot={m.get('speaker_slot')}: {c[:100]}...")

if __name__ == '__main__':
    inspect_all()

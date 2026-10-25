import json
import pathlib

SC_DIR = pathlib.Path('FINAL/scenarios')

def audit_full_parity_and_greetings():
    files = sorted(SC_DIR.glob('*.json'))
    for f in files:
        data = json.loads(f.read_text(encoding='utf-8'))
        print(f"\n==========================================")
        print(f"FILE: {f.name}")
        print(f"==========================================")
        slots = data.get('slots', [])
        slot_keys = {s['key'] for s in slots}
        greetings = data.get('greetings', [])
        
        for g_idx, g in enumerate(greetings):
            g_name = g.get('name')
            g_content = g.get('content')
            g_speaker = g.get('speaker_slot')
            messages = g.get('messages', [])
            
            # Check parity
            first_msg = messages[0] if messages else {}
            content_match = (g_content == first_msg.get('content'))
            speaker_match = (g_speaker == first_msg.get('speaker_slot'))
            
            print(f"Greeting [{g_idx}] '{g_name}' (messages: {len(messages)})")
            print(f"  Parity: content_match={content_match}, speaker_match={speaker_match}")
            if not content_match:
                print(f"  MISMATCH in greeting content!")
            if not speaker_match:
                print(f"  MISMATCH in greeting speaker_slot!")
                
            for m_idx, m in enumerate(messages):
                spk = m.get('speaker_slot')
                valid_spk = spk in slot_keys
                if not valid_spk:
                    print(f"  ERROR: msg[{m_idx}] speaker '{spk}' NOT IN SLOTS: {slot_keys}")
                # Check double quote balance
                c = m.get('content', '')
                q_count = c.count('"')
                if q_count % 2 != 0:
                    print(f"  ERROR: msg[{m_idx}] UNBALANCED DOUBLE QUOTES ({q_count}): {c}")

if __name__ == '__main__':
    audit_full_parity_and_greetings()

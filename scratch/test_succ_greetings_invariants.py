import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

def test_local_files():
    files = {
        'Alyssa': (ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Alyssa.json', 7, ['twin', 'childhood_friend', 'best_friend']),
        'Jasper': (ROOT / 'FINAL' / 'scenarios' / 'Svartulfr_Scenario_SUCC_Route_Jasper.json', 6, ['twin', 'childhood_friend', 'crush'])
    }
    
    for route_name, (path, expected_count, expected_slots) in files.items():
        print(f"\n--- Testing Local {route_name} Scenario ({path.name}) ---")
        assert path.exists(), f"File not found: {path}"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        greetings = data.get('greetings', [])
        assert len(greetings) == expected_count, f"Expected {expected_count} greetings, found {len(greetings)}"
        
        g0 = greetings[0]
        assert g0.get('name') == "SUCC Welcome Day", f"Greeting 0 name is '{g0.get('name')}', expected 'SUCC Welcome Day'"
        assert g0.get('speaker_slot') == expected_slots[0], f"Greeting 0 speaker_slot is '{g0.get('speaker_slot')}', expected '{expected_slots[0]}'"
        
        msgs = g0.get('messages', [])
        assert len(msgs) == 3, f"Expected 3 messages in greeting 0, found {len(msgs)}"
        
        actual_slots = [m.get('speaker_slot') for m in msgs]
        assert actual_slots == expected_slots, f"Expected slots {expected_slots}, got {actual_slots}"
        
        # Invariants:
        assert g0.get('speaker_slot') == msgs[0].get('speaker_slot'), "Invariant failed: greeting.speaker_slot != messages[0].speaker_slot"
        assert g0.get('content') == msgs[0].get('content'), "Invariant failed: greeting.content != messages[0].content"
        
        # Check mentions
        full_text = " ".join([m.get('content', '') for m in msgs]) + " " + g0.get('description', '')
        assert "August 26, 2024" in full_text, "Missing 'August 26, 2024'"
        assert "Lunar Quad" in full_text, "Missing 'Lunar Quad'"
        assert "Chancellor Archer Wolfwood" in full_text, "Missing 'Chancellor Archer Wolfwood'"
        assert "speech" in full_text.lower() or "address" in full_text.lower(), "Missing speech/address mention"
        assert "main stage" in full_text.lower() or "pavilion stage" in full_text.lower(), "Missing stage mention"
        
        # Check formatting discipline across all greetings
        for g_idx, g in enumerate(greetings):
            for m_idx, m in enumerate(g.get('messages', [])):
                content = m.get('content', '')
                assert '—' not in content, f"Em-dash found in greeting {g_idx} msg {m_idx}: {content}"
                assert '*' not in content, f"Asterisk found in greeting {g_idx} msg {m_idx}: {content}"
                # check quotes for dialogue if there is dialogue
                if '"' in content:
                    # check balanced quotes
                    quote_count = content.count('"')
                    assert quote_count % 2 == 0, f"Unbalanced quotes in greeting {g_idx} msg {m_idx} ({quote_count} quotes)"
        
        print(f"PASSED: {route_name} scenario meets all local invariant and formatting checks.")

if __name__ == "__main__":
    test_local_files()

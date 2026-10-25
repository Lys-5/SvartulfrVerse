import json
from pathlib import Path
import re

KNOWN_MIDDLE_NAMES = {
    # Primary
    "Dominic Rogers": ("Dominic", ["Wayne"], "Rogers"),
    "Roland Vickers": ("Roland", ["Mark"], "Vickers"),
    "Marcus Thornfield": ("Marcus", ["Iron"], "Thornfield"),
    "Kaladin Nargathon": ("Kaladin", ["Blackwolf"], "Nargathon"),
    "Iordan R. Vess": ("Iordan", ["R."], "Vess"),
    "Noah Loki Douglas Bloodmoon": ("Noah", ["Loki"], "Douglas Bloodmoon"),
    "Jasper Svartr Douglas Bloodmoon": ("Jasper", ["Svartr"], "Douglas Bloodmoon"),
    "Alyssa Hvit Douglas Bloodmoon": ("Alyssa", ["Hvit"], "Douglas Bloodmoon"),
    "Malachia Björn Douglas Bloodmoon": ("Malachia", ["Björn"], "Douglas Bloodmoon"),
    "Nixara Hvit Bloodmoon": ("Nixara", ["Hvit"], "Bloodmoon"),
    "Wulfnic Báleygr Bloodmoon": ("Wulfnic", ["Báleygr"], "Bloodmoon"),
    "Logan Járn Douglas": ("Logan", ["Járn"], "Douglas"),
    "Erik Ulfr Douglas": ("Erik", ["Ulfr"], "Douglas"),
    "Lord Cornelius Douglas": ("Cornelius", [], "Douglas"),
    "Magnus Douglas III": ("Magnus", [], "Douglas"),
    "Dr. Arthur Sinclair": ("Arthur", [], "Sinclair"),
    "Stanley Davies Sr.": ("Stanley", [], "Davies"),
    "Stanley Davies Jr.": ("Stanley", [], "Davies"),
    "Sullivan \"Sully\" Jones": ("Sullivan", [], "Jones"),
    "Federico \"Riki\" Savini": ("Federico", [], "Savini"),
    "Fade Greymoor": ("Mihaela", [], "Greymoor"),
    "Echo": ("Echo", [], ""),
    # Secondary
    "Alistair Ambrose DeVille": ("Alistair", ["Ambrose"], "DeVille"),
    "Campus Staff Rat": ("Campus", ["Staff"], "Rat"),
    "Luisa Sanchez Rogers": ("Luisa", [], "Sanchez-Rogers"),
    "Amerian de Vian": ("Amerian", ["de"], "Vian"),
    "Finn the Satyr": ("Finn", [], "the Satyr"),
    "Professor Marit Christiansen": ("Marit", [], "Christiansen"),
    "Professor Mollusk Moreau": ("Mollusk", [], "Moreau"),
    "Coach Mithers": ("Mithers", [], ""),
}

def test_name_parsing():
    for fn in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
        p = Path(r'e:\repository\SvartulfrVerse') / fn
        data = json.loads(p.read_text(encoding='utf-8'))
        print(f"\nTesting parsing in {fn}:")
        
        parsed_count = 0
        for idx, e in enumerate(data['lexicon']):
            name = e.get('name', '').strip()
            content = e.get('content', '')
            info = e.get('npc_info', {})
            
            # Check KNOWN_MIDDLE_NAMES first
            if name in KNOWN_MIDDLE_NAMES:
                fn_val, mn_val, ln_val = KNOWN_MIDDLE_NAMES[name]
            else:
                # Fallback: extract from existing npc_info or name
                fn_val = info.get('first_name') or name.split()[0]
                ln_val = info.get('last_name') or (name.split()[-1] if len(name.split()) > 1 else "")
                mn_val = info.get('middle_names', [])
                if not isinstance(mn_val, list):
                    mn_val = []
                    
            # Ensure valid types
            assert isinstance(fn_val, str) and fn_val.strip()
            assert isinstance(mn_val, list)
            assert isinstance(ln_val, str) or ln_val is None
            parsed_count += 1
            
        print(f"Successfully processed {parsed_count}/{len(data['lexicon'])} entries.")

if __name__ == '__main__':
    test_name_parsing()

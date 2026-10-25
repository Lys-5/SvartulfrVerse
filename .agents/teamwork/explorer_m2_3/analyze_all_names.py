import json
from pathlib import Path
import re

def analyze_all_names():
    for fn in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
        p = Path(r'e:\repository\SvartulfrVerse') / fn
        data = json.loads(p.read_text(encoding='utf-8'))
        print(f"\n==================== Analyzing Names in {fn} ====================")
        
        for idx, e in enumerate(data['lexicon']):
            name = e.get('name', '').strip()
            content = e.get('content', '')
            npc_info = e.get('npc_info', {})
            
            # Find [NAME: ...;
            m = re.search(r'\[NAME:\s*([^;\]]+)', content, re.IGNORECASE)
            jed_name = m.group(1).strip() if m else "NONE"
            
            # Check if there are middle names in current npc_info or in jed_name or in entry['name']
            # Look for 3+ words in jed_name or entry['name']
            clean_jed = re.sub(r'\(.*?\)', '', jed_name) # remove parens
            clean_jed = re.sub(r'".*?"', '', clean_jed) # remove quotes
            clean_jed = clean_jed.split(',')[0].strip() # remove commas
            
            tokens = clean_jed.split()
            # If tokens > 2, let's see how it's broken down
            if len(tokens) > 2 or jed_name == "NONE" or '(' in jed_name or '"' in jed_name:
                print(f"#{idx:3d} | entry: '{name}' | JED: '{jed_name}' | clean_tokens: {tokens}")

if __name__ == '__main__':
    analyze_all_names()

import json
from pathlib import Path
import re

def inspect_jed_names():
    for fn in ['FINAL/Svartulfr_NPC_Primary.json', 'FINAL/Svartulfr_NPC_Secondary.json']:
        p = Path(r'e:\repository\SvartulfrVerse') / fn
        data = json.loads(p.read_text(encoding='utf-8'))
        print(f"\n==================== {fn} ====================")
        
        name_tag_re = re.compile(r'\[NAME:\s*([^;\]]+)', re.IGNORECASE)
        
        sample_diffs = []
        no_name_tag = []
        multi_token_names = []
        
        for idx, e in enumerate(data['lexicon']):
            entry_name = e.get('name', '').strip()
            content = e.get('content', '')
            npc_info = e.get('npc_info', {})
            
            m = name_tag_re.search(content)
            if not m:
                no_name_tag.append((idx, entry_name))
                continue
                
            jed_name = m.group(1).strip()
            
            # Check if jed_name has parentheses or quotes or multiple words
            tokens = jed_name.split()
            if len(tokens) > 2:
                multi_token_names.append((idx, entry_name, jed_name, npc_info))
                
            if jed_name.lower() != entry_name.lower():
                sample_diffs.append((idx, entry_name, jed_name))
                
        print(f"Total entries: {len(data['lexicon'])}")
        print(f"Entries without [NAME: ...]: {len(no_name_tag)}")
        if no_name_tag:
            print("  Missing tag samples:", no_name_tag[:5])
        print(f"Entries with differing entry_name vs JED [NAME: ...]: {len(sample_diffs)}")
        if sample_diffs:
            for item in sample_diffs[:10]:
                print(f"  Diff #{item[0]}: entry_name='{item[1]}' vs jed='{item[2]}'")
        print(f"Entries with >2 tokens in JED name: {len(multi_token_names)}")
        if multi_token_names:
            for item in multi_token_names[:10]:
                print(f"  Multi #{item[0]}: jed='{item[2]}' | current npc_info={item[3]}")

if __name__ == '__main__':
    inspect_jed_names()

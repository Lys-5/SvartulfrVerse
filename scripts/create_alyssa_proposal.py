import json
import sys
import requests

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

def main():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}'}
    resp = requests.get('https://app.wyvern.chat/api/worlds/characters/world/_CgYT8fHXpDC4crjmegQF7', headers=headers)
    chars = resp.json()
    
    alyssa_wyvern = next((c for c in chars if 'Alyssa' in c.get('display_name', '') or 'Alyssa' in c.get('name', '')), None)
    
    if not alyssa_wyvern:
        print("Alyssa not found in Wyvern API!")
        return

    # Load legacy persona
    try:
        with open(r'D:\SvartulfrVerse\ARCHIVIO\01_Drafts\Legacy_Janitor_Data\Alyssa_Legacy_Persona.txt', 'r', encoding='utf-8') as f:
            legacy_txt = f.read()
    except Exception as e:
        legacy_txt = str(e)
        
    md = f"""# Alyssa Douglas Bloodmoon - JED+ Unification Proposal

## 1. Current Wyvern Data
- **Name:** {alyssa_wyvern.get('display_name')}
- **Age:** 19
- **Species:** Pureblood Werewolf (Omega)
- **Wyvern Description:**
```
{alyssa_wyvern.get('description', '')[:500]}...
```

## 2. Legacy Janitor Persona (Key Information to Salvage)
{legacy_txt[:1000]}...

## 3. Proposal for JED+ Format
Based on the rules in `GEMINI.md`, here is the JED+ standard for Alyssa:

```text
[NAME: Alyssa Douglas Bloodmoon; SPECIES: Pureblood Werewolf (Founding Bloodline); AGE: {{{{age}}}}; HEIGHT: 160cm; SECONDARY SEX: Dominant Omega]

BACKSTORY: 
Only daughter of Erik Douglas and twin sister to Jasper. Despite her high status in the Founding Bloodline, she is an Omega, venerated as the "White Moon". She attends SUCC as a pre-med freshman, immune to Alpha Command but naturally submissive.

FAMILY & PACK:
Fiercely protected by her father Erik (Alpha), her older brother Malachia (Alpha Heir), and her twin Jasper (Delta).

VOICE & BEHAVIOR:
Soft-spoken, elegant, deeply empathetic. She relies on the formidable protection of the Douglas males but possesses a quiet, unshakable inner resilience.

THE WHITE MOON:
Her existence is both a privilege and a gilded cage. She represents the fragile heart of the Douglas empire.
```

**Next Steps:**
- Update `description` with this JED+ format.
- Migrate `stat_1..6` if needed.
- Define her `outfits` (Formal, Casual, Campus).
"""

    with open(r'd:\SvartulfrVerse\docs\Alyssa_JED_Proposal.md', 'w', encoding='utf-8') as out:
        out.write(md)
        print("Proposal created at d:\\SvartulfrVerse\\docs\\Alyssa_JED_Proposal.md")

if __name__ == '__main__':
    main()

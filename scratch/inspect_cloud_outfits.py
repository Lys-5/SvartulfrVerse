import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL = ROOT / 'FINAL'
out = []

# 1. Wulfnic
w_live = json.loads((ROOT / 'scratch' / 'live_wulfnic.json').read_text(encoding='utf-8'))
w_loc = json.loads((FINAL / 'Wulfnic_Bloodmoon_card.json').read_text(encoding='utf-8'))
out.append(f"Wulfnic live outfits: {len(w_live.get('outfits', []))} vs local: {len(w_loc.get('outfits', []))}")
for o in w_live.get('outfits', []):
    if o.get('id') not in {x.get('id') for x in w_loc.get('outfits', [])}:
        out.append(f"  New in live Wulfnic: {json.dumps(o, ensure_ascii=False)}")

# 2. Malachia
m_live = json.loads((ROOT / 'scratch' / 'live_malachia.json').read_text(encoding='utf-8'))
m_loc = json.loads((FINAL / 'Malachia_Douglas_Bloodmoon_card.json').read_text(encoding='utf-8'))
out.append(f"Malachia live outfits: {len(m_live.get('outfits', []))} vs local: {len(m_loc.get('outfits', []))}")
for idx, (ol, olo) in enumerate(zip(m_live.get('outfits', []), m_loc.get('outfits', []))):
    if ol != olo:
        out.append(f"  Malachia outfit #{idx+1} diff: live image_url={ol.get('image_url') or ol.get('avatar')} vs local={olo.get('image_url') or olo.get('avatar')}")
        out.append(f"    Full live outfit #{idx+1}: {json.dumps(ol, ensure_ascii=False)}")

# 3. Alyssa Persona & Alyssa Card
ap_live = json.loads((ROOT / 'scratch' / 'live_alyssa_persona.json').read_text(encoding='utf-8'))
ap_loc = json.loads((FINAL / 'personas' / 'Alyssa_Persona.json').read_text(encoding='utf-8'))
ac_live = json.loads((ROOT / 'scratch' / 'live_alyssa_card.json').read_text(encoding='utf-8'))
ac_loc = json.loads((FINAL / 'Alyssa_Douglas_Bloodmoon_card.json').read_text(encoding='utf-8'))
out.append(f"Alyssa Persona live outfits: {len(ap_live.get('outfits', []))} vs local: {len(ap_loc.get('outfits', []))}")
for o in ap_live.get('outfits', []):
    if o.get('id') not in {x.get('id') for x in ap_loc.get('outfits', [])}:
        out.append(f"  New in live Alyssa Persona: {json.dumps(o, ensure_ascii=False)}")
out.append(f"Alyssa Card live outfits: {len(ac_live.get('outfits', []))} vs local: {len(ac_loc.get('outfits', []))}")

(ROOT / 'scratch' / 'cloud_outfits_diff.txt').write_text('\n'.join(out), encoding='utf-8')
print('\n'.join(out))

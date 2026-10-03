import json

p = json.load(open(r'C:\Users\mande\.gemini\antigravity\brain\0d89b0ab-f901-4d1c-afad-d3e640b70dd7\scratch\alyssa_persona_raw.json', encoding='utf-8'))
c = json.load(open('scratch/alyssa_world_card_live.json', encoding='utf-8'))

print("=== 1. BASIC FIELDS COMPARISON ===")
print(f"Persona Name:        {p.get('name')}")
print(f"Card Display Name:   {c.get('display_name')}")
print(f"Persona Avatar:      {p.get('avatar')}")
print(f"Card Avatar:         {c.get('avatar')}")
print(f"Persona Default Out: {p.get('default_outfit')}")
print(f"Card Default Out:    {c.get('default_outfit')}")

print("\n=== 2. DESCRIPTION COMPARISON ===")
p_desc = p.get('description', '')
c_long = c.get('long_summary', '')
c_summ = c.get('summary', '')

print(f"Persona Description len: {len(p_desc)}")
print(f"Card Long Summary len:   {len(c_long)}")
print(f"Card Summary len:        {len(c_summ)}")

# Save both texts for detailed diff
open('scratch/persona_desc.txt', 'w', encoding='utf-8').write(p_desc)
open('scratch/card_long_summary.txt', 'w', encoding='utf-8').write(c_long)

print("\n=== 3. OUTFITS COMPARISON ===")
p_outfits = {o['name'].lower(): o for o in p.get('outfits', [])}
c_outfits = {o['name'].lower(): o for o in c.get('outfits', [])}

print(f"Persona Outfits ({len(p_outfits)}): {list(p_outfits.keys())}")
print(f"Card Outfits    ({len(c_outfits)}): {list(c_outfits.keys())}")

missing_in_card = [k for k in p_outfits if k not in c_outfits]
missing_in_persona = [k for k in c_outfits if k not in p_outfits]
print(f"\nOutfits in Persona but NOT in Card: {missing_in_card}")
print(f"Outfits in Card but NOT in Persona: {missing_in_persona}")

print("\n--- Details of matching outfits ---")
for k in p_outfits:
    po = p_outfits[k]
    if k in c_outfits:
        co = c_outfits[k]
        p_desc_len = len(po.get('description', ''))
        c_desc_len = len(co.get('description', ''))
        same_desc = (po.get('description', '').strip() == co.get('description', '').strip())
        print(f"Outfit '{k}': same_desc={same_desc} (P len={p_desc_len}, C len={c_desc_len})")
        print(f"   P Avatar: {po.get('avatar')}")
        print(f"   C Avatar: {co.get('avatar')}")
    else:
        print(f"Outfit '{k}': NEW (only in Persona)")
        print(f"   P Avatar: {po.get('avatar')}")
        print(f"   P Desc:   {po.get('description')[:100]}...")

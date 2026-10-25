import os, json, glob

FALLBACK_AVATAR = 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/98e2d06d-a675-45e3-6096-cf976b547400/public'

print("================================================================================")
print("AUDIT ASSET VISIVI & IMMAGINI: CARDS, PERSONAS, SCENARIO, LOREBOOKS")
print("================================================================================\n")

print("--- 1. CHARACTER CARDS (14 Standalone in FINAL/) ---")
cards = sorted(glob.glob('FINAL/*_card.json'))
total_card_outfits = 0
card_outfits_with_img = 0
card_outfits_without_img = 0

cards_missing_avatar = []
cards_missing_banner = []
outfits_missing_by_card = {}

for cpath in cards:
    cname = os.path.basename(cpath)
    data = json.load(open(cpath, encoding='utf-8'))
    avatar = data.get('avatar') or data.get('avatar_url')
    banner = data.get('banner') or data.get('banner_url')
    outfits = data.get('outfits', [])
    
    if not avatar: cards_missing_avatar.append(cname)
    if not banner: cards_missing_banner.append(cname)
    
    outfits_with = [o for o in outfits if o.get('image_url') or o.get('image') or o.get('avatar')]
    outfits_without = [o for o in outfits if not (o.get('image_url') or o.get('image') or o.get('avatar'))]
    
    total_card_outfits += len(outfits)
    card_outfits_with_img += len(outfits_with)
    card_outfits_without_img += len(outfits_without)
    outfits_missing_by_card[cname] = (len(outfits), len(outfits_with), len(outfits_without))
    
    print(f"  {cname:<35} | Avatar: {'OK' if avatar else 'MANCANTE':<8} | Banner: {'OK' if banner else 'MANCANTE':<8} | Outfits: {len(outfits):2d} (con img: {len(outfits_with):2d}, mancanti: {len(outfits_without):2d})")

print(f"\nRiepilogo Cards:")
print(f"  - Avatar mancanti: {len(cards_missing_avatar)}")
print(f"  - Banner mancanti: {len(cards_missing_banner)}")
print(f"  - Outfits totali: {total_card_outfits} | Con immagine: {card_outfits_with_img} | Immagine mancante: {card_outfits_without_img}\n")

print("--- 2. USER PERSONAS (3 in FINAL/personas/) ---")
personas = sorted(glob.glob('FINAL/personas/*_Persona.json'))
total_persona_outfits = 0
persona_outfits_with_img = 0
persona_outfits_without_img = 0

for ppath in personas:
    pname = os.path.basename(ppath)
    data = json.load(open(ppath, encoding='utf-8'))
    avatar = data.get('avatar') or data.get('avatar_url')
    outfits = data.get('outfits', [])
    outfits_with = [o for o in outfits if o.get('image_url') or o.get('image') or o.get('avatar')]
    outfits_without = [o for o in outfits if not (o.get('image_url') or o.get('image') or o.get('avatar'))]
    total_persona_outfits += len(outfits)
    persona_outfits_with_img += len(outfits_with)
    persona_outfits_without_img += len(outfits_without)
    print(f"  {pname:<25} | Avatar: {'OK' if avatar else 'MANCANTE':<8} | Outfits: {len(outfits):2d} (con img: {len(outfits_with):2d}, mancanti: {len(outfits_without):2d})")

print(f"\nRiepilogo Personas:")
print(f"  - Outfits totali: {total_persona_outfits} | Con immagine: {persona_outfits_with_img} | Immagine mancante: {persona_outfits_without_img}\n")

print("--- 3. MASTER SCENARIO (FINAL/Svartulfr_Master_Scenario.json) ---")
scen_path = 'FINAL/Svartulfr_Master_Scenario.json'
if os.path.exists(scen_path):
    sdata = json.load(open(scen_path, encoding='utf-8'))
    s_avatar = sdata.get('avatar') or sdata.get('image_url') or sdata.get('avatar_url')
    s_banner = sdata.get('banner') or sdata.get('banner_url')
    greetings = sdata.get('greetings', [])
    greetings_with_img = [g for g in greetings if g.get('image_url') or g.get('avatar')]
    print(f"  Scenario Avatar: {'OK' if s_avatar else 'MANCANTE'}")
    print(f"  Scenario Banner: {'OK' if s_banner else 'MANCANTE'}")
    print(f"  Greetings con immagini custom allegate: {len(greetings_with_img)} / {len(greetings)}\n")

print("--- 4. LOREBOOKS STANDALONE (6 in FINAL/) ---")
lorebooks = sorted(glob.glob('FINAL/Svartulfr_*.json'))
for lbpath in lorebooks:
    lbname = os.path.basename(lbpath)
    if 'Scenario' in lbname: continue
    lbdata = json.load(open(lbpath, encoding='utf-8'))
    lexicon = lbdata.get('lexicon', [])
    
    custom_img = []
    fallback_img = []
    missing_img = []
    
    for e in lexicon:
        av = e.get('avatar') or e.get('image_url') or e.get('image') or ''
        ename = e.get('name', 'Unnamed')
        etype = e.get('type', 'untyped')
        if not av:
            missing_img.append((ename, etype))
        elif av == FALLBACK_AVATAR:
            fallback_img.append((ename, etype))
        else:
            custom_img.append((ename, etype))
            
    print(f"  {lbname:<30} (Totale {len(lexicon):3d} voci):")
    print(f"    - Con immagine custom:       {len(custom_img):3d}")
    print(f"    - Con Crest Fallback:        {len(fallback_img):3d}")
    print(f"    - Senza alcuna immagine:     {len(missing_img):3d}")

print("\n================================================================================")

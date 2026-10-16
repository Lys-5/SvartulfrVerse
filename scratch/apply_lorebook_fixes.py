import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'

print("=== 1. POPOLAMENTO ROGERS' BARGAIN MOTORS ===")
loc_path = FINAL_DIR / 'Svartulfr_Location.json'
loc_data = json.loads(loc_path.read_text(encoding='utf-8'))
loc_entries = loc_data.get('lexicon') or loc_data.get('entries') or []

rogers_entry = next((e for e in loc_entries if "Rogers' Bargain Motors" in e.get('name', '')), None)
if rogers_entry:
    rogers_content = (
        "[Rogers' Bargain Motors (Solarton Commercial Bypass / Industrial Lot): "
        "Sprawling used-car dealership and salvage repair yard situated along the industrial bypass on the outer perimeter of Solarton. "
        "The gravel lot is secured by high chain-link fencing topped with razor wire, crowded with rows of pre-owned pickup trucks, "
        "heavy-duty 4x4s, late-model muscle cars, salvaged roadsters, and dented domestic beaters. "
        "Business is run out of a weathered, double-wide sales trailer with faux-wood paneling, sun-bleached blinds, and a buzzing neon sign. "
        "The sales office smells permanently of stale filter coffee, cigar ash, motor oil, cheap spicy cologne, and infernal incubus musk. "
        "Owned and aggressively operated by Dominic Wayne Rogers (50-year-old incubus, estranged father of Bailey Rogers), "
        "who lords over human and supernatural clientele from behind a cluttered laminate desk stacked with vehicle titles and car keys. "
        "Notorious across Solarton for no-questions-asked cash sales, off-the-books trade-ins, and rugged unregistered vehicles favored by "
        "local pack enforcers, broke SUCC students, and hunters venturing into the rugged backroads of Hex Valley.]"
    )
    
    rogers_entry['content'] = rogers_content
    rogers_entry['enabled'] = True
    rogers_entry['avatar'] = "https://ella.janitorai.com/bot-avatars/E_9B3cNg0HvtyO93cASvZ.webp"
    rogers_entry['keys'] = [
        "Rogers' Bargain Motors",
        "Bargain Motors",
        "concessionaria Rogers",
        "used car lot",
        "Dominic Rogers lot",
        "Dominic's dealership"
    ]
    rogers_entry['secondary_keys'] = ["Solarton", "dealership", "cars", "Dominic"]
    rogers_entry['key_logic'] = "AND_ANY"
    print("Rogers' Bargain Motors popolato con successo.")

loc_data['entries'] = loc_entries
loc_data['lexicon'] = loc_entries
loc_path.write_text(json.dumps(loc_data, indent=2, ensure_ascii=False), encoding='utf-8')

print("\n=== 2. RIMOZIONE DUPLICATO NURSE ARIADNE DA LOREBOOK II ===")
lb2_path = FINAL_DIR / 'Svartulfr_Lorebook_II.json'
lb2_data = json.loads(lb2_path.read_text(encoding='utf-8'))
lb2_entries = lb2_data.get('lexicon') or lb2_data.get('entries') or []
orig_lb2_len = len(lb2_entries)
lb2_entries = [e for e in lb2_entries if 'Nurse Ariadne' not in e.get('name', '') and 'Ariadne Cirillo' not in e.get('name', '')]
print(f"Lorebook II: rimosso duplicato Ariadne ({orig_lb2_len} -> {len(lb2_entries)} voci)")
lb2_data['entries'] = lb2_entries
lb2_data['lexicon'] = lb2_entries
lb2_path.write_text(json.dumps(lb2_data, indent=2, ensure_ascii=False), encoding='utf-8')

print("\n=== 3. RIMOZIONE DUPLICATO SUGAR MOON JOB DA LOREBOOK I ===")
lb1_path = FINAL_DIR / 'Svartulfr_Lorebook_I.json'
lb1_data = json.loads(lb1_path.read_text(encoding='utf-8'))
lb1_entries = lb1_data.get('lexicon') or lb1_data.get('entries') or []
orig_lb1_len = len(lb1_entries)
seen_sugar = False
new_lb1 = []
for e in lb1_entries:
    if 'Sugar Moon: Baker Apprentice' in e.get('name', ''):
        if not seen_sugar:
            seen_sugar = True
            new_lb1.append(e) # keep first richer one
        else:
            print("Rimosso secondo duplicato Sugar Moon job")
    else:
        new_lb1.append(e)
lb1_entries = new_lb1
print(f"Lorebook I: ({orig_lb1_len} -> {len(lb1_entries)} voci)")
lb1_data['entries'] = lb1_entries
lb1_data['lexicon'] = lb1_entries
lb1_path.write_text(json.dumps(lb1_data, indent=2, ensure_ascii=False), encoding='utf-8')

print("\n=== 4. DEDUPLICAZIONE NPC PRIMARY E SECONDARY ===")
prim_path = FINAL_DIR / 'Svartulfr_NPC_Primary.json'
sec_path = FINAL_DIR / 'Svartulfr_NPC_Secondary.json'
prim_data = json.loads(prim_path.read_text(encoding='utf-8'))
sec_data = json.loads(sec_path.read_text(encoding='utf-8'))
prim_entries = prim_data.get('lexicon') or prim_data.get('entries') or []
sec_entries = sec_data.get('lexicon') or sec_data.get('entries') or []

# 7 SUCC secondary figures: remove from Primary, keep richer in Secondary
succ_dups = {'zaire ziisis', 'xaiden nershatar', 'lestat oreven', 'caien vaelion', 'aeril royen', 'ashton crowley', 'amerian de vian'}
orig_prim_len = len(prim_entries)
prim_entries = [e for e in prim_entries if e.get('name', '').strip().lower() not in succ_dups]
print(f"NPC Primary: rimossi {orig_prim_len - len(prim_entries)} personaggi SUCC secondari (ora gestiti esclusivamente in Secondary: {orig_prim_len} -> {len(prim_entries)})")

# 3 Ironhorn Nomads bikers (Goran, Kian, Radek): keep fuller in Primary alongside Marek, remove from Secondary
nomad_dups = {'goran', 'kian', 'radek'}
# First copy the richer text from Secondary to Primary for these 3 if longer
for pe in prim_entries:
    p_nl = pe.get('name', '').strip().lower()
    if p_nl in nomad_dups:
        se = next((e for e in sec_entries if e.get('name', '').strip().lower() == p_nl), None)
        if se and len(se.get('content', '')) > len(pe.get('content', '')):
            pe['content'] = se['content']
            print(f"Aggiornato testo di {pe.get('name')} in Primary con la versione estesa di Secondary")

orig_sec_len = len(sec_entries)
sec_entries = [e for e in sec_entries if e.get('name', '').strip().lower() not in nomad_dups]
print(f"NPC Secondary: rimossi i 3 biker Nomads ({orig_sec_len} -> {len(sec_entries)})")

prim_data['entries'] = prim_entries
prim_data['lexicon'] = prim_entries
prim_path.write_text(json.dumps(prim_data, indent=2, ensure_ascii=False), encoding='utf-8')

sec_data['entries'] = sec_entries
sec_data['lexicon'] = sec_entries
sec_path.write_text(json.dumps(sec_data, indent=2, ensure_ascii=False), encoding='utf-8')

print("\n=== TUTTE LE CORREZIONI APPLICATE CON SUCCESSO AI FILE LOCALI! ===")

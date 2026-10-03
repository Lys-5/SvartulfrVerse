import json

d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
chars = d.get('world_characters', [])

print(f"Total characters: {len(chars)}")

# Case 1: first_name contains space and last_name is empty
fn_with_space_no_ln = []
# Case 2: first_name is empty
no_fn = []
# Case 3: display_name differs from first_name + last_name
mismatches = []
# Case 4: characters with single name (mononym like "Zeera", "Radek", "Zero", "Dean")
mononyms = []

for c in chars:
    cid = c.get('id')
    dn = (c.get('display_name') or '').strip()
    fn = (c.get('first_name') or '').strip()
    ln = (c.get('last_name') or '').strip()
    
    if ' ' in fn and not ln:
        fn_with_space_no_ln.append((cid, dn, fn, ln))
    elif not fn:
        no_fn.append((cid, dn, fn, ln))
    elif not ln and ' ' not in dn:
        mononyms.append((cid, dn, fn))

print(f"\n[A] Characters with multiple words in first_name and EMPTY last_name: {len(fn_with_space_no_ln)}")
for cid, dn, fn, ln in fn_with_space_no_ln:
    print(f"  * [{cid}] Display: \"{dn}\" | First: \"{fn}\" | Last: \"{ln}\"")

print(f"\n[B] Characters with EMPTY first_name: {len(no_fn)}")
for cid, dn, fn, ln in no_fn:
    print(f"  * [{cid}] Display: \"{dn}\" | First: \"{fn}\" | Last: \"{ln}\"")

print(f"\n[C] Mononyms (Single names with intentionally empty last_name, e.g. Radek, Zero): {len(mononyms)}")
for cid, dn, fn in mononyms:
    print(f"  * [{cid}] \"{dn}\"")

import json

with open('exports/Svartulfr_Export.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

chars = {c.get('id'): c for c in data.get('world_characters', [])}

batch7_list = [
    ('_B9yX6RQDDBn9ftpDKcFQR', 'Gabriel'),
    ('_Hm6kdqEVhGhr2azCE8fFM', 'Everett Rottmore'),
    ('_yCF8zdAWQtQT488UKtJRR', 'Eric Grey'),
    ('_wQpJEH8Q96dkKXCfbFWgA', 'Emlyn Danes'),
    ('_CzjGd8k87dKNdFUgLNV8z', 'Emil'),
    ('_bdUxw6mQtJFRNtaK3tFkE', 'Damien Bishop'),
    ('_EFhQUz7zTT9ncLpxpp7TX', 'Dallas Rhodes'),
    ('_YckewRYA27qjRFrjGrQ87', 'Cyrus Camden'),
    ('_FjnaULjNgMhbct6pFXqPN', 'Charles DeVille'),
    ('_2LnhUCMUU2pWjLbCtdPbd', 'Caim Morningstar'),
    ('_wQmaCgpTUm7dGdq1crr28', 'August Reed'),
    ('_LxUWBR6UG1FX9gjXeY8Ky', 'Arturo Cardona'),
    ('_e6PtPLg6ENnVknQHpEmfK', 'Arran Parker'),
    ('_Hc6VKVCgW3xU9WEth88VA', 'Aris Thorne'),
    ('_6weeD6xTYcRQB9GJWGzVD', 'Amelia DeVille'),
    ('_GPn3mTr9FhL4W17dw4EFq', 'Alad C'),
    ('_fg7fY3dyNCnNzeT1GVYhP', 'Aiden Anderson')
]

for cid, name in batch7_list:
    c = chars.get(cid)
    if not c:
        print(f"NOT FOUND: {name} ({cid})")
        continue
    safe_name = name.replace(' ', '_').replace('-', '_')
    with open(f"scratch/batch7_{safe_name}.txt", 'w', encoding='utf-8') as out:
        out.write(f"NAME: {c.get('display_name')} (ID: {cid})\n")
        out.write(f"FIRST_NAME: {c.get('first_name')}\n")
        out.write(f"KEYS: {c.get('keys')}\n")
        out.write(f"SUMMARY:\n{c.get('summary')}\n\n")
        out.write(f"LONG SUMMARY:\n{c.get('long_summary')}\n")

print("Dumped all 17 batch 7 characters into scratch/")

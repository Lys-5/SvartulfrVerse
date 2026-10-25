import glob, re

for f in glob.glob('scratch/*.js'):
    content = open(f, encoding='utf-8', errors='ignore').read()
    if 'rpg_stats' in content or 'point_budget' in content:
        print(f"=== Found RPG in {f} ===")
        for kw in ['point_budget', 'auto_apply', 'show_party_stats']:
            idx = content.find(kw)
            if idx != -1:
                print(f"  [{kw}] at {idx}:")
                print("  ", content[max(0, idx-100):min(len(content), idx+200)].replace('\n', ' '))

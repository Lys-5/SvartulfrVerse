import json
import pathlib
import difflib

snap_dir = pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\backup_consolidated_snapshot')
pa = json.loads((snap_dir / 'persona_alyssa.json').read_text(encoding='utf-8'))
pe = json.loads((snap_dir / 'persona_echo.json').read_text(encoding='utf-8'))
plive = json.loads(pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\live_wyvern_snapshot_oct16\personas_live.json').read_text(encoding='utf-8'))

print('--- DIFF ALYSSA (snapshot vs live) ---')
for line in difflib.unified_diff(pa['description'].splitlines(), plive[0]['description'].splitlines(), lineterm=''):
    print(line)

print('--- DIFF ECHO (snapshot vs live) ---')
for line in difflib.unified_diff(pe['description'].splitlines(), plive[1]['description'].splitlines(), lineterm=''):
    print(line)

import json
import pathlib

snap_dir = pathlib.Path(r'e:\repository\SvartulfrVerse\scratch\backup_consolidated_snapshot')
mine = json.loads((snap_dir / 'mine_standalone_characters.json').read_text(encoding='utf-8'))
for c in mine:
    if c.get('name') in ['Zeera Darkfire', 'Jared Thompson', 'Mackenzie Sanchez-Rogers']:
        print('=== MINE:', c.get('name'), c.get('_id'))
        print(' keys:', list(c.keys()))
        print(' desc len:', len(c.get('description', '')), 'personality len:', len(c.get('personality', '')), 'outfits:', len(c.get('outfits', [])))

wc = json.loads((snap_dir / 'world_characters.json').read_text(encoding='utf-8'))
for v in wc:
    if v.get('id') in ['_DNaUEjdBpeYph6pMYAkrt', '_jeJTbxLcrYWXNWYPDx4ph', '_b7QqV43D8pU1tewx4qenY', '_EwPN1te7qtUKYEx4NLgag', '_MXcEC8Y6B3BNm3b1ttHj6']:
        print('=== WC:', v.get('display_name'), v.get('id'))
        print(' summary:', (v.get('summary') or '')[:120])
        print(' long_summary len:', len(v.get('long_summary') or ''))
        print(' outfits:', len(v.get('outfits', [])))

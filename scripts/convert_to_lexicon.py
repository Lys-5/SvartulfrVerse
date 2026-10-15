# -*- coding: utf-8 -*-
"""
Converte i lorebook di FINAL/ dal formato "entries" (SillyTavern) al formato
Lexicon: un oggetto lorebook con array `lexicon` (struttura nativa del sito/API).

Base per ogni entry: la corrispondente entry Lexicon nello snapshot del sito
(scratch/backup_consolidated_snapshot/lorebook_*.json), allineata per indice 1:1.
I campi mutabili (content, keys, enabled, ...) vengono riletti dal file FINAL,
che rappresenta lo stato post-ottimizzazione.

Le voci con type == "npc" vengono estratte dai Lorebook I/II/III e raccolte nel
nuovo Svartulfr_NPC_Secondary.json.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FINAL_DIR = os.path.join(ROOT, 'FINAL')
SNAP_DIR = os.path.join(ROOT, 'scratch', 'backup_consolidated_snapshot')

# FINAL file -> snapshot del sito
MAP = {
    'Svartulfr_Lorebook_I': 'lorebook_svartulfr_I',
    'Svartulfr_Lorebook_II': 'lorebook_svartulfr_II',
    'Svartulfr_Lorebook_III': 'lorebook_svartulfr_III',
    'Svartulfr_Location': 'lorebook_locations',
    'Svartulfr_NPC_Primary': 'lorebook_npc_primary',
}

# file da cui estrarre gli NPC (type == "npc")
NPC_SOURCES = ('Svartulfr_Lorebook_I', 'Svartulfr_Lorebook_II', 'Svartulfr_Lorebook_III')

POSITION_MAP = {0: 'before_char', 1: 'after_char', 2: 'before_an', 3: 'after_an', 4: 'at_depth'}
LOGIC_MAP = {0: 'AND_ANY', 1: 'NOT_ALL', 2: 'NOT_ANY', 3: 'AND_ALL'}


def load_entries_ordered(path):
    """Ritorna le entry di un file FINAL ordinate per uid numerico."""
    with open(path, encoding='utf-8') as fh:
        entries = json.load(fh)['entries']
    return [entries[u] for u in sorted(entries, key=lambda x: int(x))]


def derive_npc_info(name):
    parts = [p for p in re.split(r'\s+', (name or '').strip()) if p]
    if not parts:
        return {"first_name": "", "middle_names": [], "last_name": "", "nicknames": [], "titles": []}
    return {
        "first_name": parts[0],
        "middle_names": parts[1:-1],
        "last_name": parts[-1] if len(parts) > 1 else "",
        "nicknames": [],
        "titles": [],
    }


def to_lexicon(fin, snap, fallback_type):
    ext = fin.get('extensions') or {}
    wv = ext.get('wyvern') or {}

    io = wv.get('insertion_order')
    if io is None:
        io = fin.get('order', 0) or 0
    pr = wv.get('priority')
    if pr is None:
        pr = (snap or {}).get('priority', 0)
    position = wv.get('position') or POSITION_MAP.get(fin.get('position'), 'before_char')

    entry = {
        "entry_id": (snap or {}).get('entry_id') or '',
        "keys": fin.get('key') or [],
        "regex_patterns": wv.get('regex_patterns') or [],
        "content": fin.get('content') or '',
        # tutto tranne il blocco "wyvern" (promosso a campi top-level)
        "extensions": {k: v for k, v in ext.items() if k != 'wyvern'},
        "enabled": not bool(fin.get('disable')),
        "case_sensitive": bool(fin.get('caseSensitive')),
        "insertion_order": io,
        "name": fin.get('comment') or (snap or {}).get('name') or '',
        "priority": pr,
        "comment": "",
        "secondary_keys": fin.get('keysecondary') or [],
        "constant": bool(fin.get('constant')),
        "position": position,
        "scan_persona": bool(fin.get('matchPersonaDescription')),
        "whole_words_only": bool(fin.get('matchWholeWords')),
        "key_logic": LOGIC_MAP.get(fin.get('selectiveLogic', 0), 'AND_ANY'),
        "delay": fin.get('delay', 0) or 0,
        "sticky": fin.get('sticky', 0) or 0,
        "cooldown": fin.get('cooldown', 0) or 0,
        "activation_chance": fin.get('probability', 100),
        "labels": (snap or {}).get('labels') or [],
        "custom_fields": (snap or {}).get('custom_fields') or {},
        "related_entries": (snap or {}).get('related_entries') or [],
        "avatar": (snap or {}).get('avatar') or "",
        "avatar_activation_regex": (snap or {}).get('avatar_activation_regex') or "",
        "type": (snap or {}).get('type') or fallback_type,
        "callback": (snap or {}).get('callback') or "",
    }
    if entry['type'] == 'npc':
        entry['npc_info'] = (snap or {}).get('npc_info') or derive_npc_info(entry['name'])
    entry['provenance'] = wv.get('provenance') or (snap or {}).get('provenance')
    return entry


def convert_file(fname, snapname, drop_npc):
    fin_list = load_entries_ordered(os.path.join(FINAL_DIR, fname + '.json'))
    with open(os.path.join(SNAP_DIR, snapname + '.json'), encoding='utf-8') as fh:
        snapd = json.load(fh)
    snaps = snapd['lexicon']

    assert len(fin_list) == len(snaps), f'{fname}: {len(fin_list)} entries vs {len(snaps)} snapshot'

    fallback_type = 'location' if fname == 'Svartulfr_Location' else 'lore/concept'
    converted, npcs = [], []
    for fin, snap in zip(fin_list, snaps):
        entry = to_lexicon(fin, snap, fallback_type)
        if drop_npc and entry['type'] == 'npc':
            npcs.append(entry)
        else:
            converted.append(entry)

    obj = {
        "name": snapd.get('name'),
        "description": snapd.get('description') or "",
        "scan_depth": snapd.get('scan_depth', 5),
        "token_budget": snapd.get('token_budget', 5000),
        "recursive_scanning": snapd.get('recursive_scanning', True),
        "lexicon": converted,
    }
    return obj, npcs


def write_json(path, obj):
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
        fh.write('\n')


def main():
    all_npcs = []
    for fname, snapname in MAP.items():
        drop = fname in NPC_SOURCES
        obj, npcs = convert_file(fname, snapname, drop_npc=drop)
        all_npcs.extend(npcs)
        write_json(os.path.join(FINAL_DIR, fname + '.json'), obj)
        print(f'{fname}: lexicon={len(obj["lexicon"])}  NPC estratti={len(npcs)}')

    secondary = {
        "name": "Svartúlfr - NPC Secondary",
        "description": "",
        "scan_depth": 5,
        "token_budget": 5000,
        "recursive_scanning": True,
        "lexicon": all_npcs,
    }
    write_json(os.path.join(FINAL_DIR, 'Svartulfr_NPC_Secondary.json'), secondary)
    print(f'Svartulfr_NPC_Secondary: lexicon={len(all_npcs)}')


if __name__ == '__main__':
    main()

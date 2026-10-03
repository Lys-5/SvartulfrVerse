import os
import sys
import json
import re
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'


def get_headers(token):
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }


def get_char(token, cid):
    url = f"{API_BASE}/characters/{cid}?world_id={WORLD_ID}"
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))


def put_char(token, cid, body):
    url = f"{API_BASE}/characters/{cid}?world_id={WORLD_ID}"
    data = json.dumps(body).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=get_headers(token), method='PUT')
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))


def parse_name(dn, fn, ln):
    raw = fn if fn else dn
    titles = []
    nicknames = []

    if raw.startswith("Lord "):
        titles.append("Lord")
        raw = raw[5:].strip()
    elif raw.startswith("Dr. "):
        titles.append("Dr.")
        raw = raw[4:].strip()
    elif raw.startswith("Professor "):
        titles.append("Professor")
        raw = raw[10:].strip()
    elif raw.startswith("Coach "):
        titles.append("Coach")
        raw = raw[6:].strip()
    elif re.match(r'^(GREED|GLUTTONY|ENVY|WRATH|PRIDE|LUST|SLOTH)\s*-\s*', raw):
        m = re.match(r'^(GREED|GLUTTONY|ENVY|WRATH|PRIDE|LUST|SLOTH)\s*-\s*(.*)', raw)
        titles.append(m.group(1))
        raw = m.group(2).strip()

    quote_match = re.search(r'["\']([^"\']+)["\']', raw)
    if quote_match:
        nicknames.append(quote_match.group(1))
        raw = re.sub(r'\s*["\'][^"\']+["\']\s*', ' ', raw).strip()

    parts = raw.split()
    if len(parts) == 0:
        return fn, ln, titles, nicknames
    elif len(parts) == 1:
        new_fn = parts[0]
        new_ln = ""
    elif len(parts) == 2:
        new_fn = parts[0]
        new_ln = parts[1]
    elif len(parts) == 3:
        if parts[2] in ('Jr.', 'Sr.', 'III', 'IV', 'II'):
            new_fn = parts[0]
            new_ln = f"{parts[1]} {parts[2]}"
        elif parts[1] in ('Sanchez', 'van', 'de', 'von', 'la', 'del', 'da'):
            new_fn = parts[0]
            new_ln = f"{parts[1]} {parts[2]}"
        elif len(parts[1]) == 2 and parts[1].endswith('.'):
            new_fn = f"{parts[0]} {parts[1]}"
            new_ln = parts[2]
        else:
            new_fn = parts[0]
            new_ln = f"{parts[1]} {parts[2]}"
    else:
        new_fn = parts[0]
        new_ln = " ".join(parts[1:])

    return new_fn, new_ln, titles, nicknames


def run():
    token = get_auth_token()
    print("Token ottenuto.\n")

    # =========================================================================
    # 1. ASSEGNAZIONE COGNOME DARKFIRE AI 4 FRATELLI VAX
    # =========================================================================
    print("=== 1. ASSEGNAZIONE COGNOME DARKFIRE ===")
    darkfire_brothers = [
        ('_a6KYGdN3BWTgbYEbT4mx8', 'Zeera', 'CEO di HSK Consulting, Rappresentante Demoniaco'),
        ('_8catGJE98MTpfaajJD9zV', 'Aras', 'Direttore Risorse Umane di HSK Consulting'),
        ('_Agf7FxKMzPDFJj3gktYtz', 'Karshin', 'Capo Sicurezza di HSK Consulting'),
        ('_aaWfLtx19WQR7JyHKDBem', 'Boros', 'Direttore Logistica di HSK Consulting')
    ]

    for cid, first_name, role in darkfire_brothers:
        char = get_char(token, cid)
        curr_keys = char.get('keys', [])
        new_display = f"{first_name} Darkfire"
        
        # Add full name and alias to keys if not present
        if new_display not in curr_keys:
            curr_keys.insert(0, new_display)
        if first_name not in curr_keys:
            curr_keys.append(first_name)

        summary = char.get('summary', '')
        summary = summary.replace(f"NAME: {first_name};", f"NAME: {new_display};")

        long_summary = char.get('long_summary', '')
        long_summary = long_summary.replace(f"NAME: {first_name};", f"NAME: {new_display};")

        payload = {
            "display_name": new_display,
            "first_name": first_name,
            "last_name": "Darkfire",
            "keys": curr_keys,
            "summary": summary,
            "long_summary": long_summary
        }
        res = put_char(token, cid, payload)
        print(f"  [OK] {new_display} aggiornato ({cid})")

    # =========================================================================
    # 2. RISOLUZIONE SPLIT NOME E COGNOME SU TUTTI I PERSONAGGI (70 TARGET)
    # =========================================================================
    print("\n=== 2. RISOLUZIONE SPLIT FIRST_NAME / LAST_NAME ===")
    d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
    chars = d.get('world_characters', [])

    fixed_count = 0
    for c in chars:
        cid = c['id']
        # Skip Darkfire brothers as they are already handled
        if cid in [x[0] for x in darkfire_brothers] or cid == '_bh8AHn7WKkNTnLjwXrUWE':
            continue

        dn = (c.get('display_name') or '').strip()
        fn = (c.get('first_name') or '').strip()
        ln = (c.get('last_name') or '').strip()

        if (' ' in fn and not ln) or (not fn and dn):
            new_fn, new_ln, add_titles, add_nicks = parse_name(dn, fn, ln)
            
            # Fetch live character
            live_char = get_char(token, cid)
            live_titles = live_char.get('titles', []) or []
            live_nicks = live_char.get('nicknames', []) or []

            for t in add_titles:
                if t not in live_titles:
                    live_titles.append(t)
            for n in add_nicks:
                if n not in live_nicks:
                    live_nicks.append(n)

            update_payload = {
                "first_name": new_fn,
                "last_name": new_ln,
                "titles": live_titles,
                "nicknames": live_nicks
            }
            try:
                put_char(token, cid, update_payload)
                fixed_count += 1
                print(f"  [{fixed_count}] {dn} ({cid}) -> First: \"{new_fn}\" | Last: \"{new_ln}\"")
            except Exception as e:
                print(f"  [ERRORE] {dn} ({cid}): {e}")

    print(f"\nOperazione completata. Totale personaggi sistemati: {fixed_count}")


if __name__ == '__main__':
    run()

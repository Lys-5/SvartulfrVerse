import sys, json, requests, time, os
sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API = 'https://app.wyvern.chat/api'
token = get_auth_token()
H = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
SNAP_DIR = r'd:\SvartulfrVerse\docs\snapshots_2026-10-03'
os.makedirs(SNAP_DIR, exist_ok=True)

def clean(t):
    return t.replace(' \u2014 ', ', ').replace('\u2014', ', ')

log = []

# ---------- A: long_summary for 17 new characters ----------
ids = {
    "Rozalia Tănase": "_LnfCwm3DcD2TCTX4HRPXN", "Ruby Valerius": "_Gk2tkQKwkBJcxyxBp8rUh",
    "Vesna": "_33d2LUW4RpkTJ6aedwwhc", "Mikan": "_zGyw9wVqhMwNGPHPwWWnW", "Ginger": "_fWWTLEmXgHHcxYEzREXkt",
    "Orion and Sigrid Valois": "_3MU14K2y6rjQKHRyw7J6J", "Henrey Cote": "_1qQm9jKyAcPV18YqT893F",
    "Aria Xenthon": "_d1R1FMQBekE272Eqjbx3j", "Tori": "_P21wbKew3dR23fJmLQUC2", "River": "_VhxtUTGPjdEzFwRXVjN8V",
    "Ailsa Hourie": "_1wL6W2Ff2BNdeLHGQRnFM", "Silas": "_QMqFUAe1cj6Mfdp7CWcA8",
    "Bramble Mossmere": "_wckBg4xaGrHTB4E2hPMTT", "Evan": "_mW13tK1KEmVbG63zUCwJ4",
    "Vespera Thorne": "_2hPrP1ak69RA8frDTamz7", "Eira Elloway": "_xdGMDeNKBnhjYn1qdtfd7",
    "Darius Azadi": "_N4ccU2VQ4Wbwn1RX9QdQL",
}
texts = {}
for fn in ('GroupA_JED.json', 'GroupB_JED.json'):
    with open(rf'd:\SvartulfrVerse\docs\{fn}', 'r', encoding='utf-8-sig') as f:
        texts.update(json.load(f))

print('=== A: long_summary ===')
for name, cid in ids.items():
    if name not in texts:
        print(f'{name}: NO SOURCE TEXT'); continue
    body = clean(texts[name])
    r = requests.put(f'{API}/worlds/characters/{cid}', headers=H, json={'long_summary': body})
    time.sleep(0.5)
    d = requests.get(f'{API}/worlds/characters/{cid}', headers=H).json()
    got = d.get('long_summary') or ''
    ok = got == body
    print(f'{name}: PUT {r.status_code}, verified={ok}, len={len(got)}, emdash={"\u2014" in got}')

# ---------- B prep: snapshot duplicates ----------
print('=== B: snapshot duplicates ===')
dups = {"Varg": "_8DMM7UQ2qm2EEwP1z7TNt", "Aras": "_ac9DtHN4bqbp2P8gyG7cq",
        "Karshin": "_Rea4LDWJx8mfpC38rLWyR", "Boros": "_jJjhg6JPwjeFQqfpnMYnb"}
for n, cid in dups.items():
    d = requests.get(f'{API}/worlds/characters/{cid}', headers=H).json()
    p = os.path.join(SNAP_DIR, f'DUP_{n}_{cid}.json')
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f'{n}: snapshot saved ({len(json.dumps(d))} bytes), long_summary={len(d.get("long_summary") or "")}')

# ---------- C: Monster lexicon ----------
print('=== C: Monster lexicon ===')
lex = requests.get(f'{API}/worlds/lexicon/world/{WORLD_ID}', headers=H).json()
if isinstance(lex, dict):
    lex = lex.get('data') or lex.get('entries') or []
existing = {e.get('name') for e in lex}
with open(r'd:\SvartulfrVerse\docs\Monster_Lexicon.json', 'r', encoding='utf-8-sig') as f:
    monsters = json.load(f)
for e in monsters:
    if e['name'] in existing:
        print(f"{e['name']}: already exists, skipped"); continue
    e = {k: v for k, v in e.items() if k != 'category'}
    e['content'] = clean(e['content'])
    e['is_global'] = False
    e['world_id'] = WORLD_ID
    r = requests.post(f'{API}/worlds/lexicon', headers=H, json=e)
    print(f"{e['name']}: POST {r.status_code}")
    time.sleep(0.5)

# ---------- D: em-dash in existing lexicon ----------
print('=== D: em-dash fix in lexicon ===')
lex = requests.get(f'{API}/worlds/lexicon/world/{WORLD_ID}', headers=H).json()
if isinstance(lex, dict):
    lex = lex.get('data') or lex.get('entries') or []
for e in lex:
    nm = e.get('name') or ''
    if not nm.startswith(('Kink:', 'Magic:', 'Species:')):
        continue
    c = e.get('content') or ''
    if '\u2014' in c or '**' in c:
        with open(os.path.join(SNAP_DIR, f"LEX_{e['id']}.json"), 'w', encoding='utf-8') as f:
            json.dump(e, f, ensure_ascii=False, indent=2)
        new = clean(c).replace('**', '')
        r = requests.put(f"{API}/worlds/lexicon/{e['id']}", headers=H, json={'content': new})
        print(f'{nm}: PUT {r.status_code}')

# final verification of lexicon
lex = requests.get(f'{API}/worlds/lexicon/world/{WORLD_ID}', headers=H).json()
if isinstance(lex, dict):
    lex = lex.get('data') or lex.get('entries') or []
mine = [e for e in lex if (e.get('name') or '').startswith(('Kink:', 'Magic:', 'Species:'))]
bad = [e['name'] for e in mine if '\u2014' in (e.get('content') or '')]
print(f'VERIFY lexicon: total={len(mine)}, '
      f'kink={sum(1 for e in mine if e["name"].startswith("Kink:"))}, '
      f'magic={sum(1 for e in mine if e["name"].startswith("Magic:"))}, '
      f'species={sum(1 for e in mine if e["name"].startswith("Species:"))}, '
      f'still_with_emdash={bad}, non_global={all(e.get("is_global") is False for e in mine)}')

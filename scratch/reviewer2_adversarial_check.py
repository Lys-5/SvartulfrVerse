import json
import requests
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

# Load the audit results
audit_results = json.loads((ROOT / "scratch" / "reviewer2_audit_results.json").read_text(encoding='utf-8'))

# Let's inspect local and live data for adversarial edge cases
token = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/json'
}

adversarial_findings = []

for sc_name, sc_data in audit_results["scenarios"].items():
    sc_id = sc_data["id"]
    resp = requests.get(f"https://app.wyvern.chat/api/character-scenarios/{sc_id}", headers=headers)
    live = resp.json()

    # 1. Check for em-dashes in greetings
    greetings = live.get("greetings", [])
    for idx, g in enumerate(greetings):
        msg = g.get("message", "")
        name = g.get("name", "")
        if "—" in msg:
            adversarial_findings.append(f"{sc_name} greeting {idx} ('{name}') contains em-dash '—'!")
        if "—" in name:
            adversarial_findings.append(f"{sc_name} greeting {idx} name ('{name}') contains em-dash '—'!")

    # 2. Check for empty pools in slots
    slots = live.get("slots", [])
    for s_idx, s in enumerate(slots):
        pool = s.get("pool", [])
        key = s.get("key", "")
        if not pool or len(pool) == 0:
            adversarial_findings.append(f"{sc_name} slot {s_idx} ('{key}') has empty pool!")
        if s.get("unavailable_count") != 0:
            adversarial_findings.append(f"{sc_name} slot {s_idx} ('{key}') unavailable_count != 0 ({s.get('unavailable_count')})")

    # 3. Check for any None / null values in essential fields
    for field in ["id", "name", "visibility", "revision", "lorebook_ids", "slots", "greetings"]:
        if live.get(field) is None:
            adversarial_findings.append(f"{sc_name} missing essential field '{field}' in live API response!")

print("Adversarial Findings Count:", len(adversarial_findings))
for f in adversarial_findings:
    print(" -", f)

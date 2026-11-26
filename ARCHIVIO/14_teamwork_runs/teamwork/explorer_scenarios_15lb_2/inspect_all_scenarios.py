import json
import urllib.request
import urllib.error
import pathlib
import time

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
token = WT_PATH.read_text(encoding='utf-8').strip()

SCENARIOS = {
    "Master Scenario": "char_scenario_1DC43ggb6mB8YLJDJKrU4",
    "Camp Mystic": "char_scenario_nLC84wrHdrbB6P3DEhwKb",
    "SUCC Route Alyssa": "char_scenario_CKgwq246DyCj1NNTBV9rt",
    "SUCC Route Jasper": "char_scenario_Kq4mJEBH83j7Q7DdVfFnF",
    "Villa Douglas": "char_scenario_88N1eQXqkbydKX9q9XQzp",
    "DMHA Dungeons": "char_scenario_eqtRNnDpKbxDp7dmJmq6E",
    "Underworld Sindacato": "char_scenario_rrUCdBPH6WTNyBnQkMAKR"
}

headers = {
    'Authorization': f'Bearer {token}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/json'
}

results = {}

for name, sc_id in SCENARIOS.items():
    url = f'https://app.wyvern.chat/api/character-scenarios/{sc_id}'
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            greetings = data.get('greetings', [])
            greeting_samples = []
            for idx, g in enumerate(greetings):
                greeting_samples.append({
                    "index": idx,
                    "keys": list(g.keys()),
                    "has_linked_persona_ids": "linked_persona_ids" in g,
                    "linked_persona_ids": g.get("linked_persona_ids"),
                    "title": g.get("title", ""),
                    "first_msg_preview": g.get("messages", [{}])[0].get("content", "")[:60] if g.get("messages") else ""
                })
            results[name] = {
                "id": sc_id,
                "name": data.get("name"),
                "revision": data.get("revision"),
                "visibility": data.get("visibility"),
                "rating": data.get("rating"),
                "status": data.get("status"),
                "lorebook_ids_count": len(data.get("lorebook_ids", [])),
                "lorebook_ids": data.get("lorebook_ids", []),
                "slot_count": len(data.get("slots", [])),
                "greeting_count": len(greetings),
                "greetings_summary": greeting_samples,
                "top_level_keys": list(data.keys())
            }
            print(f"SUCCESS: {name} ({sc_id}) -> revision: {data.get('revision')}, lorebooks: {len(data.get('lorebook_ids', []))}, greetings: {len(greetings)}")
    except urllib.error.HTTPError as e:
        results[name] = {"id": sc_id, "error": f"HTTP {e.code} {e.reason}"}
        print(f"ERROR: {name} ({sc_id}) -> HTTP {e.code} {e.reason}")
    except Exception as e:
        results[name] = {"id": sc_id, "error": str(e)}
        print(f"ERROR: {name} ({sc_id}) -> {e}")
    time.sleep(0.5)

out_file = pathlib.Path(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_2\live_scenarios_inspection.json')
out_file.write_text(json.dumps(results, indent=2), encoding='utf-8')
print("Detailed results written to", out_file)

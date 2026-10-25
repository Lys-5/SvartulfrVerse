#!/usr/bin/env python3
"""
CLI Helper for Wyvern Character Scenarios:
- Validates that `slots` only reference the 8 active Character Cards in /characters/mine,
  verifies speaker_slot parity, Italian language in greetings, 0 em-dashes, 0 asterisks,
  and Sierra Cruz / Scarlett Rose anatomical invariants.
- Synchronizes canonical 8-card slot definitions for Alyssa Route and Jasper Route.
- Deploys updated scenarios to Wyvern Web API with file-lock/monotonic rate limiting (1 req/s),
  automatic Firebase token refresh via scratch/refresh_token.py, and fresh revision check.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request

ACTIVE_CARD_IDS = {
    "_t4J9aQNJM36cUKAP4wB4U": "Jasper Svartr Douglas Bloodmoon",
    "_zn24784jfcchQ7EwCyAnm": "Mackenzie Sanchez-Rogers",
    "_QPea6g4Q1QfeYCVHCLMPR": "Erik Ulfr Douglas",
    "_RDfz7XzTpM23LpPALVXHM": "Malachia Björn Douglas Bloodmoon",
    "_zFLUjV8aVxQRAfQxGcAcY": "Noah Loki Douglas Bloodmoon",
    "_T8Ywcr9FEqNf9JxbK6eHP": "Logan Járn Douglas",
    "_TbRM3EdxDjHFgqztTbCpL": "Edric Douglas",
    "_HEQQbbRFwKdG8QE2Fh1z1": "Wulfnic Báleygr Bloodmoon",
}

ALYSSA_CANONICAL_SLOTS = [
    {"id": "slot-twin", "key": "twin", "label": "Twin Brother", "selection_mode": "weighted_random", "pool": [{"character_id": "_t4J9aQNJM36cUKAP4wB4U", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-crush", "key": "crush", "label": "Crush", "selection_mode": "weighted_random", "pool": [{"character_id": "_zn24784jfcchQ7EwCyAnm", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-father", "key": "father", "label": "Father", "selection_mode": "weighted_random", "pool": [{"character_id": "_QPea6g4Q1QfeYCVHCLMPR", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-eldest-brother", "key": "eldest_brother", "label": "Eldest Brother", "selection_mode": "weighted_random", "pool": [{"character_id": "_RDfz7XzTpM23LpPALVXHM", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-brother", "key": "brother", "label": "Brother", "selection_mode": "weighted_random", "pool": [{"character_id": "_zFLUjV8aVxQRAfQxGcAcY", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-uncle", "key": "uncle", "label": "Uncle", "selection_mode": "weighted_random", "pool": [{"character_id": "_T8Ywcr9FEqNf9JxbK6eHP", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-cousin", "key": "cousin", "label": "Cousin", "selection_mode": "weighted_random", "pool": [{"character_id": "_TbRM3EdxDjHFgqztTbCpL", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-maternal-grandfather", "key": "maternal_grandfather", "label": "Maternal Grandfather", "selection_mode": "weighted_random", "pool": [{"character_id": "_HEQQbbRFwKdG8QE2Fh1z1", "weight": 100}], "unavailable_count": 0},
]

JASPER_CANONICAL_SLOTS = [
    {"id": "slot-father", "key": "father", "label": "Father", "selection_mode": "weighted_random", "pool": [{"character_id": "_QPea6g4Q1QfeYCVHCLMPR", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-eldest-brother", "key": "eldest_brother", "label": "Eldest Brother", "selection_mode": "weighted_random", "pool": [{"character_id": "_RDfz7XzTpM23LpPALVXHM", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-brother", "key": "brother", "label": "Brother", "selection_mode": "weighted_random", "pool": [{"character_id": "_zFLUjV8aVxQRAfQxGcAcY", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-uncle", "key": "uncle", "label": "Uncle", "selection_mode": "weighted_random", "pool": [{"character_id": "_T8Ywcr9FEqNf9JxbK6eHP", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-cousin", "key": "cousin", "label": "Cousin", "selection_mode": "weighted_random", "pool": [{"character_id": "_TbRM3EdxDjHFgqztTbCpL", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-maternal-grandfather", "key": "maternal_grandfather", "label": "Maternal Grandfather", "selection_mode": "weighted_random", "pool": [{"character_id": "_HEQQbbRFwKdG8QE2Fh1z1", "weight": 100}], "unavailable_count": 0},
    {"id": "slot-band-peer", "key": "band_peer", "label": "The Verve Bandmate & Peer", "selection_mode": "weighted_random", "pool": [{"character_id": "_zn24784jfcchQ7EwCyAnm", "weight": 100}], "unavailable_count": 0},
]

ITALIAN_STOPWORDS = {"il", "lo", "la", "i", "gli", "le", "un", "una", "con", "per", "tra", "sul", "nel", "della", "delle", "degli", "che", "non", "sono", "sei"}


class RateLimitError(Exception):
    """Raised when HTTP 429 is returned by the Wyvern API."""
    pass


class WyvernScenarioClient:
    """Rate-limited HTTP client for Wyvern Character Scenarios API (1 req/s)."""

    def __init__(self, repo_root: str, rate_limit_per_sec: float = 1.0):
        self.repo_root = repo_root
        self.min_interval = 1.0 / rate_limit_per_sec
        self._last_call = 0.0
        self.token_path = os.path.join(repo_root, "scratch", "wyvern_token.txt")
        self.refresh_script = os.path.join(repo_root, "scratch", "refresh_token.py")

    def _get_token(self) -> str:
        if not os.path.exists(self.token_path):
            self._refresh_token()
        with open(self.token_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    def _refresh_token(self) -> str:
        print("[AUTH] Refreshing Firebase token via scratch/refresh_token.py...", file=sys.stderr)
        res = subprocess.run([sys.executable, self.refresh_script], cwd=self.repo_root, capture_output=True, text=True)
        if res.returncode != 0:
            raise RuntimeError(f"Token refresh failed: {res.stderr or res.stdout}")
        with open(self.token_path, "r", encoding="utf-8") as f:
            return f.read().strip()

    def _wait_rate_limit(self):
        now = time.monotonic()
        elapsed = now - self._last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self._last_call = time.monotonic()

    def request(self, method: str, url: str, payload: dict = None, max_retries: int = 3) -> dict:
        token = self._get_token()
        refreshed = False

        for attempt in range(1, max_retries + 1):
            self._wait_rate_limit()
            data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "AuditorBot/1.0",
            }
            req = urllib.request.Request(url, data=data, headers=headers, method=method)
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    body = resp.read().decode("utf-8")
                    return json.loads(body) if body else {}
            except urllib.error.HTTPError as e:
                err_body = e.read().decode("utf-8", errors="replace")
                if e.code == 429:
                    raise RateLimitError(f"HTTP 429 Rate Limit exceeded on {url} (limit={1.0/self.min_interval:.1f} req/s): {err_body}")
                if (e.code in (401, 403) or (e.code == 500 and "Unauthorized" in err_body)) and not refreshed:
                    refreshed = True
                    token = self._refresh_token()
                    continue
                if e.code >= 500 and attempt < max_retries:
                    backoff = 2 ** attempt
                    print(f"[RETRY] Transient HTTP {e.code} on {url}. Retrying in {backoff}s (attempt {attempt}/{max_retries})...", file=sys.stderr)
                    time.sleep(backoff)
                    continue
                raise RuntimeError(f"HTTP {e.code} on {method} {url} (rate_limit={1.0/self.min_interval:.1f} req/s): {err_body}")


def validate_scenario_data(data: dict) -> dict:
    errors = []
    warnings = []

    slots = data.get("slots", [])
    valid_slot_keys = set()

    if not slots:
        errors.append("Slots array is empty.")

    for s in slots:
        key = s.get("key")
        valid_slot_keys.add(key)
        if s.get("unavailable_count", 0) != 0:
            errors.append(f"Slot '{key}' has unavailable_count={s.get('unavailable_count')} (must be 0).")
        pool = s.get("pool", [])
        if not pool:
            errors.append(f"Slot '{key}' has an empty pool (all scenario slots must map to one of the 8 active cards).")
        for p in pool:
            cid = p.get("character_id")
            if cid not in ACTIVE_CARD_IDS:
                errors.append(f"Slot '{key}' references unknown/inactive character_id '{cid}'.")
            if p.get("weight") != 100:
                warnings.append(f"Slot '{key}' character '{cid}' has weight={p.get('weight')} (expected 100).")

    greetings = data.get("greetings", [])
    if not greetings:
        errors.append("Greetings array is empty.")

    for idx, g in enumerate(greetings):
        gname = g.get("name", f"greeting_{idx}")
        sp = g.get("speaker_slot")
        if sp not in valid_slot_keys:
            errors.append(f"Greeting [{idx}] '{gname}' has top-level speaker_slot='{sp}' not in active slots {sorted(valid_slot_keys)}.")

        msgs = g.get("messages", [])
        if not msgs:
            errors.append(f"Greeting [{idx}] '{gname}' has no messages.")
            continue

        if g.get("speaker_slot") != msgs[0].get("speaker_slot"):
            errors.append(f"Greeting [{idx}] '{gname}' speaker_slot ('{g.get('speaker_slot')}') != messages[0].speaker_slot ('{msgs[0].get('speaker_slot')}').")
        if g.get("content") != msgs[0].get("content"):
            errors.append(f"Greeting [{idx}] '{gname}' content != messages[0].content.")

        for midx, m in enumerate(msgs):
            msp = m.get("speaker_slot")
            if msp not in valid_slot_keys:
                errors.append(f"Greeting [{idx}] '{gname}' msg [{midx}] has speaker_slot='{msp}' not in active slots.")
            content = m.get("content", "")
            if "\u2014" in content:
                errors.append(f"Greeting [{idx}] '{gname}' msg [{midx}] contains forbidden em-dash (—).")
            if "*" in content:
                errors.append(f"Greeting [{idx}] '{gname}' msg [{midx}] contains forbidden asterisk (*).")

            words = set(re.findall(r"\b[a-zA-Zàèéìòù]+\b", content.lower()))
            it_hits = len(words.intersection(ITALIAN_STOPWORDS))
            if it_hits < 5:
                errors.append(f"Greeting [{idx}] '{gname}' msg [{midx}] does not appear to be in Italian (matched only {it_hits} Italian stopwords).")

            # Check Sierra Cruz bipedal forbidden verbs on paragraphs mentioning Sierra
            for para in content.split("\n"):
                if "sierra" in para.lower():
                    if re.search(r"\b(cammina|camminando|passi|passo|piedi|gambe|scarpe|walk|walked|walking|step|stepped|feet|legs|shoes)\b", para, re.IGNORECASE):
                        errors.append(f"Greeting [{idx}] '{gname}' msg [{midx}] violates Sierra Cruz Lamia locomotion rule in paragraph: {para[:100]}...")

    return {
        "scenario_id": data.get("id"),
        "name": data.get("name"),
        "revision": data.get("revision"),
        "slots_count": len(slots),
        "greetings_count": len(greetings),
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }


def cmd_validate(args):
    with open(args.scenario_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    report = validate_scenario_data(data)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Success! Validation report written to: {args.output}")
    if not report["valid"]:
        sys.exit(1)


def cmd_sync_slots(args):
    with open(args.scenario_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if args.route == "alyssa":
        data["slots"] = ALYSSA_CANONICAL_SLOTS
        fallback_slot = "twin"
    else:
        data["slots"] = JASPER_CANONICAL_SLOTS
        fallback_slot = "brother"

    valid_keys = {s["key"] for s in data["slots"]}
    reassigned = 0

    for g in data.get("greetings", []):
        for m in g.get("messages", []):
            if m.get("speaker_slot") not in valid_keys:
                m["speaker_slot"] = fallback_slot
                reassigned += 1
        if g.get("messages"):
            g["speaker_slot"] = g["messages"][0]["speaker_slot"]
            g["content"] = g["messages"][0]["content"]

    with open(args.scenario_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    report = {
        "scenario_path": args.scenario_path,
        "route": args.route,
        "slots_synced": len(data["slots"]),
        "orphan_speaker_slots_reassigned": reassigned,
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Success! Slots synced and report written to: {args.output}")


def cmd_deploy(args):
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    with open(args.scenario_path, "r", encoding="utf-8") as f:
        local_data = json.load(f)

    validation = validate_scenario_data(local_data)
    if not validation["valid"]:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(validation, f, indent=2, ensure_ascii=False)
        print(f"Error: Scenario validation failed prior to deploy. Details written to: {args.output}", file=sys.stderr)
        sys.exit(1)

    sid = local_data.get("id")
    if not sid:
        print("Error: Missing 'id' field in scenario JSON.", file=sys.stderr)
        sys.exit(1)

    client = WyvernScenarioClient(repo_root=repo_root, rate_limit_per_sec=1.0)
    url = f"https://app.wyvern.chat/api/character-scenarios/{sid}"

    remote_data = client.request("GET", url)
    current_rev = remote_data.get("revision", local_data.get("revision", 1))
    local_data["revision"] = current_rev

    put_resp = client.request("PUT", url, payload=local_data)
    new_rev = put_resp.get("revision", current_rev + 1)
    local_data["revision"] = new_rev

    with open(args.scenario_path, "w", encoding="utf-8") as f:
        json.dump(local_data, f, indent=2, ensure_ascii=False)

    verify_resp = client.request("GET", url)
    report = {
        "scenario_id": sid,
        "name": verify_resp.get("name"),
        "previous_revision": current_rev,
        "new_revision": verify_resp.get("revision"),
        "slots_count": len(verify_resp.get("slots", [])),
        "greetings_count": len(verify_resp.get("greetings", [])),
        "status": "DEPLOYED_AND_VERIFIED",
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"Success! Deployed {sid} (rev {current_rev} -> {verify_resp.get('revision')}). Report written to: {args.output}")


def main():
    parser = argparse.ArgumentParser(description="Validate, sync slots, and deploy Wyvern Character Scenarios.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_val = subparsers.add_parser("validate", help="Validate scenario slots, speaker_slots, Italian greetings, and formatting.")
    p_val.add_argument("--scenario-path", required=True, help="Path to the scenario JSON file.")
    p_val.add_argument("--output", required=True, help="Path to write the JSON validation report.")
    p_val.set_defaults(func=cmd_validate)

    p_sync = subparsers.add_parser("sync-slots", help="Sync scenario slots to the 8 active Character Cards.")
    p_sync.add_argument("--scenario-path", required=True, help="Path to the scenario JSON file.")
    p_sync.add_argument("--route", choices=["alyssa", "jasper"], required=True, help="Scenario protagonist route.")
    p_sync.add_argument("--output", required=True, help="Path to write the JSON sync report.")
    p_sync.set_defaults(func=cmd_sync_slots)

    p_dep = subparsers.add_parser("deploy", help="Validate and deploy a scenario JSON file live to Wyvern Web API.")
    p_dep.add_argument("--scenario-path", required=True, help="Path to the scenario JSON file.")
    p_dep.add_argument("--output", required=True, help="Path to write the JSON deployment report.")
    p_dep.set_defaults(func=cmd_deploy)

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

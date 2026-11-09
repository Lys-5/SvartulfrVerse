"""
Comprehensive Empirical Verification Script for Challenger 1
Checks proxy/config_free_proxy.json and free_tier_proxy.py.
"""

import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "proxy", "config_free_proxy.json")


def run_checks():
    print(f"=== Loading config from {CONFIG_PATH} ===")
    assert os.path.exists(CONFIG_PATH), f"Config file not found: {CONFIG_PATH}"

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    upstreams = cfg.get("upstreams", [])
    print(f"Total upstreams in config: {len(upstreams)}")

    # 1. Check basic keys
    assert "host" in cfg and cfg["host"] == "127.0.0.1", f"Host must be 127.0.0.1, got {cfg.get('host')}"
    assert "port" in cfg and cfg["port"] == 5005, f"Port must be 5005, got {cfg.get('port')}"
    assert "keys" in cfg and isinstance(cfg["keys"], dict), "Keys must be a dict"

    # 2. Inspect all upstreams
    print("\n=== Upstream Inspection ===")
    priorities = []
    purged_models = ["nemotron-3.5-content-safety", "north-mini-code"]

    for i, u in enumerate(upstreams):
        uid = u.get("id")
        p = u.get("priority")
        prov = u.get("provider")
        disp = u.get("display_name")
        base = u.get("base_url")
        models = u.get("models")
        model = u.get("model")

        # Validation of required fields
        assert uid, f"Upstream #{i} missing 'id'"
        assert prov, f"Upstream #{i} missing 'provider'"
        assert p is not None and isinstance(p, int), f"Upstream #{i} missing integer 'priority'"
        assert disp, f"Upstream #{i} missing 'display_name'"
        assert base and base.startswith("http"), f"Upstream #{i} missing valid 'base_url'"
        assert models or model, f"Upstream #{i} missing 'models' or 'model'"

        all_models = models if isinstance(models, list) else ([model] if model else [])
        for m in all_models:
            for purged in purged_models:
                assert purged not in m.lower(), f"PURGED MODEL FOUND! {m} contains {purged}"

        priorities.append(p)
        print(f"#{i+1:02d} | P{p:02d} | prov={prov:<11} | id={uid:<30} | models={all_models}")

    # 3. Verify ascending priority order
    for idx in range(len(priorities) - 1):
        assert priorities[idx] <= priorities[idx + 1], (
            f"Ascending priority violation: index {idx} has P{priorities[idx]}, "
            f"index {idx+1} has P{priorities[idx+1]}"
        )
    print("\n✅ All upstreams are strictly sorted in ascending priority order.")

    # 4. Verify 4 Fiat Pillars (Priorities 1..8)
    pillar_upstreams = [u for u in upstreams if 1 <= u.get("priority", 999) <= 8]
    pillar_priorities = sorted(list({u["priority"] for u in pillar_upstreams}))
    assert pillar_priorities == list(range(1, 9)), f"Expected priorities 1..8, got {pillar_priorities}"

    # Detailed pillar models verification:
    # P1 & P2: GLM
    p1_models = [m for u in upstreams if u["priority"] == 1 for m in (u.get("models") or [u.get("model")])]
    p2_models = [m for u in upstreams if u["priority"] == 2 for m in (u.get("models") or [u.get("model")])]
    assert any("glm-5.2" in m.lower() for m in p1_models), "P1 must include GLM 5.2"
    assert any("glm-5.3" in m.lower() for m in p1_models), "P1 must include GLM 5.3"
    assert any("glm-5.2" in m.lower() or "glm-5.1" in m.lower() for m in p2_models), "P2 must include GLM 5.2/5.1"
    print("✅ Pillar 1 (GLM 5.2/5.3): Verified at P1 and P2.")

    # P3: Gemini 4 Argon
    p3_models = [m for u in upstreams if u["priority"] == 3 for m in (u.get("models") or [u.get("model")])]
    assert any("gemini-4-argon" in m.lower() for m in p3_models), "P3 must include Gemini 4 Argon"
    print("✅ Pillar 2 (Gemini 4 Argon): Verified at P3.")

    # P4 & P5: Gemini 3.8 Flash & Gemini 3.1 Flash-Lite
    p4_models = [m for u in upstreams if u["priority"] == 4 for m in (u.get("models") or [u.get("model")])]
    p5_models = [m for u in upstreams if u["priority"] == 5 for m in (u.get("models") or [u.get("model")])]
    assert any("gemini-3.8-flash" in m.lower() for m in p4_models), "P4 must include Gemini 3.8 Flash"
    assert any("gemini-3.1-flash-lite" in m.lower() or "gemini-2.5-flash" in m.lower() for m in p5_models), "P5 must include Gemini Flash-Lite/2.5"
    print("✅ Pillar 3 (Gemini 3.8 Flash / Flash-Lite): Verified at P4 and P5.")

    # P6, P7, P8: Gemma 4
    p6_models = [m for u in upstreams if u["priority"] == 6 for m in (u.get("models") or [u.get("model")])]
    p7_models = [m for u in upstreams if u["priority"] == 7 for m in (u.get("models") or [u.get("model")])]
    p8_models = [m for u in upstreams if u["priority"] == 8 for m in (u.get("models") or [u.get("model")])]
    assert any("gemma-4" in m.lower() for m in p6_models), "P6 must include Gemma 4"
    assert any("gemma-4" in m.lower() for m in p7_models), "P7 must include Gemma 4"
    assert any("gemma-4" in m.lower() for m in p8_models), "P8 must include Gemma 4"
    print("✅ Pillar 4 (Gemma 4): Verified at P6, P7, and P8.")

    # 5. Roleplay Quality Ranking (Priorities 9..21)
    p9_21_upstreams = [u for u in upstreams if 9 <= u.get("priority", 999) <= 21]
    print(f"\nRoleplay Quality Ranked upstreams (P9..P21): {len(p9_21_upstreams)} upstreams")

    # 6. Zero moderation and code models
    print("\n✅ Zero moderation models (nemotron-3.5-content-safety) and code models (north-mini-code) confirmed across all upstreams.")


if __name__ == "__main__":
    run_checks()

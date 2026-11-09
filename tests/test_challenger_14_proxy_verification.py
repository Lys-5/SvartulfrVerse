"""
Challenger 14 Verification Test Suite:
Empirical verification of proxy/config_free_proxy.json and free_tier_proxy.py.
"""

import json
import os
import pytest
from proxy.free_tier_proxy import PayloadCompactor, get_config

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "proxy", "config_free_proxy.json")


def load_proxy_config():
    assert os.path.exists(CONFIG_PATH), f"Config file not found at {CONFIG_PATH}"
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def test_valid_json_parsing():
    """Verify that proxy/config_free_proxy.json parses as valid JSON."""
    cfg = load_proxy_config()
    assert isinstance(cfg, dict)
    assert "upstreams" in cfg
    assert isinstance(cfg["upstreams"], list)
    assert len(cfg["upstreams"]) > 0


def test_priority_sequence_and_fiat_pillars():
    """
    Priority sequence: verify that upstreams with priority 1-8 are exactly
    the 4 fiat pillars (GLM 5.2/5.3, Gemini 4 Argon, Gemini 3.8 Flash, Gemma 4).
    """
    cfg = load_proxy_config()
    upstreams = cfg["upstreams"]

    # Filter upstreams with priority between 1 and 8
    pillar_upstreams = [u for u in upstreams if 1 <= u.get("priority", 999) <= 8]
    assert len(pillar_upstreams) > 0

    pillar_priorities = sorted(list({u["priority"] for u in pillar_upstreams}))
    assert pillar_priorities == [1, 2, 3, 4, 5, 6, 7, 8], f"Expected priorities 1..8, got {pillar_priorities}"

    # Check that each upstream in 1..8 corresponds to one of the 4 pillars:
    # Pillar 1: GLM (5.2, 5.3, 4)
    # Pillar 2: Gemini 4 Argon / Pro (Gemini 4 Argon, 2.5 Pro)
    # Pillar 3: Gemini 3.8 Flash / Flash-Lite / Thinking
    # Pillar 4: Gemma 4 (31B, 26B, Turbo)
    for u in pillar_upstreams:
        p = u["priority"]
        models = u.get("models") or ([u.get("model")] if u.get("model") else [])
        assert len(models) > 0, f"Upstream {u.get('id')} has no models configured"

        name = u.get("display_name", "").lower()
        id_str = u.get("id", "").lower()

        if p in (1, 2):
            # Must be GLM
            is_glm = any("glm" in m.lower() for m in models) or "glm" in name or "glm" in id_str
            assert is_glm, f"Priority {p} upstream {u['id']} should be GLM pillar, got {models}"
        elif p == 3:
            # Must be Gemini 4 Argon / Pro
            is_argon = any("gemini-4-argon" in m.lower() or "gemini-2.5-pro" in m.lower() for m in models)
            assert is_argon, f"Priority 3 upstream {u['id']} should be Gemini 4 Argon/Pro, got {models}"
        elif p in (4, 5):
            # Must be Gemini 3.8 Flash / Flash-Lite / Thinking
            is_gemini_flash = any("gemini" in m.lower() for m in models)
            assert is_gemini_flash, f"Priority {p} upstream {u['id']} should be Gemini Flash pillar, got {models}"
        elif p in (6, 7, 8):
            # Must be Gemma 4
            is_gemma = any("gemma-4" in m.lower() for m in models)
            assert is_gemma, f"Priority {p} upstream {u['id']} should be Gemma 4 pillar, got {models}"


def test_ascending_priority_order_for_all_upstreams():
    """Verify that all remaining upstreams (and upstreams in general) are strictly sorted in ascending priority order."""
    cfg = load_proxy_config()
    upstreams = cfg["upstreams"]

    priorities = [u["priority"] for u in upstreams]
    # Check that priorities list is non-decreasing (ascending)
    for i in range(len(priorities) - 1):
        assert priorities[i] <= priorities[i + 1], (
            f"Upstreams are not in ascending priority order: index {i} has priority {priorities[i]}, "
            f"index {i+1} has priority {priorities[i+1]}"
        )


def test_zero_moderation_and_code_models():
    """Verify that zero upstreams contain moderation models (nemotron-3.5-content-safety) or code-only models (north-mini-code)."""
    cfg = load_proxy_config()
    upstreams = cfg["upstreams"]

    banned_substrings = ["nemotron-3.5-content-safety", "north-mini-code"]

    for u in upstreams:
        models = u.get("models") or ([u.get("model")] if u.get("model") else [])
        for m in models:
            for banned in banned_substrings:
                assert banned not in m.lower(), f"Banned model '{banned}' found in upstream {u.get('id')}: {m}"


def test_required_fields_presence():
    """
    Verify that every upstream has valid id, provider, model/models, priority, base_url, display_name.
    """
    cfg = load_proxy_config()
    upstreams = cfg["upstreams"]

    for idx, u in enumerate(upstreams):
        assert "id" in u and u["id"], f"Upstream #{idx} missing valid 'id'"
        assert "provider" in u and u["provider"], f"Upstream #{idx} missing valid 'provider'"
        assert "priority" in u and isinstance(u["priority"], int), f"Upstream #{idx} missing valid 'priority'"
        assert "base_url" in u and u["base_url"].startswith("http"), f"Upstream #{idx} missing valid 'base_url'"
        assert "display_name" in u and u["display_name"], f"Upstream #{idx} missing valid 'display_name'"

        has_models = "models" in u and isinstance(u["models"], list) and len(u["models"]) > 0
        has_model = "model" in u and isinstance(u["model"], str) and len(u["model"]) > 0
        assert has_models or has_model, f"Upstream #{idx} ({u.get('id')}) has neither valid 'models' list nor 'model' string"


def test_parameter_sanitization_edge_cases():
    """
    Empirically test parameter sanitization in free_tier_proxy.py with edge case parameters
    across multiple providers: zhipu, sambanova, github, google, groq, mistral, cerebras, etc.
    """
    compactor = PayloadCompactor()

    providers_to_test = [
        "zhipu",
        "sambanova",
        "github",
        "google",
        "groq",
        "mistral",
        "cerebras",
        "nvidia",
        "cloudflare",
        "siliconflow",
        "openrouter",
        "chutes",
    ]

    for prov in providers_to_test:
        raw_body = {
            "model": "test-model",
            "messages": [{"role": "user", "content": "Hello world"}],
            "frequency_penalty": 0.8,
            "presence_penalty": 0.5,
            "top_k": 40,
            "max_tokens": 16384,
            "temperature": 0.7,
            "stop": ["\nNarrator:", "Human:", "\n\n"],
        }

        sanitized = compactor.sanitize_parameters(compactor.deep_copy_payload(raw_body), provider=prov)

        # 1. Frequency / Presence penalty check
        if prov in (
            "google",
            "sambanova",
            "groq",
            "nvidia",
            "cloudflare",
            "zhipu",
            "github",
            "cerebras",
            "mistral",
            "siliconflow",
        ):
            assert "frequency_penalty" not in sanitized, f"Provider {prov} should strip frequency_penalty"
            assert "presence_penalty" not in sanitized, f"Provider {prov} should strip presence_penalty"

        # 2. top_k handling
        if prov == "chutes":
            assert sanitized.get("top_k") == -1, f"Provider chutes must have top_k = -1"
        else:
            assert sanitized.get("top_k") == 40

        # 3. max_tokens clamping
        if prov in (
            "google",
            "openrouter",
            "groq",
            "cerebras",
            "sambanova",
            "mistral",
            "zhipu",
            "github",
            "siliconflow",
            "nvidia",
            "cloudflare",
        ):
            assert sanitized.get("max_tokens") == 8192, f"Provider {prov} must clamp max_tokens to 8192, got {sanitized.get('max_tokens')}"

        # 4. stop sequence sanitization
        stop_seq = sanitized.get("stop", [])
        assert all("narrator" not in s.lower() for s in stop_seq), f"Narrator stop sequence not removed for {prov}: {stop_seq}"


def test_parameter_sanitization_zero_values_and_none():
    """Test edge cases with 0, None, negative values, and empty stop lists."""
    compactor = PayloadCompactor()

    # Zero penalties should be popped even for providers that normally allow them
    body = {
        "frequency_penalty": 0,
        "presence_penalty": 0.0,
        "top_k": -5,
        "max_tokens": 1000,
        "stop": ["\nNarrator:"],
    }
    sanitized = compactor.sanitize_parameters(compactor.deep_copy_payload(body), provider="openrouter")
    assert "frequency_penalty" not in sanitized
    assert "presence_penalty" not in sanitized
    assert "top_k" not in sanitized
    assert "stop" not in sanitized  # entire stop removed because all items were Narrator


def test_r1_reasoning_model_penalty_stripping():
    """Verify that any target_model containing 'r1' has sampling penalties stripped, regardless of provider."""
    compactor = PayloadCompactor()
    body = {
        "frequency_penalty": 0.7,
        "presence_penalty": 0.6,
        "temperature": 0.6,
    }
    sanitized = compactor.sanitize_parameters(
        compactor.deep_copy_payload(body),
        provider="openrouter",
        target_model="deepseek/deepseek-r1:free",
    )
    assert "frequency_penalty" not in sanitized
    assert "presence_penalty" not in sanitized


def test_single_string_stop_sequence_handling():
    """Verify string 'stop' parameter handling with Narrator variants and normal sequences."""
    compactor = PayloadCompactor()

    # Case A: String contains narrator -> should be completely removed
    bodyA = {"stop": "\nNarrator: "}
    resA = compactor.sanitize_parameters(compactor.deep_copy_payload(bodyA))
    assert "stop" not in resA

    # Case B: String is normal stop -> should be preserved
    bodyB = {"stop": "\nUser: "}
    resB = compactor.sanitize_parameters(compactor.deep_copy_payload(bodyB))
    assert resB.get("stop") == "\nUser: "


def test_max_tokens_boundary_conditions():
    """Verify boundary conditions for max_tokens (<= 8192 vs > 8192, float, negative)."""
    compactor = PayloadCompactor()

    # Exactly 8192 -> unchanged
    res = compactor.sanitize_parameters({"max_tokens": 8192}, provider="groq")
    assert res["max_tokens"] == 8192

    # 8193 -> clamped to 8192
    res = compactor.sanitize_parameters({"max_tokens": 8193}, provider="groq")
    assert res["max_tokens"] == 8192

    # Float 10000.0 -> clamped to 8192
    res = compactor.sanitize_parameters({"max_tokens": 10000.0}, provider="google")
    assert res["max_tokens"] == 8192

    # Non-clamped provider (if any generic) with small token
    res = compactor.sanitize_parameters({"max_tokens": 2048}, provider="openrouter")
    assert res["max_tokens"] == 2048


def test_all_keys_block_and_aliases_resolution():
    """Verify config contains all 15 provider keys and resolve_keys checks environment aliases."""
    from proxy.free_tier_proxy import resolve_keys

    cfg = load_proxy_config()
    keys_block = cfg.get("keys", {})

    expected_keys = [
        "google_ai_studio",
        "openrouter",
        "groq",
        "chutes",
        "sambanova",
        "nvidia",
        "cloudflare",
        "github",
        "huggingface",
        "deepinfra",
        "zhipu",
        "deepseek",
        "cerebras",
        "siliconflow",
        "mistral",
    ]
    for k in expected_keys:
        assert k in keys_block, f"Missing key '{k}' in config_free_proxy.json keys block"

    # Test alias resolution for zhipu via GLM_API_KEY
    os.environ["GLM_API_KEY"] = "test-glm-alias-12345"
    resolved = resolve_keys("zhipu", incoming_auth=None)
    assert "test-glm-alias-12345" in resolved

    # Test alias resolution for github via GITHUB_TOKEN
    os.environ["GITHUB_TOKEN"] = "test-gh-token-67890"
    resolved_gh = resolve_keys("github", incoming_auth=None)
    assert "test-gh-token-67890" in resolved_gh

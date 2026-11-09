"""
Empirical Verification & Stress Test Suite: Proxy Runtime, Fallback Routing & Key Resolution
Milestone 14 — Empirical Challenger 2 (critic, specialist)
Tests:
  1. Live runtime accessibility on http://127.0.0.1:5005 (/health and /v1/models)
  2. CORS & Private Network Access (PNA) header conformance
  3. Key resolution from config_free_proxy.json (string & list formats)
  4. Key resolution from environment variables & aliases
  5. Key resolution deduplication & bearer token handling
  6. Dynamic .env loading via python-dotenv
  7. Dormant keys activation & accessibility (SambaNova & GitHub)
  8. Fallback routing in ascending priority order on HTTP errors (500, 429, 402, 403)
  9. Fallback routing on missing keys (skip without request)
  10. Fallback routing on active quarantine / cooldown
  11. Fallback routing on empty content / invalid 200 payload
  12. Total fallback exhaustion (HTTP 503 error propagation)
  13. Upstream payload parameter sanitization during fallback
"""

import os
import json
import time
import copy
import urllib.request
import urllib.error
import pytest
from unittest.mock import patch, AsyncMock
import httpx
from starlette.testclient import TestClient

from proxy.free_tier_proxy import (
    app,
    get_config,
    resolve_keys,
    cooldowns,
    make_cd_key,
    is_available,
    mark_cooldown,
    validate_and_normalize_response,
    PayloadCompactor,
)

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "proxy",
    "config_free_proxy.json",
)


@pytest.fixture(autouse=True)
def clean_proxy_state():
    """Ensure clean cooldowns and state between tests."""
    original_cooldowns = dict(cooldowns)
    cooldowns.clear()
    yield
    cooldowns.clear()
    cooldowns.update(original_cooldowns)


# =========================================================================
# 1. LIVE RUNTIME VERIFICATION (Socket level http://127.0.0.1:5005)
# =========================================================================

def test_live_runtime_health_and_models_endpoints():
    """Verify live running proxy on 127.0.0.1:5005 responds cleanly to /health and /v1/models."""
    # Test /health
    health_url = "http://127.0.0.1:5005/health"
    req_health = urllib.request.Request(health_url, headers={"User-Agent": "Challenger2"})
    try:
        with urllib.request.urlopen(req_health, timeout=5.0) as resp:
            assert resp.status == 200, f"Expected 200 from {health_url}, got {resp.status}"
            data = json.loads(resp.read().decode("utf-8"))
            assert data.get("status") == "ok", f"Expected status 'ok', got {data.get('status')}"
            assert "active_cooldowns" in data
            assert "log_file" in data
            assert os.path.exists(data["log_file"]), f"Log file does not exist: {data['log_file']}"
    except urllib.error.URLError as e:
        pytest.fail(f"Live proxy not accessible at {health_url}: {e}")

    # Test /v1/models
    models_url = "http://127.0.0.1:5005/v1/models"
    req_models = urllib.request.Request(models_url, headers={"User-Agent": "Challenger2"})
    try:
        with urllib.request.urlopen(req_models, timeout=5.0) as resp:
            assert resp.status == 200, f"Expected 200 from {models_url}, got {resp.status}"
            data = json.loads(resp.read().decode("utf-8"))
            assert data.get("object") == "list"
            models = data.get("data", [])
            assert len(models) >= 1
            master_model = next((m for m in models if m.get("id") == "free-tier-master"), None)
            assert master_model is not None, "Missing 'free-tier-master' in models endpoint"
            assert master_model.get("owned_by") == "wyvern-proxy"
    except urllib.error.URLError as e:
        pytest.fail(f"Live proxy models endpoint not accessible at {models_url}: {e}")


def test_cors_and_private_network_access_headers():
    """Verify CORS and Private Network Access (PNA) headers are returned on preflight and requests."""
    client = TestClient(app)
    # GET request with Origin
    resp = client.get("/health", headers={"Origin": "https://app.wyvern.chat"})
    assert resp.status_code == 200
    assert resp.headers.get("access-control-allow-origin") == "https://app.wyvern.chat"
    assert resp.headers.get("access-control-allow-private-network") == "true"

    # OPTIONS preflight request
    options_resp = client.options(
        "/v1/chat/completions",
        headers={
            "Origin": "https://app.wyvern.chat",
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "authorization, content-type",
        },
    )
    assert options_resp.status_code == 200
    assert options_resp.headers.get("access-control-allow-origin") == "https://app.wyvern.chat"
    assert options_resp.headers.get("access-control-allow-private-network") == "true"


# =========================================================================
# 2. KEY RESOLUTION LOGIC TESTS (Config, Env Vars, Aliases, Deduplication)
# =========================================================================

def test_key_resolution_from_config_file():
    """Verify resolve_keys extracts string and list keys from config_free_proxy.json."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    # 1. String key in config (e.g. groq, sambanova)
    groq_keys = resolve_keys("groq", None)
    assert len(groq_keys) >= 1
    assert cfg["keys"]["groq"] in groq_keys

    # 2. List of keys in config (e.g. openrouter)
    or_keys = resolve_keys("openrouter", None)
    assert len(or_keys) >= 2
    for k in cfg["keys"]["openrouter"]:
        assert k in or_keys

    # 3. Blank string in config returns empty list if no env var
    with patch.dict(os.environ, {}, clear=True):
        zhipu_keys = resolve_keys("zhipu", None)
        assert zhipu_keys == [], f"Expected empty list for blank zhipu key, got {zhipu_keys}"


def test_key_resolution_from_environment_variables():
    """Verify resolve_keys loads keys from environment variables and provider aliases."""
    test_env = {
        "SAMBANOVA_API_KEY": "env_samba_secret_123",
        "GITHUB_TOKEN": "env_gh_token_456",
        "AZURE_INFERENCE_CREDENTIAL": "env_azure_cred_789",
        "GEMINI_API_KEY": "env_gemini_key_101",
        "ZHIPU_API_KEY": "env_zhipu_key_202",
        "BIGMODEL_API_KEY": "env_bigmodel_key_303",
        "SILICON_API_KEY": "env_silicon_key_404",
        "CLOUDFLARE_API_TOKEN": "env_cf_token_505",
    }
    with patch.dict(os.environ, test_env, clear=False):
        # SambaNova env
        samba = resolve_keys("sambanova", None)
        assert "env_samba_secret_123" in samba

        # GitHub env alias GITHUB_TOKEN and AZURE_INFERENCE_CREDENTIAL
        gh = resolve_keys("github", None)
        assert "env_gh_token_456" in gh
        assert "env_azure_cred_789" in gh

        # Google AI Studio alias GEMINI_API_KEY
        google = resolve_keys("google_ai_studio", None)
        assert "env_gemini_key_101" in google

        # Zhipu alias ZHIPU_API_KEY and BIGMODEL_API_KEY
        zhipu = resolve_keys("zhipu", None)
        assert "env_zhipu_key_202" in zhipu
        assert "env_bigmodel_key_303" in zhipu

        # SiliconFlow alias SILICON_API_KEY
        sf = resolve_keys("siliconflow", None)
        assert "env_silicon_key_404" in sf

        # Cloudflare alias CLOUDFLARE_API_TOKEN
        cf = resolve_keys("cloudflare", None)
        assert "env_cf_token_505" in cf


def test_key_resolution_deduplication_and_bearer_filtering():
    """Verify duplicate keys are stripped and dummy incoming auth is ignored."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    cfg_samba = cfg["keys"]["sambanova"]

    # When env var matches config key exactly, it should NOT produce duplicate
    with patch.dict(os.environ, {"SAMBANOVA_API_KEY": cfg_samba}, clear=False):
        keys = resolve_keys("sambanova", None)
        assert keys.count(cfg_samba) == 1

    # Incoming auth filtering
    # 1. sk-dummy should be filtered out
    keys_dummy = resolve_keys("zhipu", incoming_auth="Bearer sk-dummy-key-999")
    assert "sk-dummy-key-999" not in keys_dummy

    # 2. 'local' should be filtered out
    keys_local = resolve_keys("zhipu", incoming_auth="Bearer local")
    assert "local" not in keys_local

    # 3. Legitimate user-provided bearer token should be accepted
    keys_user = resolve_keys("zhipu", incoming_auth="Bearer user-custom-valid-key")
    assert "user-custom-valid-key" in keys_user


def test_dotenv_loading_mechanism(tmp_path):
    """Verify python-dotenv dynamically loads keys from a temporary .env file."""
    from dotenv import load_dotenv

    temp_env_file = tmp_path / ".env"
    temp_env_file.write_text(
        "MISTRAL_API_KEY=dotenv_mistral_secret_999\nCEREBRAS_API_KEY=dotenv_cerebras_secret_888\n",
        encoding="utf-8",
    )

    with patch.dict(os.environ, {}, clear=False):
        os.environ.pop("MISTRAL_API_KEY", None)
        os.environ.pop("CEREBRAS_API_KEY", None)
        load_dotenv(str(temp_env_file))

        mistral = resolve_keys("mistral", None)
        assert "dotenv_mistral_secret_999" in mistral

        cerebras = resolve_keys("cerebras", None)
        assert "dotenv_cerebras_secret_888" in cerebras


# =========================================================================
# 3. DORMANT KEYS ACTIVATION & ACCESSIBILITY (SambaNova & GitHub)
# =========================================================================

def test_dormant_keys_active_and_accessible_in_config():
    """Empirically verify that dormant keys 'sambanova' and 'github' are populated and wired to upstreams."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    keys = cfg.get("keys", {})
    upstreams = cfg.get("upstreams", [])

    # 1. SambaNova key presence and validity
    assert "sambanova" in keys, "Key 'sambanova' missing from config keys"
    sambanova_key = keys["sambanova"]
    assert isinstance(sambanova_key, str) and len(sambanova_key) > 20, (
        f"Invalid or empty SambaNova key: {sambanova_key}"
    )

    # 2. GitHub key presence and validity
    assert "github" in keys, "Key 'github' missing from config keys"
    github_key = keys["github"]
    assert isinstance(github_key, str) and (github_key.startswith("ghp_") or len(github_key) > 20), (
        f"Invalid or empty GitHub key: {github_key}"
    )

    # 3. Upstreams referencing SambaNova
    sambanova_upstreams = [u for u in upstreams if u.get("key_name") == "sambanova"]
    assert len(sambanova_upstreams) >= 3, (
        f"Expected at least 3 SambaNova upstreams (P6, P12, P16), found {len(sambanova_upstreams)}"
    )

    # Verify Priority 6: Gemma 4 31B
    p6 = next((u for u in sambanova_upstreams if u.get("priority") == 6), None)
    assert p6 is not None, "Missing Priority 6 SambaNova Gemma 4 upstream"
    assert "gemma-4-31B-it" in p6.get("models", [])
    assert p6.get("base_url") == "https://api.sambanova.ai/v1/chat/completions"

    # Verify Priority 12: Qwen 2.5 72B
    p12 = next((u for u in sambanova_upstreams if u.get("priority") == 12), None)
    assert p12 is not None, "Missing Priority 12 SambaNova Qwen 2.5 upstream"
    assert "Qwen2.5-72B-Instruct" in p12.get("models", [])

    # Verify Priority 16: Llama 3.3 70B
    p16 = next((u for u in sambanova_upstreams if u.get("priority") == 16), None)
    assert p16 is not None, "Missing Priority 16 SambaNova Llama 3.3 upstream"
    assert "Meta-Llama-3.3-70B-Instruct" in p16.get("models", [])

    # 4. Upstreams referencing GitHub Models
    github_upstreams = [u for u in upstreams if u.get("key_name") == "github"]
    assert len(github_upstreams) >= 1, "Missing GitHub Models upstream"
    p22 = github_upstreams[0]
    assert p22.get("priority") == 22, f"Expected GitHub Models at Priority 22, got {p22.get('priority')}"
    assert "gpt-4o" in p22.get("models", [])
    assert p22.get("base_url") == "https://models.inference.ai.azure.com/chat/completions"


# =========================================================================
# 4. FALLBACK ROUTING TEST HARNESS (Ascending Priority Order, HTTP Errors,
#    Quarantine, Missing Keys, Empty Responses, and Complete Exhaustion)
# =========================================================================

def _build_mock_http_response(status_code: int, content_dict: dict, request: httpx.Request):
    """Helper to build httpx.Response instances."""
    return httpx.Response(
        status_code=status_code,
        content=json.dumps(content_dict).encode("utf-8"),
        request=request,
        headers={"Content-Type": "application/json"},
    )


@pytest.mark.anyio
async def test_fallback_routing_ascending_priority_on_errors():
    """
    Stress Test: Verify proxy attempts upstreams in strictly ascending priority order.
    When Priority 1 fails (HTTP 500) and Priority 2 fails (HTTP 429),
    Priority 3 is called and succeeds with HTTP 200.
    """
    call_log = []

    mock_config = {
        "host": "127.0.0.1",
        "port": 5005,
        "cooldown_seconds": 60,
        "timeout_seconds": 10.0,
        "keys": {
            "key1": "token-p1",
            "key2": "token-p2",
            "key3": "token-p3",
        },
        "upstreams": [
            {
                "priority": 3,
                "id": "upstream-p3",
                "display_name": "Upstream Priority 3",
                "provider": "generic",
                "models": ["model-p3"],
                "base_url": "https://api.p3.test/v1/chat/completions",
                "key_name": "key3",
            },
            {
                "priority": 1,
                "id": "upstream-p1",
                "display_name": "Upstream Priority 1",
                "provider": "generic",
                "models": ["model-p1"],
                "base_url": "https://api.p1.test/v1/chat/completions",
                "key_name": "key1",
            },
            {
                "priority": 2,
                "id": "upstream-p2",
                "display_name": "Upstream Priority 2",
                "provider": "generic",
                "models": ["model-p2"],
                "base_url": "https://api.p2.test/v1/chat/completions",
                "key_name": "key2",
            },
        ],
    }

    async def mock_send(self, req: httpx.Request, *args, **kwargs):
        url = str(req.url)
        call_log.append(url)
        if "api.p1.test" in url:
            return _build_mock_http_response(500, {"error": "Internal Server Error"}, req)
        elif "api.p2.test" in url:
            return _build_mock_http_response(429, {"error": "Rate limit reached"}, req)
        elif "api.p3.test" in url:
            return _build_mock_http_response(
                200,
                {
                    "id": "chatcmpl-test-p3",
                    "choices": [{"message": {"role": "assistant", "content": "Success from P3"}}],
                },
                req,
            )
        return _build_mock_http_response(404, {"error": "Not Found"}, req)

    with patch("proxy.free_tier_proxy.get_config", return_value=mock_config):
        with patch.object(httpx.AsyncClient, "send", new=mock_send):
            client = TestClient(app)
            response = client.post(
                "/v1/chat/completions",
                json={
                    "model": "free-tier-master",
                    "messages": [{"role": "user", "content": "Hello"}],
                },
            )

            assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
            data = response.json()
            assert data["choices"][0]["message"]["content"] == "Success from P3"
            assert "Upstream Priority 3" in response.headers.get("X-Served-By", "")

            # Verify STRICT ascending priority execution order
            assert len(call_log) == 3
            assert "api.p1.test" in call_log[0], f"First call must be P1, got {call_log[0]}"
            assert "api.p2.test" in call_log[1], f"Second call must be P2, got {call_log[1]}"
            assert "api.p3.test" in call_log[2], f"Third call must be P3, got {call_log[2]}"

            # Verify P1 and P2 were placed into cooldown
            cd_p1 = make_cd_key("upstream-p1", "model-p1", "token-p1")
            cd_p2 = make_cd_key("upstream-p2", "model-p2", "token-p2")
            assert not is_available(cd_p1), "P1 should be in cooldown after HTTP 500"
            assert not is_available(cd_p2), "P2 should be in cooldown after HTTP 429"


@pytest.mark.anyio
async def test_fallback_routing_skips_missing_key_without_request():
    """
    Stress Test: Verify that an upstream with NO key configured is skipped
    immediately without generating an HTTP request, proceeding to the next priority.
    """
    call_log = []

    mock_config = {
        "host": "127.0.0.1",
        "port": 5005,
        "cooldown_seconds": 60,
        "timeout_seconds": 10.0,
        "keys": {
            "empty_key": "",
            "valid_key": "token-p2",
        },
        "upstreams": [
            {
                "priority": 1,
                "id": "upstream-no-key",
                "display_name": "Upstream No Key",
                "provider": "generic",
                "models": ["model-p1"],
                "base_url": "https://api.no-key.test/v1/chat/completions",
                "key_name": "empty_key",
            },
            {
                "priority": 2,
                "id": "upstream-with-key",
                "display_name": "Upstream With Key",
                "provider": "generic",
                "models": ["model-p2"],
                "base_url": "https://api.with-key.test/v1/chat/completions",
                "key_name": "valid_key",
            },
        ],
    }

    async def mock_send(self, req: httpx.Request, *args, **kwargs):
        url = str(req.url)
        call_log.append(url)
        if "api.with-key.test" in url:
            return _build_mock_http_response(
                200,
                {
                    "id": "chatcmpl-test-p2",
                    "choices": [{"message": {"role": "assistant", "content": "Success from P2"}}],
                },
                req,
            )
        return _build_mock_http_response(500, {"error": "Unexpected"}, req)

    with patch("proxy.free_tier_proxy.get_config", return_value=mock_config):
        with patch.object(httpx.AsyncClient, "send", new=mock_send):
            client = TestClient(app)
            response = client.post(
                "/v1/chat/completions",
                json={
                    "model": "free-tier-master",
                    "messages": [{"role": "user", "content": "Hello"}],
                },
            )

            assert response.status_code == 200
            assert response.json()["choices"][0]["message"]["content"] == "Success from P2"

            # Verify P1 (no key) was NEVER called over the network!
            assert len(call_log) == 1
            assert "api.with-key.test" in call_log[0]
            assert not any("api.no-key.test" in url for url in call_log)


@pytest.mark.anyio
async def test_fallback_routing_skips_quarantined_upstream():
    """
    Stress Test: Verify that an upstream currently in active cooldown/quarantine
    is bypassed without network calls, falling through to the next available upstream.
    """
    call_log = []

    mock_config = {
        "host": "127.0.0.1",
        "port": 5005,
        "cooldown_seconds": 60,
        "timeout_seconds": 10.0,
        "keys": {
            "key1": "token-p1",
            "key2": "token-p2",
        },
        "upstreams": [
            {
                "priority": 1,
                "id": "upstream-cooldown",
                "display_name": "Upstream Cooldown",
                "provider": "generic",
                "models": ["model-p1"],
                "base_url": "https://api.cooldown.test/v1/chat/completions",
                "key_name": "key1",
            },
            {
                "priority": 2,
                "id": "upstream-active",
                "display_name": "Upstream Active",
                "provider": "generic",
                "models": ["model-p2"],
                "base_url": "https://api.active.test/v1/chat/completions",
                "key_name": "key2",
            },
        ],
    }

    # Pre-quarantine Priority 1
    cd_p1 = make_cd_key("upstream-cooldown", "model-p1", "token-p1")
    mark_cooldown(cd_p1, "Upstream Cooldown", "Simulated previous rate limit", duration=120)
    assert not is_available(cd_p1)

    async def mock_send(self, req: httpx.Request, *args, **kwargs):
        url = str(req.url)
        call_log.append(url)
        if "api.active.test" in url:
            return _build_mock_http_response(
                200,
                {
                    "id": "chatcmpl-test-active",
                    "choices": [{"message": {"role": "assistant", "content": "Served by active P2"}}],
                },
                req,
            )
        return _build_mock_http_response(500, {"error": "Unexpected"}, req)

    with patch("proxy.free_tier_proxy.get_config", return_value=mock_config):
        with patch.object(httpx.AsyncClient, "send", new=mock_send):
            client = TestClient(app)
            response = client.post(
                "/v1/chat/completions",
                json={
                    "model": "free-tier-master",
                    "messages": [{"role": "user", "content": "Hello"}],
                },
            )

            assert response.status_code == 200
            assert response.json()["choices"][0]["message"]["content"] == "Served by active P2"

            # Quarantined P1 was skipped immediately with 0 network calls
            assert len(call_log) == 1
            assert "api.active.test" in call_log[0]


@pytest.mark.anyio
async def test_fallback_routing_on_empty_content_response():
    """
    Stress Test: When an upstream returns HTTP 200 but choices[0].message.content is empty/blank,
    validate_and_normalize_response must reject it, mark cooldown, and fall through to next upstream.
    """
    call_log = []

    mock_config = {
        "host": "127.0.0.1",
        "port": 5005,
        "cooldown_seconds": 60,
        "timeout_seconds": 10.0,
        "keys": {
            "key1": "token-p1",
            "key2": "token-p2",
        },
        "upstreams": [
            {
                "priority": 1,
                "id": "upstream-empty-p1",
                "display_name": "Upstream Empty Text",
                "provider": "generic",
                "models": ["model-p1"],
                "base_url": "https://api.empty.test/v1/chat/completions",
                "key_name": "key1",
            },
            {
                "priority": 2,
                "id": "upstream-valid-p2",
                "display_name": "Upstream Valid Text",
                "provider": "generic",
                "models": ["model-p2"],
                "base_url": "https://api.valid.test/v1/chat/completions",
                "key_name": "key2",
            },
        ],
    }

    async def mock_send(self, req: httpx.Request, *args, **kwargs):
        url = str(req.url)
        call_log.append(url)
        if "api.empty.test" in url:
            # 200 OK but empty content!
            return _build_mock_http_response(
                200,
                {
                    "id": "chatcmpl-empty",
                    "choices": [{"message": {"role": "assistant", "content": "   "}}],
                },
                req,
            )
        elif "api.valid.test" in url:
            return _build_mock_http_response(
                200,
                {
                    "id": "chatcmpl-valid",
                    "choices": [{"message": {"role": "assistant", "content": "Valid narrative response"}}],
                },
                req,
            )
        return _build_mock_http_response(500, {}, req)

    with patch("proxy.free_tier_proxy.get_config", return_value=mock_config):
        with patch.object(httpx.AsyncClient, "send", new=mock_send):
            client = TestClient(app)
            response = client.post(
                "/v1/chat/completions",
                json={
                    "model": "free-tier-master",
                    "messages": [{"role": "user", "content": "Describe the scene"}],
                },
            )

            assert response.status_code == 200
            assert response.json()["choices"][0]["message"]["content"] == "Valid narrative response"

            # Both upstreams were tried in order
            assert len(call_log) == 2
            assert "api.empty.test" in call_log[0]
            assert "api.valid.test" in call_log[1]

            # P1 was marked in cooldown due to empty text response
            cd_p1 = make_cd_key("upstream-empty-p1", "model-p1", "token-p1")
            assert not is_available(cd_p1)


@pytest.mark.anyio
async def test_fallback_routing_all_upstreams_exhausted_raises_503():
    """
    Stress Test: When every upstream in the cascade fails (e.g. 500/429/timeout),
    the proxy must raise HTTP 503 Service Unavailable with descriptive details.
    """
    mock_config = {
        "host": "127.0.0.1",
        "port": 5005,
        "cooldown_seconds": 60,
        "timeout_seconds": 10.0,
        "keys": {
            "key1": "token-p1",
            "key2": "token-p2",
        },
        "upstreams": [
            {
                "priority": 1,
                "id": "upstream-failing-1",
                "display_name": "Failing 1",
                "provider": "generic",
                "models": ["model-p1"],
                "base_url": "https://api.fail1.test/v1/chat/completions",
                "key_name": "key1",
            },
            {
                "priority": 2,
                "id": "upstream-failing-2",
                "display_name": "Failing 2",
                "provider": "generic",
                "models": ["model-p2"],
                "base_url": "https://api.fail2.test/v1/chat/completions",
                "key_name": "key2",
            },
        ],
    }

    async def mock_send(self, req: httpx.Request, *args, **kwargs):
        return _build_mock_http_response(500, {"error": "Downstream failure"}, req)

    with patch("proxy.free_tier_proxy.get_config", return_value=mock_config):
        with patch.object(httpx.AsyncClient, "send", new=mock_send):
            client = TestClient(app)
            response = client.post(
                "/v1/chat/completions",
                json={
                    "model": "free-tier-master",
                    "messages": [{"role": "user", "content": "Hello"}],
                },
            )

            assert response.status_code == 503
            data = response.json()
            assert "Tutti i modelli Free Tier hanno fallito" in data["detail"]


@pytest.mark.anyio
async def test_fallback_routing_to_sambanova_dormant_pillar():
    """
    Verification Test: Simulate failure of tiers 1-5, verifying the proxy
    falls through directly to SambaNova at Priority 6 with correct authorization header and model.
    """
    captured_requests = []

    # Filter config to upstreams 1 to 6
    cfg = get_config()
    target_upstreams = [u for u in cfg["upstreams"] if u.get("priority", 99) <= 6]
    test_cfg = copy.deepcopy(cfg)
    test_cfg["upstreams"] = target_upstreams

    async def mock_send(self, req: httpx.Request, *args, **kwargs):
        captured_requests.append(req)
        url = str(req.url)
        if "api.sambanova.ai" in url:
            return _build_mock_http_response(
                200,
                {
                    "id": "sambanova-chatcmpl-123",
                    "choices": [{"message": {"role": "assistant", "content": "Hello from SambaNova Gemma 4!"}}],
                },
                req,
            )
        # Prior upstreams fail
        return _build_mock_http_response(429, {"error": "Rate limit"}, req)

    with patch("proxy.free_tier_proxy.get_config", return_value=test_cfg):
        with patch.object(httpx.AsyncClient, "send", new=mock_send):
            client = TestClient(app)
            response = client.post(
                "/v1/chat/completions",
                json={
                    "model": "free-tier-master",
                    "messages": [{"role": "user", "content": "Ping"}],
                },
            )

            assert response.status_code == 200
            assert response.json()["choices"][0]["message"]["content"] == "Hello from SambaNova Gemma 4!"

            # Find the SambaNova request
            samba_req = next((r for r in captured_requests if "api.sambanova.ai" in str(r.url)), None)
            assert samba_req is not None, "SambaNova was not reached during fallback cascade"
            assert samba_req.headers.get("authorization") == f"Bearer {cfg['keys']['sambanova']}"
            req_body = json.loads(samba_req.content.decode("utf-8"))
            assert req_body.get("model") == "gemma-4-31B-it"


@pytest.mark.anyio
async def test_fallback_routing_to_github_models():
    """
    Verification Test: Simulate cascade fallback reaching Priority 22 (GitHub Models),
    verifying proper auth bearer and target model.
    """
    captured_requests = []

    cfg = get_config()
    p22 = [u for u in cfg["upstreams"] if u.get("priority") == 22]
    assert len(p22) >= 1, "Missing Priority 22 in config"
    test_cfg = copy.deepcopy(cfg)
    test_cfg["upstreams"] = p22

    async def mock_send(self, req: httpx.Request, *args, **kwargs):
        captured_requests.append(req)
        url = str(req.url)
        if "models.inference.ai.azure.com" in url:
            return _build_mock_http_response(
                200,
                {
                    "id": "github-azure-chatcmpl-456",
                    "choices": [{"message": {"role": "assistant", "content": "Hello from GitHub Models gpt-4o!"}}],
                },
                req,
            )
        return _build_mock_http_response(500, {"error": "Unexpected"}, req)

    with patch("proxy.free_tier_proxy.get_config", return_value=test_cfg):
        with patch.object(httpx.AsyncClient, "send", new=mock_send):
            client = TestClient(app)
            response = client.post(
                "/v1/chat/completions",
                json={
                    "model": "free-tier-master",
                    "messages": [{"role": "user", "content": "Ping"}],
                },
            )

            assert response.status_code == 200
            assert response.json()["choices"][0]["message"]["content"] == "Hello from GitHub Models gpt-4o!"

            gh_req = captured_requests[0]
            assert "models.inference.ai.azure.com" in str(gh_req.url)
            assert gh_req.headers.get("authorization") == f"Bearer {cfg['keys']['github']}"
            req_body = json.loads(gh_req.content.decode("utf-8"))
            assert req_body.get("model") == "gpt-4o"


@pytest.mark.anyio
async def test_fallback_routing_streaming_mode():
    """
    Stress Test: Verify fallback behavior in streaming mode (stream=True).
    When P1 fails (HTTP 429), P2 connects as SSE stream and yields chunks.
    """
    call_log = []

    mock_config = {
        "host": "127.0.0.1",
        "port": 5005,
        "cooldown_seconds": 60,
        "timeout_seconds": 10.0,
        "keys": {
            "key1": "token-p1",
            "key2": "token-p2",
        },
        "upstreams": [
            {
                "priority": 1,
                "id": "upstream-stream-fail",
                "display_name": "Stream Fail",
                "provider": "generic",
                "models": ["model-p1"],
                "base_url": "https://api.stream1.test/v1/chat/completions",
                "key_name": "key1",
            },
            {
                "priority": 2,
                "id": "upstream-stream-ok",
                "display_name": "Stream OK",
                "provider": "generic",
                "models": ["model-p2"],
                "base_url": "https://api.stream2.test/v1/chat/completions",
                "key_name": "key2",
            },
        ],
    }

    async def mock_send(self, req: httpx.Request, stream=False, *args, **kwargs):
        url = str(req.url)
        call_log.append(url)
        if "api.stream1.test" in url:
            return _build_mock_http_response(429, {"error": "Rate limit"}, req)
        elif "api.stream2.test" in url:
            # Return streaming SSE response
            async def aiter():
                yield b'data: {"choices": [{"delta": {"content": "Chunk 1"}}]}\n\n'
                yield b'data: {"choices": [{"delta": {"content": "Chunk 2"}}]}\n\n'
                yield b'data: [DONE]\n\n'

            resp = httpx.Response(
                status_code=200,
                headers={"Content-Type": "text/event-stream"},
                request=req,
            )
            resp.aiter_bytes = aiter
            return resp
        return _build_mock_http_response(500, {}, req)

    with patch("proxy.free_tier_proxy.get_config", return_value=mock_config):
        with patch.object(httpx.AsyncClient, "send", new=mock_send):
            client = TestClient(app)
            response = client.post(
                "/v1/chat/completions",
                json={
                    "model": "free-tier-master",
                    "stream": True,
                    "messages": [{"role": "user", "content": "Stream test"}],
                },
            )

            assert response.status_code == 200
            assert "text/event-stream" in response.headers.get("content-type", "")
            assert "Stream OK (model-p2)" in response.headers.get("X-Served-By", "")
            body_text = response.text
            assert "Chunk 1" in body_text
            assert "Chunk 2" in body_text

            # Verify P1 was tried first, then P2
            assert len(call_log) == 2
            assert "api.stream1.test" in call_log[0]
            assert "api.stream2.test" in call_log[1]


def test_parameter_sanitization_across_all_configured_providers():
    """
    Stress Test: Verify PayloadCompactor parameter sanitization across all 10 target providers.
    Asserts frequency_penalty and presence_penalty are stripped, and max_tokens is clamped <= 8192.
    """
    compactor = PayloadCompactor()
    test_providers = [
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
    ]

    for p in test_providers:
        raw_body = {
            "model": "test-model",
            "frequency_penalty": 0.8,
            "presence_penalty": 0.6,
            "max_tokens": 16384,
            "messages": [{"role": "user", "content": "Hello"}],
        }
        sanitized = compactor.sanitize_parameters(raw_body, provider=p, target_model="test-model")
        assert "frequency_penalty" not in sanitized, f"Provider {p} failed to strip frequency_penalty"
        assert "presence_penalty" not in sanitized, f"Provider {p} failed to strip presence_penalty"
        assert sanitized.get("max_tokens") == 8192, f"Provider {p} failed to clamp max_tokens to 8192"


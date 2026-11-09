"""
Test Suite: Micro-Proxy Non-Destructive Payload Compaction & Network Binding
Milestone 3 — Svartulfr Verse Production Evolution
"""

import os
import json
import copy
import urllib.request
import pytest
from starlette.testclient import TestClient

from proxy.free_tier_proxy import (
    app,
    get_config,
    PayloadCompactor,
    sanitize_request_body,
    deduplicate_wyvern_prompt,
)

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "proxy",
    "config_free_proxy.json",
)


@pytest.fixture
def compactor():
    return PayloadCompactor()


@pytest.fixture
def sample_bloated_wyvern_payload():
    """
    A realistic bloated Wyvern context payload representing an active turn in Svartulfr Verse.
    Includes duplicate NPC dossiers, duplicate locations, duplicate items,
    empty tags (<special_stats></special_stats>, <outfit name=""></outfit>),
    empty attributes (labels=""), cascading newlines (\n\n\n\n\n), trailing spaces,
    and unsupported parameters (frequency_penalty: 0.0, presence_penalty: 0.0, top_k: 0, stop with Narrator).
    """
    return {
        "model": "free-tier-master",
        "stream": False,
        "max_tokens": 16384,
        "temperature": 0.75,
        "top_p": 0.95,
        "top_k": 0,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "stop": ["\nNarrator:", "\nUser:", "\nAssistant:"],
        "messages": [
            {
                "role": "system",
                "content": (
                    "[MANDATORY LANGUAGE DIRECTIVE: Rispondi sempre in italiano standard, terza persona presente.]   \n\n"
                    "Sei il Game Master dell'universo narrativo Svartulfr Verse. Mantieni tono maturo, descrizioni sensoriali crude, rispetto rigoroso del canone.\n\n"
                    "I demi-umani possiedono un solo paio di orecchie: quelle animali. Non hanno orecchie umane.\n\n\n\n\n"
                    "<world_context position=\"before\" count=\"6\">\n"
                    "<npc name=\"Jasper Douglas\" labels=\"\">\n"
                    "[NAME: Jasper Douglas; SPECIES: Werewolf Demi-Human; AGE: 20 (Born 2004-04-12); HEIGHT: 193 cm (6' 4\"); ROLE: Student / Hacker; PACK: Douglas Bloodmoon]\n"
                    "BACKSTORY: Jasper is the twin brother of Alyssa. Brilliant tech specialist and hacker at SUCC.\n"
                    "FAMILY & PACK: Twin sister Alyssa, father Erik, eldest brother Malachia, politician brother Noah.\n"
                    "VOICE & BEHAVIOR: Quiet, analytical, fiercely protective of Alyssa.\n"
                    "THE WEIGHT HE CARRIES: Balances tech genius with primal beast instincts.\n"
                    "<special_stats></special_stats>\n"
                    "</npc>\n\n\n"
                    "<location name=\"Villa Douglas\" labels=\"\">\n"
                    "La tenuta della Casata Douglas si estende sulle colline di Seven Hills, protetta da potenti rune difensive.\n"
                    "</location>\n\n\n"
                    "<location name=\"Villa Douglas\">\n"
                    "La tenuta della Casata Douglas si estende sulle colline di Seven Hills, protetta da potenti rune difensive.\n"
                    "</location>\n\n\n"
                    "<location name=\"The Verve\">\n"
                    "Secret bar e lounge esclusivo situato sul retro del Logan's Custom Garage.\n"
                    "</location>\n\n\n"
                    "<item name=\"Ambrosia Vial\">\n"
                    "Fiala contenente Ambrosia distillata dai laboratori del dottor Sinclair.\n"
                    "</item>\n\n\n"
                    "<item name=\"Ambrosia Vial\">\n"
                    "Fiala contenente Ambrosia distillata dai laboratori del dottor Sinclair.\n"
                    "</item>\n\n\n"
                    "<creature name=\"Asag Beast\">\n"
                    "Creatura abissale generata dalle faglie del Voidspace.\n"
                    "</creature>\n\n\n"
                    "<lore_entry name=\"Ecologia LSE\">\n"
                    "I licantropi LSE mantengono una gerarchia rigida basata sulla forza e sull'antico patto di sangue.\n"
                    "</lore_entry>\n\n\n"
                    "<npc name=\"Finnegan Novak\">\n"
                    "[NAME: Finnegan Novak; SPECIES: Arctic Wolf Demi-Human; AGE: 20; ROLE: SUCC Student; PACK: None]\n"
                    "BACKSTORY: Finnegan is a loyal childhood friend of the twins.\n"
                    "FAMILY & PACK: Independent civilian.\n"
                    "VOICE & BEHAVIOR: Warm, calm, dependable.\n"
                    "</npc>\n"
                    "<special_stats>\n   \n</special_stats>\n"
                    "<outfit name=\"\"></outfit>\n"
                    "</world_context>\n\n\n\n\n"
                    "<character name=\"Jasper Douglas\">\n"
                    "[NAME: Jasper Douglas; SPECIES: Werewolf Demi-Human; AGE: 20 (Born 2004-04-12); HEIGHT: 193 cm (6' 4\"); ROLE: Student / Hacker; PACK: Douglas Bloodmoon]\n"
                    "BACKSTORY: Jasper is the twin brother of Alyssa. Brilliant tech specialist and hacker at SUCC.\n"
                    "FAMILY & PACK: Twin sister Alyssa, father Erik, eldest brother Malachia, politician brother Noah.\n"
                    "VOICE & BEHAVIOR: Quiet, analytical, fiercely protective of Alyssa.\n"
                    "THE WEIGHT HE CARRIES: Balances tech genius with primal beast instincts.\n"
                    "</character>\n\n\n\n\n"
                    "<user_persona name=\"Alyssa Douglas\">\n"
                    "[NAME: Alyssa Douglas; SPECIES: Werewolf Demi-Human; AGE: 20 (Born 2004-04-12); HEIGHT: 155 cm (5' 1\"); ROLE: Pre-Med Student / Pack Healer; PACK: Douglas Bloodmoon]\n"
                    "BACKSTORY: Alyssa is Jasper's twin sister. Gentle healer with devastating lunar magic.\n"
                    "FAMILY & PACK: Twin brother Jasper, father Erik, brothers Malachia and Noah.\n"
                    "VOICE & BEHAVIOR: Empathetic, determined, protective of her brother.\n"
                    "</user_persona>\n\n\n\n\n"
                    "<story_so_far>\n"
                    "La notte è calma a Seven Hills. I gemelli sono nella loro stanza a pianificare la missione.\n"
                    "</story_so_far>   \n\n\n\n"
                ),
            },
            {
                "role": "user",
                "content": '=>Alyssa: "Jasper, hai finito di analizzare quel segnale dei Sinners?"',
            },
            {
                "role": "assistant",
                "content": '=>Jasper: "Quasi. Il firewall di Sinclair è più complesso del previsto, ma sto isolando il nodo."',
            },
            {
                "role": "user",
                "content": '=>Alyssa: "Fai attenzione. Non vogliamo attirare l\'attenzione di Erik o Malachia stanotte."',
            },
        ],
    }


# =========================================================================
# TEST 1: Network Configuration & Loopback Binding Verification
# =========================================================================

def test_config_network_host_binding():
    """Test 1: Verify config_free_proxy.json specifies 'host': '127.0.0.1' and port 5005."""
    assert os.path.exists(CONFIG_PATH), f"Config file not found at {CONFIG_PATH}"
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    assert cfg.get("host") == "127.0.0.1", (
        f"Security violation: host must be '127.0.0.1', found '{cfg.get('host')}'"
    )
    assert int(cfg.get("port", 0)) == 5005, (
        f"Port mismatch: expected 5005, found {cfg.get('port')}"
    )

    # Verify cached config loader reflects 127.0.0.1
    runtime_cfg = get_config()
    assert runtime_cfg.get("host") == "127.0.0.1"


# =========================================================================
# TEST 2: PayloadCompactor Executes 5 Phases with 15% to 35% Reduction
# =========================================================================

def test_payload_compactor_executes_all_phases_and_achieves_reduction(
    compactor, sample_bloated_wyvern_payload
):
    """
    Test 2: Verify PayloadCompactor executes all 5 phases on realistic bloated payload,
    achieving 15% to 35% character reduction.
    """
    original_copy = copy.deepcopy(sample_bloated_wyvern_payload)
    init_chars = sum(
        len(m.get("content", ""))
        for m in sample_bloated_wyvern_payload["messages"]
        if isinstance(m.get("content"), str)
    )

    # Execute full compaction for google / gemini
    compacted = compactor.compact_request_payload(
        sample_bloated_wyvern_payload, provider="google", target_model="gemini-4-argon"
    )

    comp_chars = sum(
        len(m.get("content", ""))
        for m in compacted["messages"]
        if isinstance(m.get("content"), str)
    )

    chars_saved = init_chars - comp_chars
    reduction_pct = (chars_saved / init_chars) * 100.0

    print(
        f"\n[BENCHMARK] Initial: {init_chars} chars, Compacted: {comp_chars} chars, "
        f"Saved: {chars_saved} chars ({reduction_pct:.2f}% reduction)"
    )

    # 1. Verify reduction is within 15% to 35%
    assert 15.0 <= reduction_pct <= 35.0, (
        f"Expected reduction between 15% and 35%, got {reduction_pct:.2f}% "
        f"(saved {chars_saved}/{init_chars} chars)"
    )

    # 2. Verify Phase 1 (Parameter Sanitization)
    assert "frequency_penalty" not in compacted
    assert "presence_penalty" not in compacted
    assert "top_k" not in compacted
    assert compacted.get("max_tokens") <= 8192
    assert "stop" in compacted
    assert all("narrator" not in s.lower() for s in compacted["stop"])

    # 3. Verify Phase 2 & 3 (XML Lore Dedup & Active Char Dedup)
    sys_msg = compacted["messages"][0]["content"]

    # Jasper was active character in <character>, so duplicate <npc name="Jasper Douglas"> must be removed from <world_context>
    assert '<npc name="Jasper Douglas"' not in sys_msg
    # Location "Villa Douglas" must appear exactly once
    assert sys_msg.count('<location name="Villa Douglas"') == 1
    # Item "Ambrosia Vial" must appear exactly once
    assert sys_msg.count('<item name="Ambrosia Vial"') == 1
    # Non-active NPC Finnegan Novak must remain
    assert '<npc name="Finnegan Novak"' in sys_msg

    # 4. Verify Phase 4 (Empty Tag & Attribute Pruning)
    assert "<special_stats>" not in sys_msg
    assert "</special_stats>" not in sys_msg
    assert '<outfit name="">' not in sys_msg
    assert 'labels=""' not in sys_msg

    # 5. Verify Phase 5 (Whitespace & Newlines Collapsing)
    assert "\n\n\n" not in sys_msg, "Found 3+ consecutive newlines in compacted text"
    for line in sys_msg.splitlines():
        assert not line.endswith(" "), f"Found trailing space on line: '{line}'"

    # 6. Verify Upfront Deep Copy (Original input payload was NOT mutated in-place)
    assert sample_bloated_wyvern_payload == original_copy, (
        "Original payload dictionary was mutated during compaction!"
    )


# =========================================================================
# TEST 3: Zero Semantic Loss Invariant
# =========================================================================

def test_zero_semantic_loss_invariant(compactor, sample_bloated_wyvern_payload):
    """
    Test 3: Verify Zero Semantic Loss — assert that all character names, personality brackets,
    backstory sentences, dialogue examples, and rules are retained byte-for-byte in compacted output.
    """
    compacted = compactor.compact_request_payload(sample_bloated_wyvern_payload)

    full_compacted_text = "\n".join(
        m.get("content", "")
        for m in compacted["messages"]
        if isinstance(m.get("content"), str)
    )

    # 1. Critical Rules & System Directives must be preserved byte-for-byte
    assert "[MANDATORY LANGUAGE DIRECTIVE: Rispondi sempre in italiano standard, terza persona presente.]" in full_compacted_text
    assert "Sei il Game Master dell'universo narrativo Svartulfr Verse. Mantieni tono maturo, descrizioni sensoriali crude, rispetto rigoroso del canone." in full_compacted_text
    assert "I demi-umani possiedono un solo paio di orecchie: quelle animali. Non hanno orecchie umane." in full_compacted_text

    # 2. Active Character JED+ Dossier in <character> must be preserved byte-for-byte
    assert "<character name=\"Jasper Douglas\">" in full_compacted_text
    assert "[NAME: Jasper Douglas; SPECIES: Werewolf Demi-Human; AGE: 20 (Born 2004-04-12); HEIGHT: 193 cm (6' 4\"); ROLE: Student / Hacker; PACK: Douglas Bloodmoon]" in full_compacted_text
    assert "BACKSTORY: Jasper is the twin brother of Alyssa. Brilliant tech specialist and hacker at SUCC." in full_compacted_text
    assert "FAMILY & PACK: Twin sister Alyssa, father Erik, eldest brother Malachia, politician brother Noah." in full_compacted_text
    assert "VOICE & BEHAVIOR: Quiet, analytical, fiercely protective of Alyssa." in full_compacted_text
    assert "THE WEIGHT HE CARRIES: Balances tech genius with primal beast instincts." in full_compacted_text

    # 3. User Persona JED+ Dossier in <user_persona> must be preserved byte-for-byte
    assert "<user_persona name=\"Alyssa Douglas\">" in full_compacted_text
    assert "[NAME: Alyssa Douglas; SPECIES: Werewolf Demi-Human; AGE: 20 (Born 2004-04-12); HEIGHT: 155 cm (5' 1\"); ROLE: Pre-Med Student / Pack Healer; PACK: Douglas Bloodmoon]" in full_compacted_text
    assert "BACKSTORY: Alyssa is Jasper's twin sister. Gentle healer with devastating lunar magic." in full_compacted_text
    assert "FAMILY & PACK: Twin brother Jasper, father Erik, brothers Malachia and Noah." in full_compacted_text
    assert "VOICE & BEHAVIOR: Empathetic, determined, protective of her brother." in full_compacted_text

    # 4. Non-active NPC Finnegan Novak must be preserved byte-for-byte
    assert "<npc name=\"Finnegan Novak\">" in full_compacted_text
    assert "[NAME: Finnegan Novak; SPECIES: Arctic Wolf Demi-Human; AGE: 20; ROLE: SUCC Student; PACK: None]" in full_compacted_text
    assert "BACKSTORY: Finnegan is a loyal childhood friend of the twins." in full_compacted_text
    assert "VOICE & BEHAVIOR: Warm, calm, dependable." in full_compacted_text

    # 5. Lore, Locations, and Items preserved byte-for-byte
    assert "La tenuta della Casata Douglas si estende sulle colline di Seven Hills, protetta da potenti rune difensive." in full_compacted_text
    assert "Secret bar e lounge esclusivo situato sul retro del Logan's Custom Garage." in full_compacted_text
    assert "Fiala contenente Ambrosia distillata dai laboratori del dottor Sinclair." in full_compacted_text
    assert "Creatura abissale generata dalle faglie del Voidspace." in full_compacted_text
    assert "I licantropi LSE mantengono una gerarchia rigida basata sulla forza e sull'antico patto di sangue." in full_compacted_text
    assert "La notte è calma a Seven Hills. I gemelli sono nella loro stanza a pianificare la missione." in full_compacted_text

    # 6. Dialogue turns preserved byte-for-byte
    assert '=>Alyssa: "Jasper, hai finito di analizzare quel segnale dei Sinners?"' in full_compacted_text
    assert '=>Jasper: "Quasi. Il firewall di Sinclair è più complesso del previsto, ma sto isolando il nodo."' in full_compacted_text
    assert '=>Alyssa: "Fai attenzione. Non vogliamo attirare l\'attenzione di Erik o Malachia stanotte."' in full_compacted_text

    # 7. Quotation marks and dialogue syntax integrity
    raw_quotes = sum(m.get("content", "").count('"') for m in sample_bloated_wyvern_payload["messages"])
    # Compacted quotes: exactly same dialogue quotes (note: empty labels="" attributes were pruned, so only dialogue quotes remain)
    dialogue_quotes = (
        'Jasper, hai finito di analizzare quel segnale dei Sinners?'.count('"') +
        'Quasi. Il firewall di Sinclair è più complesso del previsto, ma sto isolando il nodo.'.count('"') +
        'Fai attenzione. Non vogliamo attirare l\'attenzione di Erik o Malachia stanotte.'.count('"') + 6
    )
    compacted_quotes = full_compacted_text.count('"')
    assert compacted_quotes >= dialogue_quotes


# =========================================================================
# TEST 4: Live & TestClient Startup Test (/health and /v1/models)
# =========================================================================

def test_fastapi_testclient_health_and_models():
    """Test 4a: Verify proxy FastAPI application responds on /health and /v1/models via TestClient."""
    client = TestClient(app)

    # GET /health
    health_resp = client.get("/health")
    assert health_resp.status_code == 200
    health_json = health_resp.json()
    assert health_json.get("status") == "ok"
    assert "active_cooldowns" in health_json
    assert "log_file" in health_json

    # GET /v1/models
    models_resp = client.get("/v1/models")
    assert models_resp.status_code == 200
    models_json = models_resp.json()
    assert models_json.get("object") == "list"
    assert any(m.get("id") == "free-tier-master" for m in models_json.get("data", []))


def test_live_network_health_endpoint():
    """
    Test 4b: Verify live loopback endpoint http://127.0.0.1:5005/health.
    If the service is already running on the host machine, asserts 200 OK directly.
    """
    try:
        req = urllib.request.Request(
            "http://127.0.0.1:5005/health", headers={"User-Agent": "TestVerifier"}
        )
        with urllib.request.urlopen(req, timeout=3.0) as resp:
            assert resp.status == 200
            data = json.loads(resp.read().decode("utf-8"))
            assert data.get("status") == "ok"
            print("\n[LIVE SERVER] http://127.0.0.1:5005/health is live and responded status: ok")
    except urllib.error.URLError as e:
        # If server is not running on 5005 at test time, TestClient test (4a) guarantees correctness
        pytest.skip(f"Live server not bound on 5005: {e}")


# =========================================================================
# TEST 5: Individual Phase Isolation Tests
# =========================================================================

def test_phase1_chutes_top_k(compactor):
    """Verify Chutes provider sets top_k = -1 and removes penalties."""
    body = {
        "model": "zai-org/GLM-5.1-TEE",
        "top_k": 50,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
    }
    sanitized = compactor.sanitize_parameters(body, provider="chutes")
    assert sanitized["top_k"] == -1
    assert "frequency_penalty" not in sanitized
    assert "presence_penalty" not in sanitized


def test_phase1_gemini_max_tokens_clamp(compactor):
    """Verify Google / Gemini provider clamps max_tokens to 8192."""
    body = {
        "model": "gemini-4-argon",
        "max_tokens": 16000,
        "frequency_penalty": 0.5,
        "presence_penalty": 0.5,
    }
    sanitized = compactor.sanitize_parameters(body, provider="google")
    assert sanitized["max_tokens"] == 8192
    assert "frequency_penalty" not in sanitized
    assert "presence_penalty" not in sanitized


def test_phase1_narrator_stop_sequence_strip(compactor):
    """Verify \\nNarrator: stop sequence is stripped to prevent truncated turns."""
    body = {
        "stop": ["\nNarrator:", "\nNarratore:", "\nStopSequence:"]
    }
    sanitized = compactor.sanitize_parameters(body)
    assert sanitized["stop"] == ["\nStopSequence:"]


def test_phase2_xml_lore_deduplication(compactor):
    """Verify generic XML lore deduplication across multiple entry types."""
    messages = [
        {
            "role": "system",
            "content": (
                '<npc name="Erik Douglas">\n[NAME: Erik Douglas]\n</npc>\n'
                '<npc name="Erik Douglas">\n[NAME: Erik Douglas duplicate]\n</npc>\n'
                '<location name="Seven Hills">\nSeven Hills Residence\n</location>\n'
                '<location name="Seven Hills">\nSeven Hills Residence duplicate\n</location>\n'
                '<item name="Runic Blade">\nRunic weapon\n</item>\n'
                '<item name="Runic Blade">\nRunic weapon duplicate\n</item>\n'
            ),
        }
    ]
    deduped, saved = compactor.deduplicate_xml_lore(messages)
    content = deduped[0]["content"]
    assert content.count('<npc name="Erik Douglas">') == 1
    assert content.count('<location name="Seven Hills">') == 1
    assert content.count('<item name="Runic Blade">') == 1
    assert saved > 0


def test_phase3_active_character_cross_dedup(compactor):
    """Verify NPC duplicate of active character is removed, while other NPCs remain."""
    messages = [
        {
            "role": "system",
            "content": (
                '<world_context>\n'
                '<npc name="Malachia Douglas Bloodmoon">\n[NAME: Malachia Douglas Bloodmoon; 208 cm]\n</npc>\n'
                '<npc name="Noah Douglas Bloodmoon">\n[NAME: Noah Douglas Bloodmoon; 197 cm]\n</npc>\n'
                '</world_context>\n'
                '<character name="Malachia Douglas Bloodmoon">\n'
                '[NAME: Malachia Douglas Bloodmoon; SPECIES: Werewolf Demi-Human; 208 cm]\n'
                '</character>\n'
            ),
        }
    ]
    res, saved = compactor.cross_deduplicate_active_characters(messages)
    content = res[0]["content"]

    # Malachia was in <character>, so his duplicate in <world_context> is removed
    assert '<npc name="Malachia Douglas Bloodmoon"' not in content
    # Noah was NOT in <character>, so his NPC entry remains
    assert '<npc name="Noah Douglas Bloodmoon"' in content
    # Malachia in <character> remains intact
    assert '<character name="Malachia Douglas Bloodmoon">' in content
    assert saved > 0


def test_phase4_empty_tag_and_attribute_pruning(compactor):
    """Verify nested empty tags and empty attributes are pruned."""
    messages = [
        {
            "role": "system",
            "content": (
                '<npc name="Erik" labels="" type="">\n'
                '<special_stats>\n  \n</special_stats>\n'
                '<outfit name=""></outfit>\n'
                'Content here.\n'
                '</npc>'
            ),
        }
    ]
    res, saved = compactor.prune_empty_tags_and_attributes(messages)
    content = res[0]["content"]
    assert 'labels=""' not in content
    assert 'type=""' not in content
    assert "<special_stats>" not in content
    assert "<outfit" not in content
    assert "Content here." in content
    assert saved > 0


def test_phase5_whitespace_collapsing_and_message_merging(compactor):
    """Verify 3+ newlines collapsed to 2, trailing whitespace stripped, consecutive roles merged."""
    messages = [
        {"role": "user", "content": "First instruction.   \n\n\n\n\nSecond line.   "},
        {"role": "user", "content": "Third instruction."},
    ]
    res, saved = compactor.collapse_whitespace(messages)
    assert len(res) == 1  # Merged consecutive user messages
    content = res[0]["content"]
    assert "\n\n\n" not in content
    for line in content.splitlines():
        assert not line.endswith(" ")
    assert "First instruction." in content
    assert "Second line." in content
    assert "Third instruction." in content


def test_deep_copy_prevents_failover_loop_mutation(compactor):
    """Verify caller's dictionary is never modified during compaction or failover preparation."""
    raw_payload = {
        "model": "free-tier-master",
        "messages": [{"role": "user", "content": "Test prompt"}],
        "top_k": 0,
        "frequency_penalty": 0.0,
    }
    raw_backup = copy.deepcopy(raw_payload)

    # Run base compaction
    compacted_base = compactor.compact_request_payload(raw_payload)
    assert raw_payload == raw_backup, "Base compaction mutated raw input!"

    # Simulate multi-upstream failover loop
    providers = [
        ("google", "gemini-4-argon"),
        ("chutes", "zai-org/GLM-5.1-TEE"),
        ("openrouter", "z-ai/glm-5.1"),
    ]
    for prov, model in providers:
        provider_payload = compactor.prepare_for_provider(compacted_base, prov, model)
        assert provider_payload["model"] == model
        if prov == "chutes":
            assert provider_payload["top_k"] == -1
        assert raw_payload == raw_backup, f"Provider preparation for {prov} mutated raw input!"

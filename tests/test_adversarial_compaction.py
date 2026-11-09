"""
tests/test_adversarial_compaction.py

Empirical Adversarial Stress Suite for PayloadCompactor in proxy/free_tier_proxy.py.
Milestone 3 — Svartulfr Verse Production Evolution.

Stress Dimensions:
1. Malformed and adversarial XML (deeply nested, unclosed, attribute injection, special chars).
2. Markdown preservation (code blocks, indents, tables, lists).
3. Dialogue & quote preservation (escaped quotes, foreign language parentheticals).
4. Substring and name collision stress (sub-words, prefixes, shared first names).
5. Extreme repetition & pathological empty tags (100+ duplicates, nested empty tags).
6. Compaction reduction benchmarks (15% - 35% on bloated payloads, 0% semantic loss on lean payloads).
7. Network host loopback verification (127.0.0.1).
"""

import os
import re
import json
import copy
import pytest
from proxy.free_tier_proxy import PayloadCompactor, get_config

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "proxy",
    "config_free_proxy.json",
)


@pytest.fixture
def compactor():
    return PayloadCompactor()


# =========================================================================
# 1. NETWORK & HOST ISOLATION CHALLENGE
# =========================================================================

def test_network_host_isolation():
    """Verify that proxy/config_free_proxy.json strictly binds to 127.0.0.1 (loopback only)."""
    assert os.path.exists(CONFIG_PATH)
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    assert cfg.get("host") == "127.0.0.1", f"Host must be 127.0.0.1, got: {cfg.get('host')}"
    assert cfg.get("port") == 5005, f"Port must be 5005, got: {cfg.get('port')}"
    assert get_config().get("host") == "127.0.0.1"


# =========================================================================
# 2. MALFORMED, NESTED, AND SPECIAL XML TAGS
# =========================================================================

def test_unclosed_xml_tags_no_crash_and_preserved(compactor):
    """
    Adversarial Challenge: Unclosed XML tags must NOT crash the compactor,
    must NOT cause exponential regex backtracking, and content must be preserved.
    """
    unclosed_payload = {
        "messages": [
            {
                "role": "system",
                "content": (
                    "<world_context>\n"
                    "<npc name=\"Unclosed NPC\">\n"
                    "[NAME: Unclosed NPC; SPECIES: Wolf Demi-Human]\n"
                    "BACKSTORY: This tag was never closed.\n"
                    "<location name=\"Half Open\">\n"
                    "Some description without closing tag.\n"
                    "Normal story text continues here.\n"
                ),
            }
        ]
    }
    compacted = compactor.compact_request_payload(unclosed_payload)
    out_text = compacted["messages"][0]["content"]

    # Assert no crash and zero semantic loss of the unclosed content
    assert "Unclosed NPC" in out_text
    assert "This tag was never closed." in out_text
    assert "Half Open" in out_text
    assert "Normal story text continues here." in out_text


def test_special_characters_in_xml_attributes(compactor):
    """
    Adversarial Challenge: XML attributes with escaped quotes, single quotes,
    ampersands, and special characters must not break attribute parsing or tag identification.
    """
    payload = {
        "messages": [
            {
                "role": "system",
                "content": (
                    '<npc name="Erik &amp; Sons" title=\'Alpha\' id="ID_123#@!">\n'
                    '[NAME: Erik &amp; Sons; PACK: Douglas]\n'
                    '</npc>\n\n'
                    '<npc name="Erik &amp; Sons" title=\'Alpha\' id="ID_123#@!">\n'
                    '[NAME: Erik &amp; Sons; PACK: Douglas duplicate]\n'
                    '</npc>\n'
                ),
            }
        ]
    }
    compacted = compactor.compact_request_payload(payload)
    out_text = compacted["messages"][0]["content"]

    # Should deduplicate the second tag cleanly without crashing
    assert out_text.count('name="Erik &amp; Sons"') == 1
    assert "Erik &amp; Sons" in out_text


def test_nested_xml_tags_handling(compactor):
    """
    Adversarial Challenge: Nested tags with same name.
    Verify that nested tags do not produce unhandled exceptions or regex runaway.
    """
    payload = {
        "messages": [
            {
                "role": "system",
                "content": (
                    '<lore_entry name="Outer">\n'
                    'Outer content start.\n'
                    '<lore_entry name="Inner">\n'
                    'Inner content.\n'
                    '</lore_entry>\n'
                    'Outer content end.\n'
                    '</lore_entry>\n'
                ),
            }
        ]
    }
    compacted = compactor.compact_request_payload(payload)
    out_text = compacted["messages"][0]["content"]

    # Verify content survived
    assert "Inner content." in out_text
    assert "Outer content" in out_text


# =========================================================================
# 3. MARKDOWN FORMATTING & CODE BLOCKS PRESERVATION
# =========================================================================

def test_markdown_code_blocks_and_indentation_preservation(compactor):
    """
    Adversarial Challenge: Triple-backtick code blocks with significant indentation,
    python functions, and ascii art must NOT have their leading indentation stripped.
    """
    code_block = (
        "Here is the hacking script Jasper used:\n\n"
        "```python\n"
        "def bypass_sinclair_firewall(node_ip: str) -> bool:\n"
        "    sock = socket.socket()\n"
        "    for attempt in range(3):\n"
        "        if sock.connect_ex((node_ip, 8080)) == 0:\n"
        "            return True\n"
        "    return False\n"
        "```\n\n"
        "End of script."
    )
    payload = {"messages": [{"role": "user", "content": code_block}]}
    compacted = compactor.compact_request_payload(payload)
    out_text = compacted["messages"][0]["content"]

    # Assert exact indentation preserved
    assert "```python" in out_text
    assert "    sock = socket.socket()" in out_text
    assert "        if sock.connect_ex((node_ip, 8080)) == 0:" in out_text
    assert "            return True" in out_text
    assert "```" in out_text


def test_markdown_tables_and_lists_preservation(compactor):
    """
    Adversarial Challenge: Markdown tables and multi-level indented lists
    must retain their structure, column delimiters (|), and list indents.
    """
    table_and_lists = (
        "### S.P.E.C.I.A.L. Stat Check Results\n\n"
        "| Attribute | Score | Modifier | Roll (d20) | Result |\n"
        "| :--- | :---: | :---: | :---: | :--- |\n"
        "| Might (MGT) | 7 | +2 | 14 | Success (16 >= DC 15) |\n"
        "| Wit (WIT)   | 5 | +1 | 18 | Critical Success (19 >= DC 15) |\n\n"
        "Mission Objectives:\n"
        "* Infiltrate Sinclair's lab\n"
        "  * Avoid CCD patrol drones\n"
        "    * Hack perimeter sensors\n"
        "  * Extract Ambrosia sample\n"
        "* Rendezvous at The Verve"
    )
    payload = {"messages": [{"role": "user", "content": table_and_lists}]}
    compacted = compactor.compact_request_payload(payload)
    out_text = compacted["messages"][0]["content"]

    # Check table rows preserved
    assert "| Attribute | Score | Modifier | Roll (d20) | Result |" in out_text
    assert "| Might (MGT) | 7 | +2 | 14 | Success (16 >= DC 15) |" in out_text
    assert "| Wit (WIT)   | 5 | +1 | 18 | Critical Success (19 >= DC 15) |" in out_text

    # Check nested list indents preserved
    assert "* Infiltrate Sinclair's lab" in out_text
    assert "  * Avoid CCD patrol drones" in out_text
    assert "    * Hack perimeter sensors" in out_text
    assert "* Rendezvous at The Verve" in out_text


# =========================================================================
# 4. DIALOGUE, QUOTES, AND FOREIGN LANGUAGE PARENTHETICALS
# =========================================================================

def test_dialogue_quotes_and_foreign_parentheticals_preservation(compactor):
    """
    Adversarial Challenge: Verify that dialogue lines containing:
    - Standard double quotes (\"...\")
    - Foreign language parentheticals (\"Frase originale\" ([traduzione]))
    - Escaped quotes and Italian apostrophes (l'arma, dell'ambrosia, un'altra)
    are retained with 100% byte-for-byte fidelity.
    """
    dialogues = [
        '=>Erik: "Non fidarti mai di un Virtuoso, Jasper." ([Never trust a Virtuoso, Jasper.])',
        '=>Malachia: "L\'odore dell\'ambrosia è ovunque nel magazzino. Restami dietro."',
        '=>Jasper: "Ho isolato l\'interfaccia. Ha detto: \\"Accesso negato\\", ma ho trovato una backdoor."',
        '=>Alyssa: "Stai calmo. Non lascerò che ti feriscano di nuovo."',
    ]
    payload = {
        "messages": [
            {"role": "user", "content": dialogues[0]},
            {"role": "assistant", "content": dialogues[1]},
            {"role": "user", "content": dialogues[2]},
            {"role": "assistant", "content": dialogues[3]},
        ]
    }
    compacted = compactor.compact_request_payload(payload)
    msgs = compacted["messages"]

    # Each dialogue must be preserved byte-for-byte in the output
    full_text = "\n".join(m.get("content", "") for m in msgs)
    for dlg in dialogues:
        assert dlg in full_text, f"Dialogue line corrupted: {dlg}"


# =========================================================================
# 5. SUBSTRING AND ACTIVE CHARACTER COLLISION TESTING
# =========================================================================

def test_subword_character_names_not_falsely_stripped(compactor):
    """
    Adversarial Challenge: Verify that an active character with a short name (e.g. 'Ray')
    does NOT cause unrelated characters whose names contain that sub-word (e.g. 'Raymond Sinclair')
    to be falsely stripped.
    """
    payload = {
        "messages": [
            {
                "role": "system",
                "content": (
                    "<world_context>\n"
                    "<npc name=\"Raymond Sinclair\">\n"
                    "[NAME: Raymond Sinclair; SPECIES: Human; ROLE: Chemist]\n"
                    "BACKSTORY: Dr. Sinclair's cousin, unrelated to Ray.\n"
                    "</npc>\n"
                    "</world_context>\n"
                    "<character name=\"Ray\">\n"
                    "[NAME: Ray; SPECIES: Werewolf; ROLE: Scout]\n"
                    "</character>\n"
                ),
            }
        ]
    }
    compacted = compactor.compact_request_payload(payload)
    out_text = compacted["messages"][0]["content"]

    # Raymond Sinclair must NOT be deleted!
    assert "Raymond Sinclair" in out_text
    assert "Ray" in out_text


def test_reverse_subword_character_names_not_falsely_stripped(compactor):
    """
    Adversarial Challenge: If active character has a longer name ('Alexander'),
    an NPC with a shorter prefix name ('Alex') must NOT be stripped.
    """
    payload = {
        "messages": [
            {
                "role": "system",
                "content": (
                    "<world_context>\n"
                    "<npc name=\"Alex\">\n"
                    "[NAME: Alex; ROLE: Student]\n"
                    "</npc>\n"
                    "</world_context>\n"
                    "<character name=\"Alexander\">\n"
                    "[NAME: Alexander; ROLE: Professor]\n"
                    "</character>\n"
                ),
            }
        ]
    }
    compacted = compactor.compact_request_payload(payload)
    out_text = compacted["messages"][0]["content"]

    assert "<npc name=\"Alex\">" in out_text
    assert "<character name=\"Alexander\">" in out_text


def test_first_name_shared_between_different_characters_investigation(compactor):
    """
    Adversarial Investigation:
    In Svartulfr Verse, canon characters have full names ('Dominic Rogers' vs 'Dominic Chen',
    'Stanley Davies Jr.' vs 'Stanley Davies Sr.').
    Document how the compactor behaves when two distinct characters share the first name.
    """
    payload = {
        "messages": [
            {
                "role": "system",
                "content": (
                    "<world_context>\n"
                    "<npc name=\"Dominic Chen\">\n"
                    "[NAME: Dominic Chen; ROLE: Chemistry Lab tech]\n"
                    "</npc>\n"
                    "<npc name=\"Dominic Rogers\">\n"
                    "[NAME: Dominic Rogers; ROLE: Athlete]\n"
                    "</npc>\n"
                    "</world_context>\n"
                    "<character name=\"Dominic Rogers\">\n"
                    "[NAME: Dominic Rogers; ROLE: Athlete]\n"
                    "</character>\n"
                ),
            }
        ]
    }
    compacted = compactor.compact_request_payload(payload)
    out_text = compacted["messages"][0]["content"]

    # Active character in <character> must be preserved
    assert '<character name="Dominic Rogers">' in out_text

    # Duplicate NPC dossier for Dominic Rogers must be stripped
    assert '<npc name="Dominic Rogers">' not in out_text

    # Check whether Dominic Chen (different person) survived or was swept by first-name heuristic
    dominic_chen_survived = "Dominic Chen" in out_text
    print(f"\n[EMPIRICAL OBSERVATION] Dominic Chen survived: {dominic_chen_survived}")
    # Documented finding: When first_name is used in active_names, different characters sharing
    # the first name are treated as the active character and stripped from world_context.
    # We record this finding for the audit handoff.


# =========================================================================
# 6. EXTREME REPETITION & EMPTY TAG PRUNING STRESS
# =========================================================================

def test_extreme_repetition_100_identical_tags(compactor):
    """
    Adversarial Challenge: 100 identical <npc> tags.
    Must deduplicate down to exactly 1 instance, without quadratic performance degradation.
    """
    single_npc = (
        '<npc name="Repetitive Guard">\n'
        '[NAME: Repetitive Guard; ROLE: Security]\n'
        'Stationed at Seven Hills gates.\n'
        '</npc>\n\n'
    )
    content = "<world_context>\n" + (single_npc * 100) + "</world_context>\n"
    payload = {"messages": [{"role": "system", "content": content}]}

    compacted = compactor.compact_request_payload(payload)
    out_text = compacted["messages"][0]["content"]

    # Must contain exactly 1 occurrence of Repetitive Guard
    assert out_text.count('name="Repetitive Guard"') == 1
    assert "Repetitive Guard" in out_text


def test_pathological_empty_and_nested_tags_pruning(compactor):
    """
    Adversarial Challenge: Deeply nested empty tags and multiple empty attributes
    (<special_stats>, <outfit>, labels="", type="", etc.).
    """
    content = (
        "<world_context>\n"
        "<npc name=\"Erik Douglas\" labels=\"\" type=\"\" description=\"\" category=\"\" role=\"\" class=\"\">\n"
        "[NAME: Erik Douglas; SPECIES: Werewolf Demi-Human]\n"
        "<special_stats>\n   \n   \n</special_stats>\n"
        "<outfit name=\"\"></outfit>\n"
        "<empty_parent><empty_child><empty_leaf></empty_leaf></empty_child></empty_parent>\n"
        "Real backstory of Erik Douglas.\n"
        "</npc>\n"
        "</world_context>\n"
    )
    payload = {"messages": [{"role": "system", "content": content}]}
    compacted = compactor.compact_request_payload(payload)
    out_text = compacted["messages"][0]["content"]

    # Empty tags & empty attrs must be completely gone
    assert "<special_stats>" not in out_text
    assert "</special_stats>" not in out_text
    assert "<outfit" not in out_text
    assert "<empty_parent>" not in out_text
    assert "<empty_leaf>" not in out_text
    assert 'labels=""' not in out_text
    assert 'type=""' not in out_text

    # Real content must be intact
    assert "Erik Douglas" in out_text
    assert "Real backstory of Erik Douglas." in out_text


# =========================================================================
# 7. COMPACTION BENCHMARKS & TOKEN REDUCTION VERIFICATION
# =========================================================================

def test_production_bloat_compaction_reduction_benchmark(compactor):
    """
    Adversarial Benchmark: On a production-like bloated Wyvern prompt (6000+ chars),
    compaction must achieve between 15% and 35% character reduction while preserving
    all story and character facts.
    """
    # Build bloated prompt
    duplicate_npc = (
        '<npc name="Noah Douglas Bloodmoon" labels="">\n'
        '[NAME: Noah Douglas Bloodmoon; SPECIES: Werewolf Demi-Human; AGE: 22; HEIGHT: 197 cm (6\' 5.6"); ROLE: Student Council President / DCC Diplomat; PACK: Douglas Bloodmoon]\n'
        'BACKSTORY: Noah is the charismatic diplomat of the family, balancing politics with pack duties.\n'
        'FAMILY & PACK: Father Erik, brothers Malachia and Jasper, sister Alyssa.\n'
        'VOICE & BEHAVIOR: Eloquent, poised, calculating, fiercely protective of siblings.\n'
        '<special_stats>\n\n</special_stats>\n'
        '</npc>\n\n\n\n'
    )
    unique_npc = (
        '<npc name="Stanley Davies Jr.">\n'
        '[NAME: Stanley Davies Jr.; SPECIES: Golden Retriever Demi-Human; AGE: 20; ROLE: Student Athlete; PACK: None]\n'
        'BACKSTORY: Enthusiastic teammate of the Douglas brothers at SUCC.\n'
        'FAMILY & PACK: Civilian family.\n'
        'VOICE & BEHAVIOR: Cheerful, loyal, straightforward.\n'
        '</npc>\n\n\n'
    )
    locations = (
        '<location name="Seven Hills Residence" labels="">\n'
        'The fortified private estate of the Douglas family atop Seven Hills.\n'
        '</location>\n\n\n'
        '<location name="Seven Hills Residence">\n'
        'The fortified private estate of the Douglas family atop Seven Hills.\n'
        '</location>\n\n\n'
        '<location name="SUCC Campus">\n'
        'Solarton University of California Coast campus grounds.\n'
        '</location>\n\n\n'
        '<location name="SUCC Campus">\n'
        'Solarton University of California Coast campus grounds.\n'
        '</location>\n\n\n'
    )
    active_char = (
        '<character name="Noah Douglas Bloodmoon">\n'
        '[NAME: Noah Douglas Bloodmoon; SPECIES: Werewolf Demi-Human; AGE: 22; HEIGHT: 197 cm (6\' 5.6"); ROLE: Student Council President / DCC Diplomat; PACK: Douglas Bloodmoon]\n'
        'BACKSTORY: Noah is the charismatic diplomat of the family, balancing politics with pack duties.\n'
        'FAMILY & PACK: Father Erik, brothers Malachia and Jasper, sister Alyssa.\n'
        'VOICE & BEHAVIOR: Eloquent, poised, calculating, fiercely protective of siblings.\n'
        '</character>\n\n\n\n'
    )

    story_and_lore = (
        '<story_so_far>\n'
        'La notte avanza sulle colline di Seven Hills. La Casata Douglas è riunita per pianificare\n'
        'l\'infiltrazione nei magazzini del Sindacato dei Sinners presso il porto industriale.\n'
        '</story_so_far>\n\n'
        '<lore_entry name="Ecologia LSE">\n'
        'I licantropi LSE mantengono una gerarchia rigida basata sulla forza e sull\'antico patto di sangue.\n'
        '</lore_entry>\n\n'
        '<item name="Ambrosia Sample">\n'
        'Fiala contenente Ambrosia distillata dai laboratori clandestini.\n'
        '</item>\n\n'
        '<creature name="Shadow Beast">\n'
        'Creatura corpulenta generata dalle faglie del Voidspace.\n'
        '</creature>\n\n'
    )

    sys_content = (
        "[MANDATORY LANGUAGE DIRECTIVE: Rispondi sempre in italiano standard, terza persona presente.]   \n\n\n\n"
        "Sei il Game Master dell'universo narrativo Svartulfr Verse. Mantieni tono maturo, descrizioni sensoriali crude, rispetto rigoroso del canone.\n\n"
        "I demi-umani possiedono un solo paio di orecchie: quelle animali. Non hanno orecchie umane.\n\n"
        "<world_context>\n"
        + duplicate_npc
        + unique_npc
        + locations
        + story_and_lore
        + "</world_context>\n\n\n\n"
        + active_char
    )

    payload = {
        "model": "free-tier-master",
        "messages": [
            {"role": "system", "content": sys_content},
            {"role": "user", "content": '=>Alyssa: "Noah, hai visto Jasper?"   \n\n\n\n'},
            {"role": "user", "content": '=>Noah: "È nel suo laboratorio, come sempre."'},
            {"role": "assistant", "content": '=>Jasper: "Sto solo completando la decifrazione dei registri."'},
            {"role": "user", "content": '=>Alyssa: "Sbrighiamoci, Erik ci aspetta tra venti minuti."'},
        ],
    }

    initial_chars = sum(len(m.get("content", "")) for m in payload["messages"])
    compacted = compactor.compact_request_payload(payload)
    final_chars = sum(len(m.get("content", "")) for m in compacted["messages"])

    reduction_pct = ((initial_chars - final_chars) / initial_chars) * 100.0
    print(f"\n[BENCHMARK] Production Bloat: Initial: {initial_chars} chars -> Final: {final_chars} chars (-{reduction_pct:.2f}%)")

    # Assert reduction is within 15% to 35%
    assert 15.0 <= reduction_pct <= 35.0, (
        f"Compaction achieved {reduction_pct:.2f}%, expected between 15% and 35%."
    )

    # Assert consecutive user messages at start were merged into 1
    # Total messages: system, merged user 0+1, assistant, user 3 -> 4 messages
    assert len(compacted["messages"]) == 4


def test_heavy_duplicate_bloat_compaction_scaling(compactor):
    """
    Adversarial Benchmark: When a prompt is pathologically bloated with multiple duplicate
    NPCs and locations (>35% redundancy), verify that the compactor scales gracefully and
    reduces >35% without error or loss of unique data.
    """
    rep_location = (
        '<location name="Seven Hills Residence">\n'
        'The fortified private estate of the Douglas family atop Seven Hills.\n'
        '</location>\n\n'
    )
    content = "<world_context>\n" + (rep_location * 10) + "</world_context>\n"
    payload = {"messages": [{"role": "system", "content": content}]}

    initial_chars = sum(len(m.get("content", "")) for m in payload["messages"])
    compacted = compactor.compact_request_payload(payload)
    final_chars = sum(len(m.get("content", "")) for m in compacted["messages"])

    reduction_pct = ((initial_chars - final_chars) / initial_chars) * 100.0
    print(f"\n[BENCHMARK] Heavy Bloat Scaling: Initial: {initial_chars} chars -> Final: {final_chars} chars (-{reduction_pct:.2f}%)")
    assert reduction_pct >= 50.0, f"Expected >50% reduction on 10x duplicate, got {reduction_pct:.2f}%"



def test_lean_payload_zero_unintended_reduction(compactor):
    """
    Adversarial Invariant: On a clean, already-compacted payload,
    compactor must NOT delete any words, sentences, or tags.
    Reduction must be <= 1% (only trailing newline or space trimming).
    """
    lean_content = (
        "[MANDATORY LANGUAGE DIRECTIVE: Rispondi sempre in italiano standard, terza persona presente.]\n\n"
        "<world_context>\n"
        "<npc name=\"Finnegan Novak\">\n"
        "[NAME: Finnegan Novak; SPECIES: Arctic Wolf Demi-Human; AGE: 20; ROLE: Student]\n"
        "BACKSTORY: Loyal childhood friend.\n"
        "</npc>\n"
        "</world_context>\n\n"
        "<character name=\"Jasper Douglas\">\n"
        "[NAME: Jasper Douglas; SPECIES: Werewolf Demi-Human; AGE: 20; HEIGHT: 193 cm (6' 4\"); ROLE: Hacker]\n"
        "</character>"
    )
    payload = {
        "model": "free-tier-master",
        "messages": [
            {"role": "system", "content": lean_content},
            {"role": "user", "content": '=>Alyssa: "Pronto per la lezione?"'},
        ],
    }

    initial_chars = sum(len(m.get("content", "")) for m in payload["messages"])
    compacted = compactor.compact_request_payload(payload)
    final_chars = sum(len(m.get("content", "")) for m in compacted["messages"])

    reduction_pct = ((initial_chars - final_chars) / initial_chars) * 100.0

    # Must be virtually 0% reduction (less than 1% for whitespace normalize)
    assert reduction_pct <= 1.0, f"Unintended data loss on lean payload: -{reduction_pct:.2f}%"

    out_text = "\n".join(m.get("content", "") for m in compacted["messages"])
    assert "Finnegan Novak" in out_text
    assert "Loyal childhood friend." in out_text
    assert "Jasper Douglas" in out_text
    assert '=>Alyssa: "Pronto per la lezione?"' in out_text

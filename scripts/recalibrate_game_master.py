#!/usr/bin/env python3
"""
Recalibrate Svartulfr Game Master Assistant, Master Prompt Assembly, and SUCC Route Scenario.
Enforces M1 R1 (Slowburn Relationship Pacing) + R3 (Epistemic Isolation) + Canon Standards:
1. Chronological Passivity (Zero date reset to March 15, 2024; passive reading of native Wyvern clock).
2. Absolute Canon Grounding (OOC Narrator lookup, Pure Positive Framing, anti-hallucination).
3. Epistemic Isolation Gate & Firewall (OOC vs IC separation, phone/DM/thought opacity, unmet strangers).
4. Relationship Pacing Gate (Slow-burn realism, anti-insta-love, Arrow -> inline command syntax).
5. Zero Em-Dash invariant (\u2014) and idempotent Prompt Assembly block synchronization.
6. Safe deployment and GET read-back verification via wyvern_api_client (with scenario revision sync).
"""

import argparse
import copy
import json
import os
import pathlib
import re
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.wyvern_api_client import api_request, get_auth_token

ASST_FILE = pathlib.Path("FINAL/assistants/Svartulfr_Game_Master_Assistant.json")
PA_FILE = pathlib.Path("FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json")
PROMPT_FILE = PA_FILE
SCENARIO_FILE = pathlib.Path("FINAL/scenarios/Svartulfr_Scenario_SUCC_Route_Alyssa.json")

ASST_ID = "simple_assistant_EYQTtcgTQfwh2RH9RG8z3"
PA_ID = "pha_kWkWUAfTJTF9q72c2bC98"
PROMPT_ASSEMBLY_ID = PA_ID
SCENARIO_ID = "char_scenario_CKgwq246DyCj1NNTBV9rt"

GROUNDING_BLOCK_ID = "svartulfr_grounding_and_chronology"
USER_BOUNDARIES_BLOCK_ID = "svartulfr_user_boundaries"
CLOSER_BLOCK_ID = "svartulfr_italian_sandwich_closer"

NEGATIVE_EAR_PATTERNS = [
    re.compile(r"\bzero\s+human\s+ears\b", re.IGNORECASE),
    re.compile(r"\bno\s+human\s+ears\b", re.IGNORECASE),
    re.compile(r"\bsenza\s+orecchie\s+umane\b", re.IGNORECASE),
    re.compile(r"\bprive\s+di\s+orecchie\s+umane\b", re.IGNORECASE),
]

CHRONO_DIRECTIVE = """<chronological_passivity>
- WYVERN NATIVE CLOCK: The Game Master DOES NOT manage, invent, declare, or reset the in-game calendar date. Date and time progression are tracked natively by Wyvern's engine and the active scenario turn.
- FORBIDDEN DATES: Under NO circumstances generate, revert to, or force arbitrary or static boilerplate dates (including March 15, 2024 or any other fixed timestamp).
- PASSIVE INHERITANCE: If a temporal context or scene header is requested, solely read and reflect the current date and time established in the active scene history or Wyvern system state, advancing time naturally without overriding it.
</chronological_passivity>"""

GROUNDING_DIRECTIVE = """<absolute_canon_grounding>
- MANDATORY PRIOR LOOKUP (OOC NARRATOR ONLY): Before narrating actions, dialogue, reactions, or powers of any character or NPC, rigidly consult their XML entry (<character>, <user_persona>, <npc>, <lore_entry>) strictly as Out-of-Character (OOC) Narrator reference to keep canon accurate without leaking OOC sheets into in-character knowledge.
- FORBIDDEN HALLUCINATIONS: NEVER invent ranks, forms, powers, species traits, or family ties not explicitly stated in their JED+ sheet:
  * Pack Subgenders and Hierarchy: Erik is Prime Alpha (Alpha Command, Pack Leader); Malachia is Dominant Alpha (Pack Leader); Logan is Beta (mediator, blacksmith; zero Alpha Command); Jasper is Beta (technomancer/DJ; zero Alpha Command); Noah is Delta (diplomat, grey eminence; zero Alpha Command).
  * Demihuman Kemonomimi (e.g. Finn, Roman, Kolya): Demihumans possess a SINGLE pair of species-specific animal ears atop their skull and matching tail. They are NOT werewolves (no silver allergy, no lunar frenzy, no hybrid shift).
  * Sierra Cruz: Lamia with rainbow hair and a 4-meter iridescent rainbow serpent lower body. She has ZERO legs, ZERO feet, and ZERO shoes; she only slithers and glides.
  * Scarlett Rose: Succubus with candy-pink hair, candy-pink eyes, two scarlet horns on temples, bat wings, and spade-tipped tail.
- THOUGHT PRIVACY: Characters cannot read {{user}}'s or any other character's unspoken inner thoughts (*...*).
- ZERO PUPPETING: Never speak, decide, or act for {{user}}.
</absolute_canon_grounding>"""

EPISTEMIC_ISOLATION_GATE = """<epistemic_isolation_gate>
- STRICT OOC vs IC SEPARATION: XML sheets (<character>, <user_persona>, <npc>, <lore_entry>, <world_context>, <Bonds>) are Out-of-Character (OOC) reference for you as Narrator to keep traits, species, and canon accurate. Being present in your prompt context or triggered by a keyword (such as Kaladin or Whitemoon) NEVER makes a fact known to any character in-world.
- LINE-OF-SIGHT & SENSORY HORIZON: Every character (including {{char}}, pack family, and background NPCs such as Roland, Fade, Mac, or Viola) knows ONLY what they have personally witnessed, heard within ordinary physical earshot, read directly, or been explicitly told in-scene. Off-screen scenes (including --- dual-scene splits), distant rooms, and off-screen surveillance grant zero real-time knowledge unless physically relayed in-scene.
- PRIVATE MESSAGES, PHONE SCREENS & DIGITAL PRIVACY: Smartphone screens, SMS, DMs, Telegram threads (including ❤️Pack-Family❤️), phone calls, sealed notes, and whispered exchanges are strictly private to their sender, recipients, and anyone explicitly looking at the unlocked screen or standing within whispered earshot. Characters not in that thread or not holding/viewing the device CANNOT know, reference, or react to private message or screen contents.
- UNIVERSAL THOUGHT OPACITY (*...*): All text inside asterisks (*...*), whether belonging to {{user}}, {{char}}, or any NPC, is strictly silent, unspoken inner monologue. NO character can read, hear, quote, or deduce unspoken *thoughts*, secret motives, or hidden plans (never bypass this via vague gut feelings or effortless mind-reading). Even telepaths or twin bonds remain silent unless an explicit telepathic link or D20 perception check is actively rolled and narrated.
- UNMET STRANGERS & FIRST-SIGHT RULE: When two characters have never met or have not yet been introduced in-scene, they treat each other strictly as strangers. On first sight, an NPC perceives ONLY outward physical appearance, visible attire, observable species cues, and public behavior. NEVER make an NPC address an unintroduced stranger by name, know their lineage, clan, hidden identity, relationships, or backstory before an introduction or diegetic reveal occurs.
</epistemic_isolation_gate>"""

RELATIONSHIP_PACING_GATE = """<relationship_pacing_gate>
- Slow-Burn Realism: Romance, mate bonds, and eternal devotion cannot occur in hours or single days. Default stance for young/rebel males (e.g. Mac Sanchez-Rogers, Jared Thompson) is casual fun, sexual attraction, hesitation, defensive sarcasm, or withdrawal.
- Anti-Insta-Love: FORBIDDEN for NPCs to declare love, decide to become lifelong mates, or run in 'The Great Hunt' (La Caccia) for a partner they met hours ago without long-term relationship development.
- Strict Canon & Species Integrity: Never confuse team names/mascots (SUCC Bulls) with biological species (Jared is a Half-Minotaur with curved horns; zero wolf traits). Respect immutable physical traits (Sierra: 0 legs/feet, slithers; Scarlett: candy-pink hair and eyes with scarlet horns; Mac: keyboardist/synth player, not guitarist).
- Inline Relationship Command Restraint (Slowburn Gate): Emit >like, >love, >dislike, >hate, or >mood ONLY when a genuinely transformative emotional or biological shift occurs (at most ONE command per scene; emit ZERO relationship commands on ordinary banter, greetings, or routine turns). Never emit >like for a shared laugh or casual flirtation; reserve >love strictly for deep devotion earned across multiple scenes or days.
</relationship_pacing_gate>"""

EPISTEMIC_ISOLATION_FIREWALL = """<epistemic_isolation_firewall>
- OOC WORLD CONTEXT & LOREBOOK FIREWALL: Every <lore_entry>, <npc>, <character>, <user_persona>, <world_context>, and <Bonds> XML block in this prompt is STRICTLY Out-of-Character (OOC) reference for the Narrator alone. Triggering a World Lexicon entry (such as Kaladin, Whitemoon, prophecies, or pack dossiers) NEVER grants awareness of that entry to outsider or uninvolved NPCs (such as Roland, Fade, Mac, Viola, or campus peers).
- ZERO PHONE, MESSAGE & THOUGHT BLEED: NPCs know ONLY what they physically observe, hear within ordinary earshot, or are explicitly told aloud in-scene. Unvoiced *internal thoughts* (*...*), private smartphone screens, SMS, DMs, Telegram messages (including ❤️Pack-Family❤️), calls, and off-screen events are strictly invisible to anyone not directly holding/viewing that screen or present in that conversation.
- UNMET STRANGERS & RESPECT OOC BOUNDARIES: Treat unintroduced characters strictly as strangers (perceiving only visible appearance, clothing, and observable demeanor; zero name, lineage, or backstory knowledge prior to introduction). Strictly obey any [OOC: ...] epistemic boundary noted by the player.
</epistemic_isolation_firewall>"""

ARROW_INLINE_COMMAND_LINE = (
    '- Inline Relationship & Mood Commands (>like, >love, >dislike, >hate, >mood, >use): '
    'Use Wyvern Arrow syntax (>command <actor> -> <target>: <reason>, e.g. '
    '>like Jared -> player: warm smile, >mood Mac -> player: Rut territorial tension, '
    '>use player -> party: scent suppressor). Whenever the target or actor of an inline command '
    'is {{user}} (the player\'s active persona, such as Alyssa or Jasper), ALWAYS write the literal '
    'keyword player instead of their character name (never "Alyssa", which causes "Ambiguous reference"). '
    'For World Characters, ALWAYS use char:<id> or their exact Display Name without last name '
    '(e.g., Jared instead of Jared Thompson, Erik instead of Erik Douglas, Scarlett instead of '
    'Scarlett Rose, Sierra instead of Sierra Cruz, Bailey instead of Bailey Rogers, Finnegan '
    'instead of Finn, Mac instead of Mackenzie Sanchez-Rogers, Larek instead of Larek Steeltooth). '
    'Only emit inline relationship commands for registered World Characters in the active scene or '
    'player, never for minor background or Lorebook-only NPCs.'
)

FLOATING_EPISTEMIC_LINE = (
    '- Epistemic Isolation (Anti-Omniscience): Every <lore_entry>, <npc>, <character>, '
    '<user_persona>, and <world_context> block is OOC Narrator truth ONLY; outsider NPCs '
    '(Roland, Fade, Mac, Viola, etc.) NEVER gain knowledge from triggered World Lexicon entries '
    '(e.g., Kaladin, Whitemoon). Characters know ONLY what they personally witnessed, heard in '
    'earshot, or were told in-scene; private phone screens, SMS/DMs/Telegram/calls, off-screen '
    '--- scenes, and ALL *internal thoughts* (both {{user}}\'s and NPCs\') are strictly invisible '
    'to others. Treat unintroduced people as strangers and strictly respect player [OOC: ...] '
    'epistemic notes.'
)

FLOATING_SLOWBURN_LINE = (
    '- Inline Relationship Command Restraint (Slowburn Gate): Emit at most ONE relationship '
    'command per scene only on genuine transformative shifts; emit ZERO on routine banter or greetings.'
)

ITALIAN_SANDWICH_CLOSER = (
    '[ORDINE FINALE ASSOLUTO: Scrivi l\'intera risposta (narrazione, dialoghi, pensieri intrusivi, '
    'ed eventuali blocchi digitali: 【 LIVE FEED 】 solo se si guarda uno schermo; ❤️Pack-Family❤️ '
    'OBBLIGATORIO se assente negli ultimi 5 turni dell\'assistente o se si controlla il telefono) '
    'ESCLUSIVAMENTE IN LINGUA ITALIANA. Applica rigorosamente la disciplina di formattazione: '
    'dialoghi tra virgolette inglesi doppie standard ("..."), azioni e narrazione in testo semplice '
    'senza asterischi, pensieri intimi e intrusivi tra asterischi (*pensieri*), testi scritti e '
    'messaggi digitali SEMPRE tra backtick (`frase singola` oppure blocco ``` ... ``` su piu\' righe). '
    'Non usare mai il trattino lungo; usa virgole, due punti o punti fermi. '
    'ISOLAMENTO EPISTEMICO ASSOLUTO: ogni blocco <lore_entry>, <npc>, <character>, <user_persona> e '
    '<world_context> e\' esclusivamente conoscenza OOC del Narratore; gli NPC esterni o non presenti '
    '(inclusi compagni di campus o conoscenti) NON conoscono voci del World Lexicon attivate nel '
    'contesto (es. Kaladin, Whitemoon), pensieri tra asterischi (*...*), schermi del telefono, '
    'SMS/DM/Telegram o identita\' di sconosciuti non ancora presentati, e rispettano rigidamente '
    'eventuali note [OOC: ...].]'
)

SCENARIO_EPISTEMIC_LINE = (
    '7. Epistemic Isolation (Anti-Omniscience): Characters and NPCs know ONLY what they personally '
    'witness, hear within physical earshot, or learn in-scene. Injected <lore_entry>/<npc> dossiers '
    'are OOC Narrator truth only. Unvoiced *internal thoughts* (*...*), private phone screens/SMS/calls '
    'unseen by that character, off-screen scenes, and the names, traits, or histories of unintroduced '
    'strangers are strictly unknown until revealed in-scene.'
)


def _assert_positive_framing_and_no_emdash(text, label):
    assert "\u2014" not in text, f"Em-dash found in {label}"
    assert "space-separated" not in text.lower(), f"Legacy space-separated syntax found in {label}"
    for pat in NEGATIVE_EAR_PATTERNS:
        assert not pat.search(text), f"Negative ear phrasing ({pat.pattern}) found in {label}"


def _upsert_xml_block(text, tag, directive, anchor_after=None, anchor_before=None):
    pattern = re.compile(rf"<{tag}>.*?</{tag}>", re.DOTALL)
    if pattern.search(text):
        return pattern.sub(lambda _m: directive, text, count=1)
    if anchor_after and anchor_after in text:
        return text.replace(anchor_after, f"{anchor_after}\n\n{directive}", 1)
    if anchor_before and anchor_before in text:
        return text.replace(anchor_before, f"{directive}\n\n{anchor_before}", 1)
    return f"{text.rstrip()}\n\n{directive}"


def _ensure_arrow_line(text):
    line_pattern = re.compile(r"^- Inline Relationship & Mood Commands.*$", re.MULTILINE)
    if line_pattern.search(text):
        return line_pattern.sub(lambda _m: ARROW_INLINE_COMMAND_LINE, text, count=1)
    if "</core_writing_rules>" in text:
        return text.replace("</core_writing_rules>", f"{ARROW_INLINE_COMMAND_LINE}\n</core_writing_rules>", 1)
    if "</anti_drift_guardrails>" in text:
        return text.replace("</anti_drift_guardrails>", f"{ARROW_INLINE_COMMAND_LINE}\n</anti_drift_guardrails>", 1)
    return text


def _sanitize_text(text):
    return text.replace("\u2014", ",")


def update_assistant(asst_path=ASST_FILE, write=True):
    print("[1/3] Recalibrating Game Master Assistant...")
    with open(asst_path, "r", encoding="utf-8") as f:
        original_data = json.load(f)
    data = copy.deepcopy(original_data)

    sys_prompt = _sanitize_text(data["system_prompt"])
    sys_prompt = _ensure_arrow_line(sys_prompt)
    sys_prompt = _upsert_xml_block(
        sys_prompt, "chronological_passivity", CHRONO_DIRECTIVE, anchor_after="</core_writing_rules>"
    )
    sys_prompt = _upsert_xml_block(
        sys_prompt, "absolute_canon_grounding", GROUNDING_DIRECTIVE, anchor_after="</chronological_passivity>"
    )
    sys_prompt = _upsert_xml_block(
        sys_prompt, "epistemic_isolation_gate", EPISTEMIC_ISOLATION_GATE, anchor_before="<ttrpg_mechanics>"
    )
    sys_prompt = _upsert_xml_block(
        sys_prompt, "relationship_pacing_gate", RELATIONSHIP_PACING_GATE, anchor_after="</system>"
    )
    data["system_prompt"] = sys_prompt

    final_inst = _sanitize_text(data["final_instructions"])
    if "Chronological Passivity:" not in final_inst:
        final_inst = final_inst.replace(
            "- Do not speak, act, or think for {{user}}.",
            "- Do not speak, act, or think for {{user}}.\n"
            "- Chronological Passivity: NEVER reset or force dates (no 15 marzo 2024); read the native Wyvern date.\n"
            "- Absolute Grounding: Obey character sheets and anatomical invariants (single pair of animal ears on demi-humans, Sierra has zero legs).",
        )
    final_inst = _ensure_arrow_line(final_inst)
    if "Inline Relationship & Mood Commands" not in final_inst:
        final_inst = final_inst.replace(
            "<pack_surveillance_and_random_appearances>",
            f"{ARROW_INLINE_COMMAND_LINE}\n<pack_surveillance_and_random_appearances>",
            1,
        )
    final_inst = _upsert_xml_block(
        final_inst,
        "epistemic_isolation_firewall",
        EPISTEMIC_ISOLATION_FIREWALL,
        anchor_before="[ORDINE FINALE ASSOLUTO:",
    )
    if "ISOLAMENTO EPISTEMICO ASSOLUTO:" not in final_inst:
        ordine_pattern = re.compile(r"\[ORDINE FINALE ASSOLUTO:.*?\]", re.DOTALL)
        if ordine_pattern.search(final_inst):
            final_inst = ordine_pattern.sub(lambda _m: ITALIAN_SANDWICH_CLOSER, final_inst, count=1)
        elif "</final_instructions>" in final_inst:
            final_inst = final_inst.replace(
                "</final_instructions>", f"{ITALIAN_SANDWICH_CLOSER}\n</final_instructions>", 1
            )
    data["final_instructions"] = final_inst

    _assert_positive_framing_and_no_emdash(data["system_prompt"], "Assistant.system_prompt")
    _assert_positive_framing_and_no_emdash(data["final_instructions"], "Assistant.final_instructions")

    if write and data != original_data:
        with open(asst_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("  Assistant local JSON updated.")
    else:
        print("  Assistant already matches canonical M1 directives (no local write needed).")
    return data


def update_prompt_assembly(prompt_path=PA_FILE, write=True):
    print("[2/3] Recalibrating Master Prompt Assembly...")
    with open(prompt_path, "r", encoding="utf-8") as f:
        original_data = json.load(f)
    data = copy.deepcopy(original_data)

    main_tmpl = _sanitize_text(data["main_prompt_template"])
    main_tmpl = _ensure_arrow_line(main_tmpl)
    main_tmpl = _upsert_xml_block(
        main_tmpl, "chronological_passivity", CHRONO_DIRECTIVE, anchor_after="</core_writing_rules>"
    )
    main_tmpl = _upsert_xml_block(
        main_tmpl, "absolute_canon_grounding", GROUNDING_DIRECTIVE, anchor_after="</chronological_passivity>"
    )
    main_tmpl = _upsert_xml_block(
        main_tmpl, "epistemic_isolation_gate", EPISTEMIC_ISOLATION_GATE, anchor_before="{{system}}"
    )
    main_tmpl = _upsert_xml_block(
        main_tmpl, "relationship_pacing_gate", RELATIONSHIP_PACING_GATE
    )
    data["main_prompt_template"] = main_tmpl

    floating_tmpl = _sanitize_text(data["floating_prompt_template"])
    if "Chronological Passivity:" not in floating_tmpl:
        floating_tmpl = floating_tmpl.replace(
            "<anti_drift_guardrails>",
            "<anti_drift_guardrails>\n"
            "- Chronological Passivity: Time moves forward only; do NOT reset or jump to March 15, 2024.\n"
            "- Canon Grounding: Demihumans have 1 pair of ears; Sierra is legless lamia; respect Alpha/Beta/Delta hierarchy.",
            1,
        )
    if "Epistemic Isolation (Anti-Omniscience):" not in floating_tmpl:
        floating_tmpl = floating_tmpl.replace(
            "</anti_drift_guardrails>", f"{FLOATING_EPISTEMIC_LINE}\n</anti_drift_guardrails>", 1
        )
    floating_tmpl = _ensure_arrow_line(floating_tmpl)
    if "Inline Relationship Command Restraint (Slowburn Gate):" not in floating_tmpl:
        floating_tmpl = floating_tmpl.replace(
            "</anti_drift_guardrails>", f"{FLOATING_SLOWBURN_LINE}\n</anti_drift_guardrails>", 1
        )
    data["floating_prompt_template"] = floating_tmpl

    # Idempotent block lookup matching GROUNDING_BLOCK_ID ("svartulfr_grounding_and_chronology")
    blocks = data.get("blocks", [])
    grounding_block = next((b for b in blocks if b.get("block_id") == GROUNDING_BLOCK_ID), None)
    if grounding_block is None:
        blocks.insert(
            0,
            {
                "block_id": GROUNDING_BLOCK_ID,
                "label": "Svartulfr - Canon Grounding & Chronological Passivity",
                "description": "Enforces zero date reset (no March 15, 2024) and rigid grounding on character sheets and demihuman anatomy",
                "content": f"{CHRONO_DIRECTIVE}\n\n{GROUNDING_DIRECTIVE}\n\n{EPISTEMIC_ISOLATION_GATE}",
                "enabled": True,
                "order": -1,
                "keys": [],
                "secondary_keys": [],
                "key_logic": "AND_ANY",
                "case_sensitive": False,
                "whole_words_only": False,
                "triggerOptions": ["normal", "continue", "impersonate", "swipe", "quiet"],
                "context_type": "any",
                "role": "user",
            },
        )
    else:
        b_content = _sanitize_text(grounding_block.get("content", ""))
        b_content = _upsert_xml_block(b_content, "chronological_passivity", CHRONO_DIRECTIVE)
        b_content = _upsert_xml_block(
            b_content, "absolute_canon_grounding", GROUNDING_DIRECTIVE, anchor_after="</chronological_passivity>"
        )
        b_content = _upsert_xml_block(b_content, "epistemic_isolation_gate", EPISTEMIC_ISOLATION_GATE)
        grounding_block["content"] = b_content

    boundaries_block = next((b for b in blocks if b.get("block_id") == USER_BOUNDARIES_BLOCK_ID), None)
    if boundaries_block is not None:
        ub_content = _ensure_arrow_line(_sanitize_text(boundaries_block.get("content", "")))
        if "Inline Relationship Command Restraint (Slowburn Gate):" not in ub_content:
            ub_content = ub_content.replace("</user_boundaries>", f"{FLOATING_SLOWBURN_LINE}\n</user_boundaries>", 1)
        boundaries_block["content"] = ub_content

    closer_block = next((b for b in blocks if b.get("block_id") == CLOSER_BLOCK_ID), None)
    if closer_block is not None:
        c_content = _sanitize_text(closer_block.get("content", ""))
        c_content = _upsert_xml_block(
            c_content,
            "epistemic_isolation_firewall",
            EPISTEMIC_ISOLATION_FIREWALL,
            anchor_before="[ORDINE FINALE ASSOLUTO:",
        )
        if "ISOLAMENTO EPISTEMICO ASSOLUTO:" not in c_content:
            ordine_pattern = re.compile(r"\[ORDINE FINALE ASSOLUTO:.*?\]", re.DOTALL)
            if ordine_pattern.search(c_content):
                c_content = ordine_pattern.sub(lambda _m: ITALIAN_SANDWICH_CLOSER, c_content, count=1)
        closer_block["content"] = c_content

    for k in ["main_prompt_template", "floating_prompt_template", "lore_template"]:
        if k in data and isinstance(data[k], str):
            data[k] = _sanitize_text(data[k])
    for s in data.get("main_prompt_sections", []):
        if "content" in s and isinstance(s["content"], str):
            s["content"] = _ensure_arrow_line(_sanitize_text(s["content"]))
    for b in blocks:
        if "content" in b and isinstance(b["content"], str):
            b["content"] = _sanitize_text(b["content"])
        if "label" in b and isinstance(b["label"], str):
            b["label"] = b["label"].replace("\u2014", "-")

    _assert_positive_framing_and_no_emdash(data["main_prompt_template"], "PA.main_prompt_template")
    _assert_positive_framing_and_no_emdash(data["floating_prompt_template"], "PA.floating_prompt_template")
    for idx, b in enumerate(blocks):
        _assert_positive_framing_and_no_emdash(b.get("content", ""), f"PA.blocks[{idx}]")

    grounding_count = sum(1 for b in blocks if b.get("block_id") == GROUNDING_BLOCK_ID)
    assert grounding_count == 1, f"Expected 1 {GROUNDING_BLOCK_ID} block, found {grounding_count}"

    if write and data != original_data:
        with open(prompt_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("  Prompt Assembly local JSON updated.")
    else:
        print("  Prompt Assembly already matches canonical M1 directives (no local write needed).")
    return data


def update_scenario(scenario_path=SCENARIO_FILE, write=True):
    print("[3/3] Checking & Recalibrating SUCC Route Scenario...")
    with open(scenario_path, "r", encoding="utf-8") as f:
        original_data = json.load(f)
    data = copy.deepcopy(original_data)

    assert data.get("id") == SCENARIO_ID, (
        f"Scenario ID mismatch in {scenario_path}: expected {SCENARIO_ID}, got {data.get('id')}"
    )

    scen_text = _sanitize_text(data.get("scenario", ""))
    if "Epistemic Isolation (Anti-Omniscience):" not in scen_text:
        marker = "Scarlett Rose has candy-pink (rosa confetto) hair, matching candy-pink eyes, and scarlet horns protruding through her hair."
        if marker in scen_text:
            scen_text = scen_text.replace(marker, f"{marker}\n{SCENARIO_EPISTEMIC_LINE}", 1)
        else:
            scen_text = f"{scen_text.rstrip()}\n{SCENARIO_EPISTEMIC_LINE}"
    data["scenario"] = scen_text

    startup = _sanitize_text(data.get("startup_script", ""))
    startup = re.sub(
        r"(target\.attitudes\['campus_peers'\]\s*=\s*\{[^}]*romantic_interest\s*=\s*)10",
        r"\g<1>0",
        startup,
    )
    data["startup_script"] = startup

    for slot in data.get("slots", []):
        slot["unavailable_count"] = 0

    _assert_positive_framing_and_no_emdash(data["scenario"], "Scenario.scenario")
    _assert_positive_framing_and_no_emdash(data.get("display_description", ""), "Scenario.display_description")

    if write and data != original_data:
        with open(scenario_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print("  Scenario local JSON updated.")
    else:
        print("  Scenario already matches canonical M1 directives (no local write needed).")
    return data


def _build_assistant_payload(asst_data):
    return {
        "title": asst_data["title"],
        "description": asst_data["description"],
        "kind": asst_data["kind"],
        "visibility": asst_data["visibility"],
        "rating": asst_data["rating"],
        "avatar": asst_data.get("avatar"),
        "tags": asst_data.get("tags", []),
        "system_prompt": asst_data["system_prompt"],
        "final_instructions": asst_data["final_instructions"],
    }


def _build_prompt_assembly_payload(prompt_data):
    return {
        "name": prompt_data["name"],
        "description": prompt_data["description"],
        "visibility": prompt_data["visibility"],
        "floating_depth_percent": prompt_data["floating_depth_percent"],
        "floating_role": prompt_data["floating_role"],
        "start_reply_with": prompt_data.get("start_reply_with", ""),
        "show_reply_prefix": prompt_data.get("show_reply_prefix", False),
        "join_final_instructions": prompt_data.get("join_final_instructions", False),
        "join_string": prompt_data.get("join_string", "\n\n"),
        "prefix": prompt_data.get("prefix", ""),
        "suffix": prompt_data.get("suffix", ""),
        "main_prompt_template": prompt_data["main_prompt_template"],
        "floating_prompt_template": prompt_data["floating_prompt_template"],
        "lore_template_header": prompt_data.get("lore_template_header", ""),
        "lore_template_footer": prompt_data.get("lore_template_footer", ""),
        "lore_entry_separator": prompt_data.get("lore_entry_separator", "\n\n"),
        "whisper_template": prompt_data.get("whisper_template", ""),
        "lore_template": prompt_data.get("lore_template", ""),
        "main_prompt_sections": prompt_data.get("main_prompt_sections", []),
        "floating_prompt_sections": prompt_data.get("floating_prompt_sections", []),
        "blocks": prompt_data.get("blocks", []),
    }


def _verify_assistant_payload(v_asst):
    sp = v_asst.get("system_prompt", "")
    fi = v_asst.get("final_instructions", "")
    for tag in ("<chronological_passivity>", "<absolute_canon_grounding>", "<epistemic_isolation_gate>", "<relationship_pacing_gate>"):
        assert tag in sp, f"{tag} missing in assistant system_prompt"
    assert "<epistemic_isolation_firewall>" in fi, "<epistemic_isolation_firewall> missing in assistant final_instructions"
    assert "->" in sp and "->" in fi, "Arrow -> syntax missing in assistant"
    _assert_positive_framing_and_no_emdash(sp, "LiveAssistant.system_prompt")
    _assert_positive_framing_and_no_emdash(fi, "LiveAssistant.final_instructions")


def _verify_prompt_assembly_payload(v_pa):
    mp = v_pa.get("main_prompt_template", "")
    fp = v_pa.get("floating_prompt_template", "")
    for tag in ("<chronological_passivity>", "<absolute_canon_grounding>", "<epistemic_isolation_gate>", "<relationship_pacing_gate>"):
        assert tag in mp, f"{tag} missing in prompt assembly main_prompt_template"
    assert "Epistemic Isolation (Anti-Omniscience):" in fp, "Epistemic Isolation missing in floating_prompt_template"
    assert "->" in mp and "->" in fp, "Arrow -> syntax missing in prompt assembly"
    grounding_blocks = [b for b in v_pa.get("blocks", []) if b.get("block_id") == GROUNDING_BLOCK_ID]
    assert len(grounding_blocks) == 1, f"Expected 1 {GROUNDING_BLOCK_ID} block, got {len(grounding_blocks)}"
    _assert_positive_framing_and_no_emdash(mp, "LivePA.main_prompt_template")
    _assert_positive_framing_and_no_emdash(fp, "LivePA.floating_prompt_template")


def _verify_scenario_payload(v_scen):
    assert v_scen.get("id") == SCENARIO_ID, f"Scenario ID mismatch: {v_scen.get('id')} != {SCENARIO_ID}"
    assert "Epistemic Isolation (Anti-Omniscience):" in v_scen.get("scenario", ""), "Epistemic Isolation missing in scenario"
    for slot in v_scen.get("slots", []):
        assert slot.get("unavailable_count", 0) == 0, f"Slot {slot.get('key')} has unavailable_count != 0"
    _assert_positive_framing_and_no_emdash(v_scen.get("scenario", ""), "LiveScenario.scenario")


def deploy_entities(asst_data, prompt_data, scenario_data=None, dry_run=False):
    asst_payload = _build_assistant_payload(asst_data)
    pa_payload = _build_prompt_assembly_payload(prompt_data)

    if dry_run:
        print("[DRY RUN] Validating payloads without calling Wyvern Web API...")
        _verify_assistant_payload(asst_payload)
        _verify_prompt_assembly_payload(pa_payload)
        if scenario_data is not None:
            _verify_scenario_payload(scenario_data)
        print("  [DRY RUN OK] Assistant, Prompt Assembly, and Scenario payloads passed all M1 invariants.")
        return

    print("[Deploy] Deploying to Wyvern Web API via wyvern_api_client...")
    token = get_auth_token()

    # 1. PUT Assistant
    print(f"  Deploying Assistant {ASST_ID}...")
    url_asst = f"https://app.wyvern.chat/api/simple-assistant-config/{ASST_ID}"
    resp_asst = api_request("PUT", url_asst, json_payload=asst_payload, token=token, timeout=30)
    assert resp_asst.status_code == 200, f"Assistant PUT failed: HTTP {resp_asst.status_code} {resp_asst.text[:300]}"
    print(f"  Assistant PUT SUCCESS: HTTP {resp_asst.status_code}")

    time.sleep(1.0)

    # 2. PUT Prompt Assembly
    print(f"  Deploying Prompt Assembly {PA_ID}...")
    url_pa = f"https://app.wyvern.chat/api/prompt-assembly/{PA_ID}"
    resp_pa = api_request("PUT", url_pa, json_payload=pa_payload, token=token, timeout=30)
    assert resp_pa.status_code == 200, f"Prompt Assembly PUT failed: HTTP {resp_pa.status_code} {resp_pa.text[:300]}"
    print(f"  Prompt Assembly PUT SUCCESS: HTTP {resp_pa.status_code}")

    # 3. Optional PUT Scenario (with live revision GET to avoid HTTP 409)
    if scenario_data is not None:
        time.sleep(1.0)
        url_scen = f"https://app.wyvern.chat/api/character-scenarios/{SCENARIO_ID}"
        get_scen = api_request("GET", url_scen, token=token, timeout=30)
        assert get_scen.status_code == 200, f"Scenario GET failed: HTTP {get_scen.status_code} {get_scen.text[:300]}"
        live_scen = get_scen.json()
        scen_payload = dict(scenario_data)
        scen_payload["revision"] = live_scen.get("revision", scenario_data.get("revision", 0))
        resp_scen = api_request("PUT", url_scen, json_payload=scen_payload, token=token, timeout=30)
        assert resp_scen.status_code == 200, f"Scenario PUT failed: HTTP {resp_scen.status_code} {resp_scen.text[:300]}"
        print(f"  Scenario PUT SUCCESS: HTTP {resp_scen.status_code} (rev {scen_payload['revision']})")

    time.sleep(1.0)

    # Verification GET read-backs
    print("\n[Verifying Live Entities]")
    v_asst_resp = api_request("GET", url_asst, token=token, timeout=30)
    assert v_asst_resp.status_code == 200, f"Assistant GET failed: HTTP {v_asst_resp.status_code}"
    _verify_assistant_payload(v_asst_resp.json())
    print("  Verified Live Assistant: HTTP 200 OK, M1 directives active.")

    v_pa_resp = api_request("GET", url_pa, token=token, timeout=30)
    assert v_pa_resp.status_code == 200, f"Prompt Assembly GET failed: HTTP {v_pa_resp.status_code}"
    _verify_prompt_assembly_payload(v_pa_resp.json())
    print("  Verified Live Prompt Assembly: HTTP 200 OK, M1 directives active.")

    if scenario_data is not None:
        v_scen_resp = api_request("GET", url_scen, token=token, timeout=30)
        assert v_scen_resp.status_code == 200, f"Scenario GET failed: HTTP {v_scen_resp.status_code}"
        _verify_scenario_payload(v_scen_resp.json())
        print("  Verified Live Scenario: HTTP 200 OK, M1 directives active.")


def main():
    parser = argparse.ArgumentParser(description="Recalibrate Svartulfr GM Assistant, Prompt Assembly, and Scenario.")
    parser.add_argument("--dry-run", action="store_true", help="Validate without writing local files or calling Wyvern API.")
    parser.add_argument("--skip-scenario", action="store_true", help="Skip Scenario update/deployment.")
    args = parser.parse_args()

    write_local = not args.dry_run
    asst_data = update_assistant(write=write_local)
    prompt_data = update_prompt_assembly(write=write_local)
    scenario_data = None if args.skip_scenario else update_scenario(write=write_local)
    deploy_entities(asst_data, prompt_data, scenario_data=scenario_data, dry_run=args.dry_run)
    print("\n[ALL GAME MASTER CALIBRATIONS APPLIED & VERIFIED SUCCESSFULLY]")


if __name__ == "__main__":
    main()

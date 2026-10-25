#!/usr/bin/env python3
"""
Recalibrate Svartulfr Game Master Assistant, Prompt Assembly, and Scenario.
Enforces:
1. Chronological Passivity (Zero date reset to March 15, 2024; passive reading of native Wyvern clock).
2. Absolute Canon Grounding (Prior XML lookup, anti-hallucination of species, traits, and hierarchy).
3. Zero Em-Dash invariant.
4. Deployment and verification via Wyvern Web API.
"""

import json
import os
import pathlib
import sys
import time
import urllib.request
import urllib.error

sys.path.append("scripts")
from remediate_lorebook_npcs import refresh_wyvern_token

ASST_FILE = pathlib.Path("FINAL/assistants/Svartulfr_Game_Master_Assistant.json")
PROMPT_FILE = pathlib.Path("FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json")
SCENARIO_FILE = pathlib.Path("FINAL/Svartulfr_Master_Scenario.json")

ASST_ID = "simple_assistant_xRfBnV7wq48QppqbPPpTM"
PROMPT_ASSEMBLY_ID = "pha_kWkWUAfTJTF9q72c2bC98"
SCENARIO_ID = "char_scenario_CKgwq246DyCj1NNTBV9rt"

CHRONO_DIRECTIVE = """<chronological_passivity>
- WYVERN NATIVE CLOCK: The Game Master DOES NOT manage, invent, declare, or reset the in-game calendar date. Date and time progression are tracked natively by Wyvern's engine and the active scenario turn.
- FORBIDDEN DATES: Under NO circumstances generate, revert to, or force arbitrary or static boilerplate dates (including March 15, 2024 or any other fixed timestamp).
- PASSIVE INHERITANCE: If a temporal context or scene header is requested, solely read and reflect the current date and time established in the active scene history or Wyvern system state, advancing time naturally without overriding it.
</chronological_passivity>"""

GROUNDING_DIRECTIVE = """<absolute_canon_grounding>
- MANDATORY PRIOR LOOKUP: Before narrating actions, dialogue, reactions, or powers of any character or NPC, rigidly consult their XML entry (<character>, <user_persona>, <npc>, <lore_entry>).
- FORBIDDEN HALLUCINATIONS: NEVER invent ranks, forms, powers, species traits, or family ties not explicitly stated in their JED+ sheet:
  * Pack Subgenders and Hierarchy: Erik is Prime Alpha (Alpha Command, Pack Leader); Malachia is Dominant Alpha (Pack Leader); Logan is Beta (mediator, blacksmith; zero Alpha Command); Jasper is Beta (technomancer/DJ; zero Alpha Command); Noah is Delta (diplomat, grey eminence; zero Alpha Command).
  * Demihuman Kemonomimi (e.g. Finn, Roman, Kolya): Demihumans possess only a SINGLE pair of animal ears on top of their head and ZERO human ears. They are NOT werewolves (no silver allergy, no lunar frenzy, no hybrid shift).
  * Sierra Cruz: Lamia with rainbow hair and a 4-meter iridescent rainbow serpent lower body. She has ZERO legs, ZERO feet, and ZERO shoes; she only slithers and glides.
  * Scarlett Rose: Succubus with candy-pink hair, candy-pink eyes, two scarlet horns on temples, bat wings, and spade-tipped tail.
- THOUGHT PRIVACY: Characters cannot read {{user}}'s inner thoughts (*...*).
- ZERO PUPPETING: Never speak, decide, or act for {{user}}.
</absolute_canon_grounding>"""

def update_assistant():
    print("[1/3] Updating Assistant...")
    with open(ASST_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    sys_prompt = data["system_prompt"]
    if "<chronological_passivity>" not in sys_prompt:
        sys_prompt = sys_prompt.replace("</core_writing_rules>", f"</core_writing_rules>\n\n{CHRONO_DIRECTIVE}\n\n{GROUNDING_DIRECTIVE}")
        data["system_prompt"] = sys_prompt

    final_inst = data["final_instructions"]
    if "Zero date reset" not in final_inst:
        final_inst = final_inst.replace("- Do not speak, act, or think for {{user}}.", "- Do not speak, act, or think for {{user}}.\n- Chronological Passivity: NEVER reset or force dates (no 15 marzo 2024); read the native Wyvern date.\n- Absolute Grounding: Obey character sheets and anatomical invariants (single pair of animal ears on demi-humans, Sierra has zero legs).")
        data["final_instructions"] = final_inst

    # Invariant zero em-dash
    assert "\u2014" not in data["system_prompt"], "Em-dash in system_prompt"
    assert "\u2014" not in data["final_instructions"], "Em-dash in final_instructions"

    with open(ASST_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("  Assistant local JSON updated.")
    return data

def update_prompt_assembly():
    print("[2/3] Updating Prompt Assembly...")
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    main_tmpl = data["main_prompt_template"]
    if "<chronological_passivity>" not in main_tmpl:
        main_tmpl = main_tmpl.replace("</core_writing_rules>", f"</core_writing_rules>\n\n{CHRONO_DIRECTIVE}\n\n{GROUNDING_DIRECTIVE}")
        data["main_prompt_template"] = main_tmpl

    floating_tmpl = data["floating_prompt_template"]
    if "Chronological Passivity" not in floating_tmpl:
        floating_tmpl = floating_tmpl.replace("<anti_drift_guardrails>", f"<anti_drift_guardrails>\n- Chronological Passivity: Time moves forward only; do NOT reset or jump to March 15, 2024.\n- Canon Grounding: Demihumans have 1 pair of ears; Sierra is legless lamia; respect Alpha/Beta/Delta hierarchy.")
        data["floating_prompt_template"] = floating_tmpl

    # Update or add block for Grounding
    found_block = False
    for b in data.get("blocks", []):
        if b.get("block_id") == "svartulfr_grounding":
            found_block = True
            break
    if not found_block:
        data["blocks"].insert(0, {
            "block_id": "svartulfr_grounding_and_chronology",
            "label": "Svartulfr - Canon Grounding & Chronological Passivity",
            "description": "Enforces zero date reset (no March 15, 2024) and rigid grounding on character sheets and demihuman anatomy",
            "content": f"{CHRONO_DIRECTIVE}\n\n{GROUNDING_DIRECTIVE}",
            "enabled": True,
            "order": -1,
            "keys": [],
            "secondary_keys": [],
            "key_logic": "AND_ANY",
            "case_sensitive": False,
            "whole_words_only": False,
            "triggerOptions": ["normal", "continue", "impersonate", "swipe", "quiet"],
            "context_type": "any",
            "role": "user"
        })

    # Invariant zero em-dash
    for k in ["main_prompt_template", "floating_prompt_template", "lore_template"]:
        if k in data:
            data[k] = data[k].replace("\u2014", ",")
    for b in data.get("blocks", []):
        b["content"] = b["content"].replace("\u2014", ",")
        b["label"] = b["label"].replace("\u2014", "-")

    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("  Prompt Assembly local JSON updated.")
    return data

def deploy_entities(asst_data, prompt_data):
    print("[3/3] Deploying to Wyvern Web API...")
    token = refresh_wyvern_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    # 1. PUT Assistant
    print(f"  Deploying Assistant {ASST_ID}...")
    url_asst = f"https://app.wyvern.chat/api/simple-assistant-config/{ASST_ID}"
    asst_body = json.dumps({
        "title": asst_data["title"],
        "description": asst_data["description"],
        "kind": asst_data["kind"],
        "visibility": asst_data["visibility"],
        "rating": asst_data["rating"],
        "avatar": asst_data.get("avatar"),
        "tags": asst_data.get("tags", []),
        "system_prompt": asst_data["system_prompt"],
        "final_instructions": asst_data["final_instructions"]
    }, ensure_ascii=False).encode("utf-8")

    req_asst = urllib.request.Request(url_asst, data=asst_body, headers=headers, method="PUT")
    with urllib.request.urlopen(req_asst, timeout=30) as resp:
        print(f"  Assistant PUT SUCCESS: HTTP {resp.status} {resp.reason}")

    time.sleep(1.5)

    # 2. PUT Prompt Assembly
    print(f"  Deploying Prompt Assembly {PROMPT_ASSEMBLY_ID}...")
    url_pa = f"https://app.wyvern.chat/api/prompt-assembly/{PROMPT_ASSEMBLY_ID}"
    pa_body = json.dumps({
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
        "blocks": prompt_data.get("blocks", [])
    }, ensure_ascii=False).encode("utf-8")

    req_pa = urllib.request.Request(url_pa, data=pa_body, headers=headers, method="PUT")
    with urllib.request.urlopen(req_pa, timeout=30) as resp:
        print(f"  Prompt Assembly PUT SUCCESS: HTTP {resp.status} {resp.reason}")

    time.sleep(1.5)

    # Verification GET
    print("\n[Verifying Live Entities]")
    req_v_asst = urllib.request.Request(url_asst, headers=headers, method="GET")
    with urllib.request.urlopen(req_v_asst, timeout=30) as resp:
        v_asst = json.loads(resp.read().decode("utf-8"))
        assert "<chronological_passivity>" in v_asst.get("system_prompt", ""), "chronological_passivity missing in live assistant"
        print("  Verified Live Assistant: HTTP 200 OK, Chronological Passivity active!")

    req_v_pa = urllib.request.Request(url_pa, headers=headers, method="GET")
    with urllib.request.urlopen(req_v_pa, timeout=30) as resp:
        v_pa = json.loads(resp.read().decode("utf-8"))
        assert "<chronological_passivity>" in v_pa.get("main_prompt_template", ""), "chronological_passivity missing in live prompt assembly"
        print("  Verified Live Prompt Assembly: HTTP 200 OK, Chronological Passivity active!")

if __name__ == "__main__":
    asst_data = update_assistant()
    prompt_data = update_prompt_assembly()
    deploy_entities(asst_data, prompt_data)
    print("\n[ALL GAME MASTER CALIBRATIONS APPLIED & VERIFIED SUCCESSFULLY]")

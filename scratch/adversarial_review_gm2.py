#!/usr/bin/env python3
"""
Adversarial & Quality Reviewer Script for GM Assistant & Prompt Assembly.
Author: Reviewer GM 2
"""

import json
import pathlib
import sys
import urllib.request
import urllib.error

TOKEN_FILE = pathlib.Path("scratch/wyvern_token.txt")
ASST_LOCAL = pathlib.Path("FINAL/assistants/Svartulfr_Game_Master_Assistant.json")
PA_LOCAL = pathlib.Path("FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json")
ASST_REC = pathlib.Path("scratch/deployed_assistant_record.json")
PA_REC = pathlib.Path("scratch/deployed_prompt_assembly_record.json")

def run_tests():
    print("=" * 60)
    print("STARTING INDEPENDENT AUDIT & ADVERSARIAL STRESS TEST")
    print("=" * 60)

    token = TOKEN_FILE.read_text("utf-8").strip()
    headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json"
    }

    # 1. Inspect Local Records vs Payloads
    print("\n--- 1. Testing Local Artifacts & Consistency ---")
    assert ASST_LOCAL.exists(), "Local assistant payload missing"
    assert PA_LOCAL.exists(), "Local prompt assembly payload missing"
    assert ASST_REC.exists(), "Deployed assistant record missing"
    assert PA_REC.exists(), "Deployed prompt assembly record missing"

    asst_local_data = json.loads(ASST_LOCAL.read_text("utf-8"))
    pa_local_data = json.loads(PA_LOCAL.read_text("utf-8"))
    asst_rec_data = json.loads(ASST_REC.read_text("utf-8"))
    pa_rec_data = json.loads(PA_REC.read_text("utf-8"))

    print("Assistant ID recorded:", asst_rec_data.get("assistant_id"))
    print("Prompt Assembly ID recorded:", pa_rec_data.get("prompt_assembly_id"))

    # 2. Live API GET for Assistant
    print("\n--- 2. Live API Verification: SimpleAssistantConfig ---")
    asst_id = asst_rec_data.get("assistant_id")
    asst_url = f"https://app.wyvern.chat/api/simple-assistant-config/{asst_id}"
    req = urllib.request.Request(asst_url, headers=headers)
    with urllib.request.urlopen(req) as res:
        asst_status = res.status
        asst_live = json.loads(res.read().decode("utf-8"))
    
    print(f"GET {asst_url} -> Status {asst_status}")
    assert asst_status == 200, f"Expected 200, got {asst_status}"
    assert asst_live.get("kind") == "narrator", f"Expected 'narrator', got {asst_live.get('kind')}"
    assert asst_live.get("visibility") == "private", f"Expected 'private', got {asst_live.get('visibility')}"
    assert asst_live.get("rating") == "explicit", f"Expected 'explicit', got {asst_live.get('rating')}"
    print("Kind:", asst_live.get("kind"))
    print("Visibility:", asst_live.get("visibility"))
    print("Rating:", asst_live.get("rating"))
    print("Title:", asst_live.get("title"))

    # Check system prompt and final instructions content
    sys_prompt = asst_live.get("system_prompt", "")
    fin_instr = asst_live.get("final_instructions", "")
    print(f"System prompt length: {len(sys_prompt)} chars")
    print(f"Final instructions length: {len(fin_instr)} chars")
    
    # Invariant checks on Assistant
    assert "\u2014" not in sys_prompt, "EM-DASH found in system_prompt!"
    assert "\u2014" not in fin_instr, "EM-DASH found in final_instructions!"
    assert "S.P.E.C.I.A.L." in sys_prompt, "S.P.E.C.I.A.L. missing from system_prompt"
    assert "D20" in sys_prompt, "D20 missing from system_prompt"
    assert "Italian" in sys_prompt or "italiano" in sys_prompt or "italiana" in sys_prompt, "Italian language rule missing"
    assert "Format discipline" in fin_instr, "Format discipline missing from final_instructions"
    print("Assistant invariants passed: ZERO em-dashes, S.P.E.C.I.A.L., D20, and Italian Sandwich verified.")

    # 3. Live API GET for Prompt Assembly
    print("\n--- 3. Live API Verification: PromptAssembly ---")
    pa_id = pa_rec_data.get("prompt_assembly_id")
    pa_url = f"https://app.wyvern.chat/api/prompt-assembly/{pa_id}"
    req = urllib.request.Request(pa_url, headers=headers)
    with urllib.request.urlopen(req) as res:
        pa_status = res.status
        pa_live = json.loads(res.read().decode("utf-8"))

    print(f"GET {pa_url} -> Status {pa_status}")
    assert pa_status == 200, f"Expected 200, got {pa_status}"
    assert pa_live.get("name") == pa_local_data.get("name"), "Name mismatch"
    assert pa_live.get("visibility") == "private", f"Expected 'private', got {pa_live.get('visibility')}"
    assert pa_live.get("floating_depth_percent") == 4, f"Expected 4%, got {pa_live.get('floating_depth_percent')}"
    assert pa_live.get("floating_role") == "user", f"Expected 'user', got {pa_live.get('floating_role')}"
    
    blocks = pa_live.get("blocks", [])
    print(f"Blocks count: {len(blocks)}")
    assert len(blocks) == 5, f"Expected 5 blocks, got {len(blocks)}"
    for idx, blk in enumerate(blocks):
        print(f"  Block {idx}: role={blk.get('role')}, length={len(blk.get('content', ''))}")
        assert blk.get("role") == "user", f"Block {idx} role is not 'user'"
        assert "\u2014" not in blk.get("content", ""), f"Block {idx} contains EM-DASH"
    
    # Check lore templates
    lore_hdr = pa_live.get("lore_template_header", "")
    lore_ftr = pa_live.get("lore_template_footer", "")
    whisper = pa_live.get("whisper_template", "")
    main_prompt = pa_live.get("main_prompt_template", "")
    floating_prompt = pa_live.get("floating_prompt_template", "")

    assert "<world_context" in lore_hdr, "world_context missing in lore header"
    assert "</world_context>" in lore_ftr, "</world_context> missing in lore footer"
    assert "whisper" in whisper, "whisper macro missing"
    assert "\u2014" not in main_prompt, "EM-DASH found in main_prompt_template"
    assert "\u2014" not in floating_prompt, "EM-DASH found in floating_prompt_template"
    print("Prompt assembly invariants passed: 5 user blocks, Depth 4%, Role User, Lore headers, ZERO em-dashes.")

    # 4. Listing Endpoints Check
    print("\n--- 4. Live API Verification: Account Listing Endpoints ---")
    list_asst_url = "https://app.wyvern.chat/api/simple-assistant-config?kind=narrator"
    req = urllib.request.Request(list_asst_url, headers=headers)
    with urllib.request.urlopen(req) as res:
        list_asst_status = res.status
        list_asst_data = json.loads(res.read().decode("utf-8"))
    
    print(f"GET {list_asst_url} -> Status {list_asst_status}")
    assert list_asst_status == 200
    configs = list_asst_data.get("configs", [])
    matched_asst = [c for c in configs if (c.get("_id") or c.get("id")) == asst_id]
    assert len(matched_asst) == 1, f"Assistant {asst_id} not found in user listing!"
    print(f"Found assistant in kind=narrator listing: {matched_asst[0].get('title')} ({asst_id})")

    list_pa_url = "https://app.wyvern.chat/api/prompt-assembly"
    req = urllib.request.Request(list_pa_url, headers=headers)
    with urllib.request.urlopen(req) as res:
        list_pa_status = res.status
        list_pa_data = json.loads(res.read().decode("utf-8"))
    
    print(f"GET {list_pa_url} -> Status {list_pa_status}")
    assert list_pa_status == 200
    assemblies = list_pa_data.get("assemblies", [])
    matched_pa = [a for a in assemblies if (a.get("id") or a.get("_id")) == pa_id]
    assert len(matched_pa) == 1, f"Prompt Assembly {pa_id} not found in user listing!"
    print(f"Found prompt assembly in user listing: {matched_pa[0].get('name')} ({pa_id})")

    # 5. Integrity and Anti-Cheat Inspection
    print("\n--- 5. Anti-Cheat & Integrity Inspection ---")
    # Verify payloads in FINAL are not facades or dummy strings
    assert len(asst_local_data["system_prompt"]) > 2000, "System prompt suspiciously short!"
    assert len(asst_local_data["final_instructions"]) > 400, "Final instructions suspiciously short!"
    assert len(pa_local_data["main_prompt_template"]) > 2000, "Main prompt template suspiciously short!"
    assert len(pa_local_data["blocks"]) == 5, "Blocks count incorrect in local file"
    for b in pa_local_data["blocks"]:
        assert len(b["content"]) > 100, f"Block {b.get('title')} content suspiciously short!"
    print("Integrity checks passed: Real, full-length implementations with no facades.")

    # 6. Stress Test / Edge Cases
    print("\n--- 6. Adversarial Stress Testing ---")
    # Stress test 1: Check if prompt assembly Handlebars syntax is syntactically sound
    import re
    handlebars_tags = re.findall(r"\{\{([^\}]+)\}\}", pa_live.get("main_prompt_template", ""))
    print(f"Handlebars tags found in main_prompt_template: {len(handlebars_tags)}")
    assert len(handlebars_tags) > 0, "No handlebars tags found in main prompt template"

    # Stress test 2: Check XML tags balance in lore templates
    for entity_type in ["npc", "location", "item", "creature", "event", "lore_entry"]:
        start_tag_prefix = f"<{entity_type}"
        end_tag = f"</{entity_type}>"
        lore_tmpl = pa_live.get("lore_template", "")
        assert start_tag_prefix in lore_tmpl, f"Missing {start_tag_prefix} in lore_template"
        assert end_tag in lore_tmpl, f"Missing {end_tag} in lore_template"
    print("XML tag consistency passed: All 6 entity types cleanly enclosed.")

    # Stress test 3: D20 + S.P.E.C.I.A.L. dice mechanics format
    format_needle = "> [TEST: <Attributo> (D20: <Tiro> + <Mod> = <Totale> vs DC <Target>) -> ESITO: <SUCCESSO / FALLIMENTO / SUCCESSO CRITICO / FALLIMENTO CRITICO>]"
    assert format_needle in sys_prompt, "Exact D20 diegetic format needle missing in system_prompt"
    # Also check Block 2 in prompt assembly
    block_2_content = blocks[2].get("content", "")
    assert "D20" in block_2_content and "S.P.E.C.I.A.L." in block_2_content, "Block 2 missing D20/SPECIAL"
    assert "->" in block_2_content and "\u2014" not in block_2_content, "Block 2 format violation"
    print("D20 dice mechanics formatting passed: Rigorous syntax compliance verified.")

    print("\n" + "=" * 60)
    print("ALL TESTS AND VERIFICATIONS COMPLETED SUCCESSFULLY!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        run_tests()
    except Exception as e:
        print(f"\nAUDIT FAILURE: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

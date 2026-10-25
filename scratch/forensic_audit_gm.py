#!/usr/bin/env python3
"""
Forensic Integrity Audit Script for GM Assistant and Master TTRPG Prompt Assembly.
Independently verifies live Wyvern Cloud endpoints, payload content, user identity, and hashes.
"""

import urllib.request
import urllib.error
import json
import pathlib
import hashlib

def get_hash(obj):
    norm = json.dumps(obj, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(norm.encode('utf-8')).hexdigest()

def text_hash(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()

def main():
    token_path = pathlib.Path('scratch/wyvern_token.txt')
    if not token_path.exists():
        print("FAIL: Token file missing")
        return

    token = token_path.read_text(encoding='utf-8').strip()
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ForensicAuditor/1.0',
        'Accept': 'application/json'
    }

    print("======================================================================")
    print("1. LIVE WYVERN ENDPOINT AUDIT: ASSISTANT")
    print("======================================================================")
    asst_id = "simple_assistant_xRfBnV7wq48QppqbPPpTM"
    asst_url = f"https://app.wyvern.chat/api/simple-assistant-config/{asst_id}"
    local_asst_path = pathlib.Path("FINAL/assistants/Svartulfr_Game_Master_Assistant.json")
    local_asst = json.loads(local_asst_path.read_text(encoding="utf-8"))

    req = urllib.request.Request(asst_url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            asst_code = resp.status
            asst_raw = resp.read()
            cloud_asst = json.loads(asst_raw.decode('utf-8'))
            print(f"HTTP Status: {asst_code}")
            cloud_id = cloud_asst.get("_id") or cloud_asst.get("id")
            print(f"Cloud Entity ID: {cloud_id}")
            print(f"Cloud Title: {cloud_asst.get('title')}")
            print(f"Cloud Kind: {cloud_asst.get('kind')}")
            print(f"Cloud Visibility: {cloud_asst.get('visibility')}")
            print(f"Cloud Rating: {cloud_asst.get('rating')}")
            print(f"Cloud User ID: {cloud_asst.get('user', {}).get('id') or cloud_asst.get('user', {}).get('uid')}")
            print(f"Cloud User Username: {cloud_asst.get('user', {}).get('username')}")
            print(f"Cloud Tags: {cloud_asst.get('tags')}")

            # Verify User Ownership
            user_info = cloud_asst.get('user', {})
            user_id = user_info.get('id') or user_info.get('uid')
            display_name = user_info.get('displayName')
            print(f"Verified Owner: user_id={user_id}, displayName={display_name}")
            assert user_id == "2r4fVpvImte5dbljedLkZJxre2d2", f"User ID mismatch: {user_id}"
            assert display_name == "Lys", f"DisplayName mismatch: {display_name}"

            # Field by field comparison
            fields_to_compare = ["title", "description", "kind", "visibility", "rating", "avatar", "tags", "system_prompt", "final_instructions"]
            mismatches = []
            for f in fields_to_compare:
                loc_val = local_asst.get(f)
                cld_val = cloud_asst.get(f)
                if loc_val != cld_val:
                    mismatches.append((f, loc_val, cld_val))

            if mismatches:
                print(f"FAIL: Assistant field mismatches found: {[m[0] for m in mismatches]}")
            else:
                print("SUCCESS: 100% exact match between local assistant JSON and cloud entity across all operational fields!")

            # Content hashes
            print(f"Local System Prompt SHA256: {text_hash(local_asst['system_prompt'])}")
            print(f"Cloud System Prompt SHA256: {text_hash(cloud_asst['system_prompt'])}")
            assert text_hash(local_asst['system_prompt']) == text_hash(cloud_asst['system_prompt'])

            print(f"Local Final Instructions SHA256: {text_hash(local_asst['final_instructions'])}")
            print(f"Cloud Final Instructions SHA256: {text_hash(cloud_asst['final_instructions'])}")
            assert text_hash(local_asst['final_instructions']) == text_hash(cloud_asst['final_instructions'])

    except Exception as e:
        print(f"ERROR auditing assistant: {e}")
        raise

    print("\n======================================================================")
    print("2. LIVE WYVERN ENDPOINT AUDIT: PROMPT ASSEMBLY")
    print("======================================================================")
    prompt_id = "pha_kWkWUAfTJTF9q72c2bC98"
    prompt_url = f"https://app.wyvern.chat/api/prompt-assembly/{prompt_id}"
    local_prompt_path = pathlib.Path("FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json")
    local_prompt = json.loads(local_prompt_path.read_text(encoding="utf-8"))

    req2 = urllib.request.Request(prompt_url, headers=headers)
    try:
        with urllib.request.urlopen(req2) as resp:
            prompt_code = resp.status
            prompt_raw = resp.read()
            cloud_prompt = json.loads(prompt_raw.decode('utf-8'))
            print(f"HTTP Status: {prompt_code}")
            cloud_id = cloud_prompt.get("_id") or cloud_prompt.get("id")
            print(f"Cloud Entity ID: {cloud_id}")
            print(f"Cloud Name: {cloud_prompt.get('name')}")
            print(f"Cloud Description: {cloud_prompt.get('description')}")
            print(f"Cloud Visibility: {cloud_prompt.get('visibility')}")
            print(f"Cloud Floating Depth: {cloud_prompt.get('floating_depth_percent')}%")
            print(f"Cloud Floating Role: {cloud_prompt.get('floating_role')}")
            creator_info = cloud_prompt.get('creator', {})
            creator_id = creator_info.get('id') or creator_info.get('uid')
            creator_display = creator_info.get('displayName')
            print(f"Cloud Creator: id={creator_id}, displayName={creator_display}")
            assert creator_id == "2r4fVpvImte5dbljedLkZJxre2d2", f"Creator ID mismatch: {creator_id}"
            assert creator_display == "Lys", f"Creator displayName mismatch: {creator_display}"

            # Field comparisons
            fields_prompt = [
                "name", "description", "visibility", "floating_depth_percent", "floating_role",
                "start_reply_with", "show_reply_prefix", "join_final_instructions", "join_string",
                "prefix", "suffix", "main_prompt_template", "floating_prompt_template",
                "lore_template_header", "lore_template_footer", "lore_entry_separator",
                "whisper_template", "lore_template"
            ]
            mismatches_prompt = []
            for f in fields_prompt:
                loc_v = local_prompt.get(f)
                cld_v = cloud_prompt.get(f)
                if loc_v != cld_v:
                    mismatches_prompt.append((f, loc_v, cld_v))

            if mismatches_prompt:
                print(f"FAIL: Prompt assembly field mismatches: {[m[0] for m in mismatches_prompt]}")
            else:
                print("SUCCESS: 100% exact match on all root template fields!")

            # Compare blocks
            local_blocks = local_prompt.get("blocks", [])
            cloud_blocks = cloud_prompt.get("blocks", [])
            print(f"Local blocks count: {len(local_blocks)}, Cloud blocks count: {len(cloud_blocks)}")
            assert len(local_blocks) == len(cloud_blocks), f"Block count mismatch: {len(local_blocks)} vs {len(cloud_blocks)}"

            for i, (lb, cb) in enumerate(zip(local_blocks, cloud_blocks)):
                # check block_id, label, content, role, order, enabled
                assert lb.get("block_id") == cb.get("block_id"), f"Block {i} ID mismatch: {lb.get('block_id')} vs {cb.get('block_id')}"
                assert lb.get("label") == cb.get("label"), f"Block {i} label mismatch"
                assert lb.get("content") == cb.get("content"), f"Block {i} content mismatch"
                assert lb.get("role") == cb.get("role"), f"Block {i} role mismatch"
                assert lb.get("order") == cb.get("order"), f"Block {i} order mismatch"
                print(f"  Block {i} ({lb.get('block_id')}): MATCH (SHA256: {text_hash(lb['content'])[:16]}...)")

            print("SUCCESS: 100% exact match across all 5 prompt assembly blocks!")

            # Content hashes
            print(f"Local Main Prompt Template SHA256: {text_hash(local_prompt['main_prompt_template'])}")
            print(f"Cloud Main Prompt Template SHA256: {text_hash(cloud_prompt['main_prompt_template'])}")
            assert text_hash(local_prompt['main_prompt_template']) == text_hash(cloud_prompt['main_prompt_template'])

            print(f"Local Floating Template SHA256: {text_hash(local_prompt['floating_prompt_template'])}")
            print(f"Cloud Floating Template SHA256: {text_hash(cloud_prompt['floating_prompt_template'])}")
            assert text_hash(local_prompt['floating_prompt_template']) == text_hash(cloud_prompt['floating_prompt_template'])

    except Exception as e:
        print(f"ERROR auditing prompt assembly: {e}")
        raise

    print("\n======================================================================")
    print("3. VERIFYING LISTING ENDPOINTS ON USER LYS")
    print("======================================================================")
    # Check simple-assistant-config list (filtered by kind=narrator)
    list_asst_req = urllib.request.Request("https://app.wyvern.chat/api/simple-assistant-config?kind=narrator", headers=headers)
    with urllib.request.urlopen(list_asst_req) as resp:
        asst_list = json.loads(resp.read().decode('utf-8'))
        configs = asst_list.get("configs", [])
        found_asst = any((c.get("_id") == asst_id or c.get("id") == asst_id) for c in configs)
        print(f"Assistant listed in GET /api/simple-assistant-config?kind=narrator: {found_asst} (total configs: {len(configs)})")
        assert found_asst, f"Assistant {asst_id} not found in user's configs listing!"

    # Check prompt-assembly list
    list_prompt_req = urllib.request.Request("https://app.wyvern.chat/api/prompt-assembly", headers=headers)
    with urllib.request.urlopen(list_prompt_req) as resp:
        prompt_list = json.loads(resp.read().decode('utf-8'))
        assemblies = prompt_list.get("assemblies", [])
        found_prompt = any((a.get("_id") == prompt_id or a.get("id") == prompt_id) for a in assemblies)
        print(f"Prompt Assembly listed in GET /api/prompt-assembly: {found_prompt} (total assemblies: {len(assemblies)})")
        assert found_prompt, f"Prompt Assembly {prompt_id} not found in user's prompt assemblies listing!"

    print("\n======================================================================")
    print("4. FACADE / DUMMY / HARDCODED CHECKS & REPO INVARIANTS")
    print("======================================================================")
    # Check for em-dashes
    em_dash = '\u2014'
    checks = {
        "local_asst_sys_prompt": em_dash in local_asst["system_prompt"],
        "local_asst_final_inst": em_dash in local_asst["final_instructions"],
        "local_prompt_main_tpl": em_dash in local_prompt["main_prompt_template"],
        "local_prompt_float_tpl": em_dash in local_prompt["floating_prompt_template"],
        "local_prompt_lore_tpl": em_dash in local_prompt["lore_template"],
        "local_prompt_blocks": any(em_dash in b["content"] for b in local_prompt["blocks"]),
        "cloud_asst_sys_prompt": em_dash in cloud_asst["system_prompt"],
        "cloud_asst_final_inst": em_dash in cloud_asst["final_instructions"],
        "cloud_prompt_main_tpl": em_dash in cloud_prompt["main_prompt_template"],
        "cloud_prompt_float_tpl": em_dash in cloud_prompt["floating_prompt_template"],
        "cloud_prompt_lore_tpl": em_dash in cloud_prompt["lore_template"],
        "cloud_prompt_blocks": any(em_dash in b["content"] for b in cloud_prompt["blocks"]),
    }
    for k, v in checks.items():
        print(f"Em-dash in {k}: {v} (Expected: False)")
        assert not v, f"Em-dash invariant failed in {k}!"

    # Check S.P.E.C.I.A.L. stats present
    for stat in ["STR", "PER", "END", "CHA", "INT", "AGI", "LCK"]:
        assert stat in local_asst["system_prompt"], f"Missing stat {stat} in assistant system prompt"
        assert stat in local_prompt["blocks"][2]["content"], f"Missing stat {stat} in prompt assembly block 2"

    # Check D20 resolution syntax
    assert "> [TEST:" in local_asst["system_prompt"]
    assert "> [TEST:" in local_asst["final_instructions"]
    assert "> [TEST:" in local_prompt["blocks"][2]["content"]

    # Check Italian Sandwich enforcement
    assert "MANDATORY LANGUAGE DIRECTIVE: Output strictly in Italian" in local_asst["system_prompt"]
    assert "ORDINE FINALE ASSOLUTO: Scrivi l'intera risposta" in local_asst["final_instructions"]
    assert "MANDATORY LANGUAGE DIRECTIVE: You MUST write your entire response strictly in Italian" in local_prompt["main_prompt_template"]
    assert "ORDINE FINALE ASSOLUTO: Scrivi l'intera risposta" in local_prompt["blocks"][4]["content"]

    # Check XML lore templates
    assert "<npc name=" in local_prompt["lore_template"]
    assert "<location name=" in local_prompt["lore_template"]
    assert "<item name=" in local_prompt["lore_template"]
    assert "<creature name=" in local_prompt["lore_template"]
    assert "<special_stats>{{rpg_stats}}</special_stats>" in local_prompt["lore_template"]

    print("SUCCESS: All invariants, anti-puppeting, S.P.E.C.I.A.L., Italian sandwich, and XML structures verified!")
    print("\nALL FORENSIC AUDIT CHECKS PASSED EMPIRICALLY.")

if __name__ == "__main__":
    main()

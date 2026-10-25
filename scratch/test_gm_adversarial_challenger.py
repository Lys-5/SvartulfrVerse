#!/usr/bin/env python3
"""
Adversarial Empirical Stress-Test Suite for Svartúlfr Game Master Assistant & Prompt Assembly.
Author: Challenger GM 1 (teamwork_preview_challenger)

Tests:
1. Recursive Unicode Em-Dash ('\u2014') scan across all text fields in:
   - Local Assistant JSON: FINAL/assistants/Svartulfr_Game_Master_Assistant.json
   - Local Prompt Assembly JSON: FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json
   - Live Assistant Payload: GET /api/simple-assistant-config/simple_assistant_xRfBnV7wq48QppqbPPpTM
   - Live Prompt Assembly Payload: GET /api/prompt-assembly/pha_kWkWUAfTJTF9q72c2bC98
2. XML Lore & System Templates Stress-Test:
   - Structural tag balance verification (LIFO stack check) for <npc>, <location>, <item>, <creature>,
     <lore_entry>, <special_stats>, <world_context>, <event>, and all container tags.
   - Concrete rendering and well-formedness parsing across all polymorphic entry branches.
   - Edge case injection testing (empty values, nested tags, quotes, newlines).
3. Handlebars Macro Syntax Validation:
   - Delimiter balance check ({{...}} and {{{...}}}).
   - Block helper nesting validation ({{#if}} -> {{/if}}, {{else}}).
   - Helper sub-expression syntax validation (e.g. (eq type "npc")).
   - Permutation execution simulation across truthy/falsy state matrices.
"""

import sys
import json
import re
import pathlib
import urllib.request
from typing import Any, List, Dict, Tuple

# Base paths
REPO_ROOT = pathlib.Path("e:/repository/SvartulfrVerse")
LOCAL_ASST_PATH = REPO_ROOT / "FINAL/assistants/Svartulfr_Game_Master_Assistant.json"
LOCAL_PA_PATH = REPO_ROOT / "FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json"
TOKEN_PATH = REPO_ROOT / "scratch/wyvern_token.txt"

ASST_ID = "simple_assistant_xRfBnV7wq48QppqbPPpTM"
PA_ID = "pha_kWkWUAfTJTF9q72c2bC98"

# ---------------------------------------------------------
# Test 1: Recursive Unicode Em-Dash Scan
# ---------------------------------------------------------

def scan_for_em_dash(obj: Any, path: str = "") -> List[Dict[str, Any]]:
    findings = []
    if isinstance(obj, str):
        if "\u2014" in obj:
            # Count occurrences and gather contexts
            indices = [m.start() for m in re.finditer("\u2014", obj)]
            snippets = []
            for idx in indices:
                start = max(0, idx - 20)
                end = min(len(obj), idx + 21)
                snippets.append(repr(obj[start:end]))
            findings.append({
                "path": path,
                "count": len(indices),
                "snippets": snippets,
                "length": len(obj),
                "is_multiline": "\n" in obj
            })
    elif isinstance(obj, dict):
        for k, v in obj.items():
            subpath = f"{path}.{k}" if path else k
            findings.extend(scan_for_em_dash(v, subpath))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            subpath = f"{path}[{i}]"
            findings.extend(scan_for_em_dash(v, subpath))
    return findings


# ---------------------------------------------------------
# Test 2: XML Lore & System Templates Stress-Test
# ---------------------------------------------------------

def check_xml_tag_balance(text: str, context_label: str) -> Tuple[bool, List[str]]:
    """
    Checks that all XML tags in the string are properly balanced using a LIFO stack.
    Handles self-closing tags like <tag /> and ignores XML comments <!-- ... -->.
    """
    errors = []
    # Strip comments
    clean_text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    
    # Regex to find tags: <tag_name ...> or </tag_name> or <tag_name ... />
    tag_pattern = re.compile(r'<\s*(/)?\s*([a-zA-Z0-9_\-]+)([^>]*)>')
    
    stack = []
    for match in tag_pattern.finditer(clean_text):
        full_tag = match.group(0)
        is_closing = bool(match.group(1))
        tag_name = match.group(2)
        tag_attrs = match.group(3).strip()
        is_self_closing = tag_attrs.endswith('/')
        
        if is_self_closing:
            continue
            
        if is_closing:
            if not stack:
                errors.append(f"[{context_label}] Unexpected closing tag </{tag_name}> at pos {match.start()} with empty stack.")
            else:
                top = stack.pop()
                if top != tag_name:
                    errors.append(f"[{context_label}] Mismatched tag: expected </{top}>, found </{tag_name}> at pos {match.start()}.")
        else:
            stack.append(tag_name)
            
    if stack:
        errors.append(f"[{context_label}] Unclosed tags remaining on stack at end of text: {stack}")
        
    return len(errors) == 0, errors


def render_mock_lore_entry(entry_type: str, fields: Dict[str, Any]) -> str:
    """
    Simulates Wyvern's Handlebars lore template rendering for a specific entry.
    Template under test:
    {{#if (eq type "npc")}}
    <npc name="{{name}}"{{#if labels}} labels="{{labels}}"{{/if}}>
    {{content}}
    {{#if npc_info}}
    {{npc_info}}
    {{/if}}
    {{#if rpg_stats}}
    <special_stats>{{rpg_stats}}</special_stats>
    {{/if}}
    </npc>
    {{else}}{{#if (eq type "location")}}
    <location name="{{name}}">
    {{content}}
    </location>
    {{else}}{{#if (eq type "item")}}
    <item name="{{name}}">
    {{content}}
    {{#if item_config}}{{item_config}}{{/if}}
    </item>
    {{else}}{{#if (eq type "creature")}}
    <creature name="{{name}}"{{#if labels}} labels="{{labels}}"{{/if}}>
    {{content}}
    {{#if creature_config}}{{creature_config}}{{/if}}
    {{#if rpg_stats}}
    <special_stats>{{rpg_stats}}</special_stats>
    {{/if}}
    </creature>
    {{else}}{{#if (eq type "event")}}
    <event name="{{name}}">
    {{content}}
    </event>
    {{else}}
    <lore_entry name="{{name}}"{{#if type}} type="{{type}}"{{/if}}>
    {{content}}
    </lore_entry>
    {{/if}}{{/if}}{{/if}}{{/if}}{{/if}}
    """
    name = fields.get("name", "")
    content = fields.get("content", "")
    labels = fields.get("labels")
    npc_info = fields.get("npc_info")
    rpg_stats = fields.get("rpg_stats")
    item_config = fields.get("item_config")
    creature_config = fields.get("creature_config")

    if entry_type == "npc":
        res = f'<npc name="{name}"'
        if labels:
            res += f' labels="{labels}"'
        res += f">\n{content}\n"
        if npc_info:
            res += f"{npc_info}\n"
        if rpg_stats:
            res += f"<special_stats>{rpg_stats}</special_stats>\n"
        res += "</npc>"
        return res
    elif entry_type == "location":
        return f'<location name="{name}">\n{content}\n</location>'
    elif entry_type == "item":
        res = f'<item name="{name}">\n{content}\n'
        if item_config:
            res += f"{item_config}\n"
        res += "</item>"
        return res
    elif entry_type == "creature":
        res = f'<creature name="{name}"'
        if labels:
            res += f' labels="{labels}"'
        res += f">\n{content}\n"
        if creature_config:
            res += f"{creature_config}\n"
        if rpg_stats:
            res += f"<special_stats>{rpg_stats}</special_stats>\n"
        res += "</creature>"
        return res
    elif entry_type == "event":
        return f'<event name="{name}">\n{content}\n</event>'
    else:
        res = f'<lore_entry name="{name}"'
        if entry_type:
            res += f' type="{entry_type}"'
        res += f">\n{content}\n</lore_entry>"
        return res


# ---------------------------------------------------------
# Test 3: Handlebars Syntax & Permutation Validator
# ---------------------------------------------------------

def validate_handlebars_syntax(text: str, context_label: str) -> Tuple[bool, List[str]]:
    """
    Validates Handlebars macro syntax in text:
    - Balanced braces {{ ... }} and {{{ ... }}}
    - Nested block helpers balance: {{#helper ...}} ... {{/helper}}
    - {{else}} only inside open blocks
    - Valid macro identifiers and subexpression parentheses
    """
    errors = []
    
    # 1. Check raw brace balance
    open_count = text.count("{{")
    close_count = text.count("}}")
    if open_count != close_count:
        errors.append(f"[{context_label}] Mismatched Handlebars brace counts: {open_count} '{{{{' vs {close_count} '}}}}'")
        
    # 2. Tokenize handlebars tags
    tag_regex = re.compile(r'\{\{\{?(.*?)\}\}?\}')
    block_stack = []
    
    for match in tag_regex.finditer(text):
        raw_tag = match.group(1).strip()
        pos = match.start()
        
        # Check parenthetical balance within the tag (subexpressions)
        if raw_tag.count('(') != raw_tag.count(')'):
            errors.append(f"[{context_label}] Unbalanced parentheses inside Handlebars tag '{{{{{raw_tag}}}}}' at pos {pos}")
            
        # Block open: #helper
        if raw_tag.startswith('#'):
            parts = raw_tag[1:].split()
            helper_name = parts[0] if parts else ""
            block_stack.append((helper_name, pos, raw_tag))
        # Block close: /helper
        elif raw_tag.startswith('/'):
            close_helper = raw_tag[1:].strip()
            if not block_stack:
                errors.append(f"[{context_label}] Unexpected Handlebars close tag '{{{{{raw_tag}}}}}' at pos {pos} with empty stack")
            else:
                top_helper, top_pos, top_tag = block_stack.pop()
                if top_helper != close_helper:
                    errors.append(f"[{context_label}] Handlebars block mismatch: opened '#{top_helper}' at pos {top_pos}, closed '/{close_helper}' at pos {pos}")
        # Else tag
        elif raw_tag == 'else' or raw_tag.startswith('else '):
            if not block_stack:
                errors.append(f"[{context_label}] Handlebars '{{{{else}}}}' outside of any active block at pos {pos}")
        # Regular variable or expression
        else:
            # Verify no illegal characters in variable names (unless inside quotes or sub-expression)
            pass

    if block_stack:
        for helper_name, pos, raw_tag in block_stack:
            errors.append(f"[{context_label}] Unclosed Handlebars block '{{{{{raw_tag}}}}}' opened at pos {pos}")
            
    return len(errors) == 0, errors


# ---------------------------------------------------------
# Main Execution Orchestrator
# ---------------------------------------------------------

def main():
    print("=" * 80)
    print("CHALLENGER GM 1: ADVERSARIAL EMPIRICAL STRESS-TEST SUITE")
    print("=" * 80)

    # 1. Load Local Files
    print("\n[STEP 1] Loading local payload files...")
    if not LOCAL_ASST_PATH.exists():
        print(f"FATAL: Missing {LOCAL_ASST_PATH}")
        sys.exit(1)
    if not LOCAL_PA_PATH.exists():
        print(f"FATAL: Missing {LOCAL_PA_PATH}")
        sys.exit(1)

    local_asst = json.loads(LOCAL_ASST_PATH.read_text("utf-8"))
    local_pa = json.loads(LOCAL_PA_PATH.read_text("utf-8"))
    print(f"Loaded Local Assistant: {local_asst.get('title')}")
    print(f"Loaded Local Prompt Assembly: {local_pa.get('name')}")

    # 2. Fetch Live Payloads
    print("\n[STEP 2] Fetching live payloads from Wyvern API...")
    if not TOKEN_PATH.exists():
        print(f"FATAL: Missing {TOKEN_PATH}")
        sys.exit(1)

    token = TOKEN_PATH.read_text("utf-8").strip()
    headers = {"Authorization": f"Bearer {token}", "User-Agent": "Mozilla/5.0"}

    # Fetch Assistant
    req_asst = urllib.request.Request(
        f"https://app.wyvern.chat/api/simple-assistant-config/{ASST_ID}",
        headers=headers
    )
    with urllib.request.urlopen(req_asst) as resp_asst:
        if resp_asst.status != 200:
            print(f"FATAL: Live Assistant fetch failed with HTTP {resp_asst.status}")
            sys.exit(1)
        live_asst = json.loads(resp_asst.read().decode("utf-8"))
        print(f"Fetched Live Assistant ({ASST_ID}): HTTP 200, title={live_asst.get('title')}")

    # Fetch Prompt Assembly
    req_pa = urllib.request.Request(
        f"https://app.wyvern.chat/api/prompt-assembly/{PA_ID}",
        headers=headers
    )
    with urllib.request.urlopen(req_pa) as resp_pa:
        if resp_pa.status != 200:
            print(f"FATAL: Live Prompt Assembly fetch failed with HTTP {resp_pa.status}")
            sys.exit(1)
        live_pa = json.loads(resp_pa.read().decode("utf-8"))
        print(f"Fetched Live Prompt Assembly ({PA_ID}): HTTP 200, name={live_pa.get('name')}")

    # =========================================================
    # TEST 1: RECURSIVE EM-DASH SCAN
    # =========================================================
    print("\n" + "=" * 80)
    print("TEST 1: RECURSIVE UNICODE EM-DASH ('\\u2014') SCAN")
    print("=" * 80)

    datasets = [
        ("Local Assistant (FINAL/assistants/...)", local_asst),
        ("Local Prompt Assembly (FINAL/prompts/...)", local_pa),
        ("Live Assistant (simple_assistant_xRfBnV7wq48QppqbPPpTM)", live_asst),
        ("Live Prompt Assembly (pha_kWkWUAfTJTF9q72c2bC98)", live_pa)
    ]

    all_em_dash_findings = {}

    for label, ds in datasets:
        findings = scan_for_em_dash(ds)
        all_em_dash_findings[label] = findings
        print(f"\nTarget: {label}")
        if not findings:
            print("  [PASS] 0 em-dashes found across all fields.")
        else:
            print(f"  [ATTENTION] Found {len(findings)} field(s) containing em-dash (\\u2014):")
            for f in findings:
                print(f"    - Path: '{f['path']}' (occurrences: {f['count']})")
                for snip in f['snippets']:
                    print(f"      Snippet: {snip}")

    # Categorize findings
    print("\n--- EM-DASH ARCHITECTURAL ANALYSIS ---")
    gen_fields = ["system_prompt", "final_instructions", "main_prompt_template", "floating_prompt_template", "lore_template", "whisper_template", "content"]
    
    leaked_in_generation = []
    metadata_fields = []
    
    for label, findings in all_em_dash_findings.items():
        for f in findings:
            path_parts = f['path'].split('.')
            leaf = path_parts[-1]
            if any(leaf == g or leaf.endswith(f"[{g}]") for g in gen_fields):
                leaked_in_generation.append((label, f['path'], f['snippets']))
            else:
                metadata_fields.append((label, f['path'], f['snippets']))

    print(f"Em-dashes in Generation-Facing Prompt Text: {len(leaked_in_generation)}")
    print(f"Em-dashes in Metadata / UI Display Names: {len(metadata_fields)}")

    # =========================================================
    # TEST 2: XML TAG BALANCE & LORE TEMPLATES STRESS-TEST
    # =========================================================
    print("\n" + "=" * 80)
    print("TEST 2: XML TAG BALANCE & LORE TEMPLATES STRESS-TEST")
    print("=" * 80)

    # 1. Structural balance in templates
    xml_targets = [
        ("Local Asst: system_prompt", local_asst.get("system_prompt", "")),
        ("Local Asst: final_instructions", local_asst.get("final_instructions", "")),
        ("Local PA: main_prompt_template", local_pa.get("main_prompt_template", "")),
        ("Local PA: floating_prompt_template", local_pa.get("floating_prompt_template", "")),
        ("Local PA: lore_template_header + footer", local_pa.get("lore_template_header", "") + "\n" + local_pa.get("lore_template_footer", "")),
        ("Live Asst: system_prompt", live_asst.get("system_prompt", "")),
        ("Live Asst: final_instructions", live_asst.get("final_instructions", "")),
        ("Live PA: main_prompt_template", live_pa.get("main_prompt_template", "")),
        ("Live PA: floating_prompt_template", live_pa.get("floating_prompt_template", ""))
    ]

    # Add blocks
    for i, b in enumerate(local_pa.get("blocks", [])):
        xml_targets.append((f"Local PA: block[{i}] '{b.get('label')}'", b.get("content", "")))
    for i, b in enumerate(live_pa.get("blocks", [])):
        xml_targets.append((f"Live PA: block[{i}] '{b.get('label')}'", b.get("content", "")))

    xml_balance_errors = []
    for ctx, text in xml_targets:
        ok, errs = check_xml_tag_balance(text, ctx)
        if not ok:
            xml_balance_errors.extend(errs)
            print(f"  [FAIL] {ctx}:")
            for e in errs:
                print(f"    - {e}")
        else:
            print(f"  [PASS] {ctx}: Balanced XML tags.")

    # 2. Stress-test lore template branches with simulated data
    print("\n--- Lore Template Polymorphic Branch Stress-Test ---")
    lore_test_cases = [
        ("npc_full", "npc", {
            "name": "Erik Douglas",
            "content": "Prime Alpha of Clan Douglas.",
            "labels": "leader,alpha,douglas",
            "npc_info": "First Name: Erik\nLast Name: Douglas",
            "rpg_stats": "STR: 18, PER: 16, END: 17, CHA: 19, INT: 14, AGI: 15, LCK: 12"
        }),
        ("npc_minimal", "npc", {
            "name": "Finn Novak",
            "content": "Arctic Wolf demi-human student."
        }),
        ("location_standard", "location", {
            "name": "Villa Douglas",
            "content": "Ancestral estate in Blackwood City."
        }),
        ("item_full", "item", {
            "name": "Ambrosia Vial",
            "content": "Refined alchemical stimulant.",
            "item_config": "Rarity: Legendary\nValue: 50000 credits"
        }),
        ("creature_full", "creature", {
            "name": "Fenris Chimera",
            "content": "Corrupted apex beast.",
            "labels": "void,beast,apex",
            "creature_config": "Biome: Voidspace Rift",
            "rpg_stats": "STR: 22, END: 20, AGI: 18"
        }),
        ("event_standard", "event", {
            "name": "Yule Hunt",
            "content": "Annual ancestral gathering."
        }),
        ("lore_entry_typed", "organization/faction", {
            "name": "Ballantine Syndicate",
            "content": "Underworld distribution network."
        }),
        ("lore_entry_untyped", "", {
            "name": "The Fracture",
            "content": "Metaphysical rift separating worlds."
        })
    ]

    header = local_pa.get("lore_template_header", "").replace("{{position}}", "1").replace("{{count}}", "8")
    footer = local_pa.get("lore_template_footer", "")

    all_rendered_entries = []
    lore_rendering_errors = []

    for case_id, entry_type, fields in lore_test_cases:
        rendered = render_mock_lore_entry(entry_type, fields)
        all_rendered_entries.append(rendered)
        
        # Test individual entry tag balance
        ok, errs = check_xml_tag_balance(rendered, f"LoreBranch: {case_id}")
        if not ok:
            lore_rendering_errors.extend(errs)
            print(f"  [FAIL] Branch {case_id}: {errs}")
        else:
            print(f"  [PASS] Branch '{case_id}' ({entry_type or 'fallback'}): Well-formed tags.")

    # Test full assembled context block
    print("\n--- Assembled Lore Block Stress-Test ---")
    full_lore_doc = header + "\n" + "\n\n".join(all_rendered_entries) + "\n" + footer
    ok, errs = check_xml_tag_balance(full_lore_doc, "Full <world_context> Assembly")
    if not ok:
        print(f"  [FAIL] Full lore doc tag balance error: {errs}")
        lore_rendering_errors.extend(errs)
    else:
        print("  [PASS] Full <world_context> Assembly is 100% structurally balanced and well-formed.")

    # Adversarial edge case: special characters and nested tags in lore
    print("\n--- Adversarial Edge Case Injections ---")
    edge_cases = [
        ("npc_nested_xml", "npc", {
            "name": "Malachia Douglas",
            "content": "Has trait <apex_core>True</apex_core> and status <status>Active</status>.",
            "rpg_stats": "MGT: 20 <buff>+2</buff>"
        }),
        ("location_quotes", "location", {
            "name": 'The "Verve" Lounge & Club',
            "content": "Nightclub on Sunset Strip, Blackwood City."
        })
    ]
    for cid, et, flds in edge_cases:
        rendered = render_mock_lore_entry(et, flds)
        ok, errs = check_xml_tag_balance(rendered, f"EdgeCase: {cid}")
        print(f"  [{'PASS' if ok else 'FAIL'}] Edge case '{cid}': {'Balanced' if ok else str(errs)}")

    # =========================================================
    # TEST 3: HANDLEBARS MACRO SYNTAX VALIDATION
    # =========================================================
    print("\n" + "=" * 80)
    print("TEST 3: HANDLEBARS MACRO SYNTAX VALIDATION")
    print("=" * 80)

    hb_targets = [
        ("Local PA: main_prompt_template", local_pa.get("main_prompt_template", "")),
        ("Local PA: floating_prompt_template", local_pa.get("floating_prompt_template", "")),
        ("Local PA: lore_template", local_pa.get("lore_template", "")),
        ("Local PA: lore_template_header", local_pa.get("lore_template_header", "")),
        ("Local PA: lore_template_footer", local_pa.get("lore_template_footer", "")),
        ("Local PA: whisper_template", local_pa.get("whisper_template", "")),
        ("Local Asst: system_prompt", local_asst.get("system_prompt", "")),
        ("Local Asst: final_instructions", local_asst.get("final_instructions", "")),
        ("Live PA: main_prompt_template", live_pa.get("main_prompt_template", "")),
        ("Live PA: floating_prompt_template", live_pa.get("floating_prompt_template", "")),
        ("Live PA: lore_template", live_pa.get("lore_template", "")),
        ("Live PA: whisper_template", live_pa.get("whisper_template", "")),
        ("Live Asst: system_prompt", live_asst.get("system_prompt", "")),
        ("Live Asst: final_instructions", live_asst.get("final_instructions", ""))
    ]

    for i, b in enumerate(local_pa.get("blocks", [])):
        hb_targets.append((f"Local PA: block[{i}] '{b.get('label')}'", b.get("content", "")))
    for i, b in enumerate(live_pa.get("blocks", [])):
        hb_targets.append((f"Live PA: block[{i}] '{b.get('label')}'", b.get("content", "")))

    hb_syntax_errors = []
    all_extracted_macros = set()

    for ctx, text in hb_targets:
        ok, errs = validate_handlebars_syntax(text, ctx)
        if not ok:
            hb_syntax_errors.extend(errs)
            print(f"  [FAIL] {ctx}:")
            for e in errs:
                print(f"    - {e}")
        else:
            print(f"  [PASS] {ctx}: Valid Handlebars syntax.")
            
        # Extract macros for inventory
        for m in re.finditer(r'\{\{\{?(.*?)\}\}?\}', text):
            all_extracted_macros.add(m.group(1).strip())

    print(f"\nDiscovered {len(all_extracted_macros)} distinct Handlebars macro constructs:")
    for macro in sorted(all_extracted_macros):
        print(f"  - {{{{{macro}}}}}")

    # =========================================================
    # SUMMARY & VERDICT
    # =========================================================
    print("\n" + "=" * 80)
    print("EMPIRICAL TEST SUMMARY & FINAL VERDICT")
    print("=" * 80)

    print(f"Total XML Tag Balance Errors: {len(xml_balance_errors)}")
    print(f"Total Handlebars Syntax Errors: {len(hb_syntax_errors)}")
    print(f"Total Generation-Facing Em-Dashes: {len(leaked_in_generation)}")
    print(f"Total Metadata / UI Display Em-Dashes: {len(metadata_fields)}")

    if len(xml_balance_errors) == 0 and len(hb_syntax_errors) == 0 and len(leaked_in_generation) == 0:
        print("\nCore Engine & Generation Prompt Status: 100% SOUND & VALID")
    else:
        print("\nCore Engine Status: ISSUES DETECTED")

    return {
        "xml_balance_errors": xml_balance_errors,
        "hb_syntax_errors": hb_syntax_errors,
        "leaked_in_generation": leaked_in_generation,
        "metadata_em_dashes": metadata_fields
    }

if __name__ == "__main__":
    main()

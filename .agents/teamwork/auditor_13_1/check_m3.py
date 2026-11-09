import os
import sys

# Ensure utf-8 stdout
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

sys.path.insert(0, os.path.abspath('.'))

import json
import inspect
import copy
from proxy.free_tier_proxy import PayloadCompactor, get_config
import tests.test_proxy_compaction as test_mod

print("=== Starting Milestone 3 Independent Forensic Audit ===")

# 1. Config host verification
cfg = get_config()
assert cfg.get("host") == "127.0.0.1", f"Host is {cfg.get('host')}, expected 127.0.0.1"
assert cfg.get("port") == 5005, f"Port is {cfg.get('port')}, expected 5005"
print("[PASS] proxy/config_free_proxy.json network binding strictly on 127.0.0.1:5005.")

# 2. Adversarial test of PayloadCompactor logic
compactor = PayloadCompactor()

adversarial_payload = {
    "model": "test-model",
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
    "top_k": 0,
    "max_tokens": 12000,
    "stop": ["\nNarrator:", "\nUser:"],
    "messages": [
        {
            "role": "system",
            "content": """
<npc name="Erik Douglas" labels="" type="">
[NAME: Erik Douglas; AGE: 47; HEIGHT: 213 cm (6' 11.9"); ROLE: Alpha]
BACKSTORY: High-ranking alpha.
<special_stats></special_stats>
</npc>


<npc name="Erik Douglas">
[NAME: Erik Douglas duplicate]
</npc>


<character name="Noah Douglas Bloodmoon">
[NAME: Noah Douglas Bloodmoon; AGE: 22; HEIGHT: 197 cm (6' 5.6")]
</character>

<npc name="Noah Douglas Bloodmoon">
[NAME: Noah Douglas Bloodmoon; duplicate in NPC]
</npc>

<location name="The Verve">
Lounge
</location>

<location name="The Verve">
Lounge duplicate
</location>
"""
        }
    ]
}

orig_copy = copy.deepcopy(adversarial_payload)
compacted = compactor.compact_request_payload(adversarial_payload, provider="google")

# Verify deep copy preserved
assert adversarial_payload == orig_copy, "Deepcopy failed: input payload was mutated in-place!"
print("[PASS] Deep copy preserved input payload immutability.")

# Verify phase 1 parameter cleaning
assert "frequency_penalty" not in compacted
assert "presence_penalty" not in compacted
assert "top_k" not in compacted
assert compacted["max_tokens"] == 8192
assert compacted["stop"] == ["\nUser:"]
print("[PASS] Phase 1 parameter sanitization verified on adversarial inputs.")

# Verify phase 2 XML lore dedup
sys_content = compacted["messages"][0]["content"]
assert sys_content.count('<npc name="Erik Douglas">') == 1, f"Expected 1 Erik Douglas tag, got: {sys_content}"
assert sys_content.count('<location name="The Verve">') == 1, f"Expected 1 The Verve tag, got: {sys_content}"
print("[PASS] Phase 2 XML lore deduplication verified.")

# Verify phase 3 active character dedup
assert '<npc name="Noah Douglas Bloodmoon"' not in sys_content
assert '<character name="Noah Douglas Bloodmoon">' in sys_content
print("[PASS] Phase 3 active character cross-deduplication verified.")

# Verify phase 4 empty tag and attribute pruning
assert '<special_stats>' not in sys_content
assert 'labels=""' not in sys_content
assert 'type=""' not in sys_content
print("[PASS] Phase 4 empty tags and attributes pruning verified.")

# Verify phase 5 whitespace collapsing
assert '\n\n\n' not in sys_content
print("[PASS] Phase 5 whitespace collapsing verified.")

# 3. Source code inspection of tests/test_proxy_compaction.py
test_funcs = [f for name, f in inspect.getmembers(test_mod, inspect.isfunction) if name.startswith("test_")]
print(f"\nAnalyzing test functions in tests/test_proxy_compaction.py ({len(test_funcs)} test functions):")
for f in test_funcs:
    src = inspect.getsource(f)
    assert "assert " in src, f"Test {f.__name__} has no assertions!"
    assert "assert True" not in src, f"Test {f.__name__} has fake 'assert True'!"
    assert "pass" != src.strip().splitlines()[-1], f"Test {f.__name__} ends with pass!"
    print(f"  [PASS] {f.__name__} contains genuine assertions.")

print("\nALL INDEPENDENT M3 INTEGRITY CHECKS PASSED!")

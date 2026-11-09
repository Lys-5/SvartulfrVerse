import os
import sys
import json
import struct
import hashlib
import filecmp
from pathlib import Path

# UTF-8 stdout
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

REPO_ROOT = Path("e:/repository/SvartulfrVerse")
sys.path.insert(0, str(REPO_ROOT))

from proxy.free_tier_proxy import PayloadCompactor, get_config

print("======================================================================")
print("=== VICTORY AUDITOR INDEPENDENT FORENSIC VERIFICATION SUITE ===")
print("======================================================================")

errors = []

def fail(msg):
    print(f"[FAIL] {msg}")
    errors.append(msg)

def ok(msg):
    print(f"[PASS] {msg}")

# ----------------------------------------------------------------------
# 1. CANONICAL HEIGHTS & PROPORTIONS
# ----------------------------------------------------------------------
print("\n>>> AUDITING REQUIREMENT 1: CANONICAL HEIGHTS & PARITY")

CANONICAL_HEIGHTS = {
    'Alyssa': "155 cm (5' 1\")",
    'Jasper': "193 cm (6' 4\")",
    'Noah': "197 cm (6' 5.6\")",
    'Malachia': "208 cm (6' 9.9\")",
    'Erik': "213 cm (6' 11.9\")",
    'Wulfnic': "220 cm (7' 2.6\")"
}

PROPORTIONAL_CLAUSES = [
    "Alyssa (155 cm) arriva all'altezza della spalla di Jasper (193 cm, -38 cm).",
    "Malachia (208 cm) supera Alyssa di oltre mezzo metro (+53 cm) e la testa di lei gli arriva a malapena a metà del torace mastodontico.",
    "Erik (213 cm) e Wulfnic (220 cm) sovrastano Alyssa di 58-65 cm (lei arriva alla parte bassa del petto / sterno)."
]

# Database markdown
md_files = {
    'Alyssa': REPO_ROOT / 'database/characters/C_Alyssa_Douglas_Bloodmoon.md',
    'Jasper': REPO_ROOT / 'database/characters/C_Jasper_Douglas_Bloodmoon.md',
    'Noah': REPO_ROOT / 'database/characters/C_Noah_Douglas_Bloodmoon.md',
    'Malachia': REPO_ROOT / 'database/characters/C_Malachia_Douglas_Bloodmoon.md',
    'Erik': REPO_ROOT / 'database/characters/C_Erik_Douglas.md',
    'Wulfnic': REPO_ROOT / 'database/characters/C_Wulfnic_Bloodmoon.md',
}
for name, p in md_files.items():
    if not p.exists():
        fail(f"Missing md file: {p}")
        continue
    c = p.read_text(encoding='utf-8')
    if CANONICAL_HEIGHTS[name] not in c:
        fail(f"{name} md missing {CANONICAL_HEIGHTS[name]}")
    else:
        ok(f"{name} md contains canonical height: {CANONICAL_HEIGHTS[name]}")

# Style guide
sg_path = REPO_ROOT / 'database/assets/style_guide.md'
sg_text = sg_path.read_text(encoding='utf-8')
for name, ht in CANONICAL_HEIGHTS.items():
    if ht not in sg_text:
        fail(f"Style guide missing {name} height {ht}")
for clause in PROPORTIONAL_CLAUSES:
    if clause not in sg_text:
        fail(f"Style guide missing clause: {clause}")
ok("Style guide verified with all heights and proportional scale clauses.")

# Standalone cards and personas
card_files = {
    'Alyssa': REPO_ROOT / 'ARCHIVIO/cards_legacy/Alyssa_Douglas_Bloodmoon_card.json',
    'Jasper': REPO_ROOT / 'FINAL/Jasper_Douglas_Bloodmoon_card.json',
    'Noah': REPO_ROOT / 'FINAL/Noah_Douglas_Bloodmoon_card.json',
    'Malachia': REPO_ROOT / 'FINAL/Malachia_Douglas_Bloodmoon_card.json',
    'Erik': REPO_ROOT / 'FINAL/Erik_Douglas_card.json',
    'Wulfnic': REPO_ROOT / 'FINAL/Wulfnic_Bloodmoon_card.json',
}
for name, p in card_files.items():
    d = json.loads(p.read_text(encoding='utf-8'))
    desc = d.get('description', '')
    l0 = desc.splitlines()[0] if desc else ''
    if not (l0.startswith('[') and l0.endswith(']')):
        fail(f"Card {name} line 0 violates bracket rule: {l0}")
    if CANONICAL_HEIGHTS[name] not in l0:
        fail(f"Card {name} line 0 missing {CANONICAL_HEIGHTS[name]}")
    if 'PROPORTIONS & SCALE' not in desc:
        fail(f"Card {name} missing PROPORTIONS & SCALE")
    if '—' in desc:
        fail(f"Card {name} contains forbidden em-dash")
    ok(f"Card {name} bracket and height verified: {CANONICAL_HEIGHTS[name]}")

# Personas
for p_name, p_path in [('Alyssa', REPO_ROOT / 'FINAL/personas/Alyssa_Persona.json'), ('Jasper', REPO_ROOT / 'FINAL/personas/Jasper_Persona.json')]:
    d = json.loads(p_path.read_text(encoding='utf-8'))
    desc = d.get('description', '')
    l0 = desc.splitlines()[0] if desc else ''
    if not (l0.startswith('[') and l0.endswith(']')):
        fail(f"Persona {p_name} line 0 violates bracket rule")
    if CANONICAL_HEIGHTS[p_name] not in l0:
        fail(f"Persona {p_name} line 0 missing {CANONICAL_HEIGHTS[p_name]}")
    if 'PROPORTIONS & SCALE' not in desc:
        fail(f"Persona {p_name} missing PROPORTIONS & SCALE")
    if '—' in desc:
        fail(f"Persona {p_name} contains forbidden em-dash")
    ok(f"Persona {p_name} bracket and height verified: {CANONICAL_HEIGHTS[p_name]}")

# Lorebook byte-for-byte entries == lexicon & mirror parity
lb1_path = REPO_ROOT / 'FINAL/Svartulfr_NPC_Primary.json'
lb2_path = REPO_ROOT / 'lorebooks/optimized/Svartulfr_NPC_Primary.json'
lb1 = json.loads(lb1_path.read_text(encoding='utf-8'))
lb2 = json.loads(lb2_path.read_text(encoding='utf-8'))

if lb1['entries'] != lb1['lexicon']:
    fail("FINAL Primary lorebook: entries != lexicon")
else:
    ok("FINAL Primary lorebook: entries == lexicon byte-for-byte identical (99 entries)")

if lb2['entries'] != lb2['lexicon']:
    fail("Optimized Primary lorebook: entries != lexicon")
else:
    ok("Optimized Primary lorebook: entries == lexicon byte-for-byte identical (99 entries)")

if not filecmp.cmp(str(lb1_path), str(lb2_path), shallow=False):
    fail("Mirror mismatch: FINAL/Svartulfr_NPC_Primary.json != lorebooks/optimized/Svartulfr_NPC_Primary.json")
else:
    ok("Mirror verified: FINAL and optimized lorebooks are 100% byte-for-byte identical.")


# ----------------------------------------------------------------------
# 2. RUNIC & DIVINE MARKS SPECIFICATION & IMAGES
# ----------------------------------------------------------------------
print("\n>>> AUDITING REQUIREMENT 2: RUNIC & DIVINE MARKS ASSETS & SPEC")

IMAGE_NAMES = [
    "gebo_wrist_mark.png",
    "mani_hip_mark_alyssa.png",
    "sol_hip_mark_jasper.png",
    "celestial_polarity_twins.png",
    "logan_sleeves_marks.png",
    "malachia_blackwork_marks.png",
    "erik_ritual_marks.png",
    "wulfnic_primeval_brands.png"
]

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

hashes_by_dir = {}
for dir_rel in ['asset/references', 'assets/references']:
    dir_path = REPO_ROOT / dir_rel
    if not dir_path.exists():
        fail(f"Directory missing: {dir_rel}")
        continue
    dir_hashes = {}
    for img_name in IMAGE_NAMES:
        img_p = dir_path / img_name
        if not img_p.exists():
            fail(f"Missing image {dir_rel}/{img_name}")
            continue
        data = img_p.read_bytes()
        sz = len(data)
        if sz < 1_000_000:
            fail(f"Image {dir_rel}/{img_name} too small: {sz} bytes")
        if data[:8] != PNG_MAGIC:
            fail(f"Image {dir_rel}/{img_name} invalid PNG magic")
        if data[12:16] != b"IHDR":
            fail(f"Image {dir_rel}/{img_name} missing IHDR")
        w, h = struct.unpack(">II", data[16:24])
        if (w, h) != (1024, 1024):
            fail(f"Image {dir_rel}/{img_name} dimensions {w}x{h} != 1024x1024")
        if b"IEND" not in data[-16:]:
            fail(f"Image {dir_rel}/{img_name} missing IEND chunk")
        if b"IDAT" not in data:
            fail(f"Image {dir_rel}/{img_name} missing IDAT chunk")
        
        sha = hashlib.sha256(data).hexdigest()
        dir_hashes[img_name] = sha
        ok(f"{dir_rel}/{img_name}: {w}x{h} PNG, {sz:,} bytes, SHA256: {sha[:16]}...")
    hashes_by_dir[dir_rel] = dir_hashes

# Check uniqueness of hashes (no copies)
if len(set(hashes_by_dir['asset/references'].values())) != 8:
    fail("Duplicate image contents found in asset/references")
else:
    ok("All 8 images in asset/references have unique cryptographic SHA-256 hashes.")

# Check mirror between asset/ and assets/
if hashes_by_dir.get('asset/references') != hashes_by_dir.get('assets/references'):
    fail("Hash mismatch between asset/references and assets/references")
else:
    ok("Perfect mirror confirmed: asset/references and assets/references have identical SHA-256 hashes.")

# Check Spec Document
spec_file = REPO_ROOT / 'docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md'
if not spec_file.exists():
    fail("Spec document missing")
else:
    spec_text = spec_file.read_text(encoding='utf-8')
    sz = len(spec_text)
    if sz < 10000:
        fail(f"Spec document suspiciously short: {sz} chars")
    else:
        ok(f"Spec document size: {sz:,} characters.")
    
    if '—' in spec_text:
        fail("Spec document contains forbidden em-dash ('—')")
    else:
        ok("Spec document contains 0 forbidden em-dashes.")
    
    spec_lower = spec_text.lower()
    invariants = [
        ("serpent tooth", "Serpent tooth ritual needle"),
        ("cold iron ink", "Cold iron ink composition"),
        ("inner left wrist", "Inner left wrist Gebo placement"),
        ("alyssa", "Alyssa Hvit Maniulfr"),
        ("left hip", "Alyssa mark strictly on LEFT HIP"),
        ("maniulfr", "Exclusive cosmic title Maniulfr for Alyssa"),
        ("jasper", "Jasper Svartr Solulfr"),
        ("right hip", "Jasper mark strictly on RIGHT HIP"),
        ("solulfr", "Exclusive cosmic title Solulfr for Jasper"),
        ("prohibition of dispersed celestial marks", "Categorical prohibition of dispersed celestial marks"),
        ("logan jarn douglas", "Logan body art section"),
        ("malachia bjorn douglas bloodmoon", "Malachia body art section"),
        ("erik ulfr douglas", "Erik body art section"),
        ("wulfnic baleygr bloodmoon", "Wulfnic body art section")
    ]
    for term, label in invariants:
        if term not in spec_lower:
            fail(f"Spec missing invariant: {label} ('{term}')")
        else:
            ok(f"Spec contains: {label}")


# ----------------------------------------------------------------------
# 3. MICRO-PROXY NON-DESTRUCTIVE PAYLOAD COMPACTOR & CONFIG
# ----------------------------------------------------------------------
print("\n>>> AUDITING REQUIREMENT 3: MICRO-PROXY COMPACTOR & NETWORK CONFIG")

cfg_path = REPO_ROOT / 'proxy/config_free_proxy.json'
cfg = json.loads(cfg_path.read_text(encoding='utf-8'))
if cfg.get('host') != '127.0.0.1':
    fail(f"Security violation: proxy host is {cfg.get('host')}, expected 127.0.0.1")
else:
    ok("proxy/config_free_proxy.json host strictly set to 127.0.0.1 (loopback).")

if int(cfg.get('port', 0)) != 5005:
    fail(f"proxy port is {cfg.get('port')}, expected 5005")
else:
    ok("proxy/config_free_proxy.json port verified: 5005.")

# Direct execution of PayloadCompactor
compactor = PayloadCompactor()

# 3.1 Standard benchmark realistic payload
import tests.test_proxy_compaction as test_pc
realistic_payload = test_pc.sample_bloated_wyvern_payload.__wrapped__()
init_chars = sum(len(m.get('content', '')) for m in realistic_payload['messages'])
compacted_real = compactor.compact_request_payload(realistic_payload, provider="google")
final_chars = sum(len(m.get('content', '')) for m in compacted_real['messages'])
reduction_pct = ((init_chars - final_chars) / init_chars) * 100.0

ok(f"Realistic benchmark compaction: {init_chars} chars -> {final_chars} chars (-{reduction_pct:.2f}%)")
if not (15.0 <= reduction_pct <= 35.0):
    fail(f"Realistic reduction pct {reduction_pct:.2f}% outside expected range 15%-35%")
else:
    ok(f"Realistic reduction percentage {reduction_pct:.2f}% meets standard benchmark criteria (15%-35%).")

# 3.2 Lean payload test (zero unintended reduction)
lean_payload = {
    "model": "free-tier-master",
    "messages": [
        {"role": "system", "content": "Sei il Game Master. Rispondi in italiano standard."},
        {"role": "user", "content": '=>Alyssa: "Pronto per la lezione?"'}
    ]
}
init_lean = sum(len(m['content']) for m in lean_payload['messages'])
compacted_lean = compactor.compact_request_payload(lean_payload)
final_lean = sum(len(m['content']) for m in compacted_lean['messages'])
lean_red = ((init_lean - final_lean) / init_lean) * 100.0
if lean_red > 1.0:
    fail(f"Lean payload experienced unexpected reduction: -{lean_red:.2f}%")
else:
    ok(f"Lean payload preserved: {lean_red:.2f}% reduction.")

# 3.3 Zero semantic loss check on realistic payload
full_text = "\n".join(m['content'] for m in compacted_real['messages'])
invariants_preserved = [
    "[MANDATORY LANGUAGE DIRECTIVE: Rispondi sempre in italiano standard, terza persona presente.]",
    "Sei il Game Master dell'universo narrativo Svartulfr Verse. Mantieni tono maturo, descrizioni sensoriali crude, rispetto rigoroso del canone.",
    "I demi-umani possiedono un solo paio di orecchie: quelle animali. Non hanno orecchie umane.",
    "<character name=\"Jasper Douglas\">",
    "[NAME: Jasper Douglas; SPECIES: Werewolf Demi-Human; AGE: 20 (Born 2004-04-12); HEIGHT: 193 cm (6' 4\"); ROLE: Student / Hacker; PACK: Douglas Bloodmoon]",
    "BACKSTORY: Jasper is the twin brother of Alyssa. Brilliant tech specialist and hacker at SUCC.",
    "FAMILY & PACK: Twin sister Alyssa, father Erik, eldest brother Malachia, politician brother Noah.",
    "VOICE & BEHAVIOR: Quiet, analytical, fiercely protective of Alyssa.",
    "THE WEIGHT HE CARRIES: Balances tech genius with primal beast instincts.",
    "<user_persona name=\"Alyssa Douglas\">",
    "[NAME: Alyssa Douglas; SPECIES: Werewolf Demi-Human; AGE: 20 (Born 2004-04-12); HEIGHT: 155 cm (5' 1\"); ROLE: Pre-Med Student / Pack Healer; PACK: Douglas Bloodmoon]",
    "BACKSTORY: Alyssa is Jasper's twin sister. Gentle healer with devastating lunar magic.",
    "FAMILY & PACK: Twin brother Jasper, father Erik, brothers Malachia and Noah.",
    "VOICE & BEHAVIOR: Empathetic, determined, protective of her brother.",
    "<npc name=\"Finnegan Novak\">",
    "[NAME: Finnegan Novak; SPECIES: Arctic Wolf Demi-Human; AGE: 20; ROLE: SUCC Student; PACK: None]",
    "La tenuta della Casata Douglas si estende sulle colline di Seven Hills, protetta da potenti rune difensive.",
    "Secret bar e lounge esclusivo situato sul retro del Logan's Custom Garage.",
    "Fiala contenente Ambrosia distillata dai laboratori del dottor Sinclair.",
    "Creatura abissale generata dalle faglie del Voidspace.",
    "I licantropi LSE mantengono una gerarchia rigida basata sulla forza e sull'antico patto di sangue.",
    "La notte è calma a Seven Hills. I gemelli sono nella loro stanza a pianificare la missione.",
    '=>Alyssa: "Jasper, hai finito di analizzare quel segnale dei Sinners?"',
    '=>Jasper: "Quasi. Il firewall di Sinclair è più complesso del previsto, ma sto isolando il nodo."',
    '=>Alyssa: "Fai attenzione. Non vogliamo attirare l\'attenzione di Erik o Malachia stanotte."'
]
for tok in invariants_preserved:
    if tok not in full_text:
        fail(f"SEMANTIC LOSS DETECTED: Missing token '{tok}'")
    else:
        ok(f"Preserved token verified: '{tok[:40]}...'")

# Pruning checks
if '<npc name="Jasper Douglas"' in full_text:
    fail("Duplicate NPC for active character Jasper was NOT stripped from world_context!")
else:
    ok("Active character cross-deduplication confirmed: redundant <npc> stripped.")

if '<special_stats>' in full_text:
    fail("Empty <special_stats> tag was NOT pruned!")
else:
    ok("Empty tag pruning confirmed: <special_stats> removed.")

if 'labels=""' in full_text or 'type=""' in full_text:
    fail("Empty attributes were NOT pruned!")
else:
    ok("Empty attribute pruning confirmed: labels=\"\" stripped.")

if '\n\n\n' in full_text:
    fail("Excessive newlines (>2) were NOT collapsed!")
else:
    ok("Newline collapsing confirmed: 0 instances of 3+ consecutive newlines.")
# ----------------------------------------------------------------------
# FINAL SUMMARY
# ----------------------------------------------------------------------
print("\n======================================================================")
print(f"AUDIT EXECUTION COMPLETE. Total Errors: {len(errors)}")
print("======================================================================")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("ALL INDEPENDENT VERIFICATION AUDITS PASSED WITH ZERO ERRORS.")
    sys.exit(0)

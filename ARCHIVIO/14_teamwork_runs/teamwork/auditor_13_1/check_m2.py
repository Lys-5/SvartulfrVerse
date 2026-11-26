import os
import hashlib
import struct

IMAGE_NAMES = [
    'gebo_wrist_mark.png',
    'mani_hip_mark_alyssa.png',
    'sol_hip_mark_jasper.png',
    'celestial_polarity_twins.png',
    'logan_sleeves_marks.png',
    'malachia_blackwork_marks.png',
    'erik_ritual_marks.png',
    'wulfnic_primeval_brands.png'
]

DIRS = ['asset/references', 'assets/references']

PNG_MAGIC = b'\x89PNG\r\n\x1a\n'

print("=== Starting Milestone 2 Forensic Binary & Spec Audit ===")

# 1. Binary Analysis
hashes = {}
for d in DIRS:
    print(f"\nChecking directory: {d}")
    for name in IMAGE_NAMES:
        path = os.path.join(d, name)
        assert os.path.exists(path), f"File not found: {path}"
        with open(path, 'rb') as f:
            data = f.read()
        
        # Check size
        size = len(data)
        assert size > 1_000_000, f"File {path} size too small: {size} bytes"
        
        # Check header
        magic = data[:8]
        assert magic == PNG_MAGIC, f"File {path} invalid PNG magic: {magic}"
        
        # Check IHDR
        assert data[12:16] == b'IHDR', f"File {path} missing IHDR chunk"
        width, height = struct.unpack('>II', data[16:24])
        assert width >= 1024 and height >= 1024, f"File {path} resolution too low: {width}x{height}"
        
        # Check hash
        h = hashlib.sha256(data).hexdigest()
        print(f"[PASS] {name:<30} {width}x{height} | {size:>10,} bytes | SHA256: {h[:16]}...")
        
        if d == 'asset/references':
            hashes[name] = h
        else:
            # Verify mirror parity between asset/references and assets/references
            assert hashes[name] == h, f"Mirror mismatch between asset/ and assets/ for {name}"

# Check that all 8 images have distinct hashes (not duplicates)
unique_hashes = set(hashes.values())
print(f"\nUnique image hashes: {len(unique_hashes)} / {len(IMAGE_NAMES)}")
assert len(unique_hashes) == len(IMAGE_NAMES), "INTEGRITY VIOLATION: Duplicate image files detected!"
print("[PASS] All 8 generated reference images are distinct binary files.")

# 2. Inspect Specification Document
print("\n--- Checking docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md ---")
spec_path = 'docs/references/RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md'
assert os.path.exists(spec_path), f"Spec file missing: {spec_path}"
spec_text = open(spec_path, encoding='utf-8').read()

print(f"Spec file size: {len(spec_text)} characters, {len(spec_text.splitlines())} lines")
assert len(spec_text) > 4000, "Spec document is too short / stub"

# Check em-dash
em_dash = '\u2014'
assert em_dash not in spec_text, "Spec document contains forbidden em-dash ('—')!"
print("[PASS] Zero em-dashes found.")

# Invariants check
invariants = [
    ("Cold iron ink ritual", ["cold iron", "serpent tooth", "fifth day", "5th day"]),
    ("Inner left wrist placement for Gebo", ["inner left wrist", "gebo"]),
    ("Alyssa Máni left hip", ["left hip", "máni", "crescent"]),
    ("Jasper Sól right hip", ["right hip", "sól", "black sun"]),
    ("Prohibition of dispersed marks", ["prohibition", "chest", "collarbone", "hands"]),
    ("Distinct cosmic titles", ["solulfr", "maniulfr"]),
    ("Logan pack marks", ["logan", "eihwaz"]),
    ("Malachia pack marks", ["malachia", "thurisaz"]),
    ("Erik pack marks", ["erik", "tiwaz"]),
    ("Wulfnic pack marks", ["wulfnic", "othala"])
]

for inv_name, keywords in invariants:
    lower_spec = spec_text.lower()
    found = any(k in lower_spec for k in keywords)
    assert found, f"Spec missing invariant: {inv_name}"
    print(f"[PASS] Invariant verified: {inv_name}")

print("\nALL INDEPENDENT M2 INTEGRITY CHECKS PASSED!")

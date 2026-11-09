#!/usr/bin/env python3
"""
Verification Script: Runic and Divine Marks Reference Images and Specification
Validates the presence, dimensions, file size, and lore invariant adherence
for Milestone 2 deliverables in SvartulfrVerse.
"""

import os
import sys
from pathlib import Path
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parent.parent

REQUIRED_IMAGES = [
    "gebo_wrist_mark.png",
    "mani_hip_mark_alyssa.png",
    "sol_hip_mark_jasper.png",
    "celestial_polarity_twins.png",
    "logan_sleeves_marks.png",
    "malachia_blackwork_marks.png",
    "erik_ritual_marks.png",
    "wulfnic_primeval_brands.png",
]

TARGET_DIRS = [
    REPO_ROOT / "asset" / "references",
    REPO_ROOT / "assets" / "references",
]

SPEC_DOC = REPO_ROOT / "docs" / "references" / "RUNIC_AND_DIVINE_MARKS_SPECIFICATION.md"

LORE_INVARIANTS = [
    ("Cold Iron Ink", ["cold iron", "sacred charcoal"]),
    ("Serpent Tooth Needle", ["serpent tooth"]),
    ("5th Day Ritual Timing", ["5th day", "fifth day"]),
    ("Inner Left Wrist Placement", ["inner left wrist", "volar wrist"]),
    ("Alyssa Left Hip Invariant", ["alyssa", "left hip"]),
    ("Jasper Right Hip Invariant", ["jasper", "right hip"]),
    ("Prohibition of Dispersed Celestial Marks", ["prohibition", "chest", "collarbone", "neck", "hands"]),
    ("Cosmic Titles Distinction", ["maniulfr", "solulfr"]),
    ("Logan Sleeve Knotwork & Eihwaz", ["logan", "eihwaz", "sleeve"]),
    ("Malachia Warrior Blackwork & Thurisaz", ["malachia", "thurisaz", "blackwork"]),
    ("Erik Cheek Scar & Tiwaz/Hagalaz", ["erik", "tiwaz", "hagalaz", "cheek"]),
    ("Wulfnic 1200yo Brands & Othala/Jera", ["wulfnic", "othala", "jera", "1200"]),
]


def verify_images():
    print("=" * 70)
    print("PHASE 1: Verifying Generated Reference Images")
    print("=" * 70)
    
    total_checks = 0
    passed_checks = 0
    
    for target_dir in TARGET_DIRS:
        rel_dir = target_dir.relative_to(REPO_ROOT)
        print(f"\n[Directory Check] Inspecting {rel_dir}:")
        if not target_dir.exists():
            print(f"  [FAIL] Directory does not exist: {rel_dir}")
            continue
            
        for img_name in REQUIRED_IMAGES:
            total_checks += 1
            img_path = target_dir / img_name
            if not img_path.exists():
                print(f"  [FAIL] Missing image: {img_name}")
                continue
                
            file_size = img_path.stat().st_size
            if file_size < 100 * 1024:  # At least 100 KB
                print(f"  [FAIL] Image too small ({file_size} bytes): {img_name}")
                continue
                
            try:
                with Image.open(img_path) as img:
                    width, height = img.size
                    img_format = img.format
                    if width < 512 or height < 512:
                        print(f"  [FAIL] Resolution too low ({width}x{height}): {img_name}")
                        continue
                    if img_format != "PNG":
                        print(f"  [FAIL] Format is {img_format}, expected PNG: {img_name}")
                        continue
                    print(f"  [PASS] {img_name:<30} {width}x{height} {img_format} ({file_size:,} bytes)")
                    passed_checks += 1
            except Exception as e:
                print(f"  [FAIL] Could not open image {img_name}: {e}")
                
    print(f"\nPhase 1 Result: {passed_checks}/{total_checks} image checks passed.")
    return total_checks > 0 and passed_checks == total_checks


def verify_specification():
    print("\n" + "=" * 70)
    print("PHASE 2: Verifying Specification Document & Lore Invariants")
    print("=" * 70)
    
    if not SPEC_DOC.exists():
        print(f"[FAIL] Specification document missing: {SPEC_DOC.relative_to(REPO_ROOT)}")
        return False
        
    doc_content = SPEC_DOC.read_text(encoding="utf-8")
    doc_content_lower = doc_content.lower()
    
    # Check 1: Zero Em-Dashes
    em_dash_count = doc_content.count("—")
    if em_dash_count > 0:
        print(f"[FAIL] Format discipline violation: Found {em_dash_count} em-dashes ('—') in spec document.")
        return False
    else:
        print("[PASS] Format discipline: Exactly 0 em-dashes ('—') found.")
        
    # Check 2: Lore Invariants
    invariant_failures = 0
    for name, required_terms in LORE_INVARIANTS:
        missing = [t for t in required_terms if t.lower() not in doc_content_lower]
        if missing:
            print(f"[FAIL] Invariant '{name}': Missing required keywords: {missing}")
            invariant_failures += 1
        else:
            print(f"[PASS] Invariant '{name}': Verified.")
            
    # Check 3: Image Catalog & Prompt Blueprints
    image_key_failures = 0
    for img_name in REQUIRED_IMAGES:
        base_name = img_name.replace(".png", "")
        if base_name.lower() not in doc_content_lower:
            print(f"[FAIL] Image reference missing for '{base_name}' in spec document.")
            image_key_failures += 1
            
    if image_key_failures == 0:
        print(f"[PASS] All {len(REQUIRED_IMAGES)} image references cataloged with prompts.")
        
    total_failures = invariant_failures + image_key_failures
    print(f"\nPhase 2 Result: {len(LORE_INVARIANTS) - invariant_failures}/{len(LORE_INVARIANTS)} lore invariants verified.")
    return total_failures == 0


def main():
    print("Starting SvartulfrVerse Runic & Divine Marks Verification...\n")
    p1 = verify_images()
    p2 = verify_specification()
    
    print("\n" + "=" * 70)
    if p1 and p2:
        print("FINAL VERDICT: ALL VERIFICATION CHECKS PASSED (100% SUCCESS)")
        print("=" * 70)
        sys.exit(0)
    else:
        print("FINAL VERDICT: VERIFICATION FAILED")
        print("=" * 70)
        sys.exit(1)


if __name__ == "__main__":
    main()

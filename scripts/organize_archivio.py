import os
import shutil
import glob
import re

asset_dir = r"D:\SvartulfrVerse\asset"
archivio_dir = os.path.join(asset_dir, "archivio")
characters_dir = os.path.join(asset_dir, "characters")
main_cast_dir = os.path.join(characters_dir, "main_cast")
secondary_cast_dir = os.path.join(characters_dir, "secondary_cast")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Known main cast
main_cast = ["alyssa", "cornelius", "edric", "elizabeth", "erik", "jasper", "logan", "magnus", "malachia", "marcus", "nixara", "noah", "ut", "wulfnic", "zefir"]

# Also map 'kaladin' to 'noah' as they are the same character.
alias_map = {
    "kaladin": "noah",
    "jas": "jasper",
    "lys": "alyssa"
}

def move_files():
    files = glob.glob(os.path.join(archivio_dir, "*.*"))
    moved_count = 0
    unmatched = []
    
    for f in files:
        basename = os.path.basename(f)
        lower_name = basename.lower()
        
        # Skip generic maps/backgrounds
        if "mappa" in lower_name or "succ_campus" in lower_name or lower_name == "mood.png":
            continue
            
        # Try to find a matching character name in the filename
        matched_char = None
        
        # Check aliases first
        for alias, real_name in alias_map.items():
            if re.search(rf'\b{alias}\b', lower_name.split('.')[0], re.IGNORECASE):
                matched_char = real_name
                break
                
        if not matched_char:
            for char in main_cast:
                if re.search(rf'\b{char}\b', lower_name.split('.')[0], re.IGNORECASE):
                    matched_char = char
                    break
        
        # What about grouped files like "Malachia-Jasper-Kaladin-Noah.png"?
        # They will match the first one (Malachia), but let's see if we should copy them to all?
        # A move is better for now to clean the folder, or we can just leave group images in a "group" folder.
        group_match = [c for c in main_cast + list(alias_map.keys()) if c in lower_name]
        if len(group_match) > 1:
            group_dir = os.path.join(characters_dir, "group_shots")
            ensure_dir(group_dir)
            target_path = os.path.join(group_dir, basename)
            shutil.move(f, target_path)
            print(f"Moved group image {basename} -> group_shots/")
            moved_count += 1
            continue
            
        if matched_char:
            target_dir = os.path.join(main_cast_dir, matched_char)
            ensure_dir(target_dir)
            target_path = os.path.join(target_dir, basename)
            shutil.move(f, target_path)
            print(f"Moved {basename} -> main_cast/{matched_char}/")
            moved_count += 1
        else:
            # Hash-named files like Jd4-jka2ASnjS9romOGfg.webp or unidentifiable ones
            unmatched.append(basename)
            
    print(f"\nMoved {moved_count} files.")
    if unmatched:
        print(f"Unmatched files ({len(unmatched)}):")
        for u in unmatched[:10]:
            print(" -", u)
        if len(unmatched) > 10:
            print(" ...")

if __name__ == '__main__':
    move_files()

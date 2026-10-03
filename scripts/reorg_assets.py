import os
import shutil

base = r'd:\SvartulfrVerse\asset'

# Define new directories
dirs = {
    'main_cast': os.path.join(base, 'characters', 'main_cast'),
    'secondary_cast': os.path.join(base, 'characters', 'secondary_cast'),
    'avatars_legacy': os.path.join(base, 'characters', 'avatars_legacy'),
    'active_polaroids': os.path.join(base, 'characters', 'active_polaroids'),
    'locations': os.path.join(base, 'environments', 'locations'),
    'maps': os.path.join(base, 'environments', 'maps'),
    'lore_and_gods': os.path.join(base, 'lore_and_gods')
}

for d in dirs.values():
    os.makedirs(d, exist_ok=True)

# 1. Move polaroids
polaroids_dir = os.path.join(base, 'polaroids')
if os.path.exists(polaroids_dir):
    for f in os.listdir(polaroids_dir):
        shutil.move(os.path.join(polaroids_dir, f), os.path.join(dirs['active_polaroids'], f))
    os.rmdir(polaroids_dir)

# 2. Move maps
mappe_dir = os.path.join(base, 'mappe')
if os.path.exists(mappe_dir):
    for f in os.listdir(mappe_dir):
        shutil.move(os.path.join(mappe_dir, f), os.path.join(dirs['maps'], f))
    os.rmdir(mappe_dir)

# 3. Move locations
loc_dir = os.path.join(base, 'locations')
if os.path.exists(loc_dir):
    for f in os.listdir(loc_dir):
        shutil.move(os.path.join(loc_dir, f), os.path.join(dirs['locations'], f))
    os.rmdir(loc_dir)

# 4. Move legacy avatars (av and jai_av)
for legacy_dir_name in ['av', 'jai_av']:
    ldir = os.path.join(base, legacy_dir_name)
    if os.path.exists(ldir):
        for f in os.listdir(ldir):
            shutil.move(os.path.join(ldir, f), os.path.join(dirs['avatars_legacy'], f))
        os.rmdir(ldir)

# 5. Move Alyssa's outfits
lys_outfit = os.path.join(base, 'lys_outfit')
alyssa_dir = os.path.join(dirs['main_cast'], 'alyssa', 'outfits')
os.makedirs(alyssa_dir, exist_ok=True)
if os.path.exists(lys_outfit):
    for f in os.listdir(lys_outfit):
        shutil.move(os.path.join(lys_outfit, f), os.path.join(alyssa_dir, f))
    os.rmdir(lys_outfit)

# 6. Sort portraits
portraits_dir = os.path.join(base, 'portraits')
main_cast_names = [
    'wulfnic', 'ut', 'zefir', 'malachia', 'noah', 'jasper', 'alyssa', 
    'logan', 'edric', 'magnus', 'cornelius', 'elizabeth', 'kaladin', 
    'marcus', 'nixara', 'erik'
]

if os.path.exists(portraits_dir):
    for f in os.listdir(portraits_dir):
        src = os.path.join(portraits_dir, f)
        if not os.path.isfile(src):
            continue
            
        name_lower = f.lower().split('.')[0]
        
        # Special case: Fenris
        if 'fenris' in name_lower:
            shutil.move(src, os.path.join(dirs['lore_and_gods'], f))
            continue
            
        is_main = False
        for mc in main_cast_names:
            if mc in name_lower:
                is_main = True
                break
                
        if is_main:
            # Create a subfolder for the main character just in case they have multiple images
            char_folder = None
            for mc in main_cast_names:
                if mc in name_lower:
                    char_folder = os.path.join(dirs['main_cast'], mc)
                    os.makedirs(char_folder, exist_ok=True)
                    break
            shutil.move(src, os.path.join(char_folder, f))
        else:
            shutil.move(src, os.path.join(dirs['secondary_cast'], f))
    
    # If portraits dir is empty, remove it
    if not os.listdir(portraits_dir):
        os.rmdir(portraits_dir)

# Also move any stray files in the root of asset
for f in os.listdir(base):
    src = os.path.join(base, f)
    if os.path.isfile(src):
        if 'raw' in f.lower() or 'test' in f.lower():
            # Temp generation goes to temp
            temp_dir = os.path.join(base, 'temp_generation')
            os.makedirs(temp_dir, exist_ok=True)
            shutil.move(src, os.path.join(temp_dir, f))

print("Asset reorganization completed successfully!")

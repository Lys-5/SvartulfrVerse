import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
ASSET_MAIN = ROOT / 'asset' / 'characters' / 'main_cast'
ASSET_SEC = ROOT / 'asset' / 'characters' / 'secondary_cast'

final_cards = sorted(FINAL_DIR.glob('*_card.json'))

print("=== AUDIT OUTFITS E IMMAGINI ESISTENTI ===\n")

for cp in final_cards:
    card = json.loads(cp.read_text(encoding='utf-8'))
    cname = card.get('name')
    outfits = card.get('outfits', [])
    
    # Try to find corresponding folder in main_cast
    first_name = cname.split()[0].lower()
    char_folder = None
    for folder in ASSET_MAIN.iterdir():
        if folder.is_dir() and (folder.name.lower() in cname.lower() or first_name in folder.name.lower()):
            char_folder = folder
            break
            
    existing_images = []
    if char_folder and char_folder.exists():
        existing_images = [f.name for f in char_folder.iterdir() if f.is_file() and not f.name.endswith('.ini')]
        
    print(f"[{cname}] (Folder: {char_folder.name if char_folder else 'NONE'})")
    print(f"  Outfits totali nella card: {len(outfits)}")
    print(f"  Immagini trovate nella cartella ({len(existing_images)}): {', '.join(existing_images[:8])}")
    
    missing_outfits = []
    for o in outfits:
        oname = o.get('name') or o.get('title') or ''
        # Check if an image matches oname roughly
        match = any(oname.lower().split()[0] in img.lower() for img in existing_images)
        if not match:
            missing_outfits.append(oname)
            
    print(f"  Outfits privi di immagine ({len(missing_outfits)}/{len(outfits)}):")
    for mo in missing_outfits:
        print(f"    * {mo}")
    print("-" * 60)

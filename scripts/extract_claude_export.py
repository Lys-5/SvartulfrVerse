import zipfile
import os
import json

def extract_claude_export():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    export_dir = os.path.join(base_dir, 'drive', 'claude_export')
    out_dir = os.path.join(export_dir, 'extracted')
    os.makedirs(out_dir, exist_ok=True)

    zip_files = [f for f in os.listdir(export_dir) if f.endswith('.zip')]
    if not zip_files:
        print(f"No zip files found in {export_dir}")
        print("Please place the downloaded zip files (especially projects-000.zip) in this directory.")
        return

    print(f"Found {len(zip_files)} zip file(s) in {export_dir}:")
    for zf in zip_files:
        zpath = os.path.join(export_dir, zf)
        category_name = zf.replace('-000.zip', '').replace('.zip', '')
        dest_folder = os.path.join(out_dir, category_name)
        os.makedirs(dest_folder, exist_ok=True)
        print(f"\nExtracting {zf} -> {dest_folder}...")
        try:
            with zipfile.ZipFile(zpath, 'r') as zip_ref:
                zip_ref.extractall(dest_folder)
            extracted_items = os.listdir(dest_folder)
            print(f"  Extracted {len(extracted_items)} items: {extracted_items[:10]}")
        except Exception as e:
            print(f"  Error extracting {zf}: {e}")

    print("\nExtraction complete! Output located at:", out_dir)

if __name__ == '__main__':
    extract_claude_export()

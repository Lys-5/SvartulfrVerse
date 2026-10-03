import json
import os
import requests
from pathlib import Path

OUT_DIR = Path(r"D:\SvartulfrVerse\ARCHIVIO\01_Drafts\Character_Cards_V1")
AVATARS_DIR = OUT_DIR / "Scraped_Avatars"
AVATARS_DIR.mkdir(parents=True, exist_ok=True)

FILE1 = r"C:\Users\mande\.gemini\antigravity\brain\54916ade-7dff-4a72-9a20-dac425652f81\.system_generated\steps\67\output.txt"
FILE2 = r"C:\Users\mande\.gemini\antigravity\brain\54916ade-7dff-4a72-9a20-dac425652f81\.system_generated\steps\92\output.txt"

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Try parsing directly
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                # If there's markdown wrappers or something
                import re
                match = re.search(r'\[.*\]', content, re.DOTALL)
                if match:
                    return json.loads(match.group(0))
                
                # Check for object list
                match2 = re.search(r'\{.*\}', content, re.DOTALL)
                if match2:
                    return [json.loads(match2.group(0))]
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
    return []

def main():
    characters = load_data(FILE1)
    if isinstance(characters, dict) and "characters" in characters:
        characters = characters["characters"]
    
    chars2 = load_data(FILE2)
    if isinstance(chars2, dict) and "characters" in chars2:
        chars2 = chars2["characters"]
        
    if isinstance(chars2, list):
        characters.extend(chars2)
        
    if not characters:
        print("No characters loaded.")
        return

    md_content = "# Scraped Legacy Characters\n\n"
    
    for char in characters:
        name = char.get("name", "Unknown")
        avatar = char.get("avatar", "")
        desc = char.get("description", "")
        personality = char.get("personality", "")
        first_mes = char.get("first_mes", "")
        scenario = char.get("scenario", "")
        tags = char.get("tags", [])
        
        md_content += f"## {name}\n"
        md_content += f"**Tags:** {', '.join(tags)}\n\n"
        
        if avatar:
            avatar_url = f"https://ella.janitorai.com/bot-avatars/{avatar}"
            safe_name = "".join(x for x in name if x.isalnum() or x in " _-").replace(" ", "_")
            ext = avatar.split('.')[-1] if '.' in avatar else 'webp'
            avatar_path = AVATARS_DIR / f"{safe_name}.{ext}"
            
            try:
                # Download avatar
                img_data = requests.get(avatar_url).content
                with open(avatar_path, 'wb') as img_file:
                    img_file.write(img_data)
                md_content += f"![Avatar](Scraped_Avatars/{safe_name}.{ext})\n\n"
            except Exception as e:
                print(f"Failed to download avatar for {name}: {e}")
                
        md_content += "### Description\n```\n" + desc + "\n```\n\n"
        if personality:
            md_content += "### Personality\n```\n" + personality + "\n```\n\n"
        if first_mes:
            md_content += "### First Message\n```\n" + first_mes + "\n```\n\n"
        
        md_content += "---\n\n"

    out_file = OUT_DIR / "Scraped_Characters.md"
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print(f"Successfully processed {len(characters)} characters. Data saved to {out_file}")

if __name__ == '__main__':
    main()

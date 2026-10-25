import json
import pathlib
import re
import urllib.request

asst_path = pathlib.Path('FINAL/assistants/Svartulfr_Game_Master_Assistant.json')
prompt_path = pathlib.Path('FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json')

asst = json.loads(asst_path.read_text(encoding='utf-8'))
prompt = json.loads(prompt_path.read_text(encoding='utf-8'))

print("=== STATIC AUDIT: Svartulfr Game Master Assistant ===")
print("Title:", asst.get("title"))
print("Kind:", asst.get("kind"))
print("Visibility:", asst.get("visibility"))
print("Rating:", asst.get("rating"))
print("Avatar:", asst.get("avatar"))
print("Tags:", asst.get("tags"))

# Check em-dash
em_dash = '\u2014'
found_asst_em = []
for k, v in asst.items():
    if isinstance(v, str) and em_dash in v:
        # Note: Title contains em-dash in UI title? Let's check!
        found_asst_em.append((k, v.count(em_dash)))
print("Em-dashes in Assistant fields:", found_asst_em)

print("\n=== STATIC AUDIT: Svartulfr Master TTRPG Prompt Assembly ===")
print("Name:", prompt.get("name"))
print("Visibility:", prompt.get("visibility"))
print("Floating depth:", prompt.get("floating_depth_percent"))
print("Floating role:", prompt.get("floating_role"))
print("Lore header:", prompt.get("lore_template_header"))
print("Lore footer:", prompt.get("lore_template_footer"))
print("Whisper template:", prompt.get("whisper_template"))
print("Blocks count:", len(prompt.get("blocks", [])))

found_prompt_em = []
for k, v in prompt.items():
    if isinstance(v, str) and em_dash in v:
        found_prompt_em.append((k, v.count(em_dash)))
    elif k == "blocks":
        for i, b in enumerate(v):
            for bk, bv in b.items():
                if isinstance(bv, str) and em_dash in bv:
                    found_prompt_em.append((f"block[{i}].{bk}", bv.count(em_dash)))
print("Em-dashes in Prompt fields:", found_prompt_em)

# Detailed check of text content em-dashes (system_prompt, final_instructions, templates, blocks content)
prompt_texts = {
    "asst.system_prompt": asst.get("system_prompt", ""),
    "asst.final_instructions": asst.get("final_instructions", ""),
    "prompt.main_prompt_template": prompt.get("main_prompt_template", ""),
    "prompt.floating_prompt_template": prompt.get("floating_prompt_template", ""),
    "prompt.lore_template": prompt.get("lore_template", ""),
    "prompt.whisper_template": prompt.get("whisper_template", "")
}
for i, b in enumerate(prompt.get("blocks", [])):
    prompt_texts[f"block[{i}].{b.get('block_id')}.content"] = b.get("content", "")

text_em_dashes = {}
for name, text in prompt_texts.items():
    c = text.count(em_dash)
    if c > 0:
        text_em_dashes[name] = c

print("\nEm-dashes in text prompt bodies:", text_em_dashes)

# Live API check
token_path = pathlib.Path('scratch/wyvern_token.txt')
if token_path.exists():
    token = token_path.read_text(encoding='utf-8').strip()
    headers = {"Authorization": f"Bearer {token}", "User-Agent": "Mozilla/5.0"}
    
    # 1. Check deployed assistant
    try:
        url_asst = "https://app.wyvern.chat/api/simple-assistant-config/simple_assistant_xRfBnV7wq48QppqbPPpTM"
        req = urllib.request.Request(url_asst, headers=headers)
        with urllib.request.urlopen(req) as resp:
            live_asst = json.loads(resp.read().decode())
            print("\nLive Assistant status:", resp.status)
            print("Live Assistant id:", live_asst.get("id"))
            print("Live Assistant title:", live_asst.get("title"))
            print("Live Assistant visibility:", live_asst.get("visibility"))
            print("Live Assistant system_prompt len:", len(live_asst.get("system_prompt", "")))
            print("Live Assistant final_instructions len:", len(live_asst.get("final_instructions", "")))
    except Exception as e:
        print("Error checking live assistant:", e)
        
    # 2. Check deployed prompt assembly
    try:
        url_prompt = "https://app.wyvern.chat/api/prompt-assembly/pha_kWkWUAfTJTF9q72c2bC98"
        req = urllib.request.Request(url_prompt, headers=headers)
        with urllib.request.urlopen(req) as resp:
            live_prompt = json.loads(resp.read().decode())
            print("\nLive Prompt Assembly status:", resp.status)
            print("Live Prompt Assembly id:", live_prompt.get("id"))
            print("Live Prompt Assembly name:", live_prompt.get("name"))
            print("Live Prompt Assembly visibility:", live_prompt.get("visibility"))
            print("Live Prompt Assembly blocks count:", len(live_prompt.get("blocks", [])))
            print("Live Prompt Assembly floating_depth_percent:", live_prompt.get("floating_depth_percent"))
            print("Live Prompt Assembly floating_role:", live_prompt.get("floating_role"))
    except Exception as e:
        print("Error checking live prompt assembly:", e)

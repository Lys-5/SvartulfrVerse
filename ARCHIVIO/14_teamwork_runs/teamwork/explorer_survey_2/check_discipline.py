import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Check scenario
data = json.load(open('FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json', encoding='utf-8'))
for i, s in enumerate(data.get('premade_scenes', [])):
    text = s.get('scene_text', '')
    print(f"Scenario Scene {i} ({s.get('id')}):")
    print(f"  Em-dash count: {text.count('—')}")
    print(f"  Asterisk count: {text.count('*')}")
    print(f"  Markdown bold count: {text.count('**')}")

# Check chat message #0
msg0 = json.load(open('.agents/teamwork/explorer_survey_2/chat_msg0.json', encoding='utf-8'))
content = msg0.get('content', '')
print("Chat Message #0:")
print(f"  Em-dash count: {content.count('—')}")
print(f"  Asterisk count: {content.count('*')}")
print(f"  Markdown bold count: {content.count('**')}")

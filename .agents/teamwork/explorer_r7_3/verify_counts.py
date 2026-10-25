import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    primary = json.load(f)

with open('FINAL/Svartulfr_NPC_Secondary.json', 'r', encoding='utf-8') as f:
    secondary = json.load(f)

print("=== Svartulfr_NPC_Primary.json ===")
entries_p = primary.get('entries', [])
print(f"Total entries: {len(entries_p)}")
ph_6f_p = [e for e in entries_p if e.get('avatar') == 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public']
print(f"Entries with 6f8b7c78: {len(ph_6f_p)}")
custom_p = [e for e in entries_p if e.get('avatar') != 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public']
print(f"Entries with custom avatars: {len(custom_p)}")

print("\n=== Svartulfr_NPC_Secondary.json ===")
entries_s = secondary.get('entries', [])
print(f"Total entries: {len(entries_s)}")
ph_6f_s = [e for e in entries_s if e.get('avatar') == 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public']
print(f"Entries with 6f8b7c78: {len(ph_6f_s)}")
custom_s = [e for e in entries_s if e.get('avatar') != 'https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/6f8b7c78-b1c8-4e35-ff2b-7d2e4915f100/public']
print(f"Entries with custom avatars: {len(custom_s)}")

print("\n=== Placeholder Breakdown Summary ===")
print(f"Primary fallback count: {len(ph_6f_p)} / {len(entries_p)}")
print(f"Secondary fallback count: {len(ph_6f_s)} / {len(entries_s)}")
print(f"Total fallback count: {len(ph_6f_p) + len(ph_6f_s)} / {len(entries_p) + len(entries_s)}")
print(f"Total custom count: {len(custom_p) + len(custom_s)} / {len(entries_p) + len(entries_s)}")

import json

transcript_path = r'C:\Users\mande\.gemini\antigravity\brain\61c46121-044e-4cfb-9521-27755bb1e235\.system_generated\logs\transcript_full.jsonl'
with open(transcript_path, 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if idx in (206, 216):
            data = json.loads(line)
            print(f"=== LINE {idx} ===")
            print(data.get('content'))

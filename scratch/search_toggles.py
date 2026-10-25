import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

# Let's search in all .js files in scratch/
terms = [
    'narratorShowNpcThoughtsToggle',
    'advancedPostHistoryToggle',
    'easyParametersToggle',
    'narrator_profile_id',
    'narrator_enabled',
    'prompt_assembly_id',
    '/api/new/chat-logs',
    'api/story-engines/chats'
]

hits = {t: [] for t in terms}

for p in ROOT.rglob('*.js'):
    if 'node_modules' in str(p) or '.git' in str(p):
        continue
    try:
        content = p.read_text(encoding='utf-8', errors='ignore')
        for t in terms:
            if t in content:
                hits[t].append(str(p.relative_to(ROOT)))
    except Exception:
        pass

for t, files in hits.items():
    print(f"=== {t} ({len(files)} files) ===")
    for f in files[:5]:
        print(" ", f)

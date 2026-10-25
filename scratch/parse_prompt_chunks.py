import re
import json

chunk_files = [
    '36457-688d656b1534b9f0.js',
    '61929-5cc0e3b134146cf3.js',
    '69712-af83c29ebab813a8.js',
    '29079-b6a0d5e327fba37e.js',
    '54866-5b1f01a517163780.js'
]

print("=== SEARCHING IN 36457-688d656b1534b9f0.js ===")
content_36457 = open('e:/repository/SvartulfrVerse/scratch/36457-688d656b1534b9f0.js', encoding='utf-8').read()

# Look for API calls or endpoints
api_matches = re.findall(r'["\'](/api/[^"\']+)["\']', content_36457)
print("API endpoints in 36457:", set(api_matches))

# Look for template strings or prompt assembly fields
for pattern in [
    r'prompt_template',
    r'floating_prompt',
    r'directors_whisper',
    r'rpg_stats',
    r'special_stats',
    r'npc',
    r'lore_entry',
    r'post_history',
    r'depth',
    r'order',
    r'role'
]:
    matches = [m.start() for m in re.finditer(pattern, content_36457, re.IGNORECASE)]
    print(f"Matches for {pattern}: {len(matches)}")
    for idx in matches[:3]:
        snippet = content_36457[max(0, idx-100):min(len(content_36457), idx+200)]
        print(f"   Snippet around {pattern}: {snippet}\n")

print("\n=== SEARCHING IN 61929-5cc0e3b134146cf3.js ===")
content_61929 = open('e:/repository/SvartulfrVerse/scratch/61929-5cc0e3b134146cf3.js', encoding='utf-8').read()
api_matches_61929 = re.findall(r'["\'](/api/[^"\']+)["\']', content_61929)
print("API endpoints in 61929:", set(api_matches_61929))

for pattern in ['prompt-templates', 'Prompt Assembly', 'createPromptTemplate', 'updatePromptTemplate']:
    matches = [m.start() for m in re.finditer(pattern, content_61929, re.IGNORECASE)]
    print(f"Matches for {pattern} in 61929: {len(matches)}")
    for idx in matches[:3]:
        snippet = content_61929[max(0, idx-100):min(len(content_61929), idx+200)]
        print(f"   Snippet around {pattern}: {snippet}\n")

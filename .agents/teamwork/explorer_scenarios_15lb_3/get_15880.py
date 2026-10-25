import urllib.request

url = 'https://app.wyvern.chat/_next/static/chunks/15880-206fe0f873140574.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    text = resp.read().decode('utf-8')

with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\persona_chunk_15880.js', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Downloaded 15880 chunk, size: {len(text)} bytes")

# Find the full component
idx = text.find('Offer a persona to play as')
start = max(0, idx - 1500)
end = min(len(text), idx + 2500)
print("\n=== COMPONENT CODE ===")
print(text[start:end])

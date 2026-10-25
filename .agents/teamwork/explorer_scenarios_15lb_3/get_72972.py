import urllib.request

url = 'https://app.wyvern.chat/_next/static/chunks/72972-93036d53380b7ae7.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        text = resp.read().decode('utf-8')
        print(f"Downloaded 72972 chunk, size: {len(text)} bytes")
        with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\chunk_72972.js', 'w', encoding='utf-8') as f:
            f.write(text)
        print("First 1000 chars:\n", text[:1000])
except Exception as e:
    print("Error:", e)

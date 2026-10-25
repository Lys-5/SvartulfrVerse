import urllib.request

url = 'https://app.wyvern.chat/_next/static/chunks/29079-b6a0d5e327fba37e.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        text = resp.read().decode('utf-8')
        with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\chunk_29079.js', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Downloaded 29079, size:", len(text))
        pos = text.find('selectedLorebooks')
        if pos != -1:
            print("Snippet around selectedLorebooks:")
            print(text[max(0, pos-200):min(len(text), pos+1000)].encode('ascii', errors='replace').decode('ascii'))
except Exception as e:
    print("Error:", e)

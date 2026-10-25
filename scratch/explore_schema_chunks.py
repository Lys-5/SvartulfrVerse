import urllib.request
import re
import json

html_url = 'https://app.wyvern.chat/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4/edit'
req = urllib.request.Request(html_url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    chunks = set(re.findall(r'/_next/static/chunks/[^\"]+\.js', html))
    print(f"Found {len(chunks)} chunks in HTML")
    for c in chunks:
        try:
            url = 'https://app.wyvern.chat' + c
            t = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
            matches = []
            for term in ['entry_restrictions', 'startup_script', 'lorebook_ids', 'unavailable_count', 'speaker_slot']:
                if term in t:
                    matches.append(term)
            if matches:
                print(f"Chunk {c}: matched {matches}")
                # print snippet of matches
                for term in matches:
                    pos = t.find(term)
                    print(f"  [{term}] snippet: {t[max(0, pos-100):min(len(t), pos+200)]}\n")
        except Exception as e:
            pass
except Exception as e:
    print("Error:", e)

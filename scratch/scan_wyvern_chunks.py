import urllib.request
import re
import json

print("Fetching Next.js chunks...")
req = urllib.request.Request("https://app.wyvern.chat/character-scenarios/char_scenario_1DC43ggb6mB8YLJDJKrU4/edit", headers={"User-Agent": "Mozilla/5.0"})
try:
    html = urllib.request.urlopen(req).read().decode("utf-8")
    chunks = set(re.findall(r"/_next/static/chunks/[^\"]+\.js", html))
    print(f"Found {len(chunks)} chunks in HTML")
    for c in chunks:
        u = "https://app.wyvern.chat" + c
        try:
            txt = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})).read().decode("utf-8")
            if "_scenario" in txt or "startup_script" in txt:
                print(f"=== MATCH in {c} ===")
                for kw in ["_scenario", "startup_script", "assignments"]:
                    for m in re.finditer(re.escape(kw), txt):
                        idx = m.start()
                        print(f"[{kw}] -> {repr(txt[max(0, idx-100):min(len(txt), idx+250)])}")
        except Exception as e:
            pass
except Exception as e:
    print("Error:", e)

import json
import sys

# Load exports
d = json.load(open('exports/Svartulfr_Export.json', encoding='utf-8'))
chars = {c['id']: c for c in d['world_characters']}
lex = {l['id']: l for l in d['world_lexicon_entries']}

# Gallery items:
# 10 Kaladin -> Kaladin Nargathon (_b7QqV43D8pU1tewx4qenY)
# 11 zeera -> Zeera Darkfire (_a6KYGdN3BWTgbYEbT4mx8)
# 12 yael -> Yael (_Ht3kV76zrCE9tPmDAYh8Q)
# 13 wulfnic -> Wulfnic Bloodmoon (_W9PLYt9ERTBJBXqKQL2en)
# 14 wren -> Wren Lark (_QLeJFGFWL2GrqwGbtfUAG in Lexicon)
# 15 warg -> Varg Darkfire (_bh8AHn7WKkNTnLjwXrUWE)
# 16 thrakgor -> (no entity currently, report to user)
# 17 thomas -> Tomas Matthews (_pbNb7PrEanM1twU612VNg)
# 18 tate -> Tate (_RQQcCAN4MHETcJLhXPe9k)
# 19 sully -> Sullivan "Sully" Jones (_E7kHtwcpVYedVkVTmMGKX)
# 20 stanley -> Stanley Davies Sr. (_gqFXEaVj4aG9a8QL8R7f1)
# 21 stan -> Stanley Davies Jr. (_C18UjnQzGMLcQaNW3UaKq)
# 22 santiago -> Santiago Herrera (_c643VDjNFzAMgj7xGKGXT)
# 23 roland -> Roland Vickers (_2g1adXnHXcK62pVzGHUBm)
# 24 rev -> Rev (_DGkc2ALEYzNJ6mqGCW1KC)
# 25 radek -> Radek (_4bazKCAbPMmc19HzHAphC)
# 26 oberon -> (no entity currently, report to user)
# 27 noah -> Noah Douglas Bloodmoon (_r42cVzMjcGTAx7bR1DQVt)
# 28 nixara -> Nixara Bloodmoon (_fmzBDjDn3Gnq2hXKy7tY6)
# 29 nikolai -> Nikolaj Jökull (_AdCJWrQaTgC7xkPQECrtK)
# 30 malachia -> Malachia Douglas Bloodmoon (_rAcN9GXD1Le4WxY28e49W)
# 31 mac -> Mackenzie Sanchez-Rogers (_YY8VbpgzYk4dfFAL78rM3)
# 32 logan -> Logan Douglas (_JL37wK9PQMNDChULCDrWj)
# 33 loewe -> Professor Loewe (_E2A8prBrWg1q9zNjAR7kQ)
# 34 kian -> Kian (_kc7TyfPDQwUALKXcmTMxQ)
# 35 jasper -> Jasper Douglas Bloodmoon (_x3VY2kcbaDbKyCqywGeET)
# 36 jasmin -> Jasmin Thompson (_mfjaQDYUnAhLG8UggXg6N)
# 37 janice -> Janice Thompson (_DKY9cDLMUaYpELYAdckH2)
# 38 iordan -> Iordan R. Vess (_QfcJQRWUV2yfHGUUjLD8V)
# 39 hank -> Hank Thompson (_4GdzX4McREFg4zRpEqth2)
# 40 griven -> Asag Beast / Griven (_FkXtyrhQMhCpg7N6gm1Wm in Lexicon)
# 41 Goran -> Goran (_JQGgmwyA3qRaTLWck3GjX)
# 42 finn -> Finnegan Novak (_PQHGb4gL2LwDhNDrLFa3A)
# 43 fenris-full -> Fenris (_wpMTPQ2VVA2pWqJ3cMztJ)
# 44 fade -> Fade Greymoor (_mbBqR74dFceBFB4YegpyN)
# 45 eris -> Eris Davies (_q1n7hcz23ThY63JGEjdNq)
# 46 erik -> Erik Douglas (_d44gDc8N18kkbEhAcfUCG)
# 47 edric -> Edric Douglas (_YJQ4cjdrT7brm7HWVkf3K)
# 48 dullahan -> Dullahan (_F8ee4UpyLr7Fyr69KKhzV)
# 49 dominic -> Dominic Rogers (_dDXdeJrcYHbwagGFQVKQR)
# 50 danny -> Daniel "Danny" Boone (_VGAN3gQXchpTC2VFAcKUH)
# 51 chase -> Chase Anderson (_TLxzk97WmgYCA47nkDCVy)
# 52 brak -> Brak Ironfist (_AycV4d9dJRBakCmdH4q4J)
# 53 barkley -> Barkley Rover (_EXFAYyRCjRU19eebCFfXz)
# 54 ballantine -> Ruaraidh "Rory" Ballantine (_13rj1V7hPaJ2QederUYkx)
# 55 bailey -> Bailey Rogers (_eF7HAqWkLLYhQwt2tm4rn)
# 56 aries -> Harper Aries (_F4qM3efBRVyQnXXUxVqH7)
# 57 ariadne -> Ariadne Cirillo (_q1rYKHndN64QUgjHQazXB)
# 58 alyssa -> Alyssa Douglas Bloodmoon (_MXcEC8Y6B3BNm3b1ttHj6)
# 59 alistar -> Alistair DeVille (_daK4mwDzDLbCYQn4j2JpM in Lexicon)
# 60 alicia -> Alicia Virtuoso (_8CCMxWyPxRBaC1f2ycDqe)

# Plus Alyssa's 15/16 Outfits:
# alyssa_winter, alyssa_tactic, alyssa_summer, alyssa_spring, alyssa_sport,
# alyssa_sleep, alyssa_nude, alyssa_hybrid, alyssa_fullshift, alyssa_formal,
# alyssa_fest, alyssa_dinner, alyssa_clinic, alyssa_biker, alyssa_beach, alyssa_academy

mapping = [
    ("Kaladin", "character", "_b7QqV43D8pU1tewx4qenY"),
    ("zeera", "character", "_a6KYGdN3BWTgbYEbT4mx8"),
    ("yael", "character", "_Ht3kV76zrCE9tPmDAYh8Q"),
    ("wulfnic", "character", "_W9PLYt9ERTBJBXqKQL2en"),
    ("wren", "lexicon", "_QLeJFGFWL2GrqwGbtfUAG"),
    ("warg", "character", "_bh8AHn7WKkNTnLjwXrUWE"),
    ("thomas", "character", "_pbNb7PrEanM1twU612VNg"),
    ("tate", "character", "_RQQcCAN4MHETcJLhXPe9k"),
    ("sully", "character", "_E7kHtwcpVYedVkVTmMGKX"),
    ("stanley", "character", "_gqFXEaVj4aG9a8QL8R7f1"),
    ("stan", "character", "_C18UjnQzGMLcQaNW3UaKq"),
    ("santiago", "character", "_c643VDjNFzAMgj7xGKGXT"),
    ("roland", "character", "_2g1adXnHXcK62pVzGHUBm"),
    ("rev", "character", "_DGkc2ALEYzNJ6mqGCW1KC"),
    ("radek", "character", "_4bazKCAbPMmc19HzHAphC"),
    ("noah", "character", "_r42cVzMjcGTAx7bR1DQVt"),
    ("nixara", "character", "_fmzBDjDn3Gnq2hXKy7tY6"),
    ("nikolai", "character", "_AdCJWrQaTgC7xkPQECrtK"),
    ("malachia", "character", "_rAcN9GXD1Le4WxY28e49W"),
    ("mac", "character", "_YY8VbpgzYk4dfFAL78rM3"),
    ("logan", "character", "_JL37wK9PQMNDChULCDrWj"),
    ("loewe", "character", "_E2A8prBrWg1q9zNjAR7kQ"),
    ("kian", "character", "_kc7TyfPDQwUALKXcmTMxQ"),
    ("jasper", "character", "_x3VY2kcbaDbKyCqywGeET"),
    ("jasmin", "character", "_mfjaQDYUnAhLG8UggXg6N"),
    ("janice", "character", "_DKY9cDLMUaYpELYAdckH2"),
    ("iordan", "character", "_QfcJQRWUV2yfHGUUjLD8V"),
    ("hank", "character", "_4GdzX4McREFg4zRpEqth2"),
    ("griven", "lexicon", "_FkXtyrhQMhCpg7N6gm1Wm"),
    ("Goran", "character", "_JQGgmwyA3qRaTLWck3GjX"),
    ("finn", "character", "_PQHGb4gL2LwDhNDrLFa3A"),
    ("fenris-full", "character", "_wpMTPQ2VVA2pWqJ3cMztJ"),
    ("fade", "character", "_mbBqR74dFceBFB4YegpyN"),
    ("eris", "character", "_q1n7hcz23ThY63JGEjdNq"),
    ("erik", "character", "_d44gDc8N18kkbEhAcfUCG"),
    ("edric", "character", "_YJQ4cjdrT7brm7HWVkf3K"),
    ("dullahan", "character", "_F8ee4UpyLr7Fyr69KKhzV"),
    ("dominic", "character", "_dDXdeJrcYHbwagGFQVKQR"),
    ("danny", "character", "_VGAN3gQXchpTC2VFAcKUH"),
    ("chase", "character", "_TLxzk97WmgYCA47nkDCVy"),
    ("brak", "character", "_AycV4d9dJRBakCmdH4q4J"),
    ("barkley", "character", "_EXFAYyRCjRU19eebCFfXz"),
    ("ballantine", "character", "_13rj1V7hPaJ2QederUYkx"),
    ("bailey", "character", "_eF7HAqWkLLYhQwt2tm4rn"),
    ("aries", "character", "_F4qM3efBRVyQnXXUxVqH7"),
    ("ariadne", "character", "_q1rYKHndN64QUgjHQazXB"),
    ("alyssa", "character", "_MXcEC8Y6B3BNm3b1ttHj6"),
    ("alistar", "lexicon", "_daK4mwDzDLbCYQn4j2JpM"),
    ("alicia", "character", "_8CCMxWyPxRBaC1f2ycDqe")
]

print(f"Total mappings verified: {len(mapping)}")
for title, typ, target_id in mapping:
    target = chars.get(target_id) if typ == 'character' else lex.get(target_id)
    name = target.get('display_name') or target.get('name')
    print(f"[{typ:9s}] Gallery '{title:12s}' -> {name} ({target_id})")

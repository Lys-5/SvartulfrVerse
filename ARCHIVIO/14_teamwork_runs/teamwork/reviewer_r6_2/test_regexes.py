import re
import json

with open('FINAL/Svartulfr_NPC_Primary.json', 'r', encoding='utf-8') as f:
    primary = json.load(f)

targets = ['4NzXF4_0hYxmN7Idltzpw', 'ijy8vrlphNv19-p-gbYuY', 'YCxAqNoShpefVvk0_Pc7i', 'ekdQjq63xP7HtNuaPQJQE', 'RM6rcwv8MlY1XWaCTQp0M', 'alyssa_world_dossier_2b54a223', 'Vcj4h2TL4Usola2A4OOl6']

entries_map = {e.get('entry_id'): e for e in primary['entries']}

test_cases = {
    '4NzXF4_0hYxmN7Idltzpw': [
        ('Scarlett: "Hi there"', True),
        ('Scarlett Rose: "Let us go"', True),
        ('\n  Scarlett: "Wait"', True),
        ('Scarlett said hello', False),
        ('NotScarlett: "Nope"', False)
    ],
    'YCxAqNoShpefVvk0_Pc7i': [
        ('Russ: "What do you want?"', True),
        ('Russell Sinclair: "Later."', True),
        ("Russell 'Russ': \"Yo\"", True),
        ('\nRuss Sinclair: "Hey"', True),
        ('Russia: "No"', False)
    ],
    'ekdQjq63xP7HtNuaPQJQE': [
        ('Stan: "Whatever"', True),
        ('Stanley Davies Jr.: "Check this out"', True),
        ('Stanley Davies: "Yo"', True),
        ('Standard: "No"', False)
    ],
    'RM6rcwv8MlY1XWaCTQp0M': [
        ('Jared: "Clear out"', True),
        ('J-Man: "Let\'s hit it"', True),
        ('Jared Thompson: "Ready"', True),
        ('Jared is ready', False)
    ],
    'alyssa_world_dossier_2b54a223': [
        ('Alyssa: "Jasper, stay close."', True),
        ('Alyssa Hvit: "Listen."', True),
        ('White Moon: "Silence."', True),
        ('\n  Alyssa Douglas: "Hello"', True),
        ('Alyssa walked away', False)
    ],
    'Vcj4h2TL4Usola2A4OOl6': [
        ('Jasper: "I am in."', True),
        ('Jasper Svartr: "Hacked."', True),
        ('Shadow Wolf: "Clear."', True),
        ('Jasper Douglas: "Yo"', True),
        ('Jasper jumped', False)
    ]
}

print("=== TESTING REGEX ACTIVATION PATTERNS ===")
all_passed = True
for tid, cases in test_cases.items():
    entry = entries_map[tid]
    pattern_str = entry['avatar_activation_regex']
    reg = re.compile(pattern_str)
    for text, expected in cases:
        match = bool(reg.search(text))
        if match != expected:
            print(f"FAILED: {entry['name']} on {text!r}: got {match}, expected {expected}")
            all_passed = False
        else:
            print(f"PASSED: {entry['name']} on {text!r} -> {match}")

if all_passed:
    print("\nALL REGEX PATTERNS PASSED TEST SUITE!")

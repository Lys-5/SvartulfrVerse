lines = open('scratch/all_greetings_dump.txt', encoding='utf-8').readlines()
print('Total lines in dump:', len(lines))
suspects = []
for i, line in enumerate(lines):
    s = line.strip()
    if s.startswith('L') and ':' in s:
        actual_text = s.split(':', 1)[1].strip()
        if actual_text.startswith('"'):
            continue
        if ':' in actual_text:
            prefix = actual_text.split(':', 1)[0].strip()
            # If prefix looks like a name or tag
            if len(prefix.split()) <= 4 and not any(p in prefix.lower() for p in ['http', 'time', 'date', 'warning', 'note', 'code', 'room', 'section', 'hall', 'floor', 'tier']):
                suspects.append((i, prefix, actual_text))

print(f"Total suspects found: {len(suspects)}")
for i, p, t in suspects:
    print(f"  Line {i} [{p}]: {t[:80]}")

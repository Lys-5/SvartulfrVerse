with open('scratch/real_chars_list.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

done = [
    'adrian locke', 'finn', 'alistair deville', 'cato', 'vasile ionescu',
    'garrett locke', 'roger', 'harlow macgregor', 'bram beaumont',
    'atlas teague', 'arthur grey', 'jake thompson', 'kîwêtin', 'kiwetin', 'vargus', 'sawyer shephard'
]

print(f'Total in list: {len(lines)}')

remaining = []
for name in lines:
    is_done = False
    for d in done:
        if d in name.lower():
            is_done = True
            break
    if not is_done:
        remaining.append(name)

print(f'Remaining: {len(remaining)}')
print('Next 15 candidates:')
for i, r in enumerate(remaining[:15]):
    print(f'{i+1}. {r}')

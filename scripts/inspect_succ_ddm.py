import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

for p_name in ['succ', 'ddm']:
    fname = f'exports/portal_{p_name}_extracted.json'
    with open(fname, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"\n=======================================================")
    print(f"       ISPEZIONE DETTAGLIATA PORTALE: {p_name.upper()} ")
    print(f"=======================================================")
    for sec_id, s in data['sections'].items():
        imgs = s['images']
        print(f"\n--- SEZIONE: {sec_id} ({s['title']}) | Img: {len(imgs)} ---")
        for line in s['lines'][:20]:
            print("  ", line)
        if imgs:
            print("   Immagini:")
            for img in imgs:
                print(f"     * [{img['alt']}] {img['url']}")

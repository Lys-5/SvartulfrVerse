import requests
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
out_dir = ROOT / 'scratch' / 'lorebook_chunks'

chunks = [
    '/32697-2c943326ca1bc2fe.js',
    '/7573-ba8e396e99b1c700.js',
    '/86411-8f166ec31f689b71.js',
    '/38027-795193926500136e.js',
    '/77818-c9463c8edce6c041.js',
    '/61929-1ee7eb8e23a0548b.js',
    '/20603-3c8710ebcd658153.js',
    '/80873-830bebdfeeb356c2.js',
    '/48657-d844c7396d311699.js',
    '/99818-0d103e9ed7cc9559.js',
    '/24088-bc750791df8083cd.js',
    '/47143-664487fdc18cadef.js',
    '/65033-19d48eb20df46b34.js',
    '/50136-8ac254867171181a.js',
    '/59925-988e7a2c6652d2a1.js',
    '/9219-5349c9f9cd65f211.js',
    '/72022-7182c05c24112057.js',
    '/81038-49523cc7fb63b72d.js',
    '/16646-35780b4f3b0e541a.js',
    '/61732-a6891a763708cf2c.js',
]

headers = {'User-Agent': 'AuditorBot/1.0'}
for c in chunks:
    clean_name = c.split('/')[-1]
    out_file = out_dir / clean_name
    if not out_file.exists():
        url = 'https://app.wyvern.chat/_next/static/chunks' + c
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            out_file.write_text(resp.text, encoding='utf-8')
            print(f"Downloaded {clean_name}")

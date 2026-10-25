import requests
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
out_dir = ROOT / 'scratch' / 'lorebook_chunks'

chunks_to_check = [
    '8e1d74a4-32480693881c9e48.js',
    '70e0d97a-dc30772996c90de2.js',
    '54a60aa6-bda6577d48b98280.js',
    '06bf0ff1-66116c716b17ee21.js',
    '45412-3c7bf8f7caeb9557.js',
    '89209-ebd67c433bfdfb07.js',
    '82684-8b5c7506fe32fabb.js',
    '48280-1ebf80ade37b7962.js',
    '82451-b1de6fd77b2cd59a.js',
    '51112-51ceff4bccf391df.js',
    '45528-fb584fa844781a9f.js',
    '87077-cb557a435e455192.js',
    '76438-807d5262e1aff7e8.js',
    '33959-0509fc97d0ec06f3.js',
    '86569-1de93274d3f64c31.js',
    '83840-065c925af9ce7024.js',
    '45157-46cf87921fe31edb.js',
    '62153-80da69e6b7a84852.js',
    '11766-1e2297e5d3b2df06.js',
    '99424-7f608d672232ed88.js',
    '20358-3e3c33ab9f883bf2.js',
    '53944-e2a3f3ea28ad0416.js',
    '65630-54573550e723d84a.js',
    '50835-1ff2ef6353be10bd.js',
    '21758-ab5b7c8ff0701362.js',
    '55076-255abccd1a2660b8.js',
    '56621-741387c0839fff9f.js',
    '81904-87bfa0aca229c4ac.js',
    '93094-a08d45770dd8eeac.js',
    '76828-46f275c8256af999.js',
    '15526-e47b6b9b4c1b63ba.js',
    '54866-135b2f0269cfe519.js',
]

headers = {'User-Agent': 'AuditorBot/1.0'}
for c in chunks_to_check:
    fpath = out_dir / c
    if not fpath.exists():
        r = requests.get('https://app.wyvern.chat/_next/static/chunks/' + c, headers=headers)
        if r.status_code == 200:
            fpath.write_text(r.text, encoding='utf-8')
    if fpath.exists():
        txt = fpath.read_text(encoding='utf-8')
        if '84871:' in txt or 'getLorebookGalleryImages' in txt:
            print("FOUND in", c)
            pos = txt.find('getLorebookGalleryImages')
            if pos != -1:
                print(' '.join(txt[max(0, pos-100):min(len(txt), pos+400)].split()))

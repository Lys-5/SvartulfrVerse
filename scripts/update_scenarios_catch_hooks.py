import urllib.request
import json
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

SCENARIO_UPDATES = [
    {
        'id': '_Kn2DFVwyUgkVGz9UWUnBF',
        'title': 'Fumo di Gomma, Birra e Cloro: Il Branco dei Nomads',
        'tagline': 'Una piscina tra i chopper, il ruggito dei motori e un gigante Oni pronto a spezzare chiunque osi guardarla.',
        'location_id': '_DJxYBCM7rNrXMj1WracGM'
    },
    {
        'id': '_7X4UXynjEUKbQhPDHxVRr',
        'title': "Patti nell'Ombra: L'Audizione Segreta con Zeera",
        'tagline': 'Un colloquio clandestino alla clinica Aetheris: firmare il contratto prima che la famiglia Douglas scopra la fuga.'
    },
    {
        'id': '_X86JF72TG4p2DYqw7LzRp',
        'title': 'Maschere, Brividi e Sorority: Notte di Sangue alla Theta',
        'tagline': 'Tra incantesimi proibiti e drink al neon, la notte piu sfrenata e pericolosa del campus SUCC.'
    },
    {
        'id': '_nMaPEAzNA8rQc82NFgXRU',
        'title': 'Basso Distorto e Sguardi da Lupo: Sabato Sera al Sidewinders',
        'tagline': "I Grave Mistake sul palco, birra ghiacciata e la presenza rassicurante e letale dello zio Logan nell'angolo buio."
    },
    {
        'id': '_XWFqGmaTPkbpbFQzargbf',
        'title': 'Impatto sul Campo dei Bulls: Lo Scontro con Jared',
        'tagline': "Un passaggio fuori traiettoria al Bulls Stadium e l'incontro con il quarterback d'oro della SUCC."
    },
    {
        'id': '_p1Ffq22CTwVywz1CFQBfF',
        'title': 'Oltre i Cancelli della Villa: Il Primo Passo a Solarton',
        'tagline': "L'odore di caffe all'alba, l'ansia del primo giorno e il salto nel mondo oltre la fortezza dei Douglas."
    },
    {
        'id': '_h7N17PhK4ag3GxM8Bgr8g',
        'title': 'Overclock Notturno: Il Rave Clandestino di DJ Frequency',
        'tagline': "Bypassare i radar del Pentagono di papa per far tremare un magazzino di LA a colpi di synth abissali."
    },
    {
        'id': '_h7UQKNmxNJP8e7Jq1mEVL',
        'title': 'Asfalto e Liberta: Due Settimane On the Road con Logan',
        'tagline': "Niente guardie, niente regole: solo la Harley, motel sulla Route e l'odore del vento dell'Ovest."
    },
    {
        'id': '_F3AKNnAjh2UwUaJe9kc6A',
        'title': "L'Ombra del Primo Padre: Il Compleanno dei Gemelli Douglas",
        'tagline': 'Branchi da tutto il continente per il diciannovesimo anno: quando la leggenda millenaria di Wulfnic invade la tua festa.'
    },
    {
        'id': '_XwKb3hg1wG7gNgAdfGETr',
        'title': 'Reclute sotto Scorta: Visita Tattica al Campus SUCC',
        'tagline': 'Scegliere il college con un padre patriarca e un cyborg da guerra al seguito che scansiona ogni matricola.'
    },
    {
        'id': '_RL8HD1PbxLzNARyrHqqAn',
        'title': "Il Bivio del Patriarca: L'Ultima Scelta prima di Maggio",
        'tagline': "Lettere di ammissione sul tavolo di noce, il silenzio della sera e la domanda piu difficile di Erik."
    }
]

def update_scenarios():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    
    print(f"Updating {len(SCENARIO_UPDATES)} scenarios with catch hook titles and taglines...")
    
    for item in SCENARIO_UPDATES:
        sid = item['id']
        url = f'https://app.wyvern.chat/api/worlds/scenarios/{sid}'
        
        payload = {
            'title': item['title'],
            'name': item['title'],
            'tagline': item['tagline']
        }
        if 'location_id' in item:
            payload['location_id'] = item['location_id']
            
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers={**headers, 'Content-Type': 'application/json'},
            method='PUT'
        )
        with urllib.request.urlopen(req) as resp:
            status = resp.status
            
        # GET verify
        get_req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(get_req) as resp:
            v = json.loads(resp.read().decode('utf-8'))
            
        ver_title = v.get('title') or v.get('name')
        ver_tagline = v.get('tagline')
        ver_loc = v.get('location_id')
        ok = (ver_title == item['title'])
        print(f"[{'OK' if ok else 'FAIL'}] [{sid}] {ver_title}")
        print(f"       Tagline: {ver_tagline}")
        if 'location_id' in item:
            print(f"       Location ID: {ver_loc}")

if __name__ == '__main__':
    update_scenarios()

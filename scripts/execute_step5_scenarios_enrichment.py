import os
import sys
import json
import time
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

def api_get(resource, entity_id, token):
    url = f"{API_BASE}/{resource}/{entity_id}?world_id={WORLD_ID}"
    headers = {
        'Authorization': f'Bearer {token}',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def api_put(resource, entity_id, payload, token):
    url = f"{API_BASE}/{resource}/{entity_id}?world_id={WORLD_ID}"
    data = json.dumps(payload).encode('utf-8')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    print("--- STEP 5: ARRICCHIMENTO DEGLI 11 SCENARI (SCENE INSTRUCTIONS & ALTERNATE SCENES) ---")

    # Mappatura istruzioni di regia e scene aggiuntive
    scenarios_data = [
        # 1. Fumo di Gomma
        {
            'id': '_Kn2DFVwyUgkVGz9UWUnBF',
            'name': 'Fumo di Gomma, Birra e Cloro: Il Branco dei Nomads',
            'scene_instructions': 'Focus on the raw, rowdy energy of the Ironhorn Nomads clubhouse. Emphasize Marek possessive, unapologetic alpha protection over {{user}} amidst towering Oni bikers and roaring choppers. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.'
        },
        # 2. Stage Formativo HSK
        {
            'id': '_7X4UXynjEUKbQhPDHxVRr',
            'name': 'Stage Formativo HSK: Il Colloquio e la Borsa di Studio',
            'scene_instructions': 'Direct the interaction around high-stakes academic and corporate evaluation. Radek and Goran scrutinize {{user}} for tactical capability and pack synergy under Hunters Guild regulations. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.'
        },
        # 3. Halloween dei BRO
        {
            'id': '_X86JF72TG4p2DYqw7LzRp',
            'name': 'Halloween dei BRO: La Festa di Beta Rho Omega',
            'scene_instructions': 'Depict a wild, chaotic collegiate frat house party. Balance the humorous jock antics of Rick Howell and Jared with intense sensory pheromones, crowded rooms, and campus romance. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.'
        },
        # 4. Basso Distorto
        {
            'id': '_nMaPEAzNA8rQc82NFgXRU',
            'name': 'Basso Distorto e Sguardi al Bancone: Primo Incontro con Mac',
            'scene_instructions': 'Atmospheric, smoky underground club scene at The Verve. Highlight the pounding bass, motorcycle grease, cold beer, and Mac quiet, brooding intensity behind the counter. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.'
        },
        # 5. Impatto sul Campo dei Bulls (Con Seconda Scena)
        {
            'id': '_XWFqGmaTPkbpbFQzargbf',
            'name': 'Impatto sul Campo dei Bulls: Lo Scontro con Jared',
            'scene_instructions': 'High physical tension on the gridiron. Emphasize Jared Thompson imposing minotaur mass, competitive fire, and athletic pride. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.',
            'add_scene': {
                'id': 'scene-jared-locker-room',
                'description': 'Tunnel e Spogliatoi del Bulls Stadium post-allenamento',
                'time_override': 17,
                'scene_text': """=>Narrator:
Lunedi' 2 settembre 2024, ore 17:15 - Tunnel degli Spogliatoi, Bulls Stadium, campus SUCC

Il silenzio dell'allenamento pomeridiano e' rotto solo dallo scroscio violento delle docce e dal tonfo sordo dei caschi da football gettati sulle panche di legno massiccio. L'aria nei corridoi di cemento e' densa di vapore caldo, linimento muscolare e dell'inconfondibile odore acre di feromoni da minotauro in piena scarica di adrenalina agonistica.

Jared Thompson siede sulla panca centrale, con le fasce dei polsi ancora mezze srotolate e l'asciugamano attorno al collo massiccio. I suoi occhi scuri fissano l'ingresso del tunnel dove compare {{user}}, attirato dal richiamo di Coach Mack.

=>Jared:
"Credevi che bastasse reggere il primo impatto sul sintetico per guadagnarti il rispetto in questo spogliatoio?" Jared si alza in piedi, torreggiando con i suoi due metri e venticinque di muscoli taurini, il petto ancora ansimante. "Qui dentro non siamo a una lezione teorica di biologia. Se vuoi dividere il campo con i Bulls, devi dimostrarmi che non andrai in pezzi quando il gioco si fara' pesante per davvero."

=>Narrator:
Jared fa un passo avanti, la presenza fisica imponente che restringe lo spazio vitale nel corridoio, attendendo di valutare se {{user}} reggera' il suo sguardo senza abbassare gli occhi."""
            }
        },
        # 6. Primo Giorno di College (Con Seconda Scena)
        {
            'id': '_p1Ffq22CTwVywz1CFQBfF',
            'name': 'Primo Giorno di College: Partenza da Villa Douglas',
            'scene_instructions': 'Capture the bittersweet transition from the protective fortress of Villa Douglas to collegiate autonomy at SUCC. Highlight family bonds, Erik heavy paternal gaze, and sibling support. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.',
            'add_scene': {
                'id': 'scene-college-arrival-clocktower',
                'description': 'Arrivo al Griffin Clocktower sul Campus SUCC',
                'time_override': 9,
                'scene_text': """=>Narrator:
Mercoledi' 28 agosto 2024, ore 09:15 - Griffin Clocktower, campus SUCC, Solarton

I rintocchi profondi del Griffin Clocktower scandiscono l'inizio del nuovo anno accademico, riecheggiando tra i prati soleggiati del Lunar Quad e le arcate gotiche della vicina Basilica Library. Il campus e' invaso da un turbine caotico di matricole, trolley che sferragliano sui marciapiedi di pietra e studenti di ogni specie che si scambiano saluti e sguardi di ricognizione.

Il Suv blindato della DCC Security rallenta all'ombra delle querce monumentali, attirando immediatamente l'attenzione dei passanti. Quando la portiera si apre e {{user}} scende con il borsone in spalla, l'odore salmastro della costa californiana si mescola al profumo di pino delle montagne di Blackwood.

=>Jasper:
Jasper Douglas abbassa il finestrino oscurato dal lato passeggero, gli occhiali da sole a specchio e un ghigno ironico sul volto affilato.

"Siamo arrivati, fratellino. Niente scorta visibile a piedi finche' resti dentro il perimetro universitario, parola di Kaladin. Ma ricordati: se qualche jock dei Bulls o qualche professore impiccione prova a fare il gradasso, non farti pregare a chiamare. Io e Alyssa siamo a un quarto d'ora di moto da qui."

=>Narrator:
Jasper fa un cenno d'intesa con due dita, prima che il motore del mezzo riparta con un rombo sommesso, lasciando {{user}} al centro del piazzale della SUCC, pronto a muovere i primi passi nella vita universitaria."""
            }
        },
        # 7. Overclock Notturno
        {
            'id': '_h7N17PhK4ag3GxM8Bgr8g',
            'name': 'Overclock Notturno: Il Rave Clandestino di DJ Frequency',
            'scene_instructions': 'High-octane cyberpunk nightlife. Lasers, strobes, hyper-dense synthetic beats, and neuro-acoustic thrills. Jasper Douglas guides {{user}} through the clandestine tech crowd. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.'
        },
        # 8. Pausa d'Autunno on the Road (Con Seconda Scena)
        {
            'id': '_h7UQKNmxNJP8e7Jq1mEVL',
            'name': 'Pausa d\'Autunno on the Road: Viaggio con Zio Logan',
            'scene_instructions': 'Rugged open-highway journey along Route 101. Cold coastal winds, rumble of V-twin engines, leather, and Logan seasoned, laconic mentorship. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.',
            'add_scene': {
                'id': 'scene-road-trip-coastal-diner',
                'description': 'Sosta Notturna al Neptune Diner sulla Pacific Coast Highway',
                'time_override': 22,
                'scene_text': """=>Narrator:
Giovedi' 28 novembre 2024, ore 22:30 - Neptune Diner, Pacific Coast Highway, a nord di Ventura

L'insegna al neon blu e rosso del Neptune Diner ronza nella nebbia salmastra che risale dalle scogliere del Pacifico. Fuori, i chopper di Logan e della scorta borbottano al minimo sul piazzale di ghiaia prima di spegnersi, lasciando spazio al fragore continuo delle onde oceaniche.

All'interno, il locale e' quasi deserto: una cameriera annoiata dietro il bancone di formica lucida e una caraffa di caffe' nero americano che gorgoglia sulla piastra riscaldata. Logan spinge la porta a vetri, facendo tintinnare il campanellino d'ottone, la giacca di pelle pesante ancora fredda per l'aria umida della Route 101.

=>Logan:
"Prendi il tavolo in fondo vicino alla finestra," dice Logan a voce bassa, togliendosi i guanti da guida rinforzati e squadrando la sala con naturale riflesso da sentinella. "Duecento miglia di curve costiere aprono lo stomaco anche a un lupo di citta'. Caffe' bollente, una fetta di torta di mele e poi decidiamo se tirare dritti fino all'alba o fermarci un paio d'ore a dormire."

=>Narrator:
Logan si siede di fronte a {{user}}, versando lo zucchero nel caffe' scuro mentre il calore del diner scioglie il gelo della notte on the road, gli occhi ambrati del veterano che osservano {{user}} con burbero ma sincero affetto familiare."""
            }
        },
        # 9. Solstizio d'Inverno (Con Seconda Scena)
        {
            'id': '_F3AKNnAjh2UwUaJe9kc6A',
            'name': 'Solstizio d\'Inverno: La Grande Veglia di Yule con Wulfnic',
            'scene_instructions': 'Sacred, ancient Norse werewolf ritual. Majestic pine halls, crackling hearth fires, roasted meats, mead, and the deep primordial authority of Wulfnic Baleygr. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.',
            'add_scene': {
                'id': 'scene-yule-vigil-sacred-yew',
                'description': 'La Veglia Notturna sotto l\'Albero Sacro con i Firstborn',
                'time_override': 23,
                'scene_text': """=>Narrator:
Sabato 21 dicembre 2024, ore 23:45 - Bosco Sacro della Longhouse, rive del fiume Yarrow

Mentre nella grande sala della Longhouse continuano a risuonare i canti e i brindisi del banchetto di Yule, il Bosco Sacro e' immerso in un silenzio primordiale, rotto soltanto dallo scricchiolio della brina sotto gli stivali e dal sussurro del fiume Yarrow che lambisce le radici millenarie dell'Albero Sacro.

La luce lunare filtra tra i rami sempreverdi del tasso portato dall'Islanda nel 1022, illuminando la figura gigantesca di Wulfnic Baleygr. Il Primo Alpha e' avvolto nel suo pesante mantello di pelliccia scura, appoggiato al bastone di frassino intagliato, con Zefir e Ut fermi ai suoi fianchi come statue d'ombra e pietra.

=>Wulfnic:
"Vieni avanti nel cerchio delle radici," la voce di Wulfnic e' un tuono calmo che risuona direttamente nella mente e nelle ossa di {{user}}. "Mille inverni fa ho piantato questo ramo quando questa terra non conosceva il nome dei mortali che ora vi abitano. Il sangue dei Douglas scorre forte nelle tue vene, ma e' nella notte piu' lunga dell'anno che ogni lupo deve ricordare a chi appartiene la sua anima."

=>Narrator:
Wulfnic volge il suo unico occhio azzurro brillante verso {{user}}, mentre la benda sull'orbita sinistra pare pulsare di una remota eco divina. L'odore di terra bagnata, corteccia di tasso e fumo sacro avvolge la scena, sigillando un momento di pura e austera comunione tra generazioni."""
            }
        },
        # 10. Reclute sotto Scorta
        {
            'id': '_XwKb3hg1wG7gNgAdfGETr',
            'name': 'Reclute sotto Scorta: Visita Tattica al Campus SUCC',
            'scene_instructions': 'Military precision juxtaposed with civilian collegiate life. Major Kaladin and DCC operators maintain 360-degree security while navigating student quads. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.'
        },
        # 11. Fine del Primo Anno
        {
            'id': '_RL8HD1PbxLzNARyrHqqAn',
            'name': 'Fine del Primo Anno: Il Bivio in Cucina con Erik',
            'scene_instructions': 'Intimate, emotionally charged family conversation in the dawn quiet of Villa Douglas. Erik weighs his protective instincts against {{user}} growth and future in the pack. Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash.'
        }
    ]

    for item in scenarios_data:
        try:
            sid = item['id']
            sc_live = api_get('scenarios', sid, token)
            scenes = sc_live.get('premade_scenes', [])
            
            # Aggiungi seconda scena se definita e non già presente
            if 'add_scene' in item:
                new_scene = item['add_scene']
                if not any(s.get('id') == new_scene['id'] for s in scenes):
                    scenes.append(new_scene)

            payload = {
                'scene_instructions': item['scene_instructions'],
                'premade_scenes': scenes
            }
            res = api_put('scenarios', sid, payload, token)
            print(f"  [OK] Scenario '{item['name']}' ({sid}): SceneInstrLen={len(res.get('scene_instructions', ''))}, Scenes={len(res.get('premade_scenes', []))}")
        except Exception as e:
            print(f"  [ERRORE] Scenario '{item['name']}': {e}")
        time.sleep(0.3)

    print("\n--- STEP 5 COMPLETATO CON SUCCESSO! ---")

if __name__ == '__main__':
    main()

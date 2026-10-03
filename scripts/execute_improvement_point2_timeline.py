import os
import sys
import json
import time
import urllib.request

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

TIMELINE_EVENTS = [
    {
        'name': 'Consacrazione dei Nove Firstborn',
        'title': 'La Consacrazione dei Nove Firstborn',
        'description': 'Il dio-lupo primordiale Fenris consacra i Nove Primi Nati nel Grande Nord scandinavo, legando per sempre il loro sangue alla divinita e bloccando il loro invecchiamento biologico.',
        'content': 'La nascita dei Primi Nati segna l\'inizio dell\'era ancestrale dei lupi mannari. Wulfnic, Ut e Zefir ricevono il dono e la maledizione del sangue divino.',
        'timeline_position': 1552752,
        'start_position': 1552752,
        'event_type': 'point',
        'display_order': 1,
        'tags': ['Firstborn', 'Divine Blood', 'Historical'],
        'related_characters': ['_W9PLYt9ERTBJBXqKQL2en', '_NYtBzeKNkm3pedHMnYaka', '_FJhtBq4xUM4aUWpaJAPYF', '_wpMTPQ2VVA2pWqJ3cMztJ'],
        'related_locations': ['_RXULtwFjxCBUcxBbTfWrh']
    },
    {
        'name': 'Fondazione di House Douglas',
        'title': 'La Fondazione di House Douglas',
        'description': 'Lord Cornelius Douglas ottiene la carta coloniale e formalizza la fondazione di House Douglas, separandosi dalle dispute della corte britannica per costruire una dinastia autonoma d\'oltremare.',
        'content': 'Ha inizio la linea dinastica coloniale che portera i Douglas a diventare una delle casate Pureblood piu ricche e influenti del Nuovo Mondo.',
        'timeline_position': 7351896,
        'start_position': 7351896,
        'event_type': 'point',
        'display_order': 2,
        'tags': ['House Douglas', 'Pureblood', 'Origins'],
        'related_characters': ['_rJKYcCt61hQa8XRamHEdM', '_jeJTbxLcrYWXNWYPDx4ph'],
        'related_locations': []
    },
    {
        'name': 'Insediamento a Seven Hills',
        'title': 'L\'Insediamento a Seven Hills',
        'description': 'La famiglia Douglas acquisisce il territorio strategico di Seven Hills affacciato sull\'Oceano Pacifico, erigendo Villa Douglas e trasformandola nel bastione centrale del Branco.',
        'content': 'Acquisto formale delle scogliere e dei colli di Blackwood City. Inizio dei lavori della tenuta fortificata di Villa Douglas sotto la guida di Magnus ed Elizabeth.',
        'timeline_position': 9295248,
        'start_position': 9295248,
        'event_type': 'point',
        'display_order': 3,
        'tags': ['Villa Douglas', 'Territory', 'Seven Hills'],
        'related_characters': ['_jeJTbxLcrYWXNWYPDx4ph', '_EwPN1te7qtUKYEx4NLgag', '_d44gDc8N18kkbEhAcfUCG'],
        'related_locations': ['_9H2EmzRm92QxBpkmJUR1z', '_EwMMJ7KEg9ATJ3mTXBaha']
    },
    {
        'name': 'Fondazione della SUCC',
        'title': 'La Fondazione della SUCC',
        'description': 'Il patriarca Archer Wolfwood fonda la Supernatural University of Central California a Solarton, istituendo il primo santuario accademico riconosciuto sia dalle autorita sovrannaturali che da quelle umane.',
        'content': 'La nascita dell\'ateneo di Solarton crea un territorio neutrale di pace garantita tra le specie demi-umane, magiche e i branchi territoriali.',
        'timeline_position': 9500448,
        'start_position': 9500448,
        'event_type': 'point',
        'display_order': 4,
        'tags': ['SUCC', 'Solarton', 'Academy'],
        'related_characters': ['_6hc62Ay9tVBXecnAfmqdU'],
        'related_locations': ['_j67Dp2PVwFCpdrfWRYV2M', '_hbH9FftNr3AzzVVDyJHgg']
    },
    {
        'name': 'Morte di Nixara Bloodmoon e Nascita dei Gemelli',
        'title': 'La Morte di Nixara Bloodmoon e Nascita dei Gemelli',
        'description': 'Nixara Bloodmoon da alla luce i gemelli Jasper e Alyssa durante una violenta crisi territoriale; la sua morte lascia Erik solo alla guida della famiglia e segna indelebilmente l\'anima del branco.',
        'content': 'La perdita della White Moon devasta Erik Douglas, innescando l\'iper-protettivita ossessiva sui figli e segnando la nascita dell\'ultima Omega di sangue puro.',
        'timeline_position': 10320312,
        'start_position': 10320312,
        'event_type': 'point',
        'display_order': 5,
        'tags': ['Tragedy', 'Founding Bloodline', 'Douglas Family'],
        'related_characters': ['_fmzBDjDn3Gnq2hXKy7tY6', '_d44gDc8N18kkbEhAcfUCG', '_MXcEC8Y6B3BNm3b1ttHj6', '_x3VY2kcbaDbKyCqywGeET'],
        'related_locations': ['_9H2EmzRm92QxBpkmJUR1z']
    },
    {
        'name': 'Incidente Gamma-7 e Fondazione DCC Security',
        'title': 'L\'Incidente Gamma-7 e Fondazione DCC Security',
        'description': 'I sopravvissuti dell\'unita militare d\'elite Gamma-7 vengono integrati nel conglomerato Douglas. Kaladin Nargathon e Marcus Thornfield fondano la DCC Security Division e il braccio tattico BlackWolf PMC.',
        'content': 'La riorganizzazione aziendale della DCC trasforma la sicurezza privata di Blackwood in una potenza militare d\'avanguardia, creando il legame tra Kaladin e la famiglia.',
        'timeline_position': 10444392,
        'start_position': 10444392,
        'event_type': 'point',
        'display_order': 6,
        'tags': ['DCC Security', 'Military', 'Gamma-7'],
        'related_characters': ['_b7QqV43D8pU1tewx4qenY', '_PCC1PLfcGrdw2VfMnhVcL', '_d44gDc8N18kkbEhAcfUCG'],
        'related_locations': ['_XD2gWgyhTYmDEXWkxMLer']
    },
    {
        'name': 'Present Day: Anno Accademico Contemporaneo',
        'title': 'Present Day: Inizio del Nuovo Anno Accademico',
        'description': 'Alyssa si prepara al primo anno universitario alla SUCC mentre la tensione tra il Consiglio di Blackwood, la DCC e i clan sotterranei raggiunge il culmine.',
        'content': 'L\'inizio dell\'anno accademico a Solarton apre tutti gli scenari contemporanei: il passaggio dalla fortezza di Seven Hills alla vita studentesca aperta.',
        'timeline_position': 10489952,
        'start_position': 10489952,
        'event_type': 'point',
        'display_order': 7,
        'tags': ['Present Day', 'SUCC', 'Current Era'],
        'related_characters': ['_MXcEC8Y6B3BNm3b1ttHj6', '_d44gDc8N18kkbEhAcfUCG', '_rAcN9GXD1Le4WxY28e49W', '_r42cVzMjcGTAx7bR1DQVt', '_x3VY2kcbaDbKyCqywGeET'],
        'related_locations': ['_9H2EmzRm92QxBpkmJUR1z', '_j67Dp2PVwFCpdrfWRYV2M']
    }
]

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.\n")

    print("--- PUNTO 2: CREAZIONE DEGLI EVENTI STORICI NELLA TIMELINE ---")
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    url = f"{API_BASE}/timeline-events?world_id={WORLD_ID}"

    for ev in TIMELINE_EVENTS:
        ev_payload = dict(ev)
        ev_payload['world_id'] = WORLD_ID
        try:
            req = urllib.request.Request(url, data=json.dumps(ev_payload).encode('utf-8'), headers=headers, method='POST')
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode('utf-8'))
            eid = res.get('id')
            title = res.get('title')
            pos = res.get('timeline_position')
            print(f"  [EVENT OK] {title[:40]:40} (ID: {eid}, ore: {pos})")
        except Exception as e:
            print(f"  [EVENT ERR] {ev['title'][:40]:40}: {e}")
        time.sleep(0.3)

    print("\n--- PUNTO 2 COMPLETATO CON SUCCESSO! ---")

if __name__ == '__main__':
    main()

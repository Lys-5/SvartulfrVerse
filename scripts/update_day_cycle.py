import os
import sys
import json
import requests
import uuid

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

def get_world(token, wid):
    url = f"{API_BASE}/worlds/{wid}"
    headers = {'Authorization': f'Bearer {token}'}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(f"GET world failed: {resp.status_code} {resp.text}")
    return resp.json()

def put_world(token, wid, body):
    url = f"{API_BASE}/worlds/{wid}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    resp = requests.put(url, headers=headers, json=body)
    if resp.status_code != 200:
        raise Exception(f"PUT world failed: {resp.status_code} {resp.text}")
    return resp.json()

def main():
    token = get_auth_token()
    print("Fetching world...")
    world = get_world(token, WORLD_ID)
    
    # We only send the field we want to update
    periods = [
      {
        "id": str(uuid.uuid4()),
        "name": "Dawn",
        "description": "La sottile nebbia costiera dell'alba si dirada sulla baia di Blackwood. La luce fredda e dorata del mattino illumina le palme e l'oceano Pacifico, mentre la città si risveglia.",
        "start": 5,
        "end": 7
      },
      {
        "id": str(uuid.uuid4()),
        "name": "Morning",
        "description": "Il sole luminoso della California splende alto. Il traffico, l'aria salmastra e il rumore della metropoli in pieno fermento fanno da sfondo alla giornata.",
        "start": 7,
        "end": 12
      },
      {
        "id": str(uuid.uuid4()),
        "name": "Afternoon",
        "description": "Un caldo pomeriggio californiano. L'asfalto rovente e la brezza del Pacifico si mescolano; le ombre si allungano mentre il sole inizia la sua lenta discesa verso ovest.",
        "start": 12,
        "end": 17
      },
      {
        "id": str(uuid.uuid4()),
        "name": "Dusk",
        "description": "Il tramonto infiamma il cielo sopra l'oceano con intense sfumature di ambra e viola. L'illuminazione al neon di Blackwood City si accende e gli istinti dei demi-umani iniziano ad acuirsi.",
        "start": 17,
        "end": 20
      },
      {
        "id": str(uuid.uuid4()),
        "name": "Nightfall",
        "description": "La notte avvolge la costa. Blackwood City pulsa di vita notturna, locali e luci metropolitane. L'odore della salsedine si mischia a quello dei predatori urbani che escono allo scoperto.",
        "start": 20,
        "end": 0
      },
      {
        "id": str(uuid.uuid4()),
        "name": "Witching Hour",
        "description": "Il cuore della notte. Il silenzio cala sulla città addormentata. È il momento in cui l'attività oscura, le infiltrazioni nei Dungeon e i raid dei branchi raggiungono il loro apice.",
        "start": 0,
        "end": 3
      },
      {
        "id": str(uuid.uuid4()),
        "name": "Dead of Night",
        "description": "Le ore più fredde e buie prima dell'alba. Una spessa coltre di umidità e foschia avvolge la costa. La città è deserta, territorio esclusivo di chi prospera nell'oscurità.",
        "start": 3,
        "end": 5
      }
    ]
    
    body = {
        "time_of_day_config": {
            "day_length": 24,
            "default_time": 12,
            "periods": periods
        }
    }
    
    print("Updating time_of_day_config...")
    put_world(token, WORLD_ID, body)
    print("Update successful!")

if __name__ == '__main__':
    main()

import urllib.request
import json
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

UPDATES = [
    {
        'id': '_MXcEC8Y6B3BNm3b1ttHj6',
        'name': 'Alyssa Douglas Bloodmoon',
        'birthdate': 10320312,
        'start_timeline_position': 10320312
    },
    {
        'id': '_YJQ4cjdrT7brm7HWVkf3K',
        'name': 'Edric Douglas',
        'birthdate': 10380312,
        'start_timeline_position': 10380312
    },
    {
        'id': '_EwPN1te7qtUKYEx4NLgag',
        'name': 'Elizabeth Duskwood',
        'birthdate': 9822648,
        'start_timeline_position': 9822648
    },
    {
        'id': '_rJKYcCt61hQa8XRamHEdM',
        'name': 'Lord Cornelius Douglas',
        'birthdate': 7044624,
        'start_timeline_position': 7044624,
        'end_timeline_position': 9018888
    },
    {
        'id': '_jeJTbxLcrYWXNWYPDx4ph',
        'name': 'Magnus Douglas III',
        'birthdate': 7372272,
        'start_timeline_position': 7372272
    },
    {
        'id': '_PCC1PLfcGrdw2VfMnhVcL',
        'name': 'Marcus Thornfield',
        'birthdate': 10154736,
        'start_timeline_position': 10154736
    },
    {
        'id': '_fmzBDjDn3Gnq2hXKy7tY6',
        'name': 'Nixara Bloodmoon',
        'birthdate': 10058472,
        'start_timeline_position': 10058472,
        'end_timeline_position': 10320312
    },
    {
        'id': '_NYtBzeKNkm3pedHMnYaka',
        'name': 'Ut Berg',
        'birthdate': 0,
        'start_timeline_position': 0
    },
    {
        'id': '_wpMTPQ2VVA2pWqJ3cMztJ',
        'name': 'Fenris',
        'birthdate': 0,
        'start_timeline_position': 0
    }
]

def fix_birthdates():
    token = get_auth_token()
    headers = {'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'}
    
    print("Fixing character birthdates and timeline positions...")
    for item in UPDATES:
        cid = item['id']
        name = item['name']
        c_url = f'https://app.wyvern.chat/api/worlds/characters/{cid}'
        
        payload = {
            'birthdate': item['birthdate'],
            'start_timeline_position': item['start_timeline_position']
        }
        if 'end_timeline_position' in item:
            payload['end_timeline_position'] = item['end_timeline_position']
            
        req = urllib.request.Request(
            c_url,
            data=json.dumps(payload).encode('utf-8'),
            headers={**headers, 'Content-Type': 'application/json'},
            method='PUT'
        )
        with urllib.request.urlopen(req) as resp:
            put_status = resp.status
            
        # GET verify
        get_req = urllib.request.Request(c_url, headers=headers)
        with urllib.request.urlopen(get_req) as resp:
            v = json.loads(resp.read().decode('utf-8'))
            
        ver_bd = v.get('birthdate')
        ver_st = v.get('start_timeline_position')
        ok = (ver_bd == item['birthdate'] and ver_st == item['start_timeline_position'])
        print(f"[{'OK' if ok else 'FAIL'}] {name:30} -> bd: {ver_bd}, st: {ver_st}")

if __name__ == '__main__':
    fix_birthdates()

import json
import urllib.request
import pathlib
import uuid

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRATCH = ROOT / 'scratch'
FINAL = ROOT / 'FINAL'

TOKEN = (SCRATCH / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0'
}

def build_mapped_travel_routes():
    # 1. Load canonical routes source
    p1 = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/updated_travel_routes.json'
    old_locs_file = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json'
    
    with open(p1, 'r', encoding='utf-8') as f:
        canonical_routes = json.load(f)
    with open(old_locs_file, 'r', encoding='utf-8') as f:
        old_locs = json.load(f)
        
    old_id_to_name = {l.get('id') or l.get('_id'): l.get('name') for l in old_locs}
    
    # 2. Load live locations for _YpX47fNraQFw2dD7TdycJ
    live_locs_path = SCRATCH / 'live_world__YpX47fNraQFw2dD7TdycJ_locations.json'
    with open(live_locs_path, 'r', encoding='utf-8') as f:
        live_locs = json.load(f)
        
    name_to_new_id = {l.get('name'): (l.get('id') or l.get('_id')) for l in live_locs}
    new_loc_ids = set(name_to_new_id.values())
    
    print(f"Loaded {len(canonical_routes)} canonical routes.")
    print(f"Loaded {len(live_locs)} live locations in World {WORLD_ID}.")
    
    mapped_routes = []
    seen_pairs = set()
    
    for r in canonical_routes:
        old_from = r.get('from_location_id')
        old_to = r.get('to_location_id')
        
        from_name = old_id_to_name.get(old_from)
        to_name = old_id_to_name.get(old_to)
        
        if not from_name or not to_name:
            raise ValueError(f"Could not resolve location names for route: {old_from} -> {old_to}")
            
        new_from_id = name_to_new_id.get(from_name)
        new_to_id = name_to_new_id.get(to_name)
        
        if not new_from_id or not new_to_id:
            raise ValueError(f"Could not map names to new IDs: '{from_name}' ({new_from_id}) -> '{to_name}' ({new_to_id})")
            
        # Avoid duplicate pairs
        pair_key = tuple(sorted([new_from_id, new_to_id]))
        if pair_key in seen_pairs:
            continue
        seen_pairs.add(pair_key)
        
        route_obj = {
            "id": r.get('id') or str(uuid.uuid4()),
            "from_location_id": new_from_id,
            "to_location_id": new_to_id,
            "bidirectional": r.get('bidirectional', True),
            "travel_time": r.get('travel_time', 0),
            "distance": r.get('distance') if r.get('distance') is not None else 1,
            "required_mediums": r.get('required_mediums') or ["land"],
            "description": r.get('description', f"Travel route connecting {from_name} and {to_name}."),
            "hidden": r.get('hidden', False)
        }
        
        mapped_routes.append(route_obj)
        
    print(f"Successfully mapped {len(mapped_routes)} unique bidirectional routes.")
    return mapped_routes

def deploy_travel_routes(routes):
    url = f"https://app.wyvern.chat/api/worlds/{WORLD_ID}"
    payload = {
        "travel_routes": routes,
        "free_travel": False
    }
    
    print(f"Sending PUT to {url} with {len(routes)} travel routes...")
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers=HEADERS,
        method='PUT'
    )
    with urllib.request.urlopen(req) as resp:
        print(f"World PUT Status: {resp.status}")
        updated_world = json.loads(resp.read().decode('utf-8'))
        
    # Verify with GET
    print("Verifying via GET...")
    verify_req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(verify_req) as v_resp:
        verified_world = json.loads(v_resp.read().decode('utf-8'))
        saved_routes = verified_world.get('travel_routes', [])
        print(f"Verified travel_routes count on live world: {len(saved_routes)}")
        print(f"Verified free_travel: {verified_world.get('free_travel')}")
        
    # Save local master snapshot
    out_final = FINAL / 'Svartulfr_World_Travel_Routes.json'
    with open(out_final, 'w', encoding='utf-8') as f:
        json.dump(saved_routes, f, indent=2, ensure_ascii=False)
    print(f"Saved travel routes snapshot to {out_final}")

    out_scratch = SCRATCH / 'live_world__YpX47fNraQFw2dD7TdycJ_travel_routes.json'
    with open(out_scratch, 'w', encoding='utf-8') as f:
        json.dump(saved_routes, f, indent=2, ensure_ascii=False)
    print(f"Saved travel routes snapshot to {out_scratch}")

if __name__ == '__main__':
    routes = build_mapped_travel_routes()
    deploy_travel_routes(routes)

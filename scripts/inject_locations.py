import sys
import json
import requests
import time

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api'

locations_tree = [
    {
        "name": "S.U.C.C. Main Campus",
        "description": "The Supernatural University of Central California. A pioneering integrated campus for humans and supernatural beings.",
        "children": [
            {
                "name": "Archer Wolfwood Hall",
                "description": "The magic-proofed main lecture hall building.",
                "children": [{"name": "Main Lecture Hall"}, {"name": "Classrooms"}]
            },
            {
                "name": "Basilica Library",
                "description": "A five-story library housing magical texts and bestiaries.",
                "children": [
                    {"name": "Study Rooms"}, 
                    {"name": "Magical Sections"}, 
                    {"name": "Trophy Room"}, 
                    {"name": "Basement Meeting Room 005"}
                ]
            },
            {
                "name": "Griffin Clocktower & Lunar Quad",
                "description": "The central plaza featuring a moon fountain and living gargoyles.",
                "children": [{"name": "Law & Engineering Theatres"}, {"name": "Nocturnal Club Space"}]
            },
            {
                "name": "Wyrm Dormitories",
                "description": "Sleek modern suite-style living.",
                "children": [
                    {"name": "North Wing (Human)"}, 
                    {"name": "South Wing (Supernatural)"}, 
                    {"name": "West & East Wings (Mixed)"}, 
                    {"name": "Sun/Moon Rooms"}, 
                    {"name": "Blood Bank"}
                ]
            },
            {
                "name": "St. Neptune & Bulls Stadium",
                "description": "The athletic complex for the Bears and the Bulls.",
                "children": [{"name": "Ice Rink"}, {"name": "Indoor Pool & Sauna"}, {"name": "Bulls Football Field"}]
            },
            {
                "name": "Unicorn Hall & Science Quarter",
                "description": "Accessible building and scientific labs.",
                "children": [{"name": "Greenhouse"}, {"name": "Specimen Containment"}, {"name": "Med/Bio Labs"}]
            },
            {
                "name": "Nocturnal Hall & Student Assoc.",
                "description": "Night classes and student support services.",
                "children": [{"name": "S.H.A. Meeting Room"}]
            },
            {
                "name": "Greek Row",
                "description": "Fraternity and Sorority housing.",
                "children": [
                    {"name": "Alpha Rho Omega (ARO)"}, 
                    {"name": "Alpha Sigma Sigma (ASS)"}, 
                    {"name": "Beta Rho Omega (BRO)"}, 
                    {"name": "Mu Omega Omega (MOO)"}, 
                    {"name": "Theta Iota Theta (TIT)"}
                ]
            }
        ]
    },
    {
        "name": "Solarton, CA",
        "description": "A vibrant, monster-friendly college town with a heavy werewolf population.",
        "children": [
            {
                "name": "Solarton Square",
                "children": [{"name": "Full Moon Market"}]
            },
            {
                "name": "Bricklane Mall",
                "children": [{"name": "Medusa's Salon"}, {"name": "Yeti Shack"}]
            },
            {"name": "Sidewinders Bar & Nightclub"},
            {"name": "Solarton High School"}
        ]
    },
    {
        "name": "Hex Valley",
        "description": "A wealthy town under eternal twilight, dominated by old vampiric money.",
        "children": [
            {"name": "Hex Valley Estates"},
            {"name": "C.U.M.S. Campus"}
        ]
    }
]

def create_location(token, name, description, parent_id=None):
    url = f"{API_BASE}/worlds/locations"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "world_id": WORLD_ID,
        "name": name,
        "description": description,
        "context_description": description,
        "parent_location_id": parent_id,
        "tags": [],
        "included_character_pool": [],
        "linked_character_pool": [],
        "included_lexicon_entries": [],
        "excluded_lexicon_entries": [],
        "keys": [name],
        "key_logic": "AND_ANY"
    }
    
    resp = requests.post(url, headers=headers, json=payload)
    if resp.status_code == 200 or resp.status_code == 201:
        data = resp.json()
        loc_id = data.get("id") or data.get("_id")
        print(f"Created location: {name} ({loc_id})")
        return loc_id
    else:
        print(f"Failed to create {name}: {resp.status_code} {resp.text}")
        return None

def process_node(token, node, parent_id=None):
    name = node.get("name")
    desc = node.get("description", "")
    loc_id = create_location(token, name, desc, parent_id)
    
    time.sleep(0.5) # rate limit prevention
    
    children = node.get("children", [])
    for child in children:
        process_node(token, child, loc_id)

def main():
    token = get_auth_token()
    print("Starting location injection...")
    for root in locations_tree:
        process_node(token, root, None)
    print("All locations created successfully!")

if __name__ == '__main__':
    main()

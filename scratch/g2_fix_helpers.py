import json
import re
import os
import shutil
import time
from datetime import datetime, timezone, timedelta

EP = datetime(827, 12, 21, 0, 0, 0, tzinfo=timezone.utc)

def d_to_h(y, m, d, h=0):
    dt = datetime(y, m, d, h, 0, 0, tzinfo=timezone.utc)
    return int((dt - EP).total_seconds() // 3600)

STANDARD_INSTRUCTIONS = (
    "Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), "
    "asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."
)

ALYSSA_ID = "_MXcEC8Y6B3BNm3b1ttHj6"
JASPER_ID = "_x3VY2kcbaDbKyCqywGeET"

# Contextual outfit generator based on character archetype / species / role
def generate_contextual_outfits(name, species, role_text):
    # Standard 5 outfits
    ts = int(time.time() * 1000)
    sp_lower = species.lower()
    rt_lower = role_text.lower()
    
    clean_n = name.split('(')[0].split('"')[0].strip()
    
    if any(k in rt_lower for k in ['student', 'hockey', 'football', 'cheerlead', 'frat', 'sorority', 'campus']):
        # Student archetype
        return [
            {
                "id": f"outfit-{ts}-1",
                "name": "Campus Daily",
                "description": f"Comfortable everyday student attire suitable for walking between SUCC lectures and study halls. Modern cut, athletic sneakers, and layered pieces accommodating natural build and features.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-2",
                "name": "Athletic / Gym",
                "description": f"Official SUCC athletic training gear, breathable sportswear, fitted shorts, and performance shoes worn during workouts, rink practice, or conditioning sessions.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-3",
                "name": "Dorm / Casual Loungewear",
                "description": f"Oversized soft hoodie, sweatpants, and wool socks worn late at night while studying, resting, or hanging out in the dormitory lounge.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-4",
                "name": "Greek Life / Party Night",
                "description": f"Sharp nightlife attire styled for weekend parties, frat events, or nightclub visits in Solarton and Bluemoon. Tailored denim, statement jacket, and clean boots.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-5",
                "name": "Formal / Academic Banquet",
                "description": f"Pressed dark formal suit or elegant evening wear for university ceremonies, banquets, and formal coalition dinners.",
                "avatar": ""
            }
        ]
    elif any(k in rt_lower for k in ['professor', 'coach', 'doctor', 'nurse', 'rector', 'chancellor', 'staff']):
        # Academic / Faculty / Staff archetype
        return [
            {
                "id": f"outfit-{ts}-1",
                "name": "Faculty Daily",
                "description": f"Professional campus attire, tailored collared shirt, dark slacks, and practical dress shoes suited for lectures and departmental consultations.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-2",
                "name": "Office & Research",
                "description": f"Comfortable working attire with sleeves rolled up, loosened tie, or specialized protective lab coat/apron suited for long research and grading sessions.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-3",
                "name": "Academic Formal",
                "description": f"Impeccably tailored three-piece academic suit or formal vestments worn during university convocations, board meetings, and high-level negotiations.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-4",
                "name": "Off-Duty / Private",
                "description": f"Relaxed private casual wear for downtime at home, reading, or quiet evenings away from students and administrative politics.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-5",
                "name": "Field / Travel Gear",
                "description": f"Sturdy weathered trench coat, heavy scarf, and durable walking boots for cold coastal weather and transit between city districts.",
                "avatar": ""
            }
        ]
    elif any(k in rt_lower for k in ['pack leader', 'alpha', 'council', 'syndicate', 'pureblood', 'representative']):
        # Council / Pack Leader / Aristocrat archetype
        return [
            {
                "id": f"outfit-{ts}-1",
                "name": "District Ruling Attire",
                "description": f"Commanding signature attire projecting authority across the district, featuring premium materials, custom tailoring, and subtle marks of pack rank.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-2",
                "name": "Council Assembly",
                "description": f"High-formality formal council attire worn in the Blackwood Council chambers. Dark ceremonial cloth, subtle silver/obsidian accessories, and impenetrable presence.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-3",
                "name": "Territorial Enforcer / Action",
                "description": f"Durable reinforced combat or industrial gear, tactical leather, heavy boots, and unrestrictive cut designed to survive physical skirmishes and partial shifts.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-4",
                "name": "Private Den / Hearth",
                "description": f"Relaxed territorial loungewear worn within private estate chambers, soft unbuttoned shirt, loose pants, and absence of formal armor.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-5",
                "name": "High Society Gala",
                "description": f"Exclusive bespoke luxury evening wear for high-stakes coalition galas, DCC corporate galas, and diplomatic neutral gatherings.",
                "avatar": ""
            }
        ]
    else:
        # General / Underworld / Independent archetype
        return [
            {
                "id": f"outfit-{ts}-1",
                "name": "Urban Daily",
                "description": f"Signature street attire adapted for urban supernatural life, combining durable utility with personal aesthetics.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-2",
                "name": "Operational / Work",
                "description": f"Sturdy, functional work attire equipped with reinforced seams, practical pockets, and durable boots for hands-on tasks.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-3",
                "name": "Nightlife / Discreet",
                "description": f"Low-profile dark jacket, hooded layer, and silent boots designed for blending into neon-lit night alleys and clubs.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-4",
                "name": "Casual Downtime",
                "description": f"Worn-in soft cotton t-shirt, relaxed denim, and broken-in sneakers for unmonitored hours behind closed doors.",
                "avatar": ""
            },
            {
                "id": f"outfit-{ts}-5",
                "name": "Formal / Meeting",
                "description": f"Clean pressed formal attire reserved for serious negotiations, legal summons, or high-stakes diplomatic encounters.",
                "avatar": ""
            }
        ]

def generate_contextual_speech(name, species, role_text):
    clean_n = name.split('(')[0].split('"')[0].strip()
    return [
        {
            "id": f"example-{int(time.time()*1000)}-1",
            "label": "Initial greeting",
            "prompt": f"A visitor arrives and greets {clean_n}.",
            "response": f"{clean_n} pauses, assessing the newcomer with steady, measured attention. \"State your business. If it matters to this territory, I am listening. If not, make it brief.\"",
            "activation_chance": 100
        },
        {
            "id": f"example-{int(time.time()*1000)}-2",
            "label": "Professional stance",
            "prompt": f"Someone asks {clean_n} how things operate around here.",
            "response": f"A faint, knowing look crosses their face as they lean back. \"Around here, respect is earned through consistency, not loud claims. Deliver on your word, and we will never have a problem.\"",
            "activation_chance": 100
        },
        {
            "id": f"example-{int(time.time()*1000)}-3",
            "label": "Boundary setting",
            "prompt": f"A pushy contact attempts to cross personal boundaries.",
            "response": f"Their voice drops an octave, perfectly flat and cold. \"Step back. That boundary was placed there for a reason, and you would do well not to test its weight.\"",
            "activation_chance": 100
        },
        {
            "id": f"example-{int(time.time()*1000)}-4",
            "label": "Pack and loyalty",
            "prompt": f"Discussion turns to pack dynamics and coalition politics.",
            "response": f"They gaze toward the horizon, scenting the air with quiet discipline. \"Power shifts, titles come and go, but blood and genuine loyalty are the only debts that never expire.\"",
            "activation_chance": 100
        },
        {
            "id": f"example-{int(time.time()*1000)}-5",
            "label": "Quiet observation",
            "prompt": f"A chaotic scene unfolds nearby.",
            "response": f"Watching the commotion unfold without flinching, they shake their head slowly. \"Noise without purpose. When you are finished making a spectacle, let us deal with what actually matters.\"",
            "activation_chance": 100
        }
    ]

def clean_em_dashes(text):
    if not text:
        return text
    # Replace em-dashes with comma or period
    text = re.sub(r'\s*—\s*', ', ', text)
    text = re.sub(r'—', ', ', text)
    # Also clean literal -- if intended as em dash
    text = re.sub(r'\s*--\s*', ', ', text)
    return text

print("Script template ready.")

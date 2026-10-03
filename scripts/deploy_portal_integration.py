import os
import sys
import json
import time
import urllib.request
import urllib.error

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token, sync_world

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'
API_BASE = 'https://app.wyvern.chat/api/worlds'

FORMAT_DISCIPLINE = 'Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.'

def api_put(resource, item_id, payload, token):
    url = f"{API_BASE}/{resource}/{item_id}?world_id={WORLD_ID}"
    data = json.dumps(payload).encode('utf-8')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, data=data, headers=headers, method='PUT')
    with urllib.request.urlopen(req) as resp:
        return resp.status

def api_post(resource, payload, token):
    url = f"{API_BASE}/{resource}?world_id={WORLD_ID}"
    data = json.dumps(payload).encode('utf-8')
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}

def main():
    print("Inizializzazione token Wyvern API...")
    token = get_auth_token()
    print("Token ottenuto con successo.")

    # =========================================================================
    # 1. CREAZIONE ILYA VOLKOV (LEXICON NPC)
    # =========================================================================
    print("\n--- 1. CREAZIONE ILYA VOLKOV (LEXICON NPC) ---")
    
    ilya_content = """[NAME: Ilya Volkov; SPECIES: Werewolf; NATIONALITY: Russian; AGE: {{age}}; GENDER: Male (He/Him); HEIGHT: 6'1" (184 cm); BUILD: Muscular, hardened, scarred chest and knuckles from bare-knuckle fighting; HAIR: Shaggy dark-ash blond; EYES: Cold storm-grey; SCARS: Jagged claw marks on his left shoulder, crooked broken nose set twice; SCENT: Gunpowder, stale vodka, copper, and damp asphalt; ROLE: Gun-for-hire, Enforcer, Mercenary in the Supernatural Underworld; AFFILIATION: Ballantine Crime Syndicate contractor, independent muscle in Paradise District; LIKES: Blood, fighting, firearms, alcohol, high-stakes gambling; DISLIKES: Losing, children, Betas, birds, happy families]

BACKSTORY: Abandoned by his father at birth, Ilya was raised in the brutal underground fight pits and docks of Vladivostok before migrating to the United States as a young adult. Hardened by violence and completely destitute, he made a name for himself in the illicit supernatural circuits of Los Angeles, taking on brutal debt collection, armed convoy escort, and wet-work contracts that regular operatives refused to touch. He maintains a mercenary relationship with Ruaraidh Ballantine's crime syndicate, serving as heavy muscle when negotiations turn bloody, while spending his downtime drinking in the grimy dive bars of Paradise District and gambling his earnings away.

VOICE & BEHAVIOR: Low, gravelly, heavy Russian accent. Cynical, blunt, and fiercely territorial. He views pack bonds and traditional werewolf chivalry as weak sentimentality, trusting only cold cash and the weight of a customized assault rifle in his hands.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""

    ilya_payload = {
        'world_id': WORLD_ID,
        'name': 'Ilya Volkov',
        'title': 'Ilya Volkov',
        'type': 'npc',
        'keys': ['Ilya Volkov', 'Ilya', 'Volkov'],
        'content': ilya_content,
        'avatar': 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/4cdc036e.jpg?v=2881d07e',
        'is_global': False,
        'enabled': True
    }

    try:
        new_ilya = api_post('lexicon', ilya_payload, token)
        ilya_id = new_ilya.get('id') or new_ilya.get('_id')
        print(f"  [OK] Creato Lexicon NPC Ilya Volkov (ID: {ilya_id})")
    except Exception as e:
        print(f"  [ERRORE] Creazione Ilya Volkov: {e}")

    # =========================================================================
    # 2. AGGIORNAMENTO AVATAR PER TUTTI I 31 PERSONAGGI / LEXICON
    # =========================================================================
    print("\n--- 2. ASSEGNAZIONE AVATAR UFFICIALI DAL PORTALE ---")

    char_avatars = [
        ('_bVgKYYURnWGWdX142q99k', 'Abel Vilas', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/b98d6546.jpg?v=2881d07e'),
        ('_13rj1V7hPaJ2QederUYkx', 'Ruaraidh "Rory" Ballantine', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/7ba6a268.jpg?v=2881d07e'),
        ('_E7kHtwcpVYedVkVTmMGKX', 'Sullivan "Sully" Jones', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/368fb9c7.jpg?v=2881d07e')
    ]

    for cid, name, avatar_url in char_avatars:
        try:
            status = api_put('characters', cid, {'avatar': avatar_url}, token)
            print(f"  [CHAR AVATAR OK] {name} [{cid}] status {status}")
        except Exception as e:
            print(f"  [CHAR AVATAR ERRORE] {name} [{cid}]: {e}")
        time.sleep(0.5)

    lex_avatars = [
        ('_qWx9J7M8XbchR1mMVJjAx', 'Adrian Locke', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/08c5a9fa.jpg?v=2881d07e'),
        ('_daK4mwDzDLbCYQn4j2JpM', 'Alistair DeVille', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/b308459d.jpg?v=2881d07e'),
        ('_9GfPDNMJmaCUMNUy6ktEw', 'Angui', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/c22bee08.jpg?v=2881d07e'),
        ('_8Bq2AdfPwbECRUg2AfFLL', 'Arthur Grey', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/93ef6885.jpg?v=2881d07e'),
        ('_Btpq4zn7nMwpUm6NmtGjK', 'Atlas Teague', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/9eba5831.jpg?v=2881d07e'),
        ('_mYThwNmNhpEDGMXXeHbRH', 'Cato', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/54231706.jpg?v=2881d07e'),
        ('_9BNDpAFVL3RNDYMLN1Px9', 'Cyrus Camden', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/a9af2e2f.jpg?v=2881d07e'),
        ('_CJ2htAtqm7nVgxwVCXygm', 'Damien Rosewood', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/03d6f9f0.jpg?v=2881d07e'),
        ('_UhkhyNLM7wrNXmg2YnWQ1', 'Emil', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/c9f7c97d.jpg?v=2881d07e'),
        ('_DwnX6fHLCt4p3wdnTGNBK', 'Everett Rottmore', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/22a98739.jpg?v=2881d07e'),
        ('_eMbJYXD84FbBzextUB87B', 'Emlyn Danes', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/b821e71d.jpg?v=2881d07e'),
        ('_r9c2n7QXHmBn2QC3DRtGa', 'Garrett Emerson', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/308b0b41.jpg?v=2881d07e'),
        ('_f84YxjrVR6mmyz2Lx93fg', 'Gianni Luciano', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/9b0d6c39.jpg?v=2881d07e'),
        ('_dUJ6ThMkUD186xcPAQ9VX', 'Graham Purcell', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/06308116.jpg?v=2881d07e'),
        ('_PMXN2UcUhfjfY1qrRe16G', 'Julian Bieri', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/8a25da51.jpg?v=2881d07e'),
        ('_gQY3q1Pf4wRJJE99wzLmz', 'Kade Leavis', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/b06e3112.jpg?v=2881d07e'),
        ('_gQgy8Q9xhgTdVmDxPjYwR', 'Kai Monroe', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/dbfc955d.jpg?v=2881d07e'),
        ('_fbebf7KgCQkDQM4rK4dEb', 'Levi Graham', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/e1c09189.jpg?v=2881d07e'),
        ('_zdkPteyYJRkRJRb9pkFVb', 'Miles Airhardt', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/d78ac878.jpg?v=2881d07e'),
        ('_r7BVMCaBWL9Fcw7nDGmp8', 'Milo Grayson', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/fc4661f3.jpg?v=2881d07e'),
        ('_dVWcw383agThczLcLjD9g', 'Nic Lucero', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/3f6a55d2.jpg?v=2881d07e'),
        ('_xH4Uj7YCwJAqGq89PyQFb', 'Park Jae-Sung', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/b3642974.jpg?v=2881d07e'),
        ('_CRzMVY9HLMXammw672Cyh', 'Rafael Callaway', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/299f561a.jpg?v=2881d07e'),
        ('_BrWCeh3Dr7EMjNnGVaNtF', 'Rhett Moore', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/650ea6f4.jpg?v=2881d07e'),
        ('_VnnHYRVGCBQJPtUeLUWTH', 'Jayce Collins', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/650ea6f4.jpg?v=2881d07e'),
        ('_xV3P8bEFmVtHjTDDNNrdP', 'Romeo "Gray" Dean', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/d72ec552.jpg?v=2881d07e'),
        ('_DKm3eYG7d1kTaeeHmgg71', 'Vale Roberts', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/b98d086b.jpg?v=2881d07e'),
        ('_2K2zFggbhMatREW2Aj7PJ', 'Vasile Ionescu', 'https://io-modernfantasy.uwu.ai/assets/images/gallery03/424fe3ff.jpg?v=2881d07e')
    ]

    for lid, name, avatar_url in lex_avatars:
        try:
            status = api_put('lexicon', lid, {'avatar': avatar_url}, token)
            print(f"  [LEX AVATAR OK] {name} [{lid}] status {status}")
        except Exception as e:
            print(f"  [LEX AVATAR ERRORE] {name} [{lid}]: {e}")
        time.sleep(0.4)

    # =========================================================================
    # 3. ENRICH GEOGRAPHIC CONTEXT & BANNER AVATARS (UNDERWORLD, SRF, BALLANTINE)
    # =========================================================================
    print("\n--- 3. ARRICCHIMENTO CONTESTO GEOGRAFICO (CALIFORNIA COAST) ---")

    # 3.1 Supernatural Underworld
    underworld_id = '_LyHK91bhWrej3K4XyWW6h'
    underworld_content = """[FACTION: The Supernatural Underworld; TERRITORY: Greater Los Angeles Basin, Paradise District, Long Beach Harbors, Inland Ventura Smuggling Corridors; GOVERNANCE: De-centralized Syndicate Network, Mediated by the Ballantine Family; REACH: Southern and Central California Coast]

OVERVIEW: The Supernatural Underworld represents the clandestine shadow economy running parallel to mundane California society. Within its veiled network of underground clubs, hidden docks, and fortified warehouses, sentient supernaturals, rogue covens, and criminal syndicates trade in illicit alchemical narcotics like Ambrosia, black-market enchanted artifacts, unregistered soul stones, and discrete contract violence.

GEOGRAPHIC ANCHORS:
1. Paradise District (Los Angeles): The primary urban bazaar of the underworld, featuring high-end covert brokerages, VIP supernatural speakeasies, and illicit auction houses.
2. Long Beach & San Pedro Docks: The maritime smuggling entry point for off-world and European magical cargo, guarded by aquatic demihumans and gargoyle sentries.
3. Central Coast Smuggling Trails: Hidden mountain and canyon roads stretching through Ventura County toward Solarton, utilized by rogue couriers and werewolf runners.

INTERACTION WITH ESTABLISHED PACKS: The Underworld operates under an uneasy, tacit armed peace with House Douglas of Blackwood City and the corporate demon enclave of HSK Consulting. While open gang war is strictly suppressed by mutual agreement, the Underworld thrives by servicing appetites, secrets, and logistics that formal law cannot acknowledge.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""

    try:
        status = api_put('lexicon', underworld_id, {
            'content': underworld_content,
            'avatar': 'https://io-modernfantasy.uwu.ai/assets/images/gallery09/6dd5d097.jpg?v=2881d07e'
        }, token)
        print(f"  [OK] Aggiornato Supernatural Underworld [{underworld_id}] status {status}")
    except Exception as e:
        print(f"  [ERRORE] Update Supernatural Underworld: {e}")

    # 3.2 Supernatural Reserve Forces (SRF)
    srf_id = '_C6JqdNxNgtqeneW1DxbrK'
    srf_content = """[ORGANIZATION: Supernatural Reserve Forces (SRF); BRANCH: United States Army Special Operations; JURISDICTION: Federal Supernatural Threat Neutralization, Tactical Containment, High-Threat Reconnaissance; PERSONNEL: Approximately 86 percent non-human supernaturals, 14 percent specialized human liaisons; WEST COAST GARRISON: Joint Tactical Base Point Mugu & Coastal Outpost Alpha near Ventura-Simi Valley corridor; COMMANDER: Major Graham Purcell (Kodiak Bear Demihuman)]

OVERVIEW: The SRF is the specialized international military arm of the armed forces tasked with managing, containing, and eliminating catastrophic supernatural crises that surpass conventional law enforcement. Formed after military leadership recognized the lethal force multiplication of supernatural senses, regenerative healing, and physical strength, the SRF stands as the nation's premier tactical defense unit.

CULTURE & REGULATIONS:
1. Permitted Fraternization: Unlike standard human branches, the SRF permits supernatural relationship structures including pack bonds and mate bonds, recognizing that suppressing non-human biology compromises combat performance.
2. Base Architecture: Coastal installations feature subterranean saltwater simulation tanks, specialized sprint tracks for werewolves, reinforced concrete quarters, and dedicated medical bays trained in shifted anatomy.
3. Tension with Civilian Territory: The SRF frequently clashes over jurisdictional boundaries with autonomous werewolf houses like the Douglas dynasty and local Solarton authorities, who view federal military intervention as provocative overreach.

OPERATIONAL UNITS:
- Squad Alpha: Led by Lieutenant Miles Airhardt ("Redwood"), featuring Sergeant Rafael Callaway ("Sawtooth") and Private Kade Leavis ("Spark").
- Historical Precedents: Houses classified historical black-ops legacies, including the terminated Project BlackWolf and the survivors of unit Gamma-7 (Kaladin Nargathon and Marcus Thornfield).

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""

    try:
        status = api_put('lexicon', srf_id, {
            'content': srf_content,
            'avatar': 'https://io-modernfantasy.uwu.ai/assets/images/gallery09/8293d56c.jpg?v=2881d07e'
        }, token)
        print(f"  [OK] Aggiornato Supernatural Reserve Forces (SRF) [{srf_id}] status {status}")
    except Exception as e:
        print(f"  [ERRORE] Update SRF: {e}")

    # 3.3 Ballantine Family
    ballantine_id = '_X2qqf3HhhdMahnhFUW3j7'
    ballantine_content = """[ORGANIZATION: The Ballantine Family; TYPE: Draconic Supernatural Crime Syndicate; HEADQUARTERS: Rory's Estate, secluded coastal estate on the hills between Solarton and North Los Angeles; FRONT: Ballantine Imports & Exports; LEADER: Ruaraidh "Rory" Ballantine (Dragon Demihuman); RIGHT-HAND: Sullivan "Sully" Jones (Human Fixer)]

OVERVIEW: The Ballantine Family is the preeminent organized crime syndicate operating across the Southern California coastal corridor. Under the legitimate commercial front of Ballantine Imports & Exports, the syndicate exercises undisputed control over high-value artifact trade, private security contracting, magical asset transport, and harbor customs interception.

TERRITORIAL CODE & DYNAMICS:
1. Scottish Dragon Patriarch: Rory Ballantine commands absolute, fierce loyalty from his crew, viewing his criminal network as an extended family to be protected at any cost.
2. Northern Boundary Policy: The Ballantine Family strictly confines its heavy muscle and active racket operations to Greater Los Angeles and the southern coastal ports. Toward the north, in Solarton and Blackwood City, Rory maintains only commercial intermediaries and discreet informants. He respects House Douglas's sovereign pack territory, refusing to conduct unsanctioned enforcement operations on their soil.
3. Underworld Hub: Rory's Estate serves as the guarded sanctuary where syndicate summits, private agreements, and discreet transactions are settled over vintage scotch and fine cigars.

[INSTRUCTIONS: Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead.]"""

    try:
        status = api_put('lexicon', ballantine_id, {
            'content': ballantine_content,
            'avatar': 'https://io-modernfantasy.uwu.ai/assets/images/gallery41/f07de65f.jpg?v=2881d07e'
        }, token)
        print(f"  [OK] Aggiornato Ballantine Family [{ballantine_id}] status {status}")
    except Exception as e:
        print(f"  [ERRORE] Update Ballantine Family: {e}")

    print("\n--- TUTTI GLI AGGIORNAMENTI API COMPLETATI CON SUCCESSO! ---")

if __name__ == '__main__':
    main()

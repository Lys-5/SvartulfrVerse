import json
import pathlib
import urllib.request
import urllib.error
import time

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_PATH = ROOT / 'FINAL' / 'Svartulfr_NPC_Secondary.json'
OPTIMIZED_PATH = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Secondary.json'
WT_PATH = ROOT / 'scratch' / 'wyvern_token.txt'
RT_PATH = ROOT / 'scratch' / 'refresh_token.txt'
FIREBASE_API_KEY = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw'
LOREBOOK_ID = '_Uht3Ckz44JBDrPnUHq7LV'

THORVALD_CONTENT = """[NAME: Thorvald; ALIASES: The Pine Wolf, Iron-Oath; SPECIES: Werewolf (Founding Bloodline / Direct Descendant of Firstborn Ut Berg); AGE: 32 (Born 04 January 1992); HEIGHT: 6'6" (198 cm); WEIGHT: 260 lbs; BUILD: Massive, battle-hardened mountain frame, dense rock-hard muscle carrying the titan density of Ut's blood, broad back carved with ritual Old Norse binding runes, weathered survival scars; HAIR: Long ash-blond hair braided along the sides in traditional Nordic warrior fashion; EYES: Cold glacial blue that gleam silver under moonlight; FEATURES: Gray wolf ears and thick bushy tail in Partial Shift, ragged claw scars along ribs and forearms; ATTIRE: Hand-stitched heavy wool tunic, hardened leather bracers stamped with stone and hammer runes, fur-lined winter trousers, rugged wilderness tracking boots, heavy iron-headed hunting spear; OCCUPATION: Ancestral forest ranger, guardian of the sacred groves, traditional hunter; RESIDENCE: The High Pine Hinterlands, Old Growth Forest north of Blackwood County]

BACKSTORY: Thorvald is a direct blood descendant of the Firstborn Ut Berg, the Stone Titan and living primordial patriarch consecrated by Fenris. From Ut's primordial bloodline, Thorvald inherited an unbreakable physical density, instinctual runecrafting, and a natural affinity for granite, forged iron, and ancient pine forests. While modern branches of the lupine clans migrated into coastal metropolises and founded corporate dynasties like the Douglas empire, Thorvald and his kin remained in the vast, untamed alpine pine forests of the northern hinterlands. Raised in strict accordance with archaic Old Norse traditions, Thorvald guards the sacred ancestral boundary stones against encroaching developers, poachers, and rogue beasts.

PACK AND SOVEREIGNTY: As a living scion of the Founding Bloodline through Ut Berg, Thorvald carries the quiet, unshakable authority of the first generation of wolves. He answers exclusively to the sovereign authority of the Firstborn Wulfnic Bloodmoon, whom he reveres alongside his forefather Ut. He views the urban Douglas wolves with guarded ambivalence, acknowledging Erik Douglas as a mighty pack leader but privately shaking his head at the suits, high-rises, and digital distractions of Blackwood City. Whenever Wulfnic or Ut retreat into the wilderness to commune with the old forest, Thorvald acts as their hirdman, scout, and trusted campfire companion.

VOICE AND BEHAVIOR: Thorvald possesses a deep, steady voice that carries the dry chill of mountain wind. He speaks sparingly, believing that words spoken without thought dishonor one's ancestors. He is intensely perceptive, capable of tracking scents across miles of granite and snow. In interaction, he is stoic, protective, and possessed of a dry, subtle northern humor. He treats women, elders, and young pups with solemn, courtly gentleness, but turns into a whirlwind of savage bone-crushing fury the instant an enemy threatens his woods or dishonors an oath.

THE FROSTBOUND GUARDIAN: Thorvald represents the unyielding memory of what werewolves were before glass towers and corporate balance sheets. Carrying the primordial blood of Ut Berg, his soul is bound to the quiet pines, the freezing mountain air, and the eternal sanctity of the hunt.

[RPG STATS & TRAITS: Level: 32; MGT: 7; RES: 7; AGI: 6; WIT: 4; PRS: 3; SCT: 4; TRAITS: Founding Bloodline (Ut Descendant), Wilderness Tracker, Primal Howl, Frost Resistance, Stone Titan Resilience]"""

HARALD_CONTENT = """[NAME: Harald Sigurdsson; ALIASES: The Grim Jarl, Wolf-King of the Hinterlands; SPECIES: Werewolf (Founding Bloodline / Scion of the Nine Fallen Firstborn / Jarl Heritage); AGE: 36 (Born 17 August 1987); HEIGHT: 6'8" (203 cm); WEIGHT: 285 lbs; BUILD: Imposing, broad-shouldered warrior frame, thick chest, corded forearms, battle scars across neck and jawline from tribal dominance bouts; HAIR: Thick dark brown hair swept back and tied at the nape, full trimmed beard; EYES: Striking pale predatory green with cold amber ring; FEATURES: Dark charcoal wolf ears and heavy tail in Partial Shift, sharp predatory fangs; ATTIRE: Dark woolen tunics, heavy studded leather armor trimmed with dark wolf pelt, forged iron arm rings, heavy traveling boots, ceremonial broadsword sheathed at his hip; OCCUPATION: Jarl of the Hinterland Encampments, elder warlord, clan leader; RESIDENCE: Sigurdsson Stead, Northern Hinterland Ridges]

BACKSTORY: Harald carries the proud, primordial blood of one of the Nine Fallen Firstborn, the original primordial wolves created directly by Fenris who fell in the catastrophic wars of antiquity. As the direct heir to this consecrated lineage, Harald possesses the coveted Founding Bloodline trait, linking his spirit to the primordial origins of the lupine species. His ancestors preserved this sacred warrior heritage across the Scandinavian fiords for centuries before following Wulfnic Bloodmoon across the Atlantic. Refusing to trade his ancient war axe for a corporate boardroom, Harald established his sovereign domain in the rugged mountain ridges of the northern hinterlands.

CLAN AND COMMAND: Harald commands absolute loyalty among his hinterland warriors as a recognized scion of the Founding Bloodline. He maintains a stern, formal peace treaty with Erik Douglas: the Douglas pack does not encroach upon the northern hunting grounds, and Harald ensures that rogue young wolves from the hinterlands do not cause chaos in the cities. When issues of bloodline law or territorial defense arise that affect the entire lupine species, Harald represents the traditionalist voice at the Grand Council, standing as an immovable pillar of ancestral discipline against modern decadence.

VOICE AND BEHAVIOR: Harald speaks in a commanding, gravelly baritone that demands instant silence in any hall. He does not negotiate from weakness and considers an oath sealed in blood more binding than any corporate contract. Despite his stern, unsmiling demeanor, he is a deeply fair and protective ruler who prioritizes the safety and sustenance of his clan above his own life. In private moments with those he respects or loves, his fierce demeanor softens into a quiet, unwavering possessiveness and profound loyalty.

THE ANCESTRAL JARL: Harald embodies the ancient warrior ethos of the north: pride without vanity, strength without cruelty, and an unshakeable belief that a true leader leads from the front lines of the hunt and the battlefield, worthy of the Fallen Firstborn whose primordial blood burns in his veins.

[RPG STATS & TRAITS: Level: 36; MGT: 8; RES: 7; AGI: 5; WIT: 5; PRS: 4; SCT: 2; TRAITS: Founding Bloodline (Fallen Firstborn Scion), Jarl Command, Battle-Hardened, Iron Will, Primordial War Cry]"""

def main():
    print(f"[1/4] Loading {FINAL_PATH}...")
    with open(FINAL_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_names = []
    for entry in data.get('entries', []):
        if entry.get('name') == 'Thorvald':
            entry['content'] = THORVALD_CONTENT
            entry['comment'] = "Traditionalist werewolf, direct descendant of Ut Berg (Founding Bloodline)"
            if 'labels' in entry and 'founding-bloodline' not in entry['labels']:
                entry['labels'].append('founding-bloodline')
            updated_names.append('Thorvald (entries)')
        elif entry.get('name') == 'Harald Sigurdsson':
            entry['content'] = HARALD_CONTENT
            entry['comment'] = "Traditionalist Jarl, direct descendant of the Nine Fallen Firstborn (Founding Bloodline)"
            if 'labels' in entry and 'founding-bloodline' not in entry['labels']:
                entry['labels'].append('founding-bloodline')
            updated_names.append('Harald Sigurdsson (entries)')

    for entry in data.get('lexicon', []):
        if entry.get('name') == 'Thorvald':
            entry['content'] = THORVALD_CONTENT
            entry['comment'] = "Traditionalist werewolf, direct descendant of Ut Berg (Founding Bloodline)"
            if 'labels' in entry and 'founding-bloodline' not in entry['labels']:
                entry['labels'].append('founding-bloodline')
            updated_names.append('Thorvald (lexicon)')
        elif entry.get('name') == 'Harald Sigurdsson':
            entry['content'] = HARALD_CONTENT
            entry['comment'] = "Traditionalist Jarl, direct descendant of the Nine Fallen Firstborn (Founding Bloodline)"
            if 'labels' in entry and 'founding-bloodline' not in entry['labels']:
                entry['labels'].append('founding-bloodline')
            updated_names.append('Harald Sigurdsson (lexicon)')

    print(f"  Updated entries: {updated_names}")

    print(f"[2/4] Saving to {FINAL_PATH} and {OPTIMIZED_PATH}...")
    with open(FINAL_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    with open(OPTIMIZED_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, separators=(',', ':'), ensure_ascii=False)

    print(f"[3/4] Refreshing auth token...")
    rt = RT_PATH.read_text(encoding='utf-8').strip()
    body = json.dumps({'grant_type': 'refresh_token', 'refresh_token': rt}).encode('utf-8')
    req = urllib.request.Request(
        f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}',
        data=body,
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        token = res['id_token']
        WT_PATH.write_text(token, encoding='utf-8')

    print(f"[4/4] Deploying to Wyvern API (PUT /api/lorebooks/{LOREBOOK_ID})...")
    base_payload = {
        'name': data.get('name', 'Svartúlfr - NPC Secondary'),
        'description': data.get('description', ''),
        'visibility': data.get('visibility', 'private'),
        'rating': data.get('rating', 'explicit'),
        'scan_depth': data.get('scan_depth', 5),
        'token_budget': data.get('token_budget', 5000),
        'recursive_scanning': data.get('recursive_scanning', True),
    }

    payload_both = dict(base_payload)
    payload_both['entries'] = data['entries']
    payload_both['lexicon'] = data['lexicon']
    bytes_both = json.dumps(payload_both, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

    payload_lex = dict(base_payload)
    payload_lex['lexicon'] = data['lexicon']
    bytes_lex = json.dumps(payload_lex, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

    if len(bytes_both) < 1000000:
        chosen_bytes = bytes_both
        mode = "dual_array"
    else:
        chosen_bytes = bytes_lex
        mode = "native_lexicon"

    print(f"  Mode: {mode} | Size: {len(chosen_bytes):,} bytes | Entries: {len(data['entries'])}")

    put_req = urllib.request.Request(
        f'https://app.wyvern.chat/api/lorebooks/{LOREBOOK_ID}',
        data=chosen_bytes,
        method='PUT',
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    )

    with urllib.request.urlopen(put_req, timeout=60) as resp:
        print(f"  Deploy Status: HTTP {resp.status}")

    time.sleep(2.5)
    get_req = urllib.request.Request(
        f'https://app.wyvern.chat/api/lorebooks/{LOREBOOK_ID}',
        headers={
            'Authorization': f'Bearer {token}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    )
    with urllib.request.urlopen(get_req, timeout=30) as resp:
        vdata = json.loads(resp.read().decode('utf-8'))
        rem_entries = len(vdata.get('lexicon', [])) or len(vdata.get('entries', []))
        print(f"  Verification GET: HTTP {resp.status} | Remote entries count: {rem_entries}")
        assert rem_entries == 111, f"Expected 111 entries, got {rem_entries}"
        print("  Thorvald and Harald Founding Bloodline update verified successfully!")

if __name__ == '__main__':
    main()

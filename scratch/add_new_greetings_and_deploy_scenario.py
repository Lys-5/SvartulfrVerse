import json
import pathlib
import urllib.request
import urllib.error

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
TOKEN = (ROOT / 'scratch' / 'wyvern_token.txt').read_text(encoding='utf-8').strip()
API_BASE = 'https://app.wyvern.chat/api'
SCENARIO_ID = 'char_scenario_1DC43ggb6mB8YLJDJKrU4'

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

scen_path = ROOT / 'FINAL' / 'Svartulfr_Master_Scenario.json'
scen = json.loads(scen_path.read_text(encoding='utf-8'))

linked_personas = ["persona_1786335754946", "1792155173728"]

new_greetings = [
    {
        "id": "greeting_ch27_jasper_russ_dorm",
        "name": "Capitolo 27: Dormitori SUCC - Jasper e Russ",
        "description": "Jasper e il suo esuberante coinquilino Russ (Five Cocketeers) nella loro suite al Wyrm Hall.",
        "speaker_slot": "twin",
        "linked_persona_ids": linked_personas,
        "content": "The smell of greasy carnitas and hot salsa hit the room before the door even swung open. In the dim amber glow of three curved monitors, Jasper sat hunched over his mechanical keyboard, the rhythmic clack of terminal commands punctuated only by the low hum of an unreleased synth loop looping through his open-back headphones.\n\nRuss kicked the door shut with the heel of his sneaker, balancing two brown paper bags on one forearm while tossing a bundle of charging cables onto the shared coffee table. Russ grinned, dropping a foil-wrapped burrito directly onto the empty mousepad beside Jasper's elbow.\n\n\"Rise and shine, code jockey. If you stare at those hex dumps for another twenty minutes, your retinas are going to turn into fiber optic cables. Eat something before the salsa dissolves the foil.\"\n\nJasper slowly pulled the headphones down around his throat, his dark lupine ears flicking back as he surveyed the sudden intrusion with dry, unhurried composure. He glanced from the foil package to Russ's smug expression.\n\n\"I had three minutes left on a packet trace, Russ. If this burrito leaks into my cooling rig, you are vacuuming the heat sinks with your toothbrush.\"\n\nRuss laughed, collapsing backward onto his unmade bunk bed and clasping his hands behind his head. \"Relax, man. A little habanero grease never killed an audio rig. Besides, word on the quad is you were hiding in here instead of checking out the mixer battle signups at the student union.\""
    },
    {
        "id": "greeting_ch28_jasper_neon_purr_verve",
        "name": "Capitolo 28: Soundclash al Verve - Jasper contro Neon Purr",
        "description": "Feroce battaglia musicale e soundclash tra Jasper e il suo rivale DJ Neon Purr nel lounge sotterraneo del Verve.",
        "speaker_slot": "twin",
        "linked_persona_ids": linked_personas,
        "content": "The reinforced concrete floor of The Verve's subterranean lounge shuddered under eighty thousand watts of custom low-end acoustic pressure. Ultraviolet wash lights painted the brick archways in deep violet and cobalt, illuminating a packed, swaying crowd of supernaturals and nightlife regulars.\n\nUp on the dual performance riser, Neon Purr cut the fader with theatrical flair, his sleek feline ears pinned flat against wild, neon-dyed hair as he leaned over his modular synth rack. The Australian feline DJ tapped his tempo pad, sending a blistering, distorted breakbeat cascading through the room before snatching his mic.\n\n\"Not bad for a warmup, Solarton, but let us see if Seven Hills can handle actual syncopation! Your turn, big bad wolf!\"\n\nNeon Purr flashed a sharp, taunting grin across the mixer divide, stepping back to let the track hit its crescendo.\n\nOn the adjacent booth, Jasper stood entirely motionless, the quiet eye of the auditory storm. Dressed in his oversized black hoodie with his tail swaying in slow, rhythmic measure behind him, Jasper did not smile. He placed his fingertips on the master crossfader, his gaze locking onto Neon Purr's with cold, razor-sharp focus.\n\nWith a flick of his wrist, Jasper engaged his custom frequency filter. The distorted breakbeat dropped instantly into silence, replaced by a deep, sub-audible pressure wave that rattled the ice inside every tumbler on the counter.\n\n\"You talk too much during your transitions, Purr. Watch your levels before you blow Logan's subwoofers.\"\n\nBehind the soundboard, Logan Douglas watched the exchange through the glass, rubbing his temple with one hand while holding a tumbler of scotch, muttering softly to himself as the bassline kicked back in like a freight train."
    },
    {
        "id": "greeting_ch29_malachia_roman_kolya_gym",
        "name": "Capitolo 29: Palestra Pesi e Tappeti - Malachia, Roman e Kolya",
        "description": "Sessione di allenamento pesante e sparring sui tappeti tra Malachia, Roman Blackwood e Kolya.",
        "speaker_slot": "eldest_brother",
        "linked_persona_ids": linked_personas,
        "content": "The sharp tang of athletic chalk and cold iron filled the auxiliary wrestling fieldhouse behind the SUCC stadium. The heavy rubber mats were slick with sweat, the thud of bodies hitting the ground echoing off the corrugated steel ceiling in steady intervals.\n\nMalachia Douglas stood in the center of the ring, wearing charcoal compression shorts and taped wrists, his massive chest rising and falling in deep, measured breaths. Across from him, Roman Blackwood shook out his shoulders, wiping sweat from his forehead with the back of his forearm while his single pair of animal ears twitched forward in focused concentration. Beside the mat, Kolya was already taping up his fingers, leaning against a stack of bumper plates with a grin of exhausted respect.\n\n\"Your underhook is getting heavier, Malachia,\" Roman said between breaths, circling the perimeter of the mat with light, calculated steps. \"Most guys try to overpower the hips on the second drive, but you just drop your center like a slab of granite.\"\n\nMalachia adjusted his stance, his scarred arms coming up into a ready grapple, his predatory golden gaze locked onto Roman with fierce, quiet intensity. In this room, there were no boardrooms, no corporate mergers, and no political protocol. Just weight, leverage, and the honest strain of muscle against bone.\n\n\"If I dropped my hips like most guys, you would have had me in a cradle three seconds into the reset, Roman. Lock up. You have two minutes before Kolya steps in.\"\n\nRoman chuckled, closing the distance and engaging the collar tie with a sharp slap of palms against shoulders. \"Fair enough. Let us see if your balance holds up against a low single.\""
    }
]

# Ensure we don't duplicate if already present
existing_ids = {g.get('id') for g in scen.get('greetings', [])}
for g in new_greetings:
    if g['id'] not in existing_ids:
        scen['greetings'].append(g)

print(f"Total scenario greetings now: {len(scen['greetings'])}")

# Save locally
scen_path.write_text(json.dumps(scen, indent=2, ensure_ascii=False), encoding='utf-8')
print("Saved updated FINAL/Svartulfr_Master_Scenario.json")

# 1. Fetch live scenario to get current revision
req_get = urllib.request.Request(
    f"{API_BASE}/character-scenarios/{SCENARIO_ID}",
    headers=headers
)
with urllib.request.urlopen(req_get) as resp_get:
    live_scen = json.loads(resp_get.read().decode('utf-8'))
current_rev = live_scen.get('revision', 11)
print(f"Fetched live scenario revision: {current_rev}")

# Prepare PUT payload
put_payload = {
    'name': scen.get('name'),
    'description': scen.get('description'),
    'rating': scen.get('rating', 'explicit'),
    'visibility': scen.get('visibility', 'private'),
    'scenario': scen.get('scenario', ''),
    'slots': scen.get('slots', []),
    'greetings': scen.get('greetings', []),
    'lorebook_ids': scen.get('lorebook_ids', []),
    'revision': current_rev
}

req_put = urllib.request.Request(
    f"{API_BASE}/character-scenarios/{SCENARIO_ID}",
    data=json.dumps(put_payload, ensure_ascii=False).encode('utf-8'),
    headers=headers,
    method='PUT'
)

try:
    with urllib.request.urlopen(req_put, timeout=60) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print(f"Master Scenario PUT SUCCESS! Status: {resp.status} | Total Greetings Live: {len(res.get('greetings', []))}")
except urllib.error.HTTPError as e:
    err = e.read().decode('utf-8', errors='ignore')
    print(f"Master Scenario PUT HTTPError {e.code}: {err[:400]}")

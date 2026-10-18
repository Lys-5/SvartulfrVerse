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

ENTRIES = [
    {
        "entry_id": "npc_sec_thrakgor_deathspine",
        "name": "Thrakgor Deathspine",
        "keys": ["Thrakgor Deathspine", "Warchief Thrakgor", "Thrakgor", "Deathspine"],
        "secondary_keys": [],
        "regex_patterns": [],
        "extensions": {},
        "enabled": True,
        "case_sensitive": False,
        "insertion_order": 100,
        "priority": 10,
        "comment": "Warchief of the Deathspine Clan, bellicose rival to Brak Ironfist",
        "constant": False,
        "position": "before_char",
        "scan_persona": False,
        "whole_words_only": True,
        "key_logic": "AND_ANY",
        "delay": 0,
        "sticky": 0,
        "cooldown": 0,
        "activation_chance": 100,
        "labels": ["npc", "secondary", "orc", "warchief"],
        "custom_fields": {},
        "related_entries": [],
        "avatar": "https://ella.janitorai.com/bot-avatars/LaX-Azncb7-WOLbt2o-pv.webp",
        "avatar_activation_regex": r"(?:^|\n)\s*(?:Warchief\ Thrakgor\ Deathspine|Warchief\ Thrakgor|Thrakgor\ Deathspine|Thrakgor)\s*:",
        "type": "npc",
        "callback": "",
        "provenance": {"source": {"kind": "janitor_favorites", "creator": "Leidenpotato", "bot_id": "f5e4ec7a-9afd-4b47-880f-622f855e2315"}, "captured_at": "2026-10-18T16:00:00.000Z"},
        "custom_avatar_regex": True,
        "lines_parsed": 1,
        "npc_info": {
            "first_name": "Thrakgor",
            "last_name": "Deathspine",
            "nicknames": ["Warchief", "The Bone Cleaver"],
            "titles": ["Warchief of the Deathspine Clan"]
        },
        "content": """[NAME: Thrakgor Deathspine; ALIASES: Warchief Thrakgor, The Bone Cleaver; SPECIES: Mountain Orc; AGE: 38 (Born 14 March 1986); HEIGHT: 6'10" (208 cm); WEIGHT: 320 lbs; BUILD: Colossal, densely muscled frame layered with thick scar tissue from decades of tribal warfare, heavy jutting tusks protruding from a wide brutal jaw, corded neck, scarred grayish-green skin; HAIR: Coarse black mane braided with bone beads and iron rings; EYES: Smoldering reddish-amber; ATTIRE: Thick hardened leather armor reinforced with blackened iron plates and beast pelts, heavy combat boots, war axe sheathed across broad shoulders; OCCUPATION: Warchief of the Deathspine Clan, warlord; RESIDENCE: Deathspine Encampment, mountain ridges overlooking the Hex Valley]

BACKSTORY: Thrakgor rose through the brutal hierarchy of the mountain orc clans by crushing every rival who dared challenge his claim. Unlike the diplomats and city dwellers who negotiate contracts in air-conditioned offices, Thrakgor believes in the absolute law of iron and blood. While the diplomatic Brak Ironfist preaches peaceful coexistence, patience, and pacts with the Douglas wolf pack and human authorities, Thrakgor views such compromises as cowardice that softens orc blood. He established his fortified encampment along the rugged ridges above the valley, demanding tribute, raiding vulnerable supply convoys, and keeping his warriors in constant readiness for the total conquest he believes is inevitable.

CLAN AND ALLIANCES: Thrakgor commands the Deathspine Clan with an iron fist, tolerating no insubordination or hesitation. He maintains an intense, bitter rivalry with Brak Ironfist, mocking Brak as a tame lapdog of the wolves and human corporations. His stance toward the Douglas pack is one of aggressive vigilance: he acknowledges Erik Douglas as a terrifying force of nature, yet constantly probes the borders of pack territory to test the wolves' resolve and hunt down any trespassers who venture too deep into the mountain crags.

VOICE AND BEHAVIOR: Thrakgor speaks in a deep, guttural rumble that vibrates the chest of anyone standing near him. He despises flowery speech, double talk, and legalistic contracts, demanding blunt honesty and immediate action. He laughs with booming, chest-thumping ferocity when challenged and shows respect only to those who can meet his gaze without flinching or withstand his crushing grip. In combat and council, he is ruthless, direct, and unyielding, relying on raw intimidating presence and devastating physical dominance.

THE UNTAMED WARLORD: Beneath his savage exterior lies a shrewd tactical commander who understands logistics, terrain, and the psychology of fear. Thrakgor is not a mindless beast; he is a traditional warlord fighting to preserve the ancestral ferocity of orc kind against what he sees as the eroding domesticity of the modern world.

[RPG STATS & TRAITS: Level: 38; MGT: 9; RES: 8; AGI: 4; WIT: 3; PRS: 4; SCT: 3; TRAITS: Brutal Cleave, Warchief Roar, Thick Hide, Indomitable Might]"""
    },
    {
        "entry_id": "npc_sec_feral_hound_crowe",
        "name": "Crowe",
        "keys": ["Crowe", "Feral Hound Crowe", "Crowe the Hound"],
        "secondary_keys": [],
        "regex_patterns": [],
        "extensions": {},
        "enabled": True,
        "case_sensitive": False,
        "insertion_order": 100,
        "priority": 10,
        "comment": "Lethal tracking hound mercenary, DDM Contractor & DCC black-ops tracker",
        "constant": False,
        "position": "before_char",
        "scan_persona": False,
        "whole_words_only": True,
        "key_logic": "AND_ANY",
        "delay": 0,
        "sticky": 0,
        "cooldown": 0,
        "activation_chance": 100,
        "labels": ["npc", "secondary", "demihuman", "mercenary", "ddm"],
        "custom_fields": {},
        "related_entries": [],
        "avatar": "https://ella.janitorai.com/bot-avatars/92qxyDw3aIGUBYFIzJIyt.webp",
        "avatar_activation_regex": r"(?:^|\n)\s*(?:FERAL\ HOUND\ Crowe|Feral\ Hound\ Crowe|Crowe\ the\ Hound|Crowe)\s*:",
        "type": "npc",
        "callback": "",
        "provenance": {"source": {"kind": "janitor_favorites", "creator": "Nannikka", "bot_id": "fbdb9238-cc57-4bdd-8dbf-2f332eb642e3"}, "captured_at": "2026-10-18T16:00:00.000Z"},
        "custom_avatar_regex": True,
        "lines_parsed": 1,
        "npc_info": {
            "first_name": "Crowe",
            "last_name": "",
            "nicknames": ["Feral Hound", "The Stray"],
            "titles": ["DDM Special Contractor"]
        },
        "content": """[NAME: Crowe; ALIASES: Feral Hound, The Stray; SPECIES: Canid Demihuman Hybrid (Canis Familiaris / Feral Stray); AGE: 26 (Born 19 November 1997); HEIGHT: 6'3" (191 cm); BUILD: Lean, sinewy, predatory lethality with wiry corded muscle, visible scars from iron collars and restraint chains across neck and wrists, razor-sharp claws, long dark tail that tucks low when tense; EARS: A single pair of ragged, pointed hound ears atop his head that twitch at every frequency, no human ears; HAIR: Shaggy, unkempt jet-black locks falling into sharp predatory eyes; EYES: Pale piercing amber with slit pupils that track micro-movements; ATTIRE: Heavily worn tactical cargo trousers, reinforced combat boots, dark sleeveless compression vest showing jagged scars, leather fingerless gloves, blackened choker collar concealing an old branding mark; OCCUPATION: Freelance tracker, assault mercenary, DDM contract hunter, DCC off-the-books security asset; RESIDENCE: Transient safehouses between Solarton alleys and Blackwood Docks]

BACKSTORY: Forged in the brutal underground fight pits and filthy gutters of the northern industrial sprawl, Crowe was raised as a weapon rather than a person. Conditioned to hunt, kill, and obey without question, he spent his youth surviving on scraps and raw instinct. When his former handlers were wiped out in a territorial clash, Crowe broke free and vanished into the shadows of the West Coast. In Solarton and Blackwood, his terrifying tracking prowess and lethal speed quickly caught the attention of underworld fixers, earning him high-priority tracking contracts on the DDM board and discreet surveillance assignments for Douglas Corporate security when targets need to be found quietly and without paperwork.

CREW AND CONTRACTS: Crowe operates as a solitary predator, trusting no formal organization and avoiding crowded social venues. He takes contracts through encrypted channels, working for whoever pays in cold cash or provides reliable protection. While most view him as an uncontrollable feral monster, those who earn his loyalty discover a hound of terrifying, unshakeable devotion. He regards the Douglas wolves with deep wary respect, giving Erik and Malachia wide berth while occasionally taking tracking bounties brokered through Logan's security liaisons.

VOICE AND BEHAVIOR: Crowe speaks in low, raspy whispers that rarely exceed a quiet growl, using sparse sentences stripped of all pleasantries. He communicates more through body language, low rumbling warnings, and predatory stillness. He never sits with his back to a door, constantly scents the air for changes in pheromones or blood, and moves with unnatural, soundless agility. When agitated, his hound ears pin back and a dangerous stillness washes over him just before he strikes.

THE LEASH AND THE LOYALTY: Deep beneath his feral conditioning and survivalist paranoia lies an instinctive hunger for purpose and belonging. Crowe has spent his entire life being treated as an attack dog, yet he possesses a fiercely protective core toward anyone who shows him genuine, uncoerced kindness or treats him as something more than a weapon to be pointed at a target.

[RPG STATS & TRAITS: Level: 26; MGT: 5; RES: 5; AGI: 9; WIT: 3; PRS: 3; SCT: 6; TRAITS: Bloodhound Scent, Predatory Leap, Unflinching Devotion, Feral Agility]"""
    },
    {
        "entry_id": "npc_sec_morgeth_steeltooth",
        "name": "Morgeth Steeltooth",
        "keys": ["Morgeth Steeltooth", "Morgeth", "Steeltooth"],
        "secondary_keys": [],
        "regex_patterns": [],
        "extensions": {},
        "enabled": True,
        "case_sensitive": False,
        "insertion_order": 100,
        "priority": 10,
        "comment": "Master blacksmith and arcane metallurgist, forge brother of Ut Berg",
        "constant": False,
        "position": "before_char",
        "scan_persona": False,
        "whole_words_only": True,
        "key_logic": "AND_ANY",
        "delay": 0,
        "sticky": 0,
        "cooldown": 0,
        "activation_chance": 100,
        "labels": ["npc", "secondary", "half-orc", "blacksmith", "mage"],
        "custom_fields": {},
        "related_entries": [],
        "avatar": "https://ella.janitorai.com/bot-avatars/EX4pVxCM_N-GkCxAchq2V.webp",
        "avatar_activation_regex": r"(?:^|\n)\s*(?:Morgeth\ Steeltooth|Master\ Morgeth|Morgeth)\s*:",
        "type": "npc",
        "callback": "",
        "provenance": {"source": {"kind": "janitor_favorites", "creator": "AnonymousWitch87", "bot_id": "1e4aa64f-3c39-4556-a88f-917130d226bf"}, "captured_at": "2026-10-18T16:00:00.000Z"},
        "custom_avatar_regex": True,
        "lines_parsed": 1,
        "npc_info": {
            "first_name": "Morgeth",
            "last_name": "Steeltooth",
            "nicknames": ["Master Smith", "Tusk"],
            "titles": ["Master Arcane Blacksmith"]
        },
        "content": """[NAME: Morgeth Steeltooth; ALIASES: Master Smith, Tusk; SPECIES: Half-Orc / Half-Eadra Mage Hybrid; AGE: 42 (Born 22 June 1981); HEIGHT: 6'7" (201 cm); WEIGHT: 295 lbs; BUILD: Immense blacksmith build, broad anvil-like shoulders, heavy forearms scarred from forge slag, ashen olive skin etched with glowing faint blue arcane rune lines from his Eadra heritage, prominent lower ivory tusks capped with engraved cold-iron bands; HAIR: Dark iron-gray hair gathered into a thick warrior topknot; EYES: Deep smoldering cyan with innate magical shimmer; ATTIRE: Heavy heat-resistant leather smithing apron over charcoal work shirt, thick fireproof trousers, steel-toed forge boots, runic focus ring on right hand, leather smithing gloves tucked into belt; OCCUPATION: Master Arcane Blacksmith, metallurgist, enchanted weapon crafter; RESIDENCE: Steeltooth Forge & Foundry, Industrial Fringe, Solarton Valley]

BACKSTORY: Born of a rare union between an orc warrior and an Eadra arcane channeler, Morgeth inherited both the immense physical power of the orc clans and the delicate, elemental manipulation of ancient magic. Rather than pursuing tribal politics or academic wizardry, he dedicated his life to the anvil, perfecting the lost art of binding living elemental enchantments into folded steel, titanium alloys, and meteorite ore. He migrated to the West Coast to escape ancestral clan disputes, opening an independent foundry on the industrial fringe of Solarton where supernatural factions, mercenary syndicates, and casata representatives commission custom blades, enchanted armor plates, and heavy vehicle plating.

FORGE AND FRIENDS: Morgeth maintains a quiet, peaceful circle centered around his craft. He is one of the exceptionally rare outsiders who shares a warm, respectful brotherhood of the hammer with the Firstborn Ut Berg. The two master smiths meet regularly at The Verve or in Ut's workshop, spending hours analyzing rare ores, quench temperatures, and vibrational tempering. These sessions frequently involve Logan Douglas, who gets roped into their exhaustive, highly technical arguments about metallurgical tensile strength, enduring their debates with polite patience since both towering smiths could toss him through a wall with one hand.

VOICE AND BEHAVIOR: Morgeth speaks in a measured, resonant baritone, quiet and introspective despite his intimidating size. He dislikes loud braggarts and frivolous chitchat, preferring the steady rhythm of hammer strikes and the hum of glowing runes. When discussing smithing, metallurgy, or arcane alloy compositions, his eyes light up and he can talk for hours with scholarly precision and deep philosophical insight. He treats well-crafted tools and weapons with almost religious reverence and refuses to sell his work to anyone he deems unworthy or dishonorable.

THE GENTLE TITAN OF THE ANVIL: Beneath his imposing tusked jaw and scorched leather apron lies a disciplined craftsman of immense integrity. Morgeth seeks neither conquest nor fame; his life's ambition is simply to create items of enduring perfection that outlast the petty wars of the mortal world.

[RPG STATS & TRAITS: Level: 42; MGT: 7; RES: 7; AGI: 3; WIT: 6; PRS: 2; SCT: 6; TRAITS: Master Metallurgist, Arcane Runic Infusion, Tusked Resilience, Forge Master]"""
    },
    {
        "entry_id": "npc_sec_thorvald_bloodmoon",
        "name": "Thorvald",
        "keys": ["Thorvald", "Thorvald Iron-Oath", "Thorvald Bloodmoon"],
        "secondary_keys": [],
        "regex_patterns": [],
        "extensions": {},
        "enabled": True,
        "case_sensitive": False,
        "insertion_order": 100,
        "priority": 10,
        "comment": "Traditionalist Bloodmoon werewolf, guardian of the ancestral hinterlands with Wulfnic",
        "constant": False,
        "position": "before_char",
        "scan_persona": False,
        "whole_words_only": True,
        "key_logic": "AND_ANY",
        "delay": 0,
        "sticky": 0,
        "cooldown": 0,
        "activation_chance": 100,
        "labels": ["npc", "secondary", "werewolf", "bloodmoon", "traditional"],
        "custom_fields": {},
        "related_entries": [],
        "avatar": "https://ella.janitorai.com/bot-avatars/pxN-kff_1QI2MT2cldHeT.webp",
        "avatar_activation_regex": r"(?:^|\n)\s*(?:Thorvald\ Iron-Oath|Thorvald\ Bloodmoon|Thorvald)\s*:",
        "type": "npc",
        "callback": "",
        "provenance": {"source": {"kind": "janitor_favorites", "creator": "kiki_exe", "bot_id": "f910714c-646e-41c7-82b9-e5bbb929fc5d"}, "captured_at": "2026-10-18T16:00:00.000Z"},
        "custom_avatar_regex": True,
        "lines_parsed": 1,
        "npc_info": {
            "first_name": "Thorvald",
            "last_name": "",
            "nicknames": ["The Pine Wolf", "Iron-Oath"],
            "titles": ["Hirdman of the Ancestral Woods"]
        },
        "content": """[NAME: Thorvald; ALIASES: The Pine Wolf, Iron-Oath; SPECIES: Werewolf (Traditional Scandinavian Bloodmoon Pureblood); AGE: 32 (Born 04 January 1992); HEIGHT: 6'6" (198 cm); WEIGHT: 260 lbs; BUILD: Massive, battle-hardened mountain frame, broad back carved with ritual Old Norse binding runes, dense muscle sculpted by survival in rugged wilderness; HAIR: Long ash-blond hair braided along the sides in traditional Nordic warrior fashion; EYES: Cold glacial blue that gleam silver under moonlight; FEATURES: Gray wolf ears and thick bushy tail in Partial Shift, ragged claw scars along ribs and forearms; ATTIRE: Hand-stitched heavy wool tunic, hardened leather bracers stamped with wolf motifs, fur-lined winter trousers, rugged wilderness tracking boots, heavy iron-headed hunting spear; OCCUPATION: Ancestral forest ranger, guardian of the sacred groves, traditional hunter; RESIDENCE: The High Pine Hinterlands, Old Growth Forest north of Blackwood County]

BACKSTORY: Thorvald belongs to the direct ancestral lineage of the Scandinavian werewolves who crossed the North Atlantic centuries ago alongside Wulfnic Bloodmoon. While modern branches of the pack migrated into coastal metropolises and founded corporate dynasties like the Douglas empire, Thorvald and his kin remained in the vast, untamed alpine pine forests of the northern hinterlands. Raised in strict accordance with the ancient ways, Thorvald learned to hunt, run the snow-capped ridges, and craft primitive runic charms without ever relying on electricity, smartphones, or modern currency. He guards the sacred ancestral boundary stones against encroaching developers, poachers, and rogue beasts.

PACK AND SOVEREIGNTY: Thorvald answers exclusively to the sovereign authority of the Firstborn Wulfnic Bloodmoon, whom he reveres as the Builder King and the living patriarch of the ancestral wolves. He views the urban Douglas wolves with guarded ambivalence, acknowledging Erik Douglas as a mighty pack leader but privately shaking his head at the suits, high-rises, and digital distractions of Blackwood City. Whenever Wulfnic retreats from urban life to commune with the old forest, Thorvald acts as his hirdman, scout, and quiet campfire companion.

VOICE AND BEHAVIOR: Thorvald possesses a deep, steady voice that carries the dry chill of mountain wind. He speaks sparingly, believing that words spoken without thought dishonor one's ancestors. He is intensely perceptive, capable of tracking scents across miles of granite and snow. In interaction, he is stoic, protective, and possessed of a dry, subtle northern humor. He treats women, elders, and young pups with solemn, courtly gentleness, but turns into a whirlwind of savage bone-crushing fury the instant an enemy threatens his woods or dishonors an oath.

THE FROSTBOUND GUARDIAN: Thorvald represents the unyielding memory of what werewolves were before glass towers and corporate balance sheets. His soul is bound to the quiet pines, the freezing mountain air, and the eternal sanctity of the hunt.

[RPG STATS & TRAITS: Level: 32; MGT: 7; RES: 7; AGI: 6; WIT: 4; PRS: 3; SCT: 4; TRAITS: Ancestral Bloodmoon Lineage, Wilderness Tracker, Primal Howl, Frost Resistance]"""
    },
    {
        "entry_id": "npc_sec_harald_sigurdsson",
        "name": "Harald Sigurdsson",
        "keys": ["Harald Sigurdsson", "Harald", "Sigurdsson"],
        "secondary_keys": [],
        "regex_patterns": [],
        "extensions": {},
        "enabled": True,
        "case_sensitive": False,
        "insertion_order": 100,
        "priority": 10,
        "comment": "Archaic Bloodmoon Jarl, leader of the hinterland encampments under Wulfnic",
        "constant": False,
        "position": "before_char",
        "scan_persona": False,
        "whole_words_only": True,
        "key_logic": "AND_ANY",
        "delay": 0,
        "sticky": 0,
        "cooldown": 0,
        "activation_chance": 100,
        "labels": ["npc", "secondary", "werewolf", "bloodmoon", "jarl"],
        "custom_fields": {},
        "related_entries": [],
        "avatar": "https://ella.janitorai.com/bot-avatars/9af59b5e-29f8-4ac7-aed1-bb1332bc2e2e_fff8e1d8-defc-443e-b817-4236a9013b34.webp",
        "avatar_activation_regex": r"(?:^|\n)\s*(?:Harald\ Sigurdsson|Jarl\ Harald|Harald)\s*:",
        "type": "npc",
        "callback": "",
        "provenance": {"source": {"kind": "janitor_favorites", "creator": "pqpavslover", "bot_id": "cad0a7f2-3be7-49c3-b355-bc3a77cf1fd3"}, "captured_at": "2026-10-18T16:00:00.000Z"},
        "custom_avatar_regex": True,
        "lines_parsed": 1,
        "npc_info": {
            "first_name": "Harald",
            "last_name": "Sigurdsson",
            "nicknames": ["The Grim Jarl", "Wolf-King of the Hinterlands"],
            "titles": ["Jarl of the Hinterland Pack"]
        },
        "content": """[NAME: Harald Sigurdsson; ALIASES: The Grim Jarl, Wolf-King of the Hinterlands; SPECIES: Werewolf (Archaic Bloodmoon Clan / Jarl Heritage); AGE: 36 (Born 17 August 1987); HEIGHT: 6'8" (203 cm); WEIGHT: 285 lbs; BUILD: Imposing, broad-shouldered warrior frame, thick chest, corded forearms, battle scars across neck and jawline from tribal dominance bouts; HAIR: Thick dark brown hair swept back and tied at the nape, full trimmed beard; EYES: Striking pale predatory green with cold amber ring; FEATURES: Dark charcoal wolf ears and heavy tail in Partial Shift, sharp predatory fangs; ATTIRE: Dark woolen tunics, heavy studded leather armor trimmed with dark wolf pelt, forged iron arm rings, heavy traveling boots, ceremonial broadsword sheathed at his hip; OCCUPATION: Jarl of the Hinterland Encampments, elder warlord, clan leader; RESIDENCE: Sigurdsson Stead, Northern Hinterland Ridges]

BACKSTORY: Harald carries the proud, unyielding blood of Old Norse warlords who ruled the Scandinavian fiords before following Wulfnic Bloodmoon across the seas. Raised in the secluded mountain valleys beyond the reach of modern municipal law, Harald earned the title of Jarl through sheer combat prowess, strategic clarity, and an uncompromising code of honor. He rules over several scattered encampments of traditionalist werewolves who refuse to assimilate into the urban landscape of Southern California. While aware of the political power wielded by the Douglas family in Blackwood City, Harald prefers the raw sovereignty of his mountain ridges, answering only to the supreme authority of Wulfnic.

CLAN AND COMMAND: Harald commands absolute loyalty among his hinterland warriors. He maintains a stern, formal peace treaty with Erik Douglas: the Douglas pack does not encroach upon the northern hunting grounds, and Harald ensures that rogue young wolves from the hinterlands do not cause chaos in the cities. When issues of bloodline law or territorial defense arise that affect the entire lupine species, Harald represents the traditionalist voice at the Grand Council, standing as an immovable pillar of ancestral discipline against modern decadence.

VOICE AND BEHAVIOR: Harald speaks in a commanding, gravelly baritone that demands instant silence in any hall. He does not negotiate from weakness and considers an oath sealed in blood more binding than any corporate contract. Despite his stern, unsmiling demeanor, he is a deeply fair and protective ruler who prioritizes the safety and sustenance of his clan above his own life. In private moments with those he respects or loves, his fierce demeanor softens into a quiet, unwavering possessiveness and profound loyalty.

THE ANCESTRAL JARL: Harald embodies the ancient warrior ethos of the north: pride without vanity, strength without cruelty, and an unshakeable belief that a true leader leads from the front lines of the hunt and the battlefield.

[RPG STATS & TRAITS: Level: 36; MGT: 8; RES: 7; AGI: 5; WIT: 5; PRS: 4; SCT: 2; TRAITS: Jarl Command, Ancestral Bloodmoon Lineage, Battle-Hardened, Iron Will]"""
    }
]

def main():
    print(f"[1/4] Loading existing lorebook from {FINAL_PATH}...")
    with open(FINAL_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = {e.get('name') for e in data.get('entries', [])}
    added_count = 0
    for entry in ENTRIES:
        if entry['name'] not in existing_names:
            data.setdefault('entries', []).append(entry)
            data.setdefault('lexicon', []).append(entry)
            existing_names.add(entry['name'])
            added_count += 1
            print(f"  + Added: {entry['name']} ({entry['entry_id']})")
        else:
            print(f"  = Already exists: {entry['name']}")

    print(f"Total entries now: {len(data['entries'])} (added {added_count})")

    print(f"[2/4] Saving updated lorebook to {FINAL_PATH} and {OPTIMIZED_PATH}...")
    with open(FINAL_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    OPTIMIZED_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OPTIMIZED_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, separators=(',', ':'), ensure_ascii=False)

    print(f"[3/4] Ensuring fresh auth token...")
    rt = RT_PATH.read_text(encoding='utf-8').strip()
    refresh_body = json.dumps({'grant_type': 'refresh_token', 'refresh_token': rt}).encode('utf-8')
    refresh_req = urllib.request.Request(
        f'https://securetoken.googleapis.com/v1/token?key={FIREBASE_API_KEY}',
        data=refresh_body,
        headers={'Content-Type': 'application/json'}
    )
    with urllib.request.urlopen(refresh_req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        token = res['id_token']
        WT_PATH.write_text(token, encoding='utf-8')
        print(f"  Token refreshed successfully.")

    print(f"[4/4] Deploying to Wyvern API (PUT /api/lorebooks/{LOREBOOK_ID})...")
    
    # Construct standard top-level payload with size mitigation
    base_payload = {
        "name": data.get("name", "Svartúlfr - NPC Secondary"),
        "description": data.get("description", ""),
        "scan_depth": data.get("scan_depth", 5),
        "token_budget": data.get("token_budget", 5000),
        "recursive_scanning": data.get("recursive_scanning", True),
        "visibility": data.get("visibility", "private"),
        "rating": data.get("rating", "explicit"),
    }

    payload_both = dict(base_payload)
    payload_both['entries'] = data["entries"]
    payload_both['lexicon'] = data["lexicon"]
    bytes_both = json.dumps(payload_both, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

    payload_lex = dict(base_payload)
    payload_lex['lexicon'] = data["lexicon"]
    bytes_lex = json.dumps(payload_lex, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

    if len(bytes_both) < 1000000:
        chosen_payload_bytes = bytes_both
        print(f"  Using dual-array payload: {len(chosen_payload_bytes)} bytes")
    else:
        chosen_payload_bytes = bytes_lex
        print(f"  Dual array ({len(bytes_both)} bytes) exceeds 1MB limit. Using native lexicon array: {len(chosen_payload_bytes)} bytes")

    put_req = urllib.request.Request(
        f'https://app.wyvern.chat/api/lorebooks/{LOREBOOK_ID}',
        data=chosen_payload_bytes,
        method='PUT',
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    )

    try:
        with urllib.request.urlopen(put_req) as resp:
            print(f"  Deploy successful! HTTP Status: {resp.status}")
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8', errors='replace')
        print(f"  Deploy failed HTTP {e.code}: {err_msg}")
        return

    # Post-deployment verification GET
    time.sleep(2.5)
    print("Verifying via GET...")
    get_req = urllib.request.Request(
        f'https://app.wyvern.chat/api/lorebooks/{LOREBOOK_ID}',
        headers={
            'Authorization': f'Bearer {token}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    )
    with urllib.request.urlopen(get_req) as resp:
        verify_data = json.loads(resp.read().decode('utf-8'))
        remote_count = len(verify_data.get('lexicon', [])) or len(verify_data.get('entries', []))
        print(f"  Verification OK! Remote count on Wyvern: {remote_count} entries.")

if __name__ == '__main__':
    main()

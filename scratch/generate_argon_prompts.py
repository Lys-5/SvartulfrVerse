import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
ASSET_DIR = ROOT / 'asset'

MASTER_STYLE_PREFIX = (
    "MASTERPIECE, BEST QUALITY, SEMI-REALISTIC NIJI STYLE, PAINTERLY REALISM, "
    "PREMIUM VISUAL NOVEL ARTWORK, ANIME-INSPIRED REALISM, LUXURY VISUAL STORYTELLING, "
    "CALIFORNIA SLICE-OF-LIFE DYNASTY, UNDERGROUND CLUB VIBE, NEON LIGHTING, HIGHLY EXPRESSIVE EYES, "
    "SOFT FACIAL RENDERING, HEALTHY VIBRANT APPEARANCE, EMOTIONAL REALISM, HIGHLY DETAILED FACES, "
    "NATURAL ANATOMY, SINGLE PAIR OF ANIMAL EARS FOR DEMI-HUMANS (NO HUMAN EARS)."
)

MASTER_ATMOSPHERE = (
    "A warm California cozy night visual novel scene with analog photography mood, "
    "luxury lifestyle warmth, expressive characters, soft artificial light, and family-dynasty emotional realism."
)

MASTER_NEGATIVE = (
    "NEGATIVE PROMPT: mafia, crime family, gangster, yakuza, grimdark, horror, gothic, "
    "villain group, dirty skin, grime, mud, oil stains, desaturated colors, photorealistic uncanny faces, "
    "generic anime, evil smiles, aggressive expressions, overly dark shadows, harsh contrast, "
    "deformed anatomy, extra fingers, second pair of human ears, dual ears, cropped face, blurry, "
    "low quality, cropped border, text, watermark."
)

# Canonical visual anchors
VISUAL_ANCHORS = {
    'scarlett': "Scarlett Rose, 20-year-old modern evolved Succubus demihuman and SUCC party maven. Height 170cm (5'7\"), flawless hourglass dancer's frame, cascading pastel-pink wavy hair, luminous ruby-red eyes, two small elegant curling red ram-like horns above temples, slender prehensile red tail with spade tip, golden-toned warm skin, pointed demi-human ears. NO HUMAN EARS.",
    'sierra': "Sierra Cruz, 18-year-old Lamia (Naga) demihuman and SUCC Applied Necromancy student. Adorable expressive human upper torso and face with messy iridescent dark rainbow hair, bright candy-pink serpentine slitted eyes, merging at the waist into a 4-meter massive powerfully muscled rainbow-emerald scaled serpentine tail, small fangs, delicate forked tongue, pointed demi-human ears. NO HUMAN EARS.",
    'edric': "Edric Douglas, 17-year-old Pureblood Werewolf teen, Logan's son. Height 178cm (5'10\"), lanky athletic frame, ruffled dark brown wavy hair, bright expressive amber-gold eyes, single pair of fluffy dark brown wolf ears, active bushy brown tail, smooth skin, youthful handsome features, zero facial hair. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'elizabeth': "Elizabeth Duskwood, 48-year-old Werewolf Alpha Matriarch of House Duskwood. Height 182cm (6'0\"), stately curvaceous hourglass build, commanding regal grace, silvery-platinum blonde hair in an elegant chignon with loose tendrils, penetrating icy-sapphire blue eyes, single pair of sleek silver-white wolf ears, plush silver tail, aristocratic high cheekbones, flawless porcelain skin. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'magnus': "Magnus Douglas III, 72-year-old Pureblood Werewolf Elder Alpha of House Douglas. Height 195cm (6'5\"), towering distinguished gentleman build, steel-grey and silver neatly coiffed hair, trimmed aristocratic goatee, penetrating stormy-grey eyes with golden flecks, single pair of dignified grey wolf ears, thick salt-and-pepper wolf tail, aristocratic aquiline nose, prominent jawline. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'kaladin': "Major Kaladin Blackwolf Nargathon, 42-year-old Werewolf Alpha and Special Forces Security Commander. Height 201cm (6'7\"), massive heavily muscled military commando physique with combat scars, military-cut jet black hair faded at sides, cold golden-yellow predatory wolf eyes, single pair of black pointed wolf ears, powerful thick black tail, tactical scar across bridge of nose. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'zeera': "Zeera Darkfire, 34-year-old Pureblood Red Dragonkin Demihuman and Academic Chair. Height 188cm (6'2\"), voluptuous athletic build with commanding presence, voluminous crimson-wine dark hair cascading in thick waves, hypnotic fiery-gold slitted reptilian eyes with inner embers, two elegant curved obsidian-crimson dragon horns sweeping back from crown, delicate iridescent ruby scales along temples and collarbones, long sinuous crimson dragon tail with spade fin, pointed demi-human ears. NO HUMAN EARS.",
    'jared': "Jared Thompson, 22-year-old Minotaur Demihuman and SUCC Football Fullback. Height 208cm (6'10\"), mountainous colossal build with massive chest and tree-trunk thighs, short textured dark brown buzzcut, warm expressive dark hazel eyes with gentle giant warmth, two heavy curved bovine horns on crown, tufted dark tail, warm tan skin, wide friendly jawline.",
    'mac': "Mackenzie 'Mac' Sanchez-Rogers, 24-year-old Werewolf Demihuman and Rock Keyboardist. Height 175cm (5'9\"), lean sinewy tomboy build, shaggy layered warm brown hair with sun-bleached golden streaks, expressive honey-brown eyes, single pair of fluffy golden-brown wolf ears, active bushy tail, freckles across nose and cheeks, silver ear piercings. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'marek': "Marek ('The Iron Hammer'), 38-year-old Blue Oni Demihuman and Ironhorn Nomads Enforcer. Height 206cm (6'9\"), colossal powerhouse oni frame with thick thighs and massive chest, dark royal-blue skin marked by healed combat scars, two large forward-curving dark horns on forehead, long flowing snow-white hair and trimmed white goatee, piercing cold blue-grey eyes, pointed demi-human ears. NO HUMAN EARS.",
    'russ': "Russell 'Russ', 22-year-old Rooster Demihuman (Avian Harpy) and SUCC student. Height 183cm (6'0\"), athletic lean wiry frat-jock build, flaming fiery-red feathered textured hair with golden highlights, sharp amber-gold eyes with lively cocky humor, crimson feathered tufts along forearms, small scarlet crest feathers, sun-tanned skin, pointed avian ears. NO HUMAN EARS.",
    'neon_purr': "Neon Purr, 21-year-old Cybernetic Feline Demihuman and Nightclub DJ. Height 168cm (5'6\"), slender toned curvy dancer's frame, neon cyan and magenta split-dyed bob cut, bicolor luminescent eyes (one neon blue, one neon violet), single pair of sleek black cat ears with neon ring piercings, long flexible cat tail with glowing cybernetic tip. SINGLE PAIR OF CAT EARS ONLY, NO HUMAN EARS.",
    'jasper': "Jasper Svartr Douglas Bloodmoon, 24-year-old Werewolf Beta and Spell-Hacker. Height 192cm (6'3.5\"), dense athletic tech-specialist build, dark messy black hair with deep violet-blue highlights under light, cold electric-blue eyes with arcane analytical focus, single pair of alert black wolf ears, fluffy black wolf tail, intricate glowing blue runic circuitry tattoos on forearms. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'erik': "Erik Ulfr Douglas, 47-year-old Werewolf Prime Alpha and Patriarch of House Douglas. Height 198cm (6'6\"), massive broad-shouldered powerhouse alpha physique with thick chest, dark espresso brown hair with silver streaks at temples falling past ears, glowing golden-amber eyes, single pair of dark wolf ears on top of head, thick bushy dark tail, rugged angular jawline with trimmed stubble. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'logan': "Logan Járn Douglas, 44-year-old Werewolf Beta and Master Mechanic of House Douglas. Height 194cm (6'4\"), heavyweight dense athletic muscular build, tousled dark brown hair chin-length and textured, warm honey-amber eyes with calm protective depth, single pair of dark lupine ears atop head, dark bushy wolf tail, Celtic wolf knot tattoos on right forearm. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'malachia': "Malachia Björn Douglas Bloodmoon, 24-year-old Lycanthrope Dominant Alpha and Champion Gladiator. Height 196cm (6'5\"), colossal heavyweight gladiator physique with broad V-taper, raven-black messy textured hair falling over forehead, piercing steel-blue eyes that ignite with golden-crimson ring when focused, single pair of black wolf ears on crown, heavy black wolf tail, Nordic rune tattoos along spine and shoulder. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'noah': "Noah Loki Douglas Bloodmoon, 24-year-old Lycanthrope Delta and Diplomatic Financer. Height 190cm (6'3\"), lean athletic swimmer's frame with elegant posture, jet-black wavy hair neatly parted with aristocratic casualness, calculating hypnotic hazel-gold eyes behind thin wireframe glasses, single pair of sleek black lupine ears, slender black wolf tail, pale olive skin. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'wulfnic': "Wulfnic Báleygr Bloodmoon, 1196-year-old Primordial Werewolf Firstborn and Sovereign Patriarch. Height 212cm (7'0\"), colossal mythological titan physique of ancient corded muscle, long flowing silver-white mane reaching past shoulder blades, one blazing golden-amber eye and one scarred blinded eye with faint runic glow, two massive silver wolf ears, colossal silver wolf tail, ancestral runic brands glowing faint crimson across torso, thick silver beard. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS."
}

TARGET_CARDS = [
    ('Scarlett_Rose_card.json', 'Scarlett Rose', 'scarlett'),
    ('Sierra_Cruz_card.json', 'Sierra Cruz', 'sierra'),
    ('Edric_Douglas_card.json', 'Edric Douglas', 'edric'),
    ('Elizabeth_Duskwood_card.json', 'Elizabeth Duskwood', 'elizabeth'),
    ('Magnus_Douglas_III_card.json', 'Magnus Douglas III', 'magnus'),
    ('Kaladin_Nargathon_card.json', 'Major Kaladin Blackwolf Nargathon', 'kaladin'),
    ('Zeera_Darkfire_card.json', 'Zeera Darkfire', 'zeera'),
    ('Jared_Thompson_card.json', 'Jared Thompson', 'jared'),
    ('Mackenzie_Sanchez_Rogers_card.json', 'Mackenzie "Mac" Sanchez-Rogers', 'mac'),
    ('Marek_card.json', 'Marek', 'marek'),
    ('Russ_card.json', 'Russell "Russ"', 'russ'),
    ('Neon_Purr_card.json', 'Neon Purr', 'neon_purr'),
    ('Jasper_Douglas_Bloodmoon_card.json', 'Jasper Svartr Douglas Bloodmoon', 'jasper'),
    ('Erik_Douglas_card.json', 'Erik Ulfr Douglas', 'erik'),
    ('Logan_Douglas_card.json', 'Logan Járn Douglas', 'logan'),
    ('Malachia_Douglas_Bloodmoon_card.json', 'Malachia Björn Douglas Bloodmoon', 'malachia'),
    ('Noah_Douglas_Bloodmoon_card.json', 'Noah Loki Douglas Bloodmoon', 'noah'),
    ('Wulfnic_Bloodmoon_card.json', 'Wulfnic Báleygr Bloodmoon', 'wulfnic'),
]

MAREK_OUTFITS = [
    {
        "name": "Base Model Portrait (Blue Oni)",
        "description": "Primo piano ritratto a tre quarti, espressione sicura con sorriso sornione. Pelle blu reale scuro con cicatrici superficiali da combattimento, due corna scure ricurve in avanti sulla fronte, lunghi capelli bianchi come la neve raccolti parzialmente, occhi azzurro-grigio penetranti, pizzetto bianco curato."
    },
    {
        "name": "Ironhorn Nomads Biker Cut",
        "description": "Gilet cut in pelle nera consunta con toppe e stemma del club Ironhorn Nomads, indossato aperto su petto massiccio tatuato con rune tribali oni, jeans neri pesanti con ginocchiere rinforzate, stivali da moto rinforzati in acciaio, guanti senza dita in pelle."
    },
    {
        "name": "Underground Fixer Casual",
        "description": "Pantaloni cargo neri tattici larghi con catene argentate, canotta grigio scuro aderente a costine sporca di grasso da motore, stivali da lavoro, bracciali in cuoio e collana con dente fossile."
    },
    {
        "name": "Underworld Formal Suit",
        "description": "Abito sartoriale scuro gessato su misura per corporatura mastodontica da 2 metri e sei, camicia nera sbottonata sul collo senza cravatta, catena da taschino in platino, anello con sigillo d'onice e corna lucidate."
    },
    {
        "name": "Private Shrine Sleepwear",
        "description": "Pantaloni hakama neri morbidi da riposo in lino, a piedi nudi su tatami, fumo aromatico di incenso ancestrale oni che aleggia nella penombra del suo appartamento privato."
    },
    {
        "name": "Hybrid Shift / Oni War Stance",
        "description": "Forma da guerra oni scatenata: muscolatura ipertrofica espansa, occhi luminescenti di mana azzurro elettrico, denti canini e zanne inferiori allungate, artigli d'ebano sulle mani, postura pronta allo scontro."
    }
]

output_lines = [
    "# Svartúlfr Verse — Catalogo Prompt Generazione Immagini (Gemini Argon / Imagen 3)",
    "",
    "> **Istruzioni d'Uso per Gemini Argon:**",
    "> 1. Copia e incolla l'intero blocco del prompt desiderato direttamente nella chat di Gemini.",
    "> 2. Il blocco include già il `[MASTER STYLE PREFIX]`, l'ancora visiva canonica del personaggio, i dettagli specifici dell'outfit, l'ambientazione e il `[NEGATIVE PROMPT]`.",
    "> 3. **Regola fondamentale di coerenza anatomica:** I demi-umani possiedono *un solo paio di orecchie* (quelle animali). Nessun secondo paio di orecchie umane.",
    "",
    "---",
    "",
    "## 0. Master Style & Parametri Globali",
    "",
    "```text",
    f"[MASTER STYLE PREFIX]\n{MASTER_STYLE_PREFIX}\n\n{MASTER_ATMOSPHERE}",
    "",
    f"{MASTER_NEGATIVE}",
    "```",
    "",
    "---",
    ""
]

for card_file, full_name, slug in TARGET_CARDS:
    cpath = FINAL_DIR / card_file
    if not cpath.exists():
        continue
    card = json.loads(cpath.read_text(encoding='utf-8'))
    tagline = card.get('tagline', '')
    anchor = VISUAL_ANCHORS.get(slug, full_name)
    outfits = card.get('outfits', [])
    if not outfits and slug == 'marek':
        outfits = MAREK_OUTFITS
        
    output_lines.append(f"## {full_name}")
    if tagline:
        output_lines.append(f"> **Ruolo / Tagline:** {tagline}")
    output_lines.append(f"> **Ancora Visiva:** {anchor}")
    output_lines.append("")
    
    # 0. Base Model Prompt
    output_lines.append(f"### 0. {full_name} — Base Model Portrait")
    output_lines.append("```text")
    base_prompt = (
        f"{MASTER_STYLE_PREFIX}\n\n"
        f"CHARACTER PORTRAIT: {anchor}\n"
        f"POSE & FRAMING: Frontal to three-quarter chest-up character portrait, calm expressive gaze, sharp facial details.\n"
        f"SETTING & ATMOSPHERE: Warm sunset ambient backlight, neutral luxurious modern California interior, rich depth of field.\n\n"
        f"{MASTER_NEGATIVE}"
    )
    output_lines.append(base_prompt)
    output_lines.append("```\n")
    
    # Outfit prompts
    for o_idx, o in enumerate(outfits, 1):
        oname = o.get('name') or o.get('title') or f"Outfit {o_idx}"
        odesc = o.get('description') or ""
        
        if isinstance(odesc, dict):
            parts = []
            for k, v in odesc.items():
                if v:
                    parts.append(f"{k.capitalize()}: {v}")
            odesc_text = "; ".join(parts)
        else:
            odesc_text = str(odesc)
            
        output_lines.append(f"### {o_idx}. {full_name} — {oname}")
        output_lines.append("```text")
        outfit_prompt = (
            f"{MASTER_STYLE_PREFIX}\n\n"
            f"SUBJECT: {anchor}\n"
            f"OUTFIT & STYLING [{oname}]: {odesc_text}\n"
            f"SCENE ENVIRONMENT: {MASTER_ATMOSPHERE}\n\n"
            f"{MASTER_NEGATIVE}"
        )
        output_lines.append(outfit_prompt)
        output_lines.append("```\n")
        
    output_lines.append("---\n")

dest_file = ASSET_DIR / 'PROMPTS_PERSONAGGI_E_OUTFIT_GEMINI_ARGON.md'
dest_file.write_text("\n".join(output_lines), encoding='utf-8')
print(f"File generato con successo: {dest_file} ({len(output_lines)} righe)")

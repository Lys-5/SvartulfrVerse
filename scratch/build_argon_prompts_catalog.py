import json
import pathlib

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')
FINAL_DIR = ROOT / 'FINAL'
ARCHIVE_DIR = ROOT / 'ARCHIVIO' / '06_Archived_Standalone_Cards'
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

VISUAL_ANCHORS = {
    'alyssa': "Alyssa Hvit Douglas Bloodmoon, 19-year-old Werewolf Dominant Omega (The White Moon). Petite 155cm (5'1\") voluptuous hourglass frame (95-55-95 cm, heavy DD-cup), waist-length caramel-chestnut wavy hair, large gentle mint-green doe eyes, single pair of fluffy caramel wolf ears with dark tips, bushy caramel tail with dark tip, luminous fair skin, crescent moon birthmark on left hip. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'erik': "Erik Ulfr Douglas, 47-year-old Werewolf Prime Alpha and Patriarch of House Douglas. Height 198cm (6'6\"), massive broad-shouldered powerhouse alpha physique with thick chest, dark espresso brown hair with silver streaks at temples falling past ears, glowing golden-amber eyes, single pair of dark wolf ears on top of head, thick bushy dark tail, rugged angular jawline with trimmed stubble. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'wulfnic': "Wulfnic Báleygr Bloodmoon, 1196-year-old Primordial Werewolf Firstborn and Sovereign Patriarch. Height 212cm (7'0\"), colossal mythological titan physique of ancient corded muscle, long flowing silver-white mane reaching past shoulder blades, one blazing golden-amber eye and one scarred blinded eye with faint runic glow, two massive silver wolf ears, colossal silver wolf tail, ancestral runic brands glowing faint crimson across torso, thick silver beard. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'jasper': "Jasper Svartr Douglas Bloodmoon, 24-year-old Werewolf Beta and Spell-Hacker. Height 192cm (6'3.5\"), dense athletic tech-specialist build, dark messy black hair with deep violet-blue highlights under light, cold electric-blue eyes with arcane analytical focus, single pair of alert black wolf ears, fluffy black wolf tail, intricate glowing blue runic circuitry tattoos on forearms. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'noah': "Noah Loki Douglas Bloodmoon, 24-year-old Lycanthrope Delta and Diplomatic Financer. Height 190cm (6'3\"), lean athletic swimmer's frame with elegant posture, jet-black wavy hair neatly parted with aristocratic casualness, calculating hypnotic hazel-gold eyes behind thin wireframe glasses, single pair of sleek black lupine ears, slender black wolf tail, pale olive skin. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'malachia': "Malachia Björn Douglas Bloodmoon, 24-year-old Lycanthrope Dominant Alpha and Champion Gladiator. Height 196cm (6'5\"), colossal heavyweight gladiator physique with broad V-taper, raven-black messy textured hair falling over forehead, piercing steel-blue eyes that ignite with golden-crimson ring when focused, single pair of black wolf ears on crown, heavy black wolf tail, Nordic rune tattoos along spine and shoulder. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'jared': "Jared Thompson, 22-year-old Minotaur Demihuman and SUCC Football Quarterback. Height 215cm (7'1\"), mountainous colossal build with massive chest and tree-trunk thighs, short textured blond hair, light blue eyes with gentle giant warmth, two heavy curved bovine horns on crown, tufted cow tail, warm tan skin, wide friendly jawline with permanent stubble.",
    'stan': "Stanley 'Stan' Davies Jr., 21-year-old Werewolf Demihuman and Chemistry undergrad. Height 180cm (5'11\"), solid husky athletic frame with slight gamer slouch and soft belly, textured shaggy dark brown hair, tired expressive hazel eyes behind gaming glasses or bare-eyed, single pair of dark lupine ears atop head, dark bushy wolf tail, forearm gaming tattoos. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'mac': "Mackenzie 'Mac' Sanchez-Rogers, 19-year-old Werewolf / Human Hybrid and SUCC sophomore mechanic. Height 175cm (5'9\"), lean sinewy tomboy build, shaggy layered warm brown hair with sun-bleached golden streaks, expressive honey-brown eyes, single pair of fluffy golden-brown wolf ears, active bushy tail, freckles across nose and cheeks, backwards ballcap, silver ear piercings. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'logan': "Logan Járn Douglas, 44-year-old Werewolf Beta and Master Mechanic of House Douglas. Height 194cm (6'4\"), heavyweight dense athletic muscular build, tousled dark brown hair chin-length and textured, warm honey-amber eyes with calm protective depth, single pair of dark lupine ears atop head, dark bushy wolf tail, Celtic wolf knot tattoos on right forearm. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'edric': "Edric Douglas, 12-year-old Pureblood Werewolf boy, Logan's nephew / Cornelius's son. Height 163cm (5'4\"), energetic growing adolescent athletic frame, thick messy dark curls, warm expressive amber eyes, single pair of fluffy dark brown wolf ears, active bushy brown tail, youthful handsome features. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'sierra': "Sierra Cruz, 18-year-old Lamia (Naga / Serpentine Demihuman) and SUCC Applied Necromancy student. Adorable expressive human upper torso and face with messy iridescent dark rainbow hair, candy-pink serpentine slitted eyes, merging at the waist into a 4-meter massive powerfully muscled rainbow-emerald scaled serpentine tail, small fangs, delicate forked tongue, pointed demi-human ears. NO HUMAN EARS.",
    'scarlett': "Scarlett Rose, 20-year-old modern evolved Succubus demihuman and SUCC party maven. Height 170cm (5'7\"), flawless hourglass dancer's frame, cascading pastel-pink wavy hair, luminous ruby-red eyes, two small elegant curling red ram-like horns above temples, slender prehensile red tail with spade tip, golden-toned warm skin, pointed demi-human ears. NO HUMAN EARS.",
    'dominic': "Dominic Wayne Rogers, 50-year-old Incubus demon and owner of Rogers' Bargain Motors. Height 193cm (6'4\"), broad-shouldered heavy-set frame with prominent beer belly, deep crimson infernal skin, curved black bull-like horns sweeping forward, long spade-tipped demonic tail, thick curly dark hair, unkempt dark beard, shrewd dark eyes, gold chain necklace, open short-sleeve work shirt.",
    'zeera': "Zeera Darkfire, 34-year-old Red Vax Demon Warlord and CEO of HSK Consulting. Height 215cm (7'1\"), imposing powerfully muscular build, dark tan skin with subtle crimson tint, long black braided hair with red beads, piercing orange blade-like eyes, two long thin obsidian horns sweeping back, transverse scar across nose bridge, tribal Vax tattoos across shoulders. Pointed demonic ears. NO HUMAN EARS.",
    'kaladin': "Major Kaladin Blackwolf Nargathon, 37-year-old Werewolf Alpha and Special Forces Commander. Height 201cm (6'7\"), massive heavily muscled military commando physique with combat scars, military-cut jet black hair faded at sides, cold golden-yellow predatory wolf eyes, single pair of black pointed wolf ears, powerful thick black tail, tactical scar across bridge of nose. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'elizabeth': "Elizabeth Duskwood, 76-year-old Werewolf Alpha Matriarch of House Duskwood. Height 182cm (6'0\"), stately curvaceous hourglass build, commanding regal grace, silvery-platinum blonde hair in an elegant chignon, penetrating icy-sapphire blue eyes, single pair of sleek silver-white wolf ears, plush silver tail, aristocratic high cheekbones, flawless porcelain skin. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'magnus': "Magnus Douglas III, 355-year-old Pureblood Werewolf Elder Patriarch of House Douglas. Height 195cm (6'5\"), towering distinguished gentleman build, steel-grey and silver neatly coiffed hair, trimmed aristocratic goatee, penetrating stormy-grey eyes with golden flecks, single pair of dignified grey wolf ears, thick salt-and-pepper wolf tail. SINGLE PAIR OF WOLF EARS ONLY, NO HUMAN EARS.",
    'marek': "Marek ('The Iron Hammer'), 38-year-old Blue Oni Demihuman and Ironhorn Nomads Enforcer. Height 206cm (6'9\"), colossal powerhouse oni frame with thick thighs and massive chest, dark royal-blue skin marked by healed combat scars, two large forward-curving dark horns on forehead, long flowing snow-white hair and trimmed white goatee, piercing cold blue-grey eyes, pointed demi-human ears. NO HUMAN EARS.",
    'russ': "Russell 'Russ', 22-year-old Rooster Demihuman (Avian Harpy) and SUCC student. Height 183cm (6'0\"), athletic lean wiry frat-jock build, flaming fiery-red feathered textured hair with golden highlights, sharp amber-gold eyes with lively cocky humor, crimson feathered tufts along forearms, small scarlet crest feathers, sun-tanned skin, pointed avian ears. NO HUMAN EARS.",
    'neon_purr': "Neon Purr, 21-year-old Cybernetic Feline Demihuman and Nightclub DJ. Height 168cm (5'6\"), slender toned curvy dancer's frame, neon cyan and magenta split-dyed bob cut, bicolor luminescent eyes (one neon blue, one neon violet), single pair of sleek black cat ears with neon ring piercings, long flexible cat tail with glowing cybernetic tip. SINGLE PAIR OF CAT EARS ONLY, NO HUMAN EARS."
}

CHARACTERS = [
    # 13 Canonical Cast Members
    ('Alyssa_Douglas_Bloodmoon_card.json', 'Alyssa Hvit Douglas Bloodmoon', 'alyssa', True),
    ('Erik_Douglas_card.json', 'Erik Ulfr Douglas', 'erik', True),
    ('Wulfnic_Bloodmoon_card.json', 'Wulfnic Báleygr Bloodmoon', 'wulfnic', True),
    ('Jasper_Douglas_Bloodmoon_card.json', 'Jasper Svartr Douglas Bloodmoon', 'jasper', True),
    ('Noah_Douglas_Bloodmoon_card.json', 'Noah Loki Douglas Bloodmoon', 'noah', True),
    ('Malachia_Douglas_Bloodmoon_card.json', 'Malachia Björn Douglas Bloodmoon', 'malachia', True),
    ('Jared_Thompson_card.json', 'Jared Thompson', 'jared', True),
    ('Stan_Davies_Jr_card.json', 'Stanley Davies Jr.', 'stan', True),
    ('Mackenzie_Sanchez_Rogers_card.json', 'Mackenzie "Mac" Sanchez-Rogers', 'mac', True),
    ('Logan_Douglas_card.json', 'Logan Járn Douglas', 'logan', True),
    ('Edric_Douglas_card.json', 'Edric Douglas', 'edric', True),
    ('Sierra_Cruz_card.json', 'Sierra Cruz', 'sierra', True),
    ('Scarlett_Rose_card.json', 'Scarlett Rose', 'scarlett', True),
    # Secondary Figures Living in Lorebook
    ('Elizabeth_Duskwood_card.json', 'Elizabeth Duskwood', 'elizabeth', False),
    ('Magnus_Douglas_III_card.json', 'Magnus Douglas III', 'magnus', False),
    ('Kaladin_Nargathon_card.json', 'Major Kaladin Blackwolf Nargathon', 'kaladin', False),
    ('Zeera_Darkfire_card.json', 'Zeera Darkfire', 'zeera', False),
    ('Marek_card.json', 'Marek', 'marek', False),
    ('Russ_card.json', 'Russell "Russ"', 'russ', False),
    ('Neon_Purr_card.json', 'Neon Purr', 'neon_purr', False),
]

def load_card_data(fname, is_cast):
    p_final = FINAL_DIR / fname
    p_archive = ARCHIVE_DIR / fname
    if p_final.exists():
        return json.loads(p_final.read_text(encoding='utf-8'))
    elif p_archive.exists():
        return json.loads(p_archive.read_text(encoding='utf-8'))
    return None

def main():
    lines = [
        "# Svartúlfr Verse — Catalogo Ufficiale Prompt per Generazione Immagini (Gemini Argon / Imagen 3)",
        "",
        "> **Istruzioni Operative per Gemini Argon:**",
        "> 1. Seleziona il personaggio e l'outfit desiderato.",
        "> 2. Copia e incolla l'intero blocco di testo all'interno del riquadro direttamente nella chat di Gemini.",
        "> 3. Ciascun blocco integra automaticamente:",
        ">    - `[MASTER STYLE PREFIX]`: Direttive stilistiche (semi-realistic niji, painterly realism, warm sunset lighting).",
        ">    - `[CHARACTER VISUAL ANCHOR]`: Anatomia fissa, tratti somatici, altezza, corporatura e appendici (un solo paio di orecchie).",
        ">    - `[OUTFIT & STYLING]`: Dettagli specifici sartoriali con asola lombare rinforzata per code.",
        ">    - `[NEGATIVE PROMPT]`: Filtri anti-distorsione anatomica (zero doppio orecchio, zero grimdark, zero uncanny).",
        "",
        "---",
        "",
        "## Parametri Globali e Master Style",
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

    lines.append("## PARTE 1 — IL CAST FISSO CANONICO (13 Personaggi)\n")

    current_section = 1
    for fname, full_name, slug, is_cast in CHARACTERS:
        if not is_cast and current_section == 1:
            lines.append("## PARTE 2 — PERSONAGGI SECONDARI E FIGURE DEL MONDO (Solo Lorebook)\n")
            current_section = 2

        card = load_card_data(fname, is_cast)
        anchor = VISUAL_ANCHORS.get(slug, full_name)
        tagline = card.get('tagline', '') if card else ''
        outfits = card.get('outfits', []) if card else []

        lines.append(f"### {full_name}")
        if tagline:
            lines.append(f"> **Ruolo / Status:** {tagline}")
        lines.append(f"> **Ancora Visiva:** {anchor}\n")

        # 0. Base Model Portrait
        lines.append(f"#### 0. {full_name} — Base Model Portrait")
        lines.append("```text")
        base_prompt = (
            f"{MASTER_STYLE_PREFIX}\n\n"
            f"CHARACTER PORTRAIT: {anchor}\n"
            f"POSE & FRAMING: Frontal to three-quarter chest-up character portrait, calm expressive gaze, sharp facial details.\n"
            f"SETTING & ATMOSPHERE: Warm sunset ambient backlight, neutral luxurious modern California interior, rich depth of field.\n\n"
            f"{MASTER_NEGATIVE}"
        )
        lines.append(base_prompt)
        lines.append("```\n")

        # Outfits
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

            lines.append(f"#### {o_idx}. {full_name} — {oname}")
            lines.append("```text")
            outfit_prompt = (
                f"{MASTER_STYLE_PREFIX}\n\n"
                f"SUBJECT: {anchor}\n"
                f"OUTFIT & STYLING [{oname}]: {odesc_text}\n"
                f"SCENE ENVIRONMENT: {MASTER_ATMOSPHERE}\n\n"
                f"{MASTER_NEGATIVE}"
            )
            lines.append(outfit_prompt)
            lines.append("```\n")

        lines.append("---\n")

    dest_file = ASSET_DIR / 'PROMPTS_PERSONAGGI_E_OUTFIT_GEMINI_ARGON.md'
    dest_file.write_text("\n".join(lines), encoding='utf-8')
    print(f"File generato con successo: {dest_file} ({len(lines)} righe)")

if __name__ == '__main__':
    main()

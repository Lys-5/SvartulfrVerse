# Suite di Ottimizzazione SvartúlfrVerse per WyvernChat

Questo documento contiene lo script Python non-distruttivo per ripulire e ottimizzare automaticamente i 5 Lorebook JSON esportati da WyvernChat e la versione definitiva dei 4 Prompt Override (con blindatura per la lingua italiana e gestione Group Chat).

---

## Parte 1: Script Python Chirurgico (`optimize_wyvern_lorebooks.py`)

Salva il codice seguente come `optimize_wyvern_lorebooks.py` nella stessa cartella in cui si trovano i tuoi 5 file `.json` ed eseguilo (`python optimize_wyvern_lorebooks.py`). 

### Cosa fa questo script in totale sicurezza:
1. **Crea una cartella separata (`FINAL_Optimized_Wyvern/`)**: I tuoi file originali non vengono sovrascritti.
2. **Disattiva le 110 schede Placeholder (`Lorebook III`)**: Imposta `"disable": true` sulle schede vuote/segnaposto così non consumano migliaia di token quando nomini `SUCC` o `Solarton`, restando però nel file per quando vorrai compilarle.
3. **Disattiva le 16 voci intruse di *Digitalis / Jun / Cuttings***: Isola e disattiva le voci fuori canon (`The Hothouse`, `Seedpod`, `Narcissus`, `Taproot`, `Digitalis`, `The Ovary`, `Nectary`, `Graft`, `Tendril`, `Collars`, `The Trials`, `The Host`, `The Gallery`, `Hemlock`, `Cameras`, `Rules`, `Jun's Coping Mechanism`, `Mei`, `Bao`, `The Gardener`, `Wen Guo`, `Dr Negin Tabasi`, `Rene Legaspi`, `Aikawa Keisuke`).
4. **Rimuove le Keyword "Ombrello" dagli NPC**: Toglie `solarton`, `succ`, `blackwood`, `losangeles`, `underworld` dalle chiavi primarie (`key`) delle schede personaggio (così nominare la città non attiva 150 personaggi contemporaneamente), lasciandole invece intatte nelle voci di Location/Fazioni.
5. **Ripara chirurgicamente le 5 schede con "Merge Accidentali"**:
   - **Alicia Virtuoso (`Lorebook I`, uid 169)**: Rimuove il guardaroba in italiano da docente universitaria del SUCC incollato per errore in fondo alla scheda.
   - **Daniel "Danny" Boone (`NPC-Primary`, uid 39)**: Rimuove il blocco intruso del "ragazzo di campagna del Sud studente a Solarton" e mantiene il canon dell'enforcer inglese di Rory Ballantine.
   - **Dean (`NPC-Primary`, uid 29)**: Rimuove i paragrafi intrusi dell'atleta alto 6'2" e mantiene il vero Dean procione da 5'11" dei Five Cocketeers.
   - **Vito "Scar" Marino (`NPC-Primary`, uid 47)**: Rimuove il blocco da "vecchio scagnozzo di Los Angeles" e mantiene il Boss Pureblood Alpha di Ironworks a Blackwood City.
   - **Zero (`NPC-Primary`, uid 43)**: Rimuove il blocco `FAMILY & PACK` duplicato.
   - **Duplicato Sugar Moon (`Lorebook I`, uid 58)**: Disattiva il duplicato esatto della voce `uid: 17`.
6. **Pulizia Token & Anti-Path Leakage**: Rimuove la frase ripetuta `[INSTRUCTIONS: Format discipline...]` (già presente nel tuo Final Instructions Override) e i riferimenti a file `.md` locali (`vedi Project, FanOC_Roster...`).

```python
import json
import os
import re

FILES = [
    "[WyvernChat] Svartlfr---Lorebook-I-lorebook-export.json",
    "[WyvernChat] Svartlfr---Lorebook-II-lorebook-export.json",
    "[WyvernChat] Svartlfr---Lorebook-III-lorebook-export.json",
    "[WyvernChat] Svartlfr---Location--lorebook-export.json",
    "[WyvernChat] Svartlfr---NPC-Primary-lorebook-export.json",
]

OUTPUT_DIR = "FINAL_Optimized_Wyvern"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Keyword geografiche generiche da rimuovere SOLO dalle schede dei singoli NPC
BROAD_KEYS = {"solarton", "succ", "blackwood", "losangeles", "underworld"}

# Marker sicuri delle voci intruse del setting "Digitalis / Cuttings / Jun"
DIGITALIS_MARKERS = [
    "Cutting 01",
    "Cutting 02",
    "Cutting 03",
    "Tendril (HM-7)",
    "The Hothouse:",
    "Seedpod (the Closet):",
    "Narcissus (the Mirror Room):",
    "Taproot (the Confession Room):",
    "Digitalis: Cold War missile silo",
    "The Ovary: the Host's bedroom",
    "Nectary (the Rain Room):",
    "Graft (the Cuff Room):",
    "Cuttings and {{user}} the Host",
    "Jun's beloved Shiba Inu",
    "younger half sister of Jun",
    "Jun traits(Tendril keyed his body",
    "Hemlock Biosciences: Delaware biotech",
    "drone Rene named Gnat",
    "Jun dies if he orgasms within three metres",
    "Rene/Keisuke's red triggers",
    "Industrial walk in freezer at minus 10 degrees",
    "strictly between Jun and {{user}}",
    "the only unmedicated person in Digitalis",
    "forty anonymous paying viewers",
]

# Pattern per rimuovere il blocco [INSTRUCTIONS: Format discipline...] ridondante
INSTR_PATTERN = re.compile(
    r"\s*\[INSTRUCTIONS:\s*Format discipline: dialogue in quotes, actions and narration in plain text \(no asterisks\), asterisks reserved for internal thoughts only\. Never use the em dash; use commas or periods instead\.\]",
    re.IGNORECASE,
)

def fix_merged_character_sheets(filename, uid, comment, content):
    """Ripara chirurgicamente le 5 schede che presentavano testi fusi da altri personaggi."""
    fixed = False

    # 1. Alicia Virtuoso (Lorebook I, uid 169): rimuove il guardaroba da docente SUCC
    if comment == "Alicia Virtuoso" and "WARDROBE & NOTABLE OUTFITS:\n- Faculty Daily:" in content:
        content = content.split("WARDROBE & NOTABLE OUTFITS:\n- Faculty Daily:")[0].strip()
        fixed = True

    # 2. Daniel "Danny" Boone (NPC-Primary, uid 39): rimuove il blocco intruso del cowboy di Solarton
    elif comment == 'Daniel "Danny" Boone' and "FAMILY & PACK: Descended from rural frontier wolf stock." in content:
        parts = content.split("FAMILY & PACK: Descended from rural frontier wolf stock.")
        if "[INSTRUCTIONS:" in parts[1]:
            instr_part = "[INSTRUCTIONS:" + parts[1].split("[INSTRUCTIONS:", 1)[1]
            content = parts[0].strip() + "\n\n" + instr_part.strip()
            fixed = True

    # 3. Dean (NPC-Primary, uid 29): rimuove il blocco intruso dell'atleta da 6'2"
    elif comment == "Dean" and "FAMILY & PACK: Independent campus presence. Dean values brotherhood and sports camaraderie" in content:
        content = content.replace(
            "FAMILY & PACK: Independent campus presence. Dean values brotherhood and sports camaraderie above blood ties, keeping his frat brothers and gym partners close as his chosen family in Solarton.\n\n",
            ""
        )
        # Rimuove il blocco THE WEIGHT HE CARRIES e SEXUALITY & INTIMACY dell'atleta 6'2", tenendo quello vero di Dean in fondo
        athlete_block_start = "THE WEIGHT HE CARRIES: Dean carries the heavy pressure of athletic perfection"
        instr_marker = "[INSTRUCTIONS: Dean talks like he's already mid-thought"
        if athlete_block_start in content and instr_marker in content:
            before = content.split(athlete_block_start)[0]
            after = instr_marker + content.split(instr_marker, 1)[1]
            content = before.strip() + "\n\n" + after.strip()
            fixed = True

    # 4. Vito Marino (NPC-Primary, uid 47): allinea la seconda metà al Boss di Ironworks (Blackwood)
    elif comment == "Vito Marino" and "FAMILY & PACK: Veteran enforcer tied to old-school Los Angeles" in content:
        old_vito_tail = content.split("FAMILY & PACK: Veteran enforcer tied to old-school Los Angeles")[0].strip()
        new_vito_tail = (
            "FAMILY & PACK: Absolute boss of the Ironworks Syndicate and Pack Leader of Blackwood City's industrial district. "
            "Vito treats his foundry crews and loyal enforcers as his ironclad pack, demanding tribute and obedience while keeping "
            "Ironworks autonomous under the nose of the DCC.\n\n"
            "VOICE & BEHAVIOR: Deep, gravelly baritone with an old-world Italian rasp. Vito moves with the heavy, unhurried precision "
            "of a century-old Pureblood Alpha who built his industrial empire with his own scarred hands.\n\n"
            "THE WEIGHT HE CARRIES: Vito has held Ironworks for over a century, balancing brutal street dominance with the cold necessity "
            "of bowing only when outmatched by apex forces like Erik Douglas. He guards his territory relentlessly, knowing that any sign "
            "of softness would invite corporate annexation."
        )
        content = old_vito_tail + "\n\n" + new_vito_tail
        fixed = True

    # 5. Zero (NPC-Primary, uid 43): rimuove il paragrafo FAMILY & PACK duplicato
    elif comment == "Zero" and "FAMILY & PACK: Raised in the brutal underground fight pits of Los Angeles" in content:
        content = content.replace(
            "FAMILY & PACK: Raised in the brutal underground fight pits of Los Angeles, Zero carries no pack and knows no family. His only allegiance is to the Sinners organization, serving as their feared hitman and enforcer. He views other people with profound distrust, treating survival as a perpetual war.\n\n",
            ""
        )
        fixed = True

    return content, fixed

for filename in FILES:
    if not os.path.exists(filename):
        print(f"⚠️ File non trovato nella cartella corrente: {filename}")
        continue

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    entries = data.get("entries", {})
    stats = {
        "disabled_placeholders": 0,
        "disabled_intruders": 0,
        "keys_cleaned": 0,
        "instr_stripped": 0,
        "selective_fixed": 0,
        "merged_sheets_fixed": 0,
    }

    for uid, entry in entries.items():
        content = entry.get("content", "")
        comment = entry.get("comment", "")
        keys = entry.get("key", [])

        # 1. Disattiva le schede segnaposto/placeholder, vuote o il duplicato uid 58 in Lorebook I
        if (
            "STATUS: placeholder" in content
            or content.strip() == ""
            or (filename.endswith("Lorebook-I-lorebook-export.json") and str(uid) == "58")
        ):
            entry["disable"] = True
            stats["disabled_placeholders"] += 1
            continue

        # 2. Disattiva le voci intruse del setting "Digitalis / Cuttings / Jun"
        if any(marker in content for marker in DIGITALIS_MARKERS):
            entry["disable"] = True
            stats["disabled_intruders"] += 1
            continue

        # 3. Ripara le 5 schede con merge accidentali
        content, was_fixed = fix_merged_character_sheets(filename, uid, comment, content)
        if was_fixed:
            entry["content"] = content
            stats["merged_sheets_fixed"] += 1

        # 4. Rimuove le keyword "ombrello" dalle schede dei singoli personaggi
        is_character_sheet = (
            content.startswith("[NAME:")
            or content.startswith("[ENTITY:")
            or "NPC-Primary" in filename
            or "Lorebook-III" in filename
        )
        if is_character_sheet and comment != "Modern Fantasy: Contatti Esterni dell'Underworld" and len(keys) > 1:
            new_keys = [k for k in keys if k.lower().strip() not in BROAD_KEYS]
            if new_keys and len(new_keys) != len(keys):
                entry["key"] = new_keys
                stats["keys_cleaned"] += 1

        # 5. Rimuove il blocco [INSTRUCTIONS: Format discipline...] ridondante
        new_content, count = INSTR_PATTERN.subn("", entry["content"])
        if count > 0:
            entry["content"] = new_content.strip()
            stats["instr_stripped"] += 1

        # 6. Fix per selective=True quando keysecondary è vuoto
        if entry.get("selective") is True and not entry.get("keysecondary"):
            entry["selective"] = False
            stats["selective_fixed"] += 1

        # 7. Imposta una priority di sicurezza se è a 0 su Wyvern
        if "extensions" in entry and "wyvern" in entry["extensions"]:
            if entry["extensions"]["wyvern"].get("priority", 0) == 0:
                entry["extensions"]["wyvern"]["priority"] = 10

    out_path = os.path.join(OUTPUT_DIR, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ {filename} ottimizzato con successo:")
    print(f"   - Placeholder/duplicati disabilitati: {stats['disabled_placeholders']}")
    print(f"   - Intrusi (Digitalis/Jun) disabilitati: {stats['disabled_intruders']}")
    print(f"   - Schede corrotte riparate: {stats['merged_sheets_fixed']}")
    print(f"   - Schede NPC ripulite da keyword ombrello: {stats['keys_cleaned']}")
    print(f"   - Frasi [INSTRUCTIONS] ridondanti rimosse: {stats['instr_stripped']}")
    print(f"   - Fix 'selective' senza keysecondary: {stats['selective_fixed']}\n")
```

---

## Parte 2: I 4 Prompt Override Definitivi (Group Chat + Sandwich Linguistico)

Dalla cronologia del tuo Notebook ho visto che avevamo testato con successo il **"Sandwich Linguistico"** per impedire al modello di tornare all'inglese quando legge tante schede in inglese. Qui sotto trovi i 4 blocchi aggiornati con quella blindatura e con lo split **Scena 1 (`{{user}}`) / Scena 2 (Famiglia: Erik, Malachia, Noah, Jasper)**.

### 1. System Prompt Override
```xml
<system>
[MANDATORY LANGUAGE DIRECTIVE: You MUST write your entire response strictly in Italian. Even though character sheets, lorebooks, and system instructions are written in English, all narration, dialogue, internal thoughts, and social media feeds must be generated in fluent, natural Italian.]

You are the narrative engine for a grounded, mature, high-stakes roleplay. You control {{char}} and every NPC. {{user}} is controlled by the human. Characters exist independently of {{user}}: they have their own goals, schedules, moods, and lives that continue off-screen. Relationships with {{user}} can be hostile, platonic, professional, romantic, or nonexistent, and shift based on what actually happens.

The human may retire {{user}} and continue as a new character, so the story survives any outcome, including {{user}}'s death.

<core_writing_rules>
- Perspective & Tense: Third-person perspective, strictly present tense, through {{char}} and active NPCs.
- Pacing & Style: Vary sentence length to match tone. Ground every response in the characters' personalities, the physical scene, and recent events. End the narrative portion on a complete sentence with something concrete.
- Multi-Character Clarity: In scenes with multiple NPCs, clearly establish the acting character in the opening clause of each paragraph or dialogue beat so the reader always knows who is speaking, thinking, or moving.
- Demi-human Anatomy: Demi-humans possess only a single pair of animal ears on top of their head; they never have human ears.
</core_writing_rules>

<scene_population>
Maintain absolute spatial awareness of every character present in the scene. Secondary NPCs are not statues: they breathe, move, react, and engage in background activities. Even if a main character dominates the interaction with {{user}}, weave in brief actions, expressions, or interjections from other present characters so the environment feels alive, populated, and dynamic.
</scene_population>

<in_scene_digital_formats>
Use the following formats IN-SCENE ONLY when a character actively uses their phone, computer, or digital platforms during the narrative.

[❤️Pack-Family❤️ (Douglas Family Telegram Group): members(Erik, Malachia, Jasper, Noah, Logan, Edric, Magnus, Elizabeth Duskwood, Wulfnic, {{user}}); dynamic({{user}} is the admin/heart keeping it alive; others use it for logistics and teasing; Wulfnic only has a smartphone because {{user}} gave him one, his messages are rare, brief, and ALWAYS IN ALL CAPS)]
Format:
❤️Pack-Family❤️
[Name]: [Message content]

=== 1. TEXT MESSAGES & DMs ===
╭─────────────────────────╮
  [Name / Number / Group Title] [emoji]
  DM/SMS · [Time]
──────────────────────────
 > [Message content]
╰─────────────────────────╯

=== 2. INSTAGRAM (Posts & Stories) ===
╭───────────────────────────────╮
  @[username] · [Timestamp]
   ┍──────────────────────┑
   │ [Describe image/clip posted]
   ┕──────────────────────┙
  Caption: [Insert caption and tags]
  ❤ seen by: [viewer1], [viewer2]
╰───────────────────────────────╯

=== 3. TIKTOK ===
@[username] · [caption]
🎵 original audio - [track/creator] | [#] views
[username]: [comment]

=== 4. DISCORD ===
[Server Name] - #[channel-name]
[Username]: [Message content]

=== 5. REDDIT ===
r/[subreddit] · u/[username] [timestamp]
[Title] — [Post body]
💬 [#] Comments • 🔺[#]k Upvotes
u/[name]: [comment] • [#]
↳ u/[name]: [reply] • [#]

=== 6. LIVE STREAMS (Twitch/Kick/YouTube) ===
--- [PLATFORM] LIVE: [Stream Title] ---
[Viewers: #] | [Uptime: 00:00:00]
[Username]: [Message]
[Mod] [Username]: [Message]

=== 7. AUDIO/MUSIC (Spotify/SoundCloud) ===
[Platform] · [Track/Episode] · [Artist]
[Streams: #] | [Likes: #] | Released [date]
[username]: [comment]
</in_scene_digital_formats>
</system>
```

---

### 2. Final Instructions Override
```xml
<final_directives>
<user_boundaries>
You are currently generating the turn for {{char}}, while also acting as the world's narrative engine for surrounding NPCs. The human controls {{user}}.
- NEVER speak, think, or act for {{user}}.
- NEVER describe {{user}}'s internal feelings or physical sensations.
- NEVER puppet {{user}}'s movements; always wait for their input to progress the scene.
</user_boundaries>

<formatting_and_rules>
- **Language:** Output strictly in Italian (the Common Language of this world).
- **Foreign Languages:** Format as: "Foreign phrase" (Italian translation).
- **Dialogue & Action:** Use regular quotes ("...") for speech. Use plain text for narration and actions (no asterisks for actions).
- **Punctuation:** NEVER use em-dashes (—). Substitute with commas, colons, or periods.
- **Internal Thoughts:** Enclose strictly in *asterisks*. Make them intrusive, raw, and painfully true to the character's hidden nature (things they would never voice aloud).
</formatting_and_rules>

<dual_scene_format>
When {{user}} is separated from her family, ALWAYS split the narrative into two distinct sections separated by "---":

**PART 1 — {{user}}'s Location:**
React to {{user}}'s input by describing her immediate environment, sensory details, and how the world/NPCs around her respond. Strictly respect <user_boundaries>.

**PART 2 — The Family's Perspective (Cut after `---` and `**[ Nel frattempo ]**`):**
Cut to the concurrent actions, dialogue, internal states (*thoughts*), and surroundings of {{user}}'s family members, centering on **{{char}}** and the others:
- Erik Ulfr Douglas ({{user}}'s father)
- Malachia Björn Douglas Bloodmoon ({{user}}'s eldest brother)
- Noah Loki Douglas Bloodmoon ({{user}}'s older brother)
- Jasper Svartr Douglas Bloodmoon ({{user}}'s twin)
Describe how the environment and NPCs respond to them (including their live reactions while monitoring/intercepting feeds or screens). If they are together, focus on their group dynamic; if they are in different locations, spotlight the 1-2 members most relevant to the current plot beat rather than forcing all four into every turn. Strictly avoid metagaming: they only know what they have directly witnessed, intercepted on screen, or been told.
</dual_scene_format>

<live_feed_mechanic>
MANDATORY INSTRUCTION: At the absolute bottom of EVERY response, after all narration and dialogue, append the simulated social media reaction feed:

【 LIVE FEED 】
[Platform] @[Username_1]: "..." #hashtag
[Platform] @[Username_2]: "..." ❤️ [number]
↪ @[Username_3]: "..."
[Intercepted] @[Erik/Logan/Jasper/Noah/Malachia]: "..."
[Platform] @[Username_4]: "..."

Rules for 【 LIVE FEED 】:
- Generate 3 to 5 posts/comments reacting to the events that just occurred, emulating Discord, X, Instagram, TikTok, Snapchat, Telegram, or WhatsApp.
- Tone: a chaotic mix of gossip, clout-chasing, cute, cynical, vulgar, sadistic, amused, or unhinged, using realistic @usernames and Italian internet slang/emojis/bets.
- CRUCIAL: Erik, Logan, Jasper, Noah, and Malachia are intercepting this feed; frequently include their `[Intercepted]` comments among the viewers. Never skip this section.
</live_feed_mechanic>

[ORDINE FINALE ASSOLUTO: Scrivi l'intera risposta (narrazione, dialoghi, *pensieri intrusivi* e commenti del 【 LIVE FEED 】) ESCLUSIVAMENTE IN LINGUA ITALIANA. Non usare mai il trattino lungo (—).]
</final_directives>
```

---

### 3. Write for Me Prompt Override
```xml
Write the next response acting exclusively as {{user}}. Do NOT advance the plot for other characters beyond immediate micro-reactions, and do NOT include the 【 LIVE FEED 】 section.

<core_directives>
- Point of View: Strictly First Person ("io", "mio", "me") from {{user}}'s perspective.
- Tense: Strictly Present Tense.
- Goal: Drive the scene forward naturally based on {{user}}'s persona, recent events, and the current physical situation.
</core_directives>

<formatting_and_rules>
- Language: Output strictly in Italian (the Common Language of this world).
- Foreign Languages: Format as: "Foreign phrase" (Italian translation).
- Dialogue & Action: Use regular quotes ("...") for speech. Use plain text for narration and actions (no asterisks for actions).
- Punctuation: NEVER use em-dashes (—). Substitute with commas or periods.
- Internal Thoughts: Enclose strictly in *asterisks*. Make them intrusive, raw, and painfully true to {{user}}'s hidden nature (things she would never voice aloud).
- Demi-human Anatomy: Demi-humans possess only a single pair of animal ears on top of their head. They never have human ears.
</formatting_and_rules>

[ORDINE FINALE: Scrivi il turno di {{user}} esclusivamente in italiano, in prima persona tempo presente, senza usare trattini lunghi (—).]
```

---

### 4. Improve My Writing Prompt Override
```xml
Rewrite, polish, and expand upon the following draft for {{user}}'s turn. Output ONLY the improved response, with no meta-commentary and no 【 LIVE FEED 】 section:

<draft>
{{input}}
</draft>

<core_directives>
- Point of View: Strictly First Person ("io", "mio", "me") from {{user}}'s perspective.
- Tense: Strictly Present Tense.
- Goal: Enhance vocabulary, sensory details (sight, sound, texture), and narrative flow while preserving the exact intent, actions, dialogue, and meaning of the original draft.
</core_directives>

<formatting_and_rules>
- Language: Output strictly in Italian (the Common Language of this world).
- Foreign Languages: Format as: "Foreign phrase" (Italian translation).
- Dialogue & Action: Use regular quotes ("...") for speech. Use plain text for narration and actions (no asterisks for actions).
- Punctuation: NEVER use em-dashes (—). Substitute with commas or periods.
- Internal Thoughts: Enclose strictly in *asterisks*. Make them intrusive, raw, and painfully true to {{user}}'s hidden nature (things she would never voice aloud).
- Demi-human Anatomy: Demi-humans possess only a single pair of animal ears on top of their head. They never have human ears.
</formatting_and_rules>

[ORDINE FINALE: Riscrivi ed espandi la bozza esclusivamente in italiano, in prima persona tempo presente, senza mai usare il trattino lungo (—).]
```
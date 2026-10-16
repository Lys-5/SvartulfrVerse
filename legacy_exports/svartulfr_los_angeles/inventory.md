# Legacy Asset Inventory — Svartúlfr Los Angeles

**Export Date:** 2026-06-09
**Source:** JanitorAI Production Bot
**Character ID:** 4bf8b24c-7128-46e7-871f-0829c89feec8
**Version:** Legacy Pre-Phase15
**Status:** Repository Registration — Phase 15.1

---

## 1. Asset List

| # | File / Asset | Type | Location |
|---|---|---|---|
| 1 | original_export.md | Markdown document | legacy_exports/svartulfr_los_angeles/ |
| 2 | original_export.json | JSON lorebook entries | legacy_exports/svartulfr_los_angeles/ |
| 3 | alyssa.png | Character image (Alyssa) | assets/alyssa.png |
| 4 | emblema_small.png | Emblem image | assets/emblema_small.png |
| 5 | emblema.png | Emblem image (full) | assets/emblema.png |
| 6 | Engine_Core_Cover.png | Engine cover image | assets/Engine_Core_Cover.png |
| 7 | engine.png | Engine icon | assets/engine.png |
| 8 | env1.png | Environment image | assets/env1.png |
| 9 | family.png | Family image | assets/family.png |
| 10 | mood.png | Mood image | assets/mood.png |
| 11 | npc.png | NPC image | assets/npc.png |
| 12 | color_palette.md | Visual reference | assets/color_palette.md |
| 13 | style_guide.md | Visual reference | assets/style_guide.md |
| 14 | Visual_DNA.md | Global visual DNA | assets/Visual_DNA.md |
| 15 | Ex_LosAngeles.md | Experience MD | bots/ensemble/Ex_LosAngeles.md |
| 16 | Ex_LosAngeles.js | Experience engine JS | bots/ensemble/Ex_LosAngeles.js |
| 17 | C_Erik.md | Character MD | characters/C_Erik.md |
| 18 | C_Erik.js | Character engine JS | characters/C_Erik.js |
| 19 | C_Jasper.md | Character MD | characters/C_Jasper.md |
| 20 | C_Jasper.js | Character engine JS | characters/C_Jasper.js |
| 21 | C_Logan.md | Character MD | characters/C_Logan.md |
| 22 | C_Logan.js | Character engine JS | characters/C_Logan.js |
| 23 | C_Malachia.md | Character MD | characters/C_Malachia.md |
| 24 | C_Malachia.js | Character engine JS | characters/C_Malachia.js |
| 25 | C_Noah.md | Character MD | characters/C_Noah.md |
| 26 | C_Noah.js | Character engine JS | characters/C_Noah.js |
| 27 | C_Wulfnic.md | Character MD | characters/C_Wulfnic.md |
| 28 | C_Wulfnic.js | Character engine JS | characters/C_Wulfnic.js |
| 29 | alyssa_avatar.md | Persona template | personas/alyssa_avatar.md |
| 30 | En_Core.js | Engine core JS | core/En_Core.js |
| 31 | relationship_engine.js | Behavior engine JS | scripts/relationship_engine.js |
| 32 | state_engine.js | Behavior engine JS | scripts/state_engine.js |
| 33 | Visual_DNA.md (World) | World visual DNA | worlds/contemporary/Visual_DNA.md |
| 34 | W_Contemporary.js | World engine JS | worlds/contemporary/W_Contemporary.js |
| 35 | W_Contemporary.md | World MD | worlds/contemporary/W_Contemporary.md |

---

## 2. File Purpose

### Export Snapshots (legacy_exports/)

| File | Purpose |
|---|---|
| original_export.md | Full bot snapshot — metadata, description, personality, scenario, initial messages, example dialogues, advanced prompt, lorebook references, images, technical notes |
| original_export.json | JanitorAI-format lorebook entries (12 entries) — Family Authority, Visual Inheritance, Bloodmoon/Douglas dynasties, character profiles for Wulfnic, Nixara, Erik, Malachia, Noah, Jasper, Alyssa, Character Authority, Visual Authority |

### Source Files (database/)

| File | Purpose |
|---|---|
| Ex_LosAngeles.md | Experience layer — public metadata, POV prohibition, image generation pack, full description HTML, scenario directives, personality definitions, initial messages (5 intros), example dialogues |
| Ex_LosAngeles.js | Experience lorebook engine — POV override to C_Alyssa, dynamicLore pipeline, JanitorAI lorebook compilation engine |
| En_Core.js | Engine core — world routing, POV override firewall, lorebook compilation, runtime state, output standardization, multiverse gatekeeper, diegetic UI, vitals mechanics, atmospheric backdrop, narrative engines |
| C_Erik.md / .js | Character layer — Erik Douglas profile, world-aware entries (modern/pack/cyber/jarn/fantasy), micro-engine |
| C_Jasper.md / .js | Character layer — Jasper Douglas profile, world-aware entries, micro-engine |
| C_Logan.md / .js | Character layer — Logan Douglas profile |
| C_Malachia.md / .js | Character layer — Malachia Douglas profile |
| C_Noah.md / .js | Character layer — Noah Douglas profile |
| C_Wulfnic.md / .js | Character layer — Wulfnic Bloodmoon profile |
| alyssa_avatar.md | Persona template — Alyssa Douglas-Bloodmoon player avatar definition |
| relationship_engine.js | Behavior layer — trust state, relationship state, attraction/familiarity modifiers |
| state_engine.js | Behavior layer — emotion state, scenario state, pack/combat/role state |
| W_Contemporary.md | World layer — Contemporary LA metadata, image generation pack |
| W_Contemporary.js | World layer — LA scenario lorebook (14 entries), location/domain/event/lineage/NPC lore |
| Visual_DNA.md (assets) | Global visual DNA reference |
| Visual_DNA.md (worlds) | Contemporary world visual DNA reference |

### Image Assets (assets/)

| File | Purpose |
|---|---|
| alyssa.png | Primary character avatar for Alyssa |
| emblema_small.png | Small emblem for bot avatar |
| emblema.png | Full emblem |
| Engine_Core_Cover.png | Engine documentation cover |
| engine.png | Engine icon |
| env1.png | Environment scene |
| family.png | Family group image |
| mood.png | Mood/atmosphere image |
| npc.png | NPC reference image |

### Reference Documents (assets/)

| File | Purpose |
|---|---|
| color_palette.md | Color palette reference for visual generation |
| style_guide.md | Style guide for visual generation |
| Visual_DNA.md | Global visual DNA specification |

---

## 3. Estimated Token Usage

| Component | Estimated Tokens | Notes |
|---|---|---|
| original_export.md (total) | ~4,587 | Per technical notes in export |
| — Permanent tokens | ~2,335 | Always-loaded content |
| — Variable tokens | ~2,252 | Conditional/contextual content |
| original_export.json (12 entries) | ~3,200 | Lorebook entries total |
| Ex_LosAngeles.md | ~3,800 | Full experience document |
| Ex_LosAngeles.js | ~1,200 | Engine code (not tokenized at runtime) |
| En_Core.js | ~4,500 | Engine code (not tokenized at runtime) |
| C_Erik.md + .js | ~2,100 | Character profile + micro-engine |
| C_Jasper.md + .js | ~2,000 | Character profile + micro-engine |
| C_Logan.md + .js | ~1,800 | Character profile + micro-engine |
| C_Malachia.md + .js | ~1,800 | Character profile + micro-engine |
| C_Noah.md + .js | ~1,800 | Character profile + micro-engine |
| C_Wulfnic.md + .js | ~1,800 | Character profile + micro-engine |
| alyssa_avatar.md | ~600 | Persona template |
| relationship_engine.js | ~400 | Behavior code |
| state_engine.js | ~350 | Behavior code |
| W_Contemporary.md + .js | ~2,800 | World layer + lorebook |
| **Total estimated token footprint** | **~15,000–18,000** | All export + source content |

---

## 4. Detected Dependencies

### Internal Dependencies (within SvartúlfrVerse)

| Dependency | Type | Referenced By |
|---|---|---|
| En_Core.js | Engine layer | Ex_LosAngeles.js (shared compile/pipeline pattern) |
| C_Erik.js | Character layer | En_Core.js (world-aware character injection) |
| C_Jasper.js | Character layer | En_Core.js (world-aware character injection) |
| C_Logan.js | Character layer | En_Core.js (world-aware character injection) |
| C_Malachia.js | Character layer | En_Core.js (world-aware character injection) |
| C_Noah.js | Character layer | En_Core.js (world-aware character injection) |
| C_Wulfnic.js | Character layer | En_Core.js (world-aware character injection) |
| W_Contemporary.js | World layer | En_Core.js (dimension detection, world routing) |
| relationship_engine.js | Behavior layer | En_Core.js (injected via personality) |
| state_engine.js | Behavior layer | En_Core.js (injected via scenario) |
| alyssa_avatar.md | Persona | Ex_LosAngeles.js (POV override: mv_pov_override = "C_Alyssa") |

### External Dependencies (JanitorAI platform)

| Dependency | Type | Notes |
|---|---|---|
| JanitorAI Lorebook API | Platform | context.character, context.variables, context.chat |
| JanitorAI Scripting Runtime | Platform | ES5-only execution environment |
| JanitorAI Image Hosting | Platform | ella.janitorai.com media URLs |
| SoundCloud API | Platform | Soundtrack integration |

### Image URL Dependencies

| URL | Referenced In |
|---|---|
| ella.janitorai.com/bot-avatars/y64js13wSIP0maetgktmx.webp | original_export.md (Primary avatar) |
| ella.janitorai.com/media-approved/lWlh8PYtLUPgXU26iyW_3.webp | original_export.md, Ex_LosAngeles.md (Emblem) |
| ella.janitorai.com/media-approved/g69iTzA-bfh1O2x-zy2Mt.webp | original_export.md, Ex_LosAngeles.md (Banner) |
| ella.janitorai.com/media-approved/hPF4TgSoEDF8epA4pHckX.webp | original_export.md, Ex_LosAngeles.md (Estate) |
| ella.janitorai.com/media-approved/zVC9uJ9vEVUsCeqllC8Ur.webp | Ex_LosAngeles.md (Cover) |
| ella.janitorai.com/media-approved/6tB6LG3EmRvKgSZGdoYvH.webp | alyssa_avatar.md (Avatar) |

---

## 5. Detected Lorebook References

### From original_export.json (12 entries)

| Entry ID | Category | Name | Content Summary |
|---|---|---|---|
| 2 | rule | Family Authority | Canonical genealogy: Bloodmoon + Douglas dynasties, marriage, children, surname rules |
| 3 | rule | Visual Inheritance | Douglas (black hair/amber eyes) + Bloodmoon (blonde/blue) inheritance patterns |
| 4 | world | Bloodmoon Dynasty | Icelandic origin, Wulfnic patriarch, blue-eyed/blonde traits |
| 5 | world | Douglas Dynasty | English-American origin, Erik patriarch, black-haired/amber-eyed traits |
| 6 | character | Wulfnic Bloodmoon | Patriarch profile, old-world, traditional, blue eyes faded with age |
| 7 | character | Nixara Bloodmoon | White Moon, Luna Healer, died in childbirth, emotional anchor |
| 8 | character | Erik Douglas | Patriarch, CEO, black hair/amber eyes, Douglas not Bloodmoon |
| 9 | character | Malachia Douglas-Bloodmoon | Eldest, Douglas appearance, stoic protector |
| 10 | character | Noah Douglas-Bloodmoon | Second, Bloodmoon appearance, legal mind |
| 11 | character | Jasper Douglas-Bloodmoon | Twin, fusion appearance (caramel/mint green), rebellious DJ |
| 12 | character | Alyssa Douglas-Bloodmoon | Twin, fusion appearance, resembles Nixara, protected core |
| 5 | rule | Character Authority | Summary of all character roles |
| 6 | rule | Visual Authority | Summary of all visual inheritance rules |

### From W_Contemporary.js (14 entries)

| UID | Trigger/Keywords | Content |
|---|---|---|
| WC_001 | los angeles, la, estate, beverly hills, dcc | LA dimension container |
| WC_002 | douglas estate, villa | Estate layout and locations |
| WC_003 | dcc, douglas commerce, board, corporate | DCC corporate domain |
| WC_004 | verve, sarah, roxy, mae | The Verve bar and staff |
| WC_005 | panic, spike, breach, tracker, watch | Security escalation protocol |
| WC_006 | bloodmoon, lineage, family rank, heir | Bloodmoon lineage trigger |
| WC_007 | lineage context + security context | Lineage information |
| WC_008 | corporate intrigue, boardroom, hostile takeover | Corporate intrigue |
| WC_009 | intrigue, negotiation, merger, espionage | Intrigue style injector |
| WC_010 | mercenary, rogue, transponder, harassment | Rogue mercenary pressure |
| WC_011 | angel, angel moreno, angel&co | NPC Angel Moreno |
| WC_012 | malachia, noah, jasper, logan, erik, wulfnic, brothers | Multi-presence protocol |
| WC_013 | sierra, sisi, stylist, pink hair | NPC Sierra (SiSi) |
| WC_014 | bracket, boob bracket, bruins, ucla | UCLA Bruins Boob Bracket event |

---

## 6. Detected Script References

### Engine Scripts

| Script | Layer | Purpose |
|---|---|---|
| En_Core.js | En_ (Engine) | World routing, POV override, lorebook compilation, runtime state, output formatting, vitals, atmosphere, diegetic UI, media/social engine |
| Ex_LosAngeles.js | Ex_ (Experience) | POV override (C_Alyssa), experience-specific lorebook pipeline |
| W_Contemporary.js | W_ (World) | LA world lorebook with 14 triggerable entries |

### Character Scripts

| Script | Layer | Purpose |
|---|---|---|
| C_Erik.js | C_ (Character) | World-aware character micro-engine (modern/pack/cyber/jarn/fantasy) |
| C_Jasper.js | C_ (Character) | World-aware character micro-engine |
| C_Logan.js | C_ (Character) | Character micro-engine |
| C_Malachia.js | C_ (Character) | Character micro-engine |
| C_Noah.js | C_ (Character) | Character micro-engine |
| C_Wulfnic.js | C_ (Character) | Character micro-engine |

### Behavior Scripts

| Script | Layer | Purpose |
|---|---|---|
| relationship_engine.js | B1 (Behavior) | Trust state (0-100), relationship state machine, attraction/familiarity modifiers |
| state_engine.js | B1 (Behavior) | Emotion state, scenario state, pack/combat/role state |

---

## 7. Validation Summary

### Import Package Completeness

| Component | Status | Notes |
|---|---|---|
| Metadata | COMPLETE | Title, chat name, character ID, visibility, tags, creator, soundtrack |
| Description | COMPLETE | Full HTML-formatted description with images, roleplay dynamics, warnings, world/lore, protagonists, scenarios, boundaries, creator notes, AI guidance |
| Personality | COMPLETE | Group definition + 6 individual character definitions (Malachia, Noah, Jasper, Wulfnic, Erik, Logan) |
| Scenario | COMPLETE | Narrative directives, world invariants, lore invariants, context invariants, session dynamics, trigger contract, user contract |
| First Message | COMPLETE | 5 intro variants (Sunday Lunch, Sneak Out, Breakfast Date, Ice Cream at Mall, Custom OOC) |
| Example Dialogues | COMPLETE | 18 dialogue examples across all 6 NPCs |
| Lorebook Entries | COMPLETE | 12 JanitorAI-format entries (Family Authority, Visual Inheritance, dynasties, character profiles, Character Authority, Visual Authority) |
| Images | COMPLETE | Primary avatar + 3 additional assets referenced |
| Advanced Prompt | COMPLETE | Engine parameter overrides (language, NSFW gate, dark themes, prose style) + plugin tags |
| Technical Metadata | COMPLETE | Token counts (4587 total, 2335 permanent), bot link |

### Missing Components

| Component | Status | Notes |
|---|---|---|
| Separate lorebook file | NOT PRESENT | Lorebook is embedded in original_export.json only; no standalone .json lorebook file |
| Individual character export files | NOT PRESENT | No separate per-character export files; all character data consolidated in export |
| Script files in export | NOT PRESENT | Export contains no .js files; scripts exist only in source repository |
| World file in export | NOT PRESENT | No standalone world export file; world data consolidated in export |

---

## 8. Source File Cross-Reference

The following source files in `d:\Progetti\database\` are the canonical repository counterparts to this legacy export:

| Export Content | Repository Source | Match Status |
|---|---|---|
| Description HTML | Ex_LosAngeles.md (lines 67-378) | IDENTICAL content |
| Personality block | Ex_LosAngeles.md (lines 434-580) | IDENTICAL content |
| Scenario block | Ex_LosAngeles.md (lines 382-431) | IDENTICAL content |
| Initial messages | Ex_LosAngeles.md (lines 584-651) | IDENTICAL content (3 intros in MD vs 5 in export) |
| Example dialogues | Ex_LosAngeles.md (lines 655-751) | IDENTICAL content |
| Lorebook entries (JSON) | original_export.json | STANDALONE — not replicated in source repo |
| Engine logic | En_Core.js | Source repository version |
| Character profiles | C_*.md / C_*.js | Source repository versions (extended, world-aware) |
| World data | W_Contemporary.md / .js | Source repository versions |
| Behavior engines | relationship_engine.js, state_engine.js | Source repository versions |

---

*Generated by Phase 15.1 — Legacy Bot Import & Repository Registration*
*Analysis only — no content modified*

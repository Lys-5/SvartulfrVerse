#!/usr/bin/env python3
"""
Svartúlfr Verse — Asset Reference & Neutral Card Pipeline (Shared Real-Height Grid).

Shared Floor & Scale Grid for 1696x2528 RGBA Neutral Sprites:
  FLOOR_Y   = 2500 px  (28 px above bottom edge)
  PX_PER_CM = 9.75 px/cm (measured from sole to cranial crown/hair top; wolf ears protrude freely above)

Subcommands:
  init-manifest      Build/refresh scratch/asset_reference_manifest.json.
  probe-keys         Test Google AI Studio & AQ.* Vertex Express keys in memory (no key leakage).
  gen-api            Generate a target reference (16:9) or neutral (2:3) image via Google API.
  prep-front-anchors Extract clean 2:3 VISTA FRONTALE crops on #FFFFFF scaled to real height grid.
  finalize-reference Resize & convert a 16:9 reference sheet to (2730, 1536) RGB PNG.
  finalize-neutral   Flood-fill BFS white-bg removal -> (1696, 2528) RGBA PNG on shared height grid.
  finalize-avatar    Resize & convert a 2:3 half-body urban default avatar to (1696, 2528) RGB PNG.
  build-audit-sheet  Build high-res visual audit contact sheet (checkerboard for RGBA neutrals).
  build-height-chart Build graduated 0-250 cm height comparison chart from front_anchors or neutrals.
"""

from __future__ import annotations

import argparse
import base64
import collections
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)

ROOT = pathlib.Path(r"E:\repository\SvartulfrVerse")
ASSETS_DIR = ROOT / "assets"
MANIFEST_PATH = ROOT / "scratch" / "asset_reference_manifest.json"
ART_DIR = pathlib.Path(r"C:\Users\mande\.gemini\antigravity\brain\713be534-6fb6-4fa8-bd35-5129adcc8c16")
REFS_DIR = ART_DIR / "refs"

REF_SIZE = (2730, 1536)
NEUTRAL_SIZE = (1696, 2528)
FLOOR_Y = 2500
PX_PER_CM = 9.75

GEMINI_IMAGE_MODELS = [
    "gemini-3-pro-image",
    "gemini-3-pro-image-preview",
    "gemini-3.1-flash-image",
    "gemini-3.1-flash-image-preview",
    "gemini-3.1-flash-lite-image",
    "gemini-2.5-flash-image",
]

REGEN_QUEUED_DEFAULTS = {
    ("alyssa", "neutral"),
    ("malachia", "neutral"),
    ("noah", "neutral"),
    ("erik", "neutral"),
    ("logan", "neutral"),
    ("edric", "neutral"),
    ("wulfnic", "reference"),
    ("wulfnic", "neutral"),
    ("ut", "reference"),
    ("kaladin", "reference"),
}

HYBRID_REF_TEMPLATE = """\
Professional 16:9 widescreen creature/hybrid-form character reference sheet and turnaround model sheet of {identity}, rendered in a cohesive semi-realistic digital painting style with refined clean dark ink linework, detailed anatomical musculature, textured fur/scales, and expressive eyes.

BACKGROUND & LIGHTING:
Flat, solid, completely uniform neutral light-grey studio background (#C8C8C8) with no gradients, no floor shadows, and no environment. Even, soft neutral studio lighting that clearly displays bipedal digitigrade posture, claws, fangs, musculature, and surface markings.

LAYOUT (LEFT TO RIGHT):
1. Left — Full-body front view of the monstrous bipedal Hybrid Shift form labeled "VISTA FRONTALE" at the top in clean bold dark sans-serif uppercase font. Powerful standing combat-ready studio stance.
2. Center-left — Full-body 3/4 view (turned approx. 45 degrees) labeled "VISTA A 45° / TRE QUARTI" at the top, showing massive torso volume, scars/runes through the coat, and {tail_attach}.
3. Center-right — Full-body side profile view (facing left) labeled "VISTA LATERALE" at the top, clearly showing bipedal digitigrade hind legs, forward hunched/predatory posture, muzzle profile, and {tail_attach}.
4. Right (Top) — Large high-detail head-and-shoulders close-up portrait facing forward labeled "DETTAGLIO VOLTO" at the top, highlighting transformed fangs, snout/visage, glowing eyes, and {ear_summary}.
5. Right (Bottom) — Section titled "DETTAGLI ANATOMICI:" with subtitle "{subtitle}", above three aligned square close-up inset boxes with thin dark borders and centered uppercase captions underneath each box:
   - Box 1: {box1_desc} — caption: "{box1_cap}"
   - Box 2: {box2_desc} — caption: "{box2_cap}"
   - Box 3: {box3_desc} — caption: "{box3_cap}"

HYBRID FORM SPECS:
- Stature & Build: {build}
- Head & Eyes: {face}
- Fur / Scales & Coat: {coat}
- Limbs & Anatomy: {anatomy}
- Attire / Remains: {outfit}
"""


def build_avatar_prompt(char_desc: str, default_outfit: str, urban_bg: str) -> str:
    return (
        "Half-body (waist-up / chest-up) character portrait avatar illustration in a 2:3 vertical frame, "
        "using the attached character reference sheet strictly 1:1 for exact facial structure, scar placement, eye color, "
        "hairstyle, single species ear placement on top of the head (ZERO human ears on the sides for demi-humans/shifters), and semi-realistic digital painting style with clean linework. "
        f"CHARACTER: {char_desc} "
        f"DEFAULT OUTFIT: {default_outfit} "
        f"URBAN BACKGROUND: {urban_bg} Shallow depth-of-field cinematic bokeh, natural atmospheric lighting, zero text, zero watermarks, zero borders."
    )

MASTER_REF_TEMPLATE = """\
Professional 16:9 widescreen character reference sheet and turnaround model sheet of {identity}, rendered in a cohesive semi-realistic digital painting style with refined clean linework, rich painterly shading, detailed hair and fur texture, and warm natural skin tones.

BACKGROUND & LIGHTING:
Flat, solid, completely uniform neutral light-grey studio background (#C8C8C8) with no gradients, no floor shadows, and no environment. Even, soft neutral studio lighting that clearly shows anatomy, skin texture, scars, and ink.

LAYOUT (LEFT TO RIGHT):
1. Left — Full-body front view labeled "VISTA FRONTALE" at the top in clean bold dark sans-serif uppercase font. Relaxed standing studio pose, barefoot.
2. Center-left — Full-body 3/4 view (turned approx. 45 degrees) labeled "VISTA A 45° / TRE QUARTI" at the top, showing body volume, tattoos/marks, and tail attachment.
3. Center-right — Full-body side profile view (facing left) labeled "VISTA LATERALE" at the top, clearly showing posture, torso depth, hair silhouette, and {tail_attach}.
4. Right (Top) — Large high-detail head-and-shoulders close-up portrait facing forward labeled "DETTAGLIO VOLTO" at the top, highlighting facial structure, eye color, expression, skin details, and {ear_summary}.
5. Right (Bottom) — Section titled "TATUAGGI & SEGNI:" with subtitle "{subtitle}", above three aligned square close-up inset boxes with thin dark borders and centered uppercase captions underneath each box:
   - Box 1: {box1_desc} — caption: "{box1_cap}"
   - Box 2: {box2_desc} — caption: "{box2_cap}"
   - Box 3: {box3_desc} — caption: "{box3_cap}"

CHARACTER SPECS:
- Build & Proportions: {build}
- Face & Eyes: {face}
- Hair: {hair}
- Anatomy: {anatomy}
- Outfit: {outfit}
- Marks & Details: {marks}
"""


def build_neutral_prompt(
    char_desc: str,
    outfit_desc: str,
    height_cm: int,
    head_ratio_note: str,
    extra_notes: str = "",
) -> str:
    return (
        f"Full-body standing character sprite illustration in a 2:3 vertical frame ({height_cm} cm tall, {head_ratio_note}), "
        "using ONLY the attached 2:3 front-view body template as the exact 1:1 anatomical blueprint (face, head-to-body ratio, "
        "shoulder width, narrow/athletic waist, hip/crotch height, leg length, ear placement, tail, marks, and semi-realistic digital painting "
        "style with refined clean dark ink linework). "
        "Dress THIS exact standing front-view body 1:1 without altering head size, shoulder width, waist narrowness, hip/crotch height, "
        "or leg length; keep natural high-to-normal waistlines and long anatomical legs (strictly NO dropped-crotch pants, NO shortened legs, "
        "NO enlarged head, NO squashed torso). "
        "Keep the exact vertical height scale and bottom sole position from the attached 2:3 template so the full body from ear tips down to complete shoes fits cleanly inside the frame. "
        "BACKGROUND: Completely flat, solid pure white background (#FFFFFF) with ZERO gradients, ZERO floor shadow, ZERO ground line, "
        "ZERO text, ZERO labels, ZERO borders, and ZERO environment. Clean closed dark ink outer silhouette outline around the entire figure and outfit. "
        f"CHARACTER: {char_desc} "
        f"OUTFIT: {outfit_desc} "
        f"{extra_notes}".strip()
    )


def get_manifest_entries(existing_items: dict[str, dict] | None = None, seed_regen: bool = False) -> list[dict]:
    """Canonical registry of Wave 1 (Pack), Wave 2 (Standalone NPCs), and Wave 3 (Variants)."""
    entries: list[dict] = []
    existing_items = existing_items or {}

    def resolve_status(eid: str, kind: str, path: str | None) -> str:
        if not path:
            return "N/A"
        prev = existing_items.get(eid, {}).get(f"{kind}_status")
        if not seed_regen and prev == "REGEN_QUEUED":
            return "REGEN_QUEUED"
        if seed_regen and (eid, kind) in REGEN_QUEUED_DEFAULTS:
            return "REGEN_QUEUED"
        return "DONE" if pathlib.Path(path).exists() else "PENDING"

    def add(
        eid: str,
        wave: str,
        folder: str,
        height_cm: int,
        has_ears_above_crown: bool,
        ref_file: str | None,
        neutral_file: str | None = None,
        ref_prompt: str | None = None,
        neutral_prompt: str | None = None,
        ref_anchors: list[str] | None = None,
        neutral_anchors: list[str] | None = None,
        asset_kind: str = "character",
    ) -> None:
        ref_path = str(ASSETS_DIR / folder / ref_file) if ref_file else None
        neu_path = str(ASSETS_DIR / folder / neutral_file) if neutral_file else None
        entries.append(
            {
                "id": eid,
                "wave": wave,
                "folder": folder,
                "asset_kind": asset_kind,
                "height_cm": height_cm,
                "has_ears_above_crown": has_ears_above_crown,
                "reference_path": ref_path,
                "neutral_path": neu_path,
                "reference_status": resolve_status(eid, "reference", ref_path),
                "neutral_status": resolve_status(eid, "neutral", neu_path),
                "reference_prompt": ref_prompt,
                "neutral_prompt": neutral_prompt,
                "reference_anchors": ref_anchors or [],
                "neutral_anchors": neutral_anchors or [],
            }
        )

    # === WAVE 1A: 8 existing Pack members ===
    add("jasper", "1A", "Jasper", 193, True, "jasper_reference.png", "jasper_neutral.png")

    add(
        "alyssa",
        "1A",
        "Alyssa",
        155,
        True,
        "alyssa_reference.png",
        "alyssa_neutral.png",
        neutral_anchors=["alyssa_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Alyssa Hvit Douglas Bloodmoon, 19-year-old petite 155 cm female werewolf with a pronounced hourglass frame (full DD-cup bust, very narrow cinched waist, wide curved hips, long shapely legs), "
            "long wavy caramel-chestnut brown hair cascading past her shoulders, vivid mint-green doe eyes, soft freckles across her nose and cheeks, gentle warm smile, "
            "single pair of caramel-brown wolf ears with dark tips atop her head (no human ears on the sides), fluffy caramel-brown wolf tail with a black tip emerging behind her legs, "
            "tiny flat black Mannaz rune tattoo on her inner left wrist, and a delicate navel piercing.",
            "Sunny California casual outfit: fitted sunflower-yellow ruffled crop top with ruffled shoulder straps (keeping her narrow bare midriff and navel piercing clearly visible), "
            "high-waisted light-blue distressed denim shorts sitting at her natural waist with frayed hems and a tailored rear tail opening, thin gold chain necklace with a small sunflower pendant, "
            "and crisp white canvas low-top sneakers (clean dark ink outer outline around the white sneakers).",
            155,
            "~6.8-head petite hourglass proportions",
        ),
    )

    add(
        "malachia",
        "1A",
        "Malachia",
        208,
        True,
        "malachia_reference.png",
        "malachia_neutral.png",
        ref_anchors=["malachia_old_reference.png", "malachia_anchor.jpg"],
        ref_prompt=MASTER_REF_TEMPLATE.format(
            identity="Malachia Bjorn Douglas Bloodmoon, 28-year-old colossal 208 cm heavyweight-boxer Werewolf",
            tail_attach="thick dense black wolf tail emerging from the lower spine",
            ear_summary="single pair of large sharp charcoal-black wolf ears blending into thick spiky swept-back hair",
            subtitle="THURISAZ & FENRIS • WOLF FOREHEAD INK • BROW-CHEEK X-SCAR",
            box1_desc="Macro close-up of inner left wrist showing the dark Thurisaz & Fenris rune brand inked cleanly over rich tanned bronze skin",
            box1_cap="THURISAZ & FENRIS RUNE",
            box2_desc="Macro close-up of massive tanned forearm covered in Norse-tribal Bloodmoon blackwork featuring a roaring wolf head motif",
            box2_cap="WOLF HEAD & BLOODMOON INK",
            box3_desc="Macro close-up of face matching malachia_anchor.jpg showing the vertical scar cutting through the left eyebrow down to an X-shaped left cheek scar and pale amber-grey eyes",
            box3_cap="BROW-TO-CHEEK X-SCAR",
            build="Colossal 208 cm (6'10\") massive heavyweight-boxer frame with huge towering trapezius muscles, ultra-thick bull neck, cavernous broad shoulders, vascular muscular forearms, and rich deep sun-kissed Southern California bronze/olive-tan skin matching malachia_anchor.jpg (strictly tanned warm bronze, NOT pale).",
            face="Match malachia_anchor.jpg 1:1 in facial bone structure, scars, facial hair, and eye color across ALL 4 views: heavy chiseled squared jawline with a full trimmed dark goatee, connected mustache, and dark jawline stubble, heavy furrowed brow, intense piercing cold pale amber-grey eyes, diagonal scar across nasal bridge, and a prominent vertical scar cutting down through his left eyebrow onto his left cheek intersected by a crisp X-cut scar.",
            hair="Shorter thick spiky swept-back jet-black wolf-mane hair pulled cleanly up and back off the forehead matching malachia_anchor.jpg, blending seamlessly into the sides around the wolf ears.",
            anatomy="CRITICAL: Keep the 4-column studio turnaround composition of malachia_old_reference.png updated 1:1 with the face, skin tone, spiky swept-back shorter hair, beard goatee, and left brow-cheek scars of malachia_anchor.jpg. Single pair of large sharp dark wolf ears atop the head, thick black wolf tail. STRICTLY NO HUMAN EARS on the sides of the head.",
            outfit="Minimalist matte black photography-studio underwear (fitted black boxer briefs), barefoot.",
            marks="Extensive heavy Norse-tribal Bloodmoon blackwork tattoos climbing the neck and covering both forearms (including a distinct snarling wolf head motif on the left forearm); vertical pale combat scars on right upper arm; dark Thurisaz & Fenris rune on inner left wrist.",
        ),
        neutral_anchors=["malachia_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Malachia Bjorn Douglas Bloodmoon, 28-year-old colossal 208 cm male werewolf with a massive bulky heavyweight-boxer build, towering trapezius muscles, ultra-thick neck, very broad heavy shoulders, long powerful legs, "
            "rich deep sun-kissed bronze/olive-tan Southern California skin tone matching malachia_anchor.jpg — strictly warm deep tanned bronze skin, NOT pale, NOT grey, "
            "shorter thick spiky swept-back jet-black hair matching malachia_anchor.jpg blending seamlessly into a single pair of large sharp charcoal-black wolf ears atop his head (no human ears), "
            "heavy sculpted squared jawline with a full trimmed dark goatee, connected mustache, and jawline stubble, cold piercing pale amber-grey eyes, vertical scar across his left eyebrow down into an X-shaped left cheek scar and slight nasal scar, "
            "extensive dark Norse-tribal Bloodmoon blackwork tattoos climbing his neck and both massive forearms (featuring the snarling wolf head on his left forearm), vertical upper-arm scars, dark Thurisaz & Fenris rune brand on his inner left wrist, "
            "and a thick dark black bushy wolf tail behind his legs.",
            "Athletic combat-casual streetwear: tight short-sleeved matte-black compression t-shirt stretched across his massive chest and traps (tucked cleanly at natural waist height to preserve leg length and expose tattooed forearms), "
            "fitted dark charcoal-grey athletic cargo sweatpants sitting at natural hip/waist height with straight tailored legs (NO dropped crotch) and a rear tail opening, "
            "white athletic boxing hand wraps around his knuckles/hands (leaving the inner left wrist rune and forearm wolf ink visible), and sturdy black high-top athletic combat sneakers.",
            208,
            "~8.5-head imposing gladiator proportions",
        ),
    )

    add(
        "noah",
        "1A",
        "Noah",
        197,
        True,
        "noah_reference.png",
        "noah_neutral.png",
        neutral_anchors=["noah_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Noah Loki Douglas Bloodmoon, 25-year-old tall 197 cm male werewolf with a lean athletic tanned swimmer/frat-bro physique and long proportionate legs, "
            "neatly styled blond hair with dark tortoiseshell designer sunglasses pushed up into his hair, bright clear blue eyes, subtle nose freckles, confident charming half-smirk, "
            "single pair of blond/cream alert wolf ears atop his head (no human ears), fluffy golden-blond wolf tail behind his legs, and a dark Gebo rune tattoo (X) on his inner left wrist.",
            "Upscale Southern California preppy casual wear: tailored ice-white pique cotton short-sleeve polo shirt (with clean dark ink outer contour lines against the white background) unbuttoned at the top two pearl buttons, "
            "tucked cleanly into high-to-natural-rise tailored sand-beige chino trousers with a rear tail opening, luxury silver wristwatch on his left wrist above the Gebo rune, and crisp white-and-tan leather loafers.",
            197,
            "~8.0-head tall athletic proportions",
        ),
    )

    add(
        "erik",
        "1A",
        "Erik",
        213,
        True,
        "erik_reference.png",
        "erik_neutral.png",
        neutral_anchors=["erik_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Erik Ulfr Douglas, 55-year-old imposing 213 cm Prime Alpha werewolf patriarch with mountainous disciplined ex-athlete musculature, broad shoulders, tapered waist, and long commanding legs, "
            "jet-black hair with distinguished silver touches at the temples, severe squared jawline with trimmed dark stubble, piercing amber eyes, "
            "faint clean diagonal ritual scar on his left cheekbone, single pair of black wolf ears atop his head (no human ears), bushy black wolf tail behind his legs, "
            "Hagalaz rune tattoo on his inner left wrist, and a platinum-and-obsidian Douglas Clan signet ring on his left hand.",
            "Refined luxury patriarch smart-casual attire: tailored dark charcoal-grey Italian heavy linen dress shirt unbuttoned at the top two collar buttons (subtle gold chain glimpsed at collarbone) "
            "with sleeves neatly rolled twice to mid-forearm (showing his wrist rune), tucked cleanly into natural-waist tailored black trousers with a black leather belt and rear tail opening, "
            "and polished black leather Italian loafers.",
            213,
            "~8.5-head commanding patriarch proportions",
        ),
    )

    add(
        "logan",
        "1A",
        "Logan",
        198,
        True,
        "logan_reference.png",
        "logan_neutral.png",
        neutral_anchors=["logan_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Logan Jarn Douglas, 49-year-old rugged 198 cm male werewolf with a fit muscular biker/mechanic build and long proportionate legs, "
            "disheveled black hair greying at the temples pulled back into a low messy ponytail, observant amber eyes, weathered handsome face with salt-and-pepper beard stubble, "
            "single pair of black-and-grey wolf ears atop his head (no human ears), heavy Norse/Celtic full-sleeve tattoos on both forearms crisscrossed by faint pale hunt scars, "
            "dark Eihwaz rune brand on his inner left wrist, and a bushy dark grey-black wolf tail behind his legs.",
            "Rugged mechanic biker attire: cropped waist-length worn matte-black leather biker jacket worn open with sleeves pushed up to mid-forearm (showing tattooed forearms and wrist rune) over a tucked dark slate-grey henley shirt, "
            "natural-rise fitted worn black denim jeans with leather belt and rear tail opening (keeping natural crotch height and full leg length), and heavy scuffed black leather biker boots.",
            198,
            "~8.0-head tall rugged biker proportions",
        ),
    )

    add(
        "edric",
        "1A",
        "Edric",
        165,
        True,
        "edric_reference.png",
        "edric_neutral.png",
        neutral_anchors=["edric_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Edric Douglas, 13-year-old tall broad-boned tween werewolf boy (165 cm, strictly SFW, youthful smooth skin, thick wrists of a future Alpha), "
            "thick messy black hair falling slightly over his eyes, intense amber eyes, light freckles and thin healed scars on his cheeks, tense guarded expression, "
            "single pair of black wolf ears atop his head (no human ears), youthful bushy black wolf tail behind his legs, and a dark Sowilo rune tattoo on his inner left wrist.",
            "Casual tween streetwear mimicking his father Logan: hip-length battered black leather jacket worn open over a dark navy-blue pullover hoodie with white drawstrings (hem resting at hip bone, NOT knee-length), "
            "natural-rise faded blue straight-leg jeans scuffed at the knees with a rear tail opening, and worn black-and-white skate sneakers.",
            165,
            "~6.8-head 13-year-old tween proportions",
        ),
    )

    add(
        "wulfnic",
        "1A",
        "Wulfnic",
        220,
        True,
        "wulfnic_reference.png",
        "wulfnic_neutral.png",
        ref_anchors=["wulfnic_old_reference.png"],
        ref_prompt=MASTER_REF_TEMPLATE.format(
            identity="Wulfnic Baleygr Bloodmoon (The Wolf King), 1200-year-old Primordial Firstborn Werewolf appearing as a battle-worn 40-year-old Norse Jarl",
            tail_attach="bushy golden-blonde-and-snow-white wolf tail emerging from the lower spine",
            ear_summary="single pair of large golden-blonde wolf ears streaked with snow-white",
            subtitle="JERA & FENRIS • SVARTÚLFR INK • WARRIOR BRAID",
            box1_desc="Macro close-up of inner left wrist showing the dark Jera & Fenris geometric rune brand matching wulfnic_old_reference.png",
            box1_cap="JERA & FENRIS RUNE (LEFT WRIST)",
            box2_desc="Macro close-up of weathered scarred pectoral and left upper-arm bicep showing the intricate Svartulfr Norse tattoos and jagged battle scars from wulfnic_old_reference.png",
            box2_cap="SVARTÚLFR TATTOOS & SCARS",
            box3_desc="Macro close-up of golden-blonde hair streaked with snow-white woven into his signature braided warrior lock secured with a bronze-leather wrap",
            box3_cap="WARRIOR HAIR BRAID",
            build="220 cm (7' 2.6\") colossal heavily muscled and battle-scarred Norse warrior-demigod frame (stopped aging at 40 when Fenris consecrated him — rugged athletic battle-worn 40-year-old powerhouse, NOT an elderly 60-year-old man).",
            face="Strong rugged weathered face of a battle-hardened 40-year-old Viking warrior (subtle crow's feet and battle scars across brow and nose, crisp sharp jawline, NOT wrinkled or elderly), piercing ice-blue eyes, full groomed golden-blonde Viking beard and mustache streaked with snow-white matching his hair.",
            hair="Long golden-blonde Viking hair distinctly streaked with snow-white strands, including his thick braided warrior lock draping over his left shoulder, swept cleanly past the temples.",
            anatomy="CRITICAL: Keep the exact 4-column studio turnaround composition and pose of wulfnic_old_reference.png while updating hair, beard, wolf ears, wolf tail, and facial age to battle-worn 40-year-old golden-blonde streaked with snow-white. Single pair of large golden-blonde-and-white wolf ears atop his head, bushy golden-blonde-and-white wolf tail. STRICTLY NO HUMAN EARS on the sides of the head.",
            outfit="Minimalist matte black photography-studio underwear (fitted black boxer briefs), barefoot.",
            marks="Dark Jera + Fenris geometric rune on inner left wrist; Svartulfr circular shoulder emblem, geometric arm band, and forearm ink; authentic Viking axe/claw scars across chest, arms, legs, and face.",
        ),
        neutral_anchors=["wulfnic_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Wulfnic Baleygr Bloodmoon, 1200-year-old Primordial Firstborn werewolf appearing as a colossal 220 cm battle-worn 40-year-old Viking warrior (stopped aging at 40, rugged NOT elderly) with tall imposing long-legged heroic stature, "
            "long golden-blonde hair streaked with snow-white and a thick braided warrior lock draping over his left shoulder, full golden-blonde Viking beard and mustache streaked with snow-white, piercing ice-blue eyes, "
            "weathered battle scars across his brow and nose, single pair of large golden-blonde wolf ears streaked with snow-white atop his head (no human ears), "
            "ancient Svartulfr Norse tattoos on his forearms, dark Jera & Fenris rune on his inner left wrist, and a majestic bushy golden-blonde-and-snow-white wolf tail behind his legs.",
            "Ancient Norse Jarl sanctuary attire: dark charcoal-and-earth handwoven wool Viking tunic belted tightly at his natural waist (reaching upper-mid thigh only so his long powerful legs remain clearly visible) "
            "with V-neck fastened by a wrought-iron brooch (leather cord with wolf tooth at throat) and sleeves rolled to mid-forearm, heavy dark wolf-pelt fur mantle draped across his broad shoulders (never hiding his neck length), "
            "woven fabric waist sash with leather belt, straight dark earth-grey wool Norse trousers with leg wraps, rear tail opening, and sturdy weathered leather Viking boots.",
            220,
            "~8.5-head colossal Viking demigod proportions",
        ),
    )

    # === WAVE 1B: 7 additional Pack members ===
    add(
        "magnus",
        "1B",
        "Magnus",
        205,
        True,
        "magnus_reference.png",
        "magnus_neutral.png",
        ref_anchors=["erik_reference.png"],
        ref_prompt=MASTER_REF_TEMPLATE.format(
            identity="Sir Magnus Douglas III, 355-year-old aristocratic Pureblood Werewolf Patriarch appearing late 50s",
            tail_attach="dark charcoal-grey wolf tail emerging from the lower spine",
            ear_summary="single pair of dark charcoal-grey wolf ears",
            subtitle="OTHALA RUNE • DOUGLAS SIGNET • COLONIAL SCAR",
            box1_desc="Macro close-up of inner left wrist showing the Othala (ᛟ) ancestral heritage rune in cold-iron dark ink",
            box1_cap="OTHALA RUNE (LEFT WRIST)",
            box2_desc="Macro close-up of left hand wearing an antique gold-and-onyx House Douglas colonial signet ring",
            box2_cap="DOUGLAS SIGNET RING",
            box3_desc="Macro close-up of jawline and collarbone showing an old faded colonial sabre duel scar",
            box3_cap="COLONIAL SABRE SCAR",
            build="Tall 205 cm aristocratic upright powerhouse build, distinguished mature proportions, light chest and leg hair.",
            face="Composed noble features, calm level amber eyes, neatly trimmed silver-threaded beard and mustache, unhurried authoritative expression.",
            hair="Douglas black hair neatly combed back from forehead, heavily silvered at the temples.",
            anatomy="Single pair of dark charcoal-grey wolf ears positioned naturally on top of the head, and a bushy dark grey wolf tail. STRICTLY NO HUMAN EARS on the sides of the head; hair neatly frames the temples.",
            outfit="Minimalist matte black photography-studio underwear (fitted black boxer briefs), barefoot.",
            marks="Othala (ᛟ) rune in cold-iron dark ink on the inner left wrist; antique gold-and-onyx Douglas signet ring on left hand; old faded sabre scar near left collarbone.",
        ),
        neutral_anchors=["magnus_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Sir Magnus Douglas III, 205 cm distinguished aristocratic werewolf patriarch appearing late 50s, neatly combed-back black hair silvered at the temples, "
            "level amber eyes, trimmed silver-threaded beard, single pair of dark charcoal-grey wolf ears atop his head (no human ears), bushy dark grey wolf tail behind his legs, "
            "Othala rune on inner left wrist, and antique House Douglas signet ring on left hand.",
            "Impeccable old-money English bespoke three-piece tailored slate-grey pinstriped wool suit with two-button jacket, five-button waistcoat, crisp white dress shirt, "
            "deep burgundy silk tie, silver pocket watch chain, rear tail opening, and polished oxblood-black leather oxford shoes.",
            205,
            "~8.4-head tall aristocratic proportions",
        ),
    )

    add(
        "elizabeth",
        "1B",
        "Elizabeth",
        165,
        True,
        "elizabeth_reference.png",
        "elizabeth_neutral.png",
        ref_anchors=["alyssa_reference.png", "elizabeth_anchor.jpg"],
        ref_prompt=MASTER_REF_TEMPLATE.format(
            identity="Lady Elizabeth Duskwood, Pureblood Werewolf Pack Matriarch of House Duskwood-Douglas",
            tail_attach="ash-grey wolf tail emerging from the lower spine",
            ear_summary="single pair of ash-grey wolf ears",
            subtitle="URUZ RUNE • DUSKWOOD RINGS • PEARL NECKLACE",
            box1_desc="Macro close-up of inner left wrist showing the Uruz (ᚢ) primal endurance rune in cold-iron dark ink",
            box1_cap="URUZ RUNE (LEFT WRIST)",
            box2_desc="Macro close-up of graceful slender hand wearing antique silver Duskwood signet rings",
            box2_cap="DUSKWOOD SILVER RINGS",
            box3_desc="Macro close-up of slender collarbone and neck wearing a classic luminous white pearl necklace",
            box3_cap="PEARL NECKLACE",
            build="165 cm graceful, timeless mature feminine build (appears 40s despite age 76), poised aristocratic posture, smooth luminous fair skin.",
            face="Refined classic beauty matching the face reference, calm perceptive storm-grey eyes, warm serene subtle smile, zero wrinkles of decrepitude.",
            hair="Luminous ash-grey hair worn in a soft elegant updo with loose tendrils framing her face and temples.",
            anatomy="Single pair of ash-grey wolf ears positioned naturally on top of the head, and a fluffy pearl-grey wolf tail. STRICTLY NO HUMAN EARS on the sides of the head; wavy ash-grey tendrils cover the sides.",
            outfit="Minimalist matte black photography-studio underwear (strapless black bandeau top and minimal black briefs), barefoot.",
            marks="Uruz (ᚢ) rune in cold-iron dark ink on the inner left wrist; silver Duskwood rings on fingers; pearl necklace.",
        ),
        neutral_anchors=["elizabeth_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Lady Elizabeth Duskwood, 165 cm poised graceful werewolf matriarch appearing early-to-mid 40s, luminous ash-grey hair styled in an elegant soft updo with loose side tendrils, "
            "storm-grey perceptive eyes, warm serene smile, single pair of ash-grey wolf ears atop her head (no human ears), fluffy pearl-grey wolf tail behind her dress, "
            "and antique silver rings on her fingers.",
            "Refined Pack Matriarch attire: long flowing dark forest-green fine cashmere A-line dress with soft boat neckline and three-quarter sleeves, "
            "a soft sand-beige wool wrap stole draped gracefully over her shoulders, classic white pearl collar necklace, rear tail opening, and low elegant dark leather court flats.",
            165,
            "~7.2-head graceful feminine proportions",
        ),
    )

    add(
        "ut",
        "1B",
        "Ut",
        240,
        True,
        "ut_reference.png",
        "ut_neutral.png",
        ref_anchors=["wulfnic_reference.png"],
        ref_prompt=MASTER_REF_TEMPLATE.format(
            identity="Ut Berg (The Mountain), 1205-year-old Primordial Firstborn Werewolf Berserker appearing as a battle-worn mid-40s Viking giant",
            tail_attach="heavy reddish-auburn wolf tail streaked with iron-grey emerging from the lower spine",
            ear_summary="single pair of reddish-auburn wolf ears streaked with iron-grey",
            subtitle="LAGUZ & FENRIS • IRON ARM RINGS • BATTLE SCARS",
            box1_desc="Macro thick inner left wrist showing the Laguz (ᛚ) and Fenris rune tattoo in dark cold-iron ink",
            box1_cap="LAGUZ & FENRIS RUNE",
            box2_desc="Macro massive forearm wearing heavy hammered dark iron Viking arm rings",
            box2_cap="FORGED IRON ARM RINGS",
            box3_desc="Macro rugged weathered torso crisscrossed by thick jagged axe and fang scars and ancient Norse ink",
            box3_cap="ANCIENT BATTLE SCARS",
            build="Colossal 240 cm barrel-chested walking mountain of granite muscle (biological aging halted at 45 when Fenris turned him — rugged battle-hardened mid-40s powerhouse, NOT an elderly 60-year-old), tree-trunk limbs, thick shoulders and forearms, coarse body hair.",
            face="Rugged battle-worn mid-40s Viking warrior features framed by a thick wild bushy REDDISH-AUBURN beard streaked with iron-grey (same exact reddish-auburn and iron-grey color as his hair) across ALL four views, heavy iron-grey eyes, gruff fearless presence.",
            hair="Wild, thick unkempt REDDISH-AUBURN hair streaked with iron-grey reaching past the collar, matching his beard color 1:1.",
            anatomy="CRITICAL: Single pair of large weathered reddish-auburn wolf ears streaked with iron-grey MUST be clearly visible atop his head in ALL FOUR views (VISTA FRONTALE, 45°, LATERALE, and DETTAGLIO VOLTO), plus a massive heavy reddish-auburn wolf tail streaked with iron-grey. STRICTLY NO HUMAN EARS on the sides of the head; zero leg tattoos.",
            outfit="Minimalist matte black photography-studio underwear (fitted black boxer briefs), barefoot.",
            marks="Laguz (ᛚ) + Fenris protection brand on inner left wrist; heavy hammered iron arm rings; archaic Norse runes and thick jagged battle scars across chest and arms ONLY (clean scarred skin on legs).",
        ),
        neutral_anchors=["ut_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Ut Berg (The Mountain), 240 cm colossal barrel-chested Primordial Firstborn werewolf giant appearing as a battle-worn 45-year-old Viking warrior (NOT elderly), homogenized wild unkempt REDDISH-AUBURN hair streaked with iron-grey, "
            "matching massive bushy REDDISH-AUBURN Viking beard streaked with iron-grey, heavy iron-grey eyes, archaic Norse tattoos and thick scars across forearms and chest, heavy iron arm rings, "
            "single pair of reddish-auburn wolf ears streaked with iron-grey atop his head (no human ears), and a thick heavy reddish-auburn-and-grey wolf tail behind his legs.",
            "Firstborn Berserker modern lumberjack garb: heavy oversized red-and-black plaid flannel shirt worn completely open over a raw earth-brown cotton tank top stretched across his granite chest, "
            "thick rough leather belt with wrought-iron buckle, heavy dark reinforced denim work jeans with rear tail opening, and massive scuffed brown leather logger boots.",
            240,
            "~8.8-head towering giant proportions",
        ),
    )

    add(
        "zefir",
        "1B",
        "Zefir",
        192,
        True,
        "zefir_reference.png",
        "zefir_neutral.png",
        ref_anchors=["erik_reference.png", "zefir_anchor.jpg"],
        ref_prompt=MASTER_REF_TEMPLATE.format(
            identity="Zefir Hvitskog (The White Ghost), 1176-year-old Primordial Firstborn Werewolf Scout appearing 20-22",
            tail_attach="sleek snow-white wolf tail emerging from the lower spine",
            ear_summary="single pair of pierced snow-white wolf ears",
            subtitle="ALGIZ & FENRIS • VIKING SLEEVE INK • PIERCED WOLF EAR",
            box1_desc="Macro close-up of pale inner left wrist showing the Algiz (ᛉ) and Fenris protection rune in sharp black ink",
            box1_cap="ALGIZ & FENRIS RUNE",
            box2_desc="Macro close-up of lean forearm covered in bold black Norse Viking runic bands and knotwork tattoos",
            box2_cap="VIKING SLEEVE TATTOOS",
            box3_desc="Macro close-up of snow-white wolf ear adorned with multiple small black metal hoop piercings along the rim",
            box3_cap="PIERCED WHITE WOLF EAR",
            build="192 cm lean, wiry, shredded acrobatic scout physique, pale porcelain skin, smooth hairless chest and torso.",
            face="Youthful sharp Viking features matching the face reference, pale icy washed-out blue eyes (almost white), wicked insolent smirk, dark smudged eyeliner shadow.",
            hair="Snow-white hair shaved close on the sides into a dramatic tousled mohawk crest falling slightly over one brow.",
            anatomy="Single pair of sleek snow-white wolf ears atop his head (the left ear pierced with small black metal hoops), and a long lush snow-white wolf tail. STRICTLY NO HUMAN EARS on the sides of the head.",
            outfit="Minimalist matte black photography-studio underwear (fitted black boxer briefs), barefoot.",
            marks="Algiz (ᛉ) + Fenris rune on inner left wrist; bold black Viking symbol tattoos covering both forearms and left arm; black metal ear piercings on white wolf ear.",
        ),
        neutral_anchors=["zefir_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Zefir Hvitskog (The White Ghost), 192 cm lean wiry shredded young-looking Primordial werewolf scout, pale porcelain skin, "
            "snow-white hair in a tousled mohawk with shaved sides, icy washed-out almost-white blue eyes, wicked insolent smirk, "
            "single pair of snow-white wolf ears atop his head with small black hoop piercings on one ear (no human ears), lush snow-white wolf tail behind his legs, "
            "and bold black Viking runic band tattoos on BOTH forearms with Algiz rune on inner left wrist.",
            "Modern punk-goth scout streetwear: sleeveless studded black leather biker vest worn open over a distressed torn black t-shirt, "
            "thin leather wrist wraps leaving forearm runes visible, ripped skinny black denim jeans with a silver wallet chain and rear tail opening, "
            "and laced black leather combat boots.",
            192,
            "~8.0-head lean agile scout proportions",
        ),
    )

    add(
        "kaladin",
        "1B",
        "Kaladin",
        191,
        True,
        "kaladin_reference.png",
        "kaladin_neutral.png",
        ref_anchors=["malachia_reference.png", "kaladin_anchor.jpg"],
        ref_prompt=MASTER_REF_TEMPLATE.format(
            identity="Major Kaladin Blackwolf Nargathon (Subject Zero), 45-year-old military-engineered Alpha Werewolf Commander",
            tail_attach="thick mutated black wolf tail emerging from the lower spine",
            ear_summary="single pair of sharp black wolf ears",
            subtitle="NEURAL CAGE SCARS • GAMMA-7 DOG TAGS • BLACKWOLF SCARS",
            box1_desc="Macro close-up of nape of neck showing faint dark cold-iron neural restraint surgical scars below the low ponytail",
            box1_cap="NEURAL CAGE SCARS (NAPE)",
            box2_desc="Macro close-up of matte-black military dog tags stamped 'GAMMA-7 / SUBJECT ZERO' resting on scarred collarbone",
            box2_cap="GAMMA-7 DOG TAGS",
            box3_desc="Macro close-up of chest and shoulder showing crisp tactical knife and claw combat scars",
            box3_cap="BLACKWOLF COMBAT SCARS",
            build="191 cm (6'3\") dense functional commando musculature, broad squared shoulders, low body fat, weathered tanned scarred warrior frame.",
            face="Match kaladin_anchor.jpg 1:1 in facial bone structure, scars, facial hair, and eye color across ALL 4 views: chiseled severe masculine jawline, weathered tanned skin, piercing vivid emerald-teal eyes, sculpted trimmed dark goatee and mustache connected along the jawline, diagonal scar across forehead and left brow ridge, small vertical scar above right brow, curved cheekbone scars, zero horns.",
            hair="Long jet-black hair swept cleanly back into a low ponytail behind the nape, with TWO loose dark curtain strands framing his forehead and temples as shown in kaladin_anchor.jpg, smoothly covering the sides of his head.",
            anatomy="Werewolf ONLY (STRICTLY NO HORNS, NO DEMON HORNS): adapt the human portrait of kaladin_anchor.jpg cleanly to werewolf anatomy by adding a single pair of sharp black wolf ears atop his head and a thick mutated black wolf tail, while keeping the sides of his head smooth and covered by swept temple hair with STRICTLY ZERO HUMAN EARS visible in any view.",
            outfit="Minimalist matte black photography-studio underwear (fitted black boxer briefs), barefoot.",
            marks="Cold-iron surgical scars at the nape of the neck; Gamma-7 military dog tags; heavy combat scars across chest, arms, forehead, brow, and cheekbones.",
        ),
        neutral_anchors=["kaladin_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Major Kaladin Blackwolf Nargathon, 45-year-old 191 cm military-engineered werewolf commander (STRICTLY NO HORNS), dense functional commando musculature, weathered tanned skin, "
            "long jet-black hair swept back into a low ponytail with two loose dark front strands framing his forehead and temples (smoothly covering the sides of his head with ZERO human ears), "
            "piercing vivid emerald-teal eyes, sculpted trimmed dark goatee and mustache connected along the jawline, forehead/brow and cheekbone scars, "
            "single pair of sharp black wolf ears atop his head, and a thick mutated black wolf tail behind his legs.",
            "DCC Security Tactical Field Uniform: fitted charcoal-black fireproof long-sleeve combat shirt with sleeves pushed up slightly, "
            "matte-black modular ballistic plate carrier vest with 'DCC SECURITY' insignia patch, tactical gun belt with thigh holster, "
            "reinforced black ripstop tactical cargo pants with knee pads and rear tail opening, and rugged black tactical combat boots.",
            191,
            "~8.0-head dense commando proportions",
        ),
    )

    add(
        "nixara",
        "1B",
        "Nixara",
        165,
        True,
        "nixara_reference.png",
        "nixara_neutral.png",
        ref_anchors=["alyssa_reference.png", "nixara_anchor.jpg"],
        ref_prompt=MASTER_REF_TEMPLATE.format(
            identity="Nixara Hvit Bloodmoon, 29-year-old 3rd White Moon Dominant Omega Werewolf",
            tail_attach="lush snow-white wolf tail emerging from the lower spine",
            ear_summary="single pair of snow-white wolf ears with gold sun-moon ornament",
            subtitle="PERTHRO RUNE • WHITE MOON MARK • CELESTIAL EAR ORNAMENT",
            box1_desc="Macro close-up of slender inner left wrist showing the Perthro (ᛈ) rune tattoo in cold-iron dark ink",
            box1_cap="PERTHRO RUNE (LEFT WRIST)",
            box2_desc="Macro close-up of left hip showing a luminous pearlescent crescent White Moon birthmark",
            box2_cap="WHITE MOON MARK (LEFT HIP)",
            box3_desc="Macro close-up of snow-white wolf ear adorned with a delicate golden crescent-and-sun dangling ear ornament",
            box3_cap="CELESTIAL EAR ORNAMENT",
            build="165 cm graceful feminine hourglass figure, warm sun-kissed luminous skin, soft athletic poise.",
            face="Radiant serene feminine face matching the face reference, warm expressive sky-blue eyes, light freckles across nose and cheeks, gentle affectionate smile.",
            hair="Long voluminous honey-golden caramel wavy hair cascading past the waist with delicate thin side braids.",
            anatomy="Single pair of pure snow-white wolf ears atop her head (left ear wearing a delicate gold sun-and-moon dangling earring), and a lush fluffy snow-white wolf tail. STRICTLY NO HUMAN EARS on the sides of the head; wavy golden hair frames the temples.",
            outfit="Minimalist matte black photography-studio underwear (strapless black bandeau top and minimal black briefs), barefoot.",
            marks="Perthro (ᛈ) rune in cold-iron dark ink on inner left wrist; pearlescent crescent moon birthmark on left hip; gold sun-and-moon earring on left wolf ear.",
        ),
        neutral_anchors=["nixara_body_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Nixara Hvit Bloodmoon, 29-year-old radiant 165 cm White Moon werewolf matriarch, long voluminous honey-golden wavy hair with delicate thin braids, "
            "warm bright sky-blue eyes, soft nose and cheek freckles, affectionate serene smile, single pair of pure snow-white wolf ears atop her head with a small golden sun-and-moon dangling earring on the left ear (no human ears), "
            "lush fluffy snow-white wolf tail behind her dress, and Perthro rune on her inner left wrist.",
            "Bohemian-royal California Pack Mom dress: flowing warm cream-sand linen maxi dress with delicate golden botanical embroidery around the V-neckline, "
            "three-quarter sleeves, braided cognac leather waist belt, teardrop amber pendant necklace on a thin gold chain, delicate layered gold-and-pearl wrist bracelets, "
            "rear tail opening, and flat tan woven leather sandals.",
            165,
            "~7.2-head graceful feminine proportions",
        ),
    )

    add(
        "echo",
        "1B",
        "Echo",
        178,
        False,
        "echo_reference.png",
        "echo_neutral.png",
        ref_anchors=["jasper_reference.png"],
        ref_prompt=(
            "Professional 16:9 widescreen technical prop/construct turnaround reference sheet of E.C.H.O. (Electronic Counter-measures & Heuristic Operative), "
            "Jasper Douglas's sentient NON-HUMANOID technomantic AI manifesting EXCLUSIVELY as a compact 30 cm hovering hexagonal matte-obsidian magitech recon drone and translucent emerald-cyan holographic audio waveform projection, "
            "rendered in a cohesive semi-realistic digital illustration style matching Jasper's universe with refined clean dark ink linework and glowing emerald-cyan sci-fi light effects. "
            "STRICT INVARIANT: ZERO human body, ZERO humanoid torso, ZERO human face, ZERO arms, ZERO legs, ZERO clothing — E.C.H.O. is purely a levitating hexagonal magitech drone & holographic audio waveform. "
            "BACKGROUND & LIGHTING: Flat, solid, completely uniform neutral light-grey studio background (#C8C8C8) with no gradients, no floor shadows, and no environment. "
            "LAYOUT (LEFT TO RIGHT): "
            "1. Left — Front view labeled \"VISTA FRONTALE\" at the top: hovering hexagonal matte-obsidian titanium & cold-iron micro-drone with bevelled runes and a central luminous emerald-green geometric iris optical lens, emitting a crisp floating 3D translucent emerald-cyan holographic harmonic audio-oscilloscope waveform and concentric geometric rune data ring beside it. "
            "2. Center-left — Three-quarter view labeled \"VISTA A 45° / TRE QUARTI\" at the top: 45-degree rotated view of the hovering hexagonal drone with micro-thruster emerald glow vents and unfolded translucent holographic telemetry projection panels. "
            "3. Center-right — Side profile view labeled \"VISTA LATERALE\" at the top: sleek beveled side profile of the compact 30 cm hexagonal drone chassis, recessed cold-iron emitter array, and planar floating holo-wave ring. "
            "4. Right (Top) — Close-up detail labeled \"DETTAGLIO NUCLEO\" at the top: large macro view of the glowing emerald-green technomantic geometric iris optical eye set into brushed matte-obsidian plating with engraved Norse-circuit silver runes. "
            "5. Right (Bottom) — Section titled \"DETTAGLI TECNICI:\" with subtitle \"HOLO-WAVE • MAGITECH CHASSIS • OPTICAL CORE\", above three aligned square close-up inset boxes with thin dark borders: "
            "- Box 1: Macro glowing emerald-cyan 3D oscilloscope harmonic audio wave — caption: \"HOLO-WAVE OSCILLOSCOPE\" "
            "- Box 2: Macro brushed matte-obsidian & cold-iron drone bevel with faint Norse circuit filigree — caption: \"COLD-IRON RUNE CHASSIS\" "
            "- Box 3: Macro glowing emerald-green geometric iris sensor core — caption: \"EMERALD OPTICAL CORE\"."
        ),
        neutral_anchors=[],
        neutral_prompt=(
            "Standalone sci-fi/urban-fantasy character sprite illustration in a 2:3 vertical frame of E.C.H.O. (Electronic Counter-measures & Heuristic Operative), "
            "Jasper Douglas's sentient NON-HUMANOID technomantic AI companion manifesting EXCLUSIVELY as a compact 30 cm hovering autonomous hexagonal matte-obsidian and cold-iron magitech recon micro-drone paired with a crisp glowing 3D translucent emerald-cyan holographic audio-oscilloscope waveform and floating concentric runic telemetry rings. "
            "STRICTLY NON-HUMANOID INVARIANT: ZERO human body, ZERO humanoid torso, ZERO human face, ZERO arms, ZERO legs, ZERO clothing. Purely the sleek levitating hexagonal magitech drone centered in the upper-middle chest-to-eye zone of the 2:3 frame with a vivid luminous emerald-green geometric optical iris eye, engraved Norse-circuit cold-iron runes along the obsidian bevels, subtle bottom emerald anti-grav glow, and crisp translucent emerald-cyan holographic soundwaves orbiting beside it. "
            "BACKGROUND: Completely flat, solid pure white background (#FFFFFF) with ZERO gradients, ZERO floor shadow, ZERO ground line, ZERO text, ZERO labels, ZERO borders, and ZERO environment. Clean closed dark ink outer outline around the solid drone chassis and crisp high-contrast emerald-cyan holographic lines that stay legible against pure white."
        ),
    )

    # === WAVE 2: 10 Standalone NPCs (assets/NPC/<Name>/) ===
    wave2_specs_custom = [
        (
            "zeera",
            "NPC\\Zeera",
            208,
            False,
            ["zeera_anchor.jpg"],
            MASTER_REF_TEMPLATE.format(
                identity="Zeera Darkfire (appearing 29, 208 cm brute muscular male Red Bloodline Vax Demon CEO & Warlord, anchored 1:1 to zeera_anchor.jpg)",
                tail_attach="sleek dark-bronze spade-tipped demon tail extending cleanly from the lower spine",
                ear_summary="long horizontal pointed demon ears jutting sharply sideways, tall thick upward-curving dark ribbed horns rising above the crown, glowing crimson-red eyes, and horizontal bridge-of-nose scar",
                subtitle="CORNA ALTE RIBBED • TATUAGGI TRIBALI • CICATRICE NASALE",
                box1_desc="Macro of tall thick ribbed dark demonic horn curving upward from bronzed brow",
                box1_cap="UPWARD-CURVED HORNS",
                box2_desc="Close-up of massive dark-bronze deltoid & bicep covered in bold black demonic tribal ink",
                box2_cap="WARLORD ARM TATTOOS",
                box3_desc="Macro of glowing crimson-red eyes, horizontal nose bridge scar & pointed ear",
                box3_cap="CRIMSON EYES & SCAR",
                build="208 cm (6' 10\") colossal brute muscular warlord silhouette, huge thick shoulders and heavy arms matching zeera_anchor.jpg",
                face="Sharp fierce bronze-terracotta face with infernal crimson undertones, glowing crimson-red eyes, horizontal scar across nose bridge, stoic menacing scowl",
                hair="Long wild shaggy jet-black hair cascading loosely past shoulders and back with subtle red cord/bead accents (NO neat twin braids)",
                anatomy="Tall thick upward-curving ribbed dark horns rising above crown, long horizontal pointed demon ears (ZERO wolf ears), sleek spade-tipped dark-bronze demon tail",
                outfit="Fitted matte dark obsidian/red-accented boxer-brief trunks in the full-body turnaround views so shoulder/arm/chest tattoos, crimson-bronze skin, and tail attachment remain clear",
                marks="Bold black tribal/demonic blackwork tattoos covering BOTH massive shoulders, deltoids, biceps, and forearms, plus horizontal nose scar.",
            ),
            "Zeera Darkfire, appearing 29, 208 cm muscular male Red Bloodline Vax Demon matching zeera_anchor.jpg, bronze skin, tall upward-curving dark horns, long wild loose jet-black hair, crimson eyes, horizontal nose scar, bold black tribal arm tattoos on both shoulders/arms, horizontal pointed demon ears, sleek demon tail, tailored charcoal shirt & black slacks.",
        ),
        (
            "richard",
            "NPC\\Richard_W",
            193,
            False,
            ["richard_anchor.jpg"],
            MASTER_REF_TEMPLATE.format(
                identity="Richard Whitlock (DDM Contractor #01, 47-year-old 193 cm weathered muscular military knight commander in BASE HUMAN FORM, anchored 1:1 to richard_anchor.jpg)",
                tail_attach="clean upright human lumbar back (NO lion tail and NO lion ears in base mortal shifter form)",
                ear_summary="ordinary human ears at the sides of his head (STRICTLY ZERO lion ears and ZERO tail in base form), NO glasses, piercing icy light-blue eyes, prominent vertical scar slashing across his LEFT eye and left cheek, short neat salt-and-pepper hair, and full neatly trimmed salt-and-pepper beard",
                subtitle="CICATRICE OCCHIO SINISTRO • SIGILLO STARFALL • FORMA BASE UMANA",
                box1_desc="Macro of left eye & cheek showing vertical pale battle scar slashing through brow, icy blue eye, and cheekbone",
                box1_cap="LEFT EYE SCAR",
                box2_desc="Heavy antique gold Starfall family signet ring worn on scarred tanned knight hand",
                box2_cap="STARFALL SIGNET RING",
                box3_desc="Macro of faded neck/hanging scar & old shoulder knightly scars on weathered tanned skin",
                box3_cap="KNIGHT COMBAT SCARS",
                build="193 cm (6' 4\") broad muscular weathered military commander physique matching richard_anchor.jpg",
                face="Seasoned authoritative 47-year-old warm-tanned face matching richard_anchor.jpg, NO glasses, piercing icy light-blue eyes, prominent vertical scar cutting across his LEFT eye and cheek, neatly trimmed full salt-and-pepper beard and mustache",
                hair="Short neat side-swept salt-and-pepper / silver-grey hair with tapered sides and a single loose silver-grey lock falling over forehead",
                anatomy="Mortal Shifter BASE HUMAN FORM: ordinary human ears, STRICTLY ZERO lion ears atop head and ZERO lion tail (Lion is full beast shift ANIMAL_FORM only)",
                outfit="Fitted matte smoke-grey athletic boxer-brief trunks in the full-body turnaround views so knight scars, neck marks, and human proportions remain clear",
                marks="Vertical scar through left eye and cheek, gold Starfall signet ring on hand, faded old hanging neck scar and chest/shoulder scars.",
            ),
            "Richard Whitlock (DDM Contractor #01), 47yo 193cm weathered muscular knight commander matching richard_anchor.jpg in BASE HUMAN FORM (human ears only, NO lion ears, NO tail, NO glasses), short neat side-swept salt-and-pepper hair, neatly trimmed salt-and-pepper beard, icy light-blue eyes, vertical scar through left eye & cheek, heavy grey cable-knit sweater & smoke-grey wool trousers.",
        ),
        (
            "mac",
            "NPC\\Mac",
            204,
            True,
            ["mac_anchor.jpg"],
            MASTER_REF_TEMPLATE.format(
                identity="Mackenzie 'Mac' Sanchez-Rogers (19-year-old 204 cm Pureblood Alpha Werewolf keyboardist, anchored 1:1 to mac_anchor.jpg)",
                tail_attach="thick bushy golden-blond wolf tail extending cleanly from the lower spine",
                ear_summary="single pair of large fluffy golden-blond wolf ears atop his head (ZERO human ears), tousled golden-blond hair, scruffy blond jawline beard, double silver right-eyebrow piercing, and nose/cheek scars",
                subtitle="PIERCING SOPRACCIGLIO • TATUAGGIO COLLO/BRACCIO • CODA DORATA",
                box1_desc="Macro of right eyebrow double silver piercing, horizontal nose bridge scar & diagonal cheek scar",
                box1_cap="BROW PIERCING & SCARS",
                box2_desc="Close-up of large dark ink wing/moth tattoo on right side of neck & right-arm sleeve tattoo",
                box2_cap="NECK & RIGHT SLEEVE INK",
                box3_desc="Macro of bushy golden-blond wolf tail & calloused keyboardist hand",
                box3_cap="GOLDEN WOLF TAIL",
                build="204 cm (6' 8\") broad massive powerhouse Pureblood werewolf build with strong shoulders and arms",
                face="Warm tanned rugged Latin face matching mac_anchor.jpg, heavy-lidded warm amber-brown eyes, scruffy blond jawline beard/heavy stubble, double silver eyebrow piercing on right brow, horizontal scar across nose bridge and thin diagonal left cheek scar",
                hair="Tousled shaggy golden-dirty-blond hair cascading naturally around temples",
                anatomy="Werewolf Partial Shift: single pair of large fluffy golden-blond wolf ears atop head (ZERO human ears on sides), bushy golden-blond wolf tail",
                outfit="Fitted matte black athletic boxer-brief trunks in turnaround views so right-neck tattoo, right-arm sleeve ink, scars, and golden tail stay clear",
                marks="Large dark wing/blade tattoo on right side of neck, extensive right-arm/forearm dark illustrative sleeve tattoo, double right eyebrow piercing, nose & cheek scars.",
            ),
            "Mackenzie 'Mac' Sanchez-Rogers, 19yo 204cm powerhouse Pureblood Werewolf matching mac_anchor.jpg, shaggy golden-blond hair, scruffy blond jawline beard, double silver right-eyebrow piercing, nose/cheek scars, right-neck wing tattoo & right-arm sleeve ink, golden wolf ears & tail, plaid flannel open over olive tank top.",
        ),
        (
            "larek",
            "NPC\\Larek",
            201,
            False,
            ["larek_anchor.jpg"],
            MASTER_REF_TEMPLATE.format(
                identity="Larek Steeltooth (21-year-old 201 cm colossal muscular Orc SUCC student, anchored 1:1 to larek_anchor.jpg)",
                tail_attach="clean muscular back with NO tail",
                ear_summary="long sharply pointed Orc ears pierced with multiple dark metal hoops along lower lobes, deep-set dark crimson-amber eyes, notched lower ivory tusks, and LONG straight jet-black hair",
                subtitle="ZANNE D'AVORIO • TATUAGGI BIANCHI TRIBALI • ORECCHIE FORATE",
                box1_desc="Macro of lower jaw with two prominent ivory tusks (subtle notch on right tusk)",
                box1_cap="NOTCHED IVORY TUSKS",
                box2_desc="Sprawling pale-white/silver tribal war-paint tattoos over massive sage-green shoulder & arm",
                box2_cap="WHITE TRIBAL INK",
                box3_desc="Long pointed sage-green Orc ear pierced with dark metal hoop rings & dark hair cords",
                box3_cap="PIERCED ORC EARS",
                build="201 cm (6' 7\") colossal hyper-muscular Orc bodybuilder physique matching larek_anchor.jpg, massive deltoids and broad chest",
                face="Strong broad Orc jaw matching larek_anchor.jpg, deep-set dark crimson-amber eyes, prominent polished lower ivory tusks (subtle notch on right tusk)",
                hair="LONG straight jet-black hair cascading smoothly past chest and shoulders, bound with small leather/cord ties (NOT cropped fade)",
                anatomy="Weathered pale sage/slate-green Orc skin, long pointed Orc ears with multiple dark metal hoop piercings, strictly NO wolf ears and NO tail",
                outfit="Fitted matte dark charcoal/red-accented boxer-brief trunks in full-body turnaround views so pale-white shoulder/chest/arm tribal tattoos remain 100% clear",
                marks="Extensive pale-white / silver tribal geometric tattoos across BOTH huge shoulders, upper chest edges, biceps, and forearms; notched right lower tusk.",
            ),
            "Larek Steeltooth, 21yo 201cm colossal Orc bodybuilder matching larek_anchor.jpg, weathered sage-green skin, LONG straight jet-black hair past chest with leather ties, pale-white/silver tribal tattoos sprawling across both shoulders, chest & arms, dark crimson-amber eyes, pierced pointed Orc ears with hoops, lower ivory tusks.",
        ),
        (
            "adam",
            "NPC\\Adam",
            188,
            False,
            ["adam_anchor.jpg"],
            MASTER_REF_TEMPLATE.format(
                identity="Adam Valencia (DDM Contractor #02A, 28-year-old 188 cm muscular bronze-tanned Arctic Wolf Shifter in BASE HUMAN FORM, anchored 1:1 to adam_anchor.jpg)",
                tail_attach="clean human back with old healed sword-impalement exit scar (NO wolf tail and NO wolf ears in base mortal form)",
                ear_summary="ordinary human ears at the sides of his head (STRICTLY ZERO wolf ears and ZERO tail in base form), warm sun-kissed bronze-tan skin, messy pure snow-white shaggy mullet, and pale heterochromatic eyes",
                subtitle="PELLE BRONZEA • CAPELLI BIANCHI • CICATRICE NUCA 'II'",
                box1_desc="Macro close-up of bronze-tanned face showing luminescent pink-violet & ice-blue heterochromatic eyes",
                box1_cap="HETEROCHROMATIC EYES",
                box2_desc="Back of bronze-tanned neck showing glowing pale carved Roman numeral 'II' scar under white mullet curls",
                box2_cap="NAPE SCAR 'II'",
                box3_desc="Old healed sword-impalement scar diagonally across muscular bronze torso",
                box3_cap="TORSO SWORD SCAR",
                build="188 cm (6' 2\") lean athletic muscular broad European build matching adam_anchor.jpg",
                face="Warm sun-kissed bronze/tan-brown complexion (NOT pale!), clean-shaven sharp handsome jaw, confident smirk, pale luminescent heterochromatic blue/violet-pink eyes",
                hair="Messy tousled pure stark snow-white shaggy wolf-cut / mullet hair falling around cheeks and back of neck",
                anatomy="Mortal Shifter BASE HUMAN FORM: ordinary human ears, STRICTLY ZERO wolf ears atop head and ZERO wolf tail (Arctic Wolf is full beast shift ANIMAL_FORM only)",
                outfit="Fitted matte dark charcoal tactical boxer-brief trunks in turnaround views so bronze-tan skin & torso sword scar remain clear",
                marks="Raised pale Roman numeral 'II' scar on nape of neck, old healed diagonal sword scar across bronze chest/torso.",
            ),
            "Adam Valencia (DDM Contractor #02A), 28yo 188cm lean muscular shifter matching adam_anchor.jpg in BASE HUMAN FORM (human ears only, NO wolf ears, NO tail), warm sun-kissed bronze-brown skin contrasting pure snow-white messy mullet hair, clean-shaven smirk, pale heterochromatic eyes, 'II' nape scar, dark DDM tactical #02 turtleneck & vest.",
        ),
        (
            "hana",
            "NPC\\Hana_V",
            180,
            False,
            ["hana_anchor.jpg"],
            MASTER_REF_TEMPLATE.format(
                identity="Hana Valencia (DDM Contractor #02H, 28-year-old 180 cm athletic busty bronze-tanned Arctic Wolf Shifter in BASE HUMAN FORM, anchored 1:1 to hana_anchor.jpg)",
                tail_attach="clean human lower back (NO wolf tail and NO wolf ears in base mortal form)",
                ear_summary="ordinary human ears at the sides of her head (STRICTLY ZERO wolf ears and ZERO tail in base form), warm sun-kissed bronze-tan skin, long wavy pure snow-white hair, and pale heterochromatic eyes",
                subtitle="PELLE BRONZEA • CAPELLI BIANCHI • CICATRICE NUCA 'II'",
                box1_desc="Macro close-up of bronze-tanned face showing luminescent ice-blue & pink-violet heterochromatic eyes",
                box1_cap="HETEROCHROMATIC EYES",
                box2_desc="Back of bronze-tanned neck showing glowing pale carved Roman numeral 'II' scar under long white waves",
                box2_cap="NAPE SCAR 'II'",
                box3_desc="Old healed sword-impalement scar across athletic bronze midriff/torso",
                box3_cap="TORSO SWORD SCAR",
                build="180 cm (5' 11\") athletic, toned, busty hourglass physique matching hana_anchor.jpg",
                face="Warm sun-kissed bronze/tan-brown complexion (NOT pale!), sharp brooding handsome beauty, pale luminescent heterochromatic ice-blue & neon-pink eyes",
                hair="Long flowing wavy pure stark snow-white hair cascading over shoulders and chest",
                anatomy="Mortal Shifter BASE HUMAN FORM: ordinary human ears, STRICTLY ZERO wolf ears atop head and ZERO wolf tail (Arctic Wolf is full beast shift ANIMAL_FORM only)",
                outfit="Fitted matte dark charcoal sports bra & athletic boyshorts in turnaround views so bronze-tan skin, hourglass build, and torso sword scar remain clear",
                marks="Raised pale Roman numeral 'II' scar on nape of neck, old healed diagonal sword scar across bronze chest/midriff.",
            ),
            "Hana Valencia (DDM Contractor #02H), 28yo 180cm athletic busty shifter matching hana_anchor.jpg in BASE HUMAN FORM (human ears only, NO wolf ears, NO tail), warm sun-kissed bronze-brown skin contrasting long wavy pure snow-white hair, brooding pale heterochromatic eyes, 'II' nape scar, dark DDM tactical #02 turtleneck & vest.",
        ),
        (
            "luka",
            "NPC\\Luka",
            193,
            False,
            ["luka_anchor.jpg"],
            MASTER_REF_TEMPLATE.format(
                identity="Luka Sutter (DDM Contractor #03, 32-year-old 193 cm heavily muscular security chief in BASE HUMAN FORM, anchored 1:1 to luka_anchor.jpg)",
                tail_attach="clean muscular human lumbar back (NO bear tail and NO bear ears in base mortal shifter form)",
                ear_summary="ordinary human ears with a solid black circular ear plug/gauge in his LEFT earlobe (STRICTLY ZERO bear ears and ZERO tail in base form), windswept crimson-red hair, jawline stubble, hazel-green eyes, and X-shaped scar on LEFT cheek",
                subtitle="CICATRICE A 'X' • ORECCHINO NERO • CICATRICI AVAMBRACCIO",
                box1_desc="Macro of left cheek & intense hazel-green eye bearing a prominent deep X-shaped scar & jawline stubble",
                box1_cap="LEFT CHEEK X-SCAR",
                box2_desc="Macro of left human ear wearing a matte-black circular plug/gauge with swept crimson-red locks",
                box2_cap="BLACK EAR GAUGE",
                box3_desc="Muscular tanned right forearm bearing an old X-shaped scar & orbital decompression scars",
                box3_cap="FOREARM X-SCAR",
                build="193 cm (6' 4\") heavily muscular broad tactical brute physique matching luka_anchor.jpg",
                face="Warm sun-tanned rugged face matching luka_anchor.jpg, intense pale hazel-green eyes under furrowed brow, trimmed jawline stubble, prominent X-shaped scar on his LEFT cheek",
                hair="Short-to-medium windswept vivid crimson-red hair swept back with loose messy bangs and slightly longer nape locks",
                anatomy="Mortal Shifter BASE HUMAN FORM: ordinary human ears (black circular gauge plug in left earlobe), STRICTLY ZERO bear ears atop head and ZERO bear tail (Black Bear is full beast shift ANIMAL_FORM only)",
                outfit="Fitted matte olive-drab athletic boxer-brief trunks in full-body turnaround views so tanned muscular torso and forearm X-scar remain clear",
                marks="Prominent X-shaped scar on LEFT cheek, X-shaped scar on right forearm, black ear gauge in left earlobe, orbital scars.",
            ),
            "Luka Sutter (DDM Contractor #03), 32yo 193cm heavily muscular security chief matching luka_anchor.jpg in BASE HUMAN FORM (human ears with black left ear gauge, NO bear ears, NO tail), windswept vivid crimson-red hair, jawline stubble, X-shaped scar on left cheek & right forearm, olive tank top & camo tactical cargo pants.",
        ),
        (
            "dullahan",
            "NPC\\Dullahan",
            203,
            False,
            ["dullahan_anchor.jpg"],
            MASTER_REF_TEMPLATE.format(
                identity="Dullahan (DDM Contractor #04, 34-year-old 203 cm heavily muscular HEADLESS Euclidean Division Head in BASE FORM, anchored 1:1 to dullahan_anchor.jpg)",
                tail_attach="clean muscular pale-grey human lumbar back (NO animal tail in base form)",
                ear_summary="COMPLETELY HEADLESS void inside a perpetual dark olive-charcoal hood (pure pitch-black mist cavity — STRICTLY NO skull, NO eyes, NO face, NO head)",
                subtitle="CAPPUCCIO SENZA TESTA • MARCHIO 'IV' SPALLA • PELLE GRIGIA",
                box1_desc="Macro inside perpetual dark olive-charcoal hood showing pure pitch-black headless void & faint swirling shadow mist",
                box1_cap="HEADLESS VOID HOOD",
                box2_desc="Close-up of dull ash-grey left shoulder blade carved cleanly with Roman numeral scar 'IV'",
                box2_cap="SCAR 'IV' (SHOULDER)",
                box3_desc="Muscular pale ash-grey forearm scars alongside simple silver metal coach whistle",
                box3_cap="ARM SCARS & WHISTLE",
                build="203 cm (6' 8\") towering heavily muscular broad frame with dull pale ash-grey skin matching dullahan_anchor.jpg",
                face="NONE — STRICTLY HEADLESS: perpetual dark olive-charcoal hood reveals only pure pitch-black void and subtle swirling shadow mist",
                hair="NONE",
                anatomy="Headless muscular humanoid with dull pale ash-grey skin, NO head inside perpetual hood, NO animal ears and NO animal tail in base form (Irish Wolfhound is ANIMAL_FORM only)",
                outfit="Fitted matte dark charcoal boxer-brief trunks paired with a sleeveless/cropped perpetual dark olive-charcoal hood cowl over shoulders so pale ash-grey torso, arm scars, and left shoulder-blade 'IV' mark stay clear",
                marks="Roman numeral 'IV' carved on left shoulder blade, faded arm scars, silver coach whistle on neck lanyard.",
            ),
            "Dullahan (DDM Contractor #04), 34yo 203cm heavily muscular HEADLESS Euclidean head matching dullahan_anchor.jpg in BASE FORM (dull ash-grey skin, black mist void inside perpetual dark olive-charcoal hood, NO animal tail), 'IV' carved on left shoulder blade, silver coach whistle, dark grey hoodie & track pants.",
        ),
        (
            "johan",
            "NPC\\Johan",
            182,
            False,
            ["johan_anchor.jpg"],
            MASTER_REF_TEMPLATE.format(
                identity="Dr. Johan Jakobsen (DDM Contractor #05, 28-year-old 182 cm thin lanky sickly pale prodigy in BASE HUMAN FORM, anchored 1:1 to johan_anchor.jpg)",
                tail_attach="clean thin lanky human lumbar back (NO rat tail and NO rat ears in base mortal shifter form)",
                ear_summary="ordinary human ears peeking under long greasy black strands (STRICTLY ZERO rat ears and ZERO rat tail in base form), NO glasses, sunken pale eyes, and heavy reddish-dark insomnia circles",
                subtitle="INSONNIA PROFONDA • NESSUN OCCHIALE • CAPELLI NERI LUNGHI",
                box1_desc="Macro of gaunt pale anxious face with heavy reddish-dark insomnia circles under sunken pale-grey eyes (NO glasses)",
                box1_cap="INSOMNIAC EYES",
                box2_desc="Gaunt pale long-fingered researcher hands wearing crisp white surgical latex gloves holding sample",
                box2_cap="GLOVED RESEARCH HANDS",
                box3_desc="Faint old six-story fall trauma scars along slender pale ribcage and collarbone",
                box3_cap="GAUNT FALL SCARS",
                build="182 cm (6' 0\") thin, lanky, gaunt scholar build with narrow shoulders and visible collarbones matching johan_anchor.jpg",
                face="Gaunt pale anxious face matching johan_anchor.jpg, NO glasses, sunken dark-ringed eyes with heavy reddish insomnia circles and stressed flush across nose/cheeks",
                hair="Long straight unkempt greasy jet-black hair hanging past shoulders with messy loose dark strands framing forehead and cheeks",
                anatomy="Mortal Shifter BASE HUMAN FORM: ordinary human ears peeking through long black hair, STRICTLY ZERO rat ears atop head and ZERO rat tail (Brown Rat is full beast shift ANIMAL_FORM only)",
                outfit="Fitted matte dark slate boxer-brief trunks in turnaround views so gaunt ribcage, narrow build, and fall scars remain clear",
                marks="Heavy reddish-dark insomnia shadows under eyes, old healed six-story fall scars on slender torso.",
            ),
            "Dr. Johan Jakobsen (DDM Contractor #05), 28yo 182cm thin lanky pale prodigy matching johan_anchor.jpg in BASE HUMAN FORM (human ears only, NO rat ears, NO rat tail, NO glasses), long straight unkempt jet-black hair, heavy reddish-dark insomnia circles under sunken eyes, pale mint-green lab scrub jacket, white surgical gloves & clogs.",
        ),
        (
            "fenrir",
            "NPC\\Fenrir",
            203,
            False,
            ["fenrir_anchor.jpg"],
            MASTER_REF_TEMPLATE.format(
                identity="Fenrir (DDM Contractor #06 'Subject VI', 26-year-old 203 cm corpse-pale muscular LAZARUS Squad Leader in BASE HUMAN FORM, anchored 1:1 to fenrir_anchor.jpg)",
                tail_attach="clean muscular corpse-pale human lower spine bearing carved Roman numeral scar 'VI' (NO snake tail and NO animal ears in base form)",
                ear_summary="ordinary human ears partly covered by wild shoulder-length shaggy jet-black hair (NO mammal/snake ears, NO tail in base form), hollow dark-ringed milky-pale eerie eyes, and long jagged sutured mouth-to-cheek scar",
                subtitle="CICATRICE BOCCA/GUANCIA • BENDE INSANGUINATE • MARCHIO 'VI'",
                box1_desc="Macro of corpse-pale face with hollow dark-ringed eerie eyes & long jagged sutured scar curving from right mouth corner across jaw",
                box1_cap="SUTURED JAW SCAR",
                box2_desc="Close-up of muscular forearms heavily wrapped in worn white gauze stained with faint dark blood spots",
                box2_cap="BLOODIED ARM WRAPS",
                box3_desc="Lower spine close-up of corpse-pale back carved cleanly with Roman numeral scar 'VI'",
                box3_cap="SPINE BRAND 'VI'",
                build="203 cm (6' 8\") tall, dense muscular genetically engineered LAZARUS super-soldier physique matching fenrir_anchor.jpg",
                face="Severe corpse-pale gaunt face matching fenrir_anchor.jpg, sunken dark-ringed haunting milky/pale eyes, long jagged sutured scar curving from right mouth corner across cheek and jawline",
                hair="Shoulder-length wild messy shaggy jet-black hair hanging unevenly across brow, eyes, and collar (NOT cropped short)",
                anatomy="Mortal Shifter BASE HUMAN FORM: ordinary human ears beneath shaggy black locks, STRICTLY ZERO snake tail and ZERO mammal ears in base form (Kingsnake is full beast shift ANIMAL_FORM only)",
                outfit="Fitted matte black athletic boxer-brief trunks + signature white blood-spotted forearm gauze wraps in turnaround views so corpse-pale scars and lower-spine 'VI' brand remain clear",
                marks="Long jagged sutured right cheek/mouth scar, heavily wrapped blood-spotted white gauze on forearms, carved Roman numeral 'VI' at base of spine, nuclear/surgical torso scars.",
            ),
            "Fenrir (DDM Contractor #06 'Subject VI'), 26yo 203cm corpse-pale muscular super-soldier matching fenrir_anchor.jpg in BASE HUMAN FORM (human ears only, NO snake tail, NO mammal ears), shoulder-length messy shaggy jet-black hair, hollow dark-ringed eerie eyes, jagged sutured right mouth-to-jaw scar, blood-spotted white forearm wraps, 'VI' spine scar, black LAZARUS sleeveless tactical vest & cargo pants.",
        ),
    ]
    for eid, folder, h_cm, ears_above, r_anc, r_prompt, n_summary in wave2_specs_custom:
        add(eid, "2", folder, h_cm, ears_above, f"{eid}_reference.png", f"{eid}_neutral.png", ref_prompt=r_prompt, neutral_prompt=n_summary, ref_anchors=r_anc)

    # === WAVE 3: Variants in the SAME folder as the original ===
    variants = [
        ("jasper_fantasy", "3", "Jasper", 193, True, "jasper_fantasy_reference.png", "jasper_fantasy_neutral.png", "Jasper High Fantasy Silverhaven Rogue-Artificer"),
        ("jasper_ddm", "3", "Jasper", 193, True, "jasper_ddm_reference.png", "jasper_ddm_neutral.png", "Jasper Contractor #08 DDM Void-Weave Tactical"),
        ("jasper_human_modern", "3", "Jasper", 193, False, "jasper_human_reference.png", "jasper_human_modern_neutral.png", "Jasper Baseline Human Modern/Sci-Fi (no wolf ears, no tail, no body fur)"),
        ("jasper_human_historical", "3", "Jasper", 193, False, "jasper_human_reference.png", "jasper_human_historical_neutral.png", "Jasper Baseline Human Historical/Fantasy (no wolf ears, no tail, no body fur)"),
        ("alyssa_fantasy", "3", "Alyssa", 155, True, "alyssa_fantasy_reference.png", "alyssa_fantasy_neutral.png", "Alyssa High Fantasy Silverhaven Healing Mage"),
        ("alyssa_ddm", "3", "Alyssa", 155, True, "alyssa_ddm_reference.png", "alyssa_ddm_neutral.png", "Alyssa Contractor #07 DDM White Void-Weave Tactical"),
        ("alyssa_elf", "3", "Alyssa", 155, False, "alyssa_elf_reference.png", "alyssa_elf_neutral.png", "Alyssa Pureblood Forest Elf (long pointed elven ears, no wolf ears, no tail)"),
        ("alyssa_human_modern", "3", "Alyssa", 155, False, "alyssa_human_reference.png", "alyssa_human_modern_neutral.png", "Alyssa Baseline Human Modern/Sci-Fi (no wolf ears, no tail)"),
        ("alyssa_human_historical", "3", "Alyssa", 155, False, "alyssa_human_reference.png", "alyssa_human_historical_neutral.png", "Alyssa Baseline Human Historical/Fantasy (no wolf ears, no tail)"),
        ("malachia_fantasy", "3", "Malachia", 208, True, "malachia_fantasy_reference.png", "malachia_fantasy_neutral.png", "Malachia High Fantasy Silverhaven Coliseum Vanguard"),
        ("mac_fantasy", "3", "NPC\\Mac", 204, True, "mac_fantasy_reference.png", "mac_fantasy_neutral.png", "Mac High Fantasy Silverhaven War Skald / Sellsword"),
        ("zeera_fantasy", "3", "NPC\\Zeera", 208, True, "zeera_fantasy_reference.png", "zeera_fantasy_neutral.png", "Zeera Darkfire High/Dark Fantasy Whispering Caverns Warlord"),
    ]
    for eid, folder, sub, h_cm, ears_above, rf, nf, desc in variants:
        add(eid, folder, sub, h_cm, ears_above, rf, nf, ref_prompt=desc, neutral_prompt=desc)

    # === WAVE 4_HYBRID: 23 Shifter Hybrid Form 16:9 Reference Cards (<name>_hybrid_reference.png) ===
    hybrid_specs = [
        ("jasper_hybrid", "Jasper", 223, True, "jasper_reference.png", "Jasper 'Svartr' Douglas Bloodmoon (Shadow-Sun Hybrid Shift, 223 cm)", "long black-and-tawny wolf tail", "large tawny-chestnut wolf ears with black tips", "MANNAZ RUNE • SOL HIP MARK • SHADOW-SUN CLAWS", "Tawny-chestnut muzzle with sharp fangs and glowing mint-green-to-gold eyes", "FANGS & EYES", "Dark wolf-beast forearm with jagged obsidian claws and Mannaz rune visible on inner wrist fur", "CLAWS & MANNAZ RUNE", "Thick black-and-tawny fur along right hip glowing with warm Solar gold sub-dermal runes", "SOL RUNE (RIGHT HIP)", "223 cm (7'4\") lean explosive predator wolf-hybrid musculature, broad shoulders, digitigrade hind legs", "Elongated tawny-chestnut lupine snout matching jasper_reference.png gaze, bright mint-green eyes with subtle solar gold slit-pupil gleam", "Dense warm tawny-chestnut fur blended with shadow-black spine, chest, and long fluffy tail", "Bipedal digitigrade legs with dark paw pads and heavy claws; strictly single pair of wolf ears atop skull (zero human ears)", "Black tattered tactical/casual shorts or natural beast anatomy with dark matte fur shading groin."),
        ("alyssa_hybrid", "Alyssa", 185, True, "alyssa_reference.png", "Alyssa Hvit Douglas Bloodmoon (White Moon Wolf Hybrid Shift, 185 cm)", "lush snow-white-and-caramel wolf tail", "tall snow-white wolf ears with caramel tips", "MANNAZ RUNE • MANI MOON MARK • WHITE MOON CLAWS", "Refined fierce she-wolf snout with glowing mint-green eyes and silver-white fur", "SHE-WOLF VISAGE", "Slender clawed wolf forepaw with black obsidian claws and Mannaz rune showing cleanly on inner left wrist", "CLAWS & MANNAZ", "Left hip fur parting to reveal a subtle pearlescent silver Mani crescent glow beneath white fur", "MANI CRESCENT MARK", "185 cm agile, sinuous, fiercely athletic female werewolf-hybrid build with slender curved silhouette and digitigrade legs", "Elongated graceful snow-white lupine muzzle matching alyssa_reference.png eyes, glowing luminous mint-green iris, sharp fangs", "Silky snow-white pelage accented by warm caramel-chestnut back crest and tail markings", "Digitigrade hind paws with black claws, single pair of tall wolf ears atop head (zero human ears)", "Natural thick fur coverage (matching SFW studio modesty with tattered dark athletic wrap/shorts if needed)."),
        ("malachia_hybrid", "Malachia", 258, True, "malachia_reference.png", "Malachia 'Bjorn' Douglas Bloodmoon (Apex Enforcer Hybrid Shift, 258 cm)", "massive pitch-black wolf tail", "heavy battle-notched black wolf ears", "THURISAZ & FENRIS • BLOODMOON FUR • APEX JAWS", "Snarling colossal black wolf muzzle with cold unblinking amber eyes and eyebrow scar", "APEX MUZZLE & SCAR", "Gargantuan blackened forearm with jagged claws and Bloodmoon Norse ink etched subtly through fur", "APEX CLAWS & INK", "Inner left wrist showing Thurisaz & Fenris cold-iron brand pulsing through pitch-black fur", "THURISAZ BRAND", "258 cm (8'6\") titanic 200 kg hypertrophic heavyweight-brawler werewolf-hybrid mass, colossal chest and shoulders", "Heavy scarred pitch-black wolf snout with crooked nasal bridge scar, brow scar, cold unblinking amber eyes, massive ivory fangs", "Dense armored pitch-black Bloodmoon fur coat across torso, shoulders, and tail", "Massive digitigrade bear-like wolf hind legs, thick claws; strictly single pair of black wolf ears atop head", "Natural pitch-black furred beast anatomy (dark studio combat wrap shorts)."),
        ("noah_hybrid", "Noah", 227, True, "noah_reference.png", "Noah 'Loki' Douglas Bloodmoon (Agile Delta Wolf Hybrid Shift, 227 cm)", "sleek golden-blonde wolf tail", "alert golden-blonde wolf ears", "GEBO RUNE • DELTA FANGS • GOLDEN FUR COAT", "Sleek golden-blonde lupine muzzle with bright clear electric-blue predator eyes and cunning half-snarl", "GOLDEN MUZZLE & EYES", "Swift clawed forepaw with golden-tan fur and black razor claws, Gebo X-rune on inner left wrist", "DELTA CLAWS & GEBO", "Close-up of thick golden shoulder mane with layered cream chest fur", "GOLDEN DELTA COAT", "227 cm (7'5\") sleek, fast, streamlined athletic werewolf-hybrid physique built for speed and pouncing", "Sharp fox-lean golden-blonde wolf snout, bright clear blue slit-pupil eyes, subtle nose freckles echoed on snout bridge", "Silky shimmering golden-blonde fur with lighter warm cream belly and throat fur", "Agile digitigrade hind legs, razor-sharp claws; strictly single pair of golden-blonde wolf ears atop head", "Natural thick golden furred anatomy (dark fitted studio athletic shorts)."),
        ("erik_hybrid", "Erik", 263, True, "erik_reference.png", "Erik 'Ulfr' Douglas (Prime Alpha Sovereign Hybrid Shift, 263 cm)", "heavy night-black wolf tail", "commanding night-black wolf ears", "HAGALAZ RUNE • PRIME ALPHA EYES • RITUAL SCAR", "Sovereign night-black wolf muzzle with diagonal left cheek scar and molten-gold Alpha eyes", "SOVEREIGN VISAGE", "Immense night-black forepaw with obsidian claws and Hagalaz rune mark on inner left wrist", "ALPHA CLAWS & HAGALAZ", "Macro silver-streaked black neck ruff framing ancient scar tissue", "SILVER-STREAKED MANE", "263 cm (8'7\") mountainous Prime Alpha apex werewolf-hybrid silhouette, commanding chest and broad warrior shoulders", "Regal terrifying black wolf snout with diagonal cheek scar and silver-flecked brow ridges, piercing amber-gold eyes", "Impenetrable night-black primeval fur with distinguished silver-grey ticking along temples and neck ruff", "Massive digitigrade legs with crushing obsidian claws; strictly single pair of large wolf ears atop skull", "Natural thick night-black furred anatomy (dark matte studio shorts)."),
        ("logan_hybrid", "Logan", 228, True, "logan_reference.png", "Logan 'Jarn' Douglas (Forge-Breaker Wolf Hybrid Shift, 228 cm)", "rugged black-and-silver wolf tail", "notched black-and-grey wolf ears", "EIHWAZ RUNE • BATTLE SCARS • SILVER-FLECKED COAT", "Grizzled black-and-grey wolf muzzle with weathered scars and watchful amber eyes", "GRIZZLED MUZZLE", "Knotty scarred wolf forearm showing faded Norse sleeve ink beneath fur and Eihwaz rune on wrist", "EIHWAZ & FORE-CLAWS", "Close-up of jagged old hunt scars parting dense black-and-silver shoulder pelt", "HUNT SCARS IN FUR", "228 cm (7'6\") knotty, rugged, combat-hardened mechanic-brawler werewolf-hybrid build", "Weathered snarling black wolf muzzle dusted with silver salt-and-pepper around jaw, watchful amber eyes", "Coarse pitch-black fur with rugged silver-grey streaking along shoulders, muzzle, and tail", "Heavy digitigrade stance, iron-hard claws; strictly single pair of wolf ears atop skull", "Natural coarse black-silver furred anatomy (dark tattered work trousers/shorts)."),
        ("edric_hybrid", "Edric", 230, True, "edric_reference.png", "Edric Douglas (Junior Alpha-Bred Wolf Hybrid Shift, 230 cm)", "bushy smoke-grey and black wolf tail", "large smoke-grey and black wolf ears", "SOWILO RUNE • SMOKE-GREY FUR • ALPHA FANGS", "Fierce youthful-edged smoke-grey wolf muzzle with faint cheek scars and glowing amber eyes", "SMOKE-GREY VISAGE", "Broad-boned wolf forepaw with heavy claws and Sowilo rune mark on inner left wrist", "PAW & SOWILO RUNE", "Thick charcoal-and-smoke-grey dorsal hackle fur crest", "SMOKE-GREY PELAGE", "230 cm powerfully framed broad-boned werewolf-hybrid build, dense youthful power", "Sharp smoke-grey and black wolf muzzle with fine healed cheek marks and intense amber eyes", "Thick layered smoke-grey and charcoal-black fur across torso, limbs, and tail", "Digitigrade hind legs with sturdy dark claws; strictly single pair of wolf ears atop skull", "Natural dense furred beast anatomy (dark athletic training shorts)."),
        ("wulfnic_hybrid", "Wulfnic", 285, True, "wulfnic_reference.png", "Wulfnic Baleygr Bloodmoon (Firstborn Ancestral Wolf King Hybrid, 285 cm)", "colossal golden-blonde and snow-white wolf tail", "giant golden-blonde wolf ears streaked with white", "JERA & FENRIS • FIRSTBORN MANE • SUPERNOVA EYES", "Colossal primeval wolf muzzle with 15cm ivory fangs, golden-white ruff, and glowing ice-blue eyes", "FIRSTBORN JAWS & EYES", "Titanic clawed forepaw with Jera & Fenris geometric rune gleaming through fur", "JERA & TITAN CLAWS", "Svartulfr rune ink and ancient battle scars visible beneath golden-blonde-and-white storm mane", "STORM MANE & INK", "285 cm+ colossal Firstborn Enigma mountain of muscle, godlike primeval werewolf stature", "Terrifying battle-worn ancient wolf visage framed by a golden-blonde beard/chin ruff streaked with snow-white, glowing ice-blue eyes", "Thick armored storm-mane of golden-blonde fur heavily streaked with snow-white across shoulders, chest, and spine", "Massive digitigrade hind legs with ebony steel-rending claws; single pair of colossal wolf ears atop skull", "Natural primeval furred beast anatomy."),
        ("magnus_hybrid", "Magnus", 245, True, "magnus_reference.png", "Sir Magnus Douglas III (Pureblood Aristocratic Wolf Hybrid, 245 cm)", "plumed dark charcoal-grey wolf tail", "tall charcoal-grey wolf ears", "OTHALA RUNE • COLONIAL SCAR • CHARCOAL MANE", "Composed terrifying charcoal-silver wolf muzzle with calm amber eyes and silver jaw ruff", "ARISTOCRAT VISAGE", "Inner left wrist showing cold-iron Othala rune beneath dark charcoal fur", "OTHALA RUNE (WRIST)", "Old sabre duel scar parting silver-threaded charcoal chest fur", "SABRE SCAR IN FUR", "245 cm tall, upright, regal Pureblood werewolf-hybrid frame with broad noble chest", "Noble elongated charcoal wolf snout with silvered muzzle ruff, fierce level amber eyes", "Silky thick charcoal-grey fur heavily silver-frosted along neck, temples, and chest", "Upright digitigrade stance with dark claws; single pair of charcoal wolf ears atop skull", "Natural dark charcoal furred anatomy."),
        ("elizabeth_hybrid", "Elizabeth", 205, True, "elizabeth_reference.png", "Lady Elizabeth Duskwood (Matriarch Wolf Hybrid, 205 cm)", "lush pearl-grey and silver wolf tail", "tall ash-grey wolf ears", "URUZ RUNE • PEARL PELAGE • STORM-GREY EYES", "Elegant lethal ash-grey she-wolf muzzle with perceptive storm-grey eyes and sharp white fangs", "MATRIARCH VISAGE", "Slender clawed forepaw with Uruz rune etched in dark fur on inner left wrist", "URUZ RUNE & CLAWS", "Luminous pearl-silver neck ruff fur catching cool studio light", "PEARL-ASH COAT", "205 cm commanding yet graceful female werewolf-hybrid frame with athletic feline-wolf poise", "Refined ash-grey she-wolf snout with calm storm-grey slit-pupil eyes", "Thick velvety ash-grey and pearl-silver fur coat across shoulders, torso, and tail", "Agile digitigrade hind legs with dark claws; single pair of ash-grey wolf ears atop skull", "Natural pearl-ash furred anatomy (modest tattered dark satin wrap at hips)."),
        ("ut_hybrid", "Ut", 320, True, "ut_reference.png", "Ut Berg (The Mountain Firstborn Wolf Hybrid, 320 cm)", "massive reddish-auburn & iron-grey wolf tail", "huge reddish-auburn & iron-grey wolf ears", "LAGUZ & FENRIS • MOUNTAIN SCARS • REDDISH-GREY MANE", "Titanic battle-scarred reddish-auburn & iron-grey wolf muzzle with granite iron-grey eyes", "TITAN MUZZLE", "Tree-trunk clawed forepaw bearing Laguz + Fenris rune and heavy hammered iron arm rings strapped tightly", "LAGUZ & IRON RINGS", "Jagged centuries-old axe and fang scars across reddish-auburn barrel-chest fur", "ANCIENT CHEST SCARS", "320 cm (10'6\") unimaginable walking mountain of muscle, broadest chest and limbs among all shifters", "Massive snarling Viking-wolf snout framed by a wild reddish-auburn jaw ruff streaked with iron-grey, heavy iron-grey eyes", "Coarse, ultra-dense reddish-auburn fur streaked with iron-grey covering boulder-like shoulders and back", "Pillar-like digitigrade legs with crushing black claws; single pair of massive wolf ears atop skull", "Natural coarse furred mountain-titan anatomy."),
        ("zefir_hybrid", "Zefir", 225, True, "zefir_reference.png", "Zefir Hvitskog (North Sea Wind Wolf Hybrid, 225 cm)", "long sleek snow-white wolf tail", "pierced snow-white wolf ears", "ALGIZ & FENRIS • VIKING RUNES • PIERCED WHITE EAR", "Razor-sharp snow-white wolf snout with pale icy washed-out blue eyes and wicked grinning fangs", "GHOST WOLF VISAGE", "Left pierced white wolf ear gleaming with black metal hoop rings along the rim", "PIERCED WOLF EAR", "Lean pale-furred forearm showing dark Algiz & Viking runic skin tattoos visible through cropped white fur", "ALGIZ & VIKING INK", "225 cm lean, hyper-fast, shredded acrobatic werewolf-hybrid frame built for stealth and ambush", "Long sharp snow-white wolf snout, smudged dark periocular shading, pale almost-white ice-blue eyes", "Sleek arctic snow-white fur with wild tousled white dorsal crest along neck and spine", "Whip-fast digitigrade hind legs with curved black claws; single pair of pierced snow-white wolf ears", "Natural snow-white furred anatomy (shredded punk leather hip wrap)."),
        ("kaladin_hybrid", "Kaladin", 250, True, "kaladin_reference.png", "Major Kaladin Blackwolf Nargathon (BlackWolf Mutant Hybrid, 250 cm, ZERO HORNS)", "heavy mutated jet-black wolf tail", "large sharp mutated jet-black wolf ears", "BLACKWOLF MUTATION • CRIMSON-TEAL EYES • NAPE CAGE SCARS", "Predatory mutated black wolf snout with forehead/cheek scars and emerald-teal eyes flaring crimson-red", "BLACKWOLF EYES & SCARS", "Mutated oversized black obsidian claws and scarred tactical commando forearms", "BLACKWOLF CLAWS", "Nape of neck fur parted around faint cold-iron neural restraint surgical scars", "NEURAL CAGE SCARS", "250 cm+ dense urban-warfare mutated werewolf-hybrid physique, hyper-muscular tactical brute power", "Severe mutated black wolf muzzle preserving brow/forehead and cheekbone scars, piercing emerald-teal eyes blazing crimson-red (ZERO HORNS)", "Thick armored pitch-black mutated BlackWolf coat with bristling dorsal spine crest", "Heavy urban-assault digitigrade hind legs capable of scoring concrete; single pair of black wolf ears atop skull (ZERO horns)", "Torn remnants of matte-black tactical combat pants or natural pitch-black furred anatomy."),
        ("nixara_hybrid", "Nixara", 205, True, "nixara_reference.png", "Nixara Hvit Bloodmoon (3rd White Moon Wolf Hybrid, 205 cm)", "lush snow-white wolf tail", "snow-white wolf ears with gold celestial ornament", "PERTHRO RUNE • WHITE MOON MARK • CELESTIAL EARPIECE", "Serene fierce snow-white she-wolf muzzle with warm glowing sky-blue eyes and subtle honey-gold brow dusting", "WHITE MOON VISAGE", "Snow-white wolf ear adorned with golden sun-and-moon dangling ornament", "CELESTIAL EARPIECE", "Left inner wrist showing Perthro rune mark and left hip flashing pearlescent White Moon glow", "PERTHRO & MOON MARK", "205 cm luminous, powerful yet graceful maternal alpha-omega werewolf-hybrid stature", "Graceful fierce snow-white wolf muzzle with warm intense sky-blue eyes and radiant presence", "Luminous snow-white fur accented by delicate warm honey-golden dorsal sheen", "Swift digitigrade hind legs with obsidian claws; single pair of snow-white wolf ears atop skull", "Natural snow-white furred anatomy (modest draped cream linen combat wrap)."),
        ("mac_hybrid", "NPC\\Mac", 235, True, "NPC\\Mac\\mac_reference.png", "Mackenzie 'Mac' Sanchez-Rogers (Pureblood Wolf Hybrid, 235 cm)", "shaggy reddish-brown & ash-grey wolf tail", "large golden-brown wolf ears", "NASAL BRIDGE SCAR • REDDISH-ASH COAT • AMBER EYES", "Expressive reddish-brown wolf muzzle bearing a transverse nasal/cheek scar and bright amber eyes", "MUZZLE & SCAR", "Heavy wolf forepaw with black claws and subtle music-callused palm pads", "HYBRID FORE-PAW", "Fluffy reddish-brown and ash-grey neck ruff fur", "REDDISH-ASH PELAGE", "235 cm broad, energetic powerhouse werewolf-hybrid frame", "Rugged snout with left cheek/nasal bridge scar inherited from human form, fierce golden-amber eyes", "Dense shaggy reddish-brown and ash-grey werewolf pelage", "Agile digitigrade hind legs with dark claws; single pair of wolf ears atop skull", "Natural reddish-ash furred anatomy (torn plaid flannel & dark denim scraps)."),
        ("larek_hybrid", "NPC\\Larek", 235, False, "NPC\\Larek\\larek_reference.png", "Larek Steeltooth (Iron-Tusk Boar Orc Hybrid Shift, 235 cm)", "short coarse black-bristled boar tail", "pointed orcish ears sprouting coarse boar tufts", "IRON-TUSK JAWS • RAZORBACK BRISTLES • CLAN INK", "Massive ferocious Orc-Boar hybrid head with huge notched lower ivory tusks and blazing amber-gold eyes", "IRON-TUSK HEAD", "Gargantuan olive-green clawed boar-orc hand with blunt steel-hard hoof-claws and tribal tricep tattoo", "CLAN INK & CLAWS", "Spiny black razorback bristle ridge erupting down spine and shoulders", "RAZORBACK CREST", "235 cm monstrously wide armored olive-green Orc-Boar hybrid colossus with thick bone plating", "Heavy jutting jaw with massive curved notched ivory lower tusks, broad snout, glowing amber-gold eyes, jet-black fade crest", "Olive-green armored hide covered in coarse dark bristles along shoulders, forearms, and dorsal ridge", "Digitigrade cloven-hoof/clawed beast legs built for battering-ram charges; pointed ears only", "Shredded charcoal hoodie scraps and reinforced olive cargo joggers."),
        ("richard_hybrid", "NPC\\Richard_W", 245, True, "NPC\\Richard_W\\richard_reference.png", "Richard Whitlock (Starfall Lion Warlord Hybrid, 245 cm)", "long tufted tawny lion tail", "rounded tawny lion ears emerging from golden mane", "STARFALL SIGNET CLAW • GOLDEN-GREY MANE • LION JAWS", "Regal terrifying weathered Lion-Warlord hybrid muzzle with golden-and-silver mane, light blue predator eyes, huge fangs", "LION WARLORD VISAGE", "Massive lion paw-hand with thick golden forearm fur, black knuckle pads, and steel-sharp retractable claws", "RETRACTABLE CLAWS", "Gold Starfall signet ring retained or glowing faintly against dark paw fur", "STARFALL RING", "245 cm taurine-shouldered Lion Shifter warlord hybrid frame, massive upper chest and torso", "Broad feline lion muzzle with scarred nose bridge, thick full golden-tawny mane streaked with battle-grey, piercing icy-blue slit eyes", "Short golden-tawny lion fur across torso/limbs crowned by a colossal leonine mane", "Digitigrade feline hind legs with heavy paws; single pair of rounded lion ears atop skull", "Natural tawny furred lion-hybrid anatomy."),
        ("adam_hybrid", "NPC\\Adam", 220, True, "NPC\\Adam\\adam_reference.png", "Adam Valencia (Vanguard Arctic Wolf Hybrid, 220 cm)", "thick snow-white arctic wolf tail", "large snow-white arctic wolf ears", "HETEROCHROMATIC EYES • ROMAN II SCAR • ARCTIC CLAWS", "Snarling snow-white arctic wolf muzzle with luminescent neon-pink right eye and neon-blue left eye", "HETEROCHROMATIC VISAGE", "Nape fur parting over glowing pale scar shaped like Roman numeral 'II'", "ROMAN II NAPE SCAR", "Massive pure white wolf forearm with ice-obsidian claws", "ARCTIC CLAWS", "220 cm broad powerhouse Vanguard arctic wolf-hybrid build, dense snow-white coat", "Sharp pure-white arctic wolf snout, vibrant heterochromatic glowing pink and electric-blue eyes", "Ultra-dense pure snow-white arctic wolf fur across shoulders, chest, and bushy tail", "Heavy digitigrade hind legs with dark claws; single pair of white wolf ears atop skull", "Torn dark charcoal hoodie scraps or natural pure-white furred anatomy."),
        ("hana_hybrid", "NPC\\Hana_V", 205, True, "NPC\\Hana_V\\hana_reference.png", "Hana Valencia (Abyssal Twin Arctic She-Wolf Hybrid, 205 cm)", "plumed snow-white arctic wolf tail", "tall snow-white arctic wolf ears", "HETEROCHROMATIC EYES • ROMAN II SCAR • SILKY WHITE FUR", "Fierce sleek snow-white arctic she-wolf snout with glowing neon-pink and blue heterochromatic eyes", "ARCTIC SHE-WOLF", "Nape fur parting over pale Roman numeral 'II' brand", "ROMAN II NAPE SCAR", "Slender lethal white-furred forepaw with curved obsidian claws", "ABYSSAL CLAWS", "205 cm lithe, elastic, dangerously muscular female arctic werewolf-hybrid frame", "Sleek pure-white she-wolf snout with glowing heterochromatic pink & blue eyes and sharp twin fangs", "Silky dense snow-white arctic pelage with luxurious frost-white shoulder ruff", "Agile feline-fast digitigrade hind legs with dark claws; single pair of white wolf ears atop skull", "Natural silky white furred beast anatomy (shredded black Void-scout hip wrap)."),
        ("luka_hybrid", "NPC\\Luka", 260, True, "NPC\\Luka\\luka_reference.png", "Luka Sutter (Ursa Major Black Bear Hybrid, 260 cm)", "short stubby black bear tail", "rounded black bear ears atop massive skull", "X-SHAPED MUZZLE SCAR • URSA CLAWS • CRIMSON EYES", "Gargantuan roaring Black Bear hybrid head with prominent X-shaped scar across right cheek/muzzle and crimson-tinted eyes", "URSA MAJOR HEAD", "Enormous pitch-black bear forepaw with curved 10cm bone-crushing claws", "BEAR CLAWS", "Heavy crimson-tinted dorsal ruff hairs rising over pitch-black bear shoulders", "BEAR SHOULDER MANE", "260 cm titanic barrel-chested Black Bear hybrid juggernaut, immense shoulders and arms", "Broad heavy ursine snout with X-shaped scar etched across right muzzle, jagged fangs, crimson-hazel glowing eyes", "Ultra-thick pitch-black bear fur across massive torso, limbs, and short stubby tail", "Heavy plantigrade-to-digitigrade bear hind legs with thick paw pads; single pair of rounded bear ears atop head", "Torn camo tactical cargo scraps or natural black bear furred anatomy."),
        ("dullahan_hybrid", "NPC\\Dullahan", 250, False, "NPC\\Dullahan\\dullahan_reference.png", "Dullahan (Headless Steel-Grey Irish Wolfhound Hybrid, 250 cm, NO HEAD)", "wire-haired steel-grey wolfhound tail", "swirling black mist vortex above severed collar (STRICTLY NO HEAD)", "BLACK MIST COLLAR • WIRE-HAIRED GREY FUR • HOUND CLAWS", "Close-up of clean severed grey neck stump emitting dense swirling black spectral mist (ZERO head, ZERO eyes, ZERO face)", "HEADLESS MIST NECK", "Steel-grey wire-haired canine forepaw with spectral dark claws", "WOLFHOUND CLAWS", "Chest fur bearing pale silver DDM seal beneath shredded black shoulder fabric", "SPECTRAL CHEST PELAGE", "250 cm towering heavily muscled canine beast frame with broad taurine shoulders and STRICTLY NO HEAD ABOVE THE NECK", "STRICTLY NO HEAD, NO SKULL, NO FACE: only a continuous column of dark swirling spectral shadow mist rising from the severed grey neck above ragged dark shoulder cloth", "Coarse wiry steel-grey Irish Wolfhound fur across massive arms, chest, digitigrade legs, and tail", "Digitigrade canine hind legs with iron-hard dark claws; zero head/ears", "Tattered dark fabric scraps around shoulders and waist."),
        ("johan_hybrid", "NPC\\Johan", 175, True, "NPC\\Johan\\johan_reference.png", "Johan Jakobsen (Runic Overload Wererat Hybrid, 175 cm)", "long hairless prehensile pink-grey rat tail", "large rounded dark brown rat ears", "CURVED INCISORS • HYPERSENSITIVE WHISKERS • VERMIN CLAWS", "Sharp elongated cinnamon-furred rat snout with long sensitive whiskers, dark sunken glowing eyes, and sharp curved rodent incisors", "WERERAT SNOUT", "Slender clawed rodent forepaw with sparse cinnamon fur and delicate grasping digits", "WERERAT HANDS", "Naked scaly segmented prehensile rat tail coiling behind legs", "PREHENSILE RAT TAIL", "175 cm crouched, wiry, twitchy hyper-agile wererat-hybrid frame", "Pointed elongated rodent snout with twitching whiskers, curved sharp incisor fangs, and dark manic eyes", "Short silky cinnamon-brown fur across head, shoulders, and torso", "Digitigrade elongated rodent hind feet with sharp nimble claws; single pair of large rounded rat ears atop head", "Tattered mint-green lab coat collar/scraps or natural cinnamon furred anatomy."),
        ("fenrir_hybrid", "NPC\\Fenrir", 240, False, "NPC\\Fenrir\\fenrir_reference.png", "Fenrir (Contractor #06 Black Kingsnake Hybrid, 240 cm)", "massive thick glossy black kingsnake tail", "sleek smooth horned-scale serpent head (ZERO mammal ears)", "GLOSSY SCALES • MILKY BLIND EYES • VENOM FANGS", "Terrifying angular black-and-iridescent-blue scaled serpent-humanoid head with sightless milky white eyes, forked tongue, and curved fangs", "SERPENT HEAD & EYES", "Armored glossy black scaled forearm with iridescent blue highlights and curved obsidian talons", "SCALED TALONS", "Macro close-up of interlocking hexagonal glossy black-and-azure dorsal serpent scales", "IRIDESCENT SCALES", "240 cm colossal muscular viper-predator bipedal reptile hybrid, broad constrictor chest and neck", "Elongated muscular serpent hybrid head with smooth scale ear-slits (ZERO wolf or mammal ears), sightless glowing milky-white blind eyes, retractable fangs, forked tongue", "Entirely armored in glossy obsidian-black and iridescent cobalt-blue serpent scales across chest, torso, arms, and tail", "Powerful scaled reptilian digitigrade legs and thick heavy black kingsnake tail trailing behind; zero human/mammal ears", "Natural glossy black-and-blue scaled reptile anatomy (torn matte-black cargo scraps)."),
    ]
    for eid, folder, h_cm, ears_above, src_ref, identity, tail_attach, ear_summary, subtitle, b1d, b1c, b2d, b2c, b3d, b3c, build, face, coat, anatomy, outfit in hybrid_specs:
        add(
            eid,
            "4_HYBRID",
            folder,
            h_cm,
            ears_above,
            f"{eid}_reference.png",
            None,
            ref_anchors=[src_ref],
            ref_prompt=HYBRID_REF_TEMPLATE.format(
                identity=identity,
                tail_attach=tail_attach,
                ear_summary=ear_summary,
                subtitle=subtitle,
                box1_desc=b1d,
                box1_cap=b1c,
                box2_desc=b2d,
                box2_cap=b2c,
                box3_desc=b3d,
                box3_cap=b3c,
                build=build,
                face=face,
                coat=coat,
                anatomy=anatomy,
                outfit=outfit,
            ),
            asset_kind="hybrid_ref",
        )

    # === WAVE 5_AVATAR: 25 Base Characters Default Half-Body Urban Avatars (<name>_avatar.png) ===
    avatar_specs = [
        ("jasper_avatar", "Jasper", 193, True, "jasper_reference.png", "Jasper Svartr Douglas Bloodmoon, 19yo werewolf college hacker with tousled caramel-chestnut hair, mint-green eyes, faint freckles, subtle smirk, single pair of caramel wolf ears atop head", "Burgundy pullover hoodie with white drawstrings over dark t-shirt", "Sunny Blackwood City upscale coastal avenue outside SUCC university buildings at golden hour, warm sunlit palms and modern glass architecture with shallow depth-of-field bokeh."),
        ("alyssa_avatar", "Alyssa", 155, True, "alyssa_reference.png", "Alyssa Hvit Douglas Bloodmoon, 19yo petite werewolf with long wavy caramel-chestnut hair, vivid mint-green doe eyes, soft freckles, gentle warm smile, single pair of caramel wolf ears atop head", "Sunny sunflower-yellow ruffled crop top, thin gold sunflower necklace, natural warm aesthetic", "Sunlit Blackwood City coastal walkway lined with palm trees, cafes, and Mediterranean stucco facades with warm afternoon bokeh."),
        ("malachia_avatar", "Malachia", 208, True, "malachia_reference.png", "Malachia Bjorn Douglas Bloodmoon, 28yo colossal muscular werewolf matching malachia_anchor.jpg: rich deep sun-kissed bronze-tan skin, shorter thick spiky swept-back jet-black hair, sculpted dark goatee & connected mustache, cold pale amber-grey eyes, vertical scar through left eyebrow into an X-cut left cheek scar, neck/arm Norse ink with wolf head motif, single pair of large dark wolf ears atop head", "Tight matte-black short-sleeve compression t-shirt across massive traps and chest, white boxing hand wraps", "Moody dusk downtown Blackwood City street near an upscale security complex and glowing streetlamps with shallow golden-hour palm bokeh."),
        ("noah_avatar", "Noah", 197, True, "noah_reference.png", "Noah Loki Douglas Bloodmoon, 25yo tall tanned blond werewolf with neatly styled blond hair, sunglasses pushed into hair, bright blue eyes, confident charm, single pair of blond wolf ears atop head", "Tailored crisp white polo shirt unbuttoned at collar, silver wristwatch", "Sunny California coastal boardwalk in Blackwood City with palm silhouettes, beachside cafes, and warm ocean-breeze bokeh."),
        ("erik_avatar", "Erik", 213, True, "erik_reference.png", "Erik Ulfr Douglas, 55yo imposing Prime Alpha patriarch with jet-black hair silvered at temples, piercing amber eyes, trimmed stubble, cheek ritual scar, single pair of black wolf ears atop head", "Tailored dark charcoal Italian linen dress shirt opened at collar showing subtle gold chain", "Glass-and-steel Blackwood City financial district skyline at sunset seen from an executive DCC Tower terrace with warm golden bokeh."),
        ("logan_avatar", "Logan", 198, True, "logan_reference.png", "Logan Jarn Douglas, 49yo rugged biker-mechanic werewolf with black-and-silver hair in a low messy ponytail, observant amber eyes, salt-and-pepper stubble, single pair of black-grey wolf ears atop head", "Worn matte-black leather biker jacket open over dark slate-grey henley shirt", "Evening Solarton / Blackwood City neon mechanic garage alley with warm amber streetlights and brick facades in soft bokeh."),
        ("edric_avatar", "Edric", 165, True, "edric_reference.png", "Edric Douglas, 13yo tall tween werewolf boy with messy black hair over forehead, intense amber eyes, light cheek scars, single pair of black wolf ears atop head", "Battered black leather jacket over dark navy hoodie with white drawstrings", "Twilight suburban Blackwood City sidewalk with streetlights, skatepark rail in distance, and California pines in bokeh."),
        ("wulfnic_avatar", "Wulfnic", 220, True, "wulfnic_reference.png", "Wulfnic Baleygr Bloodmoon, battle-worn 40s-looking Primordial Wolf King with long golden-blonde hair streaked with snow-white and warrior braid, matching blonde-and-white beard, ice-blue eyes, single pair of golden-white wolf ears atop head", "Dark charcoal handwoven wool Norse tunic fastened with wrought-iron brooch and dark wolf-pelt mantle", "Twilight mist-kissed edge where Blackwood City's ancient pine park meets quiet stone architecture in moody atmospheric bokeh."),
        ("magnus_avatar", "Magnus", 205, True, "magnus_reference.png", "Sir Magnus Douglas III, aristocratic werewolf patriarch with combed-back black hair silvered at temples, trimmed silver-threaded beard, calm amber eyes, single pair of dark charcoal wolf ears atop head", "Three-piece slate-grey pinstriped bespoke wool suit, crisp white shirt, deep burgundy silk tie", "Historic Blackwood City Uptown Heritage District boulevard with neoclassical stonework and warm streetlantern bokeh."),
        ("elizabeth_avatar", "Elizabeth", 165, True, "elizabeth_reference.png", "Lady Elizabeth Duskwood, poised werewolf matriarch appearing early 40s with luminous ash-grey updo, serene storm-grey eyes, gentle smile, single pair of ash-grey wolf ears atop head", "Dark forest-green fine cashmere dress, sand-beige wool wrap stole, luminous pearl necklace", "Golden-hour Blackwood City botanical courtyard overlooking elegant limestone townhouses and flowering trellises in soft bokeh."),
        ("ut_avatar", "Ut", 240, True, "ut_reference.png", "Ut Berg, 240cm colossal battle-worn mid-40s Viking werewolf with homogenized wild reddish-auburn hair streaked with iron-grey and matching bushy beard, iron-grey eyes, jagged scars, iron arm rings, single pair of reddish-grey wolf ears", "Oversized red-and-black plaid flannel shirt worn open over earth-brown tank top", "Warm evening Solarton harbor pub district street with glowing shopfronts and industrial brickwork in shallow bokeh."),
        ("zefir_avatar", "Zefir", 192, True, "zefir_reference.png", "Zefir Hvitskog, lean pale Firstborn scout with snow-white punk mohawk, icy washed-out blue eyes, insolent smirk, single pair of pierced snow-white wolf ears atop head", "Sleeveless studded black leather biker vest over distressed black tee", "Neon-lit Solarton underground nightlife alley and SUCC off-campus punk district at night with vivid cyberpunk-city bokeh."),
        ("kaladin_avatar", "Kaladin", 191, True, "kaladin_reference.png", "Major Kaladin Blackwolf Nargathon, weathered tanned werewolf commander matching kaladin_anchor.jpg: long black low ponytail with two front locks framing forehead/temples, vivid emerald-teal eyes, sculpted dark goatee & mustache, brow/cheek scars, single pair of black wolf ears (ZERO horns)", "Charcoal-black tactical combat shirt under matte-black modular ballistic plate carrier with 'DCC SECURITY' patch", "Nighttime Blackwood City DCC Security Perimeter and modern glass-and-concrete corporate plaza under cool cyan/amber city lights in bokeh."),
        ("nixara_avatar", "Nixara", 165, True, "nixara_reference.png", "Nixara Hvit Bloodmoon, radiant werewolf matriarch with voluminous honey-golden wavy hair, warm sky-blue eyes, light freckles, single pair of pure snow-white wolf ears with gold sun-moon earring", "Flowing cream-sand bohemian linen dress with delicate golden embroidery and amber teardrop pendant", "Warm sunlit Blackwood City waterfront promenade beside palms and bright Mediterranean cafes in soft golden bokeh."),
        ("echo_avatar", "Echo", 178, False, "echo_reference.png", "E.C.H.O., Jasper's NON-HUMANOID sentient technomantic AI (strictly ZERO human body/face/limbs) hovering mid-air as a sleek 30 cm hexagonal matte-obsidian & cold-iron magitech recon drone with luminous emerald iris lens", "Autonomous engraved matte-obsidian drone chassis projecting a floating 3D translucent emerald-cyan holographic audio-oscilloscope waveform and runic data rings beside it", "Rain-slicked futuristic Solarton holographic neon night skyline and data-district canyon with glowing emerald-cyan bokeh."),
        ("mac_avatar", "NPC\\Mac", 204, True, "NPC\\Mac\\mac_reference.png", "Mackenzie 'Mac' Sanchez-Rogers, 19yo powerhouse werewolf with shaggy dirty-blonde hair, amber eyes, left cheek/nose scar, golden wolf ears atop head", "Vintage leather jacket worn over dark plaid flannel shirt and graphic tee", "Twilight SUCC indie music district street outside a neon-lit rehearsal venue with string lights in warm bokeh."),
        ("larek_avatar", "NPC\\Larek", 201, False, "NPC\\Larek\\larek_reference.png", "Larek Steeltooth, 21yo muscular olive-green Orc engineering student with jet-black fade, notched lower ivory tusks, amber-gold eyes, tricep clan ink", "Charcoal heavyweight hoodie over olive workwear vest", "Modern SUCC University Computer Engineering quad and concrete brutalist walkways in crisp afternoon urban bokeh."),
        ("zeera_avatar", "NPC\\Zeera", 208, True, "NPC\\Zeera\\zeera_reference.png", "Zeera Darkfire, 208cm dark-bronze Vax Demon CEO with crimson undertones, platinum-ringed black braids, slender carved dark horns, deep amber eyes, pointed ears, nose scar", "Tailored dark charcoal linen dress shirt open at throat with black slacks", "Upscale Blackwood City high-rise penthouse terrace overlooking glittering downtown skyscrapers at night in rich bokeh."),
        ("richard_avatar", "NPC\\Richard_W", 193, True, "NPC\\Richard_W\\richard_reference.png", "Richard Whitlock (Contractor #01), 47yo weathered Lion Shifter knight with cropped grey hair, trimmed beard, light blue eyes, lion ears atop head", "Thick grey cable-knit turtleneck sweater and dark wool coat", "Overcast modern Blackwood City harbor financial street with stone facades and misty city bokeh."),
        ("adam_avatar", "NPC\\Adam", 188, True, "NPC\\Adam\\adam_reference.png", "Adam Valencia (Contractor #02A), 28yo muscular Arctic Wolf Shifter with shoulder-length white hair, pink and blue heterochromatic eyes, white wolf ears atop head", "Dark charcoal heavy pullover hoodie", "Sleek nighttime Blackwood City metro overpass and modern concrete district under cool neon streetlights in bokeh."),
        ("hana_avatar", "NPC\\Hana_V", 180, True, "NPC\\Hana_V\\hana_reference.png", "Hana Valencia (Contractor #02H), 28yo athletic busty Arctic Wolf Shifter with long pure white hair, glowing pink and blue heterochromatic eyes, white wolf ears atop head", "Soft cream off-shoulder knit sweater", "Upscale Blackwood City evening boulevard lined with boutique glass storefronts and warm cafe bokeh."),
        ("luka_avatar", "NPC\\Luka", 193, True, "NPC\\Luka\\luka_reference.png", "Luka Sutter (Contractor #03), 32yo heavily muscled Black Bear Shifter with messy crimson hair, hazel eyes, X-shaped scar across right cheek, rounded black bear ears atop head", "Fitted olive-drab tactical tank top", "Industrial Solarton warehouse security yard at dusk with steel fences and amber floodlights in shallow bokeh."),
        ("dullahan_avatar", "NPC\\Dullahan", 203, False, "NPC\\Dullahan\\dullahan_reference.png", "Dullahan (Contractor #04), 34yo headless muscular werewolf mercenary: dull grey skin, perpetual oversized dark hood pulled forward over swirling black shadow mist where head would be (NO face, NO skull)", "Heavy oversized charcoal hoodie with whistle cord", "Fog-shrouded midnight Blackwood City asphalt viaduct beneath sodium-vapor streetlights in moody bokeh."),
        ("johan_avatar", "NPC\\Johan", 182, True, "NPC\\Johan\\johan_reference.png", "Johan Jakobsen (Contractor #05), 28yo lanky sickly-pale Rat Shifter prodigy with unkempt long black hair, wire-rimmed glasses, sunken dark-circled eyes, brown rat ears atop head", "Mint-green medical lab scrub jacket over dark shirt", "Sterile modern underground SUCC/DDM laboratory corridor with glass partitions and cool fluorescent bokeh."),
        ("fenrir_avatar", "NPC\\Fenrir", 203, False, "NPC\\Fenrir\\fenrir_reference.png", "Fenrir (Contractor #06), 26yo corpse-pale muscular Kingsnake Shifter super-soldier with cropped black hair, sightless milky blind eyes, scarred cheekbones, subtle dark facial scales", "Sleeveless black combat hoodie and white knuckle hand wraps", "Dark rain-wet Blackwood City industrial alleyway lit by distant cool blue security beacons in sharp bokeh."),
    ]
    for eid, folder, h_cm, ears_above, src_ref, c_desc, def_out, urb_bg in avatar_specs:
        add(
            eid,
            "5_AVATAR",
            folder,
            h_cm,
            ears_above,
            None,
            f"{eid.replace('_avatar', '')}_avatar.png",
            neutral_anchors=[src_ref],
            neutral_prompt=build_avatar_prompt(c_desc, def_out, urb_bg),
            asset_kind="default_avatar",
        )

    return entries


def cmd_init_manifest(args: argparse.Namespace) -> None:
    existing_items: dict[str, dict] = {}
    if MANIFEST_PATH.exists():
        try:
            old = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
            existing_items = {x["id"]: x for x in old.get("items", [])}
        except Exception:
            existing_items = {}
    entries = get_manifest_entries(existing_items=existing_items, seed_regen=args.seed_regen)
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(
        json.dumps(
            {
                "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "grid": {"canvas": list(NEUTRAL_SIZE), "floor_y": FLOOR_Y, "px_per_cm": PX_PER_CM},
                "asset_roles": {
                    "reference": "16:9 (2730x1536 RGB #C8C8C8) technical 4-column turnaround sheet (base & 23 hybrid shifter forms)",
                    "neutral_vn_sprite": "2:3 (1696x2528 RGBA transparent, FLOOR_Y=2500, PX_PER_CM=9.75) full-body Visual Novel emotion sprite for Wyvern Sprites section",
                    "default_avatar": "2:3 (1696x2528 RGB) half-body default outfit portrait on cohesive urban background for Wyvern default character/world avatar",
                },
                "items": entries,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    by_wave: dict[str, dict[str, int]] = {}
    for e in entries:
        w = e["wave"]
        d = by_wave.setdefault(w, {"done": 0, "pending": 0, "regen": 0})
        for k in ("reference_status", "neutral_status"):
            st = e[k]
            if st == "DONE":
                d["done"] += 1
            elif st == "PENDING":
                d["pending"] += 1
            elif st == "REGEN_QUEUED":
                d["regen"] += 1
    print(f"Manifest saved to {MANIFEST_PATH} ({len(entries)} entries)")
    for w, counts in sorted(by_wave.items()):
        print(f"  Wave {w}: {counts}")


def load_google_keys_in_memory() -> list[str]:
    keys: list[str] = []
    env_p = ROOT / ".env"
    if env_p.exists():
        env_map: dict[str, str] = {}
        for line in env_p.read_text(encoding="utf-8", errors="ignore").splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k_name, k_val = line.split("=", 1)
                env_map[k_name.strip()] = k_val.strip().strip('"').strip("'")
        for var in ("GOOGLE_IMAGE_API_KEY", "GOOGLE_AI_STUDIO_API_KEY"):
            val = env_map.get(var, "")
            if val and val not in keys:
                keys.append(val)
    cfg_p = ROOT / "proxy" / "config_free_proxy.json"
    if cfg_p.exists():
        cfg = json.loads(cfg_p.read_text(encoding="utf-8"))
        for k in cfg.get("keys", {}).get("google_ai_studio", []) or []:
            if k and k not in keys:
                keys.append(k)
    return keys


def call_gemini_image_api(
    key: str,
    model: str,
    prompt: str,
    aspect_ratio: str,
    anchor_paths: list[pathlib.Path] | None = None,
) -> tuple[int, bytes | None, str]:
    parts: list[dict] = [{"text": prompt}]
    for ap in anchor_paths or []:
        if ap.exists():
            mime = "image/png" if ap.suffix.lower() == ".png" else "image/jpeg"
            b64 = base64.b64encode(ap.read_bytes()).decode("ascii")
            parts.append({"inlineData": {"mimeType": mime, "data": b64}})

    body = {
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {
            "responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {"aspectRatio": aspect_ratio},
        },
    }

    endpoints: list[tuple[str, str]] = []
    if key.startswith("AQ."):
        endpoints.append(("vertex", f"https://aiplatform.googleapis.com/v1/publishers/google/models/{model}:generateContent?key={key}"))
    endpoints.append(("gla", f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"))

    last_code, last_msg = 0, ""
    for ep_name, url in endpoints:
        req = urllib.request.Request(
            url,
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                cparts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
                for p in cparts:
                    if "inlineData" in p and p["inlineData"].get("data"):
                        raw = base64.b64decode(p["inlineData"]["data"])
                        return 200, raw, f"{ep_name}:{p['inlineData'].get('mimeType', 'image/png')}"
                last_code, last_msg = 200, f"{ep_name}:NO_IMAGE_PART: {str(cparts)[:180]}"
        except urllib.error.HTTPError as he:
            err_txt = he.read().decode("utf-8", errors="ignore").replace(key, "<REDACTED>")
            try:
                msg = json.loads(err_txt).get("error", {}).get("message", err_txt)
            except Exception:
                msg = err_txt
            last_code, last_msg = he.code, f"{ep_name}:{str(msg)[:220]}"
        except Exception as exc:
            last_code, last_msg = 0, f"{ep_name}:{type(exc).__name__}: {str(exc)[:180]}"
    return last_code, None, last_msg


def cmd_probe_keys(_: argparse.Namespace) -> None:
    keys = load_google_keys_in_memory()
    print(f"Loaded {len(keys)} unique Google API key(s) in memory.")
    tiny_prompt = "A tiny solid grey circle on a plain white square, minimal flat vector icon."
    working: list[tuple[str, int]] = []
    for model in GEMINI_IMAGE_MODELS:
        for idx, k in enumerate(keys):
            status, raw, info = call_gemini_image_api(k, model, tiny_prompt, "1:1")
            tag = f"IMAGE({len(raw)}B)" if raw else info.replace("\n", " ")[:140]
            print(f"  [{model}][key#{idx}] HTTP {status} -> {tag}")
            if status == 200 and raw:
                working.append((model, idx))
                break
        if working:
            break
    print(f"WORKING_PAIRS={working}")


def resolve_anchor_path(anchor_spec: str) -> pathlib.Path:
    p_refs = REFS_DIR / anchor_spec
    if p_refs.exists():
        return p_refs
    p_assets = ASSETS_DIR / anchor_spec
    if p_assets.exists():
        return p_assets
    return p_refs


def cmd_gen_api(args: argparse.Namespace) -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    item = next((x for x in manifest["items"] if x["id"] == args.id), None)
    if not item:
        raise SystemExit(f"Unknown id: {args.id}")
    if args.kind == "reference":
        prompt = item["reference_prompt"]
        anchors = [resolve_anchor_path(a) for a in item.get("reference_anchors", [])]
        aspect = "16:9"
    else:
        prompt = item["neutral_prompt"]
        anchors = [resolve_anchor_path(a) for a in item.get("neutral_anchors", [])]
        aspect = "2:3"
    if not prompt:
        raise SystemExit(f"No prompt defined for {args.id} ({args.kind})")

    keys = load_google_keys_in_memory()
    models = [args.model] if args.model else GEMINI_IMAGE_MODELS
    for model in models:
        for idx, k in enumerate(keys):
            status, raw, info = call_gemini_image_api(k, model, prompt, aspect, anchors)
            print(f"[gen-api {args.id}:{args.kind}] model={model} key#{idx} -> HTTP {status}")
            if status == 200 and raw:
                out_p = pathlib.Path(args.out)
                out_p.parent.mkdir(parents=True, exist_ok=True)
                out_p.write_bytes(raw)
                print(f"Saved raw output: {out_p} ({len(raw)} B)")
                return
            print(f"  detail: {info}")
    raise SystemExit("All Google API keys/models failed or hit quota.")


def mark_manifest_done(eid: str, kind: str) -> None:
    if not MANIFEST_PATH.exists():
        return
    m = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    for it in m.get("items", []):
        if it["id"] == eid:
            it[f"{kind}_status"] = "DONE"
            m["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
            MANIFEST_PATH.write_text(json.dumps(m, indent=2, ensure_ascii=False), encoding="utf-8")
            return


def finalize_reference_image(src: pathlib.Path, dst: pathlib.Path, mark_id: str | None = None) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("RGB")
    if im.size != REF_SIZE:
        im = im.resize(REF_SIZE, Image.Resampling.LANCZOS)
    im.save(dst, format="PNG", optimize=True)
    if mark_id:
        mark_manifest_done(mark_id, "reference")
    print(f"[FINALIZED REF] {dst} size={im.size} mode={im.mode}")


def flood_fill_white_bg_rgba(im_rgb: Image.Image) -> Image.Image:
    """
    Remove exterior white/near-white background connected to outer edges PLUS enclosed
    pure-white pockets trapped between arms/torso/hair/legs, leaving cel-shaded white
    garments, eyes, teeth, and fur 100% opaque.
    """
    arr = np.array(im_rgb.convert("RGB"), dtype=np.uint8)
    h, w, _ = arr.shape
    r = arr[:, :, 0].astype(np.int16)
    g = arr[:, :, 1].astype(np.int16)
    b = arr[:, :, 2].astype(np.int16)

    cmin = np.minimum(np.minimum(r, g), b)
    cmax = np.maximum(np.maximum(r, g), b)
    sat = cmax - cmin
    lum = 0.299 * r + 0.587 * g + 0.114 * b

    is_bg_seed = (cmin >= 232) & (sat <= 22)
    bg_mask = np.zeros((h, w), dtype=bool)
    q = collections.deque()

    for x in range(w):
        if is_bg_seed[0, x] and not bg_mask[0, x]:
            bg_mask[0, x] = True
            q.append((0, x))
        if is_bg_seed[h - 1, x] and not bg_mask[h - 1, x]:
            bg_mask[h - 1, x] = True
            q.append((h - 1, x))
    for y in range(h):
        if is_bg_seed[y, 0] and not bg_mask[y, 0]:
            bg_mask[y, 0] = True
            q.append((y, 0))
        if is_bg_seed[y, w - 1] and not bg_mask[y, w - 1]:
            bg_mask[y, w - 1] = True
            q.append((y, w - 1))

    while q:
        cy, cx = q.popleft()
        for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
            if 0 <= ny < h and 0 <= nx < w and not bg_mask[ny, nx]:
                if is_bg_seed[ny, nx]:
                    bg_mask[ny, nx] = True
                    q.append((ny, nx))

    fg_ys = np.where(~bg_mask)[0]
    y_fg_top = int(fg_ys.min()) if len(fg_ys) else 0
    fg_h = (int(fg_ys.max()) - y_fg_top + 1) if len(fg_ys) else h
    face_protect_y = y_fg_top + int(0.14 * fg_h)

    pure_pocket = (cmin >= 248) & (sat <= 6) & (~bg_mask)
    visited_p = np.zeros((h, w), dtype=bool)
    pocket_seeds: list[tuple[int, int]] = []
    for y in range(h):
        for x in range(w):
            if pure_pocket[y, x] and not visited_p[y, x]:
                pq = collections.deque([(y, x)])
                visited_p[y, x] = True
                pts: list[tuple[int, int]] = []
                while pq:
                    cy, cx = pq.popleft()
                    pts.append((cy, cx))
                    for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                        if 0 <= ny < h and 0 <= nx < w and not visited_p[ny, nx] and pure_pocket[ny, nx]:
                            visited_p[ny, nx] = True
                            pq.append((ny, nx))
                ys_p = [p[0] for p in pts]
                xs_p = [p[1] for p in pts]
                min_y_p = min(ys_p)
                min_pts = 45 if min_y_p > face_protect_y else 120
                if len(pts) >= min_pts and float(cmin[ys_p, xs_p].mean()) >= 251.5:
                    pocket_seeds.extend(pts)

    if pocket_seeds:
        pq2 = collections.deque()
        for py, px in pocket_seeds:
            if not bg_mask[py, px]:
                bg_mask[py, px] = True
                pq2.append((py, px))
        while pq2:
            cy, cx = pq2.popleft()
            for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                if 0 <= ny < h and 0 <= nx < w and not bg_mask[ny, nx]:
                    if is_bg_seed[ny, nx]:
                        bg_mask[ny, nx] = True
                        pq2.append((ny, nx))

    fringe = np.zeros((h, w), dtype=bool)
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        shifted = np.zeros((h, w), dtype=bool)
        sy0, sy1 = max(0, -dy), min(h, h - dy)
        sx0, sx1 = max(0, -dx), min(w, w - dx)
        shifted[sy0 + dy : sy1 + dy, sx0 + dx : sx1 + dx] = bg_mask[sy0:sy1, sx0:sx1]
        fringe |= shifted
    fringe &= (~bg_mask) & (lum >= 185) & (sat <= 35)
    bg_total = bg_mask | fringe

    alpha_hard = np.where(bg_total, 0, 255).astype(np.uint8)
    alpha_img = Image.fromarray(alpha_hard, mode="L")
    alpha_blur = alpha_img.filter(ImageFilter.GaussianBlur(radius=0.8))
    blur_arr = np.array(alpha_blur, dtype=np.uint8)
    alpha_final = np.where(bg_total, np.minimum(alpha_hard, blur_arr), np.where(blur_arr < 250, blur_arr, 255)).astype(np.uint8)
    alpha_final[bg_mask] = 0

    rgba = np.zeros((h, w, 4), dtype=np.uint8)
    rgba[:, :, :3] = arr
    rgba[:, :, 3] = alpha_final
    rgba[alpha_final == 0] = [255, 255, 255, 0]
    return Image.fromarray(rgba, mode="RGBA")


def detect_crown_and_sole(alpha_arr: np.ndarray, has_ears_above_crown: bool) -> tuple[int, int, int]:
    """
    Return (y_ear_tip, y_crown, y_sole) in pixel coordinates of the cropped silhouette.
    When has_ears_above_crown is True, measure the cranial/hair crown between the two wolf ears
    so tall/short ear tips never distort canonical stature in cm.
    """
    h, w = alpha_arr.shape
    ys, xs = np.where(alpha_arr > 15)
    if len(ys) == 0:
        raise RuntimeError("Alpha channel contains no foreground pixels.")
    y_ear_tip = int(ys.min())
    y_sole = int(ys.max())
    raw_h = y_sole - y_ear_tip

    if not has_ears_above_crown:
        return y_ear_tip, y_ear_tip, y_sole

    head_mask = ys <= (y_ear_tip + int(0.18 * raw_h))
    head_xs = xs[head_mask]
    hx_mid = int(np.median(head_xs))
    strip = alpha_arr[:, max(0, hx_mid - 14) : min(w, hx_mid + 15)] > 15
    strip_ys = np.where(strip)[0]
    if len(strip_ys) == 0:
        y_crown = y_ear_tip + int(0.03 * raw_h)
    else:
        raw_crown = int(strip_ys.min())
        delta = max(int(0.018 * raw_h), min(int(0.065 * raw_h), raw_crown - y_ear_tip))
        y_crown = y_ear_tip + delta
    return y_ear_tip, y_crown, y_sole


def place_rgba_on_height_grid(rgba_im: Image.Image, height_cm: float, has_ears_above_crown: bool) -> Image.Image:
    """Isotropically scale and place an RGBA figure onto (1696, 2528) at FLOOR_Y=2500 with PX_PER_CM=9.75."""
    arr = np.array(rgba_im.convert("RGBA"))
    alpha = arr[:, :, 3]
    ys, xs = np.where(alpha > 15)
    if len(ys) == 0:
        raise RuntimeError("Matting left zero foreground pixels.")

    x0, x1 = int(xs.min()), int(xs.max())
    y0, y1 = int(ys.min()), int(ys.max())
    crop = rgba_im.crop((x0, y0, x1 + 1, y1 + 1))
    c_alpha = np.array(crop)[:, :, 3]
    _, y_crown_rel, y_sole_rel = detect_crown_and_sole(c_alpha, has_ears_above_crown)

    crown_to_sole_src = max(1, y_sole_rel - y_crown_rel)
    target_crown_to_sole = float(height_cm) * PX_PER_CM
    scale = target_crown_to_sole / crown_to_sole_src

    # Clamp horizontally only if extraordinarily wide (should never trigger for standing poses)
    max_w = NEUTRAL_SIZE[0] - 80
    if crop.width * scale > max_w:
        scale = max_w / crop.width

    nw = max(1, int(round(crop.width * scale)))
    nh = max(1, int(round(crop.height * scale)))
    resized = crop.resize((nw, nh), Image.Resampling.LANCZOS)

    sole_in_resized = int(round(y_sole_rel * scale))
    py = FLOOR_Y - sole_in_resized
    if py < 8:
        py = max(0, FLOOR_Y - nh)
    px = (NEUTRAL_SIZE[0] - nw) // 2

    canvas = Image.new("RGBA", NEUTRAL_SIZE, (255, 255, 255, 0))
    canvas.paste(resized, (px, py), resized)
    c_arr = np.array(canvas)
    c_arr[c_arr[:, :, 3] == 0] = [255, 255, 255, 0]
    return Image.fromarray(c_arr, mode="RGBA")


def lookup_height_spec(eid: str | None, height_cm: float | None, no_ears_above: bool) -> tuple[float, bool]:
    if height_cm is not None:
        return float(height_cm), not no_ears_above
    if eid:
        items = get_manifest_entries()
        it = next((x for x in items if x["id"] == eid), None)
        if it:
            return float(it["height_cm"]), bool(it["has_ears_above_crown"])
    raise SystemExit("Provide --id <item_id> or --height-cm <cm> for shared height grid scaling.")


def place_floating_rgba_on_canvas(rgba_im: Image.Image) -> Image.Image:
    """Center a floating non-humanoid drone/hologram RGBA sprite inside (1696, 2528) at eye/shoulder hover height."""
    arr = np.array(rgba_im.convert("RGBA"))
    ys, xs = np.where(arr[:, :, 3] > 15)
    if len(ys) == 0:
        raise RuntimeError("Matting left zero foreground pixels.")
    crop = rgba_im.crop((int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1))
    max_w, max_h = 980, 980
    scale = min(max_w / crop.width, max_h / crop.height)
    nw, nh = max(1, int(round(crop.width * scale))), max(1, int(round(crop.height * scale)))
    resized = crop.resize((nw, nh), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", NEUTRAL_SIZE, (255, 255, 255, 0))
    px = (NEUTRAL_SIZE[0] - nw) // 2
    py = max(180, 1180 - nh // 2)
    canvas.paste(resized, (px, py), resized)
    c_arr = np.array(canvas)
    c_arr[c_arr[:, :, 3] == 0] = [255, 255, 255, 0]
    return Image.fromarray(c_arr, mode="RGBA")


def finalize_neutral_image(
    src: pathlib.Path,
    dst: pathlib.Path,
    height_cm: float,
    has_ears_above_crown: bool,
    already_rgba: bool = False,
    mark_id: str | None = None,
    floating: bool = False,
) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    im_raw = Image.open(src)
    if already_rgba and im_raw.mode == "RGBA":
        rgba = im_raw
    else:
        rgba = flood_fill_white_bg_rgba(im_raw.convert("RGB"))

    if floating or mark_id == "echo":
        out_im = place_floating_rgba_on_canvas(rgba)
        out_im.save(dst, format="PNG", optimize=True)
        if mark_id:
            mark_manifest_done(mark_id, "neutral")
        print(f"[FINALIZED FLOATING SPRITE] {dst.name} size={out_im.size} corner={out_im.getpixel((5,5))}")
        return

    out_im = place_rgba_on_height_grid(rgba, height_cm, has_ears_above_crown)
    out_im.save(dst, format="PNG", optimize=True)
    if mark_id:
        mark_manifest_done(mark_id, "neutral")

    c_arr = np.array(out_im)
    y_ear, y_crown, y_sole = detect_crown_and_sole(c_arr[:, :, 3], has_ears_above_crown)
    eff_cm = (y_sole - y_crown) / PX_PER_CM
    print(
        f"[FINALIZED NEUTRAL] {dst.name} target={height_cm:.0f}cm eff={eff_cm:.1f}cm "
        f"(ear={y_ear}, crown={y_crown}, sole={y_sole}) corner={out_im.getpixel((5,5))}"
    )


def finalize_avatar_image(src: pathlib.Path, dst: pathlib.Path, mark_id: str | None = None) -> None:
    """Save 2:3 half-body default urban avatar to (1696, 2528) RGB PNG without background stripping."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("RGB")
    if im.size != NEUTRAL_SIZE:
        im = im.resize(NEUTRAL_SIZE, Image.Resampling.LANCZOS)
    im.save(dst, format="PNG", optimize=True)
    if mark_id:
        mark_manifest_done(mark_id, "neutral")
    print(f"[FINALIZED AVATAR] {dst} size={im.size} mode={im.mode}")


def strip_studio_grey_to_rgba(im_rgb: Image.Image) -> Image.Image:
    """Strip uniform neutral grey (#C8C8C8) studio background from VISTA FRONTALE crop to clean RGBA."""
    arr = np.array(im_rgb.convert("RGB"), dtype=np.int16)
    h, w, _ = arr.shape
    # Sample outer edge median studio grey
    edge_samples = np.vstack([arr[0:10, :].reshape(-1, 3), arr[:, 0:10].reshape(-1, 3), arr[:, w - 10 : w].reshape(-1, 3)])
    bg = np.median(edge_samples, axis=0)
    dist = np.abs(arr - bg).max(axis=2)
    sat = arr.max(axis=2) - arr.min(axis=2)
    is_bg = (dist <= 26) & (sat <= 18)

    bg_mask = np.zeros((h, w), dtype=bool)
    q = collections.deque()
    for x in range(w):
        for y in (0, h - 1):
            if is_bg[y, x] and not bg_mask[y, x]:
                bg_mask[y, x] = True
                q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if is_bg[y, x] and not bg_mask[y, x]:
                bg_mask[y, x] = True
                q.append((y, x))
    while q:
        cy, cx = q.popleft()
        for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
            if 0 <= ny < h and 0 <= nx < w and not bg_mask[ny, nx] and is_bg[ny, nx]:
                bg_mask[ny, nx] = True
                q.append((ny, nx))

    # Enclosed studio-grey pockets between arms/torso/legs
    pure_grey = (dist <= 16) & (sat <= 12) & (~bg_mask)
    visited = np.zeros((h, w), dtype=bool)
    fg_ys = np.where(~bg_mask)[0]
    y_top = int(fg_ys.min()) if len(fg_ys) else 0
    fg_h = (int(fg_ys.max()) - y_top + 1) if len(fg_ys) else h
    face_protect_y = y_top + int(0.14 * fg_h)
    seeds: list[tuple[int, int]] = []
    for y in range(h):
        for x in range(w):
            if pure_grey[y, x] and not visited[y, x]:
                pq = collections.deque([(y, x)])
                visited[y, x] = True
                pts = []
                while pq:
                    cy, cx = pq.popleft()
                    pts.append((cy, cx))
                    for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                        if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx] and pure_grey[ny, nx]:
                            visited[ny, nx] = True
                            pq.append((ny, nx))
                min_y_p = min(p[0] for p in pts)
                if len(pts) >= (45 if min_y_p > face_protect_y else 120):
                    seeds.extend(pts)
    if seeds:
        pq2 = collections.deque()
        for py, px in seeds:
            if not bg_mask[py, px]:
                bg_mask[py, px] = True
                pq2.append((py, px))
        while pq2:
            cy, cx = pq2.popleft()
            for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                if 0 <= ny < h and 0 <= nx < w and not bg_mask[ny, nx] and is_bg[ny, nx]:
                    bg_mask[ny, nx] = True
                    pq2.append((ny, nx))

    alpha = np.where(bg_mask, 0, 255).astype(np.uint8)
    rgba = np.zeros((h, w, 4), dtype=np.uint8)
    rgba[:, :, :3] = arr.astype(np.uint8)
    rgba[:, :, 3] = alpha
    rgba[bg_mask] = [255, 255, 255, 0]
    return Image.fromarray(rgba, mode="RGBA")


def cmd_prep_front_anchors(_: argparse.Namespace) -> None:
    REFS_DIR.mkdir(parents=True, exist_ok=True)
    items = get_manifest_entries()
    count = 0
    for it in items:
        if it.get("asset_kind", "character") != "character" or it.get("id") == "echo":
            continue
        rp = it["reference_path"]
        if not rp or not pathlib.Path(rp).exists():
            continue
        im = Image.open(rp).convert("RGB")
        # Crop strictly VISTA FRONTALE column (exclude header above y=102 and 45-deg view right of x=715)
        crop = im.crop((75, 102, 715, 1525))
        rgba = strip_studio_grey_to_rgba(crop)

        # 1) Save real-height-grid anchor (<id>_front_2x3.png) for height chart calibration
        grid_rgba = place_rgba_on_height_grid(rgba, float(it["height_cm"]), bool(it["has_ears_above_crown"]))
        white_bg = Image.new("RGB", NEUTRAL_SIZE, (255, 255, 255))
        white_bg.paste(grid_rgba, (0, 0), grid_rgba)
        out_p = REFS_DIR / f"{it['id']}_front_2x3.png"
        white_bg.save(out_p, format="PNG")

        # 2) Save high-res 90%-height body-only anchor (<id>_body_2x3.png) preserving 1:1 aspect ratio
        # so image-generator draws every character at maximum sharpness before finalize-neutral scales to cm.
        c_arr_raw = np.array(rgba)[:, :, 3]
        ry, rx = np.where(c_arr_raw > 15)
        tight = rgba.crop((int(rx.min()), int(ry.min()), int(rx.max()) + 1, int(ry.max()) + 1))
        target_h_body = int(round(NEUTRAL_SIZE[1] * 0.90))  # ~2275 px
        scale_b = min((NEUTRAL_SIZE[0] - 120) / tight.width, target_h_body / tight.height)
        bw, bh = max(1, int(round(tight.width * scale_b))), max(1, int(round(tight.height * scale_b)))
        tight_res = tight.resize((bw, bh), Image.Resampling.LANCZOS)
        body_canvas = Image.new("RGB", NEUTRAL_SIZE, (255, 255, 255))
        bx = (NEUTRAL_SIZE[0] - bw) // 2
        by = (NEUTRAL_SIZE[1] - bh) // 2
        body_canvas.paste(tight_res, (bx, by), tight_res)
        body_p = REFS_DIR / f"{it['id']}_body_2x3.png"
        body_canvas.save(body_p, format="PNG")

        c_arr = np.array(grid_rgba)[:, :, 3]
        y_ear, y_crown, y_sole = detect_crown_and_sole(c_arr, bool(it["has_ears_above_crown"]))
        print(
            f"[ANCHOR 2:3] {body_p.name} (body {bw}x{bh}) & {out_p.name} ({it['height_cm']}cm) -> "
            f"ear={y_ear}, crown={y_crown}, sole={y_sole}, eff={(y_sole-y_crown)/PX_PER_CM:.1f}cm"
        )
        count += 1
    print(f"Prepared {count} clean 2:3 VISTA FRONTALE & body anchors in {REFS_DIR}")


def cmd_build_audit_sheet(args: argparse.Namespace) -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    items = [x for x in manifest["items"] if x["wave"].upper() == args.wave.upper()]
    tiles: list[tuple[str, pathlib.Path, bool]] = []
    for it in items:
        if args.kind in ("reference", "both") and it["reference_path"]:
            p = pathlib.Path(it["reference_path"])
            if p.exists():
                tiles.append((f"{it['id']} REF", p, False))
        if args.kind in ("neutral", "both") and it.get("neutral_path"):
            p = pathlib.Path(it["neutral_path"])
            if p.exists():
                is_rgba_vn = it.get("asset_kind", "character") == "character"
                lbl = f"{it['id']} AVATAR" if not is_rgba_vn else f"{it['id']} NEUTRAL"
                tiles.append((lbl, p, is_rgba_vn))
    if not tiles:
        raise SystemExit(f"No completed tiles found for wave={args.wave} kind={args.kind}")

    is_ref_only = all(not is_neu for _, _, is_neu in tiles)
    tw, th = (640, 360) if is_ref_only else (424, 632)
    cols = 2 if is_ref_only else 4
    rows = (len(tiles) + cols - 1) // cols
    pad = 24
    sheet = Image.new("RGB", (cols * (tw + pad) + pad, rows * (th + pad + 26) + pad), (24, 24, 28))
    draw = ImageDraw.Draw(sheet)

    checker = Image.new("RGB", (tw, th), (42, 42, 46))
    cdraw = ImageDraw.Draw(checker)
    sq = 24
    for y in range(0, th, sq):
        for x in range(0, tw, sq):
            if ((x // sq) + (y // sq)) % 2 == 1:
                cdraw.rectangle([x, y, x + sq - 1, y + sq - 1], fill=(58, 58, 64))

    for idx, (label, path, is_neu) in enumerate(tiles):
        r, c = idx // cols, idx % cols
        ox = pad + c * (tw + pad)
        oy = pad + r * (th + pad + 26)
        im = Image.open(path)
        draw.text((ox, oy), f"{label} ({im.size[0]}x{im.size[1]} {im.mode})", fill=(235, 235, 240))
        if is_neu and im.mode == "RGBA":
            bg = checker.copy()
            fg = im.resize((tw, th), Image.Resampling.LANCZOS)
            bg.paste(fg, (0, 0), fg)
            sheet.paste(bg, (ox, oy + 20))
        else:
            fg = im.convert("RGB").resize((tw, th), Image.Resampling.LANCZOS)
            sheet.paste(fg, (ox, oy + 20))

    out_p = pathlib.Path(args.out)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_p, format="JPEG", quality=92)
    print(f"Saved audit sheet ({len(tiles)} tiles) -> {out_p}")


def cmd_build_height_chart(args: argparse.Namespace) -> None:
    items_map = {x["id"]: x for x in get_manifest_entries()}
    ids = [s.strip() for s in args.ids.split(",") if s.strip()]
    if not ids:
        raise SystemExit("Provide --ids comma list")

    scale_vis = 0.48
    chart_h = int(round(NEUTRAL_SIZE[1] * scale_vis))
    slot_w = 270
    left_pad = 95
    right_pad = 45
    chart_w = left_pad + len(ids) * slot_w + right_pad

    canvas = Image.new("RGB", (chart_w, chart_h), (24, 26, 32))
    draw = ImageDraw.Draw(canvas)

    # Graduated cm grid (0..250 cm every 10 cm, floor at FLOOR_Y * scale_vis)
    for cm in range(0, 251, 10):
        y = int(round((FLOOR_Y - cm * PX_PER_CM) * scale_vis))
        if 10 <= y <= chart_h - 5:
            is_major = (cm % 20 == 0)
            col = (72, 76, 88) if is_major else (42, 45, 54)
            if cm == 0:
                col = (190, 90, 80)
            draw.line([(left_pad - 12, y), (chart_w - right_pad + 10, y)], fill=col, width=1)
            if is_major:
                draw.text((14, y - 6), f"{cm:3d} cm", fill=(185, 190, 205))

    palette = [
        (235, 145, 160), (140, 185, 240), (130, 210, 195), (175, 215, 130),
        (230, 180, 120), (210, 145, 225), (160, 165, 245), (225, 225, 235),
    ]

    for idx, eid in enumerate(ids):
        it = items_map[eid]
        cm = int(it["height_cm"])
        ears_above = bool(it["has_ears_above_crown"])

        # Allow Jasper neutral sprite to be compared cleanly even when source=front_anchors
        if args.source == "neutrals" or (args.include_jasper_neutral and eid == "jasper"):
            p = pathlib.Path(it["neutral_path"])
            im = Image.open(p).convert("RGBA")
        else:
            fp = REFS_DIR / f"{eid}_front_2x3.png"
            im_rgb = Image.open(fp).convert("RGB")
            im = flood_fill_white_bg_rgba(im_rgb)

        arr = np.array(im)[:, :, 3]
        ys, xs = np.where(arr > 15)
        x0, x1 = int(xs.min()), int(xs.max())
        y0, y1 = int(ys.min()), int(ys.max())
        crop = im.crop((x0, y0, x1 + 1, y1 + 1))
        nw = max(1, int(round(crop.width * scale_vis)))
        nh = max(1, int(round(crop.height * scale_vis)))
        res = crop.resize((nw, nh), Image.Resampling.LANCZOS)

        px = left_pad + idx * slot_w + (slot_w - nw) // 2
        py = int(round(y0 * scale_vis))
        canvas.paste(res, (px, py), res)

        # Draw exact crown marker line for character's canonical cm height
        crown_y = int(round((FLOOR_Y - cm * PX_PER_CM) * scale_vis))
        c_col = palette[idx % len(palette)]
        lx0 = left_pad + idx * slot_w + 18
        lx1 = left_pad + (idx + 1) * slot_w - 18
        draw.line([(lx0, crown_y), (lx1, crown_y)], fill=c_col, width=2)
        label_y = max(8, int(round(y0 * scale_vis)) - 30)
        draw.text((lx0 + 10, label_y), f"{eid.capitalize()} {cm} cm", fill=c_col)

    out_p = pathlib.Path(args.out)
    out_p.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_p, format="JPEG", quality=93)
    print(f"Saved graduated height comparison chart ({len(ids)} chars) -> {out_p}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init-manifest")
    p_init.add_argument("--seed-regen", action="store_true")

    sub.add_parser("probe-keys")
    sub.add_parser("prep-front-anchors")

    p_gen = sub.add_parser("gen-api")
    p_gen.add_argument("--id", required=True)
    p_gen.add_argument("--kind", choices=["reference", "neutral"], required=True)
    p_gen.add_argument("--out", required=True)
    p_gen.add_argument("--model", default=None)

    p_ref = sub.add_parser("finalize-reference")
    p_ref.add_argument("--src", required=True)
    p_ref.add_argument("--dst", required=True)
    p_ref.add_argument("--mark-done", default=None)

    p_neu = sub.add_parser("finalize-neutral")
    p_neu.add_argument("--src", required=True)
    p_neu.add_argument("--dst", required=True)
    p_neu.add_argument("--id", default=None)
    p_neu.add_argument("--height-cm", type=float, default=None)
    p_neu.add_argument("--no-ears-above-crown", action="store_true")
    p_neu.add_argument("--already-rgba", action="store_true")
    p_neu.add_argument("--mark-done", action="store_true")

    p_av = sub.add_parser("finalize-avatar")
    p_av.add_argument("--src", required=True)
    p_av.add_argument("--dst", required=True)
    p_av.add_argument("--mark-done", default=None)

    p_aud = sub.add_parser("build-audit-sheet")
    p_aud.add_argument("--wave", required=True)
    p_aud.add_argument("--kind", choices=["reference", "neutral", "both"], default="both")
    p_aud.add_argument("--out", required=True)

    p_hgt = sub.add_parser("build-height-chart")
    p_hgt.add_argument("--ids", required=True)
    p_hgt.add_argument("--source", choices=["front_anchors", "neutrals"], default="front_anchors")
    p_hgt.add_argument("--include-jasper-neutral", action="store_true")
    p_hgt.add_argument("--out", required=True)

    args = ap.parse_args()
    if args.cmd == "init-manifest":
        cmd_init_manifest(args)
    elif args.cmd == "probe-keys":
        cmd_probe_keys(args)
    elif args.cmd == "prep-front-anchors":
        cmd_prep_front_anchors(args)
    elif args.cmd == "gen-api":
        cmd_gen_api(args)
    elif args.cmd == "finalize-reference":
        finalize_reference_image(pathlib.Path(args.src), pathlib.Path(args.dst), mark_id=args.mark_done)
    elif args.cmd == "finalize-neutral":
        h_cm, ears_above = lookup_height_spec(args.id, args.height_cm, args.no_ears_above_crown)
        finalize_neutral_image(
            pathlib.Path(args.src),
            pathlib.Path(args.dst),
            height_cm=h_cm,
            has_ears_above_crown=ears_above,
            already_rgba=args.already_rgba,
            mark_id=(args.id if args.mark_done and args.id else None),
        )
    elif args.cmd == "finalize-avatar":
        finalize_avatar_image(pathlib.Path(args.src), pathlib.Path(args.dst), mark_id=args.mark_done)
    elif args.cmd == "build-audit-sheet":
        cmd_build_audit_sheet(args)
    elif args.cmd == "build-height-chart":
        cmd_build_height_chart(args)


if __name__ == "__main__":
    main()

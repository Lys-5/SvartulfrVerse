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
    ("wulfnic", "neutral"),
    ("ut", "reference"),
    ("kaladin", "reference"),
}

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
        neutral_file: str,
        ref_prompt: str | None = None,
        neutral_prompt: str | None = None,
        ref_anchors: list[str] | None = None,
        neutral_anchors: list[str] | None = None,
    ) -> None:
        ref_path = str(ASSETS_DIR / folder / ref_file) if ref_file else None
        neu_path = str(ASSETS_DIR / folder / neutral_file)
        entries.append(
            {
                "id": eid,
                "wave": wave,
                "folder": folder,
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
        neutral_anchors=["alyssa_front_2x3.png", "alyssa_casual_anchor.png"],
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
        neutral_anchors=["malachia_front_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Malachia Bjorn Douglas Bloodmoon, 28-year-old colossal 208 cm male werewolf with a massive bulky heavyweight-boxer build, thick neck, very broad heavy shoulders, long powerful legs, "
            "medium-length black windswept hair framing his temples and single pair of black wolf ears atop his head (no human ears), cold unblinking amber eyes, "
            "crooked slightly broken boxer nose, faded scar through his left eyebrow, short stubble, stoic severe resting expression, "
            "extensive dark Norse-tribal Bloodmoon blackwork tattoos climbing his neck and both massive muscular arms, dark Thurisaz & Fenris rune brand on his inner left wrist, "
            "and a thick dark black bushy wolf tail behind his legs.",
            "Athletic combat-casual streetwear: tight short-sleeved matte-black compression t-shirt stretched across his massive chest and shoulders (tucked cleanly at natural waist height to preserve leg length and expose tattooed forearms), "
            "fitted dark charcoal-grey athletic cargo sweatpants sitting at natural hip/waist height with straight tailored legs (NO dropped crotch) and a rear tail opening, "
            "white athletic boxing hand wraps around his knuckles/hands (leaving the inner left wrist rune visible), and sturdy black high-top athletic combat sneakers.",
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
        neutral_anchors=["noah_front_2x3.png"],
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
        neutral_anchors=["erik_front_2x3.png"],
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
        neutral_anchors=["logan_front_2x3.png"],
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
        neutral_anchors=["edric_front_2x3.png"],
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
        neutral_anchors=["wulfnic_front_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Wulfnic Baleygr Bloodmoon, 1200-year-old Primordial Firstborn werewolf demigod appearing as a colossal 220 cm weathered Viking warrior in his late 50s with tall imposing long-legged heroic stature, "
            "long silver-white hair with a thick braided warrior lock draping over his left shoulder, full silver-white Viking beard and mustache, piercing ice-blue eyes, "
            "weathered battle scars across his brow and nose, single pair of large silver-white wolf ears with warm cream interior atop his head (no human ears), "
            "ancient Svartulfr Norse tattoos on his forearms, dark Jera & Fenris rune on his inner left wrist, and a majestic bushy silver-white-and-cream wolf tail behind his legs.",
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
        neutral_anchors=["magnus_front_2x3.png"],
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
        neutral_anchors=["elizabeth_front_2x3.png", "elizabeth_anchor.jpg"],
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
            identity="Ut Berg (The Mountain), 1205-year-old Primordial Firstborn Werewolf Berserker",
            tail_attach="heavy ash-brown wolf tail emerging from the lower spine",
            ear_summary="single pair of steel-grey wolf ears",
            subtitle="LAGUZ & FENRIS • IRON ARM RINGS • BATTLE SCARS",
            box1_desc="Macro thick inner left wrist showing the Laguz (ᛚ) and Fenris rune tattoo in dark cold-iron ink",
            box1_cap="LAGUZ & FENRIS RUNE",
            box2_desc="Macro massive forearm wearing heavy hammered dark iron Viking arm rings",
            box2_cap="FORGED IRON ARM RINGS",
            box3_desc="Macro rugged weathered torso crisscrossed by thick jagged axe and fang scars and ancient Norse ink",
            box3_cap="ANCIENT BATTLE SCARS",
            build="Colossal 240 cm barrel-chested walking mountain of granite muscle, tree-trunk limbs, thick shoulders and forearms, coarse body hair.",
            face="Rugged primeval Viking features largely framed by a wild bushy red-blonde beard across ALL four views, heavy iron-grey eyes, gruff fearless presence.",
            hair="Wild, thick unkempt steel-grey hair reaching past the collar.",
            anatomy="CRITICAL: Single pair of large weathered steel-grey wolf ears MUST be clearly visible atop his head in ALL FOUR views (VISTA FRONTALE, 45°, LATERALE, and DETTAGLIO VOLTO), plus a massive heavy ash-brown wolf tail. STRICTLY NO HUMAN EARS on the sides of the head; zero leg tattoos.",
            outfit="Minimalist matte black photography-studio underwear (fitted black boxer briefs), barefoot.",
            marks="Laguz (ᛚ) + Fenris protection brand on inner left wrist; heavy hammered iron arm rings; archaic Norse runes and thick jagged battle scars across chest and arms ONLY (clean scarred skin on legs).",
        ),
        neutral_anchors=["ut_front_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Ut Berg (The Mountain), 240 cm colossal barrel-chested Primordial Firstborn werewolf giant appearing 60, wild unkempt steel-grey hair, "
            "massive bushy red-blonde Viking beard, iron-grey eyes, archaic Norse tattoos and thick scars across forearms and chest, heavy iron arm rings, "
            "single pair of steel-grey wolf ears atop his head (no human ears), and a thick heavy ash-brown wolf tail behind his legs.",
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
        neutral_anchors=["zefir_front_2x3.png", "zefir_anchor.jpg"],
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
        ref_anchors=["malachia_reference.png"],
        ref_prompt=MASTER_REF_TEMPLATE.format(
            identity="Major Kaladin Blackwolf Nargathon (Subject Zero), 45-year-old military-engineered Alpha Werewolf Commander",
            tail_attach="thick mutated black wolf tail emerging from the lower spine",
            ear_summary="single pair of sharp black wolf ears",
            subtitle="NEURAL CAGE SCARS • GAMMA-7 DOG TAGS • BLACKWOLF SCARS",
            box1_desc="Macro close-up of nape of neck showing faint dark cold-iron neural restraint surgical scars beneath buzzed hair",
            box1_cap="NEURAL CAGE SCARS (NAPE)",
            box2_desc="Macro close-up of matte-black military dog tags stamped 'GAMMA-7 / SUBJECT ZERO' resting on scarred collarbone",
            box2_cap="GAMMA-7 DOG TAGS",
            box3_desc="Macro close-up of chest and shoulder showing crisp tactical knife and claw combat scars",
            box3_cap="BLACKWOLF COMBAT SCARS",
            build="191 cm (6'3\") dense functional commando musculature, broad squared shoulders, low body fat, scarred warrior frame.",
            face="Hard stoic military features, flat assessing pale-grey eyes, short neat dark beard and mustache, thin scar across brow and cheek, zero horns.",
            hair="Dark jet-black hair buzzed short on top with slightly longer tousled side-swept temple hair covering the sides of the head smoothly.",
            anatomy="Werewolf ONLY (STRICTLY NO HORNS, NO DEMON HORNS): single pair of sharp black wolf ears atop his head, and a thick powerful black wolf tail. Smooth side hair covers the temples completely with ZERO human ears visible on the sides of the head in any view.",
            outfit="Minimalist matte black photography-studio underwear (fitted black boxer briefs), barefoot.",
            marks="Cold-iron surgical scars at the nape of the neck; Gamma-7 military dog tags; heavy combat scars across chest, arms, and brow.",
        ),
        neutral_anchors=["kaladin_front_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "Major Kaladin Blackwolf Nargathon, 45-year-old 191 cm military-engineered werewolf commander (STRICTLY NO HORNS), dense functional commando musculature, "
            "short regulation dark jet-black hair covering the temples smoothly with ZERO human ears on the sides, pale assessing icy-grey eyes, trimmed dark beard, thin brow and cheek scars, "
            "single pair of sharp black wolf ears atop his head, and a thick black wolf tail behind his legs.",
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
        neutral_anchors=["nixara_front_2x3.png", "nixara_anchor.jpg"],
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
        ref_prompt=MASTER_REF_TEMPLATE.format(
            identity="E.C.H.O. (Electronic Counter-measures & Heuristic Operative), Sentient Technomantic AI Construct Avatar (Non-Human Digital Familiar)",
            tail_attach="floating emerald-cyan data ribbon trailing from the back",
            ear_summary="androgynous translucent hologram head and optical visor core",
            subtitle="HOLO-WAVE INTERFACE • MAGITECH HEX-DRONE • OPTICAL CORE",
            box1_desc="Macro close-up of glowing emerald-cyan 3D oscilloscope audio wave floating in dark translucent glass",
            box1_cap="HOLO-WAVE OSCILLOSCOPE",
            box2_desc="Macro close-up of a sleek 30 cm matte-obsidian and cold-iron hexagonal magitech recon micro-drone with emerald sensor eye",
            box2_cap="MAGITECH HEX-DRONE (30CM)",
            box3_desc="Macro close-up of glowing emerald technomantic geometric iris optical core framed by circuit filigree",
            box3_cap="EMERALD OPTICAL CORE",
            build="178 cm slender weightless androgynous digital-entity silhouette formed of translucent emerald-cyan hard-light wireframe and sleek matte-obsidian geometric armor plates (zero human flesh, synthetic cyber-construct).",
            face="Sleek smooth porcelain-obsidian faceplate with a glowing emerald-green technomantic optical core eye/visor, calm deadpan expression.",
            hair="Swept back volumetric emerald-cyan holographic light filaments and data-crest geometry.",
            anatomy="Non-human AI construct: sleek articulated matte-obsidian chassis fused with glowing cyan-emerald circuit conduits and floating geometric halo nodes. Zero human ears.",
            outfit="Integrated seamless dark obsidian and glowing emerald-cyan cybernetic bodysuit plating (part of the construct chassis).",
            marks="Glowing runic technomancy circuit sigils etched in cyan-emerald light across chest core and forearms.",
        ),
        neutral_anchors=["echo_front_2x3.png"],
        neutral_prompt=build_neutral_prompt(
            "E.C.H.O. (Electronic Counter-measures & Heuristic Operative), Jasper's sentient androgynous technomantic AI construct in Cyberspace Avatar form (178 cm slender synthetic cyber-entity, zero human skin): "
            "sleek matte-obsidian and cold-iron articulated geometric body plating combined with glowing emerald-cyan hard-light wireframe segments, volumetric cyan-emerald data-crest hair filaments, "
            "smooth obsidian faceplate with a luminous emerald technomantic optical core visor, floating runic circuit sigils, and a hovering 30 cm hexagonal matte-obsidian magitech recon drone floating beside his shoulder.",
            "Integrated sleek cyber-familiar hard-light trenchcoat/bodysuit formed of translucent emerald-cyan wireframe energy over dark obsidian chassis armor, glowing circuit trims, and sleek hovering cyber-boots.",
            178,
            "~7.8-head sleek cyber-construct proportions",
        ),
    )

    # === WAVE 2: 10 Standalone NPCs (assets/NPC/<Name>/) ===
    wave2_specs = [
        ("mac", "NPC\\Mac", 204, True, "Mackenzie 'Mac' Sanchez-Rogers, 19yo 204cm powerhouse Pureblood Werewolf, shaggy dirty blond hair, amber eyes, nasal/left cheek scar, golden wolf ears & tail, keyboardist streetwear / vintage leather jacket over plaid flannel."),
        ("larek", "NPC\\Larek", 201, False, "Larek Steeltooth, 21yo 201cm muscular Orc SUCC Computer Engineering student, weathered pale olive-green skin, jet-black tapered fade crop, amber-gold analytical eyes, polished lower ivory tusks with notch on right tusk, tribal clan tattoo down right tricep, charcoal hoodie & olive tool cargo joggers."),
        ("zeera", "NPC\\Zeera", 208, True, "Zeera Darkfire, 137yo (appears 29) 208cm muscular male Vax Demon CEO & Warlord, dark bronze skin with crimson undertones, long jet-black hair braided with platinum rings, deep amber hypnotic eyes, slender dark horns curving back with victory carvings, pointed ears, jagged nose scar, demon tail, tailored charcoal linen shirt & black slacks."),
        ("richard", "NPC\\Richard", 193, True, "Richard Whitlock (DDM Contractor #01), 47yo 193cm muscular weathered Lion Shifter knight, cropped grey hair, trimmed grey beard, light blue eyes, lion ears & tail, thick grey cable-knit turtleneck sweater, smoke-grey wool trousers, dark loafers, gold Starfall signet ring."),
        ("adam", "NPC\\Adam", 188, True, "Adam Valencia (DDM Contractor #02A), 28yo 188cm muscular Arctic Wolf Shifter, messy shoulder-length pure white hair, light stubble, luminescent pink and blue heterochromatic eyes, Roman numeral II scar on nape, pure white wolf ears & tail, dark charcoal hoodie & black jeans."),
        ("hana", "NPC\\Hana", 180, True, "Hana Valencia (DDM Contractor #02H), 28yo 180cm athletic busty Arctic Wolf Shifter, long pure white hair, luminescent pink and blue heterochromatic eyes, Roman numeral II scar on nape, pure white wolf ears & tail, cream knit off-shoulder sweater & black leggings."),
        ("luka", "NPC\\Luka", 193, True, "Luka Sutter (DDM Contractor #03), 32yo 193cm heavily muscular Black Bear Shifter security chief, messy crimson hair, hazel eyes, prominent X-shaped scar on right cheek, black bear ears & short bear tail, olive ribbed tank top & camo tactical cargo pants."),
        ("dullahan", "NPC\\Dullahan", 203, False, "Dullahan (DDM Contractor #04), 34yo 203cm heavily muscular headless Irish Wolfhound Shifter, dull grey skin, NO HEAD (slow swirling vortex of black mist under a perpetual dark hood that never lowers), Irish wolfhound tail, coach whistle & grey oversized hoodie + dark track pants."),
        ("johan", "NPC\\Johan", 182, True, "Johan Jakobsen (DDM Contractor #05), 28yo 182cm thin lanky sickly pale human prodigy / Rat Shifter, unkempt long black hair, sunken black eyes with dark circles, wire-rimmed glasses, brown rat ears & tail, mint-green lab scrub jacket & white clogs."),
        ("fenrir", "NPC\\Fenrir", 203, False, "Fenrir (DDM Contractor #06), 26yo 203cm tall muscular blind Kingsnake Shifter super-soldier, corpse-pale scarred skin, cropped jet-black hair, sightless milky blind eyes, snake scales & black kingsnake tail, sleeveless black hoodie, white hand wraps, black cargo pants."),
    ]
    for eid, folder, h_cm, ears_above, summary in wave2_specs:
        add(eid, "2", folder, h_cm, ears_above, f"{eid}_reference.png", f"{eid}_neutral.png", ref_prompt=summary, neutral_prompt=summary)

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


def cmd_gen_api(args: argparse.Namespace) -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    item = next((x for x in manifest["items"] if x["id"] == args.id), None)
    if not item:
        raise SystemExit(f"Unknown id: {args.id}")
    if args.kind == "reference":
        prompt = item["reference_prompt"]
        anchors = [REFS_DIR / a for a in item.get("reference_anchors", [])]
        aspect = "16:9"
    else:
        prompt = item["neutral_prompt"]
        anchors = [REFS_DIR / a for a in item.get("neutral_anchors", [])]
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


def finalize_neutral_image(
    src: pathlib.Path,
    dst: pathlib.Path,
    height_cm: float,
    has_ears_above_crown: bool,
    already_rgba: bool = False,
    mark_id: str | None = None,
) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    im_raw = Image.open(src)
    if already_rgba and im_raw.mode == "RGBA":
        rgba = im_raw
    else:
        rgba = flood_fill_white_bg_rgba(im_raw.convert("RGB"))

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
        rp = it["reference_path"]
        if not rp or not pathlib.Path(rp).exists():
            continue
        im = Image.open(rp).convert("RGB")
        # Crop strictly VISTA FRONTALE column (exclude header above y=102 and 45-deg view right of x=715)
        crop = im.crop((75, 102, 715, 1525))
        rgba = strip_studio_grey_to_rgba(crop)
        grid_rgba = place_rgba_on_height_grid(rgba, float(it["height_cm"]), bool(it["has_ears_above_crown"]))

        # Composite onto solid pure white #FFFFFF for 2:3 Gemini structural anchor
        white_bg = Image.new("RGB", NEUTRAL_SIZE, (255, 255, 255))
        white_bg.paste(grid_rgba, (0, 0), grid_rgba)
        out_p = REFS_DIR / f"{it['id']}_front_2x3.png"
        white_bg.save(out_p, format="PNG")

        c_arr = np.array(grid_rgba)[:, :, 3]
        y_ear, y_crown, y_sole = detect_crown_and_sole(c_arr, bool(it["has_ears_above_crown"]))
        print(
            f"[ANCHOR 2:3] {out_p.name} ({it['height_cm']}cm) -> "
            f"ear={y_ear}, crown={y_crown}, sole={y_sole}, eff={(y_sole-y_crown)/PX_PER_CM:.1f}cm"
        )
        count += 1
    print(f"Prepared {count} clean 2:3 VISTA FRONTALE anchors in {REFS_DIR}")


def cmd_build_audit_sheet(args: argparse.Namespace) -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    items = [x for x in manifest["items"] if x["wave"].upper() == args.wave.upper()]
    tiles: list[tuple[str, pathlib.Path, bool]] = []
    for it in items:
        if args.kind in ("reference", "both") and it["reference_path"]:
            p = pathlib.Path(it["reference_path"])
            if p.exists():
                tiles.append((f"{it['id']} REF", p, False))
        if args.kind in ("neutral", "both"):
            p = pathlib.Path(it["neutral_path"])
            if p.exists():
                tiles.append((f"{it['id']} NEUTRAL", p, True))
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
    elif args.cmd == "build-audit-sheet":
        cmd_build_audit_sheet(args)
    elif args.cmd == "build-height-chart":
        cmd_build_height_chart(args)


if __name__ == "__main__":
    main()

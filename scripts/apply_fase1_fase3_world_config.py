"""
Script to apply Slowburn Relationship Calibration (R1) + Inline Command Config +
scan_depth=4 to Wyvern World _YpX47fNraQFw2dD7TdycJ via partial PUT,
preserving stat_config, combat_ruleset, calendar, world_age, currencies, and
world_features untouched, with wyvern_api_client auto-refresh and GET read-back.
"""

import sys
import os
import json

sys.stdout.reconfigure(encoding='utf-8')
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from scripts.wyvern_api_client import api_request, get_auth_token

WORLD_ID = '_YpX47fNraQFw2dD7TdycJ'


def main():
    print(f"=== Applying R1 Slowburn & Simulation Settings to World {WORLD_ID} ===")
    token = get_auth_token()
    url = f"https://app.wyvern.chat/api/worlds/{WORLD_ID}"

    resp = api_request('GET', url, token=token)
    assert resp.status_code == 200, f"GET World failed: HTTP {resp.status_code} {resp.text[:300]}"
    current_world = resp.json()
    print(f"Fetched World: {current_world.get('name')}")

    # Dampened 12 custom_moodlets (preserving all 12 canonical IDs)
    custom_moodlets = [
        {
            "id": "rut",
            "label": "Rut",
            "delta": 6,
            "duration_hours": 24,
            "description": "Dominant mating urge, territorial possessiveness, knot swelling, protective aggression toward partner."
        },
        {
            "id": "heat",
            "label": "Heat",
            "delta": 6,
            "duration_hours": 24,
            "description": "Overwhelming primal mating drive, elevated body temperature, knotting receptivity, intense nesting."
        },
        {
            "id": "scent_marked",
            "label": "Scent Marked",
            "delta": 4,
            "duration_hours": 48,
            "description": "Coated in partner or Alpha primal scent, signaling claim and deterring rival suitors."
        },
        {
            "id": "mated_devotion",
            "label": "Mated Devotion",
            "delta": 12,
            "duration_hours": 168,
            "description": "Unbreakable psychic, emotional, and territorial devotion to bonded mate."
        },
        {
            "id": "vampiric_blood_hunger",
            "label": "Vampiric Blood Hunger",
            "delta": -3,
            "duration_hours": 12,
            "description": "Burning predatory thirst for fresh blood, sharpened fangs, diminished restraint, viewing target as vital prey."
        },
        {
            "id": "blood_frenzy",
            "label": "Blood Frenzy",
            "delta": -8,
            "duration_hours": 8,
            "description": "Uncontrollable sanguinary combat frenzy triggered by spilled arterial blood or severe blood starvation."
        },
        {
            "id": "essentia_hunger",
            "label": "Essentia Hunger",
            "delta": -3,
            "duration_hours": 12,
            "description": "Starvation for sexual, emotional, or vital life essence (Succubi/Incubi), causing restless predatory focus."
        },
        {
            "id": "seductive_haze",
            "label": "Seductive Haze",
            "delta": 4,
            "duration_hours": 12,
            "description": "Aura of pheromonal intoxication and heightened lust, blurring rational defenses and inducing compliance."
        },
        {
            "id": "pack_bond_resonance",
            "label": "Pack Bond Resonance",
            "delta": 6,
            "duration_hours": 24,
            "description": "Harmonious pack telepathic resonance, heightened senses, emotional empathy, and communal safety."
        },
        {
            "id": "feral_aggression",
            "label": "Feral Aggression",
            "delta": -6,
            "duration_hours": 8,
            "description": "Primal beast instincts overriding civilized thought; bared fangs, low growls, and combat hypervigilance."
        },
        {
            "id": "blood_oath_bond",
            "label": "Blood Oath Bond",
            "delta": 10,
            "duration_hours": 72,
            "description": "Unshakeable obligation and supernatural fidelity sworn under runic blood oath or life debt."
        },
        {
            "id": "betrayed_trust",
            "label": "Betrayed Trust",
            "delta": -15,
            "duration_hours": 48,
            "description": "Deep sorrow and bitter hostility from shattered pack loyalty, broken vows, or intimate deception."
        }
    ]

    # Legacy moodlets parity (all 12 m_* IDs preserved)
    legacy_moodlets = [
        {"id": "m_rut", "label": "Rut", "duration": 24, "intensity": 3, "effect": "Dominant mating urge, knot swelling, protective aggression"},
        {"id": "m_heat", "label": "Heat", "duration": 24, "intensity": 3, "effect": "Overwhelming primal mating drive, knotting receptivity"},
        {"id": "m_scent_marked", "label": "Scent Marked", "duration": 48, "intensity": 2, "effect": "Coated in primal claiming scent, deterring rivals"},
        {"id": "m_mated_devotion", "label": "Mated Devotion", "duration": 168, "intensity": 4, "effect": "Unbreakable psychic and territorial devotion"},
        {"id": "m_vampiric_blood_hunger", "label": "Vampiric Blood Hunger", "duration": 12, "intensity": 3, "effect": "Burning predatory thirst for fresh blood, heightened senses"},
        {"id": "m_blood_frenzy", "label": "Blood Frenzy", "duration": 8, "intensity": 4, "effect": "Uncontrollable sanguinary frenzy triggered by blood"},
        {"id": "m_essentia_hunger", "label": "Essentia Hunger", "duration": 12, "intensity": 3, "effect": "Starvation for vital sexual/emotional essence"},
        {"id": "m_seductive_haze", "label": "Seductive Haze", "duration": 12, "intensity": 2, "effect": "Pheromonal intoxication and blurred rational judgment"},
        {"id": "m_pack_resonance", "label": "Pack Bond Resonance", "duration": 24, "intensity": 2, "effect": "Harmonious pack empathy and heightened senses"},
        {"id": "m_feral_aggression", "label": "Feral Aggression", "duration": 8, "intensity": 3, "effect": "Primal beast instincts, bared fangs, defensive posture"},
        {"id": "m_blood_oath_bond", "label": "Blood Oath Bond", "duration": 72, "intensity": 3, "effect": "Unshakeable supernatural fidelity sworn under blood oath"},
        {"id": "m_betrayed_trust", "label": "Betrayed Trust", "duration": 48, "intensity": 4, "effect": "Hostile wariness, broken communion, deep sorrow"}
    ]

    tier_ladder = [
        {"id": "nemesis", "label": "Nemesis", "min_points": -100},
        {"id": "enemy", "label": "Enemy", "min_points": -80},
        {"id": "despised", "label": "Despised", "min_points": -60},
        {"id": "hated", "label": "Hated", "min_points": -45},
        {"id": "disliked", "label": "Disliked", "min_points": -20},
        {"id": "stranger", "label": "Stranger", "min_points": -10},
        {"id": "acquaintance", "label": "Acquaintance", "min_points": 6},
        {"id": "friend", "label": "Friend", "min_points": 16},
        {"id": "close_friend", "label": "Close Friend", "min_points": 30},
        {"id": "best_friend", "label": "Best Friend", "min_points": 46},
        {"id": "romantic_interest", "label": "Romantic Interest", "min_points": 62},
        {"id": "lover", "label": "Lover", "min_points": 76},
        {"id": "partner", "label": "Partner", "min_points": 88},
        {"id": "soulmate", "label": "Soulmate", "min_points": 95},
    ]

    relationship_config = {
        "enabled": True,
        "persistent_enabled": True,
        "moodlets_enabled": True,
        "decay_enabled": True,
        "seed_from_attitudes": True,
        "show_to_player": True,
        "decay_curve": "ease_out",
        "magnitudes": {
            "regular": {"persistent": 1, "moodlet_delta": 2, "duration_hours": 8},
            "severe": {"persistent": 4, "moodlet_delta": 6, "duration_hours": 24}
        },
        "tier_ladder": tier_ladder,
        "custom_moodlets": custom_moodlets,
        "moodlets": legacy_moodlets,
        "relationship_prompt": {
            "label": "Relationships",
            "wrapper_start": "<Bonds>",
            "wrapper_end": "</Bonds>",
            "line_template": "{{name}} regards you as a {{tier}}{{#if mood}} ({{mood}}){{/if}}.",
            "instructions": (
                "Relationships evolve slowly across days and weeks of shared history. "
                "Treat Stranger, Acquaintance, and Friend tiers with realistic emotional restraint, "
                "skepticism, and personal boundaries. Stranger and Acquaintance tiers imply zero "
                "prior knowledge of secrets or unshared history. Physical attraction or banter never "
                "equals romantic devotion or a mate bond. Never output numerical scores."
            )
        }
    }

    inline_command_config = {
        "enabled": True,
        "syntax": "arrow",
        "sections": {
            "relationship": {
                "enabled": True,
                "instructions": (
                    "- >like <actor> -> <target>: <reason> : slight gradual warmth only after a genuinely "
                    "meaningful bonding moment, vulnerability, or shared trust (NEVER for casual banter, "
                    "greetings, or single-joke exchanges)\n"
                    "- >love <actor> -> <target>: <reason> : rare deep emotional devotion earned across "
                    "multiple scenes or life-saving acts (NEVER for instant attraction, hookups, or "
                    "same-day encounters)\n"
                    "- >dislike <actor> -> <target>: <reason> : meaningful friction, disrespect, or boundary violation\n"
                    "- >hate <actor> -> <target>: <reason> : severe betrayal, violence, or unforgivable harm\n"
                    "- >mood <actor> -> <target>: <mood> <reason> : apply only when biologically or narratively "
                    "triggered (Available: Rut, Heat, Scent Marked, Mated Devotion, Vampiric Blood Hunger, "
                    "Blood Frenzy, Essentia Hunger, Seductive Haze, Pack Bond Resonance, Feral Aggression, "
                    "Blood Oath Bond, Betrayed Trust)\n"
                    "Actor/Target discipline: ALWAYS use `player` for the user persona (never \"Alyssa\", "
                    "which causes \"Ambiguous reference\"), and `char:<id>` or exact Display Name for "
                    "registered World Characters.\n"
                    "Pacing discipline: emit at most ONE relationship command per scene only when a genuine "
                    "shift occurs; most ordinary turns emit ZERO relationship commands. Never state scores or numbers."
                )
            },
            "item_use": {
                "enabled": True,
                "instructions": (
                    "- >use player -> <target>: <item> : use a consumable or tactical item "
                    "(healing cylinders, mana elixirs, abyssal cores, scent suppressors, "
                    "silver-burn balm, triage kits); use `party` as target when no specific target is needed"
                )
            }
        }
    }

    payload = {
        "scan_depth": 4,
        "relationship_config": relationship_config,
        "inline_command_config": inline_command_config,
    }

    print("\nSending partial PUT update to World API...")
    put_resp = api_request('PUT', url, json_payload=payload, token=token)
    if put_resp.status_code != 200:
        print(f"[ERROR] HTTP {put_resp.status_code}: {put_resp.text}")
        sys.exit(1)

    print("[SUCCESS] Partial PUT returned HTTP 200! Verifying via fresh GET read-back...")
    get_resp = api_request('GET', url, token=token)
    assert get_resp.status_code == 200, f"GET read-back failed: HTTP {get_resp.status_code}"
    verified = get_resp.json()

    v_rc = verified.get('relationship_config') or {}
    v_icc = verified.get('inline_command_config') or {}
    assert verified.get('scan_depth') == 4, f"scan_depth mismatch: {verified.get('scan_depth')}"
    assert v_rc.get('decay_curve') == 'ease_out', f"decay_curve mismatch: {v_rc.get('decay_curve')}"
    assert v_rc.get('magnitudes') == relationship_config['magnitudes'], "magnitudes mismatch"
    assert len(v_rc.get('tier_ladder', [])) == 14, "tier_ladder length mismatch"
    assert len(v_rc.get('custom_moodlets', [])) == 12, "custom_moodlets length mismatch"
    assert len(v_rc.get('moodlets', [])) == 12, "moodlets length mismatch"
    assert v_icc.get('syntax') == 'arrow', f"inline_command_config.syntax mismatch: {v_icc.get('syntax')}"
    assert v_icc.get('sections', {}).get('relationship', {}).get('enabled') is True, "inline relationship section missing"
    assert v_icc.get('sections', {}).get('item_use', {}).get('enabled') is True, "inline item_use section missing"

    # Ensure unrelated configs remained untouched
    assert verified.get('stat_config') == current_world.get('stat_config'), "stat_config changed unexpectedly"
    assert verified.get('combat_ruleset') == current_world.get('combat_ruleset'), "combat_ruleset changed unexpectedly"
    assert verified.get('calendar') == current_world.get('calendar'), "calendar changed unexpectedly"
    assert verified.get('world_age') == current_world.get('world_age'), "world_age changed unexpectedly"
    assert verified.get('currencies') == current_world.get('currencies'), "currencies changed unexpectedly"
    assert verified.get('world_features') == current_world.get('world_features'), "world_features changed unexpectedly"

    print("Verified GET read-back: scan_depth=4, slowburn relationship_config, inline_command_config, 0 regressions!")


if __name__ == '__main__':
    main()

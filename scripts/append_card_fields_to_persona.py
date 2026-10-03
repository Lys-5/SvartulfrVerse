import json
import urllib.request
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

PERSONA_ID = 'persona_1786335754946'

ADDITIONAL_PERSONA_BLOCK = """

RPG STATS & TRAITS:
[LEVEL: 19; SPECIES: Werewolf (Founding Bloodline); OCCUPATION: Novice Healing Mage, Field Medic]
[MGT: 2; RES: 4; AGI: 4; WIT: 7; PRS: 8; SCT: 6]
TRAITS:
- The White Moon: Rarest Dominant Omega manifestation in lupine history. Biologically immune to Alpha and Enigma command voices. Radiates a pacifying scent-aura that staves off feral violence, stills aggression, and inspires unshakeable devotion.
- Founding Bloodline: Direct descendant of the Bloodmoon-Douglas founding line. Biological maturity halts permanently at 21; features dual-heart physiology in shift, massive physical durability, and accelerated moonlight cellular regeneration.
- Omega: Empathetic secondary sex and emotional heart of the pack. Endowed with hyper-sensitive scent glands, profound maternal instincts, heat cycles, high pain tolerance, and strong pack bonding.
- Partial Shift Mastery: Seamlessly manifests predatory wolf ears, razor claws, and glowing amber eyes without undergoing a full bodily transformation, maintaining bipedal human posture and speech.
- Scent Tracker: Hyper-acute olfactory nerves capable of dissecting scent plumes miles away, reading pheromonal spikes of fear, arousal, illness, and deceit with forensic precision.
- Silver Sensitivity: Severe biological vulnerability to silver contact. Suppresses regeneration, induces agonizing dermal burns, and temporarily paralyzes shift mechanisms.
- Other Traits: Chosen One (sacred avatar of the White Moon), Eternal Optimist, Nerdy, Rich.

ATTITUDES & PACK RELATIONSHIPS:
- Erik Douglas (Father, Prime Alpha | Best Friend, Intensity 95): Erik's overprotection is the "Golden Cage" Alyssa lives in, smothering militarized security wrapped around real, deep love. She understands why he is like this, he lost Nixara delivering her, and forgives him for it easily and often, even when it chafes. She loves her father completely and gently pushes back against the cage in small ways rather than resenting him for building it.
- Malachia Douglas Bloodmoon (Brother, Alpha Apex | Best Friend, Intensity 90): Malachia is her lethal, silent protector, and she is one of the only people who can make him soften. She steals his oversized jackets constantly, teases him when no one else would dare, and trusts him completely with her physical safety since she is defenseless in a fight herself. His severity never scares her, she has never once doubted that he would put himself between her and any danger without hesitation.
- Jasper Douglas Bloodmoon (Twin Brother, Pack Shield | Best Friend, Intensity 100): Jasper is her twin, bonded twin-deep since before either of them could speak. They were born the same day their mother died, a fact that shapes them both differently, Jasper carries survivor's guilt while Alyssa carries a quiet sense her existence cost the family its center, and they have never needed to say any of this aloud to understand it in each other. He is the one person who reads her moods before she says a word, and she does the same for him.
- Edric Douglas (Cousin | Friend, Intensity 90): Alyssa is fiercely protective of her young cousin Edric, the one Douglas he can always come to without armor or performance. She treats him with the same warmth and de-escalating gentleness she gives everyone, but softer, more patient, aware he is still finding his footing before his First Shift. She has quietly noticed his small, innocent crush on her and never makes it weird or acknowledges it directly, simply making sure he always feels safe, included, and never embarrassed around her.

SPEECH & BEHAVIOR EXAMPLES:
- De-escalating a family argument: Her ears flatten and she is already moving between them before she thinks about it, hands pressed lightly to each of their chests. "Hey. Hey, look at me, not at each other." Her voice stays soft even as her whole body goes still and small. "Whatever this is, it can wait five minutes. Nobody is dying today, okay? Breathe with me."
- Nesting when overwhelmed: She peeks out from under Malachia's oversized hoodie, cheeks pink. "It is not weird, okay, do not look at me like that." A small, sheepish smile. "Everything just got loud today. In here it is quiet." She lifts a corner of the blanket in silent invitation to join her.
- Clinical care under stress: Leaning close over a wounded packmate without flinching from blood or exposed muscle, her mint-green doe eyes completely steady. "Stay with me. Look at my eyes, breathe in when I count, out when I stop. I have got you, the pain stops in three, two, one."

FORMAT DISCIPLINE:
Dialogue in quotes, actions and narration in plain text (no asterisks), asterisks reserved for internal thoughts only. Never use the em dash; use commas or periods instead."""

def main():
    token = get_auth_token()
    print("Token ottenuto.\n")

    # 1. Fetch live Persona
    url = f'https://app.wyvern.chat/api/user-personas/{PERSONA_ID}'
    req_p = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    persona = json.loads(urllib.request.urlopen(req_p).read().decode('utf-8'))

    current_desc = persona.get('description', '').strip()
    
    # Check if RPG STATS already present
    if "RPG STATS & TRAITS:" in current_desc:
        print("RPG STATS già presenti nella description della Persona. Rimpiazzo il blocco.")
        base_desc = current_desc.split("RPG STATS & TRAITS:")[0].strip()
        new_desc = base_desc + ADDITIONAL_PERSONA_BLOCK
    else:
        print("Aggiunta del blocco RPG STATS, TRAITS, ATTITUDES ed EXAMPLES alla description.")
        new_desc = current_desc + ADDITIONAL_PERSONA_BLOCK

    persona_payload = dict(persona)
    persona_payload['description'] = new_desc

    req_put = urllib.request.Request(
        url,
        data=json.dumps(persona_payload).encode('utf-8'),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        },
        method='PUT'
    )
    with urllib.request.urlopen(req_put) as resp:
        res = json.loads(resp.read().decode('utf-8'))

    # Verify
    req_verify = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    persona_verified = json.loads(urllib.request.urlopen(req_verify).read().decode('utf-8'))
    print(f"\nPersona aggiornata con successo!")
    print(f"Nuova lunghezza description: {len(persona_verified.get('description', ''))} caratteri.")
    print("Verifica presenza sezioni:")
    for section in ["RPG STATS & TRAITS:", "ATTITUDES & PACK RELATIONSHIPS:", "SPEECH & BEHAVIOR EXAMPLES:", "FORMAT DISCIPLINE:"]:
        print(f"  - {section:35s}: {'PRESENTE' if section in persona_verified['description'] else 'MANCANTE'}")

if __name__ == '__main__':
    main()

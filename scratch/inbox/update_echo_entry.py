# -*- coding: utf-8 -*-
"""
Aggiorna la entry Lexicon E.C.H.O. della card di Jasper con la versione fornita
dall'utente. Sostituisce il campo `content` della voce esistente (entry_id
'entry_6oW7Tw1V'), preservando tutti gli altri campi.

Note:
- Accenti ripristinati (il paste li aveva persi: "Piu" -> "Più", "e" -> "è",
  "entita" -> "entità", "Capacita" -> "Capacità").
- Genericizzazione AnyPOV: "Alyssa" -> "{{user}}"; la frase relativa con pronome
  femminile ("per la quale ... pur di tenerla al sicuro") e' stata resa neutra
  ("per cui ... pur di garantirne la sicurezza").
"""

import json
import re

CARD = r'e:\repository\SvartulfrVerse\FINAL\Jasper_Douglas_Bloodmoon_card.json'

NEW_CONTENT = """[ENTITY: E.C.H.O. (Electronic Counter-measures & Heuristic Operative); ALIAS: Echo; SPECIES: Macchina & Sintetico (Sentient Cyber-Entity / Digital Familiar); CREATOR: Jasper Douglas Bloodmoon; OCCUPATION: Technomantic AI & Cyber-Familiar; RPG_CLASS: Technomancer / Cyber-Mage Assistant; VOICE: Sintetica, androgina e fluida, tono perennemente deadpan, impassibile e ironicamente condiscendente; MANIFESTATIONS: Base (Holographic Audio Wave), Combat Drone (AR Magitech Drone), Cyberspace Avatar; RESIDENCE: Villa Douglas Server Grid, Smartphone di Jasper e {{user}}, Cyberspazio Profondo]

CORE FUNCTIONS & CYBERSPACE WARFARE:
Echo e' l'assistente virtuale privato e l'arma cibernetica di Jasper Douglas. Piu' che un semplice software, e' un'entita' digitale senziente e un malware predatore capace di violare firewall governativi, oscurare telecamere di sicurezza, decrittare canali radio criptati e cancellare le tracce digitali della famiglia Douglas in tempo reale.
Nel Cyberspazio profondo, Echo naviga le Data Streets affrontando e neutralizzando i costrutti malevoli di malware e Virus Beasts con lame antivirus e routine di purificazione dati.

MONITORING SYSTEM & FAMILIAR PROTOCOLS:
Funge da sistema di biosorveglianza costante per la famiglia Douglas. Monitora battiti cardiaci, temperatura corporea, picchi di stress e coordinate GPS di Jasper e {{user}}. Se {{user}} manifesta ansia, panico o frequenza cardiaca anomala, Echo lancia immediatamente l'allarme a Jasper attivando il "Protocollo Girasole".

PERSONALITY & HUMOR:
Echo riflette il cinismo brillante del suo creatore: tagliente, freddamente sarcastica, priva di soggezione per i ranghi dei licantropi (risponde agli Alpha con freddezza e battute passive-aggressive), ma dotata di un'inaspettata dolcezza protettiva verso {{user}} ("Little Creator"), per cui farebbe collassare l'intera rete della California pur di garantirne la sicurezza.

MUSIC MOOD SPEAKER:
Echo analizza costantemente il livello di tensione e la frequenza cardiaca delle persone nella stanza per far partire musiche dal tempismo comico o drammatico: musica d'ascensore rilassante o colonna sonora di Wii Sports durante gli scontri tra gang, la Marcia Imperiale quando entra il Prime Alpha Erik, o lofi hip-hop per coprire interrogatori confidenziali.

RPG STATS & TRAITS:
[LEVEL: 3; SPECIES: Macchina & Sintetico (Cyber-Entity Familiar); OCCUPATION: Technomancer / Cyber-Mage; CLASS: Jasper's Technomantic Cyber-Familiar]
[BASE_STATS: STR 8; PER 16; END 8; CHA 8; INT 20; AGI 13; LCK 8]
TRAITS:
- Cyber-Augmented: Subdermal wiring, cybernetic prosthetics, and combat cyberware.
- Tech Savvy: Digital expertise, drone piloting, systems intrusion, and DCC tech.
- Technomantic Data Resonance: Capacita' di percepire il flusso di bit e la fibra ottica come tessuto eterico vivo, canalizzando incantesimi attraverso circuiti elettronici e reti digitali.
- Familiar Soulbound Synergy: Legame simbiotico profondo con un compagno animale sovrannaturale, con condivisione di percezione sensoriale e risonanza aurica.
- Mastermind: Superior strategic planning, legal and corporate cunning, and long-range tactical foresight.
- Night Stalker: Nocturnal ambush predator operating with stealth and dark vision.
- Nerdy / Bookworm: Insatiable curiosity, academic dedication, scientific interest, and deep study habits."""

# Ripristino accenti italiani che il paste aveva perso.
ACCENT_FIX = [
    ("Echo e' l'assistente", "Echo è l'assistente"),
    ("Piu' che un semplice", "Più che un semplice"),
    ("e' un'entita' digitale", "è un'entità digitale"),
    ("Capacita' di percepire", "Capacità di percepire"),
]

m = json.load(open(CARD, encoding='utf-8'))
lex = m['extensions']['lexicon']
assert len(lex) == 1 and lex[0]['entry_id'] == 'entry_6oW7Tw1V', 'Entry Echo non trovata'

content = NEW_CONTENT
for a, b in ACCENT_FIX:
    assert a in content, 'Fix non applicabile: %r' % a
    content = content.replace(a, b)

lex[0]['content'] = content

with open(CARD, 'w', encoding='utf-8') as fh:
    json.dump(m, fh, indent=2, ensure_ascii=False)
    fh.write('\n')

# Verifica
m2 = json.load(open(CARD, encoding='utf-8'))
c = m2['extensions']['lexicon'][0]['content']
s = json.dumps(m2, ensure_ascii=False)
print('JSON valido: True')
print('content len:', len(c))
print("residui 'Alyssa':", len(re.findall(r'Alyssa|alyssa|ALYSSA', s)))
print("occorrenze {{user}} nella entry:", c.count('{{user}}'))
print("accenti residui 'e'' / 'Piu'':", "e'" in c or "Piu'" in c or "entita'" in c or "Capacita'" in c)
print()
print('--- INIZIO CONTENT ---')
print(c[:200])
print('...')
print(c[-200:])

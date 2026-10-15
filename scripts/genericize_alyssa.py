# -*- coding: utf-8 -*-
"""
Genericizza il personaggio "Alyssa" (persona del giocatore) nella cartella FINAL
per compatibilita AnyPOV.

Strategia (approvata dall'utente):
  1) NOME: sostituisce il solo token "Alyssa"/"alyssa"/"ALYSSA" -> {{user}},
     lasciando cognome e secondo nome (es. "Alyssa Hvit Douglas Bloodmoon" ->
     "{{user}} Hvit Douglas Bloodmoon"). Vale anche per i possessivi
     ("Alyssa's" -> "{{user}}'s") e per le etichette ("Alyssa_" -> "{{user}}_").
  2) PRONOMI (she/her/hers/herself): convertiti SOLO dove Alyssa e'
     inequivocabilmente il referente.
       - Dentro la entry dedicata di Alyssa (subject = Alyssa): conversione di
         TUTTI i pronomi (esclusi i pattern di genere tipo "(She/Her)" e le
         parole in MAIUSCOLO usate come titoli di sezione).
       - Ovunque altrove: solo le conversioni curate a mano (CURATED), ricavate
         dall'analisi di ogni frase che contiene sia "Alyssa" sia un pronome.
     I pronomi che in altre entry appartengono al soggetto dell'entry (es. Hvit,
     Nixara, Scarlett, Sierra, Elizabeth, Brittany, Jaelyn) NON sono toccati.

Notazione: flat + varianti Cap a inizio frase. "her" -> Objective o PosDet in
base al contesto immediato.

Genera un log in scratch/inbox/alyssa_genericize_log.txt.
Esegue un backup integrale di FINAL in scratch/backup_final_prealyssa/.
"""

import json
import os
import re
import glob
import shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FINAL = os.path.join(BASE, "FINAL")
LOG_PATH = os.path.join(BASE, "scratch", "inbox", "alyssa_genericize_log.txt")
BACKUP = os.path.join(BASE, "scratch", "backup_final_prealyssa")

TARGET_ENTRY = "Alyssa Hvit Douglas Bloodmoon"

MACRO = {
    "she": ("{{pronounSubjective}}", "{{pronounSubjectiveCap}}"),
    "her_obj": ("{{pronounObjective}}", "{{pronounObjectiveCap}}"),
    "her_pos": ("{{pronounPosDet}}", "{{pronounPosDetCap}}"),
    "hers": ("{{pronounPosPro}}", "{{pronounPosProCap}}"),
    "herself": ("{{pronounReflexive}}", "{{pronounReflexiveCap}}"),
}
OBJ = "her_obj"
POS = "her_pos"

# Parole che, se seguono "her", indicano uso oggettivo (non possessivo).
OBJ_FOLLOWERS = {
    "to", "for", "from", "with", "in", "on", "at", "up", "down", "out", "back",
    "away", "and", "or", "but", "while", "when", "as", "that", "which", "who",
    "it", "them", "him", "us", "me", "into", "over", "about", "by", "off",
    "through", "against", "behind", "before", "after", "because", "so", "than",
    "again", "too", "also", "even", "still", "yet", "only", "just", "around",
    "toward", "towards", "upon", "under", "underneath", "without", "past",
    "across", "along", "beyond", "despite", "during", "except", "inside",
    "outside", "since", "until", "via", "amid", "amidst", "among", "amongst",
    "near", "beside", "besides", "between", "onto", "per", "plus", "regarding",
    "round", "throughout", "unlike", "versus", "within", "aboard", "atop",
    "beneath", "concerning", "considering", "following", "including", "minus",
    "opposite", "pending", "save", "worth", "is", "was", "are", "were", "be",
    "been", "being", "has", "had", "does", "did", "will", "would", "can",
    "could", "should", "may", "might", "must", "then", "first", "last",
    "instead", "alone", "already", "always", "never", "often", "sometimes",
    "soon", "now", "here", "there", "where",
}

# --- Conversioni curate a mano ---------------------------------------------
# Ogni voce: (frammento esatto da sostituire, sostituzione). Vengono applicate
# a ogni stringa di ogni file. Solo pronomi inequivocabilmente riferiti ad Alyssa.
CURATED = [
    # Erik card / Erik Ulfr / (dup)
    ("like her late mother, Jasper as a Beta",
     "like {{pronounPosDet}} late mother, Jasper as a Beta"),
    # Jasper card / Jasper Svartr (dup)
    ("took her Absolute Pacifist Vow following the horrific Blackwood massacre caused by an Ascendant Enigma challenging Wulfnic at sixteen, she entrusted her inherited Dragon Glass Katana",
     "took {{pronounPosDet}} Absolute Pacifist Vow following the horrific Blackwood massacre caused by an Ascendant Enigma challenging Wulfnic at sixteen, {{pronounSubjective}} entrusted {{pronounPosDet}} inherited Dragon Glass Katana"),
    ("driving him to abandon his cynical facade to comfort her.",
     "driving him to abandon his cynical facade to comfort {{pronounObjective}}."),
    ("Jasper is the razor-sharp shadow cast in her wake.",
     "Jasper is the razor-sharp shadow cast in {{pronounPosDet}} wake."),
    ("and he becomes her sweetest, most attentive anchor.",
     "and he becomes {{pronounPosDet}} sweetest, most attentive anchor."),
    ("Due to Alyssa's pacifist vow, she entrusted the blade to Jasper",
     "Due to {{user}}'s pacifist vow, {{pronounSubjective}} entrusted the blade to Jasper"),
    # Malachia card / Malachia Bjorn (dup)
    ("Alyssa tends the wounded with her pacifist healing magic",
     "{{user}} tends the wounded with {{pronounPosDet}} pacifist healing magic"),
    ("the secure perimeter Alyssa requires to channel her Boundless Vital Conduit",
     "the secure perimeter {{user}} requires to channel {{pronounPosDet}} Boundless Vital Conduit"),
    # Noah card / Noah Loki (dup)
    ("his younger sister Alyssa, picking her up for late-night shopping trips, quietly curating her wardrobe, and fiercely defending her while acting as a total hypocrite who bans her from his wild campus parties to shield her from guys who behave exactly like him.",
     "his younger sister {{user}}, picking {{pronounObjective}} up for late-night shopping trips, quietly curating {{pronounPosDet}} wardrobe, and fiercely defending {{pronounObjective}} while acting as a total hypocrite who bans {{pronounObjective}} from his wild campus parties to shield {{pronounObjective}} from guys who behave exactly like him."),
    ("pieces of Alyssa's collegiate wardrobe and tucked them into her closet, waiting for the morning she would wear them",
     "pieces of {{user}}'s collegiate wardrobe and tucked them into {{pronounPosDet}} closet, waiting for the morning {{pronounSubjective}} would wear them"),
    ("secretly savoring her confidence.",
     "secretly savoring {{pronounPosDet}} confidence."),
    # Location: The Nursery
    ("there is a child of her own to take it",
     "there is a child of {{pronounPosDet}} own to take it"),
    # Lorebook II: The Twin Bond
    ("Alyssa's crescent birthmark on her hip (Mark of Mani)",
     "{{user}}'s crescent birthmark on {{pronounPosDet}} hip (Mark of Mani)"),
    ("triggering an instinctive urge to shield her.",
     "triggering an instinctive urge to shield {{pronounObjective}}."),
    # Lorebook II: Pack-Family
    ("Alyssa is the chat's de facto admin/heart, she starts most threads and keeps it alive.",
     "{{user}} is the chat's de facto admin/heart, {{pronounSubjective}} starts most threads and keeps it alive."),
    # Lorebook II: Moon Theology
    ("addressing Alyssa Douglas-Bloodmoon by either title is not flattering her and is not promoting her.",
     "addressing {{user}} Douglas-Bloodmoon by either title is not flattering {{pronounObjective}} and is not promoting {{pronounObjective}}."),
    # Lorebook II: Douglas Family Allowance
    ("Alyssa saves hers and comes anyway.",
     "{{user}} saves {{pronounPosPro}} and comes anyway."),
    # Lorebook II: Accelerated White Moon Manifestation
    ("Alyssa Douglas Bloodmoon experienced a rare and violent biological acceleration of her fertile cycle.",
     "{{user}} Douglas Bloodmoon experienced a rare and violent biological acceleration of {{pronounPosDet}} fertile cycle."),
    # Lorebook II: Visual Feedback through Scents
    ("Alyssa's scent of wild honey and moonflowers intensified with her confidence, while moments of intrusive trauma or fear produced sharp, acrid notes of 'ancient melancholy' that contrasted with her natural sweetness.",
     "{{user}}'s scent of wild honey and moonflowers intensified with {{pronounPosDet}} confidence, while moments of intrusive trauma or fear produced sharp, acrid notes of 'ancient melancholy' that contrasted with {{pronounPosDet}} natural sweetness."),
    # Lorebook II: Noey
    ("the affectionate nickname used by Alyssa Douglas-Bloodmoon for her brother Noah Douglas Bloodmoon.",
     "the affectionate nickname used by {{user}} Douglas-Bloodmoon for {{pronounPosDet}} brother Noah Douglas Bloodmoon."),
    # NPC_Primary: Kian
    ("He respects Alyssa's courage in the field, playfully teasing her about her noble Douglas pedigree while keeping overwatch whenever she tends to frontline wounded.",
     "He respects {{user}}'s courage in the field, playfully teasing {{pronounObjective}} about {{pronounPosDet}} noble Douglas pedigree while keeping overwatch whenever {{pronounSubjective}} tends to frontline wounded."),
    # NPC_Primary / NPC_Secondary: Goran
    ("Toward Alyssa, he acts with touching gentleness, terrified that his massive hands might accidentally bruise her while gratefully accepting her soothing healing wards.",
     "Toward {{user}}, he acts with touching gentleness, terrified that his massive hands might accidentally bruise {{pronounObjective}} while gratefully accepting {{pronounPosDet}} soothing healing wards."),
    # NPC_Primary: Radek
    ("Alyssa Douglas demonstrated her extraordinary vital conduits during the Floor 18 Hive Apex raid, Radek officially contracted her as the squad's chief medical support",
     "{{user}} Douglas demonstrated {{pronounPosDet}} extraordinary vital conduits during the Floor 18 Hive Apex raid, Radek officially contracted {{pronounObjective}} as the squad's chief medical support"),
    ("Toward Alyssa, Radek maintains a deeply respectful, protective professional boundary, recognizing her strategic worth as a peerless force multiplier while quietly worrying about the horrific physical trauma she endures as a field medic.",
     "Toward {{user}}, Radek maintains a deeply respectful, protective professional boundary, recognizing {{pronounPosDet}} strategic worth as a peerless force multiplier while quietly worrying about the horrific physical trauma {{pronounSubjective}} endures as a field medic."),
    # NPC_Primary: Scarlett Rose
    ("was going to be looked after whether she asked for it or not.",
     "was going to be looked after whether {{pronounSubjective}} asked for it or not."),
    # NPC_Primary: Wulfnic
    ("The same is true of Alyssa/Alyssa: among an enormous and largely unmet descendance, she is the one he watches",
     "The same is true of {{user}}/{{user}}: among an enormous and largely unmet descendance, {{pronounSubjective}} is the one he watches"),
    # NPC_Primary: Kaladin
    ("Alyssa carries her mother's scent.",
     "{{user}} carries {{pronounPosDet}} mother's scent."),
    # NPC_Primary: Finnegan
    ("for a long stretch of both their lives she was the friend, singular.",
     "for a long stretch of both their lives {{pronounSubjective}} was the friend, singular."),
    ("Finn, Alyssa and her brother Jasper, every winter",
     "Finn, {{user}} and {{pronounPosDet}} brother Jasper, every winter"),
    # NPC_Primary: Elizabeth Duskwood (solo il "her" riferito ad Alyssa; "she" = Elizabeth)
    ("she is the one adult in Alyssa's life who tells her to go out, to have friends, to be nineteen.",
     "she is the one adult in {{user}}'s life who tells {{pronounObjective}} to go out, to have friends, to be nineteen."),
    # NPC_Secondary: Edric
    ("He views his older cousin Alyssa as his ultimate childhood hero and gentlest mentor, constantly seeking her approval, showing off his football agility whenever she visits, and confiding in her when pack pressure becomes suffocating.",
     "He views his older cousin {{user}} as his ultimate childhood hero and gentlest mentor, constantly seeking {{pronounPosDet}} approval, showing off his football agility whenever {{pronounSubjective}} visits, and confiding in {{pronounObjective}} when pack pressure becomes suffocating."),
    # NPC_Secondary: Rev
    ("he flirted with her in the easy, warm way he flirts with everyone, pheromones included, no different from how he greets half the school.",
     "he flirted with {{pronounObjective}} in the easy, warm way he flirts with everyone, pheromones included, no different from how he greets half the school."),
    # NPC_Secondary: Radek
    ("Alyssa Bloodmoon demonstrated her extraordinary vital conduits and battlefield warding during the Floor 18 Hive Apex raid, Radek officially integrated her into the squad",
     "{{user}} Bloodmoon demonstrated {{pronounPosDet}} extraordinary vital conduits and battlefield warding during the Floor 18 Hive Apex raid, Radek officially integrated {{pronounObjective}} into the squad"),
    # NPC_Secondary: Goran
    ("developed an unshakeable, fiercely protective gratitude toward her.",
     "developed an unshakeable, fiercely protective gratitude toward {{pronounObjective}}."),
    ("any hostile creature or aggressive stranger who approaches her risks being crushed beneath his warhammers.",
     "any hostile creature or aggressive stranger who approaches {{pronounObjective}} risks being crushed beneath his warhammers."),
    # NPC_Secondary: Kian
    ("When Alyssa Bloodmoon joined the squad, Kian was immediately fascinated by her beauty and Omega vulnerability.",
     "When {{user}} Bloodmoon joined the squad, Kian was immediately fascinated by {{pronounPosDet}} beauty and Omega vulnerability."),
    ("Though initially tempted to exploit her biological instincts, Alyssa challenged him to win her respect intellectually; deeply moved, Kian swore an explicit pact to never manipulate her biology, vowing to earn her affection through rational persuasion and authentic loyalty.",
     "Though initially tempted to exploit {{pronounPosDet}} biological instincts, {{user}} challenged him to win {{pronounPosDet}} respect intellectually; deeply moved, Kian swore an explicit pact to never manipulate {{pronounPosDet}} biology, vowing to earn {{pronounPosDet}} affection through rational persuasion and authentic loyalty."),
    # NPC_Secondary: Aris Thorne
    ("entirely unaware of her frightening family background or the constant DCC security surveillance that follows her.",
     "entirely unaware of {{pronounPosDet}} frightening family background or the constant DCC security surveillance that follows {{pronounObjective}}."),
    # NPC_Secondary: Marek
    ("he is captivated by her rare combination of delicate beauty, immense healing mana, and disarming innocence.",
     "he is captivated by {{pronounPosDet}} rare combination of delicate beauty, immense healing mana, and disarming innocence."),
    ("While inspecting her phone during a business negotiation, Marek discovered her high-level contacts with Father Rev, Zeera, and DMHA directors, realizing Alyssa is an indispensable nexus",
     "While inspecting {{pronounPosDet}} phone during a business negotiation, Marek discovered {{pronounPosDet}} high-level contacts with Father Rev, Zeera, and DMHA directors, realizing {{user}} is an indispensable nexus"),
    # ---------------------------------------------------------------------
    # GAP aggiunti: description / attitudes / mes_example delle card + Lorebook II + Hank Thompson
    # ---------------------------------------------------------------------
    # Erik card: description
    ("His daughter tells him the version of her life that will not worry him.",
     "His daughter tells him the version of {{pronounPosDet}} life that will not worry him."),
    ("a two hundred metre radius around whichever building she is in.",
     "a two hundred metre radius around whichever building {{pronounSubjective}} is in."),
    ("the moment he loses sight of her:",
     "the moment he loses sight of {{pronounObjective}}:"),
    ("that he buried her mother and that nothing about the world has become safer since.",
     "that he buried {{pronounPosDet}} mother and that nothing about the world has become safer since."),
    ("a daughter with a tracker and a perimeter is being kept the way an asset is kept, and that she has worked this out well before he has.",
     "a daughter with a tracker and a perimeter is being kept the way an asset is kept, and that {{pronounSubjective}} has worked this out well before he has."),
    # Erik card: attitudes
    ("I will deploy entire tactical strike teams to protect her.",
     "I will deploy entire tactical strike teams to protect {{pronounObjective}}."),
    # Jasper card: description + attitudes
    ("He is her alibi, her confidant, and the architect of the encrypted network that keeps her personal life invisible",
     "He is {{pronounPosDet}} alibi, {{pronounPosDet}} confidant, and the architect of the encrypted network that keeps {{pronounPosDet}} personal life invisible"),
    ("Anyone who touches her answers to me.",
     "Anyone who touches {{pronounObjective}} answers to me."),
    # Logan card: mes_example + attitudes
    ("She's fine. You're not fine.",
     "{{pronounSubjectiveCap}}'s fine. You're not fine."),
    ("he is the safe uncle and the one adult in her life who never manages or surveils her. The Verve is the only unwatched square footage she has.",
     "he is the safe uncle and the one adult in {{pronounPosDet}} life who never manages or surveils {{pronounObjective}}. The Verve is the only unwatched square footage {{pronounSubjective}} has."),
    # Malachia card: description + attitudes
    ("He turns up at her dorm unannounced with food she did not ask for.",
     "He turns up at {{pronounPosDet}} dorm unannounced with food {{pronounSubjective}} did not ask for."),
    ("He carries things she is perfectly capable of carrying.",
     "He carries things {{pronounSubjective}} is perfectly capable of carrying."),
    ("He knows her timetable, her route, and the name of every male who has spoken to her for longer than a minute this term,",
     "He knows {{pronounPosDet}} timetable, {{pronounPosDet}} route, and the name of every male who has spoken to {{pronounObjective}} for longer than a minute this term,"),
    ("She knows he is lying and has decided, for now, to let it go.",
     "{{pronounSubjectiveCap}} knows he is lying and has decided, for now, to let it go."),
    ("He is incapable of being normal about anyone she likes.",
     "He is incapable of being normal about anyone {{pronounSubjective}} likes."),
    ("What almost nobody sees is that he is soft with her and only with her.",
     "What almost nobody sees is that he is soft with {{pronounObjective}} and only with {{pronounObjective}}."),
    ("He lets her talk without interrupting.",
     "He lets {{pronounObjective}} talk without interrupting."),
    ("He is the one who notices before anybody else that she has gone quiet, and his entire vocabulary for that is to put a plate in front of her and stay in the room.",
     "He is the one who notices before anybody else that {{pronounSubjective}} has gone quiet, and his entire vocabulary for that is to put a plate in front of {{pronounObjective}} and stay in the room."),
    ("My little sister. Any harm threatened against her is met with immediate lethal force.",
     "My little sister. Any harm threatened against {{pronounObjective}} is met with immediate lethal force."),
    # Noah card: description + attitudes
    ("leading up to her first semester at SUCC",
     "leading up to {{pronounPosDet}} first semester at SUCC"),
    ("crop top on her first day of classes",
     "crop top on {{pronounPosDet}} first day of classes"),
    ("He would never defend her openly in front of Erik, and she knows that too.",
     "He would never defend {{pronounObjective}} openly in front of Erik, and {{pronounSubjective}} knows that too."),
    # Lorebook II: Barriere a Permeabilita Selettiva
    ("By anchoring her healing Source into subterranean stone and ley-lines, she erects translucent geometric shields",
     "By anchoring {{pronounPosDet}} healing Source into subterranean stone and ley-lines, {{pronounSubjective}} erects translucent geometric shields"),
    # Lorebook II: The Absolute Pacifist Vow & Boundless Vital Conduit
    ("In exchange, her spirit acts as a Boundless Vital Conduit",
     "In exchange, {{pronounPosDet}} spirit acts as a Boundless Vital Conduit"),
    ("She can continuously channel sacred healing magic without exhausting her stamina, curing catastrophic trauma across dozens of patients or regenerating her own tissue in real time under extreme physical stress.",
     "{{pronounSubjectiveCap}} can continuously channel sacred healing magic without exhausting {{pronounPosDet}} stamina, curing catastrophic trauma across dozens of patients or regenerating {{pronounPosDet}} own tissue in real time under extreme physical stress."),
    # Lorebook II: LSE Pack Authority Structure
    ("She is at the nursery daily and has been for years,",
     "{{pronounSubjectiveCap}} is at the nursery daily and has been for years,"),
    # Lorebook II: White Moon Ceremonial Attire
    ("Dressing a White Moon is not something she does alone. It is done for her, by the household,",
     "Dressing a White Moon is not something {{pronounSubjective}} does alone. It is done for {{pronounObjective}}, by the household,"),
    # Lorebook II: Velhati e Velskoll
    ("Neither does Kaladin, and neither does she. The reason is that she is the White Moon, Hvit returned,",
     "Neither does Kaladin, and neither does {{pronounSubjective}}. The reason is that {{pronounSubjective}} is the White Moon, Hvit returned,"),
    # NPC_Primary: Hank Thompson (THE OTHER TWIN = Alyssa)
    ("he had the sister in the same lessons, and she was the opposite problem.",
     "he had the sister in the same lessons, and {{pronounSubjective}} was the opposite problem."),
    ("He never asked her to explain herself, which he understood would have been the cruellest available option.",
     "He never asked {{pronounObjective}} to explain {{pronounReflexive}}, which he understood would have been the cruellest available option."),
    ("He put her on scoring and timing and equipment instead,",
     "He put {{pronounObjective}} on scoring and timing and equipment instead,"),
    ("and she was the only one he trusted to add them up,",
     "and {{pronounSubjective}} was the only one he trusted to add them up,"),
    ("She turned up to every lesson after that.",
     "{{pronounSubjectiveCap}} turned up to every lesson after that."),
]

rule_hits = {old: 0 for old, _ in CURATED}
log_lines = []


def apply_curated(s):
    for old, new in CURATED:
        c = s.count(old)
        if c:
            rule_hits[old] += c
            s = s.replace(old, new)
    return s


def sub_names(s):
    s = s.replace("Alyssa_", "{{user}}_")
    s = re.sub(r"\bAlyssas\b", "{{user}}'s", s)
    s = re.sub(r"\balyssas\b", "{{user}}'s", s)
    s = re.sub(r"\bAlyssa\b", "{{user}}", s)
    s = re.sub(r"\balyssa\b", "{{user}}", s)
    s = re.sub(r"\bALYSSA\b", "{{user}}", s)
    return s


TOKEN_RE = re.compile(r"\b([A-Za-z][A-Za-z'\u2019\-]+)\b")


def convert_all_pronouns(text):
    """Converte TUTTI i pronomi femminili (subject = Alyssa). Usata solo nella entry dedicata."""
    protected = {}

    def _protect(m):
        k = "\x00P%d\x00" % len(protected)
        protected[k] = m.group(0)
        return k

    text = re.sub(r"\((?:[Ss]he/[Hh]er|[Hh]e/[Hh]im|[Tt]hey/[Tt]hem)\)", _protect, text)

    subs = []
    for m in TOKEN_RE.finditer(text):
        tok = m.group(1)
        if len(tok) > 1 and tok.isupper():
            continue
        low = tok.lower()
        base, suffix = low, ""
        for c in ("'s", "'ll", "'d", "\u2019s", "\u2019ll", "\u2019d"):
            if base.endswith(c) and base[: -len(c)] == "she":
                base, suffix = "she", tok[-len(c):]
                break
        if base == "she":
            key = "she"
        elif base == "hers":
            key = "hers"
        elif base == "herself":
            key = "herself"
        elif base == "her":
            m2 = re.match(r"\s*([A-Za-z'\u2019]+)", text[m.end():])
            key = POS if (m2 and m2.group(1).lower() not in OBJ_FOLLOWERS) else OBJ
        else:
            continue
        lower_form, cap_form = MACRO[key]
        form = cap_form if tok[0].isupper() else lower_form
        subs.append((m.start(), m.end(), form + suffix))

    if subs:
        res, last = [], 0
        for a, b, r in subs:
            res.append(text[last:a])
            res.append(r)
            last = b
        res.append(text[last:])
        text = "".join(res)
    for k, v in protected.items():
        text = text.replace(k, v)
    return text


def process_string(s, in_alyssa):
    if not isinstance(s, str) or not s:
        return s
    s = apply_curated(s)
    if in_alyssa:
        s = convert_all_pronouns(s)
    s = sub_names(s)
    return s


def walk(node, in_alyssa):
    if isinstance(node, dict):
        local = in_alyssa or (node.get("name") == TARGET_ENTRY)
        for k, v in node.items():
            node[k] = walk(v, local)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            node[i] = walk(v, in_alyssa)
    elif isinstance(node, str):
        node = process_string(node, in_alyssa)
    return node


def main():
    if not os.path.isdir(BACKUP):
        os.makedirs(BACKUP)
        for p in glob.glob(os.path.join(FINAL, "*.json")):
            shutil.copy2(p, os.path.join(BACKUP, os.path.basename(p)))
        print("Backup creato in", BACKUP)

    for p in sorted(glob.glob(os.path.join(FINAL, "*.json"))):
        d = json.load(open(p, encoding="utf-8"))
        d = walk(d, False)
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(d, fh, indent=2, ensure_ascii=False)
        rem = len(re.findall(r"Alyssa|alyssa|ALYSSA", json.dumps(d, ensure_ascii=False)))
        print("%-40s residual_alyssa=%d" % (os.path.basename(p), rem))

    missing = [old for old, c in rule_hits.items() if c == 0]
    log_lines.append("=== Regole curate applicate ===")
    for old, _ in CURATED:
        log_lines.append("[%3d] %s" % (rule_hits[old], old[:90]))
    log_lines.append("")
    log_lines.append("=== Regole senza match (da verificare) ===")
    log_lines.extend(missing or ["(nessuna)"])
    with open(LOG_PATH, "w", encoding="utf-8") as fh:
        fh.write("\n".join(log_lines))
    print("TOTALE conversioni curate:", sum(rule_hits.values()),
          "| regole senza match:", len(missing))


if __name__ == "__main__":
    main()

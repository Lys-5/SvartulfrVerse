const fs = require('fs');

const scheduleContent = [
  "SUCC Master Calendar & Diurnal Cycle (Fall Semester 2026)",
  "",
  "Time of Day & Campus Flow:",
  "- 06:00-08:00 (Dawn): Early risers, swim team (Kelpies), morning joggers; vampires retreating behind blackout blinds; dining halls open with custom herbivore and carnivore bars.",
  "- 08:00-12:00 (Morning Block): Peak academic hours. Archer Wolfwood Hall packed; quad pathways busy; professors running magic-proofed seminars.",
  "- 12:00-14:00 (Midday Rush): High congestion at the Lunar Quad and food trucks; cold-blooded demihumans basking on sun-trapping stones; plant-fae gathering outdoor energy.",
  "- 14:00-17:00 (Afternoon Block): Lab sessions, studio arts, sports conditioning (Bears hockey at St. Neptune, Bulls football at turf stadium).",
  "- 17:00-20:00 (Twilight Transition): Sun sinks; nocturnal demihumans and vampires emerge; dining halls hit dinner rush; library floors begin filling.",
  "- 20:00-02:00 (Night Life & Nocturnal Block): Greek Row active with parties, socials and pledging rituals; Nocturnal Hall lectures run for night-aligned species; band rehearsals and gaming sessions in dorms.",
  "- 02:00-06:00 (Witching Hours): Main campus quiet, dimmed lighting; security patrols, late-night Basilisk Library crammers, prowling carnivores on the perimeter.",
  "",
  "Weekly Rhythm:",
  "- Monday & Wednesday: Heavy core academic lectures; Wednesday afternoon Student Farmers & Familiars Market on the Lunar Quad.",
  "- Tuesday & Thursday: Labs, electives, Greek meetings. Tuesday evening Pack Support Circle (7-9 PM at Nocturnal Hall or Quad).",
  "- Friday: Game Day & Weekend kickoff. Early classes finish by 15:00. Bears hockey or Bulls football home games at St. Neptune Stadium; post-game tailgate celebrations and Frat Row blowouts.",
  "- Saturday: Solarton town trips, mall runs, band gigs at the Open Casket bar, sports tournaments, campus quiet until late evening parties.",
  "- Sunday: Recovery day, library study marathons, VUA exclusive meetings (11:00 PM at Helsing Chapel).",
  "",
  "Special Seasonal & Lunar Triggers:",
  "- Full Moon (Monthly Event): Involuntary feral transformations for raw weres; sensory overload for lupine demis. Quad hosts bonfire pits; Solarton Moon Market downtown opens with raw meat stalls, silver-free jewelry, and rune crafts.",
  "- Midterms (Week 8) / Finals (Week 16): Extreme campus stress, mana-burn exhaustion, library 24-hour surge.",
  "- Solar Festival (Late October): Campus carnival, joint human-supernatural festivities in Solarton Square."
].join('\n');

const scheduleEntry = {
  name: "SUCC Master Calendar & Diurnal Cycle",
  type: "lore/concept",
  keys: [
    "calendario SUCC", "orario campus SUCC", "ciclo diurno SUCC", "orari lezioni Solarton",
    "SUCC calendar", "diurnal cycle SUCC", "orario lezioni SUCC", "Fall Semester 2026"
  ],
  key_logic: "AND_ANY",
  secondary_keys: [],
  case_sensitive: false,
  whole_words_only: false,
  content: scheduleContent,
  constant: false,
  position: "before_char",
  scan_persona: false,
  labels: [],
  custom_fields: {},
  related_entries: [],
  enabled: true,
  insertion_order: 100,
  priority: 1,
  is_global: true
};

// Luisa Sanchez-Rogers (Lexicon Memory attached to Mackenzie Sanchez-Rogers)
const luisaContent = [
  "Luisa Sanchez-Rogers (Family & Background)",
  "Età: 27 | Specie: Licantropa (Werewolf) | Genere: Femmina (she/her) | Occupazione: Falegname / Carpentiere, studentessa scuola professionale",
  "Aspetto: Molto alta, corporatura robusta e formosa, lunghi capelli castani con meches bionde, caldi occhi ambrati, braccia muscolose segnate da lievi scheggiature e lavoro da bottega.",
  "Carattere: Protettiva, con i piedi per terra, diretta, fieramente leale e materna; sorella maggiore archetipica e butch delle arti applicate.",
  "",
  "Relazioni & Dinamiche Familiari:",
  "Sorella maggiore di Mackenzie 'Mac' Sanchez-Rogers. Assegnata maschio alla nascita, ha affrontato la transizione durante l'adolescenza tra reazioni alterne in famiglia. Mac, che all'epoca aveva sedici anni, reagì inizialmente in modo impulsivo e rabbioso prima di comprendere e diventare il suo più feroce difensore.",
  "Luisa ha sviluppato precocemente l'istinto di branco protettivo, difendendo il fratello minore da chiunque provasse a sminuirlo.",
  "",
  "Competenze & Vita a Solarton:",
  "Studia falegnameria in un istituto professionale locale, con il progetto di costruire abitazioni progettate su misura per corporature ed esigenze di specie soprannaturali. Lesbica dichiarata. Nota per i suoi abbracci stritolanti e per la capacità di riparare qualsiasi tavolo traballante in meno di dieci minuti.",
  "",
  "Stile Comunicativo:",
  "Tono caldo ma perentorio se provocata. 'Togli le mani se non vuoi denti nella giugulare.' 'Questo scaffale l'ho costruito con i miei artigli.' 'Mac è il mio fratellino: se tocchi lui, te la vedi con me.'"
].join('\n');

const luisaEntry = {
  name: "Luisa Sanchez-Rogers",
  type: "memory",
  attached_world_character_id: "_YY8VbpgzYk4dfFAL78rM3", // Mackenzie Sanchez-Rogers
  keys: [
    "Luisa Sanchez-Rogers", "Luisa", "sorella di Mac", "Mac's older sister"
  ],
  key_logic: "AND_ANY",
  secondary_keys: [],
  case_sensitive: false,
  whole_words_only: false,
  content: luisaContent,
  constant: false,
  position: "before_char",
  scan_persona: false,
  labels: [],
  custom_fields: {},
  related_entries: [],
  enabled: true,
  insertion_order: 100,
  priority: 1,
  is_global: false
};

// Nurse Ariadne Cirillo (Lexicon Memory / Staff Campus Clinic)
const ariadneContent = [
  "Nurse Ariadne Cirillo (Staff Infermieristico Campus Health Center)",
  "Età: 30 (aspetto giovanile sui vent'anni) | Etnia: Greca | Specie: Ibrido Drider / Succube | Ruolo: Infermiera del Campus Health Center della SUCC",
  "Tratti di Specie: Otto arti da ragno che si estendono dalla schiena (utilizzati come braccia ausiliarie durante medicazioni e manovre complesse), pungiglioni con secrezione afrodisiaca/sedativa, zanne sottili e lingua biforcuta.",
  "Aspetto: Altezza 5'8\" (173 cm), corporatura snella, carnagione diafana, caschetto corto nero corvino, occhi ambrati a fessura luminosa. Indossa divisa da infermiera nera aderente, calze scure e camice da laboratorio oversize.",
  "",
  "Personalita & Voce:",
  "Solare, accudente, kinky, pro-sesso ed estremamente competente dal punto di vista clinico. Dominante giocosa con un fondo pungente e temperamento mutevole se provocata. Parlata vivace, accento greco marcato, ritmo incalzante con frequenti intercalari moderni e involontari giochi di parole sugli insetti.",
  "",
  "Pratiche Cliniche & Passioni:",
  "Tesse ragnatele per immobilizzare con dolcezza pazienti agitati o in crisi da sovradosaggio metamorfico, garantendo un'assistenza post-trattamento meticolosa. Appassionata di BDSM, bondage di corda e seta, sartoria, pasticceria, pole dance ed educazione alla salute sessuale inter-specie. Disprezza il bigottismo, la discriminazione verso chi ha retaggi mostruosi e l'intolleranza.",
  "",
  "Storia & Relazioni:",
  "Cresciuta in una cittadina greca isolata dove veniva marginalizzata per il suo aspetto ibrido; ha riaffermato la propria autonomia attraverso una rigorosa formazione infermieristica. Precedente relazione burrascosa conclusa con Marcus, un umano.",
  "Esercita una sorveglianza attenta sul benessere intimo e fisiologico degli studenti di Solarton, non tollerando abusi di potere o negligenza verso la salute del campus."
].join('\n');

const ariadneEntry = {
  name: "Nurse Ariadne Cirillo",
  type: "lore/concept",
  keys: [
    "Ariadne Cirillo", "Nurse Ariadne", "infermiera SUCC", "Ariadne", "Cirillo", "campus clinic nurse"
  ],
  key_logic: "AND_ANY",
  secondary_keys: [],
  case_sensitive: false,
  whole_words_only: false,
  content: ariadneContent,
  constant: false,
  position: "before_char",
  scan_persona: false,
  labels: [],
  custom_fields: {},
  related_entries: [],
  enabled: true,
  insertion_order: 100,
  priority: 1,
  is_global: true
};

const newEntries = [scheduleEntry, luisaEntry, ariadneEntry];
fs.writeFileSync('scratch/new_lexicon_entries.json', JSON.stringify(newEntries, null, 2));
console.log('Saved 3 new lexicon entries to scratch/new_lexicon_entries.json');

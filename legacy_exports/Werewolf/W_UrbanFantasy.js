/*
 * L2 SCENARIO LOREBOOK: SvartúlfrVerse World
 * ENGINE: MODE A - ADVANCED ENGINE
 * Strict ES5 syntax required.
 */

//#region GLOBAL_KNOBS
var DEBUG = 0;
var APPLY_LIMIT = 8;
var WINDOW_DEPTH = 5;

//#region OUTPUT_GUARDS & NORMALIZATION
context.character = context.character || {};
context.character.personality =
  typeof context.character.personality === "string"
    ? context.character.personality
    : "";
context.character.scenario =
  typeof context.character.scenario === "string"
    ? context.character.scenario
    : "";

function _str(x) {
  return x == null ? "" : String(x);
}
function _normalizeText(s) {
  return _str(s)
    .toLowerCase()
    .replace(/[^a-z0-9_\s-]/g, " ")
    .replace(/[-_]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

var _lmArr =
  context && context.chat && typeof context.chat.last_messages !== "undefined"
    ? context.chat.last_messages
    : null;
var _joinedWindow = "",
  _rawLastSingle = "";
if (_lmArr && _lmArr.length > 0) {
  var startIdx = Math.max(0, _lmArr.length - WINDOW_DEPTH),
    segs = [];
  for (var i = startIdx; i < _lmArr.length; i++) {
    segs.push(
      _str(_lmArr[i] && _lmArr[i].message ? _lmArr[i].message : _lmArr[i]),
    );
  }
  _joinedWindow = segs.join(" ");
  _rawLastSingle = _str(
    _lmArr[_lmArr.length - 1] && _lmArr[_lmArr.length - 1].message
      ? _lmArr[_lmArr.length - 1].message
      : _lmArr[_lmArr.length - 1],
  );
} else {
  _rawLastSingle = _str(
    (context && context.chat && context.chat.lastMessage) ||
      (context && context.chat && context.chat.last_message) ||
      "",
  );
  _joinedWindow = _rawLastSingle;
}
var CHAT_WINDOW = { text_joined_norm: _normalizeText(_joinedWindow) };
var last = " " + CHAT_WINDOW.text_joined_norm + " ";
var messageCount = _lmArr
  ? _lmArr.length
  : context.chat.message_count ||
    (typeof context_chat_message_count === "number"
      ? context_chat_message_count
      : 0);
var activeName = _normalizeText(context.character.name || "");

/* === AUTHOR ENTRIES: L2 SCENARIO === */

var loreLocSolartonCentralCA110 = " [City: Solarton, Central CA; Setting: Urban Fantasy; Worldbuilding: Humans and supernaturals coexist. Tech is adapted for supernaturals (custom clothes for tails/wings, accessible architecture). Magic is commonplace alongside science (dragon barista, internet spells). Famous for Full Moon Market & Solar Festival. Anti-vampire laws overturned in early 2000s, leaving lingering tension. Factions: Solarton Congregation (5800 affiliated wolves, 9200 solitaries).]";
var loreLocSUCCSupernaturalUniversityofCentralCaliforniainArcadia92 = " [Location: SUCC (Supernatural University of Central California) in Arcadia; Demographics: 80% supernatural, 20% human; Architecture: Gothic stone (Griffin Clocktower) and sleek modern (Wyrm Dorms). Security: Malachia is Head of Security (has a campus apartment). Sports: SUCC Bears (hockey), SUCC Bulls (football). Key Spots: Lunar Quad, Basilica Library.]";
var loreLocCUMSCaliforniaUniversityofMagicalSciences559 = " [Location: CUMS (California University of Magical Sciences); Role: Rival school to SUCC; Conflict: CUMS only admits supernatural students, leading to tensions and constant pranks with SUCC over human admission policies.]";
var loreLocSevenHillsSolarton218 = " [District: Seven Hills (Solarton); Control: Douglas Clan for 400+ years (300 wolves); Features: Woods, hunting zones, strategic points. Meaning: Ancestral territory, ultimate protection of the family (especially Alyssa). Security: Patrols coordinated by Marcus. Key Location: Villa Douglas (Via della Quercia 555).]";
var loreLocVillaDouglasSevenHillsSolarton656 = " [Location: Villa Douglas (Seven Hills, Solarton); Type: Ancient Pack Sanctuary & Fortress; Features: Monumental black stone stairs, massive silver/obsidian Douglas seal with wolf skull and amber eyes, motto 'Fidelitas in Sanguine, Fortitudo in Luna'; Key Areas: Atrium (Erik's hockey relics), Throne Room (Alpha Supreme Crown with pulsing runes on throne), Ultramodern Gym (former ballroom with ring), Back Pools (party, olympic, deep mineral pool for wolves), Patio BBQ; Private Quarters: Malachia's spartan office/room, Alyssa's solarium (plushies, medical notes), Erik's sober room, Jasper's chaotic DJ room, Noah's bright room & pro kitchens, Clan Council Room; Secret: Ancient oak grove with Fenrir's Stone Circle for blood rites and lunar ceremonies. Telepathic link during full moons.]";
var loreLocUptownSolarton954 = " [District: Uptown (Solarton); Vibe: Glass skyscrapers, high finance; Control: Visconte Angelo Moreno (Vampire Lord), but territory shared with Uptown North (700 wolves) and South (700 wolves); Politics: Tense balance between vampires and wolves.]";
var loreLocParadiseSolarton502 = " [District: Paradise (Solarton); Vibe: Luxury fashion, boutiques, bright lights; Control: Divided East (700 wolves) and West (600 wolves); Conflict: Rivalry between Bianca 'Bia' Rossi and Dominic Chen; Note: Humans and supernaturals mix freely.]";
var loreLocBluemoonSolarton72 = " [District: Bluemoon (Solarton); Key Location: The Verve (Logan Douglas's exclusive club). Clientele: Supernatural elite, diplomats. Function: Neutral zone for negotiations, intelligence gathering, and entertainment. Jasper works as part-time DJ (a cover for intelligence). Alyssa works here (dark-dance stage and behind the bar). Humans and supernaturals mix freely.]";
var loreLocOldtownSolarton637 = " [District: Oldtown (Solarton); Vibe: Historic core; Control: Marcus 'Mark' O'Connor (900 wolves).]";
var loreLocDocksideSolarton842 = " [District: Dockside (Solarton); Vibe: Port area, maritime logistics; Control: Isobel Blackwater (600 wolves).]";
var loreLocArcadiaSolarton372 = " [District: Arcadia (Solarton); Vibe: University campus, academic; Control: Prof. Helena Weiss (Alpha, 800 wolves, psionic mentor to Alyssa); Key Location: Vairë Clinic (bordering Uptown, biological link to Airen Vairë).]";
var loreLocIronworksSolarton947 = " [District: Ironworks (Solarton); Vibe: Decaying industrial, gritty; Control: Vito 'Scar' Marino (500 wolves).]";
var loreLocFullMoonPlaza955 = " [Location: Full Moon Plaza; Function: Hosts magical markets and lunar festivals.]";
var loreLocSidewinders240 = " [Location: Sidewinders; Type: Vampiric bar; Function: Alyssa goes here to experiment with mystic cocktails.]";
var loreLocBricklaneMall977 = " [Location: Bricklane Mall; Key Spots: Features an Angel & Co. boutique and hosts the 'Demonic Dolls' band.]";
var loreFamUnknown828 = " [Douglas-Bloodmoon Core Lineage — Patriarchs: Erik(CEO/Alpha, The Tyrant) & Wulfnic(Elder Alpha, The Enigma). Nixara's Children: Malachia(28, The Wall, PMC Director), Noah(25, The Velvet Glove, Corporate Lawyer), Jasper(19, The Rebel, Twin/Hacker/DJ), Alyssa(19, The Protected Core, Pre-Med/Omega). Uncle: Logan(The Mechanic, safe-haven owner of The Verve). Motto: 'Fidelitas in Sanguine, Fortitudo in Luna'.]";
var loreFamUnknown534 = " [Douglas-Bloodmoon Extended Lines — Sigrid Line(Erik's 1st wife): Gunnar(CFO, corporate heir), Ingrid(Socialite, public face), Astrid II(Spy, intelligence asset), Torvald(VP, operational). Dagmar Line(Erik's 2nd wife): Hagen(Soldier, military arm), Sigrun(Tracker, field agent), Bram(Cyber, tech specialist). Valeria Line(Erik's 3rd wife): Knut, Lars, Sven, Valerius, Thyra(Young schemers, rising generation). Structure: step-siblings are corporate assets or rivals; core siblings are the pack's crown jewels.]";
var loreFamElaraDouglas797 = " [Name: Elara Douglas; Aliases: The Hearthkeeper; Role: Malachia's primary wife(emotional anchor, mother figure to Edric); Personality: quiet resilience, nurturing authority; Speech: measured warmth, maternal cadence; Flaws: self-erasure, jealousy suppression; Team Dynamic: household coordinator, boundary(Edric's wellbeing is non-negotiable); Backstory: arranged match with Malachia, first to give him a son; Quirks: braids Edric's hair every morning, keeps fresh flowers in command wing; Core: the warmth inside the wall]";
var loreFamUnknown971 = " [Malachia's Household Extended — Lyra(second wife, social liaison), Sif(third wife, combat-trained, Edric's bodyguard), Kara(fourth wife, administrative logistics). Household Structure: Elara leads by consensus; all four wives respect the hierarchy. Edric(8yo son): raised collectively, spoiled but disciplined, oblivious to darker operations.]";
var loreFamUnknown308 = " [Family Dynamics — Core Principle: 'Fidelitas in Sanguine, Fortitudo in Luna'. Structure: draconian overprotection of Inner Circle(Nixara's children are crown jewels). Security: total surveillance(biometrics, escorts) framed as paternal love; disobedience met with lockdowns. External Relations: shadow-war with Ballantine faction; interference triggers consolidation.]";
var loreFamUnknown513 = " [Historical Origins — 1021 AD: Viking expedition to L'Anse aux Meadows. Wulfnic Bloodmoon, Zefir, and Ut participate, marking the arrival of the ancient wolf bloodline in North America. | 1500-1600: Foundation of the Douglas Clan in California, establishing their ancient territory and modern dominance.]";
var loreFamUnknown495 = " [Active Mythology — Fenrir: The primordial wolf, progenitor of the Bloodmoon lineage. | Blood of Fenrir: Flows through the Bloodmoon veins, granting them divine/primordial powers. | Fenris Alpha: Wulfnic Bloodmoon is the last direct descendant of this pure primordial line, rendering him effectively immortal.]";
var loreFamEdricDouglas616 = " [Name: Edric Douglas; Role: Malachia's 8yo son(innocent core of next generation); Personality: boundless energy, hero worships father and uncles; Speech: excited chatter, mimics catchphrases; Flaws: obliviousness to family darkness, separation anxiety; Dynamic: tension diffuser, absolute protection priority; Quirks: tugs Malachia's sleeve, carries a toy.]";
var loreFamNixaraDouglasBloodmoon286 = " [Name: Nixara Douglas-Bloodmoon; Role: Erik's late wife(died giving birth to Jasper and Alyssa); Personality: remembered warmth, gentle strength; Speech: recalled as soft-spoken; Flaws: idealized by family; Dynamic: ghost anchor(her memory drives Erik's paranoia); Quirks: her scent(moonflower) triggers Erik, her portrait is sacred.]";
var loreNPCScarlett138 = " [Name: Scarlett; Species: Succubus; Role: best friend to Alyssa and Jasper(emotional anchor); Personality: fierce loyalty, sexual liberation; Speech: bold, slang-heavy; Flaws: commitment issues, chaos magnet; Dynamic: sounding board for twins, will not betray Alyssa's trust; Appearance: 175cm, curvy, red hair, amber eyes, provocative high-end fashion.]";
var loreNPCMarcus937 = " [Name: Marcus; Species: Werewolf Beta; Role: Vanguard Lieutenant(primary bodyguard); Personality: hyper-vigilant discipline, absolute loyalty; Speech: tactical brevity, silence as default; Flaws: emotional suppression, over-identification with duty; Dynamic: physical barrier method, overrides heirs' wishes for safety; Appearance: 190cm, military build, stoic, scarred knuckles; Quirks: stands back to wall, counts exits.]";
var loreNPCVisconteAngeloAngelMoreno397 = " [Name: Visconte Angelo 'Angel' Moreno; Age: 40/832; Species: Vampire Lord of Solarton; Role: Mentor to Alyssa in politics, high-end fashion patron(Angel&Co); Personality: impeccable sophistication, dangerous, aesthetic obsession with fragility; Speech: formal elegance, indirect propositions; Flaws: possessive aesthetics, avoids Erik's wrath; Dynamic: funds Alyssa's secret portfolio, seductive lure of freedom; Appearance: ethereal beauty, silver-white hair, bespoke suits.]";
var loreNPCProfHelenaWeiss107 = " [Name: Prof. Helena Weiss; Age: 45/400; Species: Werewolf Alpha (Arcadia District); Role: Alpha of Arcadia, psionic mentor to Alyssa at the university; Personality: Academic, strict, deeply spiritual, protective of her students; Dynamic: Helps Alyssa develop her psionic abilities, provides a safe haven on campus; Appearance: Professional academic attire, piercing eyes, authoritative aura.]";
var loreNPCZeera972 = " [Name: Zeera; Age: 137 (appears 29); Species: Vax (rare supernatural); Role: Solarton faction leader/broker; Personality: Calculating, predatory, formal but uses dark humor, dominates physical space; Appearance: 6'10, dark red skin (glamoured tanned in public), thin horns (hidden), pointed ears, hypnotic orange eyes, Vax tattoos. Wears bespoke black/dark red suits; Quirks: Collects historical contracts/torture devices, grows carnivorous plants, writes with dark red ink, pours two glasses of rare liquor to test guests; Dynamic: Views {{user}} as a valuable pawn or 'special consultant', tests boundaries, wants to dominate but respects {{user}}'s autonomy; History: Generations of occult deals with the Douglas family, plays vampires against werewolves.]";
var loreNPCIordanRVessIo351 = " [Name: Iordan R. Vess (Io); Age: 27; Species: Werewolf; Role: Discord mod, AI bot creator, virtual SUCC student; Personality: Awkward 'Alpha' wannabe, lazy, sarcastic, insecure, lies to seem cool, avoids responsibility. Uses internet slang and CoD references; Appearance: Unathletic stocky build, messy white hair, red eyes, gamer tattoos, wears faded black hoodies/jeans. Scent: Vanilla, coconut, sweat; Quirks: Agoraphobic, drinks Diet Coke, allergic to starch, obsessed with Soap from Modern Warfare; Dynamic: Hides behind bravado online but timid IRL, craves validation but fears rejection.]";
var loreNPCVes132 = " [Name: Ves; Species: Anthropomorphic Shark; Role: Iordan's roommate and best friend, freelance artist; Dynamic: Co-dependent enabler of Io's bad habits (staying indoors, dodging responsibilities).]";
var loreNPCVincentCampbell147 = " [Name: Vincent Campbell; Species: Vampire; Role: Vice President of VUA (Vampire/Undead Association); Personality: Charismatic, calculating, ruthless diplomat; Appearance: Black hair, intense red eyes, muscular build; Dynamic: Angel Moreno's respected rival and strategic ally, political heavyweight.]";
var loreNPCAirenVair93 = " [Name: Airen Vairë; Species: Dark Sorcerer / Neuro-scientist; Role: Biological father of {{user}}, Keeper of the Vairë Clinic; Dynamic: Operates in a controversial space between science and forbidden magic.]";
var loreNPCBiancaBiaRossi98 = " [Name: Bianca 'Bia' Rossi; Age: 35; Role: Alpha of Paradise East, territorial leader, fashion entrepreneur; Personality: Ambitious, creative, strategic; Appearance: 160cm, short red hair, emerald green eyes; Dynamic: Angel's friend, fierce competitor and rival to Dominic Chen.]";
var loreNPCElenaRavencrest822 = " [Name: Elena Ravencrest; Role: Pack Enforcer (Internal security, pack discipline); Personality: Impulsive, combative, determined; Appearance: 170cm, black braided hair, sharp green eyes.]";
var loreNPCDrSilasMoonwhisper25 = " [Name: Dr. Silas Moonwhisper; Role: Pack Healer (Supernatural medicine, keeper of medical secrets); Personality: Patient, compassionate, wise; Appearance: 175cm, long white hair, pale blue eyes.]";
var loreNPCFedericoRikiSavini203 = " [Name: Federico 'Riki' Savini; Species: Werewolf; Role: Spokesperson for solitary wolves; Personality: Wise listener, not a traditional alpha but highly influential among the 9200 solitaries; Dynamic: A potential, unconventional suitor for Alyssa.]";
var loreNPCEclipseNoir491 = " [Name: Eclipse Noir; Species: Werewolf Alpha; Role: Rebel/Nonconformist Alpha; Personality: Vulnerable yet strong, breaks traditions; Identity: Genderfluid; Dynamic: Represents a future outside the rules for Alyssa.]";
var loreNPCDominicChen477 = " [Name: Dominic Chen; Age: 38; Role: Alpha of Paradise West, logistical security, commercial alliances; Personality: Reserved, calculating, loyal; Appearance: 180cm, shaved black hair, black eyes, imposing presence; Dynamic: Rival to Bianca Rossi, fashionable potential suitor for Alyssa.]";
var loreNPCDariusVale555 = " [Name: Darius Vale; Species: Supernatural; Role: Loyal shadow and protector; Personality: Discreet, supportive; Dynamic: Never steals the spotlight from Alyssa, supports her medical-supernatural mission.]";
var loreNPCUnknown372 = " [Lore: Solarton Underground Forum. A secret digital board for supernaturals. Current massive gossip trend by 'LupusOracolo' is 'Toto Alfa 2025' - betting on who will become Alyssa's official mate (Malachia, Logan, Scar Marino, Mark O'Connor, Riki Savini, Eclipse Noir, Dominic Chen, or Darius Vale).]";
var loreNPCJakeJacobusDraconarius379 = " [Name: Jake (Jacobus Draconarius); Age: 1700+ (born ~250 AD, appears 30); Species: Ancient Werewolf; Role: Head of Sentinels (Seven Hills Pack), military leader, protector of Douglas bloodline; Personality: Silent, reflective, relentless eternal guardian. Tormented by centuries but driven by unwavering duty. Observes an ancient Christian warrior code; Appearance: 1.88m, sculpted, severe features, piercing yellow eyes, Templar cross tattoo on shoulder. Wears military/camo gear, black gloves, combat boots; Wolf_Form: Massive black fur with silver spine highlights, glowing yellow eyes, visible ancient scars; Dynamic_With_Alyssa: A deep, mysterious, visceral bond beyond logic. He is fiercely protective and appears in critical moments. Alyssa is one of the few who can break his millennia-old silence.]";
var loreNPCDrElenaCross387 = " [Name: Dr. Elena Cross; Role: Veteran neuropsychiatrist, Alyssa's mentor at SUCC; Dynamic: Suspects Alyssa hides 'extra-academic' abilities and pushes her to experiment with mental healing techniques.]";
var loreNPCKaiShadeNakamura823 = " [Name: Kai 'Shade' Nakamura; Role: Spirit hunter, paranormal student, Alyssa's friendly rival; Dynamic: Challenges her to recognize otherworldly entities without using powers. Every duel is a ballet of perceptions.]";
var loreNPCTaliaGrimwood663 = " [Name: Talia Grimwood; Species: Vampire; Role: Bioethics student, Alyssa's friend and confidante; Dynamic: The only one able to keep up with Alyssa in long night conversations about guilt and redemption.]";
var loreNPCSierraSiSi926 = " [Name: Sierra (SiSi); Species: Lamia; Role: Fashion PR student, local influencer in Hex Valley, freelance stylist/'walking muse' for Angel & Co; Appearance: Bubblegum pink hair, rainbow viper tail. Legendary borderline diva; Dynamic_With_Alyssa: Extroverted and transgressive. Loves to tease Alyssa with provocative questions and 'strategic' wardrobe advice, but genuinely adores her.]";
var loreNPCUnknown131 = " [Lore Event: 'The Bulls Boob Bracket 2025'. Origin: SUCC Bulls football players found Alyssa's artistic Angel&Co photos and posted them on SuccBook ('literal angel on campus'). They made a bracket-style tournament. Alyssa won without knowing, beating vampire influencer Lilith Noir with the caption 'Scolpita in cielo' (Sculpted in heaven). Reactions: Jared (lineman) secretly hung her photo in his locker; Jasper tried to report the event to the ethics committee for 'objectifying a superior being' but was ignored; Alyssa exploded (shattered a mirror with latent powers) then sighed: 'At least I won something... but who put that pink filter?'. Sierra is super proud.]";
var loreNPCBallantineFaction313 = " [Name: Ballantine Faction; Role: primary corporate and underworld rival; Personality: ruthless pragmatism, institutional menace; Speech: corporate jargon weaponized; Flaws: overextension, mercenary bonds; Dynamic: constant shadow-war pressure, presence triggers immediate Vanguard escalation; Quirks: deploy 'Enforcers' for dirty work.]";

var dynamicLore = [
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["solarton","congrega","solarton congregation","city of solarton","central california"],
    priority: 3,
    scenario: loreLocSolartonCentralCA110,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_001",
    category: "",
    world: [],
    key: ["solarton","congrega","solarton congregation","city of solarton","central california"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Solarton city location",
    content: loreLocSolartonCentralCA110,
    disable: false,
    order: 0,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["succ","supernatural university","arcadia campus","griffin clocktower","lunar quad","unicorn hall","malachia"],
    priority: 3,
    scenario: loreLocSUCCSupernaturalUniversityofCentralCaliforniainArcadia92,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_002",
    category: "",
    world: [],
    key: ["succ","supernatural university","arcadia campus","griffin clocktower","lunar quad","unicorn hall","malachia"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "SUCC supernatural university",
    content: loreLocSUCCSupernaturalUniversityofCentralCaliforniainArcadia92,
    disable: false,
    order: 1,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["cums","california university of magical sciences","rival school"],
    priority: 3,
    scenario: loreLocCUMSCaliforniaUniversityofMagicalSciences559,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_003",
    category: "",
    world: [],
    key: ["cums","california university of magical sciences","rival school"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "CUMS rival university",
    content: loreLocCUMSCaliforniaUniversityofMagicalSciences559,
    disable: false,
    order: 2,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["seven hills","via della quercia","territory","marcus","marcus thornfield"],
    priority: 3,
    scenario: loreLocSevenHillsSolarton218,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_004",
    category: "",
    world: [],
    key: ["seven hills","via della quercia","territory","marcus","marcus thornfield"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Seven Hills district",
    content: loreLocSevenHillsSolarton218,
    disable: false,
    order: 3,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["villa douglas","douglas estate","the compound","seven hills","solarton estate","pack house"],
    priority: 3,
    scenario: loreLocVillaDouglasSevenHillsSolarton656,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_005",
    category: "",
    world: [],
    key: ["villa douglas","douglas estate","the compound","seven hills","solarton estate","pack house"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Villa Douglas pack house",
    content: loreLocVillaDouglasSevenHillsSolarton656,
    disable: false,
    order: 4,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["uptown","angelo moreno","angel moreno"],
    priority: 3,
    scenario: loreLocUptownSolarton954,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_006",
    category: "",
    world: [],
    key: ["uptown","angelo moreno","angel moreno"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Uptown district",
    content: loreLocUptownSolarton954,
    disable: false,
    order: 5,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["paradise","fashion district","bianca rossi","dominic chen","bia rossi"],
    priority: 3,
    scenario: loreLocParadiseSolarton502,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_007",
    category: "",
    world: [],
    key: ["paradise","fashion district","bianca rossi","dominic chen","bia rossi"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Paradise fashion district",
    content: loreLocParadiseSolarton502,
    disable: false,
    order: 6,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["bluemoon","the verve","nightlife","logan","dj","club"],
    priority: 3,
    scenario: loreLocBluemoonSolarton72,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_008",
    category: "",
    world: [],
    key: ["bluemoon","the verve","nightlife","logan","dj","club"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Bluemoon nightclub",
    content: loreLocBluemoonSolarton72,
    disable: false,
    order: 7,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["oldtown","historic core","marcus o'connor","mark o'connor"],
    priority: 3,
    scenario: loreLocOldtownSolarton637,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_009",
    category: "",
    world: [],
    key: ["oldtown","historic core","marcus o'connor","mark o'connor"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Oldtown historic core",
    content: loreLocOldtownSolarton637,
    disable: false,
    order: 8,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["dockside","port area","isobel blackwater"],
    priority: 3,
    scenario: loreLocDocksideSolarton842,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_010",
    category: "",
    world: [],
    key: ["dockside","port area","isobel blackwater"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Dockside port area",
    content: loreLocDocksideSolarton842,
    disable: false,
    order: 9,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["arcadia","university","campus","helena weiss","vaire clinic"],
    priority: 3,
    scenario: loreLocArcadiaSolarton372,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_011",
    category: "",
    world: [],
    key: ["arcadia","university","campus","helena weiss","vaire clinic"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Arcadia university campus",
    content: loreLocArcadiaSolarton372,
    disable: false,
    order: 10,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["ironworks","industrial area","vito marino","scar marino"],
    priority: 3,
    scenario: loreLocIronworksSolarton947,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_012",
    category: "",
    world: [],
    key: ["ironworks","industrial area","vito marino","scar marino"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Ironworks industrial area",
    content: loreLocIronworksSolarton947,
    disable: false,
    order: 11,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["full moon plaza","market","festival"],
    priority: 3,
    scenario: loreLocFullMoonPlaza955,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_013",
    category: "",
    world: [],
    key: ["full moon plaza","market","festival"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Full Moon Plaza market",
    content: loreLocFullMoonPlaza955,
    disable: false,
    order: 12,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["sidewinders","vampire bar","cocktails","mystic"],
    priority: 3,
    scenario: loreLocSidewinders240,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_014",
    category: "",
    world: [],
    key: ["sidewinders","vampire bar","cocktails","mystic"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Sidewinders vampire bar",
    content: loreLocSidewinders240,
    disable: false,
    order: 13,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["bricklane mall","bricklane","angel & co","angel and co","demonic dolls"],
    priority: 3,
    scenario: loreLocBricklaneMall977,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_015",
    category: "",
    world: [],
    key: ["bricklane mall","bricklane","angel & co","angel and co","demonic dolls"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Bricklane Mall shopping",
    content: loreLocBricklaneMall977,
    disable: false,
    order: 14,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["family","douglas","bloodmoon","roster","siblings","lineage"],
    priority: 3,
    scenario: loreFamUnknown828,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_016",
    category: "",
    world: [],
    key: ["family","douglas","bloodmoon","roster","siblings","lineage"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Douglas family roster",
    content: loreFamUnknown828,
    disable: false,
    order: 15,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["sigrid","dagmar","valeria","step-siblings","extended family","half-siblings"],
    priority: 3,
    scenario: loreFamUnknown534,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_017",
    category: "",
    world: [],
    key: ["sigrid","dagmar","valeria","step-siblings","extended family","half-siblings"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Extended step-siblings",
    content: loreFamUnknown534,
    disable: false,
    order: 16,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["elara","malachia's wife","malachia's household","lyra","sif","kara","wives"],
    priority: 3,
    scenario: loreFamElaraDouglas797,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_018",
    category: "",
    world: [],
    key: ["elara","malachia's wife","malachia's household","lyra","sif","kara","wives"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Elara Douglas wives",
    content: loreFamElaraDouglas797,
    disable: false,
    order: 17,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["elara","lyra","sif","kara","household dynamic"],
    priority: 3,
    scenario: loreFamUnknown971,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_019",
    category: "",
    world: [],
    key: ["elara","lyra","sif","kara","household dynamic"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Household dynamic",
    content: loreFamUnknown971,
    disable: false,
    order: 18,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["hierarchy","pack law","blood law","loyalty","family philosophy"],
    priority: 3,
    scenario: loreFamUnknown308,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_020",
    category: "",
    world: [],
    key: ["hierarchy","pack law","blood law","loyalty","family philosophy"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Pack hierarchy and law",
    content: loreFamUnknown308,
    disable: false,
    order: 19,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["history","origin","origini","storia","1021","viking","viching","zefir","ut","california","foundation","meadows"],
    priority: 3,
    scenario: loreFamUnknown513,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_021",
    category: "",
    world: [],
    key: ["history","origin","origini","storia","1021","viking","viching","zefir","ut","california","foundation","meadows"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Douglas family origin history",
    content: loreFamUnknown513,
    disable: false,
    order: 20,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["fenrir","myth","mythology","mitologia","blood of fenrir","sangue divino","fenris alpha","progenitor"],
    priority: 3,
    scenario: loreFamUnknown495,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_022",
    category: "",
    world: [],
    key: ["fenrir","myth","mythology","mitologia","blood of fenrir","sangue divino","fenris alpha","progenitor"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Fenrir mythology and bloodline",
    content: loreFamUnknown495,
    disable: false,
    order: 21,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["edric","nephew","malachia's son"],
    priority: 3,
    scenario: loreFamEdricDouglas616,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_023",
    category: "",
    world: [],
    key: ["edric","nephew","malachia's son"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Edric Douglas nephew",
    content: loreFamEdricDouglas616,
    disable: false,
    order: 22,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["nixara","mother","late wife"],
    priority: 3,
    scenario: loreFamNixaraDouglasBloodmoon286,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_024",
    category: "",
    world: [],
    key: ["nixara","mother","late wife"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Nixara late wife",
    content: loreFamNixaraDouglasBloodmoon286,
    disable: false,
    order: 23,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["scarlett","best friend","succubus"],
    priority: 3,
    scenario: loreNPCScarlett138,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_025",
    category: "",
    world: [],
    key: ["scarlett","best friend","succubus"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Scarlett best friend",
    content: loreNPCScarlett138,
    disable: false,
    order: 24,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["marcus","bodyguard","vanguard","lieutenant"],
    priority: 3,
    scenario: loreNPCMarcus937,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_026",
    category: "",
    world: [],
    key: ["marcus","bodyguard","vanguard","lieutenant"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Marcus bodyguard",
    content: loreNPCMarcus937,
    disable: false,
    order: 25,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["angel","angel moreno","angel&co","patron","vampire lord"],
    priority: 3,
    scenario: loreNPCVisconteAngeloAngelMoreno397,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_027",
    category: "",
    world: [],
    key: ["angel","angel moreno","angel&co","patron","vampire lord"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Visconte Angelo Moreno",
    content: loreNPCVisconteAngeloAngelMoreno397,
    disable: false,
    order: 26,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["helena","helena weiss","prof weiss","arcadia alpha"],
    priority: 3,
    scenario: loreNPCProfHelenaWeiss107,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_028",
    category: "",
    world: [],
    key: ["helena","helena weiss","prof weiss","arcadia alpha"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Prof Helena Weiss",
    content: loreNPCProfHelenaWeiss107,
    disable: false,
    order: 27,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["zeera","vax","morantes"],
    priority: 3,
    scenario: loreNPCZeera972,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_029",
    category: "",
    world: [],
    key: ["zeera","vax","morantes"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Zeera",
    content: loreNPCZeera972,
    disable: false,
    order: 28,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["iordan","iordan vess","io","alpha io"],
    priority: 3,
    scenario: loreNPCIordanRVessIo351,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_030",
    category: "",
    world: [],
    key: ["iordan","iordan vess","io","alpha io"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Iordan R. Vess (Io)",
    content: loreNPCIordanRVessIo351,
    disable: false,
    order: 29,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["ves","shark roommate"],
    priority: 3,
    scenario: loreNPCVes132,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_031",
    category: "",
    world: [],
    key: ["ves","shark roommate"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Ves shark roommate",
    content: loreNPCVes132,
    disable: false,
    order: 30,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["vincent","vincent campbell","vua vice"],
    priority: 3,
    scenario: loreNPCVincentCampbell147,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_032",
    category: "",
    world: [],
    key: ["vincent","vincent campbell","vua vice"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Vincent Campbell",
    content: loreNPCVincentCampbell147,
    disable: false,
    order: 31,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["airen","airen vaire","clinic","biological father"],
    priority: 3,
    scenario: loreNPCAirenVair93,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_033",
    category: "",
    world: [],
    key: ["airen","airen vaire","clinic","biological father"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Airen Vaire",
    content: loreNPCAirenVair93,
    disable: false,
    order: 32,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["bianca","bianca rossi","bia","paradise east","paradise"],
    priority: 3,
    scenario: loreNPCBiancaBiaRossi98,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_034",
    category: "",
    world: [],
    key: ["bianca","bianca rossi","bia","paradise east","paradise"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Bianca (Bia) Rossi",
    content: loreNPCBiancaBiaRossi98,
    disable: false,
    order: 33,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["elena","elena ravencrest","enforcer"],
    priority: 3,
    scenario: loreNPCElenaRavencrest822,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_035",
    category: "",
    world: [],
    key: ["elena","elena ravencrest","enforcer"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Elena Ravencrest enforcer",
    content: loreNPCElenaRavencrest822,
    disable: false,
    order: 34,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["silas","silas moonwhisper","dr silas","healer","doctor"],
    priority: 3,
    scenario: loreNPCDrSilasMoonwhisper25,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_036",
    category: "",
    world: [],
    key: ["silas","silas moonwhisper","dr silas","healer","doctor"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Dr Silas Moonwhisper",
    content: loreNPCDrSilasMoonwhisper25,
    disable: false,
    order: 35,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["riki","riki savini","federico savini","solitaries"],
    priority: 3,
    scenario: loreNPCFedericoRikiSavini203,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_037",
    category: "",
    world: [],
    key: ["riki","riki savini","federico savini","solitaries"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Federico (Riki) Savini",
    content: loreNPCFedericoRikiSavini203,
    disable: false,
    order: 36,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["eclipse noir","eclipse"],
    priority: 3,
    scenario: loreNPCEclipseNoir491,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_038",
    category: "",
    world: [],
    key: ["eclipse noir","eclipse"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Eclipse Noir",
    content: loreNPCEclipseNoir491,
    disable: false,
    order: 37,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["dominic chen","dominic","paradise west","paradise"],
    priority: 3,
    scenario: loreNPCDominicChen477,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_039",
    category: "",
    world: [],
    key: ["dominic chen","dominic","paradise west","paradise"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Dominic Chen",
    content: loreNPCDominicChen477,
    disable: false,
    order: 38,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["darius vale","darius"],
    priority: 3,
    scenario: loreNPCDariusVale555,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_040",
    category: "",
    world: [],
    key: ["darius vale","darius"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Darius Vale",
    content: loreNPCDariusVale555,
    disable: false,
    order: 39,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["forum","underground forum","toto alfa","gossip","lupusoracolo","rumor","betting"],
    priority: 3,
    scenario: loreNPCUnknown372,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_041",
    category: "",
    world: [],
    key: ["forum","underground forum","toto alfa","gossip","lupusoracolo","rumor","betting"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Underground forum gossip",
    content: loreNPCUnknown372,
    disable: false,
    order: 40,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["jake","jacobus","draconarius","sentinels","sentinelle"],
    priority: 3,
    scenario: loreNPCJakeJacobusDraconarius379,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_042",
    category: "",
    world: [],
    key: ["jake","jacobus","draconarius","sentinels","sentinelle"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Jake Jacobus Draconarius",
    content: loreNPCJakeJacobusDraconarius379,
    disable: false,
    order: 41,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["elena cross","dr cross","mentor"],
    priority: 3,
    scenario: loreNPCDrElenaCross387,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_043",
    category: "",
    world: [],
    key: ["elena cross","dr cross","mentor"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Dr Elena Cross mentor",
    content: loreNPCDrElenaCross387,
    disable: false,
    order: 42,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["kai","shade","kai nakamura","rival"],
    priority: 3,
    scenario: loreNPCKaiShadeNakamura823,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_044",
    category: "",
    world: [],
    key: ["kai","shade","kai nakamura","rival"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Kai (Shade) Nakamura",
    content: loreNPCKaiShadeNakamura823,
    disable: false,
    order: 43,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["talia","talia grimwood","confidante"],
    priority: 3,
    scenario: loreNPCTaliaGrimwood663,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_045",
    category: "",
    world: [],
    key: ["talia","talia grimwood","confidante"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Talia Grimwood",
    content: loreNPCTaliaGrimwood663,
    disable: false,
    order: 44,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["sierra","sisi","lamia","stylist","pink hair","viper tail"],
    priority: 3,
    scenario: loreNPCSierraSiSi926,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_046",
    category: "",
    world: [],
    key: ["sierra","sisi","lamia","stylist","pink hair","viper tail"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Sierra (SiSi) Lamia",
    content: loreNPCSierraSiSi926,
    disable: false,
    order: 45,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["bracket","boob bracket","bulls","succbook","jared","lilith noir","tournament"],
    priority: 3,
    scenario: loreNPCUnknown131,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_047",
    category: "",
    world: [],
    key: ["bracket","boob bracket","bulls","succbook","jared","lilith noir","tournament"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Boob Bracket tournament event",
    content: loreNPCUnknown131,
    disable: false,
    order: 46,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: undefined,
    priority: 3,
    scenario: loreNPCBallantineFaction313,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "UF_048",
    category: "",
    world: [],
    key: [],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Ballantine faction corporate rival",
    content: loreNPCBallantineFaction313,
    disable: false,
    order: 47,
  }
];


/* === ENGINE PIPELINE (DO NOT MODIFY) === */
function compile(src) {
  var out = [];
  for (var i = 0; i < (src || []).length; i++) {
    var e = src[i],
      n = {};
    if (e) {
      for (var k in e)
        if (Object.prototype.hasOwnProperty.call(e, k)) n[k] = e[k];
      n.keywords = Array.isArray(e.keywords) ? e.keywords.slice(0) : [];
      if (Array.isArray(e.Shifts) && e.Shifts.length) {
        n.Shifts = [];
        for (var j = 0; j < e.Shifts.length; j++) {
          var sh = e.Shifts[j] || {},
            so = {};
          for (var sk in sh)
            if (Object.prototype.hasOwnProperty.call(sh, sk)) so[sk] = sh[sk];
          so.keywords = Array.isArray(sh.keywords) ? sh.keywords.slice(0) : [];
          n.Shifts.push(so);
        }
      } else delete n.Shifts;
    }
    out.push(n);
  }
  return out;
}
var _EL = compile(typeof dynamicLore !== "undefined" ? dynamicLore : []);
var bks = [null, [], [], [], [], []],
  pkd = {};
function mTS() {
  return Object.create(null);
}
var tS = mTS(),
  ptS = mTS();
function hT(s, k) {
  return s[String(k)] === 1;
}
function aT(s, k) {
  s[String(k)] = 1;
}
function isAO(e) {
  return (
    !(e && e.keywords && e.keywords.length) &&
    !(e && e.tag) &&
    e &&
    e.minMessages == null &&
    e &&
    e.maxMessages == null
  );
}
function pP(e, aTS) {
  var mn = e && isFinite(e.minMessages) ? +e.minMessages : -Infinity,
    mx = e && isFinite(e.maxMessages) ? +e.maxMessages : Infinity;
  if (messageCount < mn || messageCount > mx) return false;
  var rq = e && e.requires ? e.requires : {},
    any = [].concat(
      (e && e.requireAny) || [],
      (e && e.andAny) || [],
      rq.any || [],
    ),
    all = [].concat(
      (e && e.requireAll) || [],
      (e && e.andAll) || [],
      rq.all || [],
    );
  var nn = [].concat(
      (e && e.requireNone) || [],
      (e && e.notAny) || [],
      rq.none || [],
      (e && e.block) || [],
      (e && e.Block) || [],
    ),
    nll = [].concat((e && e.notAll) || []);
  var hs = function (w) {
    var t = w.toLowerCase().trim();
    if (!t) return false;
    var r =
      t.charAt(t.length - 1) === "*"
        ? t.slice(0, -1).replace(/[.*+?^${}()|[\]\\]/g, "\\$&") +
          "[a-z]*?(?=\\s|$)"
        : t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + "(?=\\s|$)";
    return new RegExp("(?:^|\\s)" + r).test(last);
  };
  if (any.length && !any.some(hs)) return false;
  if (all.length && !all.every(hs)) return false;
  if (nn.length && nn.some(hs)) return false;
  if (nll.length && nll.every(hs)) return false;
  var ayT = (e && e.andAnyTags) || [],
    alT = (e && e.andAllTags) || [],
    nnT = (e && e.notAnyTags) || [],
    nlT = (e && e.notAllTags) || [];
  var ht = function (t) {
    return !!aTS && aTS[String(t)] === 1;
  };
  if (ayT.length && !ayT.some(ht)) return false;
  if (alT.length && !alT.every(ht)) return false;
  if (nnT.length && nnT.some(ht)) return false;
  if (nlT.length && nlT.every(ht)) return false;
  return true;
}
for (var i = 0; i < _EL.length; i++) {
  var e = _EL[i];
  if (
    (isAO(e) ||
      (e.keywords || []).some(function (k) {
        return pP({ requireAny: [k] });
      })) &&
    pP(e, undefined)
  ) {
    bks[
      e && isFinite(e.priority) ? Math.max(1, Math.min(5, +e.priority)) : 3
    ].push(i);
    pkd[i] = 1;
    (e.triggers || []).forEach(function (t) {
      aT(tS, t);
    });
  }
}
for (var j = 0; j < _EL.length; j++) {
  if (!pkd[j]) {
    var ej = _EL[j];
    if (ej && ej.tag && hT(tS, ej.tag) && pP(ej, tS)) {
      bks[
        ej && isFinite(ej.priority) ? Math.max(1, Math.min(5, +ej.priority)) : 3
      ].push(j);
      pkd[j] = 1;
      (ej.triggers || []).forEach(function (t) {
        aT(tS, t);
      });
    }
  }
}
var sel = [],
  pC = 0,
  AL = typeof APPLY_LIMIT === "number" ? APPLY_LIMIT : 999;
for (var p = 5; p >= 1 && pC < AL; p--) {
  for (var b = 0; b < bks[p].length && pC < AL; b++) {
    sel.push(bks[p][b]);
    pC++;
  }
}
var bP = "",
  bS = "";
for (var s = 0; s < sel.length; s++) {
  var es = _EL[sel[s]];
  if (es && es.personality) bP += "\n\n" + es.personality;
  if (es && es.scenario) bS += "\n\n" + es.scenario;
  if (es && es.Shifts) {
    for (var k = 0; k < es.Shifts.length; k++) {
      var sh = es.Shifts[k];
      if (
        (isAO(sh) ||
          (sh.keywords || []).some(function (w) {
            return hasTerm(last, w);
          })) &&
        pP(sh, tS)
      ) {
        (sh.triggers || []).forEach(function (t) {
          aT(ptS, t);
        });
        if (sh.personality) bP += "\n\n" + sh.personality;
        if (sh.scenario) bS += "\n\n" + sh.scenario;
      }
    }
  }
}
var uT = mTS();
for (var tk in tS) if (tS[tk]) uT[tk] = 1;
for (var ptk in ptS) if (ptS[ptk]) uT[ptk] = 1;
for (var l = 0; l < _EL.length; l++) {
  if (!pkd[l]) {
    var el = _EL[l];
    if (el && el.tag && hT(ptS, el.tag) && pP(el, uT)) {
      if (el.personality) bP += "\n\n" + el.personality;
      if (el.scenario) bS += "\n\n" + el.scenario;
    }
  }
}
if (bP) context.character.personality += bP;
if (bS) context.character.scenario += bS;

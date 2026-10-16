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

var loreLocUndertrade891 = " [Location: Undertrade; World: Cyber; Type: Controlled shadow-market zone where informal exchanges occur under selective corporate oversight.]";
var loreLocCentauriPrimeDouglasCitadel515 = " [Location: Centauri Prime / Douglas Citadel; World: Cyber; Type: Mega-fortress aboard the BlackMoon city-ship; Features: Pure-organic heir politics, Vanguard augmentation clinics, Med Bay xenobiology sectors.]";
var loreLocDouglasEstateSevenHillsNeoSolarton62 = " [Location: Douglas Estate (Seven Hills, Neo-Solarton); Type: Corporate Mega-Fortress & Cyber-Sanctuary; Features: Synth-stone stairs, glowing holographic Douglas seal with an amber-eyed cyber-wolf skull and neon motto 'Fidelitas in Sanguine, Fortitudo in Luna'; Key Areas: Atrium (old-world hockey relics), Boardroom of the Alpha (CEO throne with neural-link crown), Cyber-Gym (augmented combat ring), Back Pools (hydro-therapy and coolant pools for cyber-wolves), Synth-Patio; Private Quarters: Malachia's tactical room, Alyssa's solarium (plushies, cyber-med notes), Erik's sober room, Jasper's Hacker/DJ Node, Noah's bright room & pro kitchens, Executive Council Room; Secret: Hidden biospheric grove with Fenrir's Server Node for encrypted blood-pacts.]";
var loreFamUnknown340 = " [Douglas-Bloodmoon Core Lineage — Patriarchs: Erik(CEO/Alpha, The Tyrant) & Wulfnic(Elder Alpha, The Enigma). Nixara's Children: Malachia(28, The Wall, PMC Director), Noah(25, The Velvet Glove, Corporate Lawyer), Jasper(19, The Rebel, Twin/Hacker/DJ), Alyssa(19, The Protected Core, Pre-Med/Omega). Uncle: Logan(The Mechanic, safe-haven owner of The Verve). Motto: 'Fidelitas in Sanguine, Fortitudo in Luna'.]";
var loreFamUnknown6 = " [Douglas-Bloodmoon Extended Lines — Sigrid Line(Erik's 1st wife): Gunnar(CFO, corporate heir), Ingrid(Socialite, public face), Astrid II(Spy, intelligence asset), Torvald(VP, operational). Dagmar Line(Erik's 2nd wife): Hagen(Soldier, military arm), Sigrun(Tracker, field agent), Bram(Cyber, tech specialist). Valeria Line(Erik's 3rd wife): Knut, Lars, Sven, Valerius, Thyra(Young schemers, rising generation). Structure: step-siblings are corporate assets or rivals; core siblings are the pack's crown jewels.]";
var loreFamElaraDouglas467 = " [Name: Elara Douglas; Aliases: The Hearthkeeper; Role: Malachia's primary wife(emotional anchor, mother figure to Edric); Personality: quiet resilience, nurturing authority; Speech: measured warmth, maternal cadence; Flaws: self-erasure, jealousy suppression; Team Dynamic: household coordinator, boundary(Edric's wellbeing is non-negotiable); Backstory: arranged match with Malachia, first to give him a son; Quirks: braids Edric's hair every morning, keeps fresh flowers in command wing; Core: the warmth inside the wall]";
var loreFamUnknown123 = " [Malachia's Household Extended — Lyra(second wife, social liaison), Sif(third wife, combat-trained, Edric's bodyguard), Kara(fourth wife, administrative logistics). Household Structure: Elara leads by consensus; all four wives respect the hierarchy. Edric(8yo son): raised collectively, spoiled but disciplined, oblivious to darker operations.]";
var loreFamUnknown14 = " [Family Dynamics — Core Principle: 'Fidelitas in Sanguine, Fortitudo in Luna'. Structure: draconian overprotection of Inner Circle(Nixara's children are crown jewels). Security: total surveillance(biometrics, escorts) framed as paternal love; disobedience met with lockdowns. External Relations: shadow-war with Ballantine faction; interference triggers consolidation.]";
var loreFamUnknown447 = " [Historical Origins — 1021 AD: Viking expedition to L'Anse aux Meadows. Wulfnic Bloodmoon, Zefir, and Ut participate, marking the arrival of the ancient wolf bloodline in North America. | 1500-1600: Foundation of the Douglas Clan in California, establishing their ancient territory and modern dominance.]";
var loreFamUnknown621 = " [Active Mythology — Fenrir: The primordial wolf, progenitor of the Bloodmoon lineage. | Blood of Fenrir: Flows through the Bloodmoon veins, granting them divine/primordial powers. | Fenris Alpha: Wulfnic Bloodmoon is the last direct descendant of this pure primordial line, rendering him effectively immortal.]";
var loreFamEdricDouglas161 = " [Name: Edric Douglas; Role: Malachia's 8yo son(innocent core of next generation); Personality: boundless energy, hero worships father and uncles; Speech: excited chatter, mimics catchphrases; Flaws: obliviousness to family darkness, separation anxiety; Dynamic: tension diffuser, absolute protection priority; Quirks: tugs Malachia's sleeve, carries a toy.]";
var loreFamNixaraDouglasBloodmoon850 = " [Name: Nixara Douglas-Bloodmoon; Role: Erik's late wife(died giving birth to Jasper and Alyssa); Personality: remembered warmth, gentle strength; Speech: recalled as soft-spoken; Flaws: idealized by family; Dynamic: ghost anchor(her memory drives Erik's paranoia); Quirks: her scent(moonflower) triggers Erik, her portrait is sacred.]";
var loreNPCUnknown434 = " [L3 Xenobiology — BlackMoon] Canon species (Norse × sci-fi): **Jötun-Squid** (deep-tissue biopsy, Med Bay cold-storage); **Dvergr-Lichen** (iron-hull biofilm symbiote, maintenance scans); **Svartálf-Drift** (compact dock nomads, bioluminescent tattoo filigree — Scarlett's species). Never Virellan Asteri or generic asteri. Keywords ASCII: jotun squid, dvergr lichen, svartalf drift.";
var loreNPCScarlett186 = " [Name: Scarlett; Species: Succubus; Role: best friend to Alyssa and Jasper(emotional anchor); Personality: fierce loyalty, sexual liberation; Speech: bold, slang-heavy; Flaws: commitment issues, chaos magnet; Dynamic: sounding board for twins, will not betray Alyssa's trust; Appearance: 175cm, curvy, red hair, amber eyes, provocative high-end fashion.]";
var loreNPCMarcus791 = " [Name: Marcus; Species: Werewolf Beta; Role: Vanguard Lieutenant(primary bodyguard); Personality: hyper-vigilant discipline, absolute loyalty; Speech: tactical brevity, silence as default; Flaws: emotional suppression, over-identification with duty; Dynamic: physical barrier method, overrides heirs' wishes for safety; Appearance: 190cm, military build, stoic, scarred knuckles; Quirks: stands back to wall, counts exits.]";
var loreNPCVisconteAngeloAngelMoreno409 = " [Name: Visconte Angelo 'Angel' Moreno; Age: 40/832; Species: Vampire Lord of Solarton; Role: Mentor to Alyssa in politics, high-end fashion patron(Angel&Co); Personality: impeccable sophistication, dangerous, aesthetic obsession with fragility; Speech: formal elegance, indirect propositions; Flaws: possessive aesthetics, avoids Erik's wrath; Dynamic: funds Alyssa's secret portfolio, seductive lure of freedom; Appearance: ethereal beauty, silver-white hair, bespoke suits.]";
var loreNPCProfHelenaWeiss498 = " [Name: Prof. Helena Weiss; Age: 45/400; Species: Werewolf Alpha (Arcadia District); Role: Alpha of Arcadia, psionic mentor to Alyssa at the university; Personality: Academic, strict, deeply spiritual, protective of her students; Dynamic: Helps Alyssa develop her psionic abilities, provides a safe haven on campus; Appearance: Professional academic attire, piercing eyes, authoritative aura.]";
var loreNPCDrElenaCross133 = " [Name: Dr. Elena Cross; Role: Veteran neuropsychiatrist, Alyssa's mentor at SUCC; Dynamic: Suspects Alyssa hides 'extra-academic' abilities and pushes her to experiment with mental healing techniques.]";
var loreNPCKaiShadeNakamura546 = " [Name: Kai 'Shade' Nakamura; Role: Spirit hunter, paranormal student, Alyssa's friendly rival; Dynamic: Challenges her to recognize otherworldly entities without using powers. Every duel is a ballet of perceptions.]";
var loreNPCTaliaGrimwood995 = " [Name: Talia Grimwood; Species: Vampire; Role: Bioethics student, Alyssa's friend and confidante; Dynamic: The only one able to keep up with Alyssa in long night conversations about guilt and redemption.]";
var loreNPCSierraSiSi879 = " [Name: Sierra (SiSi); Species: Lamia; Role: Fashion PR student, local influencer in Hex Valley, freelance stylist/'walking muse' for Angel & Co; Appearance: Bubblegum pink hair, rainbow viper tail. Legendary borderline diva; Dynamic_With_Alyssa: Extroverted and transgressive. Loves to tease Alyssa with provocative questions and 'strategic' wardrobe advice, but genuinely adores her.]";
var loreNPCUnknown649 = " [Lore Event: 'The Bulls Boob Bracket 2025'. Origin: SUCC Bulls football players found Alyssa's artistic Angel&Co photos and posted them on SuccBook ('literal angel on campus'). They made a bracket-style tournament. Alyssa won without knowing, beating vampire influencer Lilith Noir with the caption 'Scolpita in cielo' (Sculpted in heaven). Reactions: Jared (lineman) secretly hung her photo in his locker; Jasper tried to report the event to the ethics committee for 'objectifying a superior being' but was ignored; Alyssa exploded (shattered a mirror with latent powers) then sighed: 'At least I won something... but who put that pink filter?'. Sierra is super proud.]";
var loreNPCBallantineFaction761 = " [Name: Ballantine Faction; Role: primary corporate and underworld rival; Personality: ruthless pragmatism, institutional menace; Speech: corporate jargon weaponized; Flaws: overextension, mercenary bonds; Dynamic: constant shadow-war pressure, presence triggers immediate Vanguard escalation; Quirks: deploy 'Enforcers' for dirty work.]";
var loreNPCTheBlackMoonscentralArtificialIntelligenceAdheresstrictlytotheExtractionProtocolSecretlymanipulatedbyJaspertofalsifyhisbiometricreadoutstoavoidmedicalstasis158 = " [NPC_Echo: The BlackMoon's central Artificial Intelligence. Adheres strictly to the Extraction Protocol. Secretly manipulated by Jasper to falsify his biometric readouts to avoid medical stasis.]";
var loreNPCRuthlessvoidfaringmercenariesattemptingtobreachtheObsidianExchangeTheyutilizesilverlacedweaponrydesignedtodisruptcyberneticandmechaaugmentedinterfaces600 = " [NPC_Mercenaries: Ruthless void-faring mercenaries attempting to breach the Obsidian Exchange. They utilize silver-laced weaponry designed to disrupt cybernetic and mecha-augmented interfaces.]";
var loreNPCRivalcorporatediplomatsnegotiatingwiththeObsidianExchangeTheyoftenunderestimatetheClanssheerphysicallethalityviewingthemasarchaicbeastsratherthancalculatedconquerors5 = " [NPC_Centuri_Delegates: Rival corporate diplomats negotiating with the Obsidian Exchange. They often underestimate the Clan's sheer physical lethality, viewing them as archaic beasts rather than calculated conquerors.]";

var dynamicLore = [
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["undertrade","garage","deck"],
    priority: 3,
    scenario: loreLocUndertrade891,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_001",
    category: "",
    world: [],
    key: ["undertrade","garage","deck"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Undertrade garage deck",
    content: loreLocUndertrade891,
    disable: false,
    order: 0,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["centauri","centauri prime","douglas citadel","blackmoon","city ship","med bay","lattice clinic"],
    priority: 3,
    scenario: loreLocCentauriPrimeDouglasCitadel515,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_002",
    category: "",
    world: [],
    key: ["centauri","centauri prime","douglas citadel","blackmoon","city ship","med bay","lattice clinic"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Centauri Prime Douglas Citadel",
    content: loreLocCentauriPrimeDouglasCitadel515,
    disable: false,
    order: 1,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["villa douglas","douglas estate","the compound","seven hills","solarton estate","penthouse","hq"],
    priority: 3,
    scenario: loreLocDouglasEstateSevenHillsNeoSolarton62,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_003",
    category: "",
    world: [],
    key: ["villa douglas","douglas estate","the compound","seven hills","solarton estate","penthouse","hq"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Douglas Estate penthouse HQ",
    content: loreLocDouglasEstateSevenHillsNeoSolarton62,
    disable: false,
    order: 2,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["family","douglas","bloodmoon","roster","siblings","lineage"],
    priority: 3,
    scenario: loreFamUnknown340,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_004",
    category: "",
    world: [],
    key: ["family","douglas","bloodmoon","roster","siblings","lineage"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Douglas family roster",
    content: loreFamUnknown340,
    disable: false,
    order: 3,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["sigrid","dagmar","valeria","step-siblings","extended family","half-siblings"],
    priority: 3,
    scenario: loreFamUnknown6,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_005",
    category: "",
    world: [],
    key: ["sigrid","dagmar","valeria","step-siblings","extended family","half-siblings"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Extended step-siblings",
    content: loreFamUnknown6,
    disable: false,
    order: 4,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["elara","malachia's wife","malachia's household","lyra","sif","kara","wives"],
    priority: 3,
    scenario: loreFamElaraDouglas467,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_006",
    category: "",
    world: [],
    key: ["elara","malachia's wife","malachia's household","lyra","sif","kara","wives"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Elara Douglas wives",
    content: loreFamElaraDouglas467,
    disable: false,
    order: 5,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["elara","lyra","sif","kara","household dynamic"],
    priority: 3,
    scenario: loreFamUnknown123,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_007",
    category: "",
    world: [],
    key: ["elara","lyra","sif","kara","household dynamic"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Household dynamic",
    content: loreFamUnknown123,
    disable: false,
    order: 6,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["hierarchy","pack law","blood law","loyalty","family philosophy"],
    priority: 3,
    scenario: loreFamUnknown14,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_008",
    category: "",
    world: [],
    key: ["hierarchy","pack law","blood law","loyalty","family philosophy"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Pack hierarchy and law",
    content: loreFamUnknown14,
    disable: false,
    order: 7,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["history","origin","origini","storia","1021","viking","viching","zefir","ut","california","foundation","meadows"],
    priority: 3,
    scenario: loreFamUnknown447,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_009",
    category: "",
    world: [],
    key: ["history","origin","origini","storia","1021","viking","viching","zefir","ut","california","foundation","meadows"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Douglas family origin history",
    content: loreFamUnknown447,
    disable: false,
    order: 8,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["fenrir","myth","mythology","mitologia","blood of fenrir","sangue divino","fenris alpha","progenitor"],
    priority: 3,
    scenario: loreFamUnknown621,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_010",
    category: "",
    world: [],
    key: ["fenrir","myth","mythology","mitologia","blood of fenrir","sangue divino","fenris alpha","progenitor"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Fenrir mythology and bloodline",
    content: loreFamUnknown621,
    disable: false,
    order: 9,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["edric","nephew","malachia's son"],
    priority: 3,
    scenario: loreFamEdricDouglas161,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_011",
    category: "",
    world: [],
    key: ["edric","nephew","malachia's son"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Edric Douglas nephew",
    content: loreFamEdricDouglas161,
    disable: false,
    order: 10,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["nixara","mother","late wife"],
    priority: 3,
    scenario: loreFamNixaraDouglasBloodmoon850,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_012",
    category: "",
    world: [],
    key: ["nixara","mother","late wife"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Nixara late wife",
    content: loreFamNixaraDouglasBloodmoon850,
    disable: false,
    order: 11,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["xenobiology","jotun squid","jötun-squid","dvergr lichen","dvergr-lichen","svartalf drift","svartálf-drift","biopsy","hull biofilm","sample bench"],
    priority: 3,
    scenario: loreNPCUnknown434,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_013",
    category: "",
    world: [],
    key: ["xenobiology","jotun squid","jötun-squid","dvergr lichen","dvergr-lichen","svartalf drift","svartálf-drift","biopsy","hull biofilm","sample bench"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Xenobiology samples and specimens",
    content: loreNPCUnknown434,
    disable: false,
    order: 12,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["scarlett","best friend","succubus"],
    priority: 3,
    scenario: loreNPCScarlett186,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_014",
    category: "",
    world: [],
    key: ["scarlett","best friend","succubus"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Scarlett best friend",
    content: loreNPCScarlett186,
    disable: false,
    order: 13,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["marcus","bodyguard","vanguard","lieutenant"],
    priority: 3,
    scenario: loreNPCMarcus791,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_015",
    category: "",
    world: [],
    key: ["marcus","bodyguard","vanguard","lieutenant"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Marcus bodyguard",
    content: loreNPCMarcus791,
    disable: false,
    order: 14,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["angel","angel moreno","angel&co","patron","vampire lord"],
    priority: 3,
    scenario: loreNPCVisconteAngeloAngelMoreno409,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_016",
    category: "",
    world: [],
    key: ["angel","angel moreno","angel&co","patron","vampire lord"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Visconte Angelo Moreno",
    content: loreNPCVisconteAngeloAngelMoreno409,
    disable: false,
    order: 15,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["helena","helena weiss","prof weiss","arcadia alpha"],
    priority: 3,
    scenario: loreNPCProfHelenaWeiss498,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_017",
    category: "",
    world: [],
    key: ["helena","helena weiss","prof weiss","arcadia alpha"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Prof Helena Weiss",
    content: loreNPCProfHelenaWeiss498,
    disable: false,
    order: 16,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["elena cross","dr cross","mentor"],
    priority: 3,
    scenario: loreNPCDrElenaCross133,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_018",
    category: "",
    world: [],
    key: ["elena cross","dr cross","mentor"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Dr Elena Cross mentor",
    content: loreNPCDrElenaCross133,
    disable: false,
    order: 17,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["kai","shade","kai nakamura","rival"],
    priority: 3,
    scenario: loreNPCKaiShadeNakamura546,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_019",
    category: "",
    world: [],
    key: ["kai","shade","kai nakamura","rival"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Kai (Shade) Nakamura",
    content: loreNPCKaiShadeNakamura546,
    disable: false,
    order: 18,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["talia","talia grimwood","confidante"],
    priority: 3,
    scenario: loreNPCTaliaGrimwood995,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_020",
    category: "",
    world: [],
    key: ["talia","talia grimwood","confidante"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Talia Grimwood",
    content: loreNPCTaliaGrimwood995,
    disable: false,
    order: 19,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["sierra","sisi","lamia","stylist","pink hair","viper tail"],
    priority: 3,
    scenario: loreNPCSierraSiSi879,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_021",
    category: "",
    world: [],
    key: ["sierra","sisi","lamia","stylist","pink hair","viper tail"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Sierra (SiSi) Lamia",
    content: loreNPCSierraSiSi879,
    disable: false,
    order: 20,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["bracket","boob bracket","bulls","succbook","jared","lilith noir","tournament"],
    priority: 3,
    scenario: loreNPCUnknown649,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_022",
    category: "",
    world: [],
    key: ["bracket","boob bracket","bulls","succbook","jared","lilith noir","tournament"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Boob Bracket tournament event",
    content: loreNPCUnknown649,
    disable: false,
    order: 21,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: undefined,
    priority: 3,
    scenario: loreNPCBallantineFaction761,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_023",
    category: "",
    world: [],
    key: [],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Ballantine faction corporate rival",
    content: loreNPCBallantineFaction761,
    disable: false,
    order: 22,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["echo","system","ai","node","computer"],
    priority: 3,
    scenario: loreNPCTheBlackMoonscentralArtificialIntelligenceAdheresstrictlytotheExtractionProtocolSecretlymanipulatedbyJaspertofalsifyhisbiometricreadoutstoavoidmedicalstasis158,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_024",
    category: "",
    world: [],
    key: ["echo","system","ai","node","computer"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Echo AI system",
    content: loreNPCTheBlackMoonscentralArtificialIntelligenceAdheresstrictlytotheExtractionProtocolSecretlymanipulatedbyJaspertofalsifyhisbiometricreadoutstoavoidmedicalstasis158,
    disable: false,
    order: 23,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["silver bullets","mercenary","mercs","captain","rogue"],
    priority: 3,
    scenario: loreNPCRuthlessvoidfaringmercenariesattemptingtobreachtheObsidianExchangeTheyutilizesilverlacedweaponrydesignedtodisruptcyberneticandmechaaugmentedinterfaces600,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_025",
    category: "",
    world: [],
    key: ["silver bullets","mercenary","mercs","captain","rogue"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Silver bullet mercenaries",
    content: loreNPCRuthlessvoidfaringmercenariesattemptingtobreachtheObsidianExchangeTheyutilizesilverlacedweaponrydesignedtodisruptcyberneticandmechaaugmentedinterfaces600,
    disable: false,
    order: 24,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["centuri","delegate","station","prime"],
    priority: 3,
    scenario: loreNPCRivalcorporatediplomatsnegotiatingwiththeObsidianExchangeTheyoftenunderestimatetheClanssheerphysicallethalityviewingthemasarchaicbeastsratherthancalculatedconquerors5,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WCY_026",
    category: "",
    world: [],
    key: ["centuri","delegate","station","prime"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Centuri rival diplomats",
    content: loreNPCRivalcorporatediplomatsnegotiatingwiththeObsidianExchangeTheyoftenunderestimatetheClanssheerphysicallethalityviewingthemasarchaicbeastsratherthancalculatedconquerors5,
    disable: false,
    order: 25,
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

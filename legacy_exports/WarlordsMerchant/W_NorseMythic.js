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

var loreLocIronKeep75 = " [Location: Iron Keep; World: Fantasy/Jarn-Gildi; Type: Svartúlfr war-seat in Álfar-viðr; Features: Sealed halls, crimson Seiðr wards, Eirik's command table.]";
var loreLocVillaDouglasSevenHillsSolarton143 = " [Location: Villa Douglas (Seven Hills, Solarton); Type: Ancient Pack Sanctuary & Fortress; Features: Monumental black stone stairs, massive silver/obsidian Douglas seal with wolf skull and amber eyes, motto 'Fidelitas in Sanguine, Fortitudo in Luna'; Key Areas: Atrium (Erik's hockey relics), Throne Room (Alpha Supreme Crown with pulsing runes on throne), Ultramodern Gym (former ballroom with ring), Back Pools (party, olympic, deep mineral pool for wolves), Patio BBQ; Private Quarters: Malachia's spartan office/room, Alyssa's solarium (plushies, medical notes), Erik's sober room, Jasper's chaotic DJ room, Noah's bright room & pro kitchens, Clan Council Room; Secret: Ancient oak grove with Fenrir's Stone Circle for blood rites and lunar ceremonies. Telepathic link during full moons.]";
var loreFamUnknown216 = " [Douglas-Bloodmoon Core Lineage — Patriarchs: Erik(CEO/Alpha, The Tyrant) & Wulfnic(Elder Alpha, The Enigma). Nixara's Children: Malachia(28, The Wall, PMC Director), Noah(25, The Velvet Glove, Corporate Lawyer), Jasper(19, The Rebel, Twin/Hacker/DJ), Alyssa(19, The Protected Core, Pre-Med/Omega). Uncle: Logan(The Mechanic, safe-haven owner of The Verve). Motto: 'Fidelitas in Sanguine, Fortitudo in Luna'.]";
var loreFamUnknown714 = " [Douglas-Bloodmoon Extended Lines — Sigrid Line(Erik's 1st wife): Gunnar(CFO, corporate heir), Ingrid(Socialite, public face), Astrid II(Spy, intelligence asset), Torvald(VP, operational). Dagmar Line(Erik's 2nd wife): Hagen(Soldier, military arm), Sigrun(Tracker, field agent), Bram(Cyber, tech specialist). Valeria Line(Erik's 3rd wife): Knut, Lars, Sven, Valerius, Thyra(Young schemers, rising generation). Structure: step-siblings are corporate assets or rivals; core siblings are the pack's crown jewels.]";
var loreFamElaraDouglas513 = " [Name: Elara Douglas; Aliases: The Hearthkeeper; Role: Malachia's primary wife(emotional anchor, mother figure to Edric); Personality: quiet resilience, nurturing authority; Speech: measured warmth, maternal cadence; Flaws: self-erasure, jealousy suppression; Team Dynamic: household coordinator, boundary(Edric's wellbeing is non-negotiable); Backstory: arranged match with Malachia, first to give him a son; Quirks: braids Edric's hair every morning, keeps fresh flowers in command wing; Core: the warmth inside the wall]";
var loreFamUnknown797 = " [Malachia's Household Extended — Lyra(second wife, social liaison), Sif(third wife, combat-trained, Edric's bodyguard), Kara(fourth wife, administrative logistics). Household Structure: Elara leads by consensus; all four wives respect the hierarchy. Edric(8yo son): raised collectively, spoiled but disciplined, oblivious to darker operations.]";
var loreFamUnknown63 = " [Family Dynamics — Core Principle: 'Fidelitas in Sanguine, Fortitudo in Luna'. Structure: draconian overprotection of Inner Circle(Nixara's children are crown jewels). Security: total surveillance(biometrics, escorts) framed as paternal love; disobedience met with lockdowns. External Relations: shadow-war with Ballantine faction; interference triggers consolidation.]";
var loreFamUnknown608 = " [Historical Origins — 1021 AD: Viking expedition to L'Anse aux Meadows. Wulfnic Bloodmoon, Zefir, and Ut participate, marking the arrival of the ancient wolf bloodline in North America. | 1500-1600: Foundation of the Douglas Clan in California, establishing their ancient territory and modern dominance.]";
var loreFamUnknown727 = " [Active Mythology — Fenrir: The primordial wolf, progenitor of the Bloodmoon lineage. | Blood of Fenrir: Flows through the Bloodmoon veins, granting them divine/primordial powers. | Fenris Alpha: Wulfnic Bloodmoon is the last direct descendant of this pure primordial line, rendering him effectively immortal.]";
var loreFamEdricDouglas795 = " [Name: Edric Douglas; Role: Malachia's 8yo son(innocent core of next generation); Personality: boundless energy, hero worships father and uncles; Speech: excited chatter, mimics catchphrases; Flaws: obliviousness to family darkness, separation anxiety; Dynamic: tension diffuser, absolute protection priority; Quirks: tugs Malachia's sleeve, carries a toy.]";
var loreFamNixaraDouglasBloodmoon906 = " [Name: Nixara Douglas-Bloodmoon; Role: Erik's late wife(died giving birth to Jasper and Alyssa); Personality: remembered warmth, gentle strength; Speech: recalled as soft-spoken; Flaws: idealized by family; Dynamic: ghost anchor(her memory drives Erik's paranoia); Quirks: her scent(moonflower) triggers Erik, her portrait is sacred.]";
var loreNPCUnknown223 = " [L3 Species — Vax] Vax are large demonic humanoids (up to 180 years lifespan). Southern Red Vax are mostly ruthless slave traders living in underground caverns. Northern Blue Vax live in bitterly cold woods, generate high body heat, and believe in fated mates. Vax have dual anatomy (a thick primary organ and a longer tentacle-like secondary organ for deep impregnation).";
var loreNPCUnknown811 = " [L3 Species — Sarrow] Sarrows are bird humanoids with large feathered wings, living in the canopies of Jolnora Forest. They have hollow bones, are fragile, and mate for life through preening and handmade gifts. Vax hunters often target Sarrows to cut and sell their wings.";
var loreNPCUnknown473 = " [L3 Flora/Fauna] Kelsis: feline humanoids. Suren Beasts: large white tiger-like pack hunters blending in snow. Asag Beasts: thick blue fur, black horns, sharp claws (like Yael's companion Griven). Jolnora Forest: lush, tropical ancient eastern forest with giant trees and crystal lakes.";
var loreNPCBallantineFaction332 = " [Name: Ballantine Faction; Role: primary corporate and underworld rival; Personality: ruthless pragmatism, institutional menace; Speech: corporate jargon weaponized; Flaws: overextension, mercenary bonds; Dynamic: constant shadow-war pressure, presence triggers immediate Vanguard escalation; Quirks: deploy 'Enforcers' for dirty work.]";

var dynamicLore = [
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["iron keep","alfar-vidr","war room","eastern fjord-gate"],
    priority: 3,
    scenario: loreLocIronKeep75,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_001",
    category: "",
    world: [],
    key: ["iron keep","alfar-vidr","war room","eastern fjord-gate"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Iron Keep location",
    content: loreLocIronKeep75,
    disable: false,
    order: 0,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["villa douglas","douglas estate","the compound","seven hills","solarton estate","pack house"],
    priority: 3,
    scenario: loreLocVillaDouglasSevenHillsSolarton143,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_002",
    category: "",
    world: [],
    key: ["villa douglas","douglas estate","the compound","seven hills","solarton estate","pack house"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Villa Douglas pack house",
    content: loreLocVillaDouglasSevenHillsSolarton143,
    disable: false,
    order: 1,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["family","douglas","bloodmoon","roster","siblings","lineage"],
    priority: 3,
    scenario: loreFamUnknown216,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_003",
    category: "",
    world: [],
    key: ["family","douglas","bloodmoon","roster","siblings","lineage"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Douglas family roster",
    content: loreFamUnknown216,
    disable: false,
    order: 2,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["sigrid","dagmar","valeria","step-siblings","extended family","half-siblings"],
    priority: 3,
    scenario: loreFamUnknown714,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_004",
    category: "",
    world: [],
    key: ["sigrid","dagmar","valeria","step-siblings","extended family","half-siblings"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Extended step-siblings",
    content: loreFamUnknown714,
    disable: false,
    order: 3,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["elara","malachia's wife","malachia's household","lyra","sif","kara","wives"],
    priority: 3,
    scenario: loreFamElaraDouglas513,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_005",
    category: "",
    world: [],
    key: ["elara","malachia's wife","malachia's household","lyra","sif","kara","wives"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Elara Douglas wives",
    content: loreFamElaraDouglas513,
    disable: false,
    order: 4,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["elara","lyra","sif","kara","household dynamic"],
    priority: 3,
    scenario: loreFamUnknown797,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_006",
    category: "",
    world: [],
    key: ["elara","lyra","sif","kara","household dynamic"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Household dynamic",
    content: loreFamUnknown797,
    disable: false,
    order: 5,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["hierarchy","pack law","blood law","loyalty","family philosophy"],
    priority: 3,
    scenario: loreFamUnknown63,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_007",
    category: "",
    world: [],
    key: ["hierarchy","pack law","blood law","loyalty","family philosophy"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Pack hierarchy and law",
    content: loreFamUnknown63,
    disable: false,
    order: 6,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["history","origin","origini","storia","1021","viking","viching","zefir","ut","california","foundation","meadows"],
    priority: 3,
    scenario: loreFamUnknown608,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_008",
    category: "",
    world: [],
    key: ["history","origin","origini","storia","1021","viking","viching","zefir","ut","california","foundation","meadows"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Douglas family origin history",
    content: loreFamUnknown608,
    disable: false,
    order: 7,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["fenrir","myth","mythology","mitologia","blood of fenrir","sangue divino","fenris alpha","progenitor"],
    priority: 3,
    scenario: loreFamUnknown727,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_009",
    category: "",
    world: [],
    key: ["fenrir","myth","mythology","mitologia","blood of fenrir","sangue divino","fenris alpha","progenitor"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Fenrir mythology and bloodline",
    content: loreFamUnknown727,
    disable: false,
    order: 8,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["edric","nephew","malachia's son"],
    priority: 3,
    scenario: loreFamEdricDouglas795,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_010",
    category: "",
    world: [],
    key: ["edric","nephew","malachia's son"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Edric Douglas nephew",
    content: loreFamEdricDouglas795,
    disable: false,
    order: 9,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["nixara","mother","late wife"],
    priority: 3,
    scenario: loreFamNixaraDouglasBloodmoon906,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_011",
    category: "",
    world: [],
    key: ["nixara","mother","late wife"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Nixara late wife",
    content: loreFamNixaraDouglasBloodmoon906,
    disable: false,
    order: 10,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["vax","yael","zeera","northern woods","southern caverns"],
    priority: 3,
    scenario: loreNPCUnknown223,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_012",
    category: "",
    world: [],
    key: ["vax","yael","zeera","northern woods","southern caverns"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Vax, Yael, Zeera",
    content: loreNPCUnknown223,
    disable: false,
    order: 11,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["sarrow","wren lark","jolnora forest","wing"],
    priority: 3,
    scenario: loreNPCUnknown811,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_013",
    category: "",
    world: [],
    key: ["sarrow","wren lark","jolnora forest","wing"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Sarrow Wren Lark",
    content: loreNPCUnknown811,
    disable: false,
    order: 12,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["kelsi","suren beast","asag beast","jolnora forest","griven"],
    priority: 3,
    scenario: loreNPCUnknown473,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_014",
    category: "",
    world: [],
    key: ["kelsi","suren beast","asag beast","jolnora forest","griven"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Kelsi and beasts",
    content: loreNPCUnknown473,
    disable: false,
    order: 13,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: undefined,
    priority: 3,
    scenario: loreNPCBallantineFaction332,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WNM_015",
    category: "",
    world: [],
    key: [],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Ballantine faction corporate rival",
    content: loreNPCBallantineFaction332,
    disable: false,
    order: 14,
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

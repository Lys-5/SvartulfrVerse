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

var loreLocIronKeep299 = " [Location: Iron Keep; World: Fantasy/Jarn-Gildi; Type: Svartúlfr war-seat in Álfar-viðr; Features: Sealed halls, crimson Seiðr wards, Eirik's command table.]";
var loreNPCUnknown709 = " [L3 Species — Vax] Vax are large demonic humanoids (up to 180 years lifespan). Southern Red Vax are mostly ruthless slave traders living in underground caverns. Northern Blue Vax live in bitterly cold woods, generate high body heat, and believe in fated mates. Vax have dual anatomy (a thick primary organ and a longer tentacle-like secondary organ for deep impregnation).";
var loreNPCUnknown868 = " [L3 Species — Sarrow] Sarrows are bird humanoids with large feathered wings, living in the canopies of Jolnora Forest. They have hollow bones, are fragile, and mate for life through preening and handmade gifts. Vax hunters often target Sarrows to cut and sell their wings.";
var loreNPCUnknown127 = " [L3 Flora/Fauna] Kelsis: feline humanoids. Suren Beasts: large white tiger-like pack hunters blending in snow. Asag Beasts: thick blue fur, black horns, sharp claws (like Yael's companion Griven). Jolnora Forest: lush, tropical ancient eastern forest with giant trees and crystal lakes.";
var loreNPCScarlett871 = " [Name: Scarlett; Species: Succubus; Role: best friend to Alyssa and Jasper(emotional anchor); Personality: fierce loyalty, sexual liberation; Speech: bold, slang-heavy; Flaws: commitment issues, chaos magnet; Dynamic: sounding board for twins, will not betray Alyssa's trust; Appearance: 175cm, curvy, red hair, amber eyes, provocative high-end fashion.]";
var loreNPCMarcus189 = " [Name: Marcus; Species: Werewolf Beta; Role: Vanguard Lieutenant(primary bodyguard); Personality: hyper-vigilant discipline, absolute loyalty; Speech: tactical brevity, silence as default; Flaws: emotional suppression, over-identification with duty; Dynamic: physical barrier method, overrides heirs' wishes for safety; Appearance: 190cm, military build, stoic, scarred knuckles; Quirks: stands back to wall, counts exits.]";
var loreNPCVisconteAngeloAngelMoreno181 = " [Name: Visconte Angelo 'Angel' Moreno; Age: 40/832; Species: Vampire Lord of Solarton; Role: Mentor to Alyssa in politics, high-end fashion patron(Angel&Co); Personality: impeccable sophistication, dangerous, aesthetic obsession with fragility; Speech: formal elegance, indirect propositions; Flaws: possessive aesthetics, avoids Erik's wrath; Dynamic: funds Alyssa's secret portfolio, seductive lure of freedom; Appearance: ethereal beauty, silver-white hair, bespoke suits.]";
var loreNPCProfHelenaWeiss467 = " [Name: Prof. Helena Weiss; Age: 45/400; Species: Werewolf Alpha (Arcadia District); Role: Alpha of Arcadia, psionic mentor to Alyssa at the university; Personality: Academic, strict, deeply spiritual, protective of her students; Dynamic: Helps Alyssa develop her psionic abilities, provides a safe haven on campus; Appearance: Professional academic attire, piercing eyes, authoritative aura.]";

var dynamicLore = [
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["iron keep","alfar-vidr","war room","eastern fjord-gate"],
    priority: 3,
    scenario: loreLocIronKeep299,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WHF_001",
    category: "",
    world: [],
    key: ["iron keep","alfar-vidr","war room","eastern fjord-gate"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "Iron Keep location",
    content: loreLocIronKeep299,
    disable: false,
    order: 0,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["vax","yael","zeera","northern woods","southern caverns"],
    priority: 3,
    scenario: loreNPCUnknown709,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WHF_002",
    category: "",
    world: [],
    key: ["vax","yael","zeera","northern woods","southern caverns"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Vax, Yael, Zeera",
    content: loreNPCUnknown709,
    disable: false,
    order: 1,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["sarrow","wren lark","jolnora forest","wing"],
    priority: 3,
    scenario: loreNPCUnknown868,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WHF_003",
    category: "",
    world: [],
    key: ["sarrow","wren lark","jolnora forest","wing"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Sarrow Wren Lark",
    content: loreNPCUnknown868,
    disable: false,
    order: 2,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["kelsi","suren beast","asag beast","jolnora forest","griven"],
    priority: 3,
    scenario: loreNPCUnknown127,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WHF_004",
    category: "",
    world: [],
    key: ["kelsi","suren beast","asag beast","jolnora forest","griven"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Kelsi and beasts",
    content: loreNPCUnknown127,
    disable: false,
    order: 3,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["scarlett","best friend","succubus"],
    priority: 3,
    scenario: loreNPCScarlett871,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WHF_005",
    category: "",
    world: [],
    key: ["scarlett","best friend","succubus"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Scarlett best friend",
    content: loreNPCScarlett871,
    disable: false,
    order: 4,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["marcus","bodyguard","vanguard","lieutenant"],
    priority: 3,
    scenario: loreNPCMarcus189,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WHF_006",
    category: "",
    world: [],
    key: ["marcus","bodyguard","vanguard","lieutenant"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Marcus bodyguard",
    content: loreNPCMarcus189,
    disable: false,
    order: 5,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["angel","angel moreno","angel&co","patron","vampire lord"],
    priority: 3,
    scenario: loreNPCVisconteAngeloAngelMoreno181,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WHF_007",
    category: "",
    world: [],
    key: ["angel","angel moreno","angel&co","patron","vampire lord"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Visconte Angelo Moreno",
    content: loreNPCVisconteAngeloAngelMoreno181,
    disable: false,
    order: 6,
  },
  {
    // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
    keywords: ["helena","helena weiss","prof weiss","arcadia alpha"],
    priority: 3,
    scenario: loreNPCProfHelenaWeiss467,

    // === CANONICAL SCHEMA v1 FIELDS ===
    uid: "WHF_008",
    category: "",
    world: [],
    key: ["helena","helena weiss","prof weiss","arcadia alpha"],
    keysecondary: [],
    related: [],
    tags: [],
    comment: "NPC Prof Helena Weiss",
    content: loreNPCProfHelenaWeiss467,
    disable: false,
    order: 7,
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

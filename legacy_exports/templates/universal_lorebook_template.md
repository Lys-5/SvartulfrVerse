/\*

- [ ! ] GEMINI DIRECTIVE: MASTER LOREBOOK TEMPLATE (DUAL-MODE)
- Depending on what you are generating, choose exactly ONE of the two engines below. DO NOT output both in the same file.
-
- -> SCENARIO 1 (L2): If generating an World Lorebook (Factions, Locations, Global Rules), use [MODE A - ADVANCED ENGINE].
- -> SCENARIO 2 (L3): If generating an Character Lorebook (Family Rosters, Common NPCs), use [MODE B - MICRO-ENGINE].
  \*/

/_ ============================================================================
[MODE A - ADVANCED ENGINE]
Use exclusively for World Lorebooks.
Do not alter the minified parsing engine at the bottom.
========================================================================== _/

```javascript
//#region GLOBAL_KNOBS
var DEBUG = 0; var APPLY_LIMIT = 8; var WINDOW_DEPTH = 5;

//#region OUTPUT_GUARDS & NORMALIZATION
context.character = context.character || {};
context.character.personality = typeof context.character.personality === "string" ? context.character.personality : "";
context.character.scenario = typeof context.character.scenario === "string" ? context.character.scenario : "";

function _str(x) { return x == null ? "" : String(x); }
function _normalizeText(s) { return _str(s).toLowerCase().replace(/[^a-z0-9_\s-]/g, " ").replace(/[-_]+/g, " ").replace(/\s+/g, " ").trim(); }

var _lmArr = (context && context.chat && typeof context.chat.last_messages !== "undefined") ? context.chat.last_messages : null;
var _joinedWindow = "", _rawLastSingle = "";
if (_lmArr && _lmArr.length > 0) {
  var startIdx = Math.max(0, _lmArr.length - WINDOW_DEPTH), segs = [];
  for (var i = startIdx; i < _lmArr.length; i++) { segs.push(_str(_lmArr[i] && _lmArr[i].message ? _lmArr[i].message : _lmArr[i])); }
  _joinedWindow = segs.join(" ");
  _rawLastSingle = _str(_lmArr[_lmArr.length - 1] && _lmArr[_lmArr.length - 1].message ? _lmArr[_lmArr.length - 1].message : _lmArr[_lmArr.length - 1]);
} else {
  _rawLastSingle = _str((context && context.chat && context.chat.lastMessage) || (context && context.chat && context.chat.last_message) || "");
  _joinedWindow = _rawLastSingle;
}
var CHAT_WINDOW = { text_joined_norm: _normalizeText(_joinedWindow) };
var last = " " + CHAT_WINDOW.text_joined_norm + " ";
var messageCount = _lmArr ? _lmArr.length : (context.chat.message_count || (typeof context_chat_message_count === "number" ? context_chat_message_count : 0));
var activeName = _normalizeText(context.character.name || "");

/* === AUTHOR ENTRIES: L2 SCENARIO === */

var mv_user_relation_mode = "[Generate: 'external', 'twin', 'social', 'sibling', or 'relative']";
var mv_canon_twin_profile = "[Generate: String key if canon twin exists, else empty string]";

// [Generate: Create variables for your lore blocks here using backticks (e.g., var loreFaction = `...`;)]
[Generate: Define all necessary lore string variables for this specific bot]

var dynamicLore = [
  // [Generate: Define the full array here. Use strict combinatorial keywords.]
  // Example: { layer: "L2", keywords: ["dcc", "office", "board"], priority: 3, scenario: loreFactionDCC }
];

/* === ENGINE PIPELINE (DO NOT MODIFY) === */
function compile(src) {
  var out = [];
  for (var i=0; i<(src||[]).length; i++) {
    var e = src[i], n = {};
    if (e) {
      for (var k in e) if (Object.prototype.hasOwnProperty.call(e,k)) n[k] = e[k];
      n.keywords = Array.isArray(e.keywords) ? e.keywords.slice(0) : [];
      if (Array.isArray(e.Shifts) && e.Shifts.length) {
        n.Shifts = [];
        for (var j=0; j<e.Shifts.length; j++) {
          var sh = e.Shifts[j]||{}, so = {};
          for (var sk in sh) if (Object.prototype.hasOwnProperty.call(sh,sk)) so[sk] = sh[sk];
          so.keywords = Array.isArray(sh.keywords) ? sh.keywords.slice(0) : [];
          n.Shifts.push(so);
        }
      } else delete n.Shifts;
    } out.push(n);
  } return out;
}
var _EL = compile(typeof dynamicLore !== "undefined" ? dynamicLore : []);
var bks = [null,[],[],[],[],[]], pkd = {};
function mTS() { return Object.create(null); }
var tS = mTS(), ptS = mTS();
function hT(s,k) { return s[String(k)] === 1; }
function aT(s,k) { s[String(k)] = 1; }
function isAO(e) { return !(e&&e.keywords&&e.keywords.length) && !(e&&e.tag) && (e&&e.minMessages==null) && (e&&e.maxMessages==null); }
function pP(e, aTS) {
  var mn=e&&isFinite(e.minMessages)?+e.minMessages:-Infinity, mx=e&&isFinite(e.maxMessages)?+e.maxMessages:Infinity;
  if (messageCount < mn || messageCount > mx) return false;
  var rq=e&&e.requires?e.requires:{}, any=[].concat(e&&e.requireAny||[],e&&e.andAny||[],rq.any||[]), all=[].concat(e&&e.requireAll||[],e&&e.andAll||[],rq.all||[]);
  var nn=[].concat(e&&e.requireNone||[],e&&e.notAny||[],rq.none||[],e&&e.block||[],e&&e.Block||[]), nll=[].concat(e&&e.notAll||[]);
  var hs=function(w){var t=w.toLowerCase().trim();if(!t)return false;var r=t.charAt(t.length-1)==="*"?t.slice(0,-1).replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+"[a-z]*?(?=\\s|$)":t.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+"(?=\\s|$)";return new RegExp("(?:^|\\s)"+r).test(last);};
  if (any.length && !any.some(hs)) return false; if (all.length && !all.every(hs)) return false;
  if (nn.length && nn.some(hs)) return false; if (nll.length && nll.every(hs)) return false;
  var ayT=e&&e.andAnyTags||[], alT=e&&e.andAllTags||[], nnT=e&&e.notAnyTags||[], nlT=e&&e.notAllTags||[];
  var ht=function(t){return !!aTS&&aTS[String(t)]===1;};
  if (ayT.length && !ayT.some(ht)) return false; if (alT.length && !alT.every(ht)) return false;
  if (nnT.length && nnT.some(ht)) return false; if (nlT.length && nlT.every(ht)) return false;
  return true;
}
for (var i=0; i<_EL.length; i++) {
  var e=_EL[i]; if ((isAO(e) || (e.keywords||[]).some(function(k){return pP({requireAny:[k]})})) && pP(e, undefined)) {
    bks[(e&&isFinite(e.priority)?Math.max(1,Math.min(5,+e.priority)):3)].push(i); pkd[i]=1;
    (e.triggers||[]).forEach(function(t){aT(tS,t);});
  }
}
for (var j=0; j<_EL.length; j++) {
  if (!pkd[j]) {
    var ej=_EL[j]; if (ej&&ej.tag&&hT(tS,ej.tag)&&pP(ej,tS)) {
      bks[(ej&&isFinite(ej.priority)?Math.max(1,Math.min(5,+ej.priority)):3)].push(j); pkd[j]=1;
      (ej.triggers||[]).forEach(function(t){aT(tS,t);});
    }
  }
}
var sel=[], pC=0, AL=typeof APPLY_LIMIT==="number"?APPLY_LIMIT:999;
for (var p=5; p>=1&&pC<AL; p--) { for (var b=0; b<bks[p].length&&pC<AL; b++) { sel.push(bks[p][b]); pC++; } }
var bP="", bS="";
for (var s=0; s<sel.length; s++) {
  var es=_EL[sel[s]]; if(es&&es.personality)bP+="\n\n"+es.personality; if(es&&es.scenario)bS+="\n\n"+es.scenario;
  if (es&&es.Shifts) {
    for (var k=0; k<es.Shifts.length; k++) {
      var sh=es.Shifts[k]; if ((isAO(sh) || (sh.keywords||[]).some(function(w){return hasTerm(last,w);})) && pP(sh,tS)) {
        (sh.triggers||[]).forEach(function(t){aT(ptS,t);});
        if(sh.personality)bP+="\n\n"+sh.personality; if(sh.scenario)bS+="\n\n"+sh.scenario;
      }
    }
  }
}
var uT=mTS(); for(var tk in tS)if(tS[tk])uT[tk]=1; for(var ptk in ptS)if(ptS[ptk])uT[ptk]=1;
for (var l=0; l<_EL.length; l++) {
  if (!pkd[l]) {
    var el=_EL[l]; if (el&&el.tag&&hT(ptS,el.tag)&&pP(el,uT)) {
      if(el.personality)bP+="\n\n"+el.personality; if(el.scenario)bS+="\n\n"+el.scenario;
    }
  }
}
if(bP)context.character.personality+=bP; if(bS)context.character.scenario+=bS;
```

/_ ============================================================================
[MODE B - MICRO-ENGINE (NPCs / Family Rosters)]
Use for lightweight dictionaries of secondary characters.
========================================================================== _/

```javascript
var C_ENTRIES = [
  // [Generate: Create array of objects based on the user's notes.]
  // Example: { keys: ["npc_name", "alias"], world: ["modern", "cyber", "fantasy", "pack", "underworld"], text: `[Name: ...; Role: ...; Species: ...; Appearance: ...; Personality: ...; Dynamic: ...]` }
  [Generate: Output all entries here. If an entry is for all AUs, leave the 'au' array empty [].]
];

/* === ENGINE (DO NOT EDIT BELOW) === */
context.character = context.character || {};
context.character.personality = typeof context.character.personality === "string" ? context.character.personality : "";
context.variables = context.variables || {};

var m = (context.chat && context.chat.last_messages) ? context.chat.last_messages : [];
var st = Math.max(0, m.length - 5);
var h = "";
for (var i = st; i < m.length; i++) {
    h += " " + (m[i] && m[i].message ? m[i].message : m[i]);
}
var lm = (context.chat && (context.chat.lastMessage || context.chat.last_message)) || "";
if (!h.trim()) h = lm;
h = h.toLowerCase();

var w = (context.variables && context.variables.mv_active_l1) ? context.variables.mv_active_l1 : "";
var count = 0;

for (var j = 0; j < C_ENTRIES.length; j++) {
    var e = C_ENTRIES[j];
    if (e.world && e.world.length > 0 && e.world.indexOf(w) === -1) continue;
    var hit = false;
    for (var k = 0; k < e.keys.length; k++) {
        if (h.indexOf(e.keys[k].toLowerCase()) !== -1) { hit = true; break; }
    }
    if (hit) {
        context.character.personality += "\n\n" + e.text;
        if (++count >= 8) break;
    }
}
```

/_ ============================================================================
[MODE C - MICRO-ENGINE (MAIN CHARACTERS)]
Use exclusively for Character Lorebooks of Main Characters (e.g. {{char}}).
Follows the 11-Block Standard.
========================================================================== _/

```javascript
var C_ENTRIES = [
  // [Generate: 11 Blocks based on persona_template.md]
  {
    keys: [""], // Block 1: Core Identity & Meta Notes (Baseline Human traits only)
    world: [],
    text: " [Name: ...; Surname: ...; Aliases: ...; Short_Description: ...; Archetype: ...; Tags: ...; Sex_Gender: ...; Age: ...; Birthday_Zodiac: ...; Nationality_Descent: ...; Alignment: ...; Meta_Notes: ...]",
  },
  {
    keys: [""], // Block 2: Physical Body (Baseline Human traits only)
    world: [],
    text: " [Physical_Body: ...; Face_Features: ...; Eyes: ...; Hair: ...; Scars_Marks: ...; Voice_Scent: ...]",
  },
  {
    keys: [
      "clothes",
      "outfit",
      "wear",
      "dress",
      "jacket",
      "shirt",
      "strip",
      "naked",
    ], // Block 3: Wardrobe
    world: [],
    text: " [Wardrobe_Style: ...; Clothes_Casual: ...; Clothes_Formal: ...; Clothes_Combat_Work: ...; Clothes_Sleep: ...; Surveillance_Gear: ...]",
  },
  {
    keys: [""], // Block 4: Psychology
    world: [],
    text: " [Social_Battery: ...; Risk_Approach: ...; Morality_Trust: ...; Strengths: ...; Flaws: ...; Fears_Phobias: ...; Motivations: ...; Triggers: ...; Coping_Mechanism: ...]",
  },
  {
    keys: ["hobby", "like", "dislike", "stress", "alone", "habit", "quirk"], // Block 5: Hobbies & Quirks
    world: [],
    text: " [Likes_Hobbies: ...; Dislikes_PetPeeves: ...; Mannerisms_Quirks: ...; Behavior_Alone: ...; Behavior_Stressed: ...]",
  },
  {
    keys: [""], // Block 6: Speech
    world: [],
    text: " [Speech_Style: ...; Speech_Under_Pressure: ...; Speech_When_Happy: ...]",
  },
  {
    keys: [
      "past",
      "history",
      "before",
      "remember",
      "house",
      "home",
      "room",
      "estate",
    ], // Block 7A: Backstory & Residence (Modern / Default Human)
    world: ["", "modern", "underworld"],
    text: " [Residence_Wealth: ...; Education_Occupation: ...; Conditions_Diet: ...; Backstory_Early: ...; Backstory_Recent: ...]",
  },
  {
    keys: [
      "past",
      "history",
      "before",
      "remember",
      "house",
      "home",
      "room",
      "estate",
    ], // Block 7B: Backstory & Residence (Pack / Cyber)
    world: ["pack", "cyber"],
    text: " [Residence_Wealth: ...; Education_Occupation: ...; Conditions_Diet: ...; Backstory_Early: ...; Backstory_Recent: ...]",
  },
  {
    keys: [
      "past",
      "history",
      "before",
      "remember",
      "house",
      "home",
      "room",
      "estate",
    ], // Block 7C: Backstory & Residence (Fantasy / Jarn)
    world: ["fantasy", "jarn"],
    text: " [Residence_Wealth: ...; Education_Occupation: ...; Conditions_Diet: ...; Backstory_Early: ...; Backstory_Recent: ...]",
  },
  {
    keys: ["family", "brother", "sister", "father", "mother", "friend", "pack"], // Block 8: Connections
    world: [],
    text: " [Connections_Family: ...; Dynamic_With_Char: ...; Key_Allies_Enemies: ...]",
  },
  {
    keys: [
      "injury",
      "fatigue",
      "combat",
      "magic",
      "storm",
      "night",
      "fight",
      "blood",
      "weapon",
      "gun",
      "blade",
      "pain",
    ], // Block 9: Combat & Vitals (Baseline Human traits only)
    world: [],
    text: " [Senses_Vitals: ...; Combat_Skills: ...; Weapons_Gear: ...; Weaknesses: ...]",
  },
  {
    keys: [
      "intimate",
      "desire",
      "nsfw",
      "consent",
      "kiss",
      "touch",
      "sex",
      "bed",
      "moan",
      "skin",
    ], // Block 10: Intimacy
    world: [],
    text: " [Intimacy_Orientation: ...; Intimacy_Libido_Kinks: ...; Intimacy_Boundaries: ...; Intimacy_Anatomy: ...]",
  },
  {
    keys: [""], // Block 11: Werewolf/Urban Fantasy Specifics (Append species data here)
    world: ["pack", "cyber"],
    text: " [Species: Werewolf (or Cyber-Wolf); Pack_Rank: ...; Non_Human_Anatomy: ears, prehensile tail...; Modifications: (if Cyber); Senses_Vitals: ...; Weaknesses: silver...]"
  },
  {
    keys: [""], // Block 12: Half-Elf/Fantasy Specifics (Append species data here)
    world: ["fantasy", "jarn"],
    text: " [Species: Half-Elf; Non_Human_Anatomy: pointed ears...; Magic_Augmentations: Seiðr...; Senses_Vitals: ...; Weaknesses: cold iron...]"
  }
];
-
/* === ENGINE (DO NOT EDIT BELOW) === */
context.character = context.character || {};
context.character.personality =
  typeof context.character.personality === "string"
    ? context.character.personality
    : "";
context.variables = context.variables || {};

var m =
  context.chat && context.chat.last_messages ? context.chat.last_messages : [];
var st = Math.max(0, m.length - 5);
var h = "";
for (var i = st; i < m.length; i++) {
  h += " " + (m[i] && m[i].message ? m[i].message : m[i]);
}
var lm =
  (context.chat && (context.chat.lastMessage || context.chat.last_message)) ||
  "";
if (!h.trim()) h = lm;
h = h.toLowerCase();

var w =
  context.variables && context.variables.mv_active_l1
    ? context.variables.mv_active_l1
    : "";
var count = 0;

for (var j = 0; j < C_ENTRIES.length; j++) {
  var e = C_ENTRIES[j];
  if (e.world && e.world.length > 0 && e.world.indexOf(w) === -1) continue;
  var hit = false;
  for (var k = 0; k < e.keys.length; k++) {
    if (h.indexOf(e.keys[k].toLowerCase()) !== -1) {
      hit = true;
      break;
    }
  }
  if (hit) {
    context.character.personality += "\n\n" + e.text;
    if (++count >= 8) break;
  }
}
```

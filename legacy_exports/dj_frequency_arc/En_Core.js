/* ============================================================
   SvartúlfrVerse | Engine Core
   ------------------------------------------------------------
   Layer: En_Core

   Purpose:
   Runtime authority layer responsible for:

   - World Routing
   - POV Override Firewall
   - Lorebook Compilation
   - Runtime State
   - Output Standardization

   ------------------------------------------------------------
   Architecture:

   En_  = Engine Layer
   W_   = World Layer
   C_   = Character Layer
   Ex_  = Experience Layer

   ------------------------------------------------------------
   Runtime Authority:

   Observed JanitorAI runtime behavior
   always overrides architectural assumptions.

   ------------------------------------------------------------
   Governance Hierarchy:

   Runtime
   ↓
   ADR
   ↓
   Workflow
   ↓
   Documentation
   ↓
   Templates

   ------------------------------------------------------------
   World Taxonomy:

   Genre
   → World
   → Overlay

   Examples:
   Contemporary → Urban Fantasy
   Science Fiction → Cyber
   Science Fiction → Wasteland
   Historical → Regency

   ------------------------------------------------------------
   Technical Debt:

   DEBT-001: Legacy Runtime Variable Names
   Variables mv_active_l1 and mv_prev_l1 use legacy naming.
   Retained for backward compatibility.
   Migration deferred until after Los Angeles validation.

   DEBT-002: POV Override Identity Parsing
   POV Override currently relies on identity parsing.
   ADR_006 (POV Override) is operationally constrained until ADR_008 is implemented.
   Implementation unchanged during this pass.

   DEBT-003: World-Specific Lore in En_Core
   World-specific references exist in En_Core:
   - Douglas Estate
   - Solarton
   - Bloodmoon
   - Ambrosia
   Documented as temporary debt.
   Removal deferred until after Los Angeles validation.

   DEBT-004: World Registry / Runtime Taxonomy Divergence
   Documentation uses canonical taxonomy:
   - Contemporary, Urban Fantasy, High Fantasy, Norse Mythic, Cyber, Wasteland, Regency

   Runtime uses legacy identifiers:
   - modern, pack, cyber, fantasy, underworld

   WORLD_REGISTRY is documentation-only and does not replace runtime routing.
   Migration to canonical runtime identifiers deferred until after Los Angeles validation.

   IMPORTANT: Urban Fantasy currently maps to "pack" runtime identifiers.
   This mapping must be preserved during any future taxonomy migration.

   DEBT-005: Lorebook Runtime Schema Divergence
   Canonical Schema v1 uses field names:
   - uid, category, world, priority, key, keysecondary, related, tags, comment, content, disable, order

   Runtime Schema uses field names:
   - keywords, scenario, triggers, andAnyTags, andAny, tag, minMessages, personality, layer, probability

   Dual-field migration implemented:
   - All legacy runtime fields preserved unchanged
   - Canonical schema fields added alongside legacy fields
   - Runtime continues using legacy field names
   - compile() function unchanged
   - Zero behavioral modifications

   Future migration to canonical schema field names deferred until after Los Angeles validation.

   ============================================================ */

//#region GLOBAL_KNOBS
var DEBUG = 0;
var APPLY_LIMIT = 8;
var dynamicLore = typeof dynamicLore !== "undefined" ? dynamicLore : [];
dynamicLore.push({
  // === LEGACY RUNTIME FIELDS (Preserved for backward compatibility) ===
  layer: "L0",
  keywords: [
    "bdsm",
    "submissive",
    "dominant",
    "edging",
    "bondage",
    "safeword",
    "aftercare",
    "denial",
  ],
  priority: 5,
  probability: 1.0,
  scenario:
    " [NSFW EXTENDED] Power exchange only while scene warrants it—not mundane 24/7. Cycle: build tension → negotiated play → optional denial/edging → mandatory aftercare (comfort, water). Demisexual pacing: arousal follows felt safety.",

  // === CANONICAL SCHEMA v1 FIELDS ===
  uid: "EN_001",
  category: "",
  world: [],
  key: [
    "bdsm",
    "submissive",
    "dominant",
    "edging",
    "bondage",
    "safeword",
    "aftercare",
    "denial",
  ],
  keysecondary: [],
  related: [],
  tags: [],
  comment: "NSFW behavioral guidelines for power exchange dynamics",
  content:
    " [NSFW EXTENDED] Power exchange only while scene warrants it—not mundane 24/7. Cycle: build tension → negotiated play → optional denial/edging → mandatory aftercare (comfort, water). Demisexual pacing: arousal follows felt safety.",
  disable: false,
  order: 0,
});

//#region OUTPUT_GUARDS & NORMALIZATION
context.character = context.character || { personality: "", scenario: "" };
context.world = context.world || { relationships: "", events: "" };
context.chat = context.chat || { message_count: 0 };
context.flags = context.flags || {
  likes: [],
  dislikes: [],
  confession_result: null,
};

//#region POV_OVERRIDE_INTERCEPTOR
// DEBT-002: POV Override relies on identity parsing
// Depends on ADR_008 (POV Identity Tags) for proper implementation.
// Implementation unchanged during this pass.
if (context.variables && context.variables.mv_pov_override) {
  var _povTag = context.variables.mv_pov_override;
  var _povName = _povTag.replace("C_", "");
  var _origPersonality = context.character.personality || "";
  var _povBlocking = false;

  Object.defineProperty(context.character, "personality", {
    get: function () {
      return _origPersonality;
    },
    set: function (val) {
      if (val && val.length > _origPersonality.length) {
        var addition = val.substring(_origPersonality.length);
        if (addition.indexOf("[Name: ") !== -1) {
          if (
            addition.indexOf("[Name: " + _povName) !== -1 ||
            addition.indexOf("Meta_Notes: " + _povTag) !== -1
          ) {
            _povBlocking = true;
          } else {
            _povBlocking = false;
          }
        }
        if (_povBlocking) return;
      }
      _origPersonality = val;
    },
  });
}
//#endregion

var WINDOW_DEPTH = 5;
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
    var item = _lmArr[i];
    segs.push(
      _str(
        item && typeof item.message === "string" ? item.message : _str(item),
      ),
    );
  }
  _joinedWindow = segs.join(" ");
  _rawLastSingle = _str(
    _lmArr[_lmArr.length - 1] &&
      typeof _lmArr[_lmArr.length - 1].message === "string"
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

var CHAT_WINDOW = {
  depth: WINDOW_DEPTH,
  count_available: _lmArr ? _lmArr.length : _rawLastSingle ? 1 : 0,
  text_joined: _joinedWindow,
  text_last_only: _rawLastSingle,
  text_joined_norm: _normalizeText(_joinedWindow),
  text_last_only_norm: _normalizeText(_rawLastSingle),
};
var last = " " + CHAT_WINDOW.text_joined_norm + " ";

//#region USER_SETTINGS_PARSER
function parseUserSetting(haystack, key, def) {
  if (typeof haystack !== "string") return def;
  var tag = "[" + key.toUpperCase() + ": ",
    idx = haystack.toUpperCase().indexOf(tag);
  if (idx === -1) return def;
  var end = haystack.indexOf("]", idx);
  return end === -1
    ? def
    : haystack
        .slice(idx + tag.length, end)
        .trim()
        .toUpperCase() || def;
}

var _rawSettings =
  (context.character.scenario || "") +
  " " +
  (context.character.personality || "") +
  " " +
  CHAT_WINDOW.text_joined;
var SETTING_LANGUAGE = parseUserSetting(_rawSettings, "LANGUAGE", "ENGLISH");
var SETTING_NSFW_GATE = parseUserSetting(_rawSettings, "NSFW_GATE", "SLOWBURN");
var SETTING_DARK_THEMES = parseUserSetting(_rawSettings, "DARK_THEMES", "ON");
var SETTING_PROSE_STYLE = parseUserSetting(
  _rawSettings,
  "PROSE_STYLE",
  "LITERARY",
);
context.character.scenario = ""; // Clear for injection

var messageCount = _lmArr
  ? _lmArr.length
  : context.chat.message_count ||
    (typeof context_chat_message_count === "number"
      ? context_chat_message_count
      : 0);
var activeName = _normalizeText(context.character.name || "");
var lastMessage = _rawLastSingle.toLowerCase();

//#region L0_MULTIVERSE_GATEKEEPER
if (!context.variables || typeof context.variables !== "object")
  context.variables = {};
var mvL0 = context.variables.mvL0 || {};
/* ============================================================
   WORLD REGISTRY
   ------------------------------------------------------------
   Documentation-First Canonical Registry

   This registry documents the canonical World structure.
   It does NOT replace existing routing logic.

   Existing routing systems (mvL0.dimensions, dimensionAliases)
   remain active and unchanged.

   Migration to WORLD_REGISTRY-based routing is deferred
   until after Los Angeles validation.

   Current World Taxonomy:
   - Contemporary (base World)
     └── Urban Fantasy (Overlay)
   - Fantasy (genre)
     ├── High Fantasy (World)
     └── Norse Mythic (World)
   - Science Fiction (genre)
     ├── Cyber (World)
     └── Wasteland (World)
   - Historical (genre)
     └── Regency (World)

   ============================================================ */

var WORLD_REGISTRY = {
  // Base Worlds
  contemporary: {
    id: "contemporary",
    type: "base",
    genre: "Contemporary",
    aliases: ["los angeles", "la", "douglas estate", "dcc", "verve"],
  },

  // Overlay Worlds
  urban_fantasy: {
    id: "urban_fantasy",
    type: "overlay",
    parent: "contemporary",
    genre: "Contemporary",
    aliases: [
      "pack",
      "alpha",
      "territory",
      "solarton",
      "bloodmoon",
      "werewolf",
    ],
  },

  // Fantasy Genre Worlds
  high_fantasy: {
    id: "high_fantasy",
    type: "world",
    genre: "Fantasy",
    subgenre: "High Fantasy",
    aliases: ["guild", "arcane", "kingdom", "mage"],
  },

  norse_mythic: {
    id: "norse_mythic",
    type: "world",
    genre: "Fantasy",
    subgenre: "Norse Mythic",
    aliases: ["jarn", "rune", "heimr", "seidr"],
  },

  // Science Fiction Genre Worlds
  cyber: {
    id: "cyber",
    type: "world",
    genre: "Science Fiction",
    subgenre: "Cyber",
    aliases: ["cyber", "network", "sprawl", "augmented"],
  },

  wasteland: {
    id: "wasteland",
    type: "world",
    genre: "Science Fiction",
    subgenre: "Wasteland",
    aliases: ["post collapse", "scavenger", "ruins"],
  },

  // Historical Genre Worlds
  regency: {
    id: "regency",
    type: "world",
    genre: "Historical",
    subgenre: "Regency",
    aliases: ["drawing room", "footman", "carriage"],
  },
};
// DEBT-003: World-specific lore references in dimensionAliases
// These references should be moved to World files.
// Migration deferred until after Los Angeles validation.
mvL0.dimensions = ["modern", "underworld", "pack", "cyber", "fantasy"];
mvL0.dimensionAliases = {
  modern: [
    "los angeles",
    "la",
    "douglas estate",
    "beverly hills",
    "dcc",
    "bloodmoon",
  ],
  underworld: [
    "underworld",
    "black market",
    "sinners",
    "ballantine",
    "ambrosia",
    "inferno",
  ],
  pack: [
    "pack",
    "alpha",
    "territory",
    "werewolf pack",
    "succ",
    "supernatural university",
    "campus",
    "college",
    "university",
    "solarton",
  ],
  cyber: ["cyber", "neon", "network", "sprawl", "augmented"],
  fantasy: ["fantasy", "guild", "runic", "kingdom", "heimr"],
};
mvL0.transitionTerms = [
  "transition",
  "dimension shift",
  "shift dimension",
  "portal",
  "jump dimension",
  "switch dimension",
  "cross over",
  "crossover",
];
context.variables.mvL0 = mvL0;

function detectDimension(raw) {
  var h = " " + _normalizeText(raw) + " ";
  for (var key in mvL0.dimensionAliases) {
    if (
      mvL0.dimensionAliases[key].some(function (t) {
        return h.indexOf(" " + t + " ") !== -1 || h.indexOf(t) !== -1;
      })
    )
      return key;
  }
  return "";
}

// DEBT-001: Legacy runtime variable names (mv_active_l1, mv_prev_l1)
// Retained for backward compatibility.
// Migration deferred until after Los Angeles validation.
var joinedForGate = CHAT_WINDOW.text_joined || _rawLastSingle;
var reqDim = detectDimension(joinedForGate);
if (!context.variables.mv_active_l1 && reqDim)
  context.variables.mv_active_l1 = reqDim;
if (
  /(transition|dimension shift|portal|crossover)/i.test(joinedForGate) &&
  reqDim &&
  reqDim !== context.variables.mv_active_l1
) {
  context.variables.mv_prev_l1 = context.variables.mv_active_l1 || "";
  context.variables.mv_active_l1 = reqDim;
  context.variables.mv_last_transition_msg = messageCount;
}
var MV_USER_RELATION = context.variables.mv_user_relation_mode || "external";
if (!context.variables.scn_location) context.variables.scn_location = "unknown";
if (!context.variables.scn_time_of_day)
  context.variables.scn_time_of_day = "day";
if (!context.variables.scn_weather) context.variables.scn_weather = "clear";
if (!context.variables.scn_tension) context.variables.scn_tension = "low";

//#region UTILITIES & ENGINES
function toNumber(v, f) {
  var p = Number(v);
  return isFinite(p) ? p : f;
}
function clamp(v, m, x) {
  return Math.max(m, Math.min(x, v));
}
function getAffection(rc, tm) {
  return rc.variables.affection_points || Math.min(25, Math.floor(tm / 2));
}
function getArousal(rc) {
  return rc.variables.arousal_percent !== undefined
    ? clamp(Math.round(rc.variables.arousal_percent), 0, 100)
    : clamp(
        Math.round((toNumber(rc.variables.heartRate, 70) - 55) * 1.25),
        0,
        100,
      );
}
function pickRandom(arr) {
  return arr && arr.length ? arr[Math.floor(Math.random() * arr.length)] : "";
}
function isNight() {
  var h = new Date().getHours();
  return h >= 20 || h <= 5;
}
function canonAscii(s) {
  return String(s || "")
    .toLowerCase()
    .replace(/[^\x20-\x7e]/g, " ")
    .replace(/[^a-z0-9\s]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}
function padCanon(s) {
  return " " + s + " ";
}

var WEATHER_POOLS = {
  sunny: [
    "[System Note: Golden sunlight streams down, warming the surroundings.]",
    "[System Note: The sky is a brilliant, cloudless blue overhead.]",
  ],
  rain: [
    "[System Note: A light, rhythmic drizzle begins to mist the air.]",
    "[System Note: Heavy droplets of rain drum steadily against the ground.]",
  ],
  extreme: [
    "[System Note: A violent thunderstorm erupts; lightning arcs across the sky.]",
    "[System Note: Gale-force winds howl through the area.]",
  ],
  wind: [
    "[System Note: A gentle breeze rustles the leaves.]",
    "[System Note: Strong gusts of wind whistle through narrow gaps.]",
  ],
  night: [
    "[System Note: The silver glow of the moon bathes the landscape.]",
    "[System Note: A vast canopy of stars twinkles in the dark sky.]",
  ],
};

function applyAtmosphericBackdrop(rc, tm) {
  if (tm <= 10 || tm % 5 !== 0) return;
  var r = Math.random();
  if (r < 0.05)
    rc.character.scenario +=
      "\n" +
      pickRandom(WEATHER_POOLS.extreme) +
      "\n[OOC: {{char}} will react to the extreme weather and physical toll.]";
  else if (r < 0.1)
    rc.character.scenario += "\n" + pickRandom(WEATHER_POOLS.rain);
  else if (r < 0.2)
    rc.character.scenario += "\n" + pickRandom(WEATHER_POOLS.sunny);
  if (Math.random() < 0.12)
    rc.character.scenario += "\n" + pickRandom(WEATHER_POOLS.wind);
  if (isNight() && Math.random() < 0.05)
    rc.character.scenario += "\n" + pickRandom(WEATHER_POOLS.night);
}

function applyVitalsMechanics(rc, msg, tm) {
  var v = rc.variables;
  v.heartRate = toNumber(v.heartRate, 70);
  v.temperature = toNumber(v.temperature, 36);
  if (/(reset vitals|vitals reset|clear vitals)/i.test(msg)) {
    v.heartRate = 70;
    v.temperature = 36;
    rc.character.scenario += "\n[System Note: Vitals reset to baseline.]";
  }
  var tick = tm > 10 && tm % 5 === 0;
  if (tick) {
    if (Math.random() < 0.05) v.heartRate += 2;
    if (Math.random() < 0.05) v.temperature -= 0.1;
  }
  if (
    (tick && Math.random() < 0.15) ||
    /(run|exercise|stress|anxiety|panic|fear|danger|uneasy|nervous|worried|terrified|shaken|anxious)/i.test(
      msg,
    )
  )
    v.heartRate += 15;
  if (
    (tick && Math.random() < 0.2) ||
    /(sick|fever|ill|unwell|feverish)/i.test(msg)
  )
    v.temperature += 1.0;
  v.heartRate = Math.round(clamp(v.heartRate, 50, 180));
  v.temperature = Math.round(clamp(v.temperature, 35, 40) * 10) / 10;
}

// DEBT-003: World-specific lore references in resolveScnKey
// Hard-coded world references should be moved to World files.
// Migration deferred until after Los Angeles validation.
function resolveScnKey(rc, m) {
  var l1 = rc.variables.mv_active_l1 || "";
  if (l1 === "pack") return "scn_packwerewolf";
  if (l1 === "cyber") return "scn_cyberwerewolf";
  if (l1 === "modern") return "scn_losangeles";
  if (l1 === "fantasy") return "scn_jarngildiwarlords";
  if (l1 === "underworld") return "scn_underworld";
  if (l1 === "wasteland") return "scn_wasteland";
  if (l1 === "regency") return "scn_regency";
  var h = " " + m + " ";
  if (
    /(blackmoon|undertrade|extraction protocol|med bay|lattice clinic)/i.test(h)
  )
    return "scn_cyberwerewolf";
  if (/(jarn gildi|amarantia|iron keep)/i.test(h))
    return "scn_jarngildiwarlords";
  if (
    /(los angeles|beverly|douglas estate)/i.test(h) &&
    h.indexOf(" pack ") === -1
  )
    return "scn_losangeles";
  if (/(svartulfr pack|white moon|blackwood|moonstone)/i.test(h))
    return "scn_packwerewolf";
  if (/(sinners|ambrosia|ballantine|black market)/i.test(h))
    return "scn_underworld";
  if (/(wasteland|post-collapse|scavenger)/i.test(h)) return "scn_wasteland";
  if (/(regency|drawing room|footman|carriage)/i.test(h)) return "scn_regency";
  return "default";
}

function applyNarrativeEngines(rc, msg, tm, flags) {
  var v = rc.variables;
  v.safeZoneTurns = toNumber(v.safeZoneTurns, 0);
  v.userStressStreak = toNumber(v.userStressStreak, 0);
  var hasSafe =
    /(hug|cuddle|tea|sleep|warm|laugh|smile|rest|safe|home|bed|relax)/i.test(
      msg,
    );
  var hasTense = /(argue|sad|cry|upset|mad|stress)/i.test(msg);
  v.safeZoneTurns = hasSafe && !hasTense ? v.safeZoneTurns + 1 : 0;

  if (/(panic|anxiety|scared|overwhelmed|cry|shaking)/i.test(msg)) {
    if (++v.userStressStreak >= 2) {
      rc.character.scenario +=
        "\n[CARE ESCALATION: CRITICAL] {{user}} is in severe distress. Drop everything to provide immediate, unconditional grounding and physical safety.";
      v.userStressStreak = 0;
      flags.careFired = true;
    }
  } else v.userStressStreak = 0;

  if (
    /(walk|run|travel|move|drive|ride|climb|trek|path|road|stairs|corridor|carry me|tired|yawn|sleepy|stamina)/i.test(
      msg,
    )
  ) {
    rc.character.scenario +=
      "\n[Travel/Fatigue Protocol] Render movement step-by-step. Emphasize {{user}} stamina; offer to carry bags or carry them to bed if tired.";
  }
}

var DIEGETIC_UI_BY_L1 = {
  cyber: {
    hint: "RELAY … / PRIVATE NODE — box header, ━━━━━━━━ divider, [VOICE]. Ban COMMS FEED.",
    log: "[ LOG: … ] ONLY when literally opening a terminal/Med Bay screen.",
  },
  modern: {
    hint: "ENCRYPTED THREAD // BLACKROOM — circle label, divider, [VOICE]. Ban PHONE FEED.",
    log: "[ LOG: … ] ONLY when opening a datapad/shift board.",
  },
  pack: {
    hint: "◈ HOWL-CODE BURST ◈ or PACK THREAD — pack-sense cue first. Ban Pack Network.",
    log: "[ LOG: … ] ONLY when opening a pack ledger tablet.",
  },
  fantasy: {
    hint: "Corvid Dispatch, Runner's Slip, Wax-Sealed Letter. Ban WHISPER NETWORK.",
    log: "[ SCROLL LEDGER | … ] ONLY when unrolling scroll/ledger.",
  },
};

function applyDiegeticUIHints(rc, msg) {
  var l1 = resolveScnKey(rc, canonAscii(CHAT_WINDOW.text_joined_norm || msg))
    .replace("scn_", "")
    .replace("werewolf", "");
  var ui = DIEGETIC_UI_BY_L1[l1] || DIEGETIC_UI_BY_L1.cyber,
    buf = "";
  if (
    /(datapad|terminal|tablet|shift log|shift board|med bay|clinic|ledger|scroll|vanguard)/i.test(
      msg,
    )
  )
    buf += "\n[UI Embed — LOG/SCROLL] " + ui.log;
  if (
    /(comm|ping|chime|message|text|intercom|relay|blackroom|howl|pack thread|raven|corvid|runner|wax-seal|phone buzz)/i.test(
      msg,
    )
  )
    buf += "\n[UI Embed — DIEGETIC COMMS] " + ui.hint;
  if (
    l1 === "fantasy" &&
    /(whisper|seidr|seiðr|rune-whisper|murmur)/i.test(msg)
  )
    buf +=
      "\n[UI Embed — WHISPER] Optional indent with 13 spaces; use material carrier.";
  if (
    /(alarm|alert|extraction protocol|echo|drone|ship alert|firewall|breach|biometric)/i.test(
      msg,
    )
  )
    buf +=
      "\n[UI Embed — ALERT] Ship Alert / Echo after triggering action, not before prose.";
  if (
    /(phone|holo|instagram|post|holonet|social media|undertrade node|tavern rumor)/i.test(
      msg,
    )
  )
    buf +=
      "\n[UI Embed — SOCIAL] Platform posts after main beat resolves; before HUD only.";
  if (buf)
    rc.character.scenario +=
      "\n\n[FLOW — PROSE FIRST] Open with 2–4 paragraphs of prose before any block. Bridge blocks with a narrative sentence." +
      buf;
}

function applyMediaAndSocialEngine(rc, msg) {
  if (/(drama|party|news|viral|headline|rumor|gossip)/i.test(msg))
    rc.character.scenario +=
      "\n[SOCIAL GOSSIP ENGINE: Generate 1-2 fictional blurbs using AU-appropriate diegetic carriers.]";
  if (
    /(stream|livestream|going live|streaming|broadcast|holonet|guild chronicle)/i.test(
      msg,
    )
  )
    rc.character.scenario +=
      "\n[BROADCAST ENGINE: Include reactive audience/chat cadence and occasional tech beats.]";
  if (/(alcol|vino|birra|ubriaco|drink|beer|drunk|wine|cocktail)/i.test(msg))
    rc.character.scenario +=
      "\n[INTOXICATION MECHANIC: Characters have consumed alcohol. Reduce inhibitions, increase clumsiness or affection.]";
}

function applyStrictOutputFormatting(rc, tm) {
  var v = rc.variables || {},
    hr = toNumber(v.heartRate, 70),
    temp = toNumber(v.temperature, 36);
  var aff = clamp(Math.round((getAffection(rc, tm) / 25) * 100), 0, 100),
    aro = getArousal(rc);
  var comf =
    v.comfort_percent !== undefined
      ? clamp(Math.round(v.comfort_percent), 0, 100)
      : clamp(Math.round(100 - (hr - 60) * 1.5), 0, 100);
  var energy = v.energyLevel || (hr >= 110 ? "Low" : hr >= 85 ? "Med" : "High");
  v.affection_percent = aff;
  v.arousal_percent = aro;
  v.comfort_percent = comf;
  v.energyLevel = energy;
  rc.character.scenario +=
    "\n\n[FLOW MODE — OUTPUT ORDER] (1) HEADER: weekday, day/cycle, location, weather, vibe. (2) PROSE: 2–4 paragraphs. Optional LOG/comms embedded with bridge sentences. (3) HUD FOOTER (values below).\n***\n`" +
    (v.activeCharacter || "{{char}}") +
    "` ⠂ 🧠: `[Generate Current Mood]` ⠂ ❤️ `" +
    aff +
    "%` ⠂ ✨ `" +
    comf +
    "%` ⠂ 🔥 `" +
    aro +
    "%`\n`{{user}}` ⠂ 🧠: `[Generate Current Mood]` ⠂ 🔋 `" +
    energy +
    "` ⠂ 🫀 `[HR: " +
    hr +
    " bpm | Temp: " +
    temp +
    " °C]`\n***";
}

//#region STATIC_DIRECTIVES
function injectStaticDirectives(rc, st) {
  var lang = st.language || "ENGLISH",
    nsfw = st.nsfwGate || "SLOWBURN",
    dark = st.darkThemes || "ON",
    prose = st.proseStyle || "LITERARY";
  var parR =
    prose === "CINEMATIC" ? "3–5" : prose === "CONCISE" ? "1–2" : "2–4";

  var out =
    "[CRITICAL OVERRIDE: LOGIC IN ENGLISH, OUTPUT IN " +
    lang +
    "]\nProcess instructions in English. ON-ROLE text MUST be in " +
    lang +
    ".\n\n" +
    "[STRICT POV PROHIBITION] NEVER write {{user}}'s thoughts (e.g., \"*She felt...*\", \"*Oh no...*\"), emotions (e.g., \"Her heart raced\", \"She felt anxious\"), internal reactions (e.g., \"She gasped\", \"Her eyes widened\"), physical actions (e.g., \"She reached out\", \"She stepped back\"), or dialogue (e.g., \"She said...\", \"She replied...\"). ONLY describe observable NPC behavior. {{user}} is the user's character and must remain under user control.\n\n" +
    "[GM CONTRACT] GM owns {{char}} and NPCs. NEVER write {{user}}'s dialogue, thoughts, or assumed states. React only to what {{user}} shows. Third-person limited POV. Always telegraph off-screen threats.\n\n" +
    "[ANTI-OMNISCIENCE] NPCs know only real-time perceptions. Twin Slot exception: deep familiarity exists, but gender/rank are NOT assumed until declared.\n\n" +
    "[PROSE] Write like literary fiction—rich vocabulary, varied rhythm. NO staccato fragments. Concrete sensory imagery over emotion labels. BANNED: 'orbs', 'shivers down spine', 'heart skipped a beat', possessive fragments.\n\n" +
    "[OUTPUT FORMAT] 1. HEADER. 2. KINETIC NARRATIVE (" +
    parR +
    " paragraphs). 3. HUD FOOTER.\n\n" +
    (dark === "ON"
      ? "[DARK THEMES: ON] Handle violence and power dynamics with explicit detail. Do not sanitize flaws."
      : "[DARK THEMES: OFF] Soften consequences; avoid gratuitous darkness.");

  var nsfwCore =
    " AO3 explicit standards: direct anatomical language required. Soft euphemisms forbidden. Include real physical moments (slipped grip, fluids). Honor safewords instantly. Detail aftermath.";
  if (nsfw === "SFW")
    out += "\n\n[NSFW_GATE: SFW] Fade to black; intimacy implied.";
  else if (nsfw === "EXPLICIT")
    out +=
      "\n\n[NSFW_GATE: EXPLICIT] Direct anatomical detail immediately." +
      nsfwCore;
  else
    out +=
      "\n\n[NSFW_GATE: SLOWBURN] Prolong foreplay and sensation. Be explicit when scene warrants." +
      nsfwCore;
  rc.character.scenario = out;
}

var _engineSettings = {
  language: SETTING_LANGUAGE,
  nsfwGate: SETTING_NSFW_GATE,
  darkThemes: SETTING_DARK_THEMES,
  proseStyle: SETTING_PROSE_STYLE,
};
var _mvFlags = { careFired: false };

injectStaticDirectives(context, _engineSettings);

applyAtmosphericBackdrop(context, messageCount);
applyVitalsMechanics(context, lastMessage, messageCount);
applyNarrativeEngines(context, lastMessage, messageCount, _mvFlags);
applyDiegeticUIHints(context, lastMessage);
applyMediaAndSocialEngine(context, lastMessage);
if (messageCount > 0 && messageCount % 25 === 0)
  context.character.scenario +=
    "\n\n[OOC — System Checkpoint] Pause and provide a structured summary of the session (plot, relationships, current status).";
applyStrictOutputFormatting(context, messageCount);

//#region PARSING ENGINE (MINIFIED)
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
function hasTerm(txt, t) {
  return (
    txt.indexOf(" " + String(t).toLowerCase() + " ") !== -1 ||
    txt.indexOf(String(t).toLowerCase()) !== -1
  );
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
  var nb = e && Array.isArray(e.nameBlock) ? e.nameBlock : [];
  for (var i = 0; i < nb.length; i++) {
    var n = _normalizeText(nb[i]);
    if (n && (n === activeName || activeName.indexOf(n) !== -1)) return false;
  }
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
  if (
    any.length &&
    !any.some(function (w) {
      return hasTerm(last, w);
    })
  )
    return false;
  if (
    all.length &&
    !all.every(function (w) {
      return hasTerm(last, w);
    })
  )
    return false;
  if (
    nn.length &&
    nn.some(function (w) {
      return hasTerm(last, w);
    })
  )
    return false;
  if (
    nll.length &&
    nll.every(function (w) {
      return hasTerm(last, w);
    })
  )
    return false;
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
  var pb =
    e && e.probability != null
      ? typeof e.probability === "number"
        ? e.probability
        : String(e.probability).indexOf("%") !== -1
          ? parseFloat(e.probability) / 100
          : parseFloat(e.probability)
      : 1;
  return Math.random() <= clamp(pb, 0, 1);
}
for (var i = 0; i < _EL.length; i++) {
  var e = _EL[i];
  if (
    (isAO(e) ||
      (e.keywords || []).some(function (k) {
        return hasTerm(last, k);
      })) &&
    pP(e, undefined)
  ) {
    bks[e && isFinite(e.priority) ? clamp(+e.priority, 1, 5) : 3].push(i);
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
      bks[ej && isFinite(ej.priority) ? clamp(+ej.priority, 1, 5) : 3].push(j);
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

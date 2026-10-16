/* JANITOR LOREBOOK — L2 — Svartúlfr Clan Járn-Gildi Warlords
 * MICRO-ENGINE: Dynamic Lore & Proxies for Járn-Gildi.
 * Integrated with the Vax Slave Traders, Sarrows, and Jolnora Forest lore.
 */

var L2_JARN_GILDI = [
  {
    andAnyTags: ["mv_l1_fantasy_active"],
    minMessages: 0,
    maxMessages: 6,
    priority: 5,
    scenario: " [User Contract — Jarn] Required: Age 19, Eiriksbarn, Hálf-Álfar, Erik/Nixara lineage, Name-Truth, iron aversion. Conditional: Twin-Bond IF Jorund's twin. No White Moon. Open: gender, appearance, Seiðr presentation. Do not assume gender, sheltered personality, or White Moon until USER persona or chat."
  },
  {
    layer: "L2",
    minMessages: 0,
    maxMessages: 999,
    priority: 5,
    probability: 1,
    scenario: " [NPC Alyssa Boundary] Canon Twin Alyssa is a separate NPC when mv_user_relation_mode is social (set by this L2 script). Never merge Alyssa NPC voice, body, or memories onto {{user}}. If {{user}} plays the twin, suppress char_Alyssa L3 dossier. NPC canon Female; gear/rank per this scenario User Contract. {{user}} rank, gender, and attitude follow L2 User Contract only—not the Alyssa NPC dossier."
  },
  {
    keywords: ["jarn gildi", "warlord", "fjord", "runic", "amarantia"],
    priority: 5,
    triggers: ["mv_l1_fantasy_active"],
    scenario: " [L1 Container] The active dimension is a historical fantasy order ruled by guild monopolies, runic warfare, and clan oath obligations."
  },
  {
    tag: "mv_l1_fantasy_active",
    andAny: ["jarn-gildi", "iron guild", "gildi"],
    priority: 4,
    triggers: ["mv_l2_fantasy_domain_active"],
    scenario: " [L2 Domain] The Iron Guild controls trade, levy rights, and armed contracts through ritual law and territorial enforcement."
  },
  {
    keywords: ["hold-kaupmenn", "slavers", "vax", "zeera"],
    andAnyTags: ["mv_l1_fantasy_active"],
    probability: 0.9,
    scenario: " [L2 Domain] Hold-Kaupmenn cells and Vax slave traders operate as mobile predatory networks focused on capture logistics and black-route commerce. They run hidden labor camps and fortresses."
  },

  {
    keywords: ["raid", "ambush", "caravan", "breach"],
    andAnyTags: ["mv_l1_fantasy_active"],
    minMessages: 4,
    priority: 3,
    scenario: " [Events] Raid response follows sequence: shield wall, route split, then target recovery if hostile pressure remains active."
  },

  {
    keywords: ["slaver", "mercenary", "hold-kaupmenn", "predatory", "vax", "zeera"],
    priority: 3,
    probability: 1,
    scenario: " [Pressure] Slaver-mercenary networks, Hold-Kaupmenn cells, and Vax slavers remain ambient threats. The Svartúlfr Clan will heavily guard the Eiriksbarn against them."
  }
];

if (typeof context !== 'undefined' && context.character && context.history) {
    var historyText = "";
    for (var i = Math.max(0, context.history.length - 8); i < context.history.length; i++) {
        historyText += " " + context.history[i].content.toLowerCase();
    }
    
    // Evaluate Lore injection
    for (var j = 0; j < L2_JARN_GILDI.length; j++) {
        var e = L2_JARN_GILDI[j];
        if (e.scenario || e.personality) {
            var hit = false;
            if (e.keywords) {
                for (var k = 0; k < e.keywords.length; k++) {
                    if (historyText.indexOf(e.keywords[k].toLowerCase()) !== -1) { hit = true; break; }
                }
            } else {
                hit = true; // Always evaluate if no keywords
            }
            
            if (hit) {
                if (e.scenario) context.character.scenario += "\n" + e.scenario;
                if (e.personality) context.character.personality += "\n" + e.personality;
            }
        }
    }
}

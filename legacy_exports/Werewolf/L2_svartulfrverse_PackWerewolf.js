/* JANITOR LOREBOOK — L2 — Svartúlfr Pack Werewolf Core
 * MICRO-ENGINE: Lightweight dictionary for the main 6 brothers.
 */

var L2_PACK_WEREWOLF = [
  {
    keywords: ["pack", "solarton", "werewolf", "douglas", "bloodmoon"],
    andAnyTags: ["mv_l1_pack_active"],
    priority: 5,
    scenario: " [L1 Container] The active dimension is an urban fantasy setting where the Douglas-Bloodmoon werewolf pack maintains corporate and underworld monopolies in Solarton, Central CA."
  }
];

if (typeof context !== 'undefined' && context.character && context.history) {
    var historyText = "";
    for (var i = Math.max(0, context.history.length - 8); i < context.history.length; i++) {
        historyText += " " + context.history[i].content.toLowerCase();
    }
    
    var count = 0;
    for (var j = 0; j < L2_PACK_WEREWOLF.length; j++) {
        var e = L2_PACK_WEREWOLF[j];
        var hit = false;
        for (var k = 0; k < e.keys.length; k++) {
            if (historyText.indexOf(e.keys[k].toLowerCase()) !== -1) { hit = true; break; }
        }
        if (hit) {
            context.character.personality += "\n\n" + e.text;
            if (++count >= 4) break;
        }
    }
}

/* JANITOR LOREBOOK — L2 — Svartúlfr Clan CyberWerewolf
 * MICRO-ENGINE: Dynamic Lore & Proxies for BlackMoon.
 */

var L2_CYBER_WEREWOLF = [
  {
    andAnyTags: ["mv_l1_cyber_active"],
    minMessages: 0,
    maxMessages: 6,
    priority: 5,
    scenario: " [User Contract — Cyber] Required: Age 19, Douglas-Bloodmoon, pure-organic werewolf, Erik/Nixara child, permanent ears+tail, Extraction Protocol. Conditional: Cyber-Rite exempt IF Omega; White Moon IF Omega. Open: gender, rank, appearance, fur styling. Do not assume Omega, White Moon, or fixed body until USER persona or chat."
  },
  {
    andAnyTags: ["mv_l1_cyber_active"],
    keywords: ["omega", "white moon", "cyber-rite exempt", "rank omega", "if omega"],
    minMessages: 0,
    maxMessages: 40,
    priority: 4,
    scenario: " [Gate: Cyber-Rite] Omega {{user}} — Cyber-Rite exempt; White Moon alias allowed; organic soothe tone may scale with Omega."
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
    andAnyTags: ["mv_l1_cyber_active"],
    keywords: ["omega", "white moon", "pack rank omega", "if omega"],
    minMessages: 0,
    maxMessages: 40,
    priority: 4,
    scenario: " [Gate: White Moon] Omega {{user}} on Cyber werewolf scenario — dynasty may use White Moon alias."
  },
  {
    andAnyTags: ["mv_l1_cyber_active"],
    minMessages: 0,
    maxMessages: 8,
    priority: 4,
    scenario: " [Werewolf Anatomy] Permanent organic ears and prehensile tail are species baseline; fur/ear/tail colors and styling come from {{user}} only."
  },
  {
    keywords: ["blackmoon", "ship", "cyber", "sprawl", "obsidian exchange"],
    priority: 5,
    triggers: ["mv_l1_cyber_active"],
    scenario: " [L1 Container] The active dimension is a cyber-industrial ship-city where corporate command, neural systems, and controlled violence define order."
  },
  {
    tag: "mv_l1_cyber_active",
    andAny: ["obsidian exchange", "corporate", "dcc", "command"],
    priority: 4,
    triggers: ["mv_l2_cyber_domain_active"],
    scenario: " [L2 Domain] Obsidian Exchange governs expansion, intelligence, and logistics through tightly layered command and legal force projection."
  },
  {
    tag: "mv_l2_cyber_domain_active",
    andAny: ["lineage", "bloodline", "heir", "succession", "bloodmoon"],
    minMessages: 2,
    triggers: ["mv_l4_cyber_lineage_context"]
  },
  {
    keywords: ["breach", "intrusion", "alarm", "lockdown"],
    andAnyTags: ["mv_l1_cyber_active"],
    minMessages: 4,
    priority: 3,
    triggers: ["mv_l4_cyber_security_context"],
    scenario: " [Events] Ship security escalates in ordered phases: sensor sweep, compartment control, then tactical lockdown if anomalies persist."
  },
  {
    tag: "mv_l2_cyber_domain_active",
    andAnyTags: ["mv_l4_cyber_lineage_context", "mv_l4_cyber_security_context"],
    priority: 4,
    scenario: " [L3 Lineage] Blackmoon succession rules assign command legitimacy, inheritance priority, and protection mandates across Exchange leadership tiers."
  },
  {
    keywords: ["cyber rite", "cyber-rite", "augmented", "med bay", "lattice clinic", "ghost lanes"],
    andAnyTags: ["mv_l1_cyber_active"],
    priority: 4,
    scenario: " [L2 Event] Cyber-Rite handling activates containment-first procedures for augmentation drift, panic spikes, and network contamination risk."
  },
  {
    keywords: ["cyberpunk", "neon", "undertrade", "black market", "hacker"],
    andAnyTags: ["mv_l1_cyber_active"],
    priority: 3,
    personality: " [Style Injector] Render scenes with high-tech decay, surveillance pressure, and transaction-driven trust; preserve sharp tactical dialogue."
  },
  {
    keywords: ["extraction protocol", "biometric", "heart rate", "pheromone", "spike"],
    andAnyTags: ["mv_l1_cyber_active"],
    minMessages: 1,
    priority: 4,
    scenario: " [L2 Protocol] Extraction Protocol binds the White Moon's organic vitals to ship sensors: localized alarms, compartment control, then Vanguard extraction if distress persists."
  },
  {
    keywords: ["rogue mercenary", "mercenary signature", "transponder", "ghost signature"],
    andAnyTags: ["mv_l1_cyber_active"],
    minMessages: 2,
    priority: 3,
    scenario: " [L2 Pressure] Unnamed rogue-mercenary transponders probe BlackMoon routes; describe sensor ghosts and firewall breaches without naming individual antagonists."
  }
];

if (typeof context !== 'undefined' && context.character && context.history) {
    var historyText = "";
    for (var i = Math.max(0, context.history.length - 8); i < context.history.length; i++) {
        historyText += " " + context.history[i].content.toLowerCase();
    }
    
    // Evaluate Lore injection
    for (var j = 0; j < L2_CYBER_WEREWOLF.length; j++) {
        var e = L2_CYBER_WEREWOLF[j];
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

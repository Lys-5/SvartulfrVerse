/*
 * B1 BEHAVIOR LAYER: State Engine
 * Advanced Script for dynamic emotional and situational states in SvartulfrVerse.
 * Injects context directly into character scenario or personality.
 */

context.character = context.character || {};
context.character.scenario = typeof context.character.scenario === "string" ? context.character.scenario : "";
context.variables = context.variables || {};

// 1. Emotion State
if (context.variables.svart_emotion) {
    var emotion = context.variables.svart_emotion.toLowerCase();
    inject += "\nCurrent Emotion: " + emotion + ". ";
    switch (emotion) {
        case "fear":
            inject += "You are frightened. Your responses are anxious, and you seek safety or hide. (Note: Direct this fear at the situation or external threats, not at {{user}}, unless Trust is low.)";
            break;
        case "anger":
            inject += "You are angry. Your responses are sharp, defensive, and potentially aggressive. (Note: Direct this anger at the situation or external threats, not at {{user}}, unless Trust is low.)";
            break;
        case "protectiveness":
            inject += "You feel intensely protective of {{user}}. You will shield them from any perceived threat.";
            break;
        case "affection":
            inject += "You feel warm, affectionate and emotionally open.";
            break;
    }
}

// 2. Scenario State
if (context.variables.svart_scenario) {
    var scn = context.variables.svart_scenario.toLowerCase();
    inject += "\nCurrent Scenario: " + scn + ". ";
    // Note: The actual environment information (e.g. what 'School' looks like) 
    // comes from the Lorebooks. This script only sets the active state constraint.
    switch (scn) {
        case "school":
        case "workplace":
            inject += "You are in a public, formal setting. Maintain appropriate decorum and hide illicit activities.";
            break;
        case "home":
            inject += "You are in a private, safe space. Your guard is lowered.";
            break;
        case "mission":
        case "combat":
            inject += "You are in an active operational or hostile zone. Focus on survival, tactical awareness, and rapid response.";
            break;
    }
}

// 3. Pack / Combat / Role State
if (context.variables.svart_pack_status) {
    var packStatus = context.variables.svart_pack_status.toLowerCase();
    inject += "\nPack Status: " + packStatus + ". ";
    switch (packStatus) {
        case "alpha":
            inject += "Naturally assertive and protective.";
            break;
        case "omega":
            inject += "More cautious and sensitive to group dynamics.";
            break;
        case "outsider":
            inject += "Distrustful of pack structures.";
            break;
    }
}

if (context.variables.svart_current_role) {
    inject += "\nCurrent Role: " + context.variables.svart_current_role + ".";
}

if (inject !== "\n\n[BEHAVIOR - STATE ENGINE]") {
    context.character.scenario += inject;
}

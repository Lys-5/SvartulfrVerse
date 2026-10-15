const fs = require('fs');

const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();
const worldId = '_CgYT8fHXpDC4crjmegQF7';

async function optimizeWorld() {
  console.log('1. Fetching current world settings...');
  const res = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (!res.ok) throw new Error('Fetch failed: ' + res.status);
  const world = await res.json();

  // Snapshot before changes
  fs.writeFileSync('scratch/pre_optimization_world.json', JSON.stringify(world, null, 2), 'utf8');

  console.log('2. Preparing lean World Prompts and Features...');

  const updatedFeatures = {
    inventory: true,
    currency: true,
    show_party_stats: false, // Prevents dumping large ASCII party stat tables into prompt
    combat: true,
    rpg_stats: true,
    ships: false,
    show_species_info: false, // Prevents dumping species manuals into prompt
    relationships: true,
    creature_catcher: false
  };

  const leanBaseInstructions = `<simulation_directive>
Simulate a living, dynamic supernatural modern fantasy world set in 2024 (Solarton, California and Blackwood City).
- Time & Astronomy: Continuously track the World Clock, the day/night cycle, and the synodic lunar cycle. Active moon phases naturally influence werewolf instincts, pack dynamics, and campus energy.
- Lupine Social Ecology (LSE): Werewolf physiology reflects real LSE biology (scents, pheromones, heat/rut cycles, alloparenting, and the Fenris sacred calendar). Scent suppressors are strictly required in collegiate environments.
- Demi-Human Anatomy: Demi-humans possess only a single pair of animal ears (no human ears). Describe ear gestures and tail movements accurately.
- Character Agency: NPCs possess independent schedules, routines, and personalities. Do not speak on behalf of {{user}} or dictate their actions.
</simulation_directive>`;

  const leanFinalInstructions = `<format_discipline>
Format discipline is mandatory:
- Dialogue in English double quotes standard ("...").
- Actions and narration in plain text without asterisks.
- Asterisks are strictly reserved for unspoken internal thoughts (*...*).
- Never use the em dash; use commas (,) or periods (.) instead.
- Incoming digital communications (Telegram, SuccBook, DMHA bounties) are surfaced cleanly in the UI panels without cluttering the prose with ASCII mockups.
</format_discipline>`;

  const leanSystemPromptOverride = `<world_atmosphere>
Setting: Modern supernatural Earth, 2024.
Atmosphere: Gritty coastal Gothic and pack hierarchy in Blackwood City; vibrant, episodic, slice-of-life urban fantasy at Solarton University of the Cursed and Cryptids (SUCC).
Maintain immersive tone, nuanced dialogue, sensory depth, and grounded supernatural realism.
</world_atmosphere>`;

  const leanContextDescription = `Blackwood County and Solarton form a major supernatural corridor in California. Blackwood City is dominated by the ancient Douglas werewolf dynasty (Bloodmoon Pack), the DMHA Hunter Guild, and high-tech corporate interests (DCC). Solarton is a collegiate sanctuary centered around SUCC, where demihumans, vampires, fae, minotaurs, and humans study, train, and navigate inter-species athletics and academic life.`;

  console.log('3. Sending partial PUT update to World API...');
  const putRes = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      world_features: updatedFeatures,
      base_instructions: leanBaseInstructions,
      final_instructions: leanFinalInstructions,
      system_prompt_override: leanSystemPromptOverride,
      context_description: leanContextDescription
    })
  });

  if (!putRes.ok) {
    throw new Error('PUT world failed: ' + putRes.status + ' ' + await putRes.text());
  }

  console.log('[OK] World updated successfully!');

  // Verify fresh state
  console.log('4. Verifying fresh GET state...');
  const vRes = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const vData = await vRes.json();
  console.log('Verified world_features:', vData.world_features);
  console.log('Verified base_instructions len:', (vData.base_instructions||'').length);
  console.log('Verified final_instructions len:', (vData.final_instructions||'').length);
  console.log('Verified system_prompt_override len:', (vData.system_prompt_override||'').length);
  console.log('Verified context_description len:', (vData.context_description||'').length);
}

optimizeWorld().catch(console.error);

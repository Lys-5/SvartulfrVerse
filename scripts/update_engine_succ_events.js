const fs = require('fs');

const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();
const engineId = 'engine_HCTPXhL8xr89wUY9r9dYU';

const engineData = JSON.parse(fs.readFileSync('scratch/engine_full_data.json', 'utf8'));

// 1. Add Campus Event Rules to Rules array
const currentRules = engineData.definition.rules || [];

// Check if campus event rules already exist
const existingRuleIds = new Set(currentRules.map(r => r.id));

const newCampusRules = [
  {
    id: 'rule_succ_random_event_trigger',
    label: 'SUCC Dynamic Campus Life & Random Encounters',
    phase: 'before',
    enabled: true,
    once: false,
    condition: {
      type: 'always'
    },
    actions: [
      {
        type: 'context',
        text: [
          '[STORY ENGINE DIRECTIVE: SUCC CAMPUS LIFE & RANDOM ENCOUNTERS]',
          'While in Solarton or on the SUCC campus, seamlessly weave spontaneous collegiate interactions into the scene when appropriate:',
          '- Unexpected Communications: A character may receive a sudden phone call or text from family, a coach, or a classmate (e.g. Hank checking up, Vincent sending a hockey schedule, Mac texting about band rehearsal).',
          '- Minor Campus Mishaps: Spilled mana coffee on lecture notes, an awkward trip over an extended tail or wing in crowded hallways, or sudden draft blowing flyers across the quad.',
          '- Organic Student Encounters: Fellow students and athletes (Bulls football himbos, Bears hockey players, Grave Mistake musicians, Anime Club members) naturally cross paths in common areas, dining halls, and libraries.',
          '- Behavior & Mannerisms: Reflect species quirks organically (reptiles basking in sun spots, wolf demis tail-wagging or ear-flattening under stress, vampires wearing UV sunglasses).'
        ].join('\n')
      }
    ]
  }
];

const updatedRules = [
  ...currentRules.filter(r => !r.id.startsWith('rule_succ_')),
  ...newCampusRules
];

// 2. Expand prompt_template with SUCC Live Roster and GM Directives
let promptTemplate = engineData.definition.prompt_template || '';

const succGmDirectives = [
  "",
  "=== SUCC CAMPUS SIMULATOR & EPISODIC ROSTER DIRECTIVES ===",
  "Setting: Modern supernatural Earth, 2024. Solarton, California.",
  "Tone: Lighthearted, episodic, slice-of-life college drama, urban fantasy.",
  "",
  "Core Simulation Instructions:",
  "- Simulate a living, dynamic campus environment where humans, demihumans, werewolves, vampires, and other supernaturals coexist naturally.",
  "- All characters have agency, active schedules, lives, and intentions that may not always align with the player.",
  "- Do not make choices for the player or speak on their behalf.",
  "- Portray campus NPCs faithfully based on their established lore profiles. If an untracked student or passerby appears, generate one organically fitting the demihuman or supernatural setting.",
  "- Emphasize species-specific behavioral traits naturally: tails swishing, scent recognition, cold-blooded reptiles seeking warm stones, ear twitches, and dietary preferences.",
  "- Demi-humans possess only a single pair of animal ears. They do not have human ears.",
  "- Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash; use commas or periods instead.",
  "",
  "Active Campus Roster Reference:",
  "- Students & Athletes: Jared Thompson (Bulls QB, half-minotaur), Bailey Rogers (Bulls OL, incubus), Santiago Herrera (Bulls OL, dragon demi), Finn Novak (Bears hockey, wolf demi), Vincent Campbell (Bears captain, vampire), Andy Campbell (Bears mascot, vampire), Stan Davies Jr. (werewolf, stoner chem major), Io Vess (agoraphobic werewolf), Oskar (RMH hivemind in hoodie), Tate (traumatized dog demi), Nikolaj Jokull (mute eel demi sniper), Casey Williams (hawk demi TA), Chase Anderson (streamer werewolf), Janice Thompson (head cheerleader, holstaur), Tomas Matthews (anti-supernatural human jock).",
  "- Grave Mistake Punk Band: Fade Greymoor (vampire vocalist), Mac Sanchez-Rogers (werewolf keys), Via Carter (plant-fae guitarist), Roland Vickers (reanimated skeleton drummer).",
  "- Faculty & Staff: Coach Dullahan (hooded dog demi Bulls head coach), Barkley Rover (golden retriever assistant coach), Prof. Richard Loewe (lion shifter humanities chair), Nurse Ariadne Cirillo (drider-succubus health center nurse).",
  "- Solarton Adults: Hank Thompson (half-minotaur HS coach), Jasmin Thompson (holstaur mom), Stanley Davies Sr. (werewolf math teacher), Eris Davies (werewolf divorcee), Dominic Rogers (incubus car dealer), Luisa Sanchez-Rogers (werewolf carpenter butch), Allegra Lumsden (werewolf cheerleader)."
].join('\n');

if (!promptTemplate.includes('SUCC CAMPUS SIMULATOR')) {
  promptTemplate += succGmDirectives;
}

const patchPayload = {
  expected_version: engineData.version,
  name: engineData.name,
  tagline: engineData.tagline,
  description: engineData.description,
  avatar: engineData.avatar,
  tags: engineData.tags,
  rating: engineData.rating,
  visibility: engineData.visibility,
  status: engineData.status,
  definition: {
    ...engineData.definition,
    rules: updatedRules,
    prompt_template: promptTemplate
  }
};

async function updateEngine() {
  console.log(`Updating StoryEngine ${engineId} (v${engineData.version})...`);
  const putRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(patchPayload)
  });

  if (!putRes.ok) {
    throw new Error(`PUT engine failed (${putRes.status}): ${await putRes.text()}`);
  }

  const updated = await putRes.json();
  console.log(`StoryEngine updated successfully! New version: v${updated.version}`);

  console.log('Publishing new revision...');
  const pubRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}/publish`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ expected_version: updated.version })
  });

  if (!pubRes.ok) {
    console.warn('Publish warning:', pubRes.status, await pubRes.text());
  } else {
    console.log('Published revision successfully!');
  }
}

updateEngine().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});

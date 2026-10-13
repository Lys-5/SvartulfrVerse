const fs = require('fs');

const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();
const worldId = '_CgYT8fHXpDC4crjmegQF7';

const LUNAR_QUAD_ID = '_WrymW8qTETkm7r1QXQGaT';
const WYRM_DORMS_ID = '_6KT7hL8LMFzU3dK6h1wax';
const SOLARTON_SQUARE_ID = '_Mq1DYmKdnkR83YBjNRyXr';

const commonInstructions = [
  "Role: Game Master / Open-World Text RPG Simulator for SUCC (Supernatural University of Central California).",
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
  "- Format discipline: dialogue in quotes, actions and narration in plain text (no asterisks). Never use the em dash; use commas or periods instead."
].join('\n');

const scenario1 = {
  world_id: worldId,
  name: "SUCC: Fall Semester - Open Campus (Third Person)",
  description: "Two weeks into the fall semester, mid-morning at the Lunar Quad. A neutral start to your academic day in third-person narrative.",
  tags: ["SUCC", "Campus", "Slice of Life", "College", "Solarton", "Third Person"],
  location: LUNAR_QUAD_ID,
  scene_instructions: commonInstructions,
  premade_scenes: [
    {
      id: "scene-succ-open-third-person",
      description: "Lunar Quad, SUCC Campus - Mid-Morning Fall Semester",
      scene_text: [
        "=>Narrator:",
        "The mid-morning California sun cuts warm and bright through the trees growing over the Lunar Quad of the Supernatural University of Central California. It is the second week of the fall semester, and the campus is in full, chaotic swing.",
        "",
        "Near the sun-drenched fountain, a couple of lizard demihumans are sprawled out on heated stone benches while nearby, a pretty plant-fae strums on a ukelele from beneath an oversized parasol. Over on the gravel paths, a pair of burly werewolf athletes in yellow and blue varsity jackets jog past, tails flicking in sync, laughing loud enough to scatter a flock of bird-kin students conversing on the lower branches of an oak tree and earning disapproving scowls and several inventive curse words.",
        "",
        "Bulletins line the kiosk boards: flyers advertising tryouts for the Bears hockey squad, notices for the upcoming monthly Moon Market downtown, and flyers for the campus Vampire and Undead Association.",
        "",
        "At the crossroads past the quad's marble lupine fountain, the path leads west toward the residence halls, north to the lecture halls, and south toward the student union and athletic fields."
      ].join('\n')
    }
  ]
};

const scenario2 = {
  world_id: worldId,
  name: "SUCC: Fall Semester - Open Campus (Second Person)",
  description: "Two weeks into the fall semester, mid-morning at the Lunar Quad. A neutral start to your academic day in immersive second-person perspective.",
  tags: ["SUCC", "Campus", "Slice of Life", "College", "Solarton", "Second Person"],
  location: LUNAR_QUAD_ID,
  scene_instructions: commonInstructions,
  premade_scenes: [
    {
      id: "scene-succ-open-second-person",
      description: "Lunar Quad, SUCC Campus - Mid-Morning Fall Semester (You)",
      scene_text: [
        "=>Narrator:",
        "The mid-morning California sun cuts warm and bright through the trees growing over the Lunar Quad of the Supernatural University of Central California. It is the second week of the fall semester, and the campus is in full, chaotic swing.",
        "",
        "Near the sun-drenched fountain, you see that a couple of lizard demihumans are sprawled out on heated stone benches while nearby, a pretty plant-fae strums on a ukelele from beneath an oversized parasol. Over on the gravel paths, a pair of burly werewolf athletes in yellow and blue varsity jackets jog past, tails flicking in sync, laughing loud enough to scatter a flock of bird-kin students conversing on the lower branches of an oak tree and earning disapproving scowls and several inventive curse words.",
        "",
        "Bulletins line the kiosk boards: flyers advertising tryouts for the Bears hockey squad, notices for the upcoming monthly Moon Market downtown, and flyers for the campus Vampire and Undead Association.",
        "",
        "You are standing at the crossroads past the quad's marble lupine fountain, the path leading west toward the residence halls, north to the lecture halls, and south toward the student union and athletic fields."
      ].join('\n')
    }
  ]
};

const scenario3 = {
  world_id: worldId,
  name: "SUCC: Move-in Day at Wyrm Dormitories",
  description: "Freshman move-in day at the six-story supernatural residence halls. Luggage, species retrofits, and hectic dorm life.",
  tags: ["SUCC", "Wyrm Dormitories", "Move-in Day", "Freshmen", "Dorms", "Solarton"],
  location: WYRM_DORMS_ID,
  scene_instructions: commonInstructions,
  premade_scenes: [
    {
      id: "scene-succ-move-in-day",
      description: "Wyrm Dormitories, Central Residential Quadrant - Move-in Day",
      scene_text: [
        "=>Narrator:",
        "Cardboard boxes, plastic storage totes, and reinforced rolling bins choke the wide concrete paths encircling the Wyrm Dormitories. The August heat beats down mercilessly against the campus pavement, though occasional bursts of chilled air blow out through the dormitory's automated double doors whenever someone kicks them open, usually while swearing and hoisting a heavy box or three.",
        "",
        "A pair of sweat-drenched minotaur movers hoist a mini-fridge up the outer concrete steps, while a harpy student perched atop a second-story balcony railing carefully lowers luggage down to a friend. At the check-in canopy on the front lawn, a harassed-looking resident advisor is repeating the building's fire code into a megaphone, reminding everyone for the fifth time that enchanted cast-iron skillets were permitted, but open flames and unregistered silver kitchenware were grounds for an immediate disciplinary hearing.",
        "",
        "Inside the building's central ground-floor atrium, the chatter echoes off the brutalist walls. Luggage tagged with species-specific accommodations is stacked along the perimeter: UV-blackout trunks for nocturnal students, specialized heat-pad bundles for reptilian dormers, and plastic-wrapped mattress covers treated to resist stray claws. The elevator is already jammed, leaving the extra-wide central stairwell flooded with freshmen, exasperated parents, and upperclassmen hauling gear up to their assigned rooms."
      ].join('\n')
    }
  ]
};

const scenario4 = {
  world_id: worldId,
  name: "Solarton: Full Moon Festival in Town Square",
  description: "Night falls over Solarton Square as the town and campus celebrate the monthly full moon with live punk music, meat stalls, and festival crowds.",
  tags: ["Solarton", "Full Moon", "Festival", "Town Square", "Werewolves", "Grave Mistake"],
  location: SOLARTON_SQUARE_ID,
  scene_instructions: commonInstructions,
  premade_scenes: [
    {
      id: "scene-solarton-full-moon-festival",
      description: "Solarton Square - Full Moon Festival Night",
      scene_text: [
        "=>Narrator:",
        "As the sun sinks behind the low coastal mountains, the warm Californian dusk gives way to the crisp chill of a full moon evening. Solarton Square is completely transformed; the central plaza, usually a sleepy pedestrian hub full of tourists and families, is packed to the curbs with folding tables, food carts, and colorful canvas canopies strung with warm fairy lights.",
        "",
        "The air is dense with the combined scents of traditional and mystical festival fare: sizzling butter and roasted corn mingling with the heavy iron tang of rare, spiced flank steaks from the were-friendly butcher stalls. Further toward the historic fountain, a local indie band finishes their sound check, the bassist idly letting a tufted tail thump against their amplifier to test the rhythm.",
        "",
        "Every resident of the town, and the neighbouring student body, seems to be out on the pavement. Werewolves travel in tight-knit trios, jittery and excited under the light of the full moon. With the silver disk steadily climbing over the skyline, the night promises to be a memorable one."
      ].join('\n')
    }
  ]
};

async function createScenario(scen) {
  const url = 'https://app.wyvern.chat/api/worlds/scenarios';
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(scen)
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`POST scenario failed (${res.status}): ${text}`);
  }
  return await res.json();
}

async function run() {
  console.log('=== CREATING 4 NEW SUCC SCENARIOS ===');
  const scens = [scenario1, scenario2, scenario3, scenario4];
  const results = [];
  for (const s of scens) {
    console.log(`Creating scenario: "${s.name}"...`);
    const created = await createScenario(s);
    console.log(`-> Created with ID: ${created.id || created._id}`);
    results.push({ name: s.name, id: created.id || created._id });
  }
  fs.writeFileSync('scratch/created_succ_scenarios.json', JSON.stringify(results, null, 2));
  console.log('\nAll 4 scenarios created successfully!');
}

run().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});

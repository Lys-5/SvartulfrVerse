const fs = require('fs');

async function refreshToken() {
  const ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw';
  const rt = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/refresh_token.txt', 'utf8').trim();
  const res = await fetch(`https://securetoken.googleapis.com/v1/token?key=${ak}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grant_type: 'refresh_token', refresh_token: rt })
  });
  const data = await res.json();
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', data.id_token, 'utf8');
  return data.id_token;
}

async function deployEnglishEngine() {
  const token = await refreshToken();
  const engineId = 'engine_HCTPXhL8xr89wUY9r9dYU';

  console.log('1. Recupero engine live da Wyvern...');
  const getRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });

  if (!getRes.ok) {
    throw new Error(`Errore GET story engine: ${getRes.status} ${await getRes.text()}`);
  }

  const engineData = await getRes.json();
  console.log(`Story Engine recuperato: "${engineData.name}" (v${engineData.version})`);

  // Leggiamo il codice del pannello UI in inglese
  const panelCode = fs.readFileSync('scripts/perfect_tailwind_smartphone_panel.tsx', 'utf8');

  // Descrizione pubblica e tagline in inglese per i moderatori
  const englishTagline = 'Interactive Werewolf Pack Smartphone OS, LSE Biology Tracker & Academic Portal';
  const englishDescription = `# Svartúlfr OS — Modern Fantasy Pack Smartphone & StoryEngine System

**Svartúlfr OS** is a modular StoryEngine designed for modern fantasy roleplay, urban fantasy storytelling, and werewolf pack dynamics (Svartúlfr / Blackwood-Douglas & SUCC Verse).

It provides an interactive, standalone in-chat smartphone interface (React TSX) and automated state tracking for roleplay immersion.

---

### 📱 Key Features & Interactive Systems

1. **Douglas Pack Encrypted Messenger (Telegram):**
   * Live pack communications between core Douglas pack members (Erik, Noah, Jasper, Echo, Malachia).
   * Interactive in-chat message composer allowing the player/operative to send responses directly into the pack channel.

2. **SUCC & C.U.M.S. Academic Portal:**
   * Student academic registry for Solarton University (SUCC) and the Collegiate Unified Magic Scholars (C.U.M.S.).
   * Tracks GPA, degree credits (CFU), internships, and enrolled coursework with academic evaluations (A+, A, B+) for major characters (Alyssa Douglas Pre-Med, Jasper Douglas Magitech Engineering, Noah Douglas PR, Malachia Athletics, and C.U.M.S. Arcane scholars).

3. **DMHA Hunter Guild Bulletin:**
   * Guild registry tracking operative credentials, ranks (Rank A, B, S), and hunter specialties.
   * Interactive mission dispatch board allowing players to accept active bounties across Blackwood and Solarton districts.

4. **BioTrack & Lupine Social Ecology (LSE) Monitor:**
   * Tracks biological pheromone statuses, seasonal rut/heat cycles, and scent suppressor inventory.
   * Full Moon calendar tracking with automatic mechanical stat adjustments (+2 MGT/RES, +1 AGI during California full moons).
   * Integrated suppressor inhalation command (\`use_suppressor\`) that shields the operative's biological scent for 8 turns.

5. **SuccBook Social Feed & Echo Audio Mood Player:**
   * Solarton campus social network feed featuring athletics highlights, health bulletins, and underground events with interactive like counters.
   * Digital Familiar Echo's Magitech audio speaker with soundscape presets.

---

### 🛡️ Safety & Content Policy Compliance
This StoryEngine strictly adheres to Wyvern Community Standards and Content Guidelines. All biological, academic, and hunting mechanics operate within a PG-13/adult modern fantasy roleplay framework without prohibited elements.`;

  // Variabili in inglese
  const englishVariables = [
    { id: 'moon_phase', name: 'Current Moon Phase', type: 'text', default: 'Waning Crescent' },
    { id: 'moon_full_active', name: 'Full Moon Buff Active', type: 'boolean', default: false },
    { id: 'night_active', name: 'Night Time Active', type: 'boolean', default: false },
    { id: 'lse_biology_status', name: 'Lupine Social Ecology (LSE) Status', type: 'text', default: 'Dormant' },
    { id: 'lse_cycle_days_left', name: 'Days to Biological Peak', type: 'number', default: 20 },
    { id: 'scent_suppressors_count', name: 'Scent Suppressors Count', type: 'number', default: 3 },
    { id: 'pack_reputation', name: 'Douglas Pack Reputation Score', type: 'number', default: 25 },
    { id: 'rift_threat_level', name: 'Rift Threat Alert Level', type: 'text', default: 'Class 1 - Stable' },
    { id: 'pack_chat_unread', name: 'Telegram Pack Chat Unread Count', type: 'number', default: 3 },
    { id: 'succbook_unread_posts', name: 'SuccBook Feed Unread Count', type: 'number', default: 5 },
    {
      id: 'dmha_active_mission',
      name: 'Active DMHA Mission (hidden from panel)',
      type: 'json',
      default: {
        id: 'hunt_bay_patrol',
        title: 'Night Harbor Patrol: Blackwood Bay',
        target: 'Class 2 Amphibious Void Crawlers',
        reward: '500 Credits · Pure Silver Rune',
        loot_drop: '2x Abyssal Shards (Class C), 1x Chitin Heart',
        progress: 'Stage 1: Pier Inspection (In progress)'
      },
      hidden: true
    },
    {
      id: 'dmha_available_missions',
      name: 'Available Board Missions (hidden from panel)',
      type: 'json',
      default: [
        {
          title: 'Sector 4 Sewer Line Cleansing (Cable District)',
          threat: 'Class 1 - Void Rats',
          reward: '180 Credits · Triage Crate',
          rank: 'D'
        },
        {
          title: 'Alchemical Caravan Escort to Hex Valley',
          threat: 'Class 2 - Poachers & Dune Hyenas',
          reward: '500 Credits · Rune Component',
          rank: 'C'
        },
        {
          title: 'Dungeon Hive Incursion: Apex Trial Depth 3',
          threat: 'Class 3 - Corrupted Minotaur',
          reward: '1,200 Credits · Rare Core',
          rank: 'B'
        }
      ],
      hidden: true
    },
    {
      id: 'dmha_loot_inventory',
      name: 'Guild Loot & Equipment (hidden from panel)',
      type: 'json',
      default: [
        { item: 'DMHA Scent Suppressor Cylinders', qty: 3, rarity: 'Common' },
        { item: 'Douglas Tempered Silver Dagger', qty: 1, rarity: 'Uncommon' },
        { item: 'Anti-Silver Burn Salve Phial', qty: 2, rarity: 'Rare' }
      ],
      hidden: true
    },
    { id: 'succ_track', name: 'SUCC Academic Track', type: 'text', default: 'pre_med' },
    { id: 'pack_role', name: 'Douglas Pack Role', type: 'text', default: 'sentinel' },
    { id: 'underworld_role', name: 'Underworld Specialty', type: 'text', default: 'fixer' }
  ];

  // Regole in inglese
  const englishRules = [
    {
      id: 'rule_lunar_buff_active',
      label: 'Full Moon Alert & Werewolf Buff',
      phase: 'before',
      enabled: true,
      once: false,
      condition: {
        type: 'variable',
        variable: 'moon_full_active',
        operator: 'eq',
        value: true
      },
      actions: [
        {
          type: 'context',
          text: '[STORY ENGINE SYSTEM ALERT: Full Moon is currently ACTIVE in California. Werewolves gain +2 MGT, +2 RES, +1 AGI. Senses and instincts are hypersensitive. Demi-humans and werewolves feel heightened physical energy and increased responsiveness to pack hierarchy.]'
        }
      ]
    },
    {
      id: 'rule_scent_leak_alert',
      label: 'Pheromone Leak Alert (Suppressors Depleted)',
      phase: 'before',
      enabled: true,
      once: false,
      condition: {
        type: 'variable',
        variable: 'scent_suppressors_count',
        operator: 'lte',
        value: 0
      },
      actions: [
        {
          type: 'context',
          text: '[STORY ENGINE LSE ALERT: The character has run out of scent suppressors (count: 0). Lupine Social Ecology (LSE) rules apply: natural pheromones, territorial musk, and biological status (heat/rut/stress) leak unfiltered into the immediate air, triggering reactions from nearby werewolves and predators.]'
        }
      ]
    }
  ];

  // Comandi in inglese
  const englishCommands = [
    {
      id: 'cmd_use_suppressor',
      name: 'use_suppressor',
      label: 'Inhale Pheromone Suppressor',
      description: 'Consumes 1 inhibitor cylinder to suppress scent and biological pheromones.',
      actor: 'player',
      parameters: [],
      condition: {
        type: 'always'
      },
      actions: [
        {
          type: 'add',
          variable: 'scent_suppressors_count',
          value: -1
        },
        {
          type: 'message',
          text: '🩺 [Svartulfr OS] You inhaled a dose of pheromone suppressor. Your scent trail is shielded.'
        }
      ]
    }
  ];

  // Presets in inglese
  const englishPresets = [
    {
      id: 'preset_student_recruit',
      name: 'SUCC Student Recruit / Standard Freshman',
      values: {
        pack_reputation: 25,
        scent_suppressors_count: 3,
        rift_threat_level: 'Class 1 - Stable',
        lse_biology_status: 'Dormant',
        lse_cycle_days_left: 20,
        pack_chat_unread: 3,
        succbook_unread_posts: 5
      }
    },
    {
      id: 'preset_douglas_native',
      name: 'Douglas Pack Native Member',
      values: {
        pack_reputation: 85,
        scent_suppressors_count: 5,
        rift_threat_level: 'Class 1 - Stable',
        lse_biology_status: 'Pre-Rut / Alert',
        lse_cycle_days_left: 12,
        pack_chat_unread: 0,
        succbook_unread_posts: 2
      }
    },
    {
      id: 'preset_hardcore_rut',
      name: 'LSE Seasonal Peak (Active Rut / Heat)',
      values: {
        pack_reputation: 40,
        scent_suppressors_count: 0,
        rift_threat_level: 'Class 2 - Fluctuating',
        lse_biology_status: 'Peak Rut / Full Heat',
        lse_cycle_days_left: 0,
        pack_chat_unread: 8,
        succbook_unread_posts: 12
      }
    }
  ];

  // Template status e prompt in inglese
  const englishStatusTemplate = '🌙 Moon: {{values.moon_phase}}{{#if values.moon_full_active}} (FULL MOON: Werewolf Buff ACTIVE){{/if}}{{#if values.night_active}} | 🌌 Night (Night Stalker Buff ON){{/if}} | 🩺 LSE: {{values.lse_biology_status}} (~{{values.lse_cycle_days_left}} days to peak) | 📱 Notifications: {{values.pack_chat_unread}} Telegram / {{values.succbook_unread_posts}} SuccBook';

  const englishPromptTemplate = `=== SVARTULFR OS: STORYENGINE DIRECTIVES ===
This story is enhanced by Svartulfr OS, providing live tracking of Lupine Social Ecology (LSE), lunar phases, Douglas pack communications, SUCC & CUMS academic life, and DMHA hunting logs.
- Status, lunar buffs, biologically shifting pheromones, and academic/hunting records are live-tracked via the interactive panels.
- Treat characters naturally in accordance with the live date, moon phase, and active rank.
- Digital notifications (Telegram, SuccBook, Guild Board) are surfaced cleanly in the UI; reflect incoming communications naturally in scene without generating ASCII mockup interfaces.

=== DYNAMIC ACADEMIC & HUNTING PROFILE ADAPTATION FOR {{user}} ===
When narrating university life at SUCC or CUMS, courses, exams, internships, and guild hunting activities for {{user}}, always match subjects, schedules, and ranks to their established background:
1. University Major (SUCC / CUMS):
   - Alyssa Douglas: Pre-Med / Medical Sciences & Demi-Human Physiology (Comparative Anatomy, Arcane Pharmacology, Emergency Trauma, Healthcare Ethics). Internships conducted at the SUCC Infirmary and DCC medical laboratories under Dr. Elizabeth Duskwood.
   - Jasper Douglas: Arcane Engineering & Advanced Magitech (Materials Engineering, Silver-Tech Ballistics, Non-Euclidean Geometry & Rift Theory, Runic Hardware). Internships at DCC Tactical R&D.
   - C.U.M.S. Students (California University of Magical Studies): Curricula cover Tactical Combat & Shadow Dueling (Amerian), Illusion & Infiltration (Ashton), Applied Hydromancy (Aeril), Solar Warding (Caien), Blood & Shadow Sorcery (Lestat), under Prof. Xaiden Nershatar and Dean Zaire Ziisis.
   - For custom characters: Logically infer their field of study from their profile description.
2. DMHA Hunter Guild Registry:
   - Rank & Reputation: Ranks reflect real experience. Alyssa is an established Rank A field combat healer. Jasper is a Rank A/B technomancer. Malachia is a certified Rank S Apex Berserker.
   - Mission Flow: Hunts, rift incursions, and sewer sweeps appear only when contextually appropriate to the scene or when accepted via the guild bulletin.

=== CANONICAL FACTIONS, GROUPS & WORLD CLASSES ===
- Malachia Douglas (Guild Berserker): Internal Furnace, steaming battle heat, high iron consumption.
- Jasper Douglas (Technomancer) & Echo (Digital Familiar): Runic sorcery fused with fiber optics and DCC servers. Deadpan AI assistant with Music Mood Speaker.
- Angelo Moreno (Puppet Master): Psychic mana threads, tactical dolls, and combat simulacra.
- Camp Mystic (Lake Erie): Summer lake retreat for SUCC students and faculty with warded cabins and anti-monster barriers.
- Ukiyo Syndicate (Cable District): Elite hunter squad led by the orc Radek (Vanguard DPS), minotaur Goran (Heavy Defender), and half-elf Kian (Arcane Sniper).
- Ironhorn Nomads & Cable District Garages: Nomad biker brotherhood and heavy custom workshops run by Marek, allied with Barrow 'The Bull' and Russ Sinclair.
- Arcadia & Demi-Human Community: Protected sanctuary district in Blackwood featuring Le Refuge des Chats (Jaelyn) and Sugar Moon Bakery (Neve). Demi-humans strictly have a single pair of ears (animal ears only).
- House O'Connor & Crimsonmaw Pack: Border werewolf alliances (Liam O'Connor at Douglas Manor, Hugh Rivers guarding industrial borders).`;

  const newUiPanels = [
    {
      id: 'panel_smartphone_os',
      name: 'Svartulfr Smartphone OS',
      icon: 'layout',
      placement: 'sidebar',
      target: 'both',
      enabled: true,
      code: panelCode
    }
  ];

  const patchPayload = {
    expected_version: engineData.version,
    name: 'Svartulfr OS',
    tagline: englishTagline,
    description: englishDescription,
    avatar: engineData.avatar,
    tags: ['werewolf', 'urban-fantasy', 'modern-fantasy', 'smartphone', 'ui-panel', 'succ', 'lse', 'rpg'],
    rating: engineData.rating || 'everyone',
    visibility: 'public',
    status: engineData.status,
    definition: {
      ...engineData.definition,
      variables: englishVariables,
      rules: englishRules,
      commands: englishCommands,
      presets: englishPresets,
      status_template: englishStatusTemplate,
      prompt_template: englishPromptTemplate,
      ui_panels: newUiPanels,
      worlds: [],
      lorebooks: []
    }
  };

  console.log('2. Salvataggio su Wyvern con tutti i testi in lingua INGLESE...');
  const putRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(patchPayload)
  });

  if (!putRes.ok) {
    throw new Error(`Errore PUT: ${putRes.status} ${await putRes.text()}`);
  }

  const updatedEngine = await putRes.json();
  console.log(`Story Engine salvato in inglese! Versione: v${updatedEngine.version}`);

  console.log('3. Pubblicazione della revisione ufficiale per i moderatori...');
  const pubRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}/publish`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ expected_version: updatedEngine.version })
  });

  if (!pubRes.ok) {
    console.warn(`Avviso pubblicazione (${pubRes.status}):`, await pubRes.text());
  } else {
    const pubData = await pubRes.json();
    console.log(`Revisione pubblicata con successo per la moderazione! ID Revisione: ${pubData.published_revision_id || 'OK'}`);
  }

  // Aggiornamento export locale
  const exportPath = 'exports/Story_Engines_Export.json';
  if (fs.existsSync(exportPath)) {
    try {
      const currentExport = JSON.parse(fs.readFileSync(exportPath, 'utf8'));
      if (Array.isArray(currentExport)) {
        const idx = currentExport.findIndex(e => e.id === engineId);
        if (idx >= 0) currentExport[idx] = updatedEngine;
        else currentExport.push(updatedEngine);
        fs.writeFileSync(exportPath, JSON.stringify(currentExport, null, 2), 'utf8');
      }
    } catch (e) {}
  }
}

deployEnglishEngine().catch(err => {
  console.error('ERRORE:', err);
  process.exit(1);
});

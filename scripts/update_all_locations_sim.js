const fs = require('fs');

const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
const USD = "fbecc738-f9f7-4426-b8a1-a237b8ad922c";
const DMHA = "8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a";

// 1. Definition of Marketplaces & Iconic Items
const MARKETPLACE_DEFS = {
  "_63BP7yfwEpEJbDgEqP2ew": { // Sugar Moon Bakery
    enabled: true,
    name: "Sugar Moon Bakery",
    description: "Pasticceria artigianale di Arcadia famosa per dolci al miele di luna, pane fresco e infusi calmi per therianthropi.",
    buy_rate: 0.5,
    inventory: [
      { lexicon_entry_id: "_nKrK7KRNbpFHtg6f8QkLj", stock: 20, price_override: { [USD]: 8 } },
      { lexicon_entry_id: "_HFeBYyrcXfB1pcbDW8NC6", stock: 15, price_override: { [USD]: 6 } },
      { lexicon_entry_id: "_Xcgd9WWjX3GHMm7DkaLtw", stock: 25, price_override: { [USD]: 5 } },
      { lexicon_entry_id: "_NyLqqJg949nYc7wRKmx3Y", stock: 30, price_override: { [USD]: 4 } }
    ]
  },
  "_XUV6jWXTXG6wgj2WKBEpr": { // The Roasted Bean
    enabled: true,
    name: "The Roasted Bean Coffeehouse",
    description: "Caffetteria accademica all'interno della Basilica Library con espresso al mana, intrugli concentrati e frullati iperproteici.",
    buy_rate: 0.5,
    inventory: [
      { lexicon_entry_id: "_dQETHC2VcbXFYdzfrMq4q", stock: 40, price_override: { [USD]: 6 } },
      { lexicon_entry_id: "_rp37qdqnyPYJcaxXVU3w7", stock: 30, price_override: { [USD]: 9 } },
      { lexicon_entry_id: "_6yGCH9nwKCA6AjYAB4aVh", stock: 35, price_override: { [USD]: 7 } }
    ]
  },
  "_1wcb4XHMXfg2YBwa2PFkM": { // The Lunar Pharmacy
    enabled: true,
    name: "The Lunar Pharmacy & Herbal Dispensary",
    description: "Dispensario farmaceutico di Solarton Square specializzato in soppressori di feromoni LSE, pomate per ustioni da argento e sieri rigeneranti.",
    buy_rate: 0.6,
    inventory: [
      { lexicon_entry_id: "_rpdaHWWHwAm9MtRdwBLFc", stock: 25, price_override: { [USD]: 45 } },
      { lexicon_entry_id: "_knRtF326efCGWVceqTtLC", stock: 30, price_override: { [USD]: 35 } },
      { lexicon_entry_id: "_nX6qJe6VLcQYhHYbmjA8r", stock: 15, price_override: { [USD]: 60 } },
      { lexicon_entry_id: "_EQFdgEkN3tkLzwHjjqrjz", stock: 20, price_override: { [USD]: 50 } }
    ]
  },
  "_7LmyTdEgVPeFbmkG4Rwe7": { // Directions & Dragons
    enabled: true,
    name: "Directions & Dragons Hobby & TTRPG Shop",
    description: "Negozio storico di giochi da tavolo, dadi in ossidiana, miniature in peltro e manuali arcani a Solarton Square.",
    buy_rate: 0.5,
    inventory: [
      { lexicon_entry_id: "_yYWeN3Wf4KdtTB9MnMaRK", stock: 20, price_override: { [USD]: 35 } },
      { lexicon_entry_id: "_76mhdVfxx2Xc8WJGkbFNm", stock: 10, price_override: { [USD]: 40 } },
      { lexicon_entry_id: "_17kEd89wqx2Nwf8pWJGe9", stock: 15, price_override: { [USD]: 18 } }
    ]
  },
  "_mfW6WAcWPcwkPxWyfPCye": { // The Dusty Coyote Diner
    enabled: true,
    name: "The Dusty Coyote Roadhouse Diner",
    description: "Diner autentico di Bakersfield con porzioni pantagrueliche per therianthropi, monster burger, caffe nero e fette di torta.",
    buy_rate: 0.4,
    inventory: [
      { lexicon_entry_id: "_kqkxxYEjhydrdHWgtkN9j", stock: 35, price_override: { [USD]: 15 } },
      { lexicon_entry_id: "_8NNchTCV4k92J4kQVgNJ1", stock: 50, price_override: { [USD]: 4 } },
      { lexicon_entry_id: "_V9x7dGabzykELrmaHAzq3", stock: 25, price_override: { [USD]: 7 } }
    ]
  },
  "_UW8r3dr8VW7T6e1pFEd6U": { // Kerrigan & Sons Butchers
    enabled: true,
    name: "Kerrigan & Sons Premium Meats & Charcuterie",
    description: "Macelleria artigianale a Bricklane Mall specializzata in tagli crudi frollati, costate, salsicce di cinghiale e midollo fresco.",
    buy_rate: 0.5,
    inventory: [
      { lexicon_entry_id: "_U9tGgqpbdEtrQ8BTHeNXH", stock: 20, price_override: { [USD]: 32 } },
      { lexicon_entry_id: "_gWmQ7WcNyqRHt1bn19Bzr", stock: 30, price_override: { [USD]: 14 } },
      { lexicon_entry_id: "_NUTnm79jUTXX4F9qpUDRE", stock: 25, price_override: { [USD]: 12 } }
    ]
  },
  "_3tNeXcGBfcUX6J1mtjqAw": { // Claws Steel & Ink
    enabled: true,
    name: "Claws Steel & Ink Tattoo & Piercing Parlor",
    description: "Studio professionale di tatuaggi e piercing a Bricklane Mall con aghi runici, barre in titanio nero e balsami lenitivi all'aloe.",
    buy_rate: 0.5,
    inventory: [
      { lexicon_entry_id: "_XBKWVDfDfJkUpHqNAtkNL", stock: 25, price_override: { [USD]: 18 } },
      { lexicon_entry_id: "_E7YP9KKKXP3GcqgxtXYwG", stock: 30, price_override: { [USD]: 25 } }
    ]
  },
  "_Vhqnmrg3YAdWMTfPcGGxP": { // Tidewrack Surf & Rental
    enabled: true,
    name: "Tidewrack Surf & Rental Outpost",
    description: "Negozio e noleggio fronte mare per tavole da surf rinforzate in fibra di carbonio, mute oceaniche in neoprene e paraffina.",
    buy_rate: 0.5,
    inventory: [
      { lexicon_entry_id: "_GcEzkXjfe2cpgLcpz2e4E", stock: 8, price_override: { [USD]: 380 } },
      { lexicon_entry_id: "_m92yL4TN6gtYbjxhDR1wf", stock: 12, price_override: { [USD]: 160 } },
      { lexicon_entry_id: "_3XwFNeRcU7w2FcTtbxt6c", stock: 40, price_override: { [USD]: 8 } }
    ]
  },
  "_GYF4znCTjcJgLH9XYVbg8": { // Full Moon Market
    enabled: true,
    name: "Full Moon Open Market & Curiosities",
    description: "Bazar e fiera notturna a Solarton Square con amuleti protettivi in argento, muschio bioluminescente e borse in cuoio artigianali.",
    buy_rate: 0.6,
    inventory: [
      { lexicon_entry_id: "_hT1ddewgttrJECmxBDwbY", stock: 20, price_override: { [USD]: 30 } },
      { lexicon_entry_id: "_LYJ2JgC7Hh6y7BkxfeRhf", stock: 25, price_override: { [USD]: 22 } },
      { lexicon_entry_id: "_yK4Mdxr2k7dea6aQJjqU1", stock: 18, price_override: { [USD]: 25 } }
    ]
  },
  "_FQVVaJrXtd4Y66mPna87C": { // Rhodes Farm
    enabled: true,
    name: "Rhodes Family Farmstand & Dairy",
    description: "Punto vendita agricolo della famiglia Rhodes con latte crudo di pascolo, formaggi artigianali affumicati e burro dolce montato a mano.",
    buy_rate: 0.5,
    inventory: [
      { lexicon_entry_id: "_aaJ26BUnQdhXaTrL6CMKc", stock: 30, price_override: { [USD]: 7 } },
      { lexicon_entry_id: "_B2Ufw6VfzPK2jm3WFHBgg", stock: 20, price_override: { [USD]: 16 } },
      { lexicon_entry_id: "_QBF8D9z1cJM7Brb63WEtm", stock: 25, price_override: { [USD]: 6 } }
    ]
  },
  "_RVRf9PtEdwhGt3rGGFjMC": { // The Cable District (Workshop & Bikers)
    enabled: true,
    name: "Cable District Garages & Mod Workshop",
    description: "Officina meccanica specializzata in chopper pesanti, motori termici, lubrificanti al grafene e toppe Ironhorn Nomads.",
    buy_rate: 0.6,
    inventory: [
      { lexicon_entry_id: "_PMz2XtFccYTgUzcpRxHPx", stock: 30, price_override: { [USD]: 25 } },
      { lexicon_entry_id: "_NgNrDUPFNPHWrD8FrcKY1", stock: 15, price_override: { [USD]: 45 } },
      { lexicon_entry_id: "_rVQnejyY8XEgTWNzq4trh", stock: 20, price_override: { [USD]: 20 } }
    ]
  },
  "_BD8F76PngMyD2yURFWV76": { // La Dimora del Rifugio (Le Refuge des Chats)
    enabled: true,
    name: "Le Refuge des Chats Sanctuary & Tearoom",
    description: "Santuario accogliente e sala da te per famigli felini, con bevande rilassanti all'erba gatta e biscotti empatici curativi.",
    buy_rate: 0.5,
    inventory: [
      { lexicon_entry_id: "_WzhY7j4bDWPULghNkEAT2", stock: 35, price_override: { [USD]: 7 } },
      { lexicon_entry_id: "_cMaDqw4N4akacY1eq3YwM", stock: 40, price_override: { [USD]: 5 } }
    ]
  },
  "_hfm1W4nYnXfQEqcNGwNxr": { // The Verve
    enabled: true,
    name: "The Verve VIP Lounge & Bar",
    description: "Lounge bar di lusso a Bluemoon con cocktail d'autore, riserva Douglas di bourbon 18 anni e champagne millesimato.",
    buy_rate: 0.5,
    inventory: [
      { lexicon_entry_id: "_eczVz8mKa6agXjgkAXUDn", stock: 15, price_override: { [USD]: 28 } },
      { lexicon_entry_id: "_H3DqdqrxKjjEAaenVdGpn", stock: 12, price_override: { [USD]: 35 } },
      { lexicon_entry_id: "_YxGJRFDkjdVyeH1mJNM1T", stock: 40, price_override: { [USD]: 15 } },
      { lexicon_entry_id: "_UVX1RAqE8CWz8ywYkT4Fm", stock: 20, price_override: { [USD]: 75 } }
    ]
  },
  "_VbjcwqJnc7BaED9A9t2Dq": { // Sidewinders Bar & Nightclub
    enabled: true,
    name: "Sidewinders Bar & Nightclub",
    description: "Locale notturno studentesco di Solarton con shot di tequila all'agave, cocktail neon fosforescenti e birre alla spina.",
    buy_rate: 0.4,
    inventory: [
      { lexicon_entry_id: "_EkDh4LJGDj8KmFbYgQU6V", stock: 50, price_override: { [USD]: 8 } },
      { lexicon_entry_id: "_PVKE7rfUNxJAmQK9NfL9Q", stock: 45, price_override: { [USD]: 12 } },
      { lexicon_entry_id: "_YxGJRFDkjdVyeH1mJNM1T", stock: 30, price_override: { [USD]: 10 } }
    ]
  }
};

// 2. Definition of Jobs for specific Locations
const JOBS_MAPPING = {
  "_63BP7yfwEpEJbDgEqP2ew": ["_tatXe1j7kFVmnKNzftMrE"], // Sugar Moon Bakery
  "_XUV6jWXTXG6wgj2WKBEpr": ["_mkxzPqVHBFcxtwKw9N113"], // The Roasted Bean
  "_BD8F76PngMyD2yURFWV76": ["_1j2dE6JDHY3znKRRk8z8P"], // La Dimora del Rifugio
  "_1wcb4XHMXfg2YBwa2PFkM": ["_k6pYEaPrh8htM8hnj9fET"], // The Lunar Pharmacy
  "_RVRf9PtEdwhGt3rGGFjMC": ["_ENGjChMgjbW2wURn88wNg"], // The Cable District
  "_7LmyTdEgVPeFbmkG4Rwe7": ["_g1dczxekHn1XtWLJhCT68"], // Directions & Dragons
  "_FQVVaJrXtd4Y66mPna87C": ["_Hh9HDxT9ecVGeN9dLjUVF"], // Rhodes Farm
  "_UW8r3dr8VW7T6e1pFEd6U": ["_djeGA7yd1HFcRGHztQg9a"], // Kerrigan Butchers
  "_mfW6WAcWPcwkPxWyfPCye": ["_EpWMABRmDgGAbxkQcYrtP"], // Dusty Coyote Diner
  "_VbjcwqJnc7BaED9A9t2Dq": ["_j4ckmcna7dtdLAY6H4eKC"], // Sidewinders
  "_hfm1W4nYnXfQEqcNGwNxr": ["_NH6npW4nBExJXHD8mVtdR"], // The Verve
  "_3tNeXcGBfcUX6J1mtjqAw": ["_GFJVM4qaRBCQUFNQ7BFYW"], // Claws Steel & Ink
  "_Vhqnmrg3YAdWMTfPcGGxP": ["_nVKABK6mKebCncyBnKdKc"], // Tidewrack Surf
  "_jYJxF7fte2Gz1F2HGXpUR": ["_RB6TdAUCMcWUHBPYtdCkF"], // Basilica Library
  "_erHMcydnPVEyk7NY3K9wf": ["_Em2BRqwrRy1BMK66En3j9"], // Team Ukiyo
  "_yPxa34RwGz9wbjm1zjhLJ": ["_Yz4XB7PezjgKkqqrdg8jC"]  // Camp Mystic
};

// 3. Definition of Properties (Housing / Dorms / Apartments / Suites)
const PROPERTY_DEFS = {
  "_6KT7hL8LMFzU3dK6h1wax": { // Wyrm Dormitories
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 450 }
  },
  "_WAHzgab11F3k9BRqNJHb2": { // West & East Wings (Mixed)
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 400 }
  },
  "_Wrg47JYXUBq7R2yT47Nrm": { // South Wing (Supernatural)
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 420 }
  },
  "_AdgYjLPG44QV2Xrq9ePgJ": { // North Wing (Human)
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 380 }
  },
  "_xLd2GzGayGJXUhjAdTPye": { // Additional Student Housing
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 350 }
  },
  "_yXApVAkzqLrFkLkhW7fdU": { // Fraternity & Sorority Row (Greek Row)
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 500 }
  },
  "_E6ga9CmYQ31CwNkrHkGX9": { // Alpha Rho Omega
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 480 }
  },
  "_tFj1yzTVDaEhdJLYe13YM": { // Alpha Sigma Sigma
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 460 }
  },
  "_Wj2hkqUxDrB4aDaGDM8q9": { // Beta Epsilon Epsilon
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 480 }
  },
  "_p1JatqFwBPeKPQrh6CmGe": { // Beta Rho Omega
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 520 }
  },
  "_Ug2jTR6Wq3XGhQGzchcft": { // Delta Omicron Epsilon
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 500 }
  },
  "_jrpjEjGF6eFNcVWATaH91": { // Kappa Sigma Alpha
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 500 }
  },
  "_89J6GpNndcJnAEUB33DqP": { // Mu Alpha Nu
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 490 }
  },
  "_bpQD4kCGHK1LW7WjahdU4": { // Mu Omega Omega
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 470 }
  },
  "_Ep6xM191zpn6jpUygJakP": { // Theta Iota Theta
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 530 }
  },
  "_9YKj9HxFkRWnNJUJk84Tr": { // Artemis Dorms
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 600 }
  },
  "_wEkzHgpxfetQr16bTWNUP": { // Apollo Dorms
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 600 }
  },
  "_3kFK6JCz9WEM2wGNRXnxq": { // Nocturnal Hall
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 650 }
  },
  "_nKAXKmzHrCbRTQeqqFx3T": { // Nightwine Hall
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 650 }
  },
  "_CPWKPYwWeDY7ktNgBLWAy": { // Apartment C
    enabled: true, rentable: true, purchasable: true,
    rent_interval_hours: 168, rent_price: { [USD]: 550 },
    purchase_price: { [USD]: 180000 }
  },
  "_WX48nzYX28GRM1gj9gQBf": { // Flat above Directions & Dragons
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 600 }
  },
  "_UeKEhHTnCP6yQk7mhMVU1": { // Coastal Residential
    enabled: true, rentable: true, purchasable: true,
    rent_interval_hours: 168, rent_price: { [USD]: 1200 },
    purchase_price: { [USD]: 350000 }
  },
  "_9qzfFrQrFW1X3yBznanaT": { // Hex Valley Estates
    enabled: true, rentable: true, purchasable: true,
    rent_interval_hours: 168, rent_price: { [USD]: 2500 },
    purchase_price: { [USD]: 1200000 }
  },
  "_CFdc6hPMPCQMja7ABT3zP": { // Parco Roulotte di Oildale
    enabled: true, rentable: true, purchasable: true,
    rent_interval_hours: 168, rent_price: { [USD]: 120 },
    purchase_price: { [USD]: 25000 }
  },
  "_RTxCmM7pKQGx8VVA83B7Q": { // Eidolon Creative Private Suites
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 1800 }
  },
  "_qBt3jf1kppwrmMwTBbYJB": { // Dead Dog Motel / Voidspace
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 150 }
  },
  "_mUHCbXLjDAy8YqraaR7jf": { // Villa Douglas: Guest Wing
    enabled: true, rentable: true, purchasable: false,
    rent_interval_hours: 168, rent_price: { [USD]: 1 }
  },
  "_88QNj8BnFMN143XxNat1n": { // Dullahan's Condo
    enabled: true, rentable: true, purchasable: true,
    rent_interval_hours: 168, rent_price: { [USD]: 800 },
    purchase_price: { [USD]: 280000 }
  },
  "_TLEaxwQCB24kQYfYHy8pq": { // Rory's Estate
    enabled: true, rentable: true, purchasable: true,
    rent_interval_hours: 168, rent_price: { [USD]: 5000 },
    purchase_price: { [USD]: 3500000 }
  }
};

async function main() {
  console.log('Fetching all current locations from Wyvern API...');
  const res = await fetch('https://app.wyvern.chat/api/worlds/locations/world/_CgYT8fHXpDC4crjmegQF7', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (!res.ok) {
    throw new Error('Failed to fetch locations: ' + res.status);
  }
  const locations = await res.json();
  console.log(`Fetched ${locations.length} locations.`);

  let updatedCount = 0;
  let skippedCount = 0;
  let errorCount = 0;

  for (let i = 0; i < locations.length; i++) {
    const loc = locations[i];
    const locId = loc.id || loc._id;
    
    // Determine ideal simulation overrides
    const propConfig = PROPERTY_DEFS[locId] || (loc.property_config?.enabled ? loc.property_config : { enabled: false });
    const marketConfig = MARKETPLACE_DEFS[locId] || (loc.marketplace_config?.enabled ? loc.marketplace_config : { enabled: false });
    const jobsList = JOBS_MAPPING[locId] || (loc.jobs && loc.jobs.length > 0 ? loc.jobs : []);

    // Check if changes are needed
    const currentProp = JSON.stringify(loc.property_config || { enabled: false });
    const targetProp = JSON.stringify(propConfig);

    const currentMarket = JSON.stringify(loc.marketplace_config || { enabled: false });
    const targetMarket = JSON.stringify(marketConfig);

    const currentJobs = JSON.stringify(loc.jobs || []);
    const targetJobs = JSON.stringify(jobsList);

    if (currentProp === targetProp && currentMarket === targetMarket && currentJobs === targetJobs) {
      skippedCount++;
      continue;
    }

    const payload = {
      property_config: propConfig,
      marketplace_config: marketConfig,
      jobs: jobsList
    };

    console.log(`[${i + 1}/${locations.length}] Updating "${loc.name}" (${locId})...`);
    try {
      const putRes = await fetch(`https://app.wyvern.chat/api/worlds/locations/${locId}`, {
        method: 'PUT',
        headers: {
          'Authorization': 'Bearer ' + token,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (!putRes.ok) {
        console.error(`  ERROR updating ${loc.name}: status ${putRes.status}`);
        errorCount++;
      } else {
        updatedCount++;
      }
    } catch (err) {
      console.error(`  EXCEPTION updating ${loc.name}:`, err.message);
      errorCount++;
    }

    // Small delay to be polite to the API
    await new Promise(r => setTimeout(r, 120));
  }

  console.log('\n=== SUMMARY ===');
  console.log(`Total Locations: ${locations.length}`);
  console.log(`Updated: ${updatedCount}`);
  console.log(`Skipped (already ideal): ${skippedCount}`);
  console.log(`Errors: ${errorCount}`);
}

main().catch(console.error);

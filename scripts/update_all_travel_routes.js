const fs = require('fs');
const crypto = require('crypto');

const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
const worldId = '_CgYT8fHXpDC4crjmegQF7';

function genUuid() {
  return crypto.randomUUID();
}

async function main() {
  console.log('Fetching world data...');
  const res = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (!res.ok) throw new Error('Fetch failed: ' + res.status);
  const world = await res.json();

  const currentRoutes = world.travel_routes || [];
  console.log(`Current routes count: ${currentRoutes.length}`);

  // Location IDs mapping
  const LOC = {
    // Cities / Roots
    BlackwoodCity: "_D8B9QAfHPn3NfD4mAnJen",
    Solarton: "_761mFFeCcQyR9JxhLCWcy",
    Bakersfield: "_fekTA9NRygQ49q7cxRz8A",
    LosAngeles: "_X4A8gWVr43a7dRr9TbJ4m",
    HexValley: "_k118p3PTLgG88pkXn48BQ",
    Ventura101: "_FrXnp2CALTP44CP3KVAhb",
    CampMystic: "_yPxa34RwGz9wbjm1zjhLJ",
    DDMVoidspace: "_BUfxJEGc4Td36H8kMmVD3",

    // Blackwood Districts
    SevenHills: "_EwMMJ7KEg9ATJ3mTXBaha",
    Oldtown: "_Gnm9WMQNjhUWJLhrkpqQk",
    Dockside: "_B7Eq8K8CUXrCe9NKATXGE",
    Bluemoon: "_MkkwDR7AHq4tYLmnk134f",
    Paradise: "_H6PUHPMMUEmM2wJbfd8et",
    Arcadia: "_X6R6dKTzkjdFk6cqdt2we",
    Ironworks: "_fyC1LJ8CAK8rP7k8Dr2a2",
    Uptown: "_8fRJTJVkd7VjkQ3jfJWQ1",
    CableDistrict: "_RVRf9PtEdwhGt3rGGFjMC",
    BlackwoodForest: "_HN1tmm3Ex4LBh2HtWGUbq",
    StBrugge: "_4wJ11ttfz78gfH2cqdx4R",
    VillaDouglas: "_9H2EmzRm92QxBpkmJUR1z",
    TheOtherworld: "_AqRjXRDRm23gAHJFaWC39",
    SugarMoonBakery: "_63BP7yfwEpEJbDgEqP2ew",
    McKaySmokehouse: "_fBmdJReXCqdRLzYzyKw7w",
    TheHorns: "_MxFzj8MUgHPXd8Y9m8hX4",
    ApartmentC: "_CPWKPYwWeDY7ktNgBLWAy",
    DocksideFerry: "_AWyPeCP8QWhD4D1M6hfzT",

    // Solarton PIs
    SolartonSquare: "_Mq1DYmKdnkR83YBjNRyXr",
    BricklaneMall: "_hGpPMY77NaH4j6AxNGLVe",
    Sidewinders: "_VbjcwqJnc7BaED9A9t2Dq",
    CoastalResidential: "_UeKEhHTnCP6yQk7mhMVU1",
    SolartonFerry: "_NVALjebTDk1kPC9AjWhWt",
    SolartonBeach: "_a2pRKBjYnQ1Q1LaN6xdeh",
    SUCC: "_j67Dp2PVwFCpdrfWRYV2M",
    ClinicaOrtus: "_aWcjmPKnChpzGndYD62gP",
    RefugeChats: "_BD8F76PngMyD2yURFWV76",
    StaticInk: "_CKkP1PfqRJDQLBPQeFyWF",
    DullahansCondo: "_88QNj8BnFMN143XxNat1n",
    SolartonHigh: "_BgLjFRGNj9YX7tzybBzda",
    OpenCasket: "_EK4EPeKCjmFd3EbPNTCkT",
    RogersMotors: "_CAhgArEXA2eBDQPpPe1gE",
    DirectionsDragons: "_7LmyTdEgVPeFbmkG4Rwe7",
    FlatAboveDD: "_WX48nzYX28GRM1gj9gQBf",
    LunarPharmacy: "_1wcb4XHMXfg2YBwa2PFkM",
    FullMoonMarket: "_GYF4znCTjcJgLH9XYVbg8",
    KerriganButchers: "_UW8r3dr8VW7T6e1pFEd6U",
    ClawsInk: "_3tNeXcGBfcUX6J1mtjqAw",
    TidewrackSurf: "_Vhqnmrg3YAdWMTfPcGGxP",

    // SUCC Campus Core
    LunarQuad: "_WrymW8qTETkm7r1QXQGaT",
    BasilicaLibrary: "_jYJxF7fte2Gz1F2HGXpUR",
    RoastedBean: "_XUV6jWXTXG6wgj2WKBEpr",
    ArcherWolfwoodHall: "_A3V3pEPJjBEtNK4nMCqwP",
    HelsingChapel: "_jX3bYbn8FHra6qNYUC3Ux",
    UnicornHall: "_nhdQ7xkycT1yfn1wWXN8U",
    WyrmDorms: "_6KT7hL8LMFzU3dK6h1wax",
    ApolloDorms: "_wEkzHgpxfetQr16bTWNUP",
    ArtemisDorms: "_9YKj9HxFkRWnNJUJk84Tr",
    AdditionalHousing: "_xLd2GzGayGJXUhjAdTPye",
    GreekRow: "_yXApVAkzqLrFkLkhW7fdU",
    ScienceQuarter: "_DA14L9eU8wdcfFR1acpbn",
    ArtsBuilding: "_Dw9VQxmgEDGTyQdJzwJgG",
    StudentAssocBuilding: "_aLqMW6UHHj1D9M4xxENF7",
    SSC: "_G33ABhpFceN7HanHwp8rr",
    Clocktower: "_ptpGD1VeVep7YknRmhFXM",
    BullsStadium: "_Bx2U1xzg1D3wpFRe39L7y",
    IndoorPool: "_JTRYG4tbNaYd72V7cKNVQ",
    SportsFields: "_WRBThTNK3wJawVdLRhA1e",
    GymChanging: "_EmJg3zdjTT8kwteJJkyUR",

    // Hex Valley
    HexValleyFerry: "_C7Nj1emPcrhDQb1gFYMDr",
    HexValleyEstates: "_9qzfFrQrFW1X3yBznanaT",
    CUMS: "_Caw9nRwKf4Gx9VzW21QJj",

    // Transit & Border
    VenturaSquare: "_h9UDyMzPtBwnzfbjj3DP3",
    HalfwayHouse: "_XeqYfUxwTWKmy6rpmqaQC",
    DeadDogMotel: "_qBt3jf1kppwrmMwTBbYJB",
    SimiValley: "_4k3RT1nxw994yHRM66LQb",
    SimiInfopoint: "_82cNpDwVJwVd8qGRUgFw8",
    SimiGrid: "_KAa4FrdtffjCETKPEK7fr",
    HiveApexDungeon: "_CaKc8CcYADYxLRmb2GYpG",

    // Bakersfield
    BakersfieldSquare: "_11LzwJB9B6rGrEQTTd7xd",
    DustyCoyote: "_mfW6WAcWPcwkPxWyfPCye",
    RhodesFarm: "_FQVVaJrXtd4Y66mPna87C",
    ParcoRoulotte: "_CFdc6hPMPCQMja7ABT3zP",
    CampiPetroliferi: "_VEXr9e9eUWwEpFNCRUm9V",
    KernRiverCanyon: "_jx7cMhrTAtCztbPMJTb1H",
    MercatoContadino: "_tbbaxN7A3pgFQ8x73xGNr",

    // Los Angeles
    PershingSquare: "_16nUQjhqXaFaUEKy1zgpA",
    DCCTower: "_XD2gWgyhTYmDEXWkxMLer",
    Hollywood: "_pTqkAfBAEFUtEA3BqUjRz",
    BeverlyHills: "_yqQeB1GzKJyqfwjUPRP2M",
    RorysEstate: "_TLEaxwQCB24kQYfYHy8pq",
    SkidRow: "_NqaNWcjcwHXmXFTptBEbP",
    OsservatorioGriffith: "_N923td3fCdLPXBDDftp2T",
    FortMacArthur: "_cDDqVXg3jbxEhBd3qJ3ME",
    Molo42: "_jABzFFNTGRdRLEkNYTKx2",
    NeonMirage: "_NNtDFU6T1h929Kc79Uej1",

    // DDM
    DDMHQ: "_eUkmTYmVng7bdJTAb8cdC"
  };

  // 1. Process existing routes: fix broken location IDs and assign flavor distance
  const fixedExistingRoutes = currentRoutes.map(r => {
    const updated = { ...r };

    // Fix invalid legacy IDs
    if (updated.to_location_id === "_rnNnjzcmDkgg2xbHYFftH") updated.to_location_id = LOC.SolartonFerry;
    if (updated.to_location_id === "_6JEr2rqCjJa9tWzgbDcrb") updated.to_location_id = LOC.HexValley;
    if (updated.to_location_id === "_ndMkLAHyKgBDyeMpjwhBt") updated.to_location_id = LOC.IndoorPool;
    if (updated.from_location_id === "_ndMkLAHyKgBDyeMpjwhBt") updated.from_location_id = LOC.IndoorPool;
    if (updated.to_location_id === "_xfz8yrt2RjqHyTa8MXG3W") updated.to_location_id = LOC.WyrmDorms;

    // Assign distance if missing
    if (updated.distance == null || updated.distance === 0) {
      if (updated.travel_time >= 24) {
        updated.distance = 50; // Nautical miles for ferry
      } else if (updated.travel_time >= 3) {
        updated.distance = 110; // Long highway
      } else if (updated.travel_time === 2) {
        updated.distance = 85; // Highway commute (Solarton - Blackwood)
      } else if (updated.travel_time === 1) {
        updated.distance = 25; // Regional road / pass
      } else {
        // travel_time == 0
        updated.distance = 2; // Urban/campus walk or quick drive
      }
    }

    if (!updated.required_mediums || updated.required_mediums.length === 0) {
      updated.required_mediums = ["land"];
    }

    return updated;
  });

  // Track existing route pairs
  const existingPairSet = new Set();
  fixedExistingRoutes.forEach(r => {
    existingPairSet.add(`${r.from_location_id}<->${r.to_location_id}`);
    existingPairSet.add(`${r.to_location_id}<->${r.from_location_id}`);
  });

  // 2. Define New Missing Routes
  const newRoutesDefs = [
    // Blackwood City Districts
    {
      from: LOC.Oldtown, to: LOC.CableDistrict,
      time: 0, dist: 3, mediums: ["land"],
      desc: "Industrial boulevard leading south from Oldtown into The Cable District."
    },
    {
      from: LOC.BlackwoodCity, to: LOC.StBrugge,
      time: 0, dist: 5, mediums: ["land"],
      desc: "Gated private avenue climbing to St. Brugge Private Academy."
    },
    {
      from: LOC.Oldtown, to: LOC.BlackwoodForest,
      time: 1, dist: 12, mediums: ["land"],
      desc: "Old mountain highway passing beneath towering ancient redwoods into Blackwood Forest."
    },
    {
      from: LOC.BlackwoodForest, to: LOC.TheOtherworld,
      time: 1, dist: 8, mediums: ["land"],
      desc: "Concealed leyline trail through the silver fog into The Otherworld sanctuary.",
      hidden: true
    },
    {
      from: LOC.Oldtown, to: LOC.Bluemoon,
      time: 0, dist: 3, mediums: ["land"],
      desc: "Avenue connecting historical Oldtown to the modern nightlife of Bluemoon."
    },
    {
      from: LOC.Arcadia, to: LOC.SugarMoonBakery,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Quiet residential side street leading to Sugar Moon Bakery."
    },
    {
      from: LOC.Oldtown, to: LOC.McKaySmokehouse,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Stone cobblestone lane leading directly to McKay's Smokehouse."
    },
    {
      from: LOC.Dockside, to: LOC.TheHorns,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Harbor street running along warehouse docks into The Horns residential blocks."
    },
    {
      from: LOC.TheHorns, to: LOC.ApartmentC,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Brick stairwell and walkway leading up to Apartment C."
    },

    // Solarton Local PIs
    {
      from: LOC.Solarton, to: LOC.ClinicaOrtus,
      time: 0, dist: 2, mediums: ["land"],
      desc: "Medical avenue linking central Solarton to Clinica Ortus."
    },
    {
      from: LOC.Solarton, to: LOC.RefugeChats,
      time: 0, dist: 3, mediums: ["land"],
      desc: "Leafy side road leading to Le Refuge des Chats sanctuary."
    },
    {
      from: LOC.Solarton, to: LOC.StaticInk,
      time: 0, dist: 2, mediums: ["land"],
      desc: "Downtown arts alleyway leading to Static & Ink tattoo studio."
    },
    {
      from: LOC.Solarton, to: LOC.DullahansCondo,
      time: 0, dist: 2, mediums: ["land"],
      desc: "Quiet suburban avenue connecting to Coach D's private condo."
    },
    {
      from: LOC.Solarton, to: LOC.SolartonHigh,
      time: 0, dist: 3, mediums: ["land"],
      desc: "School corridor boulevard leading to Solarton High School."
    },
    {
      from: LOC.Solarton, to: LOC.OpenCasket,
      time: 0, dist: 2, mediums: ["land"],
      desc: "Underground street leading to The Open Casket club."
    },
    {
      from: LOC.Solarton, to: LOC.RogersMotors,
      time: 0, dist: 4, mediums: ["land"],
      desc: "Industrial commercial bypass out to Rogers' Bargain Motors lot."
    },
    {
      from: LOC.SolartonSquare, to: LOC.DirectionsDragons,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Square promenade storefront path to Directions & Dragons."
    },
    {
      from: LOC.DirectionsDragons, to: LOC.FlatAboveDD,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Rear exterior wooden staircase climbing to the flat above Directions & Dragons."
    },
    {
      from: LOC.SolartonSquare, to: LOC.LunarPharmacy,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Covered arcade pathway leading to The Lunar Pharmacy."
    },
    {
      from: LOC.SolartonSquare, to: LOC.FullMoonMarket,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Open cobblestone plaza opening into the stalls of Full Moon Market."
    },
    {
      from: LOC.BricklaneMall, to: LOC.KerriganButchers,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Ground-floor gourmet concourse leading to Kerrigan & Sons Butchers."
    },
    {
      from: LOC.BricklaneMall, to: LOC.ClawsInk,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Second-level urban corridor leading to Claws Steel & Ink."
    },
    {
      from: LOC.BricklaneMall, to: LOC.TidewrackSurf,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Beach-facing mall exit opening into Tidewrack Surf & Rental outpost."
    },

    // SUCC Campus Connections
    {
      from: LOC.LunarQuad, to: LOC.ArcherWolfwoodHall,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Central campus quad avenue leading up to Archer Wolfwood Hall."
    },
    {
      from: LOC.LunarQuad, to: LOC.HelsingChapel,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Stone pathway through the cypress grove to Helsing Chapel."
    },
    {
      from: LOC.LunarQuad, to: LOC.UnicornHall,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Student club concourse connecting to Unicorn Hall."
    },
    {
      from: LOC.BasilicaLibrary, to: LOC.RoastedBean,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Arched library corridor leading directly into The Roasted Bean coffeehouse."
    },

    // Hex Valley Local
    {
      from: LOC.HexValleyFerry, to: LOC.HexValley,
      time: 0, dist: 2, mediums: ["land"],
      desc: "Pier road climbing up from the ferry docks into Hex Valley."
    },
    {
      from: LOC.HexValley, to: LOC.HexValleyEstates,
      time: 0, dist: 6, mediums: ["land"],
      desc: "Misty private mountain highway curving into Hex Valley Estates."
    },
    {
      from: LOC.HexValley, to: LOC.CUMS,
      time: 0, dist: 4, mediums: ["land"],
      desc: "Enchanted avenue leading into the campus of California University of Magical Sciences."
    },

    // Transit & Border
    {
      from: LOC.Ventura101, to: LOC.VenturaSquare,
      time: 0, dist: 3, mediums: ["land"],
      desc: "Highway 101 exit ramp into coastal Ventura Square."
    },
    {
      from: LOC.Ventura101, to: LOC.HalfwayHouse,
      time: 0, dist: 2, mediums: ["land"],
      desc: "Roadside service lane leading into The Halfway House rest stop."
    },
    {
      from: LOC.Ventura101, to: LOC.SimiValley,
      time: 1, dist: 22, mediums: ["land"],
      desc: "State Route 118 corridor running eastward into Simi Valley."
    },
    {
      from: LOC.SimiValley, to: LOC.SimiGrid,
      time: 0, dist: 3, mediums: ["land"],
      desc: "Suburban grid avenue connecting through central Simi Valley."
    },
    {
      from: LOC.SimiValley, to: LOC.HiveApexDungeon,
      time: 1, dist: 14, mediums: ["land"],
      desc: "Restricted DMHA mountain access trail leading to Hive Apex Rift."
    },

    // Bakersfield Regional
    {
      from: LOC.Bakersfield, to: LOC.BakersfieldSquare,
      time: 0, dist: 2, mediums: ["land"],
      desc: "Central thoroughfare leading into Bakersfield Square."
    },
    {
      from: LOC.BakersfieldSquare, to: LOC.DustyCoyote,
      time: 0, dist: 4, mediums: ["land"],
      desc: "Highway 99 frontage road leading out to The Dusty Coyote Diner."
    },
    {
      from: LOC.BakersfieldSquare, to: LOC.RhodesFarm,
      time: 1, dist: 12, mediums: ["land"],
      desc: "Rural country route through alfalfa pastures to Rhodes Farm."
    },
    {
      from: LOC.BakersfieldSquare, to: LOC.ParcoRoulotte,
      time: 0, dist: 5, mediums: ["land"],
      desc: "North avenue leading across the river into Parco Roulotte di Oildale."
    },
    {
      from: LOC.BakersfieldSquare, to: LOC.CampiPetroliferi,
      time: 1, dist: 8, mediums: ["land"],
      desc: "Industrial oil field service road into Kern River Oilfields."
    },
    {
      from: LOC.BakersfieldSquare, to: LOC.KernRiverCanyon,
      time: 1, dist: 18, mediums: ["land"],
      desc: "Winding canyon highway climbing along the Kern River Gorge."
    },
    {
      from: LOC.BakersfieldSquare, to: LOC.MercatoContadino,
      time: 0, dist: 3, mediums: ["land"],
      desc: "Boulevard leading to the weekly open-air Farmer's Market."
    },

    // Los Angeles District
    {
      from: LOC.LosAngeles, to: LOC.PershingSquare,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Downtown transit corridor opening into Pershing Square."
    },
    {
      from: LOC.PershingSquare, to: LOC.Hollywood,
      time: 1, dist: 7, mediums: ["land"],
      desc: "Hollywood Boulevard heading northwest through the entertainment district."
    },
    {
      from: LOC.Hollywood, to: LOC.BeverlyHills,
      time: 0, dist: 5, mediums: ["land"],
      desc: "Sunset Boulevard corridor curving west into Beverly Hills."
    },
    {
      from: LOC.BeverlyHills, to: LOC.RorysEstate,
      time: 0, dist: 2, mediums: ["land"],
      desc: "Guarded private canyon driveway leading into Rory's secluded estate."
    },
    {
      from: LOC.PershingSquare, to: LOC.SkidRow,
      time: 0, dist: 1, mediums: ["land"],
      desc: "Eastern downtown street crossing over into Skid Row."
    },
    {
      from: LOC.PershingSquare, to: LOC.OsservatorioGriffith,
      time: 1, dist: 8, mediums: ["land"],
      desc: "Scenic hillside drive climbing Mount Hollywood to Griffith Observatory."
    },
    {
      from: LOC.PershingSquare, to: LOC.FortMacArthur,
      time: 1, dist: 25, mediums: ["land"],
      desc: "Harbor Freeway heading south all the way to Fort MacArthur."
    },
    {
      from: LOC.FortMacArthur, to: LOC.Molo42,
      time: 0, dist: 3, mediums: ["land"],
      desc: "Port access road connecting naval grounds to Pier 42."
    },
    {
      from: LOC.PershingSquare, to: LOC.NeonMirage,
      time: 0, dist: 4, mediums: ["land"],
      desc: "Neon-lit boulevard avenue leading to The Neon Mirage."
    },

    // Camp Mystic
    {
      from: LOC.BlackwoodCity, to: LOC.CampMystic,
      time: 1, dist: 28, mediums: ["land"],
      desc: "Scenic mountain road climbing from Blackwood foothills into Camp Mystic."
    },
    {
      from: LOC.Solarton, to: LOC.CampMystic,
      time: 1, dist: 32, mediums: ["land"],
      desc: "Pine ridge highway heading north from Solarton into Camp Mystic valley."
    },

    // Voidspace / DDM
    {
      from: LOC.DeadDogMotel, to: LOC.DDMVoidspace,
      time: 0, dist: 0, mediums: ["omniversal"],
      desc: "Liminal tear through motel Room 00 into Voidspace.",
      hidden: true
    },
    {
      from: LOC.DDMVoidspace, to: LOC.DDMHQ,
      time: 0, dist: 1, mediums: ["omniversal"],
      desc: "Shifting non-euclidean corridor connecting Voidspace threshold to DDM Headquarters."
    }
  ];

  const addedRoutes = [];
  newRoutesDefs.forEach(nr => {
    const key = `${nr.from}<->${nr.to}`;
    if (!existingPairSet.has(key)) {
      addedRoutes.push({
        id: genUuid(),
        from_location_id: nr.from,
        to_location_id: nr.to,
        bidirectional: true,
        travel_time: nr.time,
        distance: nr.dist,
        required_mediums: nr.mediums,
        description: nr.desc,
        hidden: nr.hidden || false
      });
      existingPairSet.add(key);
    }
  });

  const finalRoutes = [...fixedExistingRoutes, ...addedRoutes];
  console.log(`Initial routes: ${currentRoutes.length}`);
  console.log(`Added new routes: ${addedRoutes.length}`);
  console.log(`Total final routes: ${finalRoutes.length}`);

  // 3. Update world via PUT
  console.log('Sending PUT update to World API...');
  const putPayload = {
    free_travel: false,
    travel_routes: finalRoutes
  };

  const putRes = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(putPayload)
  });

  if (!putRes.ok) {
    throw new Error('PUT failed: ' + putRes.status);
  }
  console.log('PUT succeeded (status 200).');

  // 4. Fresh GET verification
  console.log('Verifying with fresh GET...');
  const verifyRes = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const verified = await verifyRes.json();
  console.log('Verified free_travel:', verified.free_travel);
  console.log('Verified travel_routes count:', verified.travel_routes?.length);

  const missingDist = verified.travel_routes.filter(r => r.distance == null);
  console.log('Routes with missing distance:', missingDist.length);

  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/updated_travel_routes.json', JSON.stringify(verified.travel_routes, null, 2));
  console.log('Saved updated routes snapshot.');
}

main().catch(console.error);

async function searchSpeciesSchema() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  // Find where species is used in RPG build: "Choose your species"
  let idx = text.indexOf('Choose your species');
  if (idx !== -1) {
    console.log('--- Context of "Choose your species" ---');
    console.log(text.slice(Math.max(0, idx - 200), Math.min(text.length, idx + 1000)));
  }

  // Find where occupation is used: "Choose your occupation"
  let idx2 = text.indexOf('Choose your occupation');
  if (idx2 !== -1) {
    console.log('\n--- Context of "Choose your occupation" ---');
    console.log(text.slice(Math.max(0, idx2 - 200), Math.min(text.length, idx2 + 1000)));
  }
}

searchSpeciesSchema().catch(console.error);

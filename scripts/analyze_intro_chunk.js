async function analyzeIntroChunk() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const res = await fetch(url);
  const text = await res.text();
  
  // Find definitions of lW and lq
  const idx = text.indexOf('lW(e.type)');
  console.log('--- Context of lW(e.type) ---');
  console.log(text.slice(Math.max(0, idx - 500), Math.min(text.length, idx + 1000)));

  // Find where lW is defined
  const defLW = text.indexOf('function lW(') !== -1 ? text.indexOf('function lW(') : text.indexOf('lW=');
  console.log('\n--- Definition of lW ---');
  console.log(text.slice(Math.max(0, defLW - 100), Math.min(text.length, defLW + 400)));

  // Find where page rendering happens: switch (page.type) or if (page.type === ...)
  // Search for "character" or "rpg_build" or "fieldId"
  let rIdx = text.indexOf('.fieldId');
  while (rIdx !== -1) {
    console.log('\n--- FieldId usage ---');
    console.log(text.slice(Math.max(0, rIdx - 200), Math.min(text.length, rIdx + 400)));
    rIdx = text.indexOf('.fieldId', rIdx + 10);
  }
}

analyzeIntroChunk().catch(console.error);

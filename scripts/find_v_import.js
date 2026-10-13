async function findVImport() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/35454-a8397a1df44fbba7.js';
  const text = await (await fetch(url)).text();
  
  let idx = text.indexOf('.Nf)(');
  console.log('--- Context of .Nf)( ---');
  console.log(text.slice(Math.max(0, idx - 100), Math.min(text.length, idx + 100)));
  
  // Find where v is imported
  let idx2 = text.indexOf('v=a(');
  if (idx2 === -1) idx2 = text.indexOf('v = a(');
  console.log('--- v=a( ---');
  console.log(text.slice(Math.max(0, idx2 - 50), Math.min(text.length, idx2 + 100)));
}

findVImport().catch(console.error);

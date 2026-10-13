const fs = require('fs');

async function printMoreHelpers() {
  const res = await fetch('https://app.wyvern.chat/_next/static/chunks/88676-11ecc49c3bd7ce22.js');
  const text = await res.text();
  const idx = text.indexOf('v=async function(t){');
  console.log(text.slice(idx, idx + 2000));
}

printMoreHelpers();

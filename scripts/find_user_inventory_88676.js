const fs = require('fs');

async function findUserInventoryIn88676() {
  const res = await fetch('https://app.wyvern.chat/_next/static/chunks/88676-11ecc49c3bd7ce22.js');
  const text = await res.text();
  const idx = text.indexOf('userInventory');
  console.log('userInventory index in 88676:', idx);
  if (idx !== -1) {
    console.log(text.slice(idx - 50, idx + 600));
  }
}

findUserInventoryIn88676();

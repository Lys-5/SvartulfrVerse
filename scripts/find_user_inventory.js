const fs = require('fs');

async function findUserInventory() {
  const res = await fetch('https://app.wyvern.chat/_next/static/chunks/61929-6b204a5b5f89b57b.js');
  const text = await res.text();
  const idx = text.indexOf('userInventory');
  console.log('userInventory index:', idx);
  // Look backwards for where userInventory is defined
  const defIdx = text.lastIndexOf('userInventory:', idx);
  if (defIdx !== -1) {
    console.log(text.slice(defIdx, defIdx + 600));
  } else {
    console.log(text.slice(idx - 100, idx + 200));
  }
}

findUserInventory();

const fs = require('fs');

async function findUnderImport() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-9837bb651bfa2afb.js';
  const res = await fetch(url);
  const text = await res.text();
  
  const idx = text.indexOf('eb=(0,_.dX)');
  // Search backward for '_='
  let searchPos = idx;
  while (searchPos > 0) {
    const underIdx = text.lastIndexOf('_=', searchPos);
    if (underIdx === -1) break;
    console.log('Found _= at', underIdx);
    console.log(text.slice(underIdx - 20, underIdx + 80));
    searchPos = underIdx - 1;
    break;
  }
}

findUnderImport();

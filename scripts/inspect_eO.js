const fs = require('fs');

async function findUnderscoreDecl() {
  const r1 = await fetch('https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-9837bb651bfa2afb.js');
  const txt1 = await r1.text();
  const idx = txt1.indexOf('function eO(e){');
  const slice = txt1.substring(0, idx);
  // Find where `_=a(...)` occurs
  const matches = [...slice.matchAll(/\b_=(?:a\([0-9]+\)|[a-zA-Z0-9_\$]+)/g)];
  for (const m of matches.slice(-10)) {
    console.log(m[0]);
    const pos = m.index;
    console.log(slice.substring(Math.max(0, pos - 50), Math.min(slice.length, pos + 100)));
  }
}

findUnderscoreDecl();

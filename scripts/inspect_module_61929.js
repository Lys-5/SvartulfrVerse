const fs = require('fs');

async function findWV() {
  const res = await fetch('https://app.wyvern.chat/_next/static/chunks/61929-6b204a5b5f89b57b.js');
  const text = await res.text();
  const startIdx = text.indexOf('61929:function');
  const modText = text.slice(startIdx);
  
  // Find W = and v =
  const m1 = modText.match(/\bW\s*=\s*(?:function|\([^)]*\)\s*=>)/);
  if (m1) {
    console.log('--- W ---');
    console.log(modText.slice(m1.index, m1.index + 1200));
  }
  const m2 = modText.match(/\bv\s*=\s*(?:function|\([^)]*\)\s*=>)/);
  if (m2) {
    console.log('--- v ---');
    console.log(modText.slice(m2.index, m2.index + 800));
  }
}

findWV();

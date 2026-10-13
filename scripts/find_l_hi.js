const fs = require('fs');

async function findLHiImport() {
  const res = await fetch('https://app.wyvern.chat/_next/static/chunks/61929-6b204a5b5f89b57b.js');
  const text = await res.text();
  const startIdx = text.indexOf('61929:function');
  const modText = text.slice(startIdx);
  // find 'l=t(' or 'l=a(' or 'var l=t('
  const matches = modText.match(/[a-zA-Z0-9_$]+=t\(\d+\)/g) || [];
  console.log('Matches:', matches.slice(0, 10));
}

findLHiImport();

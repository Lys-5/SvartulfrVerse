const fs = require('fs');

async function find61929Exports() {
  const res = await fetch('https://app.wyvern.chat/_next/static/chunks/61929-6b204a5b5f89b57b.js');
  const text = await res.text();
  const startIdx = text.indexOf('61929:function');
  const sub = text.slice(startIdx);
  const dXIdx = sub.indexOf('dX:function');
  console.log('dX export:');
  console.log(sub.slice(dXIdx, dXIdx + 50));
  
  // The var returned by dX is y!
  // Let's find all occurrences of 'let y=' or 'var y=' or 'function y' in 61929
  // Wait, let's see how many modules are in 61929-6b204a5b5f89b57b.js
  const moduleMatches = [...text.matchAll(/(\d+):function/g)].map(m => m[1]);
  console.log('Modules in chunk:', moduleMatches);
}

find61929Exports();

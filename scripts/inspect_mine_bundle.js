const fs = require('fs');

async function findLorebookTab() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-9837bb651bfa2afb.js';
  const res = await fetch(url);
  const text = await res.text();
  
  const regex = /"lorebooks"/g;
  let m;
  let count = 0;
  while ((m = regex.exec(text)) !== null && count < 5) {
    console.log('--- lorebooks match at', m.index, '---');
    console.log(text.slice(Math.max(0, m.index - 200), m.index + 300));
    count++;
  }
}
findLorebookTab();

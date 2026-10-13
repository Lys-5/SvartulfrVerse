const fs = require('fs');

async function inspectModule61929FunctionY() {
  const res = await fetch('https://app.wyvern.chat/_next/static/chunks/61929-6b204a5b5f89b57b.js');
  const text = await res.text();
  const startIdx = text.indexOf('61929:function');
  const modText = text.slice(startIdx);
  const idx = modText.indexOf('y=function(e)');
  console.log(modText.slice(idx, idx + 800));
}

inspectModule61929FunctionY();

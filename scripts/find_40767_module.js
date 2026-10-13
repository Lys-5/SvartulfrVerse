const fs = require('fs');

async function findModule() {
  const r = await fetch('https://app.wyvern.chat/mine');
  const html = await r.text();
  const allScripts = html.split('src="').slice(1).map(s => s.split('"')[0]);
  
  for (const s of allScripts) {
    if (!s.endsWith('.js')) continue;
    const res = await fetch('https://app.wyvern.chat' + s);
    const text = await res.text();
    if (text.includes('40767:function')) {
      console.log('Found 40767 in:', s);
      const idx = text.indexOf('40767:function');
      console.log(text.slice(idx, idx + 1000));
      break;
    }
  }
}

findModule();

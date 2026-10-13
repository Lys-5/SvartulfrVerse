const fs = require('fs');

async function find40767() {
  const r = await fetch('https://app.wyvern.chat/mine');
  const html = await r.text();
  const allScripts = html.split('src="').slice(1).map(s => s.split('"')[0]);
  const s40767 = allScripts.find(s => s.includes('40767'));
  console.log('40767 script:', s40767);
  if (s40767) {
    const res = await fetch('https://app.wyvern.chat' + s40767);
    const text = await res.text();
    const idx = text.indexOf('dX:');
    console.log('dX index:', idx);
    if (idx !== -1) {
      console.log(text.slice(idx, idx + 500));
      // find function or variable returned
      const sub = text.slice(idx);
      const varName = sub.split('return ')[1].split('}')[0].trim();
      console.log('Var name:', varName);
      // search for varName definition
      const defIdx = text.indexOf(varName + '=');
      console.log('defIdx:', defIdx);
      console.log(text.slice(defIdx, defIdx + 600));
    }
  }
}

find40767();

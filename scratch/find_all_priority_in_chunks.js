const fs = require('fs');

async function run() {
  const r = await fetch('https://app.wyvern.chat/mine');
  const html = await r.text();
  const scriptRegex = /src="([^"]+\.js)"/g;
  let match;
  const scripts = [];
  while ((match = scriptRegex.exec(html)) !== null) {
    scripts.push(match[1]);
  }

  for (const s of scripts) {
    const url = s.startsWith('http') ? s : 'https://app.wyvern.chat' + s;
    try {
      const res = await fetch(url);
      if (!res.ok) continue;
      const txt = await res.text();
      let idx = 0;
      while ((idx = txt.indexOf('priority', idx)) !== -1) {
        // Grab context
        const ctx = txt.slice(Math.max(0, idx - 50), Math.min(txt.length, idx + 80));
        // Check if it looks like an object key or zod field or api payload
        if (ctx.includes('priority:') || ctx.includes('"priority"') || ctx.includes("'priority'")) {
          // ignore Next Image priority
          if (!ctx.includes('priority:!0') && !ctx.includes('priority:!1') && !ctx.includes('priority:true') && !ctx.includes('priority:false')) {
            console.log(`[${s.split('/').pop()}] at ${idx}: ${ctx.replace(/\n/g, ' ')}`);
          }
        }
        idx += 8;
      }
    } catch (e) {}
  }
}

run();

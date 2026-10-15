const fs = require('fs');

(async () => {
  const html = await (await fetch('https://app.wyvern.chat/')).text();
  const chunks = [...new Set([...html.matchAll(/\/static\/chunks\/([a-zA-Z0-9_\.-]+\.js)/g)].map(m => m[1]))];
  for (const c of chunks) {
    try {
      const res = await fetch('https://app.wyvern.chat/_next/static/chunks/' + c);
      if (res.ok) {
        const text = await res.text();
        if (text.includes('priority')) {
          // Look for zod schema patterns: .object({ ... priority: or priority: e.number() or z.number()
          const zodMatches = [...text.matchAll(/.{0,60}priority\s*:\s*[a-zA-Z0-9_\$]+\.(?:number|string|int|coerce|optional|default)[^,}]{0,60}/g)].map(m => m[0]);
          if (zodMatches.length > 0) {
            console.log(`Zod matches in ${c}:`);
            zodMatches.forEach(m => console.log('  ', m));
          }
        }
      }
    } catch(e) {}
  }
})();

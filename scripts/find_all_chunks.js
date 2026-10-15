const fs = require('fs');

async function main() {
  const res = await fetch('https://app.wyvern.chat');
  const html = await res.text();
  const buildIdMatch = html.match(/"buildId":"([^"]+)"/);
  const buildId = buildIdMatch ? buildIdMatch[1] : null;
  console.log('Build ID:', buildId);

  let manifestChunks = [];
  if (buildId) {
    const manRes = await fetch(`https://app.wyvern.chat/_next/static/${buildId}/_buildManifest.js`);
    const manText = await manRes.text();
    const chunkMatches = [...manText.matchAll(/"static\/chunks\/([^"]+)"/g)].map(m => m[1]);
    manifestChunks = chunkMatches;
  }
  console.log('Manifest chunks count:', manifestChunks.length);

  for (const chunk of manifestChunks) {
    try {
      const cRes = await fetch(`https://app.wyvern.chat/_next/static/chunks/${chunk}`);
      const text = await cRes.text();
      if (text.includes('Distance (flavor)')) {
        console.log('FOUND "Distance (flavor)" in:', chunk);
        const p = text.indexOf('Distance (flavor)');
        console.log(text.slice(Math.max(0, p - 300), p + 300));
        return;
      }
    } catch (e) {}
  }
  console.log('Done scanning manifest chunks.');
}

main().catch(console.error);

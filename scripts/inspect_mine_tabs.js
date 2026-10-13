const fs = require('fs');

async function inspectMine() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  // Test endpoints related to /mine
  const candidateEndpoints = [
    '/api/characters/mine',
    '/api/characters',
    '/api/lorebooks/mine',
    '/api/lorebooks',
    '/api/user-personas',
    '/api/story-engines',
    '/api/story-engines/mine',
    '/api/presets',
    '/api/presets/mine',
    '/api/prompts',
    '/api/prompts/mine',
    '/api/worlds/mine',
    '/api/worlds',
    '/api/users/me',
    '/api/user/characters',
    '/api/user/lorebooks'
  ];

  for (const ep of candidateEndpoints) {
    try {
      const res = await fetch('https://app.wyvern.chat' + ep, {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      console.log(ep.padEnd(30), 'Status:', res.status);
      if (res.ok) {
        const data = await res.json();
        const count = Array.isArray(data) ? data.length : (data.items ? data.items.length : (typeof data === 'object' ? Object.keys(data).length : 'ok'));
        console.log('   Data summary:', count, Array.isArray(data) ? data.slice(0, 3).map(x => x.name || x.display_name || x.title || x.id) : '');
      }
    } catch (e) {
      console.log(ep.padEnd(30), 'Error:', e.message);
    }
  }
}

inspectMine();

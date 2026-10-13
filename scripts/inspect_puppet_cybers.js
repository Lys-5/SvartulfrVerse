const fs = require('fs');

function inspectLb(name, p) {
  const d = JSON.parse(fs.readFileSync(p, 'utf8'));
  console.log('=== ' + name + ' (' + d.length + ' entries) ===');
  d.forEach((e, idx) => {
    const keys = Array.isArray(e.keys) ? e.keys.join(', ') : '';
    const title = (e.name || e.comment || (e.content || '').split('\n')[0]).replace(/^#+\s*/, '').slice(0, 60);
    console.log((idx + 1) + '. [' + keys.slice(0, 30) + '] ' + title);
  });
}

inspectLb('Puppet Master', 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/lb_puppet_master.json');
console.log('----------------------------------------------------');
inspectLb('Cybers', 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/lb_cybers.json');

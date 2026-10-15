const fs = require('fs');
const files = fs.readdirSync('scripts');
files.forEach(f => {
  if (f.endsWith('.js') || f.endsWith('.py')) {
    const text = fs.readFileSync('scripts/' + f, 'utf8');
    if (text.includes('scripts') || text.includes('lua') || text.includes('buildPrompt')) {
      console.log('Match in scripts/' + f);
    }
  }
});

const fs = require('fs');

const filesToProcess = [
    'd:\\Progetti\\database\\templates\\universal_lorebook_template.md',
    'd:\\Progetti\\database\\docs\\prompt.md'
];

filesToProcess.forEach(file => {
    if (!fs.existsSync(file)) return;
    let content = fs.readFileSync(file, 'utf8');

    // Replace L3_ENTRIES
    content = content.replace(/L3_ENTRIES/g, 'C_ENTRIES');
    
    // Replace au: with world:
    content = content.replace(/\bau\s*:/g, 'world:');
    
    // Replace e.au with e.world
    content = content.replace(/\be\.au\b/g, 'e.world');
    
    // Replace var au = with var w = 
    content = content.replace(/var au =/g, 'var w =');
    content = content.replace(/indexOf\(au\)/g, 'indexOf(w)');

    // In templates, references like "L2 Scenario Lorebook" -> "World Lorebook (W_)"
    content = content.replace(/L2 SCENARIO LOREBOOK/g, 'WORLD LOREBOOK');
    content = content.replace(/L2 Scenario Lorebook/g, 'World Lorebook');
    content = content.replace(/L2 Scenario Lorebooks/g, 'World Lorebooks');
    content = content.replace(/L3 Character Lorebook/g, 'Character Lorebook');
    content = content.replace(/L3 Character Lorebooks/g, 'Character Lorebooks');
    content = content.replace(/L3 Lorebooks/g, 'Character Lorebooks');
    content = content.replace(/L3 Lorebook/g, 'Character Lorebook');
    
    // In prompt.md:
    content = content.replace(/\*\*L1\*\*/g, '**En_Core**');
    content = content.replace(/\*\*L2\*\*/g, '**W_ (World)**');
    content = content.replace(/\*\*L3\*\*/g, '**C_ (Character)**');

    fs.writeFileSync(file, content, 'utf8');
    console.log('Updated ' + file);
});

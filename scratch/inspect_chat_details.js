const fs = require('fs');

const log = JSON.parse(fs.readFileSync('scratch/bad_chat_log.json', 'utf8'));

console.log('current_location_id:', log.current_location_id);
console.log('world_party:', JSON.stringify(log.world_party, null, 2));
console.log('memory:', JSON.stringify(log.memory, null, 2));
console.log('object_data:', JSON.stringify(log.object_data, null, 2));
console.log('world_data keys:', Object.keys(log.world_data || {}));
console.log('info_board_override:', JSON.stringify(log.info_board_override, null, 2));

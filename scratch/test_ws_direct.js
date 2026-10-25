const http = require('http');

console.log('Testing raw HTTP upgrade to WebSocket...');

const req = http.request({
  hostname: '127.0.0.1',
  port: 9222,
  path: '/devtools/browser/c4078182-22f9-4a63-ae69-a5292e74571b',
  headers: {
    'Connection': 'Upgrade',
    'Upgrade': 'websocket',
    'Sec-WebSocket-Version': '13',
    'Sec-WebSocket-Key': 'dGhlIHNhbXBsZSBub25jZQ=='
  }
});

req.on('response', (res) => {
  console.log('Got standard HTTP response:', res.statusCode, res.headers);
  process.exit(0);
});

req.on('upgrade', (res, socket, upgradeHead) => {
  console.log('Successfully upgraded to WebSocket!', res.statusCode);
  socket.end();
  process.exit(0);
});

req.on('error', (err) => {
  console.error('Request error:', err);
  process.exit(1);
});

req.end();

setTimeout(() => {
  console.log('Timeout waiting for upgrade response!');
  process.exit(1);
}, 5000);

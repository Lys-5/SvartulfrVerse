const fs = require('fs');

async function refreshToken() {
  const ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw';
  const rtPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/refresh_token.txt';
  const wtPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';

  const rt = fs.readFileSync(rtPath, 'utf8').trim();
  const res = await fetch('https://securetoken.googleapis.com/v1/token?key=' + ak, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      grant_type: 'refresh_token',
      refresh_token: rt
    })
  });
  const data = await res.json();
  if (data.id_token) {
    fs.writeFileSync(wtPath, data.id_token, 'utf8');
    console.log('Firebase ID token refreshed successfully!');
    return data.id_token;
  } else {
    throw new Error('Refresh failed: ' + JSON.stringify(data));
  }
}

refreshToken().catch(console.error);

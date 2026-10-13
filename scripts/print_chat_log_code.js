async function printCreateWorldChatLog() {
  const url = 'https://app.wyvern.chat/_next/static/chunks/24224-6accf84b4f65cb82.js';
  const text = await (await fetch(url)).text();
  console.log(text.slice(144150, 145200));
}

printCreateWorldChatLog().catch(console.error);

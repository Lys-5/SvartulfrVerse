const fs = require('fs');

async function updateAndPublish() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json'
  };

  // 1. Fetch current engine
  const getRes = await fetch('https://app.wyvern.chat/api/story-engines/engine_HCTPXhL8xr89wUY9r9dYU', { headers });
  const eng = await getRes.json();
  const def = eng.definition;

  // 2. Component code with full interactive sub-views (Telegram chat + SUCCbook feed)
  const smartphoneCode = `export default function Panel({ engine }) {
  const [screen, setScreen] = useState('home'); // 'home' | 'telegram' | 'succbook'

  const moonPhase = String(engine.values.moon_phase || 'Ultimo Quarto Calante');
  const isFullMoon = Boolean(engine.values.moon_full_active);
  const isNight = Boolean(engine.values.night_active);
  const lseStatus = String(engine.values.lse_biology_status || 'Dormant');
  const daysLeft = Number(engine.values.lse_cycle_days_left ?? 20);
  const suppressors = Number(engine.values.scent_suppressors_count ?? 3);
  const packChat = Number(engine.values.pack_chat_unread ?? 3);
  const succPosts = Number(engine.values.succbook_unread_posts ?? 5);
  const repScore = Number(engine.values.pack_reputation ?? 25);
  const repLabel = repScore >= 80 ? 'Riconosciuto' : repScore >= 50 ? 'Rispettato' : 'Matricola';
  const riftAlert = String(engine.values.rift_threat_level || 'Classe 1 - Stabile');

  const [packUnread, setPackUnread] = useState(packChat);
  const [succUnread, setSuccUnread] = useState(succPosts);
  const [suppressorDoses, setSuppressorDoses] = useState(suppressors);
  const [inputMsg, setInputMsg] = useState('');

  const [chatMessages, setChatMessages] = useState([
    {
      id: 1,
      sender: 'Papà (Erik)',
      role: 'Prime Alpha',
      color: 'text-amber-400',
      badgeColor: 'bg-amber-950 text-amber-300 border border-amber-800',
      text: 'Ragazzi, siete arrivati al campus? Kaladin ha predisposto la scorta discreta attorno all\\'ingresso est. Niente sciocchezze e prendete i soppressori.',
      time: '08:02'
    },
    {
      id: 2,
      sender: 'Noah',
      role: 'Beta / PR',
      color: 'text-sky-400',
      badgeColor: 'bg-sky-950 text-sky-300 border border-sky-800',
      text: 'Tranquillo Boss, ho già avvistato tre matricole perse al Quad. Io sono al banchetto SUCC. Se Alyssa ritarda è colpa delle scarpe 💅',
      time: '08:05'
    },
    {
      id: 3,
      sender: 'Jasper',
      role: 'Twin / Shield',
      color: 'text-emerald-400',
      badgeColor: 'bg-emerald-950 text-emerald-300 border border-emerald-800',
      text: 'Siamo arrivati. Ho il portatile e le cuffie. Sto accompagnando Alyssa verso la segreteria del dipartimento di Botanica. Noah piantala.',
      time: '08:08'
    },
    {
      id: 4,
      sender: 'Malachia',
      role: 'Apex Predator',
      color: 'text-rose-400',
      badgeColor: 'bg-rose-950 text-rose-300 border border-rose-800',
      text: 'Ho finito i pesi al campo dei Bulls. Chiunque si avvicini con cattive intenzioni se la vede con me. Mandatemi la posizione.',
      time: '08:11'
    }
  ]);

  const notifications = [
    {
      id: 1,
      tag: 'SUCC ACADEMIC',
      tagColor: 'bg-blue-950 text-sky-300 border border-sky-800',
      title: 'Sessione Esami Autunno Aperta',
      desc: 'Registrazione corsi matricole e pre-med disponibile nel portale studenti.',
      time: '15m fa'
    },
    {
      id: 2,
      tag: 'BULLS ATHLETICS',
      tagColor: 'bg-amber-950 text-amber-300 border border-amber-800',
      title: 'Tryout Stagione Rugby & Football',
      desc: 'Allenamenti aperti al campo centrale ore 17:30. Alpha e Beta prioritari.',
      time: '42m fa'
    },
    {
      id: 3,
      tag: 'DJ FREQUENCY',
      tagColor: 'bg-purple-950 text-purple-300 border border-purple-800',
      title: 'Secret Warehouse Rave Announce',
      desc: 'Underground party venerdì notte nei magazzini industriali di Solarton.',
      time: '1h fa'
    },
    {
      id: 4,
      tag: 'CLINICA HSK',
      tagColor: 'bg-emerald-950 text-emerald-300 border border-emerald-800',
      title: 'Turni Volontariato Botanica & Pronto Soccorso',
      desc: 'Bando di supporto medico accademico per matricole con doti rigenerative.',
      time: '2h fa'
    },
    {
      id: 5,
      tag: 'SEVEN HILLS SECURITY',
      tagColor: 'bg-neutral-900 text-zinc-300 border border-zinc-700',
      title: 'Rilevazione Miasma Rift Perimetro Nord',
      desc: 'Anomalia Classe 1 sotto controllo dai team di ronda. Nessun pericolo civile.',
      time: '3h fa'
    }
  ];

  const inalaSoppressore = async () => {
    if (suppressorDoses > 0) {
      setSuppressorDoses(s => Math.max(0, s - 1));
    }
    try {
      await engine.runCommand('cmd_use_suppressor', {});
    } catch (e) {}
  };

  const handleSendMessage = () => {
    if (!inputMsg.trim()) return;
    const newEntry = {
      id: Date.now(),
      sender: 'Tu',
      role: 'Me',
      color: 'text-amber-300',
      badgeColor: 'bg-amber-950 text-amber-200 border border-amber-800',
      text: inputMsg.trim(),
      time: 'Adesso'
    };
    setChatMessages(prev => [...prev, newEntry]);
    setInputMsg('');
  };

  // VISTA TELEGRAM DOUGLAS
  if (screen === 'telegram') {
    return (
      <div className="space-y-3 font-sans text-xs select-none">
        <Card className="bg-black border-zinc-800 text-zinc-300 shadow-xl overflow-hidden">
          <CardHeader className="px-4 py-3 bg-neutral-900 border-b border-zinc-800 flex flex-row items-center justify-between">
            <div className="flex items-center gap-2">
              <Button
                size="sm"
                variant="ghost"
                className="h-7 px-2 text-xs text-sky-400 hover:text-sky-300 hover:bg-neutral-800 -ml-1 flex items-center gap-1"
                onClick={() => setScreen('home')}
              >
                <span>←</span>
                <span>Dashboard</span>
              </Button>
            </div>
            <div className="text-right">
              <p className="font-bold text-xs text-zinc-100">Famiglia Douglas</p>
              <p className="text-[10px] text-emerald-400">● 5 membri · 4 online</p>
            </div>
          </CardHeader>

          <CardContent className="p-4 space-y-3">
            <div className="space-y-2.5 max-h-[340px] overflow-y-auto pr-1">
              {chatMessages.map(msg => (
                <div key={msg.id} className="p-3 bg-neutral-900/95 rounded-lg border border-zinc-800/80 space-y-1">
                  <div className="flex items-center justify-between">
                    <span className={'font-bold text-xs ' + msg.color}>{msg.sender}</span>
                    <div className="flex items-center gap-1.5">
                      <span className={'text-[9px] px-1.5 py-0.2 rounded font-semibold ' + msg.badgeColor}>{msg.role}</span>
                      <span className="text-[10px] text-zinc-500 font-mono">{msg.time}</span>
                    </div>
                  </div>
                  <p className="text-xs text-zinc-200 leading-relaxed pt-0.5">{msg.text}</p>
                </div>
              ))}
            </div>

            {/* Input bar */}
            <div className="pt-2 border-t border-zinc-800 flex gap-2">
              <input
                type="text"
                value={inputMsg}
                placeholder="Scrivi al gruppo di famiglia..."
                onChange={(e) => setInputMsg(e.target.value)}
                onKeyDown={(e) => { if (e.key === 'Enter') handleSendMessage(); }}
                className="flex-1 bg-neutral-900 text-zinc-200 placeholder-zinc-500 text-xs px-3 py-1.5 rounded-lg border border-zinc-800 focus:outline-none focus:border-sky-500"
              />
              <Button
                size="sm"
                className="bg-sky-600 hover:bg-sky-500 text-white font-semibold text-xs px-3 h-8"
                onClick={handleSendMessage}
              >
                Invia
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    );
  }

  // VISTA SUCCBOOK FEED
  if (screen === 'succbook') {
    return (
      <div className="space-y-3 font-sans text-xs select-none">
        <Card className="bg-black border-zinc-800 text-zinc-300 shadow-xl overflow-hidden">
          <CardHeader className="px-4 py-3 bg-neutral-900 border-b border-zinc-800 flex flex-row items-center justify-between">
            <Button
              size="sm"
              variant="ghost"
              className="h-7 px-2 text-xs text-yellow-400 hover:text-yellow-300 hover:bg-neutral-800 -ml-1 flex items-center gap-1"
              onClick={() => setScreen('home')}
            >
              <span>←</span>
              <span>Dashboard</span>
            </Button>
            <div className="text-right">
              <p className="font-bold text-xs text-zinc-100">SUCCbook Feed</p>
              <p className="text-[10px] text-zinc-400">Campus Solarton · Notifiche</p>
            </div>
          </CardHeader>

          <CardContent className="p-4 space-y-3">
            <div className="flex items-center justify-between pb-1">
              <span className="text-[11px] text-zinc-400">Notifiche recenti campus</span>
              <Button
                size="sm"
                variant="ghost"
                className="h-6 text-[10px] text-zinc-400 hover:text-zinc-200 px-1.5"
                onClick={() => setSuccUnread(0)}
              >
                Segna tutte come lette
              </Button>
            </div>

            <div className="space-y-2.5 max-h-[340px] overflow-y-auto pr-1">
              {notifications.map(item => (
                <div key={item.id} className="p-3 bg-neutral-900/95 rounded-lg border border-zinc-800/80 space-y-1">
                  <div className="flex items-center justify-between">
                    <span className={'text-[9px] px-1.5 py-0.2 rounded font-semibold ' + item.tagColor}>
                      {item.tag}
                    </span>
                    <span className="text-[10px] text-zinc-500 font-mono">{item.time}</span>
                  </div>
                  <p className="font-semibold text-xs text-zinc-100 pt-0.5">{item.title}</p>
                  <p className="text-xs text-zinc-300 leading-relaxed">{item.desc}</p>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    );
  }

  // VISTA HOME (DASHBOARD SMARTPHONE)
  return (
    <div className="space-y-3 font-sans text-xs select-none">
      <Card className="bg-black border-zinc-800 text-zinc-300 shadow-xl overflow-hidden">
        <CardHeader className="px-4 py-3 bg-neutral-900 border-b border-zinc-800 flex flex-row items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 inline-block animate-pulse"></span>
            <span className="font-bold text-sm text-zinc-100 tracking-wide">Svartúlfr OS</span>
          </div>
          <Badge className="text-[10px] bg-blue-950 text-sky-300 border-0 font-mono px-2 py-0.5">5G · DOUGLAS NET</Badge>
        </CardHeader>
        
        <CardContent className="p-4 space-y-3">
          <div className="bg-neutral-900 rounded-lg p-3.5 border-0 flex items-center justify-between">
            <div className="space-y-1">
              <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Ciclo Lunare & Orario</p>
              <p className="font-semibold text-xs text-zinc-200">{moonPhase} <span className="text-[11px] text-sky-300 font-normal">(~48% · Gemelli)</span></p>
            </div>
            <div className="flex gap-1.5 items-center">
              {isNight && (
                <Badge className="bg-blue-950 text-sky-300 border-0 text-[10px] font-semibold px-2 py-0.5">🌙 Notte</Badge>
              )}
              {isFullMoon ? (
                <Badge className="bg-yellow-400 text-black font-bold text-[10px] border-0 px-2 py-0.5">LUNA PIENA (+MGT)</Badge>
              ) : (
                <Badge className="bg-neutral-950 text-emerald-400 border border-zinc-800 text-[10px] font-medium px-2 py-0.5">Stabile</Badge>
              )}
            </div>
          </div>

          <div className="bg-neutral-900 rounded-lg p-3.5 border-0 space-y-2.5">
            <div className="flex items-center justify-between">
              <div className="space-y-1">
                <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Biologia LSE</p>
                <p className="font-semibold text-xs text-amber-300">{lseStatus}</p>
              </div>
              <Badge className="bg-yellow-900 text-amber-200 border-0 text-[10px] font-medium px-2 py-0.5">~{daysLeft} gg al picco</Badge>
            </div>
            <div className="flex items-center justify-between pt-2 border-t border-zinc-800 text-[11px]">
              <span className="text-zinc-400">Soppressori Odore: <strong className="text-amber-300 font-bold text-xs">{suppressorDoses}</strong> dosi</span>
              <Button size="sm" variant="secondary" className="h-7 px-3 text-xs bg-zinc-800 hover:bg-zinc-700 text-zinc-200 border-0" onClick={inalaSoppressore}>Inala Dose</Button>
            </div>
          </div>

          {/* Griglia interattiva con pulsanti cliccabili */}
          <div className="grid grid-cols-2 gap-2.5">
            <div
              onClick={() => {
                setPackUnread(0);
                setScreen('telegram');
              }}
              className="bg-neutral-900 hover:bg-neutral-800 cursor-pointer transition-all active:scale-[0.98] rounded-lg p-3 border border-zinc-800/80 hover:border-sky-700/60 space-y-1 group"
            >
              <div className="flex items-center justify-between">
                <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400 group-hover:text-sky-300 transition-colors">Telegram Douglas</p>
                <span className="text-[11px] text-zinc-500 group-hover:text-sky-400 transition-colors">→</span>
              </div>
              <p className="text-sm font-bold text-sky-300">
                {packUnread} <span className="text-[11px] font-normal text-zinc-400">nuovi msg</span>
              </p>
              <p className="text-[9px] text-sky-400/80 group-hover:text-sky-300 font-medium">Tocca per aprire chat</p>
            </div>

            <div
              onClick={() => {
                setSuccUnread(0);
                setScreen('succbook');
              }}
              className="bg-neutral-900 hover:bg-neutral-800 cursor-pointer transition-all active:scale-[0.98] rounded-lg p-3 border border-zinc-800/80 hover:border-yellow-700/60 space-y-1 group"
            >
              <div className="flex items-center justify-between">
                <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400 group-hover:text-yellow-300 transition-colors">SUCCbook Feed</p>
                <span className="text-[11px] text-zinc-500 group-hover:text-yellow-400 transition-colors">→</span>
              </div>
              <p className="text-sm font-bold text-yellow-400">
                {succUnread} <span className="text-[11px] font-normal text-zinc-400">notifiche</span>
              </p>
              <p className="text-[9px] text-yellow-400/80 group-hover:text-yellow-300 font-medium">Tocca per aprire feed</p>
            </div>
          </div>

          <div className="bg-neutral-900 rounded-lg p-3 border-0 flex items-center justify-between text-[11px]">
            <span className="text-zinc-400">Reputazione Branco:</span>
            <span className="font-semibold text-zinc-200">{repLabel} <span className="text-amber-300 font-mono text-[10px]">({repScore}/100)</span></span>
          </div>

          <div className="bg-neutral-900 rounded-lg p-3 border-0 flex items-center justify-between text-[11px]">
            <span className="text-zinc-400">Allerta Rift (Hunters):</span>
            <Badge className="bg-neutral-950 text-emerald-400 border border-zinc-800 text-[10px] font-medium px-2 py-0.5">{riftAlert}</Badge>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}`;

  // Update ui_panels[0]
  def.ui_panels[0].code = smartphoneCode;

  // 3. PUT engine definition
  const putRes = await fetch('https://app.wyvern.chat/api/story-engines/engine_HCTPXhL8xr89wUY9r9dYU', {
    method: 'PUT',
    headers,
    body: JSON.stringify({
      expected_version: eng.version,
      definition: def
    })
  });
  const putData = await putRes.json();
  console.log('PUT engine status:', putRes.status, 'New version:', putData.version);

  if (putRes.status !== 200) {
    console.error('Failed to update engine:', putData);
    return;
  }

  // 4. Publish engine so live chat gets the updated component immediately
  const pubRes = await fetch('https://app.wyvern.chat/api/story-engines/engine_HCTPXhL8xr89wUY9r9dYU/publish', {
    method: 'POST',
    headers,
    body: JSON.stringify({ expected_version: putData.version })
  });
  const pubData = await pubRes.json();
  console.log('PUBLISH status:', pubRes.status, 'Publish result:', pubData);
}

updateAndPublish().catch(console.error);

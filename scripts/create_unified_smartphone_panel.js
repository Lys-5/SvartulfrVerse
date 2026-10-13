const fs = require('fs');
const path = require('path');

async function refreshToken() {
  const ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw';
  const rt = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/refresh_token.txt', 'utf8').trim();
  const res = await fetch(`https://securetoken.googleapis.com/v1/token?key=${ak}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grant_type: 'refresh_token', refresh_token: rt })
  });
  const data = await res.json();
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', data.id_token, 'utf8');
  return data.id_token;
}

// Codice del Componente Unificato Smartphone OS
const unifiedSmartphoneCode = `export default function Panel({ engine }) {
  // Navigation: 'home' | 'telegram' | 'academics' | 'guild' | 'biotrack' | 'succbook' | 'music'
  const [activeApp, setActiveApp] = useState('home');

  // Variabili live da Wyvern Story Engine
  const moonPhase = String(engine.values.moon_phase || 'Ultimo Quarto Calante');
  const isFullMoon = Boolean(engine.values.moon_full_active);
  const isNight = Boolean(engine.values.night_active);
  const lseStatus = String(engine.values.lse_biology_status || 'Dormant');
  const daysLeft = Number(engine.values.lse_cycle_days_left ?? 20);
  const suppressorsInitial = Number(engine.values.scent_suppressors_count ?? 3);
  const packRep = Number(engine.values.pack_reputation ?? 25);
  const riftAlert = String(engine.values.rift_threat_level || 'Classe 1 - Stabile');

  // Stati locali interattivi
  const [suppressorCount, setSuppressorCount] = useState(suppressorsInitial);
  const [suppressorUsedNotice, setSuppressorUsedNotice] = useState(false);
  const [telegramUnread, setTelegramUnread] = useState(3);
  const [succbookUnread, setSuccbookUnread] = useState(5);
  const [guildAcceptedMission, setGuildAcceptedMission] = useState(null);
  const [musicPlaying, setMusicPlaying] = useState(true);
  const [activeTrack, setActiveTrack] = useState({ title: 'Subterranean Bass Drive', artist: 'Echo (Digital Familiar) · DCC Net', mood: 'Dungeon Synth / Focus' });

  // -------------------------------------------------------------
  // DATABASE 1: TELEGRAM CHAT
  // -------------------------------------------------------------
  const [chatInput, setChatInput] = useState('');
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: 'Papà (Erik)',
      role: 'Prime Alpha · DCC',
      color: 'text-amber-400',
      badge: 'bg-amber-950/80 text-amber-300 border border-amber-800',
      text: 'Ragazzi, siete arrivati a Solarton? Kaladin ha predisposto la scorta discreta attorno all\\'ingresso est del campus. Non dimenticate i soppressori.',
      time: '08:02'
    },
    {
      id: 2,
      sender: 'Noah',
      role: 'Beta · PR',
      color: 'text-sky-400',
      badge: 'bg-sky-950/80 text-sky-300 border border-sky-800',
      text: 'Tranquillo Boss, sono già al banchetto matricole SUCC. Se Alyssa ritarda è perché doveva abbinare le scarpe alla borsa medica 💅',
      time: '08:05'
    },
    {
      id: 3,
      sender: 'Jasper',
      role: 'Technomancer',
      color: 'text-emerald-400',
      badge: 'bg-emerald-950/80 text-emerald-300 border border-emerald-800',
      text: 'Siamo arrivati. Sto accompagnando Alyssa verso la segreteria di Medicina e Botanica. Noah piantala o ti blocco il Wi-Fi di Villa Douglas.',
      time: '08:08'
    },
    {
      id: 4,
      sender: 'Echo',
      role: 'Digital Familiar',
      color: 'text-cyan-300',
      badge: 'bg-cyan-950/80 text-cyan-300 border border-cyan-800',
      text: '[Audio Mood Speaker: Avviata playlist \\'Subterranean Bass Drive\\']. Parametri vitali del Fireteam nella norma. Nessuna anomalia miasmatica nel raggio di 800m.',
      time: '08:09'
    },
    {
      id: 5,
      sender: 'Malachia',
      role: 'Berserker Strike',
      color: 'text-rose-400',
      badge: 'bg-rose-950/80 text-rose-300 border border-rose-800',
      text: 'Ho finito la sessione pesi al campo Bulls. Chiunque si avvicini con cattive intenzioni se la vede con me. Mandatemi la posizione.',
      time: '08:12'
    }
  ]);

  const handleSendMessage = () => {
    if (!chatInput.trim()) return;
    const newMsg = {
      id: Date.now(),
      sender: 'Tu (Active User)',
      role: 'Operativo',
      color: 'text-violet-300',
      badge: 'bg-violet-950 text-violet-300 border border-violet-800',
      text: chatInput.trim(),
      time: 'Adesso'
    };
    setMessages(prev => [...prev, newMsg]);
    setChatInput('');
  };

  // -------------------------------------------------------------
  // DATABASE 2: SUCC & CUMS ACADEMICS
  // -------------------------------------------------------------
  const STUDENTS_DATA = {
    alyssa: {
      name: 'Alyssa Douglas',
      badge: 'Matricola · Pre-Med',
      school: 'SUCC (Solarton University)',
      major: 'Scienze Mediche & Botanica Arcana',
      dept: 'Facoltà di Medicina e Fisiologia Demi-Umani',
      gpa: '3.92',
      credits: 28,
      internship: 'Infermeria SUCC & Laboratori Medici DCC (Dr.ssa Duskwood)',
      courses: [
        { code: 'MED-101', name: 'Anatomia Comparata Demi-Umani', prof: 'H. Vance', cfu: 8, grade: 'A+' },
        { code: 'BOT-104', name: 'Botanica Arcana & Proprietà Lunari', prof: 'M. Willow', cfu: 6, grade: 'A' },
        { code: 'FAR-202', name: 'Farmacologia & Inibitori Ferormonali', prof: 'E. Duskwood', cfu: 8, grade: 'A' },
        { code: 'EMR-108', name: 'Primo Soccorso & Traumi da Argento', prof: 'G. Vance', cfu: 6, grade: 'A+' }
      ]
    },
    jasper: {
      name: 'Jasper Douglas',
      badge: '1° Anno · Ingegneria',
      school: 'SUCC (Solarton University)',
      major: 'Ingegneria Arcana & Meccanica Avanzata',
      dept: 'Dipartimento di Tecnologie Silver-Tech e Magitech',
      gpa: '3.78',
      credits: 30,
      internship: 'R&D Tecnologico & Droni Tattici DCC (Laboratorio Ovest)',
      courses: [
        { code: 'ENG-102', name: 'Balistica Silver-Tech & Armi Magiche', prof: 'K. Rourke', cfu: 8, grade: 'A' },
        { code: 'RIF-201', name: 'Geometria Non-Euclidea & Teoria dei Rift', prof: 'V. Aris', cfu: 6, grade: 'A-' },
        { code: 'MAT-105', name: 'Ingegneria dei Materiali Anti-Miasma', prof: 'L. Sterling', cfu: 8, grade: 'B+' },
        { code: 'RUN-110', name: 'Fabbricazione Runica & Magitech', prof: 'T. Stone', cfu: 8, grade: 'A+' }
      ]
    },
    noah: {
      name: 'Noah Douglas',
      badge: '2° Anno · Public Relations',
      school: 'SUCC (Solarton University)',
      major: 'Scienze Politiche, PR & Management Sportivo',
      dept: 'Scuola di Relazioni Istituzionali e Diplomazia',
      gpa: '3.55',
      credits: 54,
      internship: 'Ufficio Stampa DCC & Relazioni SUCC Bulls Athletics',
      courses: [
        { code: 'COM-201', name: 'Comunicazione Istituzionale & Crisi di Branco', prof: 'D. Sterling', cfu: 8, grade: 'A' },
        { code: 'DIR-204', name: 'Diritto Commerciale Fazioni Supernatural', prof: 'E. Thornton', cfu: 8, grade: 'B+' },
        { code: 'MKT-208', name: 'Marketing & Sponsorizzazioni DMHA Bulls', prof: 'G. Hayes', cfu: 6, grade: 'A' }
      ]
    },
    malachia: {
      name: 'Malachia Douglas',
      badge: '3° Anno · Tattica',
      school: 'SUCC (Solarton University)',
      major: 'Scienze Motorie, Tattica di Combattimento & Difesa',
      dept: 'Accademia Tattica e Addestramento Operativo',
      gpa: '3.30',
      credits: 82,
      internship: 'Istruttore Assistente Combattimento Corpo a Corpo SUCC',
      courses: [
        { code: 'TAC-301', name: 'Tattica di Branco & Incursioni nei Rift', prof: 'K. Nargathon', cfu: 10, grade: 'A+' },
        { code: 'SPT-305', name: 'Condizionamento Fisico Demi-Umani & Shift', prof: 'Coach D', cfu: 8, grade: 'A+' },
        { code: 'BIO-209', name: 'Fisiologia dello Sforzo & Resistenza Miasma', prof: 'E. Duskwood', cfu: 6, grade: 'B' }
      ]
    },
    cums_students: {
      name: 'C.U.M.S. Collegio Magico (Amerian & Studenti)',
      badge: 'Duellanti Arcani & Mages',
      school: 'C.U.M.S. (California University of Magical Studies)',
      major: 'Arti Arcane Superiori, Evocazione & Duello Tattico',
      dept: 'Presidenza del Rettore Zaire Ziisis · Cattedra Prof. Xaiden Nershatar',
      gpa: '3.88',
      credits: 45,
      internship: 'Arena di Duello Magico CUMS & Pattuglie Difesa Solarton',
      courses: [
        { code: 'DUE-101', name: 'Combattimento Tattico e Duello d\\'Ombra', prof: 'X. Nershatar', cfu: 10, grade: 'A+' },
        { code: 'SOL-202', name: 'Evocazione Solare & Barriere Pure (Caien)', prof: 'Z. Ziisis', cfu: 8, grade: 'A' },
        { code: 'HYD-105', name: 'Idromanzia Applicata & Correnti Fluide (Aeril)', prof: 'M. Orena', cfu: 8, grade: 'A-' },
        { code: 'BLD-303', name: 'Magia del Sangue & Ombre Proibite (Lestat)', prof: 'X. Nershatar', cfu: 8, grade: 'B+' }
      ]
    }
  };

  const [selectedStudent, setSelectedStudent] = useState('alyssa');
  const currentStudentData = STUDENTS_DATA[selectedStudent] || STUDENTS_DATA.alyssa;

  // -------------------------------------------------------------
  // DATABASE 3: DMHA HUNTER GUILD
  // -------------------------------------------------------------
  const HUNTERS_DATA = {
    alyssa: {
      name: 'Alyssa Douglas',
      rank: 'Rango A',
      rankColor: 'bg-blue-950 text-sky-300 border border-blue-800',
      role: 'Healer & Supporto di Campo',
      squad: 'Douglas Vanguard / Seven Hills Fireteam',
      credits: 4850,
      completed: 18,
      specialty: 'Medicina da Campo, Terapie Anti-Miasma & Incanti Rigenerativi'
    },
    jasper: {
      name: 'Jasper Douglas',
      rank: 'Rango A',
      rankColor: 'bg-blue-950 text-sky-300 border border-blue-800',
      role: 'Technomancer & Netrunner Tattico',
      squad: 'Douglas Vanguard / Seven Hills Fireteam',
      credits: 3600,
      completed: 14,
      specialty: 'Cyber-Tracciamento Rift, Dispositivi Anti-Interferenza & Katana di Vetro di Drago'
    },
    malachia: {
      name: 'Malachia Douglas',
      rank: 'Rango S',
      rankColor: 'bg-rose-950 text-rose-300 border border-rose-800',
      role: 'Apex Berserker / Assaltatore Primario',
      squad: 'Seven Hills Apex Strike Force',
      credits: 9200,
      completed: 35,
      specialty: 'Neutralizzazione Minacce Classe S, Breccia nei Rift & Caccia ai Capi Branco'
    },
    ukiyo: {
      name: 'Team Ukiyo (Radek, Goran, Kian)',
      rank: 'Rango S / A',
      rankColor: 'bg-purple-950 text-purple-300 border border-purple-800',
      role: 'Dungeon Crawler Elite Trio',
      squad: 'Team Ukiyo (Cable District HQ)',
      credits: 8400,
      completed: 29,
      specialty: 'Vanguard Orc DPS (Radek), Minotaur Frontline Tank (Goran), Half-Elf Mana Sniper (Kian)'
    },
    noah: {
      name: 'Noah Douglas',
      rank: 'Rango B',
      rankColor: 'bg-amber-950 text-amber-300 border border-amber-800',
      role: 'Logistica & Field Coordinator',
      squad: 'Douglas Vanguard Support',
      credits: 2100,
      completed: 11,
      specialty: 'Coordinamento Squadre, Negoziazione con Autorità Civili & Mappe Tattiche'
    }
  };

  const [selectedHunter, setSelectedHunter] = useState('alyssa');
  const currentHunterData = HUNTERS_DATA[selectedHunter] || HUNTERS_DATA.alyssa;

  const GUILD_MISSIONS = [
    {
      id: 'hunt_bay',
      title: 'Pattugliamento Notturno: Baia di Blackwood',
      rank: 'Rango C',
      reward: '350 Crediti Gilda · 2x Frammenti Abissali',
      threat: 'Miasma Spiders & Anomalie Fluviali',
      desc: 'Scansione anomalie termiche e bonifica mostri minori vicino ai vecchi magazzini fluviali.'
    },
    {
      id: 'hunt_cable',
      title: 'Bonifica Condotti Settore 4 (Cable District)',
      rank: 'Rango D',
      reward: '180 Crediti Gilda · 1x Cassa Ricambi',
      threat: 'Ratti del Vuoto & Fango Tossico',
      desc: 'Segnalazione pervenuta dalle officine Ironhorn Nomads di Marek per infiltrazioni nel seminterrato.'
    },
    {
      id: 'hunt_hex',
      title: 'Scorta Carovana Alchemica verso Hex Valley',
      rank: 'Rango C',
      reward: '500 Crediti Gilda · Runa d\\'Argento',
      threat: 'Iene delle Dune & Bracconieri',
      desc: 'Scorta armata per trasporto rifornimenti tra campus SUCC, CUMS e la valle agricola di Solarton.'
    },
    {
      id: 'hunt_apex',
      title: 'Incursione Rift Profondità 3: Apex Trial',
      rank: 'Rango B/S',
      reward: '1.200 Crediti Gilda · 1x Abyssal Core Raro',
      threat: 'Minotauro Corrotto del Rift & Chimera',
      desc: 'Trial sotterraneo ad alta densità di miasma. Consigliata squadra con Heavy Tank e supporto medico.'
    }
  ];

  // -------------------------------------------------------------
  // DATABASE 4: SUCCBOOK CAMPUS SOCIAL FEED
  // -------------------------------------------------------------
  const [feedPosts, setFeedPosts] = useState([
    {
      id: 1,
      author: 'SUCC Athletics (Bulls)',
      handle: '@succ_bulls_official',
      badge: 'Verificato',
      avatar: '🏈',
      time: '25m fa',
      text: 'Tryouts aperti per la stagione autunnale di Rugby & Football magico! Prima selezione oggi alle 17:30 al campo ovest. Coach D e Malachia supervisionano il riscaldamento. Presentarsi in tenuta regolamentare!',
      likes: 84,
      liked: false
    },
    {
      id: 2,
      author: 'Le Refuge des Chats · Arcadia',
      handle: '@refuge_chats_arcadia',
      badge: 'Bottega',
      avatar: '☕',
      time: '1h fa',
      text: 'Buongiorno Solarton e Blackwood! Jaelyn ha sfornato i nuovi croissant alla crema di mandorle lunari. Caffè macinato fresco e soppressori di odore naturali in omaggio per tutti gli studenti!',
      likes: 142,
      liked: false
    },
    {
      id: 3,
      author: 'DJ Frequency & Warehouse Raves',
      handle: '@sub_frequency_solarton',
      badge: 'Eventi',
      avatar: '🎧',
      time: '2h fa',
      text: 'Venerdì notte rave underground nei vecchi magazzini industriali al confine tra Solarton e Blackwood. Sound system magitech curato dai netrunner della DCC. Ingresso riservato a studenti e licantropi con controllo odore all\\'ingresso.',
      likes: 215,
      liked: false
    }
  ]);

  const toggleLike = (postId) => {
    setFeedPosts(prev => prev.map(p => {
      if (p.id === postId) {
        return { ...p, liked: !p.liked, likes: p.liked ? p.likes - 1 : p.likes + 1 };
      }
      return p;
    }));
  };

  // Azione Inala Soppressore
  const handleInhaleSuppressor = () => {
    if (suppressorCount <= 0) return;
    setSuppressorCount(c => c - 1);
    setSuppressorUsedNotice(true);
    setTimeout(() => setSuppressorUsedNotice(false), 3500);
  };

  return (
    <div className="w-full max-w-md mx-auto font-sans select-none text-zinc-100">
      {/* SCOCCA DELLO SMARTPHONE */}
      <div className="bg-zinc-950 border-2 border-zinc-800 rounded-3xl p-3 shadow-2xl relative overflow-hidden">
        
        {/* STATUS BAR SUPERIORE DELLO SMARTPHONE */}
        <div className="flex items-center justify-between px-3 py-1 bg-black/90 rounded-t-2xl border-b border-zinc-800/80 text-[11px] font-mono text-zinc-400 mb-2">
          <div className="flex items-center gap-1.5">
            <span className="font-bold text-zinc-200">08:24</span>
            <span className="text-[9px] px-1 py-0.2 bg-zinc-900 rounded text-emerald-400 font-sans">DCC 5G</span>
          </div>

          {/* DYNAMIC ISLAND / NOTCH CENTRALE */}
          <div className="flex items-center gap-1.5 px-2 py-0.5 bg-zinc-900 border border-zinc-800 rounded-full text-[10px]">
            <span title="Fase Lunare">{isFullMoon ? '🌕 Piena' : '🌙 ' + moonPhase}</span>
            <span className="text-zinc-600">|</span>
            <span title="Soppressori Odore" className={suppressorCount <= 1 ? 'text-rose-400 font-bold animate-pulse' : 'text-emerald-400'}>
              🧪 x{suppressorCount}
            </span>
          </div>

          <div className="flex items-center gap-1 text-[10px]">
            <span>📶</span>
            <span>🛜</span>
            <span className="text-emerald-400 font-bold">98%</span>
          </div>
        </div>

        {/* FEEDBACK INALAZIONE SOPPRESSORE */}
        {suppressorUsedNotice && (
          <div className="mb-2 p-2 bg-emerald-950 border border-emerald-800 rounded-xl text-center text-xs text-emerald-300 font-medium animate-in fade-in slide-in-from-top-1">
            🩺 <span className="font-bold">Dose Inalata:</span> Fuga ferormonale bloccata. Schermatura olfattiva attiva per 8 ore.
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 1: HOME DASHBOARD DELLO SMARTPHONE                             */}
        {/* ========================================================================= */}
        {activeApp === 'home' && (
          <div className="space-y-3">
            {/* WIDGET CLOCK & WORLD ENVIRONMENT */}
            <div className="bg-gradient-to-br from-zinc-900 via-zinc-900/90 to-zinc-950 border border-zinc-800 rounded-2xl p-3.5 shadow-inner">
              <div className="flex items-center justify-between text-xs text-zinc-400 mb-1">
                <span>Venerdì, 5 Aprile 2024</span>
                <span className="px-2 py-0.5 rounded-full bg-zinc-800 text-[10px] text-zinc-300">Solarton & Blackwood</span>
              </div>
              <div className="flex items-baseline justify-between">
                <div>
                  <div className="text-2xl font-black tracking-tight text-white">08:24 <span className="text-xs font-normal text-zinc-400">PST</span></div>
                  <div className="text-xs text-zinc-400 flex items-center gap-1.5 mt-0.5">
                    <span>{isNight ? '🌃 Notte' : '☀️ Mattina'}</span>
                    <span>·</span>
                    <span className="text-amber-300 font-medium">{moonPhase}</span>
                  </div>
                </div>
                <div className="text-right">
                  <span className="text-[10px] px-2 py-0.5 bg-blue-950/80 border border-sky-800/60 rounded-full text-sky-300 font-mono">
                    Rift: {riftAlert}
                  </span>
                </div>
              </div>
            </div>

            {/* WIDGET RAPIDO BIOTRACK & BUFFER LUNARE */}
            <div className="grid grid-cols-2 gap-2 text-xs">
              <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-2.5 flex flex-col justify-between">
                <div className="text-[10px] text-zinc-400 uppercase tracking-wider font-semibold">Biologia LSE</div>
                <div className="font-bold text-sm text-zinc-200 mt-1 flex items-center justify-between">
                  <span>{lseStatus}</span>
                  <span className="text-[10px] font-normal text-zinc-500">Peak -{daysLeft}d</span>
                </div>
                <button
                  onClick={handleInhaleSuppressor}
                  disabled={suppressorCount <= 0}
                  className="mt-2 w-full py-1 bg-zinc-800 hover:bg-zinc-700 active:scale-95 disabled:opacity-40 rounded-lg text-[10px] font-medium text-emerald-300 border border-zinc-700 transition"
                >
                  {suppressorCount > 0 ? '+ Inala Soppressore' : 'Esauriti! (Allerta)'}
                </button>
              </div>

              <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-2.5 flex flex-col justify-between">
                <div className="text-[10px] text-zinc-400 uppercase tracking-wider font-semibold">Reputazione Branco</div>
                <div className="font-bold text-sm text-amber-300 mt-1 flex items-center justify-between">
                  <span>Douglas DCC</span>
                  <span className="text-[10px] text-zinc-400 font-mono">{packRep}/100</span>
                </div>
                <div className="w-full bg-zinc-800 h-1.5 rounded-full overflow-hidden mt-2">
                  <div className="bg-amber-400 h-full rounded-full" style={{ width: packRep + '%' }}></div>
                </div>
              </div>
            </div>

            {/* GRIGLIA ICONE APP SMARTPHONE */}
            <div className="pt-1">
              <div className="text-[11px] font-semibold text-zinc-400 px-1 mb-2 uppercase tracking-wider">Applicazioni Installate</div>
              <div className="grid grid-cols-4 gap-2.5 text-center">
                
                {/* App 1: Telegram */}
                <button
                  onClick={() => { setActiveApp('telegram'); setTelegramUnread(0); }}
                  className="group flex flex-col items-center gap-1.5 p-2 bg-zinc-900/80 hover:bg-zinc-800/90 active:scale-95 rounded-2xl border border-zinc-800 transition"
                >
                  <div className="relative w-11 h-11 rounded-2xl bg-gradient-to-tr from-sky-600 to-sky-400 flex items-center justify-center text-xl shadow-md">
                    💬
                    {telegramUnread > 0 && (
                      <span className="absolute -top-1 -right-1 bg-rose-500 text-white text-[9px] font-bold w-4 h-4 rounded-full flex items-center justify-center border-2 border-zinc-950">
                        {telegramUnread}
                      </span>
                    )}
                  </div>
                  <span className="text-[10px] font-medium text-zinc-300 group-hover:text-white">Telegram</span>
                </button>

                {/* App 2: SUCC & CUMS Portal */}
                <button
                  onClick={() => setActiveApp('academics')}
                  className="group flex flex-col items-center gap-1.5 p-2 bg-zinc-900/80 hover:bg-zinc-800/90 active:scale-95 rounded-2xl border border-zinc-800 transition"
                >
                  <div className="w-11 h-11 rounded-2xl bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center text-xl shadow-md">
                    🎓
                  </div>
                  <span className="text-[10px] font-medium text-zinc-300 group-hover:text-white">Accademia</span>
                </button>

                {/* App 3: DMHA Gilda */}
                <button
                  onClick={() => setActiveApp('guild')}
                  className="group flex flex-col items-center gap-1.5 p-2 bg-zinc-900/80 hover:bg-zinc-800/90 active:scale-95 rounded-2xl border border-zinc-800 transition"
                >
                  <div className="w-11 h-11 rounded-2xl bg-gradient-to-tr from-rose-700 to-amber-600 flex items-center justify-center text-xl shadow-md">
                    ⚔️
                  </div>
                  <span className="text-[10px] font-medium text-zinc-300 group-hover:text-white">DMHA Gilda</span>
                </button>

                {/* App 4: LSE BioTrack */}
                <button
                  onClick={() => setActiveApp('biotrack')}
                  className="group flex flex-col items-center gap-1.5 p-2 bg-zinc-900/80 hover:bg-zinc-800/90 active:scale-95 rounded-2xl border border-zinc-800 transition"
                >
                  <div className="w-11 h-11 rounded-2xl bg-gradient-to-tr from-emerald-600 to-teal-400 flex items-center justify-center text-xl shadow-md">
                    🐾
                  </div>
                  <span className="text-[10px] font-medium text-zinc-300 group-hover:text-white">BioTrack LSE</span>
                </button>

                {/* App 5: SUCCbook Social */}
                <button
                  onClick={() => { setActiveApp('succbook'); setSuccbookUnread(0); }}
                  className="group flex flex-col items-center gap-1.5 p-2 bg-zinc-900/80 hover:bg-zinc-800/90 active:scale-95 rounded-2xl border border-zinc-800 transition"
                >
                  <div className="relative w-11 h-11 rounded-2xl bg-gradient-to-tr from-blue-700 to-cyan-500 flex items-center justify-center text-xl shadow-md">
                    🌐
                    {succbookUnread > 0 && (
                      <span className="absolute -top-1 -right-1 bg-rose-500 text-white text-[9px] font-bold w-4 h-4 rounded-full flex items-center justify-center border-2 border-zinc-950">
                        {succbookUnread}
                      </span>
                    )}
                  </div>
                  <span className="text-[10px] font-medium text-zinc-300 group-hover:text-white">SUCCbook</span>
                </button>

                {/* App 6: Echo Spotify Net */}
                <button
                  onClick={() => setActiveApp('music')}
                  className="group flex flex-col items-center gap-1.5 p-2 bg-zinc-900/80 hover:bg-zinc-800/90 active:scale-95 rounded-2xl border border-zinc-800 transition"
                >
                  <div className="w-11 h-11 rounded-2xl bg-gradient-to-tr from-emerald-500 to-green-600 flex items-center justify-center text-xl shadow-md">
                    🎵
                  </div>
                  <span className="text-[10px] font-medium text-zinc-300 group-hover:text-white">Echo Audio</span>
                </button>

                {/* App 7: C.U.M.S. Dueling Arena */}
                <button
                  onClick={() => { setActiveApp('academics'); setSelectedStudent('cums_students'); }}
                  className="group flex flex-col items-center gap-1.5 p-2 bg-zinc-900/80 hover:bg-zinc-800/90 active:scale-95 rounded-2xl border border-zinc-800 transition"
                >
                  <div className="w-11 h-11 rounded-2xl bg-gradient-to-tr from-purple-700 to-pink-600 flex items-center justify-center text-xl shadow-md">
                    🔮
                  </div>
                  <span className="text-[10px] font-medium text-zinc-300 group-hover:text-white">CUMS Arena</span>
                </button>

                {/* App 8: Cable Distr. & Nomads */}
                <button
                  onClick={() => { setActiveApp('guild'); setSelectedHunter('ukiyo'); }}
                  className="group flex flex-col items-center gap-1.5 p-2 bg-zinc-900/80 hover:bg-zinc-800/90 active:scale-95 rounded-2xl border border-zinc-800 transition"
                >
                  <div className="w-11 h-11 rounded-2xl bg-gradient-to-tr from-amber-700 to-yellow-600 flex items-center justify-center text-xl shadow-md">
                    🏍️
                  </div>
                  <span className="text-[10px] font-medium text-zinc-300 group-hover:text-white">Team Ukiyo</span>
                </button>
              </div>
            </div>

            {/* MINI MUSIC PLAYER WIDGET IN HOME */}
            <div className="p-2.5 bg-zinc-900/90 border border-zinc-800 rounded-xl flex items-center justify-between text-xs">
              <div className="flex items-center gap-2 overflow-hidden">
                <span className="text-base animate-pulse">📻</span>
                <div className="truncate">
                  <div className="font-semibold text-zinc-200 truncate text-[11px]">{activeTrack.title}</div>
                  <div className="text-[9px] text-zinc-400 truncate">{activeTrack.artist}</div>
                </div>
              </div>
              <button
                onClick={() => setMusicPlaying(!musicPlaying)}
                className="px-2.5 py-1 bg-zinc-800 hover:bg-zinc-700 rounded-lg text-[10px] font-medium text-zinc-200 border border-zinc-700 transition"
              >
                {musicPlaying ? '⏸ Pausa' : '▶ Play'}
              </button>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 2: TELEGRAM (DOUGLAS PACK CHAT)                                */}
        {/* ========================================================================= */}
        {activeApp === 'telegram' && (
          <div className="space-y-2">
            {/* Header Chat */}
            <div className="flex items-center justify-between pb-2 border-b border-zinc-800">
              <div className="flex items-center gap-2">
                <button onClick={() => setActiveApp('home')} className="text-zinc-400 hover:text-white text-xs font-bold px-1.5 py-0.5 bg-zinc-900 rounded">⬅ Home</button>
                <div>
                  <div className="text-xs font-bold text-white flex items-center gap-1">
                    <span>🐺 Douglas Pack Chat</span>
                    <span className="w-2 h-2 rounded-full bg-emerald-400 inline-block"></span>
                  </div>
                  <div className="text-[9px] text-zinc-400">Canale Criptato DCC · 6 membri connessi</div>
                </div>
              </div>
            </div>

            {/* Area Messaggi Scrollabile */}
            <div className="h-64 overflow-y-auto space-y-2 pr-1 text-xs">
              {messages.map(m => (
                <div key={m.id} className="p-2 bg-zinc-900/90 rounded-xl border border-zinc-800/80">
                  <div className="flex items-center justify-between mb-1">
                    <div className="flex items-center gap-1.5">
                      <span className={'font-bold text-[11px] ' + m.color}>{m.sender}</span>
                      <span className={'text-[8px] px-1 py-0.2 rounded font-mono ' + m.badge}>{m.role}</span>
                    </div>
                    <span className="text-[9px] text-zinc-500 font-mono">{m.time}</span>
                  </div>
                  <p className="text-zinc-200 text-[11px] leading-relaxed">{m.text}</p>
                </div>
              ))}
            </div>

            {/* Input per Rispondere */}
            <div className="flex items-center gap-1.5 pt-1">
              <input
                type="text"
                placeholder="Scrivi messaggio al branco..."
                value={chatInput}
                onChange={e => setChatInput(e.target.value)}
                onKeyDown={e => e.key === 'Enter' && handleSendMessage()}
                className="flex-1 bg-zinc-900 border border-zinc-800 rounded-xl px-2.5 py-1.5 text-xs text-white placeholder-zinc-500 focus:outline-none focus:border-sky-500"
              />
              <button
                onClick={handleSendMessage}
                className="px-3 py-1.5 bg-sky-600 hover:bg-sky-500 active:scale-95 text-white font-medium text-xs rounded-xl transition"
              >
                Invia
              </button>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 3: PORTALE ACCADEMICO (SUCC & C.U.M.S.)                        */}
        {/* ========================================================================= */}
        {activeApp === 'academics' && (
          <div className="space-y-2.5">
            {/* Header App */}
            <div className="flex items-center justify-between pb-1.5 border-b border-zinc-800">
              <div className="flex items-center gap-2">
                <button onClick={() => setActiveApp('home')} className="text-zinc-400 hover:text-white text-xs font-bold px-1.5 py-0.5 bg-zinc-900 rounded">⬅ Home</button>
                <div className="text-xs font-bold text-white">🎓 Portale Universitario (SUCC / CUMS)</div>
              </div>
            </div>

            {/* Selettore Studente Pills */}
            <div className="flex gap-1 overflow-x-auto pb-1 text-[10px]">
              {[
                { id: 'alyssa', label: 'Alyssa (Pre-Med)' },
                { id: 'jasper', label: 'Jasper (Ing.)' },
                { id: 'noah', label: 'Noah (PR)' },
                { id: 'malachia', label: 'Malachia (Tattica)' },
                { id: 'cums_students', label: 'CUMS Arcani' }
              ].map(s => (
                <button
                  key={s.id}
                  onClick={() => setSelectedStudent(s.id)}
                  className={'px-2 py-1 rounded-lg whitespace-nowrap transition ' + (selectedStudent === s.id ? 'bg-indigo-600 text-white font-bold' : 'bg-zinc-900 text-zinc-400 hover:bg-zinc-800')}
                >
                  {s.label}
                </button>
              ))}
            </div>

            {/* Scheda Profilo Studente Selezionato */}
            <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-3 text-xs space-y-2">
              <div className="flex items-start justify-between">
                <div>
                  <div className="font-bold text-sm text-white">{currentStudentData.name}</div>
                  <div className="text-[10px] text-zinc-400 font-medium">{currentStudentData.major}</div>
                  <div className="text-[9px] text-indigo-400 mt-0.5">{currentStudentData.school} · {currentStudentData.dept}</div>
                </div>
                <div className="text-right">
                  <div className="text-sm font-black font-mono text-emerald-400">{currentStudentData.gpa}</div>
                  <div className="text-[9px] text-zinc-500 uppercase">GPA / Media</div>
                </div>
              </div>

              {/* Barra Avanzamento Crediti */}
              <div>
                <div className="flex justify-between text-[10px] text-zinc-400 mb-1">
                  <span>CFU Acquisiti: <span className="text-zinc-200 font-bold">{currentStudentData.credits}</span> / 180</span>
                  <span>{Math.round((currentStudentData.credits / 180) * 100)}%</span>
                </div>
                <div className="w-full bg-zinc-800 h-1.5 rounded-full overflow-hidden">
                  <div className="bg-indigo-500 h-full rounded-full" style={{ width: (currentStudentData.credits / 180 * 100) + '%' }}></div>
                </div>
              </div>

              {/* Tirocinio */}
              <div className="p-2 bg-black/50 rounded-lg text-[10px] text-zinc-300 border border-zinc-800/80">
                <span className="text-zinc-500 uppercase font-semibold">Stage / Tirocinio:</span> {currentStudentData.internship}
              </div>

              {/* Tabella Corsi & Voti */}
              <div className="space-y-1.5 pt-1">
                <div className="text-[10px] font-bold text-zinc-400 uppercase tracking-wider">Corsi Iscritti & Valutazioni</div>
                {currentStudentData.courses.map((c, i) => (
                  <div key={i} className="p-1.5 bg-zinc-950/70 border border-zinc-800 rounded-lg flex items-center justify-between text-[11px]">
                    <div>
                      <div className="font-medium text-zinc-200">{c.name}</div>
                      <div className="text-[9px] text-zinc-500 font-mono">{c.code} · Prof. {c.prof} · {c.cfu} CFU</div>
                    </div>
                    <span className="font-mono font-bold px-1.5 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px]">
                      {c.grade}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 4: REGISTRO GILDA DEI CACCIATORI (DMHA)                         */}
        {/* ========================================================================= */}
        {activeApp === 'guild' && (
          <div className="space-y-2.5">
            {/* Header App */}
            <div className="flex items-center justify-between pb-1.5 border-b border-zinc-800">
              <div className="flex items-center gap-2">
                <button onClick={() => setActiveApp('home')} className="text-zinc-400 hover:text-white text-xs font-bold px-1.5 py-0.5 bg-zinc-900 rounded">⬅ Home</button>
                <div className="text-xs font-bold text-white">⚔️ Registro Gilda Cacciatori (DMHA)</div>
              </div>
            </div>

            {/* Selettore Cacciatori Pills */}
            <div className="flex gap-1 overflow-x-auto pb-1 text-[10px]">
              {[
                { id: 'alyssa', label: 'Alyssa' },
                { id: 'jasper', label: 'Jasper' },
                { id: 'malachia', label: 'Malachia' },
                { id: 'ukiyo', label: 'Team Ukiyo' },
                { id: 'noah', label: 'Noah' }
              ].map(h => (
                <button
                  key={h.id}
                  onClick={() => setSelectedHunter(h.id)}
                  className={'px-2 py-1 rounded-lg whitespace-nowrap transition ' + (selectedHunter === h.id ? 'bg-rose-700 text-white font-bold' : 'bg-zinc-900 text-zinc-400 hover:bg-zinc-800')}
                >
                  {h.label}
                </button>
              ))}
            </div>

            {/* Profilo Cacciatore Attivo */}
            <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-2.5 text-xs space-y-2">
              <div className="flex items-start justify-between">
                <div>
                  <div className="font-bold text-sm text-white">{currentHunterData.name}</div>
                  <div className="text-[10px] text-zinc-400">{currentHunterData.role}</div>
                  <div className="text-[9px] text-zinc-500">{currentHunterData.squad}</div>
                </div>
                <div className="text-right">
                  <span className={'px-2 py-0.5 rounded text-[10px] font-bold font-mono ' + currentHunterData.rankColor}>
                    {currentHunterData.rank}
                  </span>
                  <div className="text-[10px] text-amber-300 font-mono mt-1">{currentHunterData.credits} Crediti</div>
                </div>
              </div>
              <div className="text-[10px] text-zinc-300 bg-black/40 p-1.5 rounded border border-zinc-800/80">
                <span className="text-zinc-500 font-semibold">Specialità:</span> {currentHunterData.specialty}
              </div>
            </div>

            {/* Bacheca Incarichi Attivi & Disponibili */}
            <div className="space-y-1.5">
              <div className="flex items-center justify-between text-[10px] font-bold text-zinc-400 uppercase tracking-wider">
                <span>Bacheca Incarichi di Bonifica</span>
                <span className="text-zinc-500 font-normal">Rift & Territorio</span>
              </div>
              <div className="h-44 overflow-y-auto space-y-1.5 pr-0.5">
                {GUILD_MISSIONS.map(m => {
                  const isAccepted = guildAcceptedMission === m.id;
                  return (
                    <div key={m.id} className={'p-2 rounded-xl border text-[11px] transition ' + (isAccepted ? 'bg-amber-950/40 border-amber-800' : 'bg-zinc-900 border-zinc-800')}>
                      <div className="flex items-center justify-between mb-1">
                        <span className="font-bold text-zinc-200">{m.title}</span>
                        <span className="text-[9px] px-1 py-0.2 bg-zinc-800 rounded font-mono text-zinc-300">{m.rank}</span>
                      </div>
                      <p className="text-[10px] text-zinc-400 leading-snug mb-1.5">{m.desc}</p>
                      <div className="flex items-center justify-between text-[10px]">
                        <span className="text-amber-400 font-mono font-medium">{m.reward}</span>
                        <button
                          onClick={() => setGuildAcceptedMission(isAccepted ? null : m.id)}
                          className={'px-2 py-0.5 rounded text-[10px] font-bold transition ' + (isAccepted ? 'bg-amber-500 text-black' : 'bg-zinc-800 hover:bg-zinc-700 text-zinc-200')}
                        >
                          {isAccepted ? '✓ In Corso' : 'Accetta'}
                        </button>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 5: BIOTRACK LSE (SALUTE, LUNA & FERORMONI)                       */}
        {/* ========================================================================= */}
        {activeApp === 'biotrack' && (
          <div className="space-y-3">
            <div className="flex items-center justify-between pb-1.5 border-b border-zinc-800">
              <div className="flex items-center gap-2">
                <button onClick={() => setActiveApp('home')} className="text-zinc-400 hover:text-white text-xs font-bold px-1.5 py-0.5 bg-zinc-900 rounded">⬅ Home</button>
                <div className="text-xs font-bold text-white">🐾 BioTrack LSE & Monitoraggio Branco</div>
              </div>
            </div>

            <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-3 text-xs space-y-2.5">
              <div className="flex items-center justify-between">
                <div>
                  <div className="text-xs font-bold text-white">Stato Biologico Ferormonale</div>
                  <div className="text-[10px] text-zinc-400">Ciclo Heat / Rut & Livello di Allerta</div>
                </div>
                <span className="px-2 py-0.5 bg-emerald-950 text-emerald-300 border border-emerald-800 rounded-full text-[10px] font-bold">
                  {lseStatus}
                </span>
              </div>

              {/* Scorte Cilindri Inibitori */}
              <div className="p-2.5 bg-black/60 rounded-xl border border-zinc-800 flex items-center justify-between">
                <div>
                  <div className="text-[11px] font-bold text-zinc-200">Cilindri Soppressori Odore DMHA</div>
                  <div className="text-[9px] text-zinc-500">Blocca la fuoriuscita ferormonale in pubblico</div>
                </div>
                <div className="flex items-center gap-2">
                  <span className={'text-sm font-black font-mono ' + (suppressorCount <= 1 ? 'text-rose-400 animate-pulse' : 'text-emerald-400')}>
                    x{suppressorCount}
                  </span>
                  <button
                    onClick={handleInhaleSuppressor}
                    disabled={suppressorCount <= 0}
                    className="px-2.5 py-1 bg-emerald-700 hover:bg-emerald-600 active:scale-95 disabled:opacity-40 rounded-lg text-[10px] font-bold text-white transition"
                  >
                    Inala Dose
                  </button>
                </div>
              </div>

              {/* Widget Luna Piena */}
              <div className="p-2.5 bg-zinc-950 rounded-xl border border-zinc-800 text-[11px] space-y-1">
                <div className="flex justify-between items-center">
                  <span className="font-bold text-amber-300">🌙 {moonPhase}</span>
                  <span className={'text-[9px] font-bold px-1.5 py-0.2 rounded ' + (isFullMoon ? 'bg-amber-950 text-amber-300 border border-amber-800' : 'bg-zinc-800 text-zinc-400')}>
                    {isFullMoon ? 'BUFF ATTIVO (+2 MGT/RES, +1 AGI)' : 'Influsso Standard'}
                  </span>
                </div>
                <p className="text-[10px] text-zinc-400 leading-relaxed">
                  Lupine Social Ecology: durante la luna piena, l\\'olfatto, la sensibilità ai ferormoni di branco e la risposta all\\'Alpha Command risultano massimizzati.
                </p>
              </div>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 6: SUCCBOOK (CAMPUS SOCIAL FEED)                                 */}
        {/* ========================================================================= */}
        {activeApp === 'succbook' && (
          <div className="space-y-2.5">
            <div className="flex items-center justify-between pb-1.5 border-b border-zinc-800">
              <div className="flex items-center gap-2">
                <button onClick={() => setActiveApp('home')} className="text-zinc-400 hover:text-white text-xs font-bold px-1.5 py-0.5 bg-zinc-900 rounded">⬅ Home</button>
                <div className="text-xs font-bold text-white">🌐 SUCCbook · Campus Social Network</div>
              </div>
            </div>

            <div className="h-64 overflow-y-auto space-y-2 pr-1 text-xs">
              {feedPosts.map(p => (
                <div key={p.id} className="p-2.5 bg-zinc-900 border border-zinc-800 rounded-xl space-y-1.5">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-1.5">
                      <span className="text-base">{p.avatar}</span>
                      <div>
                        <div className="font-bold text-[11px] text-zinc-200 flex items-center gap-1">
                          {p.author}
                          <span className="text-[8px] px-1 py-0.2 bg-blue-950 text-sky-400 rounded">{p.badge}</span>
                        </div>
                        <div className="text-[9px] text-zinc-500">{p.handle} · {p.time}</div>
                      </div>
                    </div>
                  </div>
                  <p className="text-[11px] text-zinc-300 leading-relaxed">{p.text}</p>
                  <div className="flex items-center justify-between pt-1 border-t border-zinc-800/60 text-[10px]">
                    <button
                      onClick={() => toggleLike(p.id)}
                      className={'flex items-center gap-1 px-2 py-0.5 rounded transition ' + (p.liked ? 'text-rose-400 font-bold' : 'text-zinc-400 hover:text-zinc-200')}
                    >
                      <span>{p.liked ? '❤️' : '🤍'}</span>
                      <span>{p.likes} Mi piace</span>
                    </button>
                    <span className="text-zinc-500">Condividi</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 7: ECHO SPOTIFY AUDIO MOOD SPEAKER                              */}
        {/* ========================================================================= */}
        {activeApp === 'music' && (
          <div className="space-y-3">
            <div className="flex items-center justify-between pb-1.5 border-b border-zinc-800">
              <div className="flex items-center gap-2">
                <button onClick={() => setActiveApp('home')} className="text-zinc-400 hover:text-white text-xs font-bold px-1.5 py-0.5 bg-zinc-900 rounded">⬅ Home</button>
                <div className="text-xs font-bold text-white">🎵 Echo Music Mood Speaker</div>
              </div>
            </div>

            <div className="bg-zinc-900 border border-zinc-800 rounded-xl p-3 text-center space-y-2">
              <div className="w-16 h-16 mx-auto rounded-2xl bg-gradient-to-tr from-emerald-600 to-teal-400 flex items-center justify-center text-3xl shadow-lg animate-pulse">
                📻
              </div>
              <div>
                <div className="font-bold text-sm text-white">{activeTrack.title}</div>
                <div className="text-[10px] text-zinc-400">{activeTrack.artist}</div>
                <div className="text-[9px] text-emerald-400 font-mono mt-0.5">Mood: {activeTrack.mood}</div>
              </div>

              <div className="flex justify-center gap-2 pt-1">
                <button
                  onClick={() => setMusicPlaying(!musicPlaying)}
                  className="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 active:scale-95 rounded-xl text-xs font-bold text-white transition"
                >
                  {musicPlaying ? '⏸ Pausa' : '▶ Play'}
                </button>
              </div>

              {/* Selettore Canali / Playlist */}
              <div className="pt-2 text-left space-y-1">
                <div className="text-[10px] font-bold text-zinc-400 uppercase tracking-wider">Preset Mood Famiglio</div>
                {[
                  { title: 'Subterranean Bass Drive', artist: 'Echo · DCC Net', mood: 'Dungeon Synth / Focus' },
                  { title: 'Villa Douglas Midnight Hearth', artist: 'Acoustic Yarrow', mood: 'Relax & Intimacy' },
                  { title: 'Rift Hazard: Apex Berserker', artist: 'Industrial Silver-Tech', mood: 'High Adrenaline Combat' },
                  { title: 'Solarton Coffeehouse Vibe', artist: 'Le Refuge des Chats', mood: 'Casual Campus Morning' }
                ].map((tr, idx) => (
                  <button
                    key={idx}
                    onClick={() => { setActiveTrack(tr); setMusicPlaying(true); }}
                    className={'w-full p-1.5 rounded-lg text-left text-[10px] flex items-center justify-between transition ' + (activeTrack.title === tr.title ? 'bg-emerald-950/80 text-emerald-300 border border-emerald-800 font-bold' : 'bg-black/40 text-zinc-400 hover:bg-zinc-800')}
                  >
                    <span className="truncate">{tr.title}</span>
                    <span className="text-[8px] opacity-75 font-mono">{tr.mood}</span>
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* BOTTOM DOCK NAVIGATION BAR (SEMPRE VISIBILE DELLO SMARTPHONE)              */}
        {/* ========================================================================= */}
        <div className="mt-3 pt-2 border-t border-zinc-800/80 flex items-center justify-around bg-black/80 rounded-b-2xl py-1 text-xs">
          <button
            onClick={() => setActiveApp('home')}
            className={'flex flex-col items-center gap-0.5 transition ' + (activeApp === 'home' ? 'text-white font-bold scale-110' : 'text-zinc-500 hover:text-zinc-300')}
          >
            <span className="text-sm">🏠</span>
            <span className="text-[9px]">Home</span>
          </button>
          <button
            onClick={() => { setActiveApp('telegram'); setTelegramUnread(0); }}
            className={'flex flex-col items-center gap-0.5 relative transition ' + (activeApp === 'telegram' ? 'text-sky-400 font-bold scale-110' : 'text-zinc-500 hover:text-zinc-300')}
          >
            <span className="text-sm">💬</span>
            <span className="text-[9px]">Chat</span>
            {telegramUnread > 0 && <span className="absolute -top-1 right-1 w-2 h-2 rounded-full bg-rose-500"></span>}
          </button>
          <button
            onClick={() => setActiveApp('academics')}
            className={'flex flex-col items-center gap-0.5 transition ' + (activeApp === 'academics' ? 'text-indigo-400 font-bold scale-110' : 'text-zinc-500 hover:text-zinc-300')}
          >
            <span className="text-sm">🎓</span>
            <span className="text-[9px]">Studio</span>
          </button>
          <button
            onClick={() => setActiveApp('guild')}
            className={'flex flex-col items-center gap-0.5 transition ' + (activeApp === 'guild' ? 'text-rose-400 font-bold scale-110' : 'text-zinc-500 hover:text-zinc-300')}
          >
            <span className="text-sm">⚔️</span>
            <span className="text-[9px]">Gilda</span>
          </button>
          <button
            onClick={() => setActiveApp('biotrack')}
            className={'flex flex-col items-center gap-0.5 transition ' + (activeApp === 'biotrack' ? 'text-emerald-400 font-bold scale-110' : 'text-zinc-500 hover:text-zinc-300')}
          >
            <span className="text-sm">🐾</span>
            <span className="text-[9px]">LSE</span>
          </button>
        </div>

      </div>
    </div>
  );
}`;

async function deployUnifiedSmartphone() {
  let token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const engineId = 'engine_HCTPXhL8xr89wUY9r9dYU';

  console.log('1. Recupero dati live di Story Engine...');
  let getRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });

  if (getRes.status === 401) {
    console.log('Token scaduto, refresh in corso...');
    token = await refreshToken();
    getRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
      headers: { 'Authorization': 'Bearer ' + token }
    });
  }

  const engine = await getRes.json();
  console.log(`Story Engine trovato: "${engine.name}" (v${engine.version})`);

  const def = engine.definition || {};

  // Configura un UNICO pannello UI unificato
  const singleUnifiedPanel = {
    id: 'panel_smartphone_os',
    name: 'Svartulfr Smartphone OS',
    icon: 'layout',
    placement: 'sidebar',
    target: 'both',
    enabled: true,
    code: unifiedSmartphoneCode
  };

  def.ui_panels = [singleUnifiedPanel];

  console.log('\n2. Salvataggio Story Engine con il pannello unificato...');
  const patchPayload = {
    expected_version: engine.version,
    name: engine.name,
    tagline: 'Svartulfr OS · Unified Smartphone Interactive UI',
    description: engine.description,
    avatar: engine.avatar,
    tags: engine.tags,
    rating: engine.rating,
    visibility: engine.visibility,
    status: engine.status,
    definition: def
  };

  const putRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(patchPayload)
  });

  if (!putRes.ok) {
    console.error(`Errore PUT (${putRes.status}):`, await putRes.text());
    return;
  }

  const updatedEngine = await putRes.json();
  console.log(`Story Engine salvato con successo! Nuova versione: v${updatedEngine.version}`);

  // Pubblicazione revisione se supportata
  console.log('\n3. Pubblicazione della nuova revisione...');
  try {
    const pubRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}/publish`, {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ expected_version: updatedEngine.version })
    });
    if (pubRes.ok) {
      const pubData = await pubRes.json();
      console.log(`Pubblicazione riuscita! Nuova revisione: ${pubData.published_revision_id}`);
    } else {
      console.log('Publish status:', pubRes.status);
    }
  } catch (err) {
    console.log('Nota publish:', err.message);
  }

  // Aggiornamento export locale
  const exportPath = path.join(__dirname, '..', 'exports', 'Story_Engines_Export.json');
  let enginesExport = [];
  if (fs.existsSync(exportPath)) {
    try {
      enginesExport = JSON.parse(fs.readFileSync(exportPath, 'utf8'));
    } catch (e) {}
  }
  const idx = enginesExport.findIndex(e => (e.id || e._id) === engineId);
  if (idx !== -1) enginesExport[idx] = updatedEngine;
  else enginesExport.push(updatedEngine);

  fs.writeFileSync(exportPath, JSON.stringify(enginesExport, null, 2), 'utf8');
  console.log(`Export locale aggiornato con successo: ${exportPath}`);
}

deployUnifiedSmartphone();

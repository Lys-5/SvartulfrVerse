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

// Codice TSX perfezionato per Wyvern StoryEngine:
// - Inline styling robusto e pulito (elimina i bordi bianchi aggressivi e la fusione del testo dock)
// - Spaziature e padding equilibrati
// - Dynamic island su riga singola senza wrap sgradevole
// - Bottom dock con pulsanti flex-col ben spaziati
// - Zero dipendenze da API browser o hook vietati (no useEffect, no DOM events)
const perfectedSmartphoneCode = `export default function Panel({ engine }) {
  // Navigazione attiva: 'home' | 'telegram' | 'academics' | 'guild' | 'biotrack' | 'succbook' | 'music'
  const [activeApp, setActiveApp] = useState('home');

  // Valori del motore
  const values = engine.values || {};
  const moonPhase = String(values.moon_phase || 'Ultimo Quarto Calante');
  const isFullMoon = Boolean(values.moon_full_active);
  const isNight = Boolean(values.night_active);
  const lseStatus = String(values.lse_biology_status || 'Dormant');
  const daysLeft = Number(values.lse_cycle_days_left ?? 20);
  const suppressors = Number(values.scent_suppressors_count ?? 3);
  const packRep = Number(values.pack_reputation ?? 25);
  const riftAlert = String(values.rift_threat_level || 'Classe 1 - Stabile');
  const sessionMode = String(engine.mode || 'world');

  // Stati locali interattivi
  const [telegramUnread, setTelegramUnread] = useState(3);
  const [succbookUnread, setSuccbookUnread] = useState(5);
  const [selectedStudent, setSelectedStudent] = useState('alyssa');
  const [selectedHunter, setSelectedHunter] = useState('alyssa');
  const [acceptedMissionId, setAcceptedMissionId] = useState(null);
  const [musicPlaying, setMusicPlaying] = useState(true);
  const [chatInput, setChatInput] = useState('');
  const [nextMsgId, setNextMsgId] = useState(10);
  const [activeTrack, setActiveTrack] = useState({
    title: 'Subterranean Bass Drive',
    artist: 'Echo (Digital Familiar) · DCC Net',
    mood: 'Dungeon Synth / Focus'
  });

  // Chiamata comando nativo Wyvern
  const handleUseSuppressor = async () => {
    try {
      await engine.runCommand('cmd_use_suppressor');
    } catch (e) {}
  };

  // Chat Telegram del Branco
  const [messages, setMessages] = useState([
    {
      id: 1,
      sender: 'Papà (Erik)',
      role: 'Prime Alpha · DCC',
      color: '#fbbf24',
      badgeBg: 'rgba(120, 53, 15, 0.4)',
      badgeBorder: '#92400e',
      text: 'Ragazzi, siete arrivati a Solarton? Kaladin ha predisposto la scorta discreta attorno all\\'ingresso est del campus. Non dimenticate i soppressori.',
      time: '08:02'
    },
    {
      id: 2,
      sender: 'Noah',
      role: 'Beta · PR',
      color: '#38bdf8',
      badgeBg: 'rgba(12, 74, 110, 0.4)',
      badgeBorder: '#0369a1',
      text: 'Tranquillo Boss, sono già al banchetto matricole SUCC. Se Alyssa ritarda è perché doveva abbinare le scarpe alla borsa medica 💅',
      time: '08:05'
    },
    {
      id: 3,
      sender: 'Jasper',
      role: 'Technomancer',
      color: '#34d399',
      badgeBg: 'rgba(6, 78, 59, 0.4)',
      badgeBorder: '#047857',
      text: 'Siamo arrivati. Sto accompagnando Alyssa verso la segreteria di Medicina e Botanica. Noah piantala o ti blocco il Wi-Fi di Villa Douglas.',
      time: '08:08'
    },
    {
      id: 4,
      sender: 'Echo',
      role: 'Digital Familiar',
      color: '#22d3ee',
      badgeBg: 'rgba(22, 78, 99, 0.4)',
      badgeBorder: '#0e7490',
      text: '[Audio Mood Speaker: Avviata playlist \\'Subterranean Bass Drive\\']. Parametri vitali del Fireteam nella norma. Nessuna anomalia miasmatica nel raggio di 800m.',
      time: '08:09'
    },
    {
      id: 5,
      sender: 'Malachia',
      role: 'Berserker Strike',
      color: '#fb7185',
      badgeBg: 'rgba(136, 19, 55, 0.4)',
      badgeBorder: '#be123c',
      text: 'Ho finito la sessione pesi al campo Bulls. Chiunque si avvicini con cattive intenzioni se la vede con me. Mandatemi la posizione.',
      time: '08:12'
    }
  ]);

  const handleSendMessage = () => {
    const textToSend = String(chatInput || '').trim();
    if (!textToSend) return;
    const newMsg = {
      id: nextMsgId,
      sender: 'Tu (Operativo)',
      role: 'Player',
      color: '#c084fc',
      badgeBg: 'rgba(88, 28, 135, 0.4)',
      badgeBorder: '#7e22ce',
      text: textToSend,
      time: 'Adesso'
    };
    setNextMsgId(id => id + 1);
    setMessages(prev => [...prev, newMsg]);
    setChatInput('');
  };

  // Database Studenti SUCC & CUMS
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
      name: 'C.U.M.S. Collegio Magico',
      badge: 'Duellanti Arcani & Mages',
      school: 'C.U.M.S. (California University of Magical Studies)',
      major: 'Arti Arcane Superiori, Evocazione & Duello Tattico',
      dept: 'Presidenza Rettore Zaire Ziisis · Cattedra Prof. Xaiden Nershatar',
      gpa: '3.88',
      credits: 45,
      internship: 'Arena di Duello Magico CUMS & Pattuglie Difesa Solarton',
      courses: [
        { code: 'DUE-101', name: 'Combattimento Tattico e Duello d\\'Ombra (Amerian)', prof: 'X. Nershatar', cfu: 10, grade: 'A+' },
        { code: 'SOL-202', name: 'Evocazione Solare & Barriere Pure (Caien)', prof: 'Z. Ziisis', cfu: 8, grade: 'A' },
        { code: 'HYD-105', name: 'Idromanzia Applicata & Correnti Fluide (Aeril)', prof: 'M. Orena', cfu: 8, grade: 'A-' },
        { code: 'BLD-303', name: 'Magia del Sangue & Ombre Proibite (Lestat)', prof: 'X. Nershatar', cfu: 8, grade: 'B+' }
      ]
    }
  };

  const studentData = STUDENTS_DATA[selectedStudent] || STUDENTS_DATA.alyssa;

  // Database Cacciatori DMHA
  const HUNTERS_DATA = {
    alyssa: {
      name: 'Alyssa Douglas',
      rank: 'Rango A',
      rankBg: 'rgba(30, 58, 138, 0.5)',
      rankColor: '#7dd3fc',
      role: 'Healer & Supporto di Campo',
      squad: 'Douglas Vanguard / Seven Hills Fireteam',
      credits: 4850,
      specialty: 'Medicina da Campo, Terapie Anti-Miasma & Incanti Rigenerativi'
    },
    jasper: {
      name: 'Jasper Douglas',
      rank: 'Rango A',
      rankBg: 'rgba(30, 58, 138, 0.5)',
      rankColor: '#7dd3fc',
      role: 'Technomancer & Netrunner Tattico',
      squad: 'Douglas Vanguard / Seven Hills Fireteam',
      credits: 3600,
      specialty: 'Cyber-Tracciamento Rift, Dispositivi Anti-Interferenza & Katana di Vetro di Drago'
    },
    malachia: {
      name: 'Malachia Douglas',
      rank: 'Rango S',
      rankBg: 'rgba(159, 18, 57, 0.5)',
      rankColor: '#fda4af',
      role: 'Apex Berserker / Assaltatore Primario',
      squad: 'Seven Hills Apex Strike Force',
      credits: 9200,
      specialty: 'Neutralizzazione Minacce Classe S, Breccia nei Rift & Caccia ai Capi Branco'
    },
    ukiyo: {
      name: 'Team Ukiyo (Radek, Goran, Kian)',
      rank: 'Rango S / A',
      rankBg: 'rgba(88, 28, 135, 0.5)',
      rankColor: '#d8b4fe',
      role: 'Dungeon Crawler Elite Trio',
      squad: 'Team Ukiyo (Cable District HQ)',
      credits: 8400,
      specialty: 'Vanguard Orc DPS (Radek), Minotaur Tank (Goran), Half-Elf Mana Sniper (Kian)'
    },
    noah: {
      name: 'Noah Douglas',
      rank: 'Rango B',
      rankBg: 'rgba(120, 53, 15, 0.5)',
      rankColor: '#fde68a',
      role: 'Logistica & Field Coordinator',
      squad: 'Douglas Vanguard Support',
      credits: 2100,
      specialty: 'Coordinamento Squadre, Negoziazione con Autorità Civili & Mappe Tattiche'
    }
  };

  const hunterData = HUNTERS_DATA[selectedHunter] || HUNTERS_DATA.alyssa;

  const GUILD_MISSIONS = [
    {
      id: 'hunt_bay',
      title: 'Pattugliamento: Baia di Blackwood',
      rank: 'Rango C',
      reward: '350 Crediti · 2x Frammenti Abissali',
      desc: 'Scansione anomalie termiche e bonifica mostri minori vicino ai vecchi magazzini fluviali.'
    },
    {
      id: 'hunt_cable',
      title: 'Bonifica Condotti (Cable District)',
      rank: 'Rango D',
      reward: '180 Crediti · 1x Cassa Ricambi',
      desc: 'Segnalazione pervenuta dalle officine Ironhorn Nomads di Marek per infiltrazioni nel seminterrato.'
    },
    {
      id: 'hunt_hex',
      title: 'Scorta Carovana verso Hex Valley',
      rank: 'Rango C',
      reward: '500 Crediti · Runa d\\'Argento',
      desc: 'Scorta armata per trasporto rifornimenti tra campus SUCC, CUMS e la valle agricola di Solarton.'
    },
    {
      id: 'hunt_apex',
      title: 'Incursione Rift: Apex Trial Prof. 3',
      rank: 'Rango B/S',
      reward: '1.200 Crediti · 1x Abyssal Core Raro',
      desc: 'Trial sotterraneo ad alta densità di miasma. Consigliata squadra con Heavy Tank e supporto medico.'
    }
  ];

  // Feed SUCCbook
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

  // Stringa luna compatta per notch
  const compactMoon = isFullMoon ? '🌕 Piena' : '🌙 ' + (moonPhase.includes('Calante') ? 'Calante' : moonPhase.includes('Crescente') ? 'Crescente' : moonPhase.split(' ')[0] || 'Luna');

  return (
    <div style={{ width: '100%', maxWidth: '390px', margin: '0 auto', fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif', color: '#f4f4f5' }}>
      
      {/* SCOCCA SMARTPHONE CON BORDO DARK ELEGANTE */}
      <div style={{ background: '#09090b', border: '1px solid #27272a', borderRadius: '26px', padding: '12px', boxShadow: '0 20px 40px -15px rgba(0,0,0,0.8)' }}>
        
        {/* TOP STATUS BAR REALISTICA */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '2px 4px 10px 4px', borderBottom: '1px solid #18181b', fontSize: '11px', color: '#a1a1aa' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span style={{ fontWeight: 'bold', color: '#f4f4f5' }}>08:24</span>
            <span style={{ fontSize: '9px', padding: '1px 5px', background: '#18181b', color: '#34d399', borderRadius: '4px', border: '1px solid #27272a' }}>5G DCC</span>
          </div>

          {/* DYNAMIC ISLAND SU RIGA SINGOLA */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '3px 10px', background: '#121215', border: '1px solid #27272a', borderRadius: '9999px', fontSize: '10px', whiteSpace: 'nowrap' }}>
            <span>{compactMoon}</span>
            <span style={{ color: '#52525b' }}>·</span>
            <span style={{ color: suppressors <= 1 ? '#f87171' : '#34d399', fontWeight: 'bold' }}>🧪 x{suppressors}</span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '4px', fontSize: '10px' }}>
            <span>📶</span>
            <span>🛜</span>
            <span style={{ color: '#34d399', fontWeight: 'bold' }}>98%</span>
          </div>
        </div>

        {/* ========================================================================= */}
        {/* SCHERMATA 1: HOME DASHBOARD                                               */}
        {/* ========================================================================= */}
        {activeApp === 'home' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '11px', marginTop: '10px' }}>
            
            {/* WIDGET CLOCK & WORLD ENVIRONMENT */}
            <div style={{ background: 'linear-gradient(135deg, #18181b 0%, #0d0d0f 100%)', border: '1px solid #27272a', borderRadius: '16px', padding: '12px 14px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '11px', color: '#a1a1aa', marginBottom: '2px' }}>
                <span>Venerdì, 5 Aprile 2024</span>
                <span style={{ padding: '2px 8px', background: '#27272a', borderRadius: '9999px', fontSize: '9px', textTransform: 'capitalize', color: '#e4e4e7' }}>{sessionMode}</span>
              </div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginTop: '4px' }}>
                <div>
                  <div style={{ fontSize: '26px', fontWeight: 900, color: '#ffffff', letterSpacing: '-0.5px', lineHeight: 1 }}>
                    08:24 <span style={{ fontSize: '11px', fontWeight: 400, color: '#71717a' }}>PST</span>
                  </div>
                  <div style={{ fontSize: '11px', color: '#a1a1aa', marginTop: '4px', display: 'flex', gap: '6px' }}>
                    <span>{isNight ? '🌃 Notte' : '☀️ Mattina'}</span>
                    <span style={{ color: '#52525b' }}>·</span>
                    <span style={{ color: '#fbbf24', fontWeight: 500 }}>{moonPhase}</span>
                  </div>
                </div>
                <div style={{ padding: '4px 8px', background: 'rgba(30, 58, 138, 0.4)', border: '1px solid rgba(59, 130, 246, 0.3)', borderRadius: '9999px', fontSize: '10px', color: '#7dd3fc', fontFamily: 'monospace' }}>
                  Rift: {riftAlert}
                </div>
              </div>
            </div>

            {/* WIDGET RAPIDI BIOTRACK & REPUTAZIONE */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
              <div style={{ background: '#121215', border: '1px solid #27272a', borderRadius: '14px', padding: '10px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                <div>
                  <div style={{ fontSize: '10px', color: '#a1a1aa', textTransform: 'uppercase', fontWeight: 600, letterSpacing: '0.5px' }}>Biologia LSE</div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '4px' }}>
                    <span style={{ fontSize: '13px', fontWeight: 'bold', color: '#f4f4f5' }}>{lseStatus}</span>
                    <span style={{ fontSize: '10px', color: '#71717a' }}>Peak -{daysLeft}d</span>
                  </div>
                </div>
                <button
                  onClick={handleUseSuppressor}
                  disabled={suppressors <= 0}
                  style={{
                    marginTop: '8px',
                    width: '100%',
                    padding: '6px 4px',
                    background: suppressors > 0 ? '#14532d' : '#18181b',
                    border: '1px solid ' + (suppressors > 0 ? '#16a34a' : '#27272a'),
                    borderRadius: '8px',
                    color: suppressors > 0 ? '#86efac' : '#71717a',
                    fontSize: '10px',
                    fontWeight: 600,
                    cursor: suppressors > 0 ? 'pointer' : 'not-allowed'
                  }}
                >
                  {suppressors > 0 ? '+ Inala Soppressore' : 'Esauriti! (Allerta)'}
                </button>
              </div>

              <div style={{ background: '#121215', border: '1px solid #27272a', borderRadius: '14px', padding: '10px', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                <div>
                  <div style={{ fontSize: '10px', color: '#a1a1aa', textTransform: 'uppercase', fontWeight: 600, letterSpacing: '0.5px' }}>Branco Douglas</div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: '4px' }}>
                    <span style={{ fontSize: '13px', fontWeight: 'bold', color: '#fbbf24' }}>DCC Clan</span>
                    <span style={{ fontSize: '10px', color: '#a1a1aa', fontFamily: 'monospace' }}>{packRep}/100</span>
                  </div>
                </div>
                <div style={{ marginTop: '8px' }}>
                  <div style={{ width: '100%', background: '#27272a', height: '6px', borderRadius: '9999px', overflow: 'hidden' }}>
                    <div style={{ width: packRep + '%', background: '#f59e0b', height: '100%', borderRadius: '9999px' }}></div>
                  </div>
                </div>
              </div>
            </div>

            {/* GRIGLIA APPLICAZIONI SMARTPHONE */}
            <div style={{ marginTop: '2px' }}>
              <div style={{ fontSize: '10px', fontWeight: 600, color: '#a1a1aa', textTransform: 'uppercase', letterSpacing: '0.6px', marginBottom: '8px', paddingLeft: '2px' }}>
                Applicazioni Installate
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '9px' }}>
                
                {/* 1. Telegram */}
                <button
                  onClick={() => { setActiveApp('telegram'); setTelegramUnread(0); }}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '9px 2px', background: '#121215', border: '1px solid #27272a', borderRadius: '16px', cursor: 'pointer' }}
                >
                  <div style={{ position: 'relative', width: '38px', height: '38px', borderRadius: '12px', background: 'linear-gradient(135deg, #0284c7, #38bdf8)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '18px', marginBottom: '5px' }}>
                    💬
                    {telegramUnread > 0 && (
                      <span style={{ position: 'absolute', top: '-4px', right: '-4px', background: '#ef4444', color: '#fff', fontSize: '9px', fontWeight: 'bold', width: '16px', height: '16px', borderRadius: '9999px', display: 'flex', alignItems: 'center', justifyContent: 'center', border: '2px solid #09090b' }}>
                        {telegramUnread}
                      </span>
                    )}
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 500, color: '#e4e4e7' }}>Telegram</span>
                </button>

                {/* 2. Accademia */}
                <button
                  onClick={() => setActiveApp('academics')}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '9px 2px', background: '#121215', border: '1px solid #27272a', borderRadius: '16px', cursor: 'pointer' }}
                >
                  <div style={{ width: '38px', height: '38px', borderRadius: '12px', background: 'linear-gradient(135deg, #4f46e5, #818cf8)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '18px', marginBottom: '5px' }}>
                    🎓
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 500, color: '#e4e4e7' }}>Accademia</span>
                </button>

                {/* 3. DMHA Gilda */}
                <button
                  onClick={() => setActiveApp('guild')}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '9px 2px', background: '#121215', border: '1px solid #27272a', borderRadius: '16px', cursor: 'pointer' }}
                >
                  <div style={{ width: '38px', height: '38px', borderRadius: '12px', background: 'linear-gradient(135deg, #b91c1c, #f59e0b)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '18px', marginBottom: '5px' }}>
                    ⚔️
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 500, color: '#e4e4e7' }}>DMHA Gilda</span>
                </button>

                {/* 4. BioTrack LSE */}
                <button
                  onClick={() => setActiveApp('biotrack')}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '9px 2px', background: '#121215', border: '1px solid #27272a', borderRadius: '16px', cursor: 'pointer' }}
                >
                  <div style={{ width: '38px', height: '38px', borderRadius: '12px', background: 'linear-gradient(135deg, #059669, #34d399)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '18px', marginBottom: '5px' }}>
                    🐾
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 500, color: '#e4e4e7' }}>BioTrack</span>
                </button>

                {/* 5. SUCCbook */}
                <button
                  onClick={() => { setActiveApp('succbook'); setSuccbookUnread(0); }}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '9px 2px', background: '#121215', border: '1px solid #27272a', borderRadius: '16px', cursor: 'pointer' }}
                >
                  <div style={{ position: 'relative', width: '38px', height: '38px', borderRadius: '12px', background: 'linear-gradient(135deg, #1d4ed8, #06b6d4)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '18px', marginBottom: '5px' }}>
                    🌐
                    {succbookUnread > 0 && (
                      <span style={{ position: 'absolute', top: '-4px', right: '-4px', background: '#ef4444', color: '#fff', fontSize: '9px', fontWeight: 'bold', width: '16px', height: '16px', borderRadius: '9999px', display: 'flex', alignItems: 'center', justifyContent: 'center', border: '2px solid #09090b' }}>
                        {succbookUnread}
                      </span>
                    )}
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 500, color: '#e4e4e7' }}>SUCCbook</span>
                </button>

                {/* 6. Echo Audio */}
                <button
                  onClick={() => setActiveApp('music')}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '9px 2px', background: '#121215', border: '1px solid #27272a', borderRadius: '16px', cursor: 'pointer' }}
                >
                  <div style={{ width: '38px', height: '38px', borderRadius: '12px', background: 'linear-gradient(135deg, #10b981, #047857)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '18px', marginBottom: '5px' }}>
                    🎵
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 500, color: '#e4e4e7' }}>Echo Audio</span>
                </button>

                {/* 7. CUMS Arena */}
                <button
                  onClick={() => { setActiveApp('academics'); setSelectedStudent('cums_students'); }}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '9px 2px', background: '#121215', border: '1px solid #27272a', borderRadius: '16px', cursor: 'pointer' }}
                >
                  <div style={{ width: '38px', height: '38px', borderRadius: '12px', background: 'linear-gradient(135deg, #6d28d9, #ec4899)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '18px', marginBottom: '5px' }}>
                    🔮
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 500, color: '#e4e4e7' }}>CUMS</span>
                </button>

                {/* 8. Team Ukiyo */}
                <button
                  onClick={() => { setActiveApp('guild'); setSelectedHunter('ukiyo'); }}
                  style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '9px 2px', background: '#121215', border: '1px solid #27272a', borderRadius: '16px', cursor: 'pointer' }}
                >
                  <div style={{ width: '38px', height: '38px', borderRadius: '12px', background: 'linear-gradient(135deg, #b45309, #eab308)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '18px', marginBottom: '5px' }}>
                    🏍️
                  </div>
                  <span style={{ fontSize: '10px', fontWeight: 500, color: '#e4e4e7' }}>Ukiyo</span>
                </button>
              </div>
            </div>

            {/* MINI AUDIO WIDGET IN HOME */}
            <div style={{ padding: '9px 12px', background: '#121215', border: '1px solid #27272a', borderRadius: '14px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', overflow: 'hidden' }}>
                <span style={{ fontSize: '16px' }}>📻</span>
                <div style={{ overflow: 'hidden', whiteSpace: 'nowrap' }}>
                  <div style={{ fontSize: '11px', fontWeight: 600, color: '#f4f4f5', overflow: 'hidden', textOverflow: 'ellipsis' }}>{activeTrack.title}</div>
                  <div style={{ fontSize: '9px', color: '#71717a', overflow: 'hidden', textOverflow: 'ellipsis' }}>{activeTrack.artist}</div>
                </div>
              </div>
              <button
                onClick={() => setMusicPlaying(!musicPlaying)}
                style={{ padding: '4px 10px', background: '#27272a', border: '1px solid #3f3f46', borderRadius: '8px', fontSize: '10px', fontWeight: 600, color: '#f4f4f5', cursor: 'pointer' }}
              >
                {musicPlaying ? '⏸ Pausa' : '▶ Play'}
              </button>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 2: TELEGRAM                                                    */}
        {/* ========================================================================= */}
        {activeApp === 'telegram' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '6px' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingBottom: '8px', borderBottom: '1px solid #1f1f23' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <button
                  onClick={() => setActiveApp('home')}
                  style={{ background: '#27272a', border: 'none', color: '#f4f4f5', borderRadius: '6px', padding: '3px 8px', fontSize: '11px', cursor: 'pointer', fontWeight: 600 }}
                >
                  ⬅ Home
                </button>
                <div>
                  <div style={{ fontSize: '12px', fontWeight: 'bold', color: '#ffffff', display: 'flex', alignItems: 'center', gap: '5px' }}>
                    🐺 Douglas Pack Chat
                  </div>
                  <div style={{ fontSize: '9px', color: '#71717a' }}>Canale Criptato DCC · 6 membri connessi</div>
                </div>
              </div>
            </div>

            <div style={{ height: '260px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '7px', paddingRight: '2px' }}>
              {messages.map(m => (
                <div key={m.id} style={{ background: '#121215', border: '1px solid #27272a', borderRadius: '12px', padding: '8px 10px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '3px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                      <span style={{ fontSize: '11px', fontWeight: 'bold', color: m.color }}>{m.sender}</span>
                      <span style={{ fontSize: '8px', padding: '1px 5px', borderRadius: '4px', background: m.badgeBg, border: '1px solid ' + m.badgeBorder, color: m.color }}>{m.role}</span>
                    </div>
                    <span style={{ fontSize: '9px', color: '#71717a', fontFamily: 'monospace' }}>{m.time}</span>
                  </div>
                  <p style={{ fontSize: '11px', color: '#e4e4e7', lineHeight: '1.4', margin: 0 }}>{m.text}</p>
                </div>
              ))}
            </div>

            <div style={{ display: 'flex', gap: '6px', alignItems: 'center', paddingTop: '2px' }}>
              <input
                type="text"
                placeholder="Scrivi messaggio al branco..."
                value={chatInput}
                onChange={val => setChatInput(typeof val === 'object' && val && val.target ? val.target.value : val)}
                style={{ flex: 1, background: '#121215', border: '1px solid #27272a', borderRadius: '10px', padding: '7px 10px', fontSize: '11px', color: '#ffffff', outline: 'none' }}
              />
              <button
                onClick={handleSendMessage}
                style={{ background: '#0284c7', border: 'none', borderRadius: '10px', padding: '7px 13px', fontSize: '11px', fontWeight: 600, color: '#ffffff', cursor: 'pointer' }}
              >
                Invia
              </button>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 3: ACCADEMIA (SUCC & CUMS)                                      */}
        {/* ========================================================================= */}
        {activeApp === 'academics' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '6px' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingBottom: '6px', borderBottom: '1px solid #1f1f23' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <button
                  onClick={() => setActiveApp('home')}
                  style={{ background: '#27272a', border: 'none', color: '#f4f4f5', borderRadius: '6px', padding: '3px 8px', fontSize: '11px', cursor: 'pointer', fontWeight: 600 }}
                >
                  ⬅ Home
                </button>
                <div style={{ fontSize: '12px', fontWeight: 'bold', color: '#ffffff' }}>🎓 Portale Universitario</div>
              </div>
            </div>

            {/* SELETTORE STUDENTI PILLS BEN SPAZIATI */}
            <div style={{ display: 'flex', gap: '5px', overflowX: 'auto', paddingBottom: '4px' }}>
              {[
                { id: 'alyssa', label: 'Alyssa' },
                { id: 'jasper', label: 'Jasper' },
                { id: 'noah', label: 'Noah' },
                { id: 'malachia', label: 'Malachia' },
                { id: 'cums_students', label: 'CUMS Arcani' }
              ].map(s => {
                const isSel = selectedStudent === s.id;
                return (
                  <button
                    key={s.id}
                    onClick={() => setSelectedStudent(s.id)}
                    style={{
                      padding: '4px 10px',
                      borderRadius: '9999px',
                      fontSize: '10px',
                      fontWeight: isSel ? 700 : 500,
                      background: isSel ? '#4f46e5' : '#18181b',
                      color: isSel ? '#ffffff' : '#a1a1aa',
                      border: '1px solid ' + (isSel ? '#6366f1' : '#27272a'),
                      cursor: 'pointer',
                      whiteSpace: 'nowrap'
                    }}
                  >
                    {s.label}
                  </button>
                );
              })}
            </div>

            {/* SCHEDA STUDENTE */}
            <div style={{ background: '#121215', border: '1px solid #27272a', borderRadius: '14px', padding: '12px', display: 'flex', flexDirection: 'column', gap: '9px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <div style={{ fontSize: '13px', fontWeight: 'bold', color: '#ffffff' }}>{studentData.name}</div>
                  <div style={{ fontSize: '10px', color: '#a1a1aa', marginTop: '1px' }}>{studentData.major}</div>
                  <div style={{ fontSize: '9px', color: '#818cf8', marginTop: '2px' }}>{studentData.school} · {studentData.dept}</div>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <div style={{ fontSize: '15px', fontWeight: 900, color: '#34d399', fontFamily: 'monospace' }}>{studentData.gpa}</div>
                  <div style={{ fontSize: '8px', color: '#71717a', textTransform: 'uppercase' }}>GPA / MEDIA</div>
                </div>
              </div>

              {/* BARRA CREDITI */}
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '10px', color: '#a1a1aa', marginBottom: '3px' }}>
                  <span>CFU: <strong style={{ color: '#fff' }}>{studentData.credits}</strong> / 180</span>
                  <span>{Math.round((studentData.credits / 180) * 100)}%</span>
                </div>
                <div style={{ width: '100%', background: '#27272a', height: '5px', borderRadius: '9999px', overflow: 'hidden' }}>
                  <div style={{ width: (studentData.credits / 180 * 100) + '%', background: '#6366f1', height: '100%', borderRadius: '9999px' }}></div>
                </div>
              </div>

              {/* TIROCINIO */}
              <div style={{ background: '#09090b', border: '1px solid #1f1f23', borderRadius: '8px', padding: '7px 9px', fontSize: '10px', color: '#d4d4d8' }}>
                <span style={{ color: '#71717a', fontWeight: 'bold' }}>STAGE / TIROCINIO:</span> {studentData.internship}
              </div>

              {/* LISTA CORSI */}
              <div style={{ marginTop: '2px' }}>
                <div style={{ fontSize: '10px', fontWeight: 600, color: '#a1a1aa', textTransform: 'uppercase', marginBottom: '6px' }}>
                  Corsi Iscritti & Valutazioni
                </div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
                  {studentData.courses.map((c, i) => (
                    <div key={i} style={{ background: '#09090b', border: '1px solid #1f1f23', borderRadius: '8px', padding: '6px 9px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <div>
                        <div style={{ fontSize: '11px', fontWeight: 500, color: '#f4f4f5' }}>{c.name}</div>
                        <div style={{ fontSize: '9px', color: '#71717a', fontFamily: 'monospace' }}>{c.code} · Prof. {c.prof} · {c.cfu} CFU</div>
                      </div>
                      <span style={{ fontSize: '10px', fontWeight: 'bold', fontFamily: 'monospace', padding: '2px 6px', background: 'rgba(5, 150, 105, 0.2)', border: '1px solid #059669', color: '#6ee7b7', borderRadius: '4px' }}>
                        {c.grade}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 4: REGISTRO GILDA DMHA                                          */}
        {/* ========================================================================= */}
        {activeApp === 'guild' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '6px' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingBottom: '6px', borderBottom: '1px solid #1f1f23' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <button
                  onClick={() => setActiveApp('home')}
                  style={{ background: '#27272a', border: 'none', color: '#f4f4f5', borderRadius: '6px', padding: '3px 8px', fontSize: '11px', cursor: 'pointer', fontWeight: 600 }}
                >
                  ⬅ Home
                </button>
                <div style={{ fontSize: '12px', fontWeight: 'bold', color: '#ffffff' }}>⚔️ Registro Gilda DMHA</div>
              </div>
            </div>

            {/* SELETTORE CACCIATORE */}
            <div style={{ display: 'flex', gap: '5px', overflowX: 'auto', paddingBottom: '4px' }}>
              {[
                { id: 'alyssa', label: 'Alyssa' },
                { id: 'jasper', label: 'Jasper' },
                { id: 'malachia', label: 'Malachia' },
                { id: 'ukiyo', label: 'Team Ukiyo' },
                { id: 'noah', label: 'Noah' }
              ].map(h => {
                const isSel = selectedHunter === h.id;
                return (
                  <button
                    key={h.id}
                    onClick={() => setSelectedHunter(h.id)}
                    style={{
                      padding: '4px 10px',
                      borderRadius: '9999px',
                      fontSize: '10px',
                      fontWeight: isSel ? 700 : 500,
                      background: isSel ? '#b91c1c' : '#18181b',
                      color: isSel ? '#ffffff' : '#a1a1aa',
                      border: '1px solid ' + (isSel ? '#dc2626' : '#27272a'),
                      cursor: 'pointer',
                      whiteSpace: 'nowrap'
                    }}
                  >
                    {h.label}
                  </button>
                );
              })}
            </div>

            {/* SCHEDA PROFILO CACCIATORE */}
            <div style={{ background: '#121215', border: '1px solid #27272a', borderRadius: '14px', padding: '10px', display: 'flex', flexDirection: 'column', gap: '7px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                <div>
                  <div style={{ fontSize: '13px', fontWeight: 'bold', color: '#ffffff' }}>{hunterData.name}</div>
                  <div style={{ fontSize: '10px', color: '#a1a1aa' }}>{hunterData.role}</div>
                  <div style={{ fontSize: '9px', color: '#71717a' }}>{hunterData.squad}</div>
                </div>
                <div style={{ textAlign: 'right' }}>
                  <span style={{ fontSize: '10px', fontWeight: 'bold', fontFamily: 'monospace', padding: '2px 7px', background: hunterData.rankBg, color: hunterData.rankColor, borderRadius: '4px', border: '1px solid ' + hunterData.rankColor }}>
                    {hunterData.rank}
                  </span>
                  <div style={{ fontSize: '10px', color: '#fbbf24', fontFamily: 'monospace', marginTop: '3px' }}>{hunterData.credits} Crediti</div>
                </div>
              </div>
              <div style={{ background: '#09090b', border: '1px solid #1f1f23', borderRadius: '8px', padding: '6px 8px', fontSize: '10px', color: '#d4d4d8' }}>
                <span style={{ color: '#71717a', fontWeight: 'bold' }}>SPECIALITÀ:</span> {hunterData.specialty}
              </div>
            </div>

            {/* BACHECA INCARICHI */}
            <div style={{ marginTop: '2px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '10px', fontWeight: 600, color: '#a1a1aa', textTransform: 'uppercase', marginBottom: '6px' }}>
                <span>Bacheca Incarichi di Bonifica</span>
                <span style={{ color: '#71717a' }}>Rift & Territorio</span>
              </div>
              <div style={{ height: '170px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '6px', paddingRight: '2px' }}>
                {GUILD_MISSIONS.map(m => {
                  const isAccepted = acceptedMissionId === m.id;
                  return (
                    <div key={m.id} style={{ background: isAccepted ? 'rgba(120, 53, 15, 0.2)' : '#121215', border: '1px solid ' + (isAccepted ? '#b45309' : '#27272a'), borderRadius: '10px', padding: '8px 10px' }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2px' }}>
                        <span style={{ fontSize: '11px', fontWeight: 'bold', color: '#f4f4f5' }}>{m.title}</span>
                        <span style={{ fontSize: '9px', padding: '1px 5px', background: '#27272a', borderRadius: '4px', color: '#d4d4d8', fontFamily: 'monospace' }}>{m.rank}</span>
                      </div>
                      <p style={{ fontSize: '10px', color: '#a1a1aa', margin: '2px 0 5px 0', lineHeight: '1.3' }}>{m.desc}</p>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ fontSize: '10px', color: '#fbbf24', fontFamily: 'monospace' }}>{m.reward}</span>
                        <button
                          onClick={() => setAcceptedMissionId(isAccepted ? null : m.id)}
                          style={{
                            padding: '3px 9px',
                            borderRadius: '6px',
                            fontSize: '10px',
                            fontWeight: 700,
                            background: isAccepted ? '#f59e0b' : '#27272a',
                            color: isAccepted ? '#000000' : '#e4e4e7',
                            border: '1px solid ' + (isAccepted ? '#fbbf24' : '#3f3f46'),
                            cursor: 'pointer'
                          }}
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
        {/* SCHERMATA 5: BIOTRACK LSE                                                */}
        {/* ========================================================================= */}
        {activeApp === 'biotrack' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '6px' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingBottom: '6px', borderBottom: '1px solid #1f1f23' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <button
                  onClick={() => setActiveApp('home')}
                  style={{ background: '#27272a', border: 'none', color: '#f4f4f5', borderRadius: '6px', padding: '3px 8px', fontSize: '11px', cursor: 'pointer', fontWeight: 600 }}
                >
                  ⬅ Home
                </button>
                <div style={{ fontSize: '12px', fontWeight: 'bold', color: '#ffffff' }}>🐾 BioTrack LSE & Monitoraggio Branco</div>
              </div>
            </div>

            <div style={{ background: '#121215', border: '1px solid #27272a', borderRadius: '14px', padding: '12px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <div style={{ fontSize: '12px', fontWeight: 'bold', color: '#ffffff' }}>Stato Biologico Ferormonale</div>
                  <div style={{ fontSize: '10px', color: '#a1a1aa' }}>Ciclo Heat / Rut & Livello di Allerta</div>
                </div>
                <span style={{ fontSize: '10px', fontWeight: 'bold', padding: '3px 8px', background: 'rgba(5, 150, 105, 0.25)', border: '1px solid #059669', color: '#6ee7b7', borderRadius: '9999px' }}>
                  {lseStatus}
                </span>
              </div>

              <div style={{ background: '#09090b', border: '1px solid #1f1f23', borderRadius: '10px', padding: '10px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <div style={{ fontSize: '11px', fontWeight: 'bold', color: '#f4f4f5' }}>Cilindri Soppressori Odore DMHA</div>
                  <div style={{ fontSize: '9px', color: '#71717a' }}>Blocca la fuoriuscita ferormonale in pubblico</div>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <span style={{ fontSize: '14px', fontWeight: 900, fontFamily: 'monospace', color: suppressors <= 1 ? '#f87171' : '#34d399' }}>
                    x{suppressors}
                  </span>
                  <button
                    onClick={handleUseSuppressor}
                    disabled={suppressors <= 0}
                    style={{
                      padding: '5px 10px',
                      background: suppressors > 0 ? '#15803d' : '#27272a',
                      border: 'none',
                      borderRadius: '8px',
                      fontSize: '10px',
                      fontWeight: 'bold',
                      color: '#ffffff',
                      cursor: suppressors > 0 ? 'pointer' : 'not-allowed'
                    }}
                  >
                    Inala Dose
                  </button>
                </div>
              </div>

              <div style={{ background: '#09090b', border: '1px solid #1f1f23', borderRadius: '10px', padding: '10px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                  <span style={{ fontSize: '11px', fontWeight: 'bold', color: '#fbbf24' }}>🌙 {moonPhase}</span>
                  <span style={{ fontSize: '9px', fontWeight: 'bold', padding: '1px 6px', background: isFullMoon ? 'rgba(120, 53, 15, 0.5)' : '#18181b', color: isFullMoon ? '#fde68a' : '#a1a1aa', border: '1px solid ' + (isFullMoon ? '#b45309' : '#27272a'), borderRadius: '4px' }}>
                    {isFullMoon ? 'BUFF ATTIVO (+2 MGT/RES, +1 AGI)' : 'Influsso Standard'}
                  </span>
                </div>
                <p style={{ fontSize: '10px', color: '#a1a1aa', margin: 0, lineHeight: '1.4' }}>
                  Lupine Social Ecology: durante la luna piena, l\\'olfatto, la sensibilità ai ferormoni di branco e la risposta all\\'Alpha Command risultano massimizzati.
                </p>
              </div>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 6: SUCCBOOK                                                     */}
        {/* ========================================================================= */}
        {activeApp === 'succbook' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '6px' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingBottom: '6px', borderBottom: '1px solid #1f1f23' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <button
                  onClick={() => setActiveApp('home')}
                  style={{ background: '#27272a', border: 'none', color: '#f4f4f5', borderRadius: '6px', padding: '3px 8px', fontSize: '11px', cursor: 'pointer', fontWeight: 600 }}
                >
                  ⬅ Home
                </button>
                <div style={{ fontSize: '12px', fontWeight: 'bold', color: '#ffffff' }}>🌐 SUCCbook · Campus Social Network</div>
              </div>
            </div>

            <div style={{ height: '260px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '8px', paddingRight: '2px' }}>
              {feedPosts.map(p => (
                <div key={p.id} style={{ background: '#121215', border: '1px solid #27272a', borderRadius: '12px', padding: '10px', display: 'flex', flexDirection: 'column', gap: '6px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <span style={{ fontSize: '16px' }}>{p.avatar}</span>
                    <div>
                      <div style={{ fontSize: '11px', fontWeight: 'bold', color: '#f4f4f5', display: 'flex', alignItems: 'center', gap: '5px' }}>
                        {p.author}
                        <span style={{ fontSize: '8px', padding: '1px 4px', background: 'rgba(30, 58, 138, 0.4)', color: '#38bdf8', borderRadius: '4px' }}>{p.badge}</span>
                      </div>
                      <div style={{ fontSize: '9px', color: '#71717a' }}>{p.handle} · {p.time}</div>
                    </div>
                  </div>
                  <p style={{ fontSize: '11px', color: '#d4d4d8', margin: 0, lineHeight: '1.4' }}>{p.text}</p>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: '4px', borderTop: '1px solid #1f1f23', fontSize: '10px' }}>
                    <button
                      onClick={() => toggleLike(p.id)}
                      style={{ display: 'flex', alignItems: 'center', gap: '4px', background: 'transparent', border: 'none', color: p.liked ? '#fb7185' : '#a1a1aa', fontWeight: p.liked ? 'bold' : 'normal', cursor: 'pointer', padding: 0 }}
                    >
                      <span>{p.liked ? '❤️' : '🤍'}</span>
                      <span>{p.likes} Mi piace</span>
                    </button>
                    <span style={{ color: '#52525b' }}>Condividi</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* SCHERMATA 7: ECHO AUDIO MOOD                                              */}
        {/* ========================================================================= */}
        {activeApp === 'music' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '6px' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingBottom: '6px', borderBottom: '1px solid #1f1f23' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <button
                  onClick={() => setActiveApp('home')}
                  style={{ background: '#27272a', border: 'none', color: '#f4f4f5', borderRadius: '6px', padding: '3px 8px', fontSize: '11px', cursor: 'pointer', fontWeight: 600 }}
                >
                  ⬅ Home
                </button>
                <div style={{ fontSize: '12px', fontWeight: 'bold', color: '#ffffff' }}>🎵 Echo Music Mood Speaker</div>
              </div>
            </div>

            <div style={{ background: '#121215', border: '1px solid #27272a', borderRadius: '14px', padding: '14px', textAlign: 'center', display: 'flex', flexDirection: 'column', gap: '8px' }}>
              <div style={{ width: '56px', height: '56px', margin: '0 auto', borderRadius: '14px', background: 'linear-gradient(135deg, #059669, #10b981)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '26px' }}>
                📻
              </div>
              <div>
                <div style={{ fontSize: '13px', fontWeight: 'bold', color: '#ffffff' }}>{activeTrack.title}</div>
                <div style={{ fontSize: '10px', color: '#a1a1aa' }}>{activeTrack.artist}</div>
                <div style={{ fontSize: '9px', color: '#34d399', fontFamily: 'monospace', marginTop: '2px' }}>Mood: {activeTrack.mood}</div>
              </div>

              <div style={{ display: 'flex', justifyContent: 'center', marginTop: '4px' }}>
                <button
                  onClick={() => setMusicPlaying(!musicPlaying)}
                  style={{ padding: '6px 18px', background: '#059669', border: 'none', borderRadius: '10px', fontSize: '11px', fontWeight: 'bold', color: '#ffffff', cursor: 'pointer' }}
                >
                  {musicPlaying ? '⏸ Pausa' : '▶ Play'}
                </button>
              </div>

              <div style={{ textAlign: 'left', marginTop: '6px' }}>
                <div style={{ fontSize: '10px', fontWeight: 600, color: '#a1a1aa', textTransform: 'uppercase', marginBottom: '5px' }}>Preset Mood Famiglio</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                  {[
                    { title: 'Subterranean Bass Drive', artist: 'Echo · DCC Net', mood: 'Dungeon Synth / Focus' },
                    { title: 'Villa Douglas Midnight Hearth', artist: 'Acoustic Yarrow', mood: 'Relax & Intimacy' },
                    { title: 'Rift Hazard: Apex Berserker', artist: 'Industrial Silver-Tech', mood: 'High Adrenaline Combat' },
                    { title: 'Solarton Coffeehouse Vibe', artist: 'Le Refuge des Chats', mood: 'Casual Campus Morning' }
                  ].map((tr, idx) => {
                    const isTr = activeTrack.title === tr.title;
                    return (
                      <button
                        key={idx}
                        onClick={() => { setActiveTrack(tr); setMusicPlaying(true); }}
                        style={{
                          width: '100%',
                          padding: '6px 8px',
                          borderRadius: '8px',
                          textAlign: 'left',
                          fontSize: '10px',
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center',
                          background: isTr ? 'rgba(5, 150, 105, 0.25)' : '#09090b',
                          border: '1px solid ' + (isTr ? '#059669' : '#1f1f23'),
                          color: isTr ? '#6ee7b7' : '#a1a1aa',
                          fontWeight: isTr ? 'bold' : 'normal',
                          cursor: 'pointer'
                        }}
                      >
                        <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{tr.title}</span>
                        <span style={{ fontSize: '8px', opacity: 0.7, fontFamily: 'monospace' }}>{tr.mood}</span>
                      </button>
                    );
                  })}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* ========================================================================= */}
        {/* BOTTOM DOCK BAR DEFINITIVA (MAI PIÙ TESTO ACCAVALLATO)                     */}
        {/* ========================================================================= */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-around', marginTop: '12px', paddingTop: '8px', paddingBottom: '2px', borderTop: '1px solid #1f1f23', background: '#09090b' }}>
          {[
            { id: 'home', label: 'Home', icon: '🏠', activeColor: '#ffffff' },
            { id: 'telegram', label: 'Chat', icon: '💬', activeColor: '#38bdf8', badge: telegramUnread },
            { id: 'academics', label: 'Studio', icon: '🎓', activeColor: '#818cf8' },
            { id: 'guild', label: 'Gilda', icon: '⚔️', activeColor: '#f87171' },
            { id: 'biotrack', label: 'LSE', icon: '🐾', activeColor: '#34d399' }
          ].map(tab => {
            const isTab = activeApp === tab.id;
            return (
              <button
                key={tab.id}
                onClick={() => {
                  setActiveApp(tab.id);
                  if (tab.id === 'telegram') setTelegramUnread(0);
                }}
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  flex: 1,
                  background: 'transparent',
                  border: 'none',
                  cursor: 'pointer',
                  padding: '3px 2px',
                  gap: '2px',
                  position: 'relative'
                }}
              >
                <span style={{ fontSize: '18px', lineHeight: 1 }}>{tab.icon}</span>
                <span style={{ fontSize: '10px', fontWeight: isTab ? 700 : 400, color: isTab ? tab.activeColor : '#71717a', lineHeight: 1.2 }}>
                  {tab.label}
                </span>
                {tab.badge && tab.badge > 0 ? (
                  <span style={{ position: 'absolute', top: '0px', right: '14px', width: '7px', height: '7px', borderRadius: '9999px', background: '#ef4444' }}></span>
                ) : null}
              </button>
            );
          })}
        </div>

      </div>
    </div>
  );
}`;

async function deployPerfectedPanel() {
  let token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const engineId = 'engine_HCTPXhL8xr89wUY9r9dYU';

  console.log('1. Recupero engine live da Wyvern...');
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

  def.ui_panels = [
    {
      id: 'panel_smartphone_os',
      name: 'Svartulfr Smartphone OS',
      icon: 'layout',
      placement: 'sidebar',
      target: 'both',
      enabled: true,
      code: perfectedSmartphoneCode
    }
  ];

  console.log('\n2. Salvataggio Story Engine con layout e stile perfezionati...');
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

  // Aggiorna l'export locale
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
  console.log(`Export locale aggiornato: ${exportPath}`);
}

deployPerfectedPanel();

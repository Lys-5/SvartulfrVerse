import React, { useState } from 'react';

export default function Panel({ engine }: { engine: any }) {
  // Navigazione app: 'home' | 'telegram' | 'academics' | 'guild' | 'biotrack' | 'succbook' | 'music'
  const [activeApp, setActiveApp] = useState<string>('home');

  // Valori del motore live
  const values = engine.values || {};
  const moonPhase = String(values.moon_phase || 'Ultimo Quarto Calante');
  const isFullMoon = Boolean(values.moon_full_active);
  const isNight = Boolean(values.night_active);
  const lseStatus = String(values.lse_biology_status || 'Dormant');
  const daysLeft = Number(values.lse_cycle_days_left ?? 20);
  const suppressors = Number(values.scent_suppressors_count ?? 3);
  const packRep = Number(values.pack_reputation ?? 25);
  const riftAlert = String(values.rift_threat_level || 'Classe 1 - Stabile');

  // Stati interattivi
  const [telegramUnread, setTelegramUnread] = useState<number>(3);
  const [succbookUnread, setSuccbookUnread] = useState<number>(5);
  const [selectedStudent, setSelectedStudent] = useState<string>('alyssa');
  const [selectedHunter, setSelectedHunter] = useState<string>('alyssa');
  const [acceptedMissionId, setAcceptedMissionId] = useState<string | null>(null);
  const [musicPlaying, setMusicPlaying] = useState<boolean>(true);
  const [chatInput, setChatInput] = useState<string>('');
  const [nextMsgId, setNextMsgId] = useState<number>(10);
  const [activeTrack, setActiveTrack] = useState<{ title: string; artist: string; mood: string }>({
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

  // Chat Telegram del Branco Douglas
  const [messages, setMessages] = useState<any[]>([
    {
      id: 1,
      sender: 'Papà (Erik)',
      role: 'Prime Alpha · DCC',
      color: 'text-amber-400',
      badgeClass: 'bg-amber-950 text-amber-300 border border-amber-700',
      text: "Ragazzi, siete arrivati a Solarton? Kaladin ha predisposto la scorta discreta attorno all'ingresso est del campus. Non dimenticate i soppressori.",
      time: '08:02'
    },
    {
      id: 2,
      sender: 'Noah',
      role: 'Beta · PR',
      color: 'text-sky-400',
      badgeClass: 'bg-sky-950 text-sky-300 border border-sky-700',
      text: 'Tranquillo Boss, sono già al banchetto matricole SUCC. Se Alyssa ritarda è perché doveva abbinare le scarpe alla borsa medica 💅',
      time: '08:05'
    },
    {
      id: 3,
      sender: 'Jasper',
      role: 'Technomancer',
      color: 'text-emerald-400',
      badgeClass: 'bg-emerald-950 text-emerald-300 border border-emerald-700',
      text: 'Siamo arrivati. Sto accompagnando Alyssa verso la segreteria di Medicina e Botanica. Noah piantala o ti blocco il Wi-Fi di Villa Douglas.',
      time: '08:08'
    },
    {
      id: 4,
      sender: 'Echo',
      role: 'Digital Familiar',
      color: 'text-cyan-300',
      badgeClass: 'bg-cyan-950 text-cyan-300 border border-cyan-700',
      text: "[Audio Mood Speaker: Avviata playlist 'Subterranean Bass Drive']. Parametri vitali del Fireteam nella norma. Nessuna anomalia miasmatica nel raggio di 800m.",
      time: '08:09'
    },
    {
      id: 5,
      sender: 'Malachia',
      role: 'Berserker Strike',
      color: 'text-rose-400',
      badgeClass: 'bg-rose-950 text-rose-300 border border-rose-700',
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
      color: 'text-purple-300',
      badgeClass: 'bg-purple-950 text-purple-300 border border-purple-700',
      text: textToSend,
      time: 'Adesso'
    };
    setNextMsgId((id: number) => id + 1);
    setMessages((prev: any[]) => [...prev, newMsg]);
    setChatInput('');
  };

  // Database Studenti SUCC & CUMS
  const STUDENTS_DATA: Record<string, any> = {
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
      badge: 'Atleta · Berserker Strike',
      school: 'SUCC Athletics (DMHA Bulls)',
      major: 'Scienze Motorie & Combattimento Tattico',
      dept: 'Accademia Atletica e Difesa Territoriale',
      gpa: '3.10',
      credits: 45,
      internship: 'Seven Hills Security & Pattuglie Notturne DCC',
      courses: [
        { code: 'CMB-101', name: 'Combattimento Pesante & Fornace Interna', prof: 'Coach D', cfu: 8, grade: 'A+' },
        { code: 'TAC-203', name: 'Tattiche d Ingaggio Demoniaco & Miasma', prof: 'K. O Connor', cfu: 8, grade: 'A' },
        { code: 'NUT-105', name: 'Metabolismo dei Predatori & Apporto Ferroso', prof: 'Dr. Thorne', cfu: 6, grade: 'B' }
      ]
    },
    cums_students: {
      name: 'Accademia C.U.M.S. (Studenti di Magia)',
      badge: 'Classe Incantatori',
      school: 'C.U.M.S. (Collegiate Unified Magic Scholars)',
      major: 'Alta Stregoneria, Rituali Lunari & Illusione',
      dept: 'Polo Magico e Arcano di Solarton',
      gpa: '3.85',
      credits: 60,
      internship: 'Laboratori Arcani & Gilda dei Maghi di Solarton',
      courses: [
        { code: 'MAG-101', name: 'Fondamenti di Tessitura del Mana (Lestat, Zaire)', prof: 'A. Nairene', cfu: 8, grade: 'A' },
        { code: 'ABJ-205', name: 'Barriere Abbiurative & Difesa da Miasma (Caien, Aeril)', prof: 'M. Vance', cfu: 8, grade: 'A+' },
        { code: 'DUE-101', name: "Combattimento Tattico e Duello d'Ombra (Amerian)", prof: 'X. Nershatar', cfu: 10, grade: 'A+' },
        { code: 'NEC-301', name: 'Controllo delle Anime & Anatomia Spettrale (Xaiden, Ashton)', prof: 'V. Raven', cfu: 8, grade: 'A' }
      ]
    }
  };

  const studentData = STUDENTS_DATA[selectedStudent] || STUDENTS_DATA.alyssa;

  // Database Cacciatori DMHA
  const HUNTERS_DATA: Record<string, any> = {
    alyssa: {
      name: 'Alyssa Douglas',
      rank: 'Rango A',
      rankClass: 'bg-blue-950 text-sky-300 border border-blue-700',
      role: 'Healer & Supporto di Campo',
      squad: 'Douglas Vanguard / Seven Hills Fireteam',
      credits: 4850,
      specialty: 'Medicina da Campo, Terapie Anti-Miasma & Incanti Rigenerativi'
    },
    jasper: {
      name: 'Jasper Douglas',
      rank: 'Rango A',
      rankClass: 'bg-blue-950 text-sky-300 border border-blue-700',
      role: 'Technomancer & Netrunner Tattico',
      squad: 'Douglas Vanguard / Seven Hills Fireteam',
      credits: 5200,
      specialty: 'Silver-Tech, Droni da Ricognizione & Sovraccarico Runico'
    },
    malachia: {
      name: 'Malachia Douglas',
      rank: 'Rango S',
      rankClass: 'bg-rose-950 text-rose-300 border border-rose-700',
      role: 'Apex Berserker / Vanguard Strike',
      squad: 'Douglas First Strike Squad',
      credits: 8900,
      specialty: 'Fornace Interna, Rottura Linee Mostro & Caccia Alpha'
    },
    ukiyo: {
      name: 'Distaccamento Ukiyo (Radek, Goran, Marek)',
      rank: 'Rango B+',
      rankClass: 'bg-amber-950 text-amber-300 border border-amber-700',
      role: 'Operazioni Clandestine & Caccia Notturna',
      squad: 'Ukiyo Specialist Syndicate',
      credits: 3400,
      specialty: 'Infiltrazione Bassifondi, Neutralizzazione Bersagli & Controllo Territorio'
    }
  };

  const hunterData = HUNTERS_DATA[selectedHunter] || HUNTERS_DATA.alyssa;

  // Missioni DMHA in bacheca
  const MISSIONS = [
    {
      id: 'miss_cums_anomaly',
      title: 'Anomalia Miasmatica nei Sotterranei CUMS',
      zone: 'Solarton · Distretto Accademico Ovest',
      rank: 'Rango A',
      rankClass: 'text-sky-400 bg-sky-950 border border-sky-700',
      reward: "850 Crediti · Catalizzatore d'Ombra",
      desc: 'Segnalato rift minore nella biblioteca proibita del CUMS. Richiesto team di contenimento con healer e technomancer per stabilizzazione runica.'
    },
    {
      id: 'miss_bay_patrol',
      title: 'Pattugliamento Notturno: Baia di Blackwood',
      zone: 'Blackwood City · Docks Industriali',
      rank: 'Rango B',
      rankClass: 'text-amber-400 bg-amber-950 border border-amber-700',
      reward: "500 Crediti · Runa d'Argento",
      desc: 'Avvistamento creature anfibie attirate dai rifornimenti navali DCC. Bonificare il molo 4 prima delle ore 05:00.'
    },
    {
      id: 'miss_sewer_sweep',
      title: 'Bonifica Condotto Fognario Settore 4',
      zone: 'Solarton · Cable District',
      rank: 'Rango C',
      rankClass: 'text-emerald-400 bg-emerald-950 border border-emerald-700',
      reward: '300 Crediti · 2x Cilindri Soppressori',
      desc: 'Nido di ratti miasmatici di classe 1 nelle condotte di scolo adiacenti al campus SUCC. Intervento rapido richiesto.'
    }
  ];

  // Feed SuccBook
  const [feedPosts, setFeedPosts] = useState<any[]>([
    {
      id: 1,
      author: 'SUCC Athletics (DMHA Bulls)',
      handle: '@succ_bulls',
      badge: 'Ufficiale · Campus',
      avatar: '🏈',
      time: '32m fa',
      text: 'Vittoria schiacciante dei Bulls contro la Hex Valley League (42-14)! Malachia Douglas e Wulfric dominano la linea di mischia. Prossimo match venerdì!',
      likes: 342,
      liked: false
    },
    {
      id: 2,
      author: 'Elizabeth Duskwood (DCC Health)',
      handle: '@dr_duskwood',
      badge: 'Medicina Demi-Umani',
      avatar: '🩺',
      time: '1h fa',
      text: 'Bollettino LSE: con la luna calante e il cambio di stagione i livelli ormonali mostrano picchi improvvisi. Si ricorda agli studenti demi-umani di ritirare i soppressori in infermeria.',
      likes: 128,
      liked: false
    },
    {
      id: 3,
      author: 'Underground Frequency',
      handle: '@solarton_underground',
      badge: 'Eventi & Nightlife',
      avatar: '🔊',
      time: '2h fa',
      text: "Venerdì notte rave underground nei vecchi magazzini industriali al confine tra Solarton e Blackwood. Sound system magitech curato dai netrunner della DCC. Ingresso riservato a studenti e licantropi con controllo odore all'ingresso.",
      likes: 215,
      liked: false
    }
  ]);

  const toggleLike = (postId: number) => {
    setFeedPosts((prev: any[]) => prev.map((p: any) => {
      if (p.id === postId) {
        return { ...p, liked: !p.liked, likes: p.liked ? p.likes - 1 : p.likes + 1 };
      }
      return p;
    }));
  };

  // Tracce Audio Mood Speaker
  const TRACKS = [
    { title: 'Subterranean Bass Drive', artist: 'Echo (Digital Familiar) · DCC Net', mood: 'Dungeon Synth / Focus' },
    { title: 'Solarton Nightwave 104.2', artist: 'Netrunner Collective', mood: 'Lo-Fi Chill & Silver Beat' },
    { title: 'Bloodline Resonance (Erik Theme)', artist: 'Blackwood Orchestral', mood: 'Heavy Dark Ambience' },
    { title: 'Vanguard Alpha Strike', artist: 'Seven Hills Tactical Unit', mood: 'Combat High BPM' }
  ];

  return (
    <div className="w-full max-w-md mx-auto my-1 bg-zinc-950 text-zinc-100 rounded-3xl border border-zinc-800 shadow-2xl p-4 flex flex-col gap-3 font-sans select-none">
      
      {/* ========================================================================= */}
      {/* 1. TOP STATUS BAR / NOTCH SMARTPHONE                                      */}
      {/* ========================================================================= */}
      <div className="bg-zinc-900 rounded-2xl px-4 py-2 border border-zinc-800 flex items-center justify-between text-xs">
        <div className="flex items-center gap-2">
          <span className="font-bold text-zinc-100 font-mono">08:14</span>
          <span className="text-[10px] text-zinc-400 font-mono">DCC-5G ●●●</span>
        </div>

        {/* Dynamic Island: LSE & Moon status */}
        <div className="flex items-center gap-2 bg-black px-3 py-1 rounded-full border border-zinc-700">
          <span className="text-xs">{isFullMoon ? '🌕' : '🌙'}</span>
          <span className="text-[10px] font-semibold text-amber-300 truncate max-w-[110px]">
            {isFullMoon ? 'Piena Luna' : moonPhase}
          </span>
          {isFullMoon && (
            <span className="w-2 h-2 rounded-full bg-red-500 animate-pulse" />
          )}
        </div>

        <div className="flex items-center gap-2">
          <span className="text-[10px] text-emerald-400 font-mono font-bold">98% ⚡</span>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* 2. BARRA DI STATO RAPIDA: SOPPRESSORI FERORMONALI & RIFT THREAT           */}
      {/* ========================================================================= */}
      <div className="bg-zinc-900 rounded-2xl px-4 py-3 border border-zinc-800 flex items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <span className="text-xl">🩺</span>
          <div>
            <div className="text-xs font-bold text-zinc-100 flex items-center gap-2">
              <span>Soppressori:</span>
              <span className={suppressors > 0 ? 'text-emerald-400' : 'text-red-400'}>
                {suppressors} Dosi
              </span>
            </div>
            <div className="text-[11px] text-zinc-400 pt-1">
              LSE: <span className="text-amber-300 font-semibold">{lseStatus}</span> (~{daysLeft}gg picco)
            </div>
          </div>
        </div>

        <button
          onClick={handleUseSuppressor}
          className="bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold px-4 py-2 rounded-xl border border-emerald-500 shadow-sm transition active:scale-95 shrink-0"
        >
          Inala Dose
        </button>
      </div>

      {/* ========================================================================= */}
      {/* 3. SCHERMATE DELL'OS (VISTE INTERATTIVE)                                   */}
      {/* ========================================================================= */}
      <div className="min-h-[390px] flex flex-col justify-between">

        {/* ----------------------------------------------------------------------- */}
        {/* APP 1: HOME DASHBOARD                                                   */}
        {/* ----------------------------------------------------------------------- */}
        {activeApp === 'home' && (
          <div className="flex flex-col gap-3">
            {/* Widget Benvenuto Operativo */}
            <div className="bg-zinc-900 rounded-2xl p-4 border border-zinc-800 flex flex-col gap-2">
              <div className="flex items-center justify-between gap-3">
                <span className="text-xs font-bold text-zinc-100">Svartúlfr OS · Mobile Net</span>
                <span className="text-xs font-mono font-semibold bg-purple-950 text-purple-200 border border-purple-700 px-3 py-1 rounded-lg shrink-0">
                  Rep. Branco: {packRep}%
                </span>
              </div>
              <p className="text-xs text-zinc-300 leading-relaxed pr-1 pt-1">
                Benvenuto nel terminale crittografato del Branco Douglas e del polo accademico SUCC/CUMS.
              </p>
            </div>

            {/* Griglia Icone Applicazioni Smartphone */}
            <div className="grid grid-cols-3 gap-2">
              <button
                onClick={() => { setActiveApp('telegram'); setTelegramUnread(0); }}
                className="bg-zinc-900 hover:bg-zinc-850 p-4 rounded-2xl border border-zinc-800 flex flex-col items-center justify-center gap-2 transition active:scale-95 text-center relative"
              >
                <span className="text-3xl">💬</span>
                <span className="text-xs font-bold text-sky-400">Telegram</span>
                <span className="text-[10px] text-zinc-400">Branco Douglas</span>
                {telegramUnread > 0 && (
                  <span className="absolute top-2 right-2 bg-sky-500 text-white text-[10px] font-bold px-2 py-1 rounded-full min-w-[20px]">
                    {telegramUnread}
                  </span>
                )}
              </button>

              <button
                onClick={() => setActiveApp('academics')}
                className="bg-zinc-900 hover:bg-zinc-850 p-4 rounded-2xl border border-zinc-800 flex flex-col items-center justify-center gap-2 transition active:scale-95 text-center"
              >
                <span className="text-3xl">🎓</span>
                <span className="text-xs font-bold text-indigo-400">SUCC & CUMS</span>
                <span className="text-[10px] text-zinc-400">Libretto Corsi</span>
              </button>

              <button
                onClick={() => setActiveApp('guild')}
                className="bg-zinc-900 hover:bg-zinc-850 p-4 rounded-2xl border border-zinc-800 flex flex-col items-center justify-center gap-2 transition active:scale-95 text-center"
              >
                <span className="text-3xl">⚔️</span>
                <span className="text-xs font-bold text-red-400">Gilda DMHA</span>
                <span className="text-[10px] text-zinc-400">Bacheca Caccia</span>
              </button>

              <button
                onClick={() => setActiveApp('biotrack')}
                className="bg-zinc-900 hover:bg-zinc-850 p-4 rounded-2xl border border-zinc-800 flex flex-col items-center justify-center gap-2 transition active:scale-95 text-center"
              >
                <span className="text-3xl">🐾</span>
                <span className="text-xs font-bold text-emerald-400">BioTrack LSE</span>
                <span className="text-[10px] text-zinc-400">Ferormoni & Luna</span>
              </button>

              <button
                onClick={() => { setActiveApp('succbook'); setSuccbookUnread(0); }}
                className="bg-zinc-900 hover:bg-zinc-850 p-4 rounded-2xl border border-zinc-800 flex flex-col items-center justify-center gap-2 transition active:scale-95 text-center relative"
              >
                <span className="text-3xl">📸</span>
                <span className="text-xs font-bold text-yellow-400">SuccBook</span>
                <span className="text-[10px] text-zinc-400">Social Campus</span>
                {succbookUnread > 0 && (
                  <span className="absolute top-2 right-2 bg-yellow-500 text-black text-[10px] font-bold px-2 py-1 rounded-full min-w-[20px]">
                    {succbookUnread}
                  </span>
                )}
              </button>

              <button
                onClick={() => setActiveApp('music')}
                className="bg-zinc-900 hover:bg-zinc-850 p-4 rounded-2xl border border-zinc-800 flex flex-col items-center justify-center gap-2 transition active:scale-95 text-center"
              >
                <span className="text-3xl">🎵</span>
                <span className="text-xs font-bold text-cyan-300">Audio Mood</span>
                <span className="text-[10px] text-zinc-400">Echo Speaker</span>
              </button>
            </div>

            {/* Quick Banner: Allerta Minaccia Rift */}
            <div className="bg-zinc-900 rounded-2xl px-4 py-3 border border-zinc-800 flex items-center justify-between text-xs">
              <div className="flex items-center gap-2">
                <span className="text-amber-400 font-bold">⚠️ Allerta Rift:</span>
                <span className="text-zinc-200 font-mono">{riftAlert}</span>
              </div>
              <span className="text-[10px] text-zinc-500 font-mono">DCC SEC OK</span>
            </div>
          </div>
        )}

        {/* ----------------------------------------------------------------------- */}
        {/* APP 2: TELEGRAM DOUGLAS (CHAT DI BRANCO)                                */}
        {/* ----------------------------------------------------------------------- */}
        {activeApp === 'telegram' && (
          <div className="flex flex-col gap-3">
            <div className="flex items-center justify-between pb-2 border-b border-zinc-800">
              <div className="flex items-center gap-2">
                <span className="text-sky-400 font-bold text-sm">💬 Branco Douglas</span>
                <span className="text-[10px] text-emerald-400 font-medium">● 5 online</span>
              </div>
              <button
                onClick={() => setActiveApp('home')}
                className="text-xs text-zinc-300 hover:text-white px-3 py-1 rounded-lg bg-zinc-800 border border-zinc-700"
              >
                Chiudi
              </button>
            </div>

            <div className="flex flex-col gap-2 max-h-[290px] overflow-y-auto pr-1">
              {messages.map((m: any) => (
                <div
                  key={m.id}
                  className="bg-zinc-900 rounded-2xl p-4 border border-zinc-800 flex flex-col gap-2 shadow-sm"
                >
                  <div className="flex items-center justify-between gap-3">
                    <span className={'text-xs font-bold ' + m.color}>{m.sender}</span>
                    <div className="flex items-center gap-2">
                      <span className={'text-[10px] px-3 py-1 rounded-md font-semibold shrink-0 ' + m.badgeClass}>
                        {m.role}
                      </span>
                      <span className="text-xs text-zinc-500 font-mono shrink-0">{m.time}</span>
                    </div>
                  </div>
                  <p className="text-xs text-zinc-200 leading-relaxed pr-1 pt-1">{m.text}</p>
                </div>
              ))}
            </div>

            <div className="flex items-center gap-2 pt-1">
              <input
                type="text"
                placeholder="Scrivi messaggio al branco..."
                value={chatInput}
                onChange={(e: any) => setChatInput(String(e?.target?.value ?? e ?? ''))}
                className="flex-1 bg-zinc-900 text-zinc-100 placeholder-zinc-500 text-xs px-4 py-3 rounded-xl border border-zinc-800 focus:outline-none focus:border-sky-500"
              />
              <button
                onClick={handleSendMessage}
                className="bg-sky-600 hover:bg-sky-500 text-white font-bold text-xs px-4 py-3 rounded-xl transition shadow-sm"
              >
                Invia
              </button>
            </div>
          </div>
        )}

        {/* ----------------------------------------------------------------------- */}
        {/* APP 3: SUCC & CUMS ACADEMICS (RIDEFINITO CON SPAZIATURA ECCELLENTE)     */}
        {/* ----------------------------------------------------------------------- */}
        {activeApp === 'academics' && (
          <div className="flex flex-col gap-3">
            <div className="flex items-center justify-between pb-2 border-b border-zinc-800">
              <span className="text-indigo-400 font-bold text-sm">🎓 Libretto Accademico SUCC & CUMS</span>
              <button
                onClick={() => setActiveApp('home')}
                className="text-xs text-zinc-300 hover:text-white px-3 py-1 rounded-lg bg-zinc-800 border border-zinc-700"
              >
                Chiudi
              </button>
            </div>

            {/* Selettore Studente con respiro verticale in modo da non essere MAI clippato */}
            <div className="flex gap-2 overflow-x-auto py-1 text-xs">
              {[
                { id: 'alyssa', label: 'Alyssa' },
                { id: 'jasper', label: 'Jasper' },
                { id: 'noah', label: 'Noah' },
                { id: 'malachia', label: 'Malachia' },
                { id: 'cums_students', label: 'CUMS Magic' }
              ].map((s: any) => (
                <button
                  key={s.id}
                  onClick={() => setSelectedStudent(s.id)}
                  className={'px-3 py-2 rounded-xl font-semibold whitespace-nowrap transition ' + (selectedStudent === s.id ? 'bg-indigo-600 text-white shadow-sm' : 'bg-zinc-900 text-zinc-400 hover:text-zinc-200 border border-zinc-800')}
                >
                  {s.label}
                </button>
              ))}
            </div>

            {/* Scheda Dati Studente */}
            <div className="bg-zinc-900 rounded-2xl p-4 border border-zinc-800 flex flex-col gap-2">
              <div className="flex items-center justify-between gap-3">
                <div>
                  <div className="text-xs font-bold text-zinc-100">{studentData.name}</div>
                  <div className="text-[11px] text-zinc-400">{studentData.school}</div>
                </div>
                <span className="text-xs bg-indigo-950 text-indigo-300 border border-indigo-700 px-3 py-1 rounded-lg font-mono font-semibold shrink-0">
                  GPA {studentData.gpa} · {studentData.credits} CFU
                </span>
              </div>
              <div className="text-xs text-zinc-300 pt-1 border-t border-zinc-800">
                <span className="font-semibold text-zinc-400">Indirizzo:</span> {studentData.major}
              </div>
              <div className="text-[11px] text-zinc-400">
                <span className="font-semibold text-zinc-400">Tirocinio:</span> {studentData.internship}
              </div>
            </div>

            {/* Lista Corsi: layout senza bordi interni rigidi e con badge voto a blocco fisso (w-10 h-8) */}
            <div className="flex flex-col gap-2 max-h-[180px] overflow-y-auto pr-1">
              {studentData.courses.map((c: any, i: number) => (
                <div
                  key={i}
                  className="bg-zinc-900 hover:bg-zinc-850 rounded-2xl p-4 border border-zinc-800 flex items-center justify-between gap-4 text-xs"
                >
                  <div className="flex-1 min-w-0 pr-1">
                    <div className="text-xs font-semibold text-zinc-100 truncate">{c.name}</div>
                    <div className="text-[10px] text-zinc-400 font-mono pt-1">
                      {c.code} · Prof. {c.prof} · {c.cfu} CFU
                    </div>
                  </div>
                  {/* Badge voto: larghezza 40px, altezza 32px, flex center per perfetto allineamento del voto */}
                  <div className="w-10 h-8 rounded-xl flex items-center justify-center font-mono font-bold text-xs bg-emerald-950 text-emerald-300 border border-emerald-600 shrink-0 shadow-sm">
                    {c.grade}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ----------------------------------------------------------------------- */}
        {/* APP 4: GILDA DMHA (BACHECA CACCIATORI)                                  */}
        {/* ----------------------------------------------------------------------- */}
        {activeApp === 'guild' && (
          <div className="flex flex-col gap-3">
            <div className="flex items-center justify-between pb-2 border-b border-zinc-800">
              <span className="text-red-400 font-bold text-sm">⚔️ Gilda dei Cacciatori DMHA</span>
              <button
                onClick={() => setActiveApp('home')}
                className="text-xs text-zinc-300 hover:text-white px-3 py-1 rounded-lg bg-zinc-800 border border-zinc-700"
              >
                Chiudi
              </button>
            </div>

            {/* Selettore Cacciatore */}
            <div className="flex gap-2 overflow-x-auto py-1 text-xs">
              {[
                { id: 'alyssa', label: 'Alyssa' },
                { id: 'jasper', label: 'Jasper' },
                { id: 'malachia', label: 'Malachia' },
                { id: 'ukiyo', label: 'Ukiyo' }
              ].map((h: any) => (
                <button
                  key={h.id}
                  onClick={() => setSelectedHunter(h.id)}
                  className={'px-3 py-2 rounded-xl font-semibold whitespace-nowrap transition ' + (selectedHunter === h.id ? 'bg-red-600 text-white shadow-sm' : 'bg-zinc-900 text-zinc-400 hover:text-zinc-200 border border-zinc-800')}
                >
                  {h.label}
                </button>
              ))}
            </div>

            {/* Badge Rango Cacciatore */}
            <div className="bg-zinc-900 rounded-2xl p-4 border border-zinc-800 flex items-center justify-between gap-3">
              <div>
                <div className="text-xs font-bold text-zinc-100">{hunterData.name}</div>
                <div className="text-[11px] text-zinc-400">{hunterData.role}</div>
                <div className="text-[10px] text-zinc-400 font-mono pt-1">Crediti Caccia: {hunterData.credits} CR</div>
              </div>
              <span className={'text-xs font-bold px-3 py-2 rounded-xl border font-mono shrink-0 shadow-sm ' + hunterData.rankClass}>
                {hunterData.rank}
              </span>
            </div>

            {/* Missioni DMHA */}
            <div className="flex flex-col gap-2 max-h-[170px] overflow-y-auto pr-1">
              {MISSIONS.map((m: any) => (
                <div key={m.id} className="bg-zinc-900 rounded-2xl p-4 border border-zinc-800 flex flex-col gap-2">
                  <div className="flex items-center justify-between gap-2">
                    <span className="text-xs font-bold text-zinc-100">{m.title}</span>
                    <span className={'text-[10px] font-bold px-2 py-1 rounded-md border font-mono shrink-0 ' + m.rankClass}>
                      {m.rank}
                    </span>
                  </div>
                  <p className="text-xs text-zinc-300 leading-relaxed">{m.desc}</p>
                  <div className="flex items-center justify-between pt-1 text-xs">
                    <span className="text-amber-400 font-mono font-semibold">Ricompensa: {m.reward}</span>
                    <button
                      onClick={() => setAcceptedMissionId(m.id)}
                      className={'px-3 py-2 rounded-xl font-bold transition shadow-sm ' + (acceptedMissionId === m.id ? 'bg-emerald-600 text-white' : 'bg-zinc-800 text-zinc-200 hover:bg-zinc-700 border border-zinc-700')}
                    >
                      {acceptedMissionId === m.id ? 'Accettata ✓' : 'Accetta Incarico'}
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ----------------------------------------------------------------------- */}
        {/* APP 5: BIOTRACK LSE (FERORMONI & FASI LUNARI)                           */}
        {/* ----------------------------------------------------------------------- */}
        {activeApp === 'biotrack' && (
          <div className="flex flex-col gap-3">
            <div className="flex items-center justify-between pb-2 border-b border-zinc-800">
              <span className="text-emerald-400 font-bold text-sm">🐾 BioTrack LSE & Monitor Ferormonale</span>
              <button
                onClick={() => setActiveApp('home')}
                className="text-xs text-zinc-300 hover:text-white px-3 py-1 rounded-lg bg-zinc-800 border border-zinc-700"
              >
                Chiudi
              </button>
            </div>

            {/* Pannello Biologico Licantropo */}
            <div className="bg-zinc-900 rounded-2xl p-4 border border-zinc-800 flex flex-col gap-3 shadow-sm">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold text-zinc-200">Stato Fisiologico LSE:</span>
                <span className="text-xs font-bold text-amber-400 bg-amber-950 px-3 py-1 rounded-lg border border-amber-700">
                  {lseStatus}
                </span>
              </div>
              <div className="flex items-center justify-between text-xs pt-1 border-t border-zinc-800">
                <span className="text-zinc-400">Giorni al Picco Stagionale:</span>
                <span className="font-mono font-bold text-zinc-100">{daysLeft} giorni</span>
              </div>
              <div className="flex items-center justify-between text-xs">
                <span className="text-zinc-400">Scorta Soppressori Odore:</span>
                <span className={'font-mono font-bold ' + (suppressors > 0 ? 'text-emerald-400' : 'text-red-400')}>
                  {suppressors} cilindri attivi
                </span>
              </div>
            </div>

            {/* Influsso Lunare */}
            <div className="bg-zinc-900 rounded-2xl p-4 border border-zinc-800 flex flex-col gap-2 shadow-sm">
              <div className="flex items-center justify-between gap-2">
                <span className="text-xs font-bold text-amber-300">🌙 Influsso Lunare Attuale</span>
                <span className={'text-xs font-bold px-3 py-1 rounded-lg border shrink-0 ' + (isFullMoon ? 'bg-red-950 text-red-300 border-red-700' : 'bg-zinc-800 text-zinc-400 border-zinc-700')}>
                  {isFullMoon ? 'BUFF ATTIVO (+2 MGT/RES, +1 AGI)' : 'Influsso Standard'}
                </span>
              </div>
              <p className="text-xs text-zinc-300 leading-relaxed pt-1">
                Fase corrente: <span className="font-semibold text-zinc-100">{moonPhase}</span>. {isNight ? 'Notte attiva in California (sensi acuiti, visibilità notturna attiva).' : 'Giorno standard nel campus di Solarton.'}
              </p>
            </div>
          </div>
        )}

        {/* ----------------------------------------------------------------------- */}
        {/* APP 6: SUCCBOOK (SOCIAL CAMPUS)                                         */}
        {/* ----------------------------------------------------------------------- */}
        {activeApp === 'succbook' && (
          <div className="flex flex-col gap-3">
            <div className="flex items-center justify-between pb-2 border-b border-zinc-800">
              <span className="text-yellow-400 font-bold text-sm">📸 SuccBook · Campus Solarton</span>
              <button
                onClick={() => setActiveApp('home')}
                className="text-xs text-zinc-300 hover:text-white px-3 py-1 rounded-lg bg-zinc-800 border border-zinc-700"
              >
                Chiudi
              </button>
            </div>

            <div className="flex flex-col gap-2 max-h-[300px] overflow-y-auto pr-1">
              {feedPosts.map((p: any) => (
                <div key={p.id} className="bg-zinc-900 rounded-2xl p-4 border border-zinc-800 flex flex-col gap-2 shadow-sm">
                  <div className="flex items-center justify-between gap-2">
                    <div className="flex items-center gap-2">
                      <span className="text-xl">{p.avatar}</span>
                      <div>
                        <div className="text-xs font-bold text-zinc-100">{p.author}</div>
                        <div className="text-[10px] text-zinc-400 font-mono">{p.handle} · {p.time}</div>
                      </div>
                    </div>
                    <span className="text-[10px] bg-zinc-800 text-zinc-300 px-3 py-1 rounded-md border border-zinc-700 font-medium shrink-0">
                      {p.badge}
                    </span>
                  </div>
                  <p className="text-xs text-zinc-200 leading-relaxed pr-1 pt-1">{p.text}</p>
                  <div className="flex items-center justify-between pt-2 border-t border-zinc-800 text-xs">
                    <button
                      onClick={() => toggleLike(p.id)}
                      className={'flex items-center gap-2 px-3 py-2 rounded-lg transition ' + (p.liked ? 'text-red-400 bg-red-950 border border-red-700 font-bold' : 'text-zinc-400 hover:text-red-400 bg-zinc-800 border border-zinc-700')}
                    >
                      <span>{p.liked ? '❤️' : '🤍'}</span>
                      <span>{p.likes} Like</span>
                    </button>
                    <span className="text-[10px] text-zinc-500 font-mono">DCC Social Net</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* ----------------------------------------------------------------------- */}
        {/* APP 7: AUDIO MOOD SPEAKER                                               */}
        {/* ----------------------------------------------------------------------- */}
        {activeApp === 'music' && (
          <div className="flex flex-col gap-3">
            <div className="flex items-center justify-between pb-2 border-b border-zinc-800">
              <span className="text-cyan-300 font-bold text-sm">🎵 Echo Mood Audio Player</span>
              <button
                onClick={() => setActiveApp('home')}
                className="text-xs text-zinc-300 hover:text-white px-3 py-1 rounded-lg bg-zinc-800 border border-zinc-700"
              >
                Chiudi
              </button>
            </div>

            {/* Now Playing Card */}
            <div className="bg-zinc-900 rounded-2xl p-4 border border-zinc-800 flex flex-col gap-3 shadow-md">
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 rounded-xl bg-cyan-950 flex items-center justify-center text-2xl border border-cyan-700 shrink-0 shadow-inner">
                  🎧
                </div>
                <div>
                  <div className="text-xs font-bold text-zinc-100">{activeTrack.title}</div>
                  <div className="text-xs text-cyan-300 font-medium">{activeTrack.artist}</div>
                  <div className="text-[10px] text-zinc-400 font-mono">{activeTrack.mood}</div>
                </div>
              </div>
              <div className="flex items-center justify-between pt-1">
                <button
                  onClick={() => setMusicPlaying(!musicPlaying)}
                  className="bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs px-4 py-2 rounded-xl transition shadow-sm"
                >
                  {musicPlaying ? 'Pause ⏸' : 'Play ▶'}
                </button>
                <span className="text-xs text-cyan-400 font-mono font-semibold">
                  {musicPlaying ? 'Status: In Riproduzione ●' : 'Status: In Pausa ○'}
                </span>
              </div>
            </div>

            {/* Playlist Selettore */}
            <div className="flex flex-col gap-2">
              <span className="text-[10px] font-bold text-zinc-400 uppercase tracking-wider px-1">
                Playlist Consigliate da Echo
              </span>
              {TRACKS.map((t: any, i: number) => (
                <button
                  key={i}
                  onClick={() => { setActiveTrack(t); setMusicPlaying(true); }}
                  className={'w-full p-3 rounded-2xl border flex items-center justify-between text-left transition text-xs ' + (activeTrack.title === t.title ? 'bg-cyan-950 border-cyan-700 text-white shadow-sm' : 'bg-zinc-900 border-zinc-800 text-zinc-300 hover:bg-zinc-850')}
                >
                  <div>
                    <div className="font-semibold text-xs">{t.title}</div>
                    <div className="text-[10px] text-zinc-400">{t.artist}</div>
                  </div>
                  <span className="text-[10px] text-cyan-400 font-mono shrink-0 pl-2">{t.mood}</span>
                </button>
              ))}
            </div>
          </div>
        )}

      </div>

      {/* ========================================================================= */}
      {/* 4. BOTTOM DOCK SMARTPHONE: CON BADGE RELATIVO PERFETTO                     */}
      {/* ========================================================================= */}
      <div className="bg-zinc-900 rounded-2xl p-2 border border-zinc-800 flex items-center justify-around text-xs mt-1 shadow-inner">
        {[
          { id: 'home', label: 'Home', icon: '🏠' },
          { id: 'telegram', label: 'Chat', icon: '💬', badge: telegramUnread },
          { id: 'academics', label: 'Studio', icon: '🎓' },
          { id: 'guild', label: 'Gilda', icon: '⚔️' },
          { id: 'biotrack', label: 'LSE', icon: '🐾' }
        ].map((tab: any) => {
          const isActive = activeApp === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => {
                setActiveApp(tab.id);
                if (tab.id === 'telegram') setTelegramUnread(0);
              }}
              className={'relative flex flex-col items-center justify-center py-2 px-3 rounded-xl transition ' + (isActive ? 'bg-zinc-800 text-white font-bold shadow-sm' : 'text-zinc-400 hover:text-zinc-200')}
            >
              <div className="relative flex items-center justify-center">
                <span className="text-xl leading-none">{tab.icon}</span>
                {tab.badge && tab.badge > 0 && (
                  <span className="absolute -top-1 -right-3 bg-sky-500 text-white text-[9px] font-bold px-2 py-1 rounded-full min-w-[16px] text-center leading-none">
                    {tab.badge}
                  </span>
                )}
              </div>
              <span className="text-[10px] font-medium mt-1">{tab.label}</span>
            </button>
          );
        })}
      </div>

    </div>
  );
}

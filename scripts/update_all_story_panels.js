const fs = require('fs');

async function updateAllPanels() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
  };

  // 1. Fetch current engine
  const getRes = await fetch('https://app.wyvern.chat/api/story-engines/engine_HCTPXhL8xr89wUY9r9dYU', { headers });
  const eng = await getRes.json();
  const def = eng.definition;

  // -------------------------------------------------------------
  // PANEL 2: SUCC LIBRETTO ACCADEMICO (DINAMICO CON TAB PER STUDENTI)
  // -------------------------------------------------------------
  const succAcademicsCode = `export default function Panel({ engine }) {
  // Database Studenti SUCC
  const STUDENTS_DATA = {
    alyssa: {
      name: 'Alyssa Douglas',
      shortName: 'Alyssa',
      roleBadge: 'Matricola · Pre-Med',
      major: 'Scienze Mediche & Botanica Arcana',
      department: 'Facoltà di Medicina e Fisiologia Demi-Umani',
      gpa: '3.92',
      gpaLabel: 'Eccellente (Summa)',
      credits: 28,
      totalCredits: 180,
      internship: 'Infermeria SUCC & Laboratori Medici DCC (Supervisione Dr.ssa Duskwood)',
      courses: [
        { code: 'MED-101', name: 'Anatomia Comparata Demi-Umani', prof: 'H. Vance', cfu: 8, grade: 'A+' },
        { code: 'BOT-104', name: 'Botanica Arcana & Proprietà Lunari', prof: 'M. Willow', cfu: 6, grade: 'A' },
        { code: 'FAR-202', name: 'Farmacologia & Inibitori Ferormonali', prof: 'E. Duskwood', cfu: 8, grade: 'A' },
        { code: 'EMR-108', name: 'Primo Soccorso & Traumi da Argento', prof: 'G. Vance', cfu: 6, grade: 'A+' }
      ]
    },
    jasper: {
      name: 'Jasper Douglas',
      shortName: 'Jasper',
      roleBadge: '1° Anno · Ingegneria',
      major: 'Ingegneria Arcana & Meccanica Avanzata',
      department: 'Dipartimento di Tecnologie Silver-Tech e Magitech',
      gpa: '3.78',
      gpaLabel: 'Distinto',
      credits: 30,
      totalCredits: 180,
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
      shortName: 'Noah',
      roleBadge: '2° Anno · Public Relations',
      major: 'Scienze Politiche, PR & Management Sportivo',
      department: 'Scuola di Relazioni Istituzionali e Diplomazia',
      gpa: '3.55',
      gpaLabel: 'Buono',
      credits: 54,
      totalCredits: 180,
      internship: 'Ufficio Relazioni Pubbliche DCC & Addetto Stampa SUCC Bulls',
      courses: [
        { code: 'COM-201', name: 'Comunicazione Istituzionale & Crisi di Branco', prof: 'D. Sterling', cfu: 8, grade: 'A' },
        { code: 'DIR-204', name: 'Diritto Commerciale Fazioni Supernatural', prof: 'E. Thornton', cfu: 8, grade: 'B+' },
        { code: 'MKT-208', name: 'Marketing & Sponsorizzazioni DMHA Bulls', prof: 'G. Hayes', cfu: 6, grade: 'A' },
        { code: 'DIP-210', name: 'Diplomazia Inter-Specie & Mediazione', prof: 'M. Mirei', cfu: 6, grade: 'A-' }
      ]
    },
    malachia: {
      name: 'Malachia Douglas',
      shortName: 'Malachia',
      roleBadge: '3° Anno Senior · Tattica',
      major: 'Scienze Motorie, Tattica di Combattimento & Difesa',
      department: 'Accademia Tattica e Addestramento Operativo',
      gpa: '3.30',
      gpaLabel: 'Soddisfacente',
      credits: 82,
      totalCredits: 180,
      internship: 'Istruttore Assistente Combattimento Corpo a Corpo SUCC',
      courses: [
        { code: 'TAC-301', name: 'Tattica di Branco & Incursioni nei Rift', prof: 'K. Nargathon', cfu: 10, grade: 'A+' },
        { code: 'SPT-305', name: 'Condizionamento Fisico Demi-Umani & Shift', prof: 'Coach D', cfu: 8, grade: 'A+' },
        { code: 'LEG-202', name: 'Legislazione Uso della Forza nei Distretti', prof: 'R. Miller', cfu: 6, grade: 'C+' },
        { code: 'BIO-209', name: 'Fisiologia dello Sforzo & Resistenza Miasma', prof: 'E. Duskwood', cfu: 6, grade: 'B' }
      ]
    },
    jared: {
      name: 'Jared Thompson',
      shortName: 'Jared',
      roleBadge: '2° Anno · Economics',
      major: 'Economia, Finanza & Gestione Aziendale',
      department: 'Scuola di Business e Finanza Applicata',
      gpa: '3.85',
      gpaLabel: 'Ottimo',
      credits: 58,
      totalCredits: 180,
      internship: 'Divisione Finanziaria Douglas Commercial Coalition (Desk Investimenti)',
      courses: [
        { code: 'ECO-201', name: 'Contabilità Avanzata & Bilanci Fazioni', prof: 'R. Klein', cfu: 8, grade: 'A' },
        { code: 'FIN-203', name: 'Macroeconomia Mercati Arcani & Cristalli', prof: 'H. Adler', cfu: 8, grade: 'A' },
        { code: 'DIR-205', name: 'Diritto Tributario & Contrattualistica DCC', prof: 'E. Thornton', cfu: 6, grade: 'A-' },
        { code: 'STA-208', name: 'Statistica Applicata al Rischio Rift', prof: 'H. Choi', cfu: 6, grade: 'A' }
      ]
    },
    edric: {
      name: 'Edric Douglas',
      shortName: 'Edric',
      roleBadge: 'Matricola · Studi Umanistici',
      major: 'Scienze Umanistiche & Storia delle Fazioni',
      department: 'Dipartimento di Lettere e Retaggio Supernatural',
      gpa: '3.40',
      gpaLabel: 'Buono',
      credits: 24,
      totalCredits: 180,
      internship: 'Archivio Storico Villa Douglas & Biblioteca Centrale SUCC',
      courses: [
        { code: 'HST-101', name: 'Storia delle Guerre di Branco & Trattati', prof: 'E. Holbrook', cfu: 8, grade: 'B+' },
        { code: 'LNG-105', name: 'Lingue Antiche & Runologia Nordica', prof: 'Revazhael', cfu: 8, grade: 'A' },
        { code: 'SOC-109', name: 'Sociologia delle Comunità Metropolitane', prof: 'S. Martin', cfu: 8, grade: 'B' }
      ]
    },
    viola: {
      name: 'Viola Carter',
      shortName: 'Viola',
      roleBadge: '2° Anno · Fine Arts',
      major: 'Belle Arti, Grafica & Design Arcana',
      department: 'Facoltà di Arti Visive e Simbolismo',
      gpa: '3.70',
      gpaLabel: 'Distinto',
      credits: 52,
      totalCredits: 180,
      internship: 'Studio Artistico Seven Hills & Grafica Ufficiale SUCC',
      courses: [
        { code: 'ART-201', name: 'Pittura Energetica & Pigmenti Magici', prof: 'E. Delacroix', cfu: 8, grade: 'A' },
        { code: 'DES-203', name: 'Design Visivo & Identità per Fazioni', prof: 'S. Moreau', cfu: 8, grade: 'A' },
        { code: 'ARC-207', name: 'Storia dell Arte dei Popoli della Faglia', prof: 'E. Holbrook', cfu: 8, grade: 'B+' }
      ]
    }
  };

  // Rilevamento dinamico degli studenti presenti nel party / DOM
  const [showAllPack, setShowAllPack] = useState(false);

  // Scansione del DOM per identificare chi e presente nel party
  const detectedKeys = (() => {
    if (typeof document === 'undefined') return ['alyssa'];
    const pageText = (document.body?.innerText || '').toLowerCase();
    
    // Controlliamo la presenza dei soli personaggi universitari (escludendo Mac, Erik, Logan ecc.)
    const candidates = ['alyssa', 'jasper', 'noah', 'malachia', 'jared', 'edric', 'viola'];
    const found = candidates.filter(key => pageText.includes(key));
    return found.length > 0 ? found : ['alyssa'];
  })();

  const activeKeys = showAllPack ? Object.keys(STUDENTS_DATA) : detectedKeys;
  const [selectedStudentKey, setSelectedStudentKey] = useState(() => activeKeys[0] || 'alyssa');

  const currentKey = activeKeys.includes(selectedStudentKey) ? selectedStudentKey : activeKeys[0] || 'alyssa';
  const curr = STUDENTS_DATA[currentKey] || STUDENTS_DATA.alyssa;

  return (
    <div className="space-y-3 font-sans text-xs select-none">
      <Card className="bg-black border-zinc-800 text-zinc-300 shadow-xl overflow-hidden">
        <CardHeader className="px-4 py-3 bg-neutral-900 border-b border-zinc-800 flex flex-row items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="text-base">🎓</span>
            <div>
              <CardTitle className="text-sm font-bold text-zinc-100">SUCC · Libretto Accademico</CardTitle>
              <CardDescription className="text-[10px] text-zinc-400">Solarton University & Community College</CardDescription>
            </div>
          </div>
          <Badge className="bg-blue-950 text-sky-300 border-0 font-bold text-xs px-2.5 py-0.5">A.A. 2024/2025</Badge>
        </CardHeader>

        {/* Tab di Selezione Dinamica degli Studenti nel Party */}
        <div className="bg-neutral-950 px-4 py-2 border-b border-zinc-800/80 flex items-center justify-between gap-2 overflow-x-auto">
          <div className="flex items-center gap-1.5 overflow-x-auto pb-0.5">
            {activeKeys.map(k => {
              const s = STUDENTS_DATA[k];
              const isSelected = k === currentKey;
              return (
                <button
                  key={k}
                  onClick={() => setSelectedStudentKey(k)}
                  className={'px-2.5 py-1 rounded-md text-xs font-semibold transition-all whitespace-nowrap flex items-center gap-1 ' + (isSelected ? 'bg-sky-600 text-white shadow-sm' : 'bg-neutral-900 text-zinc-400 hover:text-zinc-200 hover:bg-neutral-800')}
                >
                  <span>{s.shortName}</span>
                  {isSelected && <span className="text-[9px] bg-sky-800/80 px-1 rounded font-mono">{s.gpa}</span>}
                </button>
              );
            })}
          </div>

          <button
            onClick={() => setShowAllPack(prev => !prev)}
            title={showAllPack ? 'Filtra solo membri party attivi' : 'Mostra tutti gli studenti del branco'}
            className="text-[10px] text-zinc-400 hover:text-sky-300 font-medium px-1.5 py-0.5 rounded border border-zinc-800 bg-neutral-900 shrink-0 whitespace-nowrap"
          >
            {showAllPack ? 'Filtra Party' : '+ Branco'}
          </button>
        </div>

        <CardContent className="p-4 space-y-3.5">
          {/* Header Profilo dello Studente Selezionato */}
          <div className="bg-neutral-900 rounded-lg p-3.5 border-0 space-y-1.5">
            <div className="flex items-center justify-between">
              <span className="font-bold text-sm text-zinc-100">{curr.name}</span>
              <Badge className="bg-neutral-950 text-sky-300 border border-zinc-800 text-[10px] font-semibold px-2 py-0.5">
                {curr.roleBadge}
              </Badge>
            </div>
            <p className="text-xs font-semibold text-amber-300 leading-snug">{curr.major}</p>
            <p className="text-[10px] text-zinc-400">{curr.department}</p>
          </div>

          {/* Statistiche Accademiche (GPA & CFU) */}
          <div className="grid grid-cols-2 gap-2.5">
            <div className="bg-neutral-900 rounded-lg p-3.5 border-0 text-center space-y-1">
              <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Media Accademica (GPA)</p>
              <p className="text-lg font-bold text-emerald-400">{curr.gpa} <span className="text-[10px] font-normal text-zinc-400">/ 4.00</span></p>
              <p className="text-[10px] text-emerald-300/80 font-medium">{curr.gpaLabel}</p>
            </div>
            <div className="bg-neutral-900 rounded-lg p-3.5 border-0 text-center space-y-1">
              <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Crediti Universitari</p>
              <p className="text-lg font-bold text-sky-400">{curr.credits} <span className="text-[10px] font-normal text-zinc-400">/ {curr.totalCredits} CFU</span></p>
              <div className="w-full bg-zinc-800 rounded-full h-1 mt-1 overflow-hidden">
                <div className="bg-sky-500 h-1 rounded-full" style={{ width: Math.round((curr.credits / curr.totalCredits) * 100) + '%' }}></div>
              </div>
            </div>
          </div>

          {/* Elenco Insegnamenti del Semestre */}
          <div className="space-y-2">
            <div className="flex items-center justify-between px-0.5">
              <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Insegnamenti & Valutazioni Attive</p>
              <span className="text-[10px] text-sky-300 font-mono">Semestre 1</span>
            </div>
            {curr.courses.map((c, i) => (
              <div key={i} className="bg-neutral-900 hover:bg-zinc-800 transition-colors rounded-lg p-3 border-0 flex items-center justify-between gap-2">
                <div className="space-y-0.5 min-w-0 pr-1">
                  <p className="font-semibold text-xs text-zinc-200 leading-snug">{c.name}</p>
                  <p className="text-[10px] text-zinc-400">{c.code} · Prof. {c.prof} · <span className="text-amber-300 font-medium">{c.cfu} CFU</span></p>
                </div>
                <Badge className="bg-neutral-950 text-emerald-400 font-bold border border-zinc-800 text-xs px-2.5 py-0.5 shrink-0">
                  {c.grade}
                </Badge>
              </div>
            ))}
          </div>

          {/* Tirocinio e Laboratori */}
          <div className="bg-neutral-900 rounded-lg p-3.5 border-0 space-y-1">
            <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Tirocini & Laboratori Accreditati</p>
            <p className="font-semibold text-xs text-sky-300 leading-snug">{curr.internship}</p>
            <p className="text-[10px] text-zinc-400">Certificazione approvata dal Comitato Accademico SUCC</p>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}`;

  // -------------------------------------------------------------
  // PANEL 3: DMHA REGISTRO GILDA & MISSIONI (INTERATTIVO CON ROSTER)
  // -------------------------------------------------------------
  const dmhaGuildCode = `export default function Panel({ engine }) {
  // Database Cacciatori DMHA
  const HUNTERS_DATA = {
    alyssa: {
      name: 'Alyssa Douglas',
      shortName: 'Alyssa',
      rank: 'Rango A',
      rankColor: 'bg-blue-950 text-sky-300',
      role: 'Healer & Field Support',
      squad: 'Douglas Vanguard / Seven Hills Fireteam',
      credits: 4850,
      completed: 18,
      specialty: 'Medicina da Campo, Terapie Anti-Miasma & Incanti Rigenerativi',
      gear: 'Borsa Medica Rinforzata, Fiale Tattiche & Medaglione Autonomo'
    },
    jasper: {
      name: 'Jasper Douglas',
      shortName: 'Jasper',
      rank: 'Rango A',
      rankColor: 'bg-blue-950 text-sky-300',
      role: 'Tech Vanguard & Netrunner',
      squad: 'Douglas Vanguard / Seven Hills Fireteam',
      credits: 3600,
      completed: 14,
      specialty: 'Cyber-Tracciamento Rift, Dispositivi Anti-Interferenza & Katana di Vetro di Drago',
      gear: 'Katana Dragon Glass, Cuffie Acustiche Tattiche & Deck Portatile'
    },
    malachia: {
      name: 'Malachia Douglas',
      shortName: 'Malachia',
      rank: 'Rango S',
      rankColor: 'bg-rose-950 text-rose-300 border border-rose-800',
      role: 'Apex Strike / Assaltatore Primario',
      squad: 'Seven Hills Apex Strike Force',
      credits: 9200,
      completed: 35,
      specialty: 'Neutralizzazione Minacce Classe S, Breccia nei Rift & Caccia ai Capi Branco',
      gear: 'Nocche Fasciate Incantate, Pettorina Tattica Rinforzata DCC'
    },
    noah: {
      name: 'Noah Douglas',
      shortName: 'Noah',
      rank: 'Rango B',
      rankColor: 'bg-purple-950 text-purple-300',
      role: 'Logistica & Field Coordinator',
      squad: 'Douglas Vanguard Support',
      credits: 2100,
      completed: 11,
      specialty: 'Coordinamento Squadre, Negoziazione con Autorità Civili & Mappe Tattiche',
      gear: 'Visore Tattico a Lenti Oscurate, Terminale Radio Criptato'
    },
    mac: {
      name: 'Mackenzie "Mac"',
      shortName: 'Mac',
      rank: 'Rango B',
      rankColor: 'bg-purple-950 text-purple-300',
      role: 'Infiltration & Scout Operativo',
      squad: 'Independent Hunters / Task Force California',
      credits: 2800,
      completed: 16,
      specialty: 'Ricognizione Invisibile, Disinnesco Trappole & Movimento Ombra',
      gear: 'Pugnali da Lancio al Titanio, Mantello Mimetico Anti-Sensori'
    },
    jared: {
      name: 'Jared Thompson',
      shortName: 'Jared',
      rank: 'Rango C',
      rankColor: 'bg-emerald-950 text-emerald-300',
      role: 'Supporto Tattico & Sicurezza',
      squad: 'Seven Hills Reserve Perimeter',
      credits: 1450,
      completed: 7,
      specialty: 'Copertura Linea di Ritiro & Rifornimento Munizioni Silver-Tech',
      gear: 'Fucile Tattico di Precisione, Kit Pronto Soccorso da Campo'
    },
    kaladin: {
      name: 'Kaladin Nargathon',
      shortName: 'Kaladin',
      rank: 'Rango S',
      rankColor: 'bg-rose-950 text-rose-300 border border-rose-800',
      role: 'Comandante Tattico Generale',
      squad: 'DCC Executive Strike Team',
      credits: 12500,
      completed: 48,
      specialty: 'Comando Forze Speciali, Bonifica Minacce Apocrypha & Barriere Difensive',
      gear: 'Lama Cerimoniale Runica, Corazza Integrale DCC Pesante'
    }
  };

  // Rilevamento dinamico dei cacciatori nel party / DOM
  const [showAllGuild, setShowAllGuild] = useState(false);

  const detectedHunterKeys = (() => {
    if (typeof document === 'undefined') return ['alyssa'];
    const pageText = (document.body?.innerText || '').toLowerCase();
    const candidates = ['alyssa', 'jasper', 'malachia', 'noah', 'mac', 'mackenzie', 'jared', 'kaladin'];
    const found = candidates
      .map(k => (k === 'mackenzie' ? 'mac' : k))
      .filter(key => pageText.includes(key));
    const unique = [...new Set(found)];
    return unique.length > 0 ? unique : ['alyssa'];
  })();

  const activeHunterKeys = showAllGuild ? Object.keys(HUNTERS_DATA) : detectedHunterKeys;
  const [selectedHunterKey, setSelectedHunterKey] = useState(() => activeHunterKeys[0] || 'alyssa');

  const currentHunterKey = activeHunterKeys.includes(selectedHunterKey) ? selectedHunterKey : activeHunterKeys[0] || 'alyssa';
  const currHunter = HUNTERS_DATA[currentHunterKey] || HUNTERS_DATA.alyssa;

  // Stato dinamico delle Missioni (Accetta / Prenota / Completa)
  const [userCredits, setUserCredits] = useState(currHunter.credits);
  const [missionsCompletedCount, setMissionsCompletedCount] = useState(currHunter.completed);
  const [activeMission, setActiveMission] = useState(null); // null oppure oggetto missione

  const AVAILABLE_MISSIONS = [
    {
      id: 'm1',
      title: 'Scansione Baia di Blackwood & Docks',
      desc: 'Pattugliamento anomalia miasma Classe 1 lungo i moli fluviali.',
      rankReq: 'Rango C',
      rewardCr: 250,
      rewardText: '250 Crediti · Rango C'
    },
    {
      id: 'm2',
      title: 'Bonifica Hive Sotterraneo Cable District',
      desc: 'Incursione coordinata per contenere un focolaio di ratti abissali.',
      rankReq: 'Rango B',
      rewardCr: 600,
      rewardText: '600 Crediti · Rango B'
    },
    {
      id: 'm3',
      title: 'Fornitura Nuclei Abissali alla Gilda',
      desc: 'Recupero 3 core energetici integri tra i vecchi depositi industriali.',
      rankReq: 'Rango C',
      rewardCr: 400,
      rewardText: '400 Crediti · Rango C'
    },
    {
      id: 'm4',
      title: 'Scorta Convoglio Medico HSK nei Bassifondi',
      desc: 'Protezione furgone medicinali e scorte anti-ferormonali verso la clinica.',
      rankReq: 'Rango B',
      rewardCr: 750,
      rewardText: '750 Crediti · Rango B'
    },
    {
      id: 'm5',
      title: 'Tracciamento Faglia Anomala Seven Hills',
      desc: 'Indagine rapida su increspatura dimensionale ad alta intensità a nord.',
      rankReq: 'Rango A',
      rewardCr: 1200,
      rewardText: '1.200 Crediti · Rango A'
    }
  ];

  const handleAcceptMission = (mission) => {
    setActiveMission(mission);
    try {
      if (typeof engine.runCommand === 'function') {
        engine.runCommand('cmd_accept_quest', { title: mission.title });
      }
    } catch (e) {}
  };

  const handleCompleteMission = () => {
    if (!activeMission) return;
    setUserCredits(prev => prev + activeMission.rewardCr);
    setMissionsCompletedCount(prev => prev + 1);
    setActiveMission(null);
  };

  const handleAbandonMission = () => {
    setActiveMission(null);
  };

  return (
    <div className="space-y-3 font-sans text-xs select-none">
      <Card className="bg-black border-zinc-800 text-zinc-300 shadow-xl overflow-hidden">
        <CardHeader className="px-4 py-3 bg-neutral-900 border-b border-zinc-800 flex flex-row items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="text-base">⚔️</span>
            <div>
              <CardTitle className="text-sm font-bold text-zinc-100">DMHA · Registro Caccia & Gilda</CardTitle>
              <CardDescription className="text-[10px] text-sky-300 font-medium">{currHunter.squad}</CardDescription>
            </div>
          </div>
          <Badge className={'font-bold text-xs px-2.5 py-0.5 border-0 ' + currHunter.rankColor}>
            {currHunter.rank}
          </Badge>
        </CardHeader>

        {/* Tab di Selezione Membri del Party registrati alla Gilda */}
        <div className="bg-neutral-950 px-4 py-2 border-b border-zinc-800/80 flex items-center justify-between gap-2 overflow-x-auto">
          <div className="flex items-center gap-1.5 overflow-x-auto pb-0.5">
            {activeHunterKeys.map(k => {
              const h = HUNTERS_DATA[k];
              const isSelected = k === currentHunterKey;
              return (
                <button
                  key={k}
                  onClick={() => {
                    setSelectedHunterKey(k);
                    setUserCredits(h.credits);
                    setMissionsCompletedCount(h.completed);
                  }}
                  className={'px-2.5 py-1 rounded-md text-xs font-semibold transition-all whitespace-nowrap flex items-center gap-1 ' + (isSelected ? 'bg-amber-600 text-white shadow-sm' : 'bg-neutral-900 text-zinc-400 hover:text-zinc-200 hover:bg-neutral-800')}
                >
                  <span>{h.shortName}</span>
                  <span className="text-[9px] bg-neutral-950/80 px-1 rounded font-mono">{h.rank}</span>
                </button>
              );
            })}
          </div>

          <button
            onClick={() => setShowAllGuild(prev => !prev)}
            title={showAllGuild ? 'Filtra solo cacciatori del party' : 'Mostra tutti i cacciatori'}
            className="text-[10px] text-zinc-400 hover:text-amber-300 font-medium px-1.5 py-0.5 rounded border border-zinc-800 bg-neutral-900 shrink-0 whitespace-nowrap"
          >
            {showAllGuild ? 'Filtra Party' : '+ Roster'}
          </button>
        </div>

        <CardContent className="p-4 space-y-3.5">
          {/* Dettagli Profilo Cacciatore Selezionato */}
          <div className="bg-neutral-900 rounded-lg p-3.5 border-0 space-y-1.5">
            <div className="flex items-center justify-between">
              <span className="font-bold text-sm text-zinc-100">{currHunter.name}</span>
              <Badge className="bg-neutral-950 text-amber-300 border border-zinc-800 text-[10px] font-semibold px-2 py-0.5">
                {currHunter.role}
              </Badge>
            </div>
            <p className="text-[11px] text-zinc-300 leading-relaxed pt-0.5"><span className="text-zinc-400 font-medium">Specialità:</span> {currHunter.specialty}</p>
            <p className="text-[10px] text-zinc-400"><span className="text-zinc-500 font-medium">Equipaggiamento:</span> {currHunter.gear}</p>
          </div>

          {/* Crediti & Cacce Concluse */}
          <div className="grid grid-cols-2 gap-2.5">
            <div className="bg-neutral-900 rounded-lg p-3.5 border-0 text-center space-y-1">
              <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Crediti Gilda Personali</p>
              <p className="text-sm font-bold text-amber-300">{userCredits} <span className="text-[10px] font-normal text-zinc-400">CR</span></p>
            </div>
            <div className="bg-neutral-900 rounded-lg p-3.5 border-0 text-center space-y-1">
              <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Cacce Concluse</p>
              <p className="text-sm font-bold text-emerald-400">{missionsCompletedCount} <span className="text-[10px] font-normal text-zinc-400">Missioni</span></p>
            </div>
          </div>

          {/* Stato Missione Attiva con Controlli */}
          <div className="bg-neutral-900 rounded-lg p-3.5 border-0 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-zinc-400 font-medium text-xs">Stato Incarico Attivo:</span>
              {activeMission ? (
                <Badge className="bg-yellow-900 text-yellow-300 border-0 text-[10px] font-bold px-2 py-0.5 animate-pulse">
                  IN CORSO
                </Badge>
              ) : (
                <Badge className="bg-neutral-950 text-zinc-400 border border-zinc-800 text-[10px] font-medium px-2 py-0.5">
                  STANDBY / DISPONIBILE
                </Badge>
              )}
            </div>

            {activeMission ? (
              <div className="pt-2 border-t border-zinc-800 space-y-2">
                <p className="font-semibold text-xs text-yellow-300 leading-snug">{activeMission.title}</p>
                <p className="text-[11px] text-zinc-300">{activeMission.desc}</p>
                <div className="flex items-center justify-between pt-1">
                  <span className="text-[10px] text-amber-300 font-medium">Ricompensa: +{activeMission.rewardCr} CR</span>
                  <div className="flex gap-1.5">
                    <Button
                      size="sm"
                      onClick={handleCompleteMission}
                      className="h-7 text-xs bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-2.5"
                    >
                      Completa (+{activeMission.rewardCr} CR)
                    </Button>
                    <Button
                      size="sm"
                      variant="ghost"
                      onClick={handleAbandonMission}
                      className="h-7 text-xs text-rose-400 hover:text-rose-300 hover:bg-neutral-800 px-2"
                    >
                      Abbandona
                    </Button>
                  </div>
                </div>
              </div>
            ) : (
              <p className="text-[10px] text-zinc-400 pt-0.5">Seleziona e prenota un contratto dalla bacheca sottostante per iniziare.</p>
            )}
          </div>

          {/* Bacheca Contratti & Opportunita Lavorative */}
          <div className="space-y-2">
            <div className="flex items-center justify-between px-0.5">
              <p className="text-[10px] uppercase font-bold tracking-wider text-zinc-400">Bacheca Contratti Disponibili</p>
              <span className="text-[10px] text-sky-300 font-mono">DMHA Board</span>
            </div>

            {AVAILABLE_MISSIONS.map((m) => {
              const isThisActive = activeMission && activeMission.id === m.id;
              return (
                <div key={m.id} className="bg-neutral-900 hover:bg-zinc-800/90 transition-colors rounded-lg p-3.5 border border-zinc-800/60 space-y-2">
                  <div className="flex items-center justify-between gap-2">
                    <p className="font-semibold text-xs text-zinc-200 leading-snug">{m.title}</p>
                    <Badge className="bg-neutral-950 text-sky-300 border border-zinc-800 text-[10px] font-semibold px-2 py-0.5 shrink-0">
                      {m.rankReq}
                    </Badge>
                  </div>
                  <p className="text-[11px] text-zinc-400 leading-relaxed">{m.desc}</p>
                  
                  <div className="flex items-center justify-between pt-1 border-t border-zinc-800/60">
                    <span className="text-[10px] font-semibold text-amber-300">{m.rewardText}</span>
                    {isThisActive ? (
                      <Badge className="bg-yellow-900 text-yellow-200 border-0 text-[10px] font-bold px-2 py-0.5">
                        PRENOTATA
                      </Badge>
                    ) : (
                      <Button
                        size="sm"
                        disabled={Boolean(activeMission)}
                        onClick={() => handleAcceptMission(m)}
                        className={'h-7 text-xs font-semibold px-3 ' + (activeMission ? 'bg-zinc-800 text-zinc-500 cursor-not-allowed' : 'bg-amber-600 hover:bg-amber-500 text-white')}
                      >
                        {activeMission ? 'Occupato' : 'Accetta / Prenota'}
                      </Button>
                    )}
                  </div>
                </div>
              );
            })}
          </div>

          {/* Inventario Bottino / Materiali */}
          <div className="bg-neutral-900 rounded-lg p-3 border-0 flex items-center justify-between text-[11px]">
            <span className="text-zinc-400">Inventario Bottino / Cores:</span>
            <Badge className="bg-blue-950 text-sky-300 border-0 font-mono text-[10px] px-2 py-0.5">3x Abyssal Core · 2x Silver-Dust</Badge>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}`;

  // 2. Update panel codes in engine definition
  const pAcademics = def.ui_panels.find(p => p.id === 'panel_succ_academics');
  if (pAcademics) pAcademics.code = succAcademicsCode;

  const pGuild = def.ui_panels.find(p => p.id === 'panel_dmha_guild');
  if (pGuild) pGuild.code = dmhaGuildCode;

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

  // 4. Publish engine
  const pubRes = await fetch('https://app.wyvern.chat/api/story-engines/engine_HCTPXhL8xr89wUY9r9dYU/publish', {
    method: 'POST',
    headers,
    body: JSON.stringify({ expected_version: putData.version })
  });
  const pubData = await pubRes.json();
  console.log('PUBLISH status:', pubRes.status, 'New published revision:', pubData.published_revision_id);
}

updateAllPanels().catch(console.error);

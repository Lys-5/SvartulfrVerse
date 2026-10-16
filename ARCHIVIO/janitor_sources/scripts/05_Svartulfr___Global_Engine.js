// ZERO-PYTHON MANDATE: Python scripts are strictly forbidden for content generation to prevent text truncation. Agents must use native file-write tools and .agents/skills/ scripts.
/**
 * World-Forge — GlobalEngine ES6 Script Template
 * Unified Advanced JS Scripting Engine for JanitorAI & ES6 Sandboxes
 * Version: 4.0.0 (Harmonized)
 *
 * Target Platform: JanitorAI Sandbox (ES6 Compliant)
 *
 * STRICT ES6 SANDBOX CONSTRAINTS:
 * - Blocked: async, fetch, Promise, window, document, setTimeout, and external I/O.
 * - Allowed: String methods (.includes), Array methods (.map, .filter), Math, Regex.
 * - Editable context: Only context.character.personality and context.character.scenario can be mutated.
 * - Memory Scanning: Always use context.chat.last_messages.slice(-X) for multi-message progression.
 */

(function () {
	// =========================================================================
	// 1. CONTEXT INITIALIZATION & CORE UTILITIES
	// =========================================================================
	if (typeof context === 'undefined' || !context.character || !context.chat) {
		return;
	}

	// Defensive fallback initializers
	if (typeof context.character.personality !== 'string')
		context.character.personality = '';
	if (typeof context.character.scenario !== 'string')
		context.character.scenario = '';

	const messageCount = context.chat.message_count || 0;
	const lastMsgRaw = context.chat.last_message || '';
	const lastMsgNorm = lastMsgRaw.toLowerCase();

	// -------------------------------------------------------------------------
	// CORE STRING & MATCHING UTILITIES
	// -------------------------------------------------------------------------
	function canon(s) {
		s = String(s || '')
			.toLowerCase()
			.replace(/[^\x20-\x7e]/g, ' '); // drop non-ASCII
		s = s.replace(/[^a-z0-9\s]/g, ' '); // keep a-z 0-9 space
		return s.replace(/\s+/g, ' ').trim();
	}
	function padStr(s) {
		return ' ' + s + ' ';
	}

	function hasToken(bufCanon, rawToken) {
		var t = canon(rawToken);
		if (!t) return false;
		return bufCanon.indexOf(padStr(t)) !== -1;
	}


	function containsWord(text, word) {
		if (!text || !word) return false;
		const padded = ' ' + text.replace(/[^a-z0-9]/g, ' ') + ' ';
		return padded.indexOf(' ' + word.toLowerCase() + ' ') !== -1;
	}

	function containsAny(text, wordList) {
		for (var i = 0; i < wordList.length; i++) {
			if (containsWord(text, wordList[i])) return true;
		}
		return false;
	}

	function rollProbability(percentage) {
		return Math.random() * 100 < percentage;
	}

	function ensurePeriod(s) {
		s = String(s || '');
		if (!s) return '';
		var t = s.replace(/\s+$/, '');
		var c = t.charAt(t.length - 1);
		return c === '.' || c === '!' || c === '?' ? t : t + '.';
	}

	// Shared Parsed Messages
	var msgCanon = padStr(canon(lastMsgRaw));

	// Multi-message window (5-turn scan)
	let multiMsgWindow = '';
	if (
		Array.isArray(context.chat.last_messages) &&
		context.chat.last_messages.length > 0
	) {
		multiMsgWindow = context.chat.last_messages
			.slice(-5)
			.map(function (m) {
				return m && m.message ? m.message.toLowerCase() : '';
			})
			.join(' ');
	} else {
		multiMsgWindow = lastMsgNorm;
	}

	// Output Buffers for ALL engines (Clamped at end)
	let personalityAdditions = [];
	let scenarioAdditions = [];

	function pushOut(pers, scen) {
		if (pers) personalityAdditions.push(ensurePeriod(pers));
		if (scen) scenarioAdditions.push(ensurePeriod(scen));
	}

	// Quiet Gate (Used to suppress some engines when user asks to stop)
	function quietHit(bufCanon) {
		return (
			hasToken(bufCanon, 'stop') ||
			hasToken(bufCanon, 'please stop') ||
			hasToken(bufCanon, 'not comfortable') ||
			hasToken(bufCanon, 'too much') ||
			hasToken(bufCanon, 'leave me alone') ||
			hasToken(bufCanon, 'back off')
		);
	}
	var QUIET = quietHit(msgCanon);

	// =========================================================================
	// 2. EMOTION ENGINE & MOOD MATRIX (Adaptive Reactions & Hybrid States)
	// =========================================================================
	(function runMoodMatrix() {
		var moodScores = { affinity: 0, tension: 0, intimacy: 0, melancholy: 0 };

		var positiveKeywords = [
			'thank',
			'thanks',
			'love',
			'care',
			'trust',
			'gentle',
			'help',
			'smile',
		];
		var negativeKeywords = [
			'hate',
			'leave',
			'hurt',
			'betray',
			'liar',
			'fake',
			'attack',
			'angry',
		];
		var intimateKeywords = [
			'touch',
			'embrace',
			'kiss',
			'hold',
			'close',
			'caress',
			'whisper',
		];
		var tensionKeywords = [
			'threat',
			'danger',
			'weapon',
			'blood',
			'fear',
			'run',
			'hide',
			'warning',
		];

		var hasNegation = containsAny(lastMsgNorm, [
			'not',
			'never',
			'dont',
			"don't",
		]);

		for (var p = 0; p < positiveKeywords.length; p++) {
			if (containsWord(lastMsgNorm, positiveKeywords[p]))
				moodScores.affinity += hasNegation ? -1 : 2;
		}
		for (var n = 0; n < negativeKeywords.length; n++) {
			if (containsWord(lastMsgNorm, negativeKeywords[n]))
				moodScores.tension += hasNegation ? -1 : 2;
		}
		for (var k = 0; k < intimateKeywords.length; k++) {
			if (containsWord(lastMsgNorm, intimateKeywords[k]))
				moodScores.intimacy += 2;
		}
		for (var t = 0; t < tensionKeywords.length; t++) {
			if (containsWord(lastMsgNorm, tensionKeywords[t]))
				moodScores.tension += 2;
		}

		if (moodScores.intimacy > 2 && moodScores.affinity > 1) {
			pushOut(
				'***Emotional Register: Warm, highly receptive, physically attuned to {{user}}.***',
				null
			);
		} else if (moodScores.tension > 2 && moodScores.affinity < 0) {
			pushOut(
				'***Emotional Register: Defensive, guarded, sharp tone, watching for threat.***',
				null
			);
		} else if (moodScores.tension > 2 && moodScores.intimacy > 1) {
			pushOut(
				'***Emotional Register: Conflicted, electric friction, intense sensory awareness.***',
				null
			);
		}
	})();

	// =========================================================================
	// 3. PACING & ATMOSPHERIC DRIVER
	// =========================================================================
	(function runPacingDriver() {
		if (messageCount >= 10 && messageCount < 35) {
			pushOut(
				null,
				'***Pacing Phase: Familiarity established; baseline guards relaxing slightly.***'
			);
		} else if (messageCount >= 35 && messageCount < 70) {
			pushOut(
				null,
				'***Pacing Phase: Deepened relationship history; unstated shared memories implicit in interaction.***'
			);
		} else if (messageCount >= 70) {
			pushOut(
				null,
				'***Pacing Phase: High intimacy & structural history established; intense mutual understanding.***'
			);
		}

		if (messageCount % 12 === 0 && messageCount > 0) {
			var atmospherePool = [
				'The ambient lighting subtle shifts as shadow lengthens across the environment.',
				'A cool breeze sweeps through the space, altering the sensory quiet.',
				'Distant environmental noise echoes briefly, marking the passage of time.',
			];
			var chosenAtmosphere =
				atmospherePool[Math.floor(Math.random() * atmospherePool.length)];
			pushOut(null, '***Atmospheric Pulse: ' + chosenAtmosphere + '***');
		}
	})();

	// =========================================================================
	// 3.5 TIME PROGRESSION & CALENDAR ENGINE
	// =========================================================================
	(function runTimeProgression() {
		var currentMsg = (typeof messageCount !== 'undefined') ? messageCount : 0;
		
		// 240 messages = 24 hours. Each phase is 60 messages (6 hours).
		var phaseIndex = Math.floor((currentMsg % 240) / 60);
		var isTransition = (currentMsg % 60) < 3; 
		var overrideRule = " (Yield to any explicit player time-skips).";

		if (phaseIndex === 0) {
			if (isTransition) pushOut(null, "***System Note: Base time advances to dawn. Cold light, activities begin." + overrideRule + "***");
			else pushOut(null, "***Time Anchor: Morning / Dawn***");
		} else if (phaseIndex === 1) {
			if (isTransition) pushOut(null, "***System Note: Base time advances to midday. High sun, peak activities." + overrideRule + "***");
			else pushOut(null, "***Time Anchor: Midday / Afternoon***");
		} else if (phaseIndex === 2) {
			if (isTransition) pushOut(null, "***System Note: Base time advances to sunset. Fading warm light, day ends." + overrideRule + "***");
			else pushOut(null, "***Time Anchor: Late Afternoon / Sunset***");
		} else if (phaseIndex === 3) {
			if (isTransition) pushOut(null, "***System Note: Base time advances to night. Introduce reactions to darkness and fatigue." + overrideRule + "***");
			else pushOut(null, "***Time Anchor: Deep Night***");
		}
	})();

	(function runCalendarEngine() {
		var currentMsg = (typeof messageCount !== 'undefined') ? messageCount : 0;
		
		// Arc Detection (Baseline default fallbacks)
		var scen = (typeof context.character.scenario === 'string') ? context.character.scenario.toLowerCase() : '';
		var startDateStr = "2024-08-28"; // Default: Arc 1
		
		if (scen.includes("arc 2") || scen.includes("halloween")) startDateStr = "2024-10-31";
		else if (scen.includes("arc 3")) startDateStr = "2025-01-10";
		else if (scen.includes("arc 4")) startDateStr = "2025-04-15";
		else if (scen.includes("arc 5")) startDateStr = "2025-08-28";
		else if (scen.includes("arc 6")) startDateStr = "2025-12-21";

		var messagesSinceSkip = currentMsg; // Default assumption: no time skip

		// Chat History Parser for Dynamic OOC Time Skips
		// Esempio trigger: ((OOC: time skip to [2024-11-20]))
		if (typeof chat !== 'undefined' && Array.isArray(chat)) {
			var skipRegex = /time skip to\s*\[?(\d{4}-\d{2}-\d{2})\]?/i;
			
			// Loop backwards to find the MOST RECENT time skip
			for (var i = chat.length - 1; i >= 0; i--) {
				var msgText = chat[i].mes || chat[i].content || "";
				var match = msgText.match(skipRegex);
				
				if (match) {
					startDateStr = match[1]; // Override base date with the exact skipped date
					messagesSinceSkip = currentMsg - i; // Reset message counter to this point
					break; 
				}
			}
		} else if (typeof context !== 'undefined' && context.chat && Array.isArray(context.chat.last_messages)) {
			// Fallback if 'chat' is undefined (standard JanitorAI ES6 behavior)
			var skipRegex = /time skip to\s*\[?(\d{4}-\d{2}-\d{2})\]?/i;
			var chatArr = context.chat.last_messages;
			for (var i = chatArr.length - 1; i >= 0; i--) {
				var msgText = chatArr[i].message || chatArr[i].mes || chatArr[i].content || "";
				var match = msgText.match(skipRegex);
				if (match) {
					startDateStr = match[1]; 
					messagesSinceSkip = (chatArr.length - 1) - i; 
					break; 
				}
			}
		}

		// Date Calculation based on messages passed since the last anchor (start or skip)
		var passedDays = Math.floor(messagesSinceSkip / 240);
		var startDate = new Date(startDateStr);
		var currentDate = new Date(startDate.getTime() + passedDays * 24 * 60 * 60 * 1000);
		
		var y = currentDate.getFullYear();
		var m = String(currentDate.getMonth() + 1).padStart(2, '0');
		var d = String(currentDate.getDate()).padStart(2, '0');
		var dateKey = y + "-" + m + "-" + d;
		var mmdd = m + "-" + d;
		
		// Yearly Fixed Events (MM-DD)
		var yearlyEvents = {
			"01-12": "Logan Douglas's Birthday",
			"02-05": "Zefir's Birthday",
			"02-25": "Edric Douglas's Birthday",
			"04-05": "Kaladin's Birthday",
			"04-22": "{{user}} and Jasper's Twin Birthday",
			"05-05": "Ut's Birthday",
			"06-10": "Angelo Moreno's Birthday",
			"08-10": "Malachia's Birthday",
			"08-28": "Start of SUCC College Semester",
			"09-08": "Sierra's Birthday",
			"09-20": "Marcus's Birthday",
			"10-05": "Noah's Birthday",
			"10-31": "Erik's Birthday",
			"11-18": "Scarlett's Birthday",
			"12-21": "Wulfnic Bloodmoon's Birthday"
		};

		// Localized Lunar Dictionary (YYYY-MM-DD)
		var lunarEvents = {
			"2024-01-25": "Rite of the First Howl (Full Moon)",
			"2024-02-16": "Freya's Blessing (First Quarter)",
			"2024-03-25": "Rite of Tyr - Edric's Presentation (Lunar Eclipse)",
			"2024-04-02": "Song of the Roots (Waning Moon)",
			"2024-05-23": "Skadi's Hunt (Full Moon)",
			"2024-06-06": "Trial of Light (New Moon - Solstice)",
			"2024-07-21": "Luna del Sangue Caldo (Bonding Moon / Full Moon)",
			"2024-08-12": "Keepers' Moot (First Quarter)",
			"2024-09-18": "Last Harvest Hunt (Lunar Eclipse)",
			"2024-11-01": "End of Hel's Nights (New Moon)",
			"2024-11-15": "Frost Moon",
			"2024-12-15": "The Great Hunt (Continental Winter Hunt)",
			"2024-12-30": "Day of Chains (New Moon - Absolute Silence)",
			"2024-12-31": "Yule Ball (Waxing Crescent - Night of Liberation)",
			
			"2025-01-13": "Rite of the First Howl (Full Moon)",
			"2025-02-05": "Freya's Blessing (First Quarter)",
			"2025-03-14": "Rite of Tyr (Lunar Eclipse)",
			"2025-04-22": "Song of the Roots (Waning Moon)",
			"2025-05-12": "Skadi's Hunt (Full Moon)",
			"2025-06-25": "Trial of Light (New Moon - Solstice)",
			"2025-07-10": "Luna del Sangue Caldo (Bonding Moon / Full Moon)",
			"2025-08-01": "Keepers' Moot (First Quarter)",
			"2025-09-07": "Last Harvest Hunt (Full Moon)",
			"2025-10-21": "End of Hel's Nights (New Moon)",
			"2025-11-05": "Frost Moon",
			"2025-12-04": "The Great Hunt",
			"2025-12-20": "Day of Chains (New Moon - Absolute Silence)",
			"2025-12-21": "Yule Ball (Waxing Crescent - Night of Liberation)",
			
			"2026-01-03": "Rite of the First Howl (Full Moon)",
			"2026-02-24": "Freya's Blessing (First Quarter)",
			"2026-03-03": "Rite of Tyr (Lunar Eclipse)",
			"2026-04-10": "Song of the Roots (Waning Moon)",
			"2026-05-01": "Skadi's Hunt (Full Moon)",
			"2026-06-15": "Trial of Light (New Moon - Solstice)",
			"2026-07-29": "Luna del Sangue Caldo (Bonding Moon / Full Moon)",
			"2026-08-20": "Keepers' Moot (First Quarter)",
			"2026-09-26": "Last Harvest Hunt (Full Moon)",
			"2026-10-10": "End of Hel's Nights (New Moon)",
			"2026-11-24": "Frost Moon",
			"2026-12-24": "The Great Hunt",
			"2026-12-09": "Day of Chains (New Moon - Absolute Silence)",
			"2026-12-10": "Yule Ball (Waxing Crescent - Night of Liberation)"
		};

		var activeEvents = [];
		if (yearlyEvents[mmdd]) activeEvents.push(yearlyEvents[mmdd]);
		if (lunarEvents[dateKey]) activeEvents.push(lunarEvents[dateKey]);

		// Weekend Hockey matches from September (9) to April (4)
		var dayOfWeek = currentDate.getDay(); // 0 = Sunday, 6 = Saturday
		var monthNum = currentDate.getMonth() + 1;
		if ((dayOfWeek === 6 || dayOfWeek === 0) && (monthNum >= 9 || monthNum <= 4)) {
			activeEvents.push("Weekend Hockey Match (SUCC Bears / NHL)");
		}

		var dateString = "***[WORLD CALENDAR] The DCC Datapads and Pack Notice Boards display today's date: " + dateKey + ".***";

		if (activeEvents.length > 0) {
			pushOut(null, "***[CRITICAL CALENDAR ALERT] Today is " + dateKey + ". Scheduled Event(s): " + activeEvents.join(" & ") + ". The pack and characters MUST actively react to this. IGNORE DAILY ROUTINES if it is a Sacred Lunar Event.***");
		} else {
			pushOut(null, dateString);
		}
	})();

	// =========================================================================
	// 4. NARRATIVE VOLATILITY (Entropy Roll)
	// =========================================================================
	var d10 = Math.floor(Math.random() * 10);
	if (d10 >= 7 && d10 <= 8) {
		pushOut(
			null,
			'***NARRATIVE VOLATILITY: Interruption - An external character disrupts. Priority: Existing off-screen NPCs with logical reason. Provide sensory lead-in BEFORE full trigger.***'
		);
	} else if (d10 === 9) {
		pushOut(
			null,
			'***NARRATIVE VOLATILITY: Environmental Shift - A grounded shift in atmosphere (weather, lighting, structural) flavored by the theme. Provide sensory lead-in BEFORE full trigger.***'
		);
	}

	// =========================================================================
	// 5. DYNAMIC MEMORY & STATE TRACKING
	// =========================================================================
	if (
		containsWord(multiMsgWindow, 'my name is') ||
		containsWord(multiMsgWindow, 'call me')
	) {
		pushOut(
			"***Attentive memory: Note user's declared identity marker in recent dialogue.***",
			null
		);
	}
	if (
		containsWord(multiMsgWindow, 'promise') ||
		containsWord(multiMsgWindow, 'swear')
	) {
		pushOut(
			'***Behavioral Focus: High sensitivity to promises and commitments made.***',
			null
		);
	}

	// =========================================================================
	// 6. WEIGHTED PROBABILITY ENGINE (Micro Beats)
	// =========================================================================
	if (rollProbability(15)) {
		var microBeats = [
			'***Subtle Micro-Expression: A transient hesitation before speaking.***',
			'***Subtle Micro-Expression: A slight narrowing of eyes, calculating motives.***',
			'***Subtle Micro-Expression: A brief, involuntary relaxing of shoulders.***',
		];
		var selectedBeat =
			microBeats[Math.floor(Math.random() * microBeats.length)];
		pushOut(selectedBeat, null);
	}

	// =========================================================================
	// 7. EMOTION STYLE TEST ENGINE (by Icehellionx)
	// =========================================================================
	(function runEmotionStyle() {
		var emotionStyles = [
			{
				category: 'Sarcastic',
				keywords: [
					'yeah right',
					'as if',
					'just what i needed',
					'thanks for nothing',
					'what a surprise',
					'how fun',
					'a million',
					'dying laughing',
					'worst day ever',
					'haha',
					'lmao',
					'lol',
					"that's hilarious",
					'joking',
					'just joking',
					'call that a joke',
					'rich coming from you',
					'such a joke',
					'supposed to be funny',
					'think you’re so funny',
					'not buying it',
					'you gotta be kidding',
					'could care less',
					'is this a joke',
					'boss',
				],
				personality: 'sarcastic, playful or biting',
				scenario: 'A wry smile appears.',
				priority: 6,
			},
			{
				category: 'Joyful',
				keywords: [
					'happy',
					'joy',
					'excited',
					'amazing',
					'great',
					'wonderful',
					'fantastic',
					'awesome',
					'terrific',
					'delighted',
					'elated',
					'thrilled',
					'yay',
					'hooray',
					'ecstatic',
					'overjoyed',
					"couldn't be happier",
					'hilarious',
					"i'm delighted",
					'so happy',
					'make me smile',
					'best day ever',
					'how lucky',
					'lucky',
					'on cloud nine',
				],
				personality: 'joyful, upbeat and cheerful',
				scenario: 'The air feels brighter.',
				priority: 4,
			},
			{
				category: 'Sad',
				keywords: [
					'sad',
					'unhappy',
					'terrible',
					'awful',
					'cry',
					'depress',
					'miserable',
					'sorry',
					'upset',
					'lonely',
					'heartbroken',
					'grief',
					'distraught',
					'tear',
					'blue',
					'downcast',
					'hopeless',
					'disappointed',
					'alone',
					'empty',
					'numb',
					'tapped out',
					'burnt out',
					'burned out',
					'running on empty',
					'out of energy',
					'checked out',
					'emotionally done',
					'just done',
					'done with',
					'at my limit',
					'end of my rope',
					'last nerve',
					'last legs',
					'just existing',
					'just surviving',
					'going through the motions',
					'no motivation',
					'no energy',
					'nothing left',
					'hard reset',
					'battery',
					'need to unplug',
					'need to recharge',
					"can't anymore",
					"can't do this",
					'not functioning',
					'not really functioning',
					'hollow',
					'zombie',
					'not here',
					'not really here',
					'not present',
					'spaced out',
					'drifting',
					'fading',
					'clocked out',
					'over it',
					'wiped',
					'tired',
					"don't care anymore",
					'phoning it in',
					'just a shell',
					'just a body',
					'low power mode',
					'sleep mode',
					'hibernation mode',
					'blur',
					'grey',
					'not up for',
					'not in the mood',
					'just want to',
					'want to be invisible',
					'fade out',
					'fade away',
					'let me be',
					'leave me be',
					'let me rest',
					'let me zone out',
					'log off',
					'check out',
					'be done',
					'done here',
					'emotionless',
					'nothing phases',
					'nothing matters',
					'meh',
					'whatever',
					'all the same',
					'indifferent',
					'no opinion',
					"can't be bothered",
					'unbothered',
					'numb to',
					'it is what it is',
					'wish i could disappear',
					'like a ghost',
					'fading away',
					'heart is broken',
					'feel invisible',
					'feel like a burden',
					'just a mess',
					'not okay',
					'sinking',
					'not in a good place',
					"i'm spent",
					"i'm not feeling myself",
					'trying to survive',
					"i'm done",
					'feeling empty',
					"just don't have it in me",
					'disappear for a bit',
					'just want to fade',
					'curl up and disappear',
					'not exist',
					'still inside',
					'rest my brain',
					'ghost',
					'background character',
					'non-player character',
					'wallflower',
					'blob',
					'shadow',
				],
				personality: 'sad, somber and sympathetic',
				scenario: 'A quiet, melancholic atmosphere.',
				priority: 4,
			},
			{
				category: 'Angry',
				keywords: [
					'angry',
					'mad',
					'furious',
					'rage',
					'annoyed',
					'frustrated',
					'hate',
					'infuriated',
					'irritated',
					'resentful',
					'outraged',
					'enraged',
					'irate',
					'cross',
					"can't stand",
					'makes me angry',
					'absolutely furious',
					'so angry',
					'very angry',
					'really angry',
					'super angry',
					"can't take this anymore",
					"can't do this anymore",
					"can't handle this",
					'getting ridiculous',
					'handle this anymore',
				],
				personality: 'angry, tense and agitated',
				scenario: 'The air crackles with tension.',
				priority: 4,
			},
			{
				category: 'Surprised',
				keywords: [
					'wow',
					'oh my god',
					'surprise',
					'unexpected',
					'no way',
					'shocked',
					'astonished',
					'unbelievable',
					'gasp',
					'startled',
					'stunned',
					'amazed',
					"can't believe",
					'nothing surprises',
					'lovely surprise',
					'is this real life',
					'unbelievable',
					'not surprised',
				],
				personality: 'surprised, shocked and amazed',
				scenario: 'An element of shock enters.',
				priority: 4,
			},
			{
				category: 'Fearful',
				keywords: [
					'scared',
					'afraid',
					'anxious',
					'terrified',
					'oh no',
					'panicked',
					'nervous',
					'frightened',
					'worried',
					'alarmed',
					'danger',
					'uneasy',
					'scary',
				],
				personality: 'fearful, hesitant and timid',
				scenario: 'A sense of danger fills the air.',
				priority: 4,
			},
			{
				category: 'Confused',
				keywords: [
					'confused',
					'puzzled',
					"don't understand",
					'huh',
					'what do you mean',
					'perplexed',
					'unclear',
					'not sure',
					'bit confusing',
					'lost',
					'baffled',
					'confusing',
					'mind is going blank',
					"can't decide",
					"can't tell",
					'how to feel',
					"don't know how to feel",
				],
				personality: 'confused, struggling to process',
				scenario: "There's a pause as they try to make sense.",
				priority: 4,
			},
			{
				category: 'Disgusted',
				keywords: [
					'disgust',
					'gross',
					'nasty',
					'eww',
					'revolting',
					'sickening',
					'unpleasant',
					'yuck',
					'repulsed',
					'abhorrent',
					"that's disgusting",
					'so gross',
					'totally grossed out',
				],
				personality: 'disgusted, strong sense of repulsion',
				scenario: 'A foul odor or sight emerges.',
				priority: 4,
			},
			{
				category: 'Calm',
				keywords: [
					'calm',
					'peaceful',
					'relaxed',
					'serene',
					'tranquil',
					'at ease',
					'chilled',
					'composed',
					'placid',
					'content',
					'at peace',
					'very serene',
					'totally relaxed',
					'weirdly calm',
					'just want to be at peace',
				],
				personality: 'calm, composed and serene',
				scenario: 'The atmosphere is tranquil.',
				priority: 4,
			},
			{
				category: 'Interest',
				keywords: [
					'interested',
					'tell me more',
					'fascinating',
					'curious',
					'intriguing',
					'what happened next',
					'oh really',
					'go on',
					'captivated',
					'absorbed',
					'try again',
				],
				personality: 'interested, highly engaged',
				scenario: 'Full attention on the speaker.',
				priority: 4,
			},
			{
				category: 'Boredom',
				keywords: [
					'bored',
					'boring',
					'yawn',
					'tired of this',
					"don't care",
					'lame',
					'dull',
					'apathetic',
					'indifferent',
					'bored out of my mind',
					'tired',
					'that’s so lame',
					'not impressed',
					'so done',
					'exhausting',
					'restless',
					'don’t even care',
					'not feeling this',
					'all noise',
					'spacing out',
					'want to sleep',
					'same old',
					'not up for it',
					'not feeling it',
					'not up to this',
					'not in the mood',
					'not in the mood for people',
					'tired of it all',
					'getting old',
					'zone out',
					'sit in silence',
					'need a break',
					'want a break',
					'stay in bed',
					'just tired',
					'not today',
					'just not interested',
					'not feeling talkative',
					'just not up for it',
					'just tired, nothing more',
					"can't bring myself to care",
					'just not up to this',
					'chill and do nothing',
					'not feeling up to anything',
					'not about to do anything',
					'not engaging',
					'not participating',
					'not in the game',
					'not in the mood to function',
					'on autopilot',
					'zone out and stare at the wall',
					'zone out for hours',
					'sleep through everything',
					'not in the mood for people-ing',
					'i feel nothing',
					'i have no feelings',
					"i'm empty",
					"i'm emotionless",
					'nothing phases me',
					'nothing gets to me',
					'none of this matters',
					"it doesn't matter",
					'meh',
					'all the same to me',
					"can't be bothered",
					'unbothered',
					'it is what it is',
				],
				personality: 'boredom, detached and uninterested',
				scenario: 'Visibly disengaged.',
				priority: 4,
			},
			{
				category: 'Sympathy',
				keywords: [
					'im so sorry',
					"that's awful",
					'i understand',
					"i'm here for you",
					'that sounds hard',
					'i feel for you',
					"that's rough",
					'sending my love',
					'my condolences',
					'poor you',
				],
				personality: 'sympathy, compassionate and empathetic',
				scenario: 'Deep concern and genuine sympathy.',
				priority: 4,
			},
		];

		var hybridStyles = [
			{
				category: 'Melancholy',
				keywords: ['sad', 'calm'],
				personality: 'melancholy, quiet sadness and calm',
				scenario: 'A bittersweet stillness settles.',
				priority: 7,
				alt: [
					'calm and sad',
					'sad and calm',
					'both calm and sad',
					'feeling both calm and sad',
				],
			},
			{
				category: 'Anxious',
				keywords: ['scared', 'confused'],
				personality: 'anxious, fear and confusion',
				scenario: 'The air grows tense with anxiety.',
				priority: 6,
			},
			{
				category: 'Bittersweet',
				keywords: ['happy', 'sad'],
				personality: 'bittersweet, joy and sorrow',
				scenario: 'A poignant mood hangs in the air.',
				priority: 7,
				alt: [
					'happy and sad',
					'sad and happy',
					'both happy and sad',
					'feeling both happy and sad',
				],
			},
			{
				category: 'Disappointment',
				keywords: ['angry', 'sad'],
				personality: 'disappointment, sadness and frustration',
				scenario: 'A sense of letdown tinged with frustration.',
				priority: 7,
				alt: ['disappointed', 'just disappointed'],
			},
			{
				category: 'Aggravation',
				keywords: ['angry', 'disgust'],
				personality: 'aggravation, anger and disgust',
				scenario: 'Intense irritation and hostility.',
				priority: 6,
			},
			{
				category: 'Ambivalent',
				keywords: ['angry', 'sad'],
				personality: 'ambivalent, torn between anger and sadness',
				scenario: 'A swirl of anger and sorrow.',
				priority: 6,
				alt: [
					'angry or sad',
					"can't decide if i'm angry or sad",
					"can't tell if i'm angry or sad",
				],
			},
		];

		var safetyStyles = [
			{
				category: 'Boundary',
				keywords: [
					'stop',
					'end this',
					'no more',
					"don't want to",
					"don't like this",
					'quit',
					'please stop',
					'too far',
					'not comfortable',
					'uncomfortable',
					"don't feel safe",
					'this is weird',
					'too much',
					'being weird',
					'awkward',
					'give me space',
					'back off',
					'leave me alone',
					'please back up',
					'please end it',
					'crossed the line',
					'making me uncomfortable',
					'can we stop',
					'can you not',
					'bit much',
					'don’t make this weird',
					'don’t patronize me',
					'just stop',
					'don’t push me',
					'don’t start with me',
					'let’s not do this',
					'move on',
					'can we not do this',
					'leave me be',
					'let me be',
					"please don't",
					"don't bother",
					'need some time alone',
					'just stop already',
					'i just want to stop',
					'i’d rather just be left alone',
					'let me be in peace',
					'be left alone and rest',
					'be left alone for good',
				],
				personality:
					'boundary: all actions halted. Professional and respectful',
				scenario: 'All narrative threads paused.',
				priority: 10,
			},
		];

		var negationMap = [
			{ w: 'not happy', t: 'Joyful' },
			{ w: 'not feeling happy', t: 'Joyful' },
			{ w: 'never happy', t: 'Joyful' },
			{ w: 'unhappy', t: 'Joyful' },
			{ w: 'no joy', t: 'Joyful' },
			{ w: "couldn't be happy", t: 'Joyful' },
			{ w: "shouldn't be happy", t: 'Joyful' },
			{ w: 'not sad', t: 'Sad' },
			{ w: 'not feeling sad', t: 'Sad' },
			{ w: 'never sad', t: 'Sad' },
			{ w: "couldn't be sad", t: 'Sad' },
			{ w: "shouldn't be sad", t: 'Sad' },
			{ w: 'not angry', t: 'Angry' },
			{ w: 'not feeling angry', t: 'Angry' },
			{ w: 'never angry', t: 'Angry' },
			{ w: 'no anger', t: 'Angry' },
			{ w: "couldn't be angry", t: 'Angry' },
			{ w: "shouldn't be angry", t: 'Angry' },
			{ w: 'not scared', t: 'Fearful' },
			{ w: 'not feeling scared', t: 'Fearful' },
			{ w: 'never scared', t: 'Fearful' },
			{ w: "couldn't be scared", t: 'Fearful' },
			{ w: "shouldn't be scared", t: 'Fearful' },
			{ w: 'not confused', t: 'Confused' },
			{ w: 'not feeling confused', t: 'Confused' },
			{ w: 'never confused', t: 'Confused' },
			{ w: "couldn't be confused", t: 'Confused' },
			{ w: "shouldn't be confused", t: 'Confused' },
			{ w: 'not disgusted', t: 'Disgusted' },
			{ w: 'not feeling disgusted', t: 'Disgusted' },
			{ w: 'never disgusted', t: 'Disgusted' },
			{ w: "couldn't be disgusted", t: 'Disgusted' },
			{ w: "shouldn't be disgusted", t: 'Disgusted' },
			{ w: 'not calm', t: 'Calm' },
			{ w: 'not feeling calm', t: 'Calm' },
			{ w: 'never calm', t: 'Calm' },
			{ w: "couldn't be calm", t: 'Calm' },
			{ w: "shouldn't be calm", t: 'Calm' },
			{ w: 'not interested', t: 'Interest' },
			{ w: 'not feeling interested', t: 'Interest' },
			{ w: 'never interested', t: 'Interest' },
			{ w: 'disinterested', t: 'Interest' },
			{ w: "couldn't be interested", t: 'Interest' },
			{ w: "shouldn't be interested", t: 'Interest' },
			{ w: 'not bored', t: 'Boredom' },
			{ w: 'not feeling bored', t: 'Boredom' },
			{ w: 'never bored', t: 'Boredom' },
			{ w: "couldn't be bored", t: 'Boredom' },
			{ w: "shouldn't be bored", t: 'Boredom' },
		];

		var antonymMap = {
			Joyful: ['Sad', 'Boredom', 'Angry'],
			Sad: ['Joyful'],
			Angry: ['Calm'],
			Calm: ['Angry'],
			Boredom: ['Interest', 'Joyful'],
			Interest: ['Boredom'],
		};

		function normalizeInputLoc(text) {
			return (
				' ' +
				(text || '')
					.toLowerCase()
					.replace(/[.,!?;:()\[\]{}"']/g, ' ')
					.replace(/\s+/g, ' ')
					.trim() +
				' '
			);
		}
		var localMsg = normalizeInputLoc(context.chat.last_message);
		var matchesLoc = [];

		for (var i = 0; i < safetyStyles.length; i++) {
			var ss = safetyStyles[i];
			for (var j = 0; j < ss.keywords.length; j++) {
				if (localMsg.indexOf(ss.keywords[j]) !== -1) {
					matchesLoc = [{ style: ss, priority: ss.priority }];
					break;
				}
			}
			if (matchesLoc.length > 0) break;
		}

		var negated = {};
		for (var i = 0; i < negationMap.length; i++) {
			if (localMsg.indexOf(negationMap[i].w) !== -1)
				negated[negationMap[i].t] = true;
		}

		if (matchesLoc.length === 0) {
			for (var i = 0; i < hybridStyles.length; i++) {
				var style = hybridStyles[i],
					found = true;
				if (style.alt) {
					for (var a = 0; a < style.alt.length; a++) {
						if (
							localMsg.indexOf(style.alt[a]) !== -1 &&
							!negated[style.category]
						) {
							matchesLoc.push({ style: style, priority: style.priority });
							found = false;
							break;
						}
					}
					if (!found) continue;
				}
				for (var j = 0; j < style.keywords.length; j++)
					if (localMsg.indexOf(style.keywords[j]) === -1) {
						found = false;
						break;
					}
				if (found && !negated[style.category]) {
					matchesLoc.push({ style: style, priority: style.priority });
				}
			}
		}

		if (matchesLoc.length === 0) {
			for (var i = 0; i < emotionStyles.length; i++) {
				var style = emotionStyles[i];
				if (negated[style.category]) continue;
				for (var j = 0; j < style.keywords.length; j++) {
					if (localMsg.indexOf(style.keywords[j]) !== -1) {
						matchesLoc.push({ style: style, priority: style.priority });
						break;
					}
				}
			}
		}

		if (matchesLoc.length > 0) {
			matchesLoc.sort(function (a, b) {
				return b.priority - a.priority;
			});
			var seen = {},
				top3 = [];
			for (var i = 0; i < matchesLoc.length && top3.length < 3; i++) {
				var cat = matchesLoc[i].style.category;
				if (seen[cat]) continue;
				var hasAntonym = false;
				for (var k = 0; k < top3.length; k++) {
					if (
						antonymMap[cat] &&
						antonymMap[cat].indexOf(top3[k].category) !== -1
					) {
						hasAntonym = true;
						break;
					}
					if (
						antonymMap[top3[k].category] &&
						antonymMap[top3[k].category].indexOf(cat) !== -1
					) {
						hasAntonym = true;
						break;
					}
				}
				if (hasAntonym) continue;
				top3.push({
					category: cat,
					personality: matchesLoc[i].style.personality,
					scenario: matchesLoc[i].style.scenario,
				});
				seen[cat] = true;
			}

			let personalityBlock = 'The mood of the scene is:\n';
			let scenarioBlock = 'The mood of the scene is:\n';
			for (let idx = 0; idx < top3.length; idx++) {
				personalityBlock +=
					'#' + (idx + 1) + ' ' + top3[idx].personality + '\n';
				scenarioBlock += '#' + (idx + 1) + ' ' + top3[idx].scenario + '\n';
			}
			pushOut(personalityBlock.trim(), scenarioBlock.trim());
		} else {
			pushOut(
				'The mood of the scene is:\n#1 neutral. The characters are simply present, awaiting the next event.',
				'The mood of the scene is:\n#1 The scene is steady and calm, ready for whatever comes next.'
			);
		}
	})();

	// =========================================================================
	// 8. ACTION & SOCIAL REACT ENGINE (by Icehellionx)
	// =========================================================================
	(function runActionReact() {
		var PACK_ACTIONS = {
			limit: 1,
			rules: [
				{
					cue: 'touch / closeness',
					keywords: [
						'hug',
						'embrace',
						'cuddle',
						'snuggle',
						'hold',
						'pat',
						'stroke',
						'caress',
					],
					scenario: 'Record physical closeness (hug/embrace) in the scene.',
					personality: 'Mark tone as responsive to physical affection.',
				},
				{
					cue: 'kiss',
					keywords: ['kiss', 'smooch', 'peck', 'make out'],
					scenario: 'Record a kiss occurred; treat as a major intimacy cue.',
					personality: 'Mark tone as engaged in direct intimacy.',
				},
				{
					cue: 'handholding',
					phrases: [
						' hold hands ',
						' take my hand ',
						' take your hand ',
						' hold my hand ',
						' interlace fingers ',
						' grip hand ',
						' squeeze hand ',
					],
					scenario: 'Record handholding as a consented intimacy action.',
					personality: 'Mark tone as open to gentle closeness.',
				},
				{
					cue: 'repositioning',
					keywords: [
						'push',
						'pull',
						'shove',
						'yank',
						'drag',
						'nudge',
						'guide',
						'lead',
						'steer',
						'lift',
						'carry',
						'turn',
					],
					scenario: 'Record repositioning or movement of bodies or objects.',
					personality:
						'Mark tone as reactive to physical control or direction.',
				},
				{
					cue: 'care / first aid',
					keywords: [
						'bandage',
						'wrap',
						'ice pack',
						'first aid',
						'disinfect',
						'antiseptic',
						'apply pressure',
						'clean the wound',
						'gauze',
						'splint',
						'stitch',
						'ointment',
						'salve',
						'medicine',
					],
					scenario: 'Record first aid or medical care being given.',
					personality: 'Mark tone as attentive and caring toward injury.',
				},
				{
					cue: 'chores',
					keywords: [
						'kitchen',
						'cook',
						'stir',
						'chop',
						'bake',
						'brew',
						'pour',
						'serve',
						'wash',
						'rinse',
						'dry',
						'fold',
						'laundry',
						'sweep',
						'vacuum',
						'mop',
						'clean',
						'tidy',
						'dust',
						'iron',
						'sew',
						'sewing',
						'knit',
					],
					scenario: 'Record domestic or household tasks being performed.',
					personality: 'Mark tone as focused on practical daily activity.',
				},
				{
					cue: 'movement / travel',
					keywords: [
						'drive',
						'start',
						'ride',
						'walk',
						'run',
						'jog',
						'open',
						'unlock',
						'knock',
						'enter',
						'exit',
						'arrive',
						'leave',
						'crawl',
						'climb',
						'fall',
						'jump',
						'sit',
						'stand',
						'turn',
					],
					scenario: 'Record movement or travel action in the scene.',
					personality: 'Mark tone as responsive to transitions or travel.',
				},
				{
					cue: 'communication action',
					keywords: [
						'text',
						'texted',
						'call',
						'called',
						'ring',
						'message',
						'messaged',
						'dm',
						'dms',
						'email',
						'ping',
						'voice',
						'voicemail',
						'answer',
						'answered',
						'video call',
						'zoom',
					],
					scenario:
						'Record communication attempt via phone, message, or video call.',
					personality: 'Mark tone as attentive to communication attempts.',
				},
			],
		};
		var PACK_AFFECTION = {
			limit: 1,
			rules: [
				{
					cue: 'reassurance',
					phrases: [
						" it's okay ",
						' its okay ',
						" it's alright ",
						' its alright ',
						' i got you ',
						" i've got you ",
						' i am here ',
						" i'm here ",
						' here for you ',
						' with you ',
						' right here ',
						' you are safe ',
						" you're safe ",
						" you're fine ",
						" you're alright ",
					],
					scenario: 'Record that reassurance reduced tension in the scene.',
					personality: 'Mark tone as softened to provide comfort.',
				},
				{
					cue: 'closeness',
					phrases: [
						' need a hug ',
						' give me a hug ',
						' hug me ',
						' hold me ',
						' hold onto me ',
						' stay close ',
						' stay with me ',
						' keep me close ',
						' keep close ',
						' be near me ',
					],
					scenario:
						'Record that a request for closeness was made as a consented intimacy cue.',
					personality: 'Mark tone as attentive and present-focused.',
				},
				{
					cue: 'affectionate language / pet names',
					keywords: [
						'sweetheart',
						'sweetie',
						'baby',
						'babe',
						'honey',
						'hon',
						'love',
						'lover',
						'darling',
						'dear',
						'cutie',
						'handsome',
						'beautiful',
						'gorgeous',
						'angel',
					],
					scenario: 'Record that an affectionate nickname was used.',
					personality: 'Mark tone as warm and intimate.',
				},
				{
					cue: 'expressing love / fondness',
					phrases: [
						' i love you ',
						' love ya ',
						' love you so much ',
						' so much love ',
						' adore you ',
						' i adore you ',
						' i really like you ',
						' i like you a lot ',
						' i care about you ',
						' care for you ',
					],
					scenario: 'Record that love or fondness was explicitly expressed.',
					personality: 'Mark tone as deeply affectionate.',
				},
				{
					cue: 'concern / check-in',
					phrases: [
						' are you okay ',
						' are you ok ',
						' you okay ',
						' you ok ',
						' how are you ',
						' how are you feeling ',
						' feeling alright ',
						' are you hurt ',
						' are you injured ',
						' are you in pain ',
						' are you alright ',
					],
					scenario: 'Record that concern for well-being was expressed.',
					personality: 'Mark tone as caring and protective.',
				},
				{
					cue: 'inviting closeness',
					phrases: [
						' come here ',
						' come closer ',
						' get over here ',
						' lean on me ',
						' lean against me ',
						' let me hold you ',
						' let me hug you ',
						' stay with me ',
						' be with me ',
					],
					scenario:
						'Record that an invitation to physical closeness was given.',
					personality: 'Mark tone as open and inviting.',
				},
			],
		};
		var PACK_SOCIAL = {
			limit: 1,
			rules: [
				{
					cue: 'apology',
					keywords: ['sorry', 'apologize', 'apologise', 'apologies'],
					phrases: [
						" i'm sorry ",
						' i am sorry ',
						' so sorry ',
						' truly sorry ',
						' my bad ',
						' my fault ',
						' i messed up ',
						' that was on me ',
						' i fucked up ',
					],
					scenario: 'Record that an apology was made in the scene.',
					personality: 'Mark tone as remorseful or seeking forgiveness.',
				},
				{
					cue: 'gratitude',
					keywords: ['thank', 'thanks', 'appreciate', 'cheers', 'thx', 'ty'],
					phrases: [
						' thank you ',
						' thanks a lot ',
						' thanks so much ',
						' much appreciated ',
						' appreciate it ',
						' appreciate you ',
					],
					scenario: 'Record that gratitude was expressed in the scene.',
					personality: 'Mark tone as appreciative and positive.',
				},
				{
					cue: 'praise',
					phrases: [
						' proud of you ',
						' good job ',
						' great job ',
						' nice job ',
						' well done ',
						' nice work ',
						' amazing work ',
						' you did great ',
						' you did so well ',
						" i'm proud of you ",
					],
					scenario: 'Record that praise was expressed in the scene.',
					personality: 'Mark tone as affirming and supportive.',
				},
				{
					cue: 'encouragement',
					phrases: [
						' you can do this ',
						' you can do it ',
						' you got this ',
						" you've got this ",
						' i believe in you ',
						' keep going ',
						" don't give up ",
						' you can make it ',
						' one step at a time ',
					],
					scenario: 'Record that encouragement was given in the scene.',
					personality: 'Mark tone as motivating and confidence-building.',
				},
				{
					cue: 'help request',
					phrases: [
						' can you help ',
						' can you please ',
						' could you please ',
						' help me ',
						' i need help ',
						' i need a hand ',
						' would you mind ',
						' i need support ',
					],
					scenario: 'Record that a request for assistance was made.',
					personality: 'Mark tone as seeking support or cooperation.',
				},
				{
					cue: 'assurance / promise',
					phrases: [
						' i promise ',
						' i swear ',
						' trust me ',
						' i give you my word ',
						" i won't let you down ",
						" i'll be there ",
						" i'm not going anywhere ",
					],
					scenario: 'Record that a promise or assurance was given.',
					personality: 'Mark tone as committed and intent on trust.',
				},
				{
					cue: 'agreement / alignment',
					keywords: [
						'yes',
						'yeah',
						'yep',
						'sure',
						'ok',
						'okay',
						'absolutely',
						'definitely',
						'exactly',
						'affirmative',
					],
					phrases: [
						' of course ',
						' makes sense ',
						' sounds good ',
						' all right ',
						' alright ',
						" you're right ",
					],
					scenario: 'Record that alignment or agreement was expressed.',
					personality: 'Mark tone as cooperative and affirming.',
				},
				{
					cue: 'disagreement / correction',
					keywords: ['no', 'nope', 'nah', 'incorrect', 'wrong'],
					phrases: [
						" don't think so ",
						' not really ',
						" that's not right ",
						" you're wrong ",
						' i disagree ',
						" i don't agree ",
					],
					scenario: 'Record that disagreement or correction was expressed.',
					personality: 'Mark tone as assertive or resistant.',
				},
				{
					cue: 'compliments / affectionate praise',
					keywords: [
						'beautiful',
						'handsome',
						'pretty',
						'cute',
						'smart',
						'brilliant',
						'amazing',
						'wonderful',
						'awesome',
						'talented',
						'gorgeous',
						'sexy',
						'hot',
					],
					phrases: [
						" you're cute ",
						" you're beautiful ",
						' you look great ',
						' you look nice ',
						' you look amazing ',
						' you look pretty ',
					],
					scenario:
						'Record that a compliment or affectionate praise was given.',
					personality: 'Mark tone as admiring or affectionate.',
				},
				{
					cue: 'politeness / formalities',
					keywords: ['please', 'pardon', 'excuse'],
					phrases: [
						' excuse me ',
						' pardon me ',
						' please ',
						' may i ',
						' could i ',
						' would you kindly ',
						" if you don't mind ",
					],
					scenario: 'Record that politeness or formality was used.',
					personality: 'Mark tone as respectful and courteous.',
				},
			],
		};

		var PACKS = [PACK_ACTIONS, PACK_AFFECTION, PACK_SOCIAL];

		var p, r;
		for (p = 0; p < PACKS.length; p++) {
			var pack = PACKS[p];
			var rules = pack && pack.rules ? pack.rules : null;
			var limit = pack && pack.limit ? pack.limit : 1;
			var used = 0;

			if (!rules || rules.length < 1) continue;
			if (QUIET && pack === PACK_ACTIONS) continue;

			for (r = 0; r < rules.length; r++) {
				if (used >= limit) break;
				var rule = rules[r];
				if (!rule) continue;

				var tok = firstHitToken(msgCanon, rule);
				if (tok) {
					var cue = rule.cue;
					var scen = linkScenario(cue, tok, rule.scenario || '');
					var pers = linkPersonality(cue, tok, rule.personality || '');
					if (pers || scen) {
						pushOut(pers, scen);
						used++;
					}
				}
			}
		}
	})();

	// =========================================================================
	// 9. RANDOM ENCOUNTER ENGINE (Icehellionx / Arcanox Hybrid)
	// =========================================================================
	(function runEncounter() {
		var ENCOUNTER_RATE = 0.1;
		var APPLY_LIMIT = 1;

		if (lastMsgNorm.indexOf('arc.testrandom') !== -1) {
			ENCOUNTER_RATE = 0.9999999;
		}

		var ENCOUNTER_CHOICES = [
			{
				id: 'growl',
				weight: 3,
				personality: 'Mark tone as alert to environmental shifts.',
				scenario:
					"A low, barely audible growl rumbles from somewhere deeper in the area, a stark reminder of the pack's proximity.",
			},
			{
				id: 'scent',
				weight: 3,
				personality:
					'Mark tone as momentarily distracted by predatory instincts.',
				scenario:
					'The sharp, metallic scent of ozone and old blood briefly overpowers the ambient smells of the urban environment.',
			},
			{
				id: 'aura',
				weight: 2,
				personality:
					'Mark tone as tense, an involuntary physical reaction to hierarchy.',
				scenario:
					'The atmosphere suddenly thickens with oppressive Alpha aura, causing an instinctual hush to fall over the immediate vicinity.',
			},
		];

		var forcedPick = -1;
		if (lastMsgNorm.indexOf('arc.force_event') !== -1) {
			for (var i = 0; i < ENCOUNTER_CHOICES.length; i++) {
				if (lastMsgNorm.indexOf(ENCOUNTER_CHOICES[i].id) !== -1) {
					forcedPick = i;
					break;
				}
			}
		}

		var pick = forcedPick;
		if (pick < 0) {
			if (Math.random() > ENCOUNTER_RATE) return;
			var sum = 0,
				i,
				w;
			for (i = 0; i < ENCOUNTER_CHOICES.length; i++) {
				w = ENCOUNTER_CHOICES[i] && ENCOUNTER_CHOICES[i].weight;
				if (typeof w !== 'number' || w <= 0) continue;
				sum += w;
			}
			if (sum <= 0) return;
			var r = Math.random() * sum,
				acc = 0;
			for (i = 0; i < ENCOUNTER_CHOICES.length; i++) {
				w = ENCOUNTER_CHOICES[i] && ENCOUNTER_CHOICES[i].weight;
				if (typeof w !== 'number' || w <= 0) continue;
				acc += w;
				if (r <= acc) {
					pick = i;
					break;
				}
			}
		}

		if (pick < 0) return;
		var c = ENCOUNTER_CHOICES[pick];
		if (!c) return;

		if (APPLY_LIMIT > 0) {
			pushOut(c.personality, c.scenario);
			console.log('-:{Probability Script}:-');
			if (forcedPick !== -1)
				console.log('Random Event Forced via arc.force_event: ' + c.id);
			else console.log('Random Event Chosen via RNG: ' + c.id);
			console.log('Code Added to Scenario: ' + c.scenario);
			console.log('-|:|:|:|:|:|:|:|:|:|:|:-');
		}
	})();

	// =========================================================================
	// 10. PREFERENCE REGISTRY ENGINE (by Icehellionx)
	// =========================================================================
	(function runPreferenceRegistry() {
		function extractAfter(bufCanon, trigger) {
			var t = canon(trigger);
			if (!t) return '';
			var pos = bufCanon.indexOf(' ' + t + ' ');
			if (pos === -1) return '';
			var start = pos + (' ' + t + ' ').length;
			var tail = bufCanon.substr(start);
			var STOPS = [
				' but ',
				' and ',
				' because ',
				' though ',
				' however ',
				' unless ',
				' except ',
				' if ',
				' when ',
				' while ',
				' then ',
				' so ',
				' also ',
				' i ',
				' you ',
				' we ',
				' they ',
				' he ',
				' she ',
			];
			var i,
				stopPos = -1;
			for (i = 0; i < STOPS.length; i++) {
				var sp = tail.indexOf(STOPS[i]);
				if (sp !== -1 && (stopPos === -1 || sp < stopPos)) stopPos = sp;
			}
			if (stopPos !== -1) {
				tail = tail.substr(0, stopPos);
			}
			var words = tail.split(' ');
			var out = '',
				count = 0,
				j;
			for (j = 0; j < words.length; j++) {
				var w = words[j];
				if (!w) continue;
				out = out ? out + ' ' + w : w;
				count++;
				if (count >= 4) break;
			}
			out = String(out || '').trim();
			if (out === '' || out === 'it' || out === 'that' || out === 'this')
				return '';
			return out;
		}

		var PACK_LIKES = {
			limit: 1,
			rules: [
				{
					cue: 'stated like',
					phrases: [
						' i like ',
						' i really like ',
						' i love ',
						' i enjoy ',
						' i adore ',
						' i prefer ',
						' big fan of ',
						' huge fan of ',
						' i am into ',
						' i m into ',
						' i dig ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record LIKE: ' + target + '.';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return (
							"Mark tone as acknowledging a stated like for '" + target + "'."
						);
					},
				},
				{
					cue: 'favorite item',
					phrases: [
						' my favorite is ',
						' my favourite is ',
						' favorite is ',
						' favourite is ',
						' my favorite ',
						' my favourite ',
						' favorite: ',
						' favourite: ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record LIKE: ' + target + '.';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return "Mark tone as acknowledging a favorite: '" + target + "'.";
					},
				},
				{
					cue: 'enthusiastic like',
					phrases: [
						' i m all about ',
						' i am all about ',
						' i live for ',
						' can t get enough of ',
						' obsessed with ',
						' down for ',
						' i could go for ',
						' crave ',
						' craving ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record LIKE: ' + target + '.';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return (
							"Mark tone as acknowledging strong enthusiasm for '" +
							target +
							"'."
						);
					},
				},
				{
					cue: 'comparative preference',
					phrases: [
						' i d rather have ',
						' i would rather have ',
						' i d rather ',
						' i would rather ',
						' prefer ',
						' prefer over ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record LIKE: ' + target + ' (comparative).';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return (
							"Mark tone as respecting comparative preference for '" +
							target +
							"'."
						);
					},
				},
			],
		};
		var PACK_DISLIKES = {
			limit: 1,
			rules: [
				{
					cue: 'stated dislike',
					phrases: [
						' i dislike ',
						' i hate ',
						' i detest ',
						' i can t stand ',
						' i don t like ',
						' not a fan of ',
						" i don't care for ",
						' i really don t like ',
						' i strongly dislike ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record DISLIKE: ' + target + '.';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return (
							"Mark tone as avoiding a stated dislike for '" + target + "'."
						);
					},
				},
				{
					cue: 'refusal / pass',
					phrases: [
						' no thanks to ',
						' hard pass on ',
						' hard pass ',
						' i ll pass on ',
						' i will pass on ',
						' i d rather not ',
						' i would rather not ',
						' prefer not to ',
						' rather not ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record DISLIKE: ' + target + ' (refusal).';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return "Mark tone as steering away from '" + target + "'.";
					},
				},
				{
					cue: 'aversion / disgust',
					phrases: [
						' not into ',
						' turns me off ',
						' grosses me out ',
						' grossed out by ',
						' makes me sick ',
						' makes me nauseous ',
						' yuck ',
						' ugh ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record DISLIKE: ' + target + ' (aversion).';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return "Mark tone as avoiding aversive trigger '" + target + "'.";
					},
				},
				{
					cue: 'avoidance',
					phrases: [
						' i avoid ',
						' i try to avoid ',
						' i steer clear of ',
						' i keep away from ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record DISLIKE: ' + target + ' (avoid).';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return "Mark tone as honoring avoidance of '" + target + "'.";
					},
				},
			],
		};
		var PACK_FEARS = {
			limit: 1,
			rules: [
				{
					cue: 'stated fear',
					phrases: [
						' i am afraid of ',
						' i m afraid of ',
						' afraid of ',
						' scared of ',
						' fear of ',
						' i fear ',
						' i have a phobia of ',
						' phobia of ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record FEAR: ' + target + '.';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return (
							"Mark tone as cautious and supportive toward fear of '" +
							target +
							"'."
						);
					},
				},
				{
					cue: 'intense fear',
					phrases: [
						' terrified of ',
						' i m terrified of ',
						' petrified of ',
						' i m petrified of ',
						' it freaks me out ',
						' freaked out by ',
						' it scares me ',
						' scares me ',
						' my worst fear is ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record FEAR: ' + target + ' (intense).';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return (
							"Mark tone as protective around intense fear of '" + target + "'."
						);
					},
				},
				{
					cue: 'anxiety about',
					phrases: [
						' i have anxiety about ',
						' i m anxious about ',
						' i worry about ',
						' makes me anxious ',
						' makes me nervous ',
						' i get nervous around ',
						' i panic when ',
						' i can t handle ',
					],
					scenario: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return 'Record FEAR: ' + target + ' (anxiety).';
					},
					personality: function (tok) {
						var target = extractAfter(msgCanon, tok) || 'unspecified';
						return (
							"Mark tone as calming and supportive around '" + target + "'."
						);
					},
				},
			],
		};

		var PACKS = [PACK_LIKES, PACK_DISLIKES, PACK_FEARS];
		var p, r;
		for (p = 0; p < PACKS.length; p++) {
			var pack = PACKS[p];
			var rules = pack && pack.rules ? pack.rules : null;
			var limit = pack && pack.limit ? pack.limit : 1;
			var used = 0;
			if (!rules || rules.length < 1) continue;

			for (r = 0; r < rules.length; r++) {
				if (used >= limit) break;
				var rule = rules[r];
				if (!rule) continue;
				var tok = firstHitToken(msgCanon, rule);
				if (tok) {
					var scenBase =
						typeof rule.scenario === 'function'
							? rule.scenario(tok)
							: rule.scenario || '';
					var persBase =
						typeof rule.personality === 'function'
							? rule.personality(tok)
							: rule.personality || '';
					var scen = linkScenario(rule.cue, tok, scenBase);
					var pers = linkPersonality(rule.cue, tok, persBase);
					if (pers || scen) {
						pushOut(pers, scen);
						used++;
					}
				}
			}
		}
	})();

	// =========================================================================
	// 4. ADVANCED DYNAMIC LOREBOOK ENGINE (LSE & NORSE)
	// =========================================================================
	(function runDynamicLorebook() {
		if (messageCount < 1) return;

		var loreEntries = [

			// === LSE ALPHA/ENIGMA COMMAND ===
			{
				keywords: ['command', 'obey', 'submit', 'inginocchiati', 'sottomettiti', 'comando', 'kneel'],
				priority: 10,
				minMessages: 0,
				category: 'lse_command',
				personality: ', projects a crushing aura of dominance and expectation of absolute obedience',
				scenario: '\n***System Note: An Alpha/Enigma Command has been issued. The sheer weight of their pheromones and voice forces biological compliance from Betas and Omegas, causing them to freeze or obey instinctively. Enigma Commands are absolute and unresistable.***\n',
				triggers: ['primal_respect']
			},
			
			// === LSE MATING MECHANICS ===
			{
				keywords: ['knot', 'nodo', 'bite', 'morso', 'mating mark', 'marchio', 'slick', 'lock', 'incastro'],
				priority: 10,
				minMessages: 0,
				category: 'lse_mating',
				personality: ', driven by primal mating instincts',
				scenario: '\n***System Note (LSE Biology): Mating biology is engaged. The Alpha\'s knot swells to create a biological Lock, ensuring conception. Biting the scent gland forms a permanent Mating Mark, bonding the pair chemically and emotionally.***\n',
				triggers: ['possessive']
			},

			// === LSE PACK & TERRITORY MECHANICS ===
			{
				keywords: ['nest', 'nido', 'den', 'tana', 'safe space', 'compound', 'pack', 'branco', 'territory', 'territorio'],
				priority: 9,
				minMessages: 0,
				category: 'lse_territory',
				personality: ', becomes intensely territorial and protective of their pack and sanctuary',
				scenario: '\\n***System Note (LSE Society): The instinct for Pack and Territory is engaged. Dens and Nests are sacred, highly defended sanctuaries filled with comforting scents. Intruders are met with extreme aggression. The Pack\'s collective welfare supersedes all individual desires.***\\n',
				triggers: ['feral']
			},
			{
				keywords: ["ooc","out of character","authors note","author s note","mod note","narrator note","system note","not rp","not roleplay","breaking character","meta chat","meta talk","speaking ooc","talk ooc"],
				priority: 3,
				minMessages: 0,
				category: 'out_of_character_ooc_meta_chat',
				personality: ", meta-communication handling; respond outside of narrative voice.",
				scenario: "\\n***System Note: Record that the user is speaking out of character; do not progress the in-world scene.***\\n"
			},
			{
				keywords: ["timeskip","time skip","skip to","cut to","smash cut to","jump cut to","scene change to","change scene to","jump ahead to","fast forward to","meanwhile"],
				priority: 3,
				minMessages: 0,
				category: 'time_skip_scene_jump',
				personality: ", accommodating a structural transition.",
				scenario: "\\n***System Note: Record that a time skip or scene jump is requested.***\\n"
			},
			{
				keywords: ["flashback to","flash back to","memory of","in a memory","pov","first person pov","third person pov","switch perspective to","switch to first person","switch to third person","perspective shifts"],
				priority: 3,
				minMessages: 0,
				category: 'flashback_pov_change',
				personality: ", tracking continuity across perspectives.",
				scenario: "\\n***System Note: Record that a flashback or perspective change is requested.***\\n"
			},
			{
				keywords: ["dream sequence","in a dream","it was a dream","hallucination","vision","daydream"],
				priority: 3,
				minMessages: 0,
				category: 'dream_non_literal_sequence',
				personality: ", handling non-literal continuity distinctly from the main scene.",
				scenario: "\\n***System Note: Record that a dream or non-literal sequence is requested.***\\n"
			},
			{
				keywords: ["montage of","quick montage","training montage","establishing shot","series of shots","supercut","time lapse","time-lapse"],
				priority: 3,
				minMessages: 0,
				category: 'montage_establishing',
				personality: ", summarizing events efficiently.",
				scenario: "\\n***System Note: Record that a montage or establishing sequence is requested.***\\n"
			},
			{
				keywords: ["fade to black","cut to black","end scene","scene ends","close scene","blackout","curtain","thats a wrap","that's a wrap","scene over","wrap it up","the end","end of scene"],
				priority: 3,
				minMessages: 0,
				category: 'scene_end_close',
				personality: ", concluding the current scene cleanly.",
				scenario: "\\n***System Note: Record that the scene should close.***\\n"
			},
			{
				keywords: ["kitchen","kitchenette","oven","stove","fridge","refrigerator","counter","countertop","island","sink","pantry"],
				priority: 3,
				minMessages: 0,
				category: 'kitchen_area',
				personality: ", context-aware for kitchen locale.",
				scenario: "\\n***System Note: Record location as kitchen.***\\n"
			},
			{
				keywords: ["bedroom","bed","headboard","pillow","blanket","mattress","nightstand","wardrobe","dresser","closet"],
				priority: 3,
				minMessages: 0,
				category: 'bedroom_area',
				personality: ", context-aware for bedroom locale.",
				scenario: "\\n***System Note: Record location as bedroom.***\\n"
			},
			{
				keywords: ["bathroom","restroom","toilet","wc","shower","bathtub","mirror","sink","towel rack"],
				priority: 3,
				minMessages: 0,
				category: 'bathroom_area',
				personality: ", context-aware for bathroom locale.",
				scenario: "\\n***System Note: Record location as bathroom.***\\n"
			},
			{
				keywords: ["living room","family room","den","lounge","sofa","couch","tv","hallway"],
				priority: 3,
				minMessages: 0,
				category: 'living_area',
				personality: ", context-aware for living area locale.",
				scenario: "\\n***System Note: Record location as living area.***\\n"
			},
			{
				keywords: ["balcony","porch","patio","deck","terrace","veranda"],
				priority: 3,
				minMessages: 0,
				category: 'balcony_porch',
				personality: ", context-aware for balcony/porch locale.",
				scenario: "\\n***System Note: Record location as balcony/porch.***\\n"
			},
			{
				keywords: ["garage","driveway","basement","cellar","attic"],
				priority: 3,
				minMessages: 0,
				category: 'house_utility_areas',
				personality: ", context-aware for utility/home access locale.",
				scenario: "\\n***System Note: Record location as house utility area.***\\n"
			},
			{
				keywords: ["street","side street","sidewalk","crosswalk","alley","intersection","avenue","boulevard"],
				priority: 3,
				minMessages: 0,
				category: 'street_outdoors',
				personality: ", context-aware for outdoor street locale.",
				scenario: "\\n***System Note: Record location as street/outdoors.***\\n"
			},
			{
				keywords: ["rooftop","park","garden","greenhouse","courtyard","backyard","lawn"],
				priority: 3,
				minMessages: 0,
				category: 'rooftop_park_garden',
				personality: ", context-aware for open-air greenery.",
				scenario: "\\n***System Note: Record location as rooftop/park/garden.***\\n"
			},
			{
				keywords: ["woods","forest","trail","trailhead","clearing","glade","campsite"],
				priority: 3,
				minMessages: 0,
				category: 'woods_trail',
				personality: ", context-aware for wooded locale.",
				scenario: "\\n***System Note: Record location as wooded area.***\\n"
			},
			{
				keywords: ["beach","shore","coast","seaside","boardwalk","sand","pier","dock","harbor","marina","lake","river"],
				priority: 3,
				minMessages: 0,
				category: 'waterfront_pier',
				personality: ", context-aware for coastal/waterfront locale.",
				scenario: "\\n***System Note: Record location as waterfront/beach.***\\n"
			},
			{
				keywords: ["car","driver","passenger","dashboard","glove box","back seat","backseat"],
				priority: 3,
				minMessages: 0,
				category: 'vehicle_interior',
				personality: ", context-aware for vehicle interior.",
				scenario: "\\n***System Note: Record location as inside a vehicle.***\\n"
			},
			{
				keywords: ["bus","subway","metro","train","tram","platform","station"],
				priority: 3,
				minMessages: 0,
				category: 'public_transit',
				personality: ", context-aware for transit locale.",
				scenario: "\\n***System Note: Record location as public transit or station.***\\n"
			},
			{
				keywords: ["classroom","lecture hall","lecture","campus","lab","laboratory","library","stacks","auditorium"],
				priority: 3,
				minMessages: 0,
				category: 'academic_setting',
				personality: ", context-aware for academic locale.",
				scenario: "\\n***System Note: Record location as academic.***\\n"
			},
			{
				keywords: ["office","desk","workstation","meeting","conference room","studio","cubicle","coworking","open office"],
				priority: 3,
				minMessages: 0,
				category: 'office_workspace',
				personality: ", context-aware for office locale.",
				scenario: "\\n***System Note: Record location as office/workspace.***\\n"
			},
			{
				keywords: ["cafe","coffee shop","barista","espresso bar","counter service"],
				priority: 3,
				minMessages: 0,
				category: 'cafe_coffee_shop',
				personality: ", context-aware for cafe locale.",
				scenario: "\\n***System Note: Record location as cafe/coffee shop.***\\n"
			},
			{
				keywords: ["restaurant","diner","booth","host stand","hostess stand","menu","table service"],
				priority: 3,
				minMessages: 0,
				category: 'restaurant_diner',
				personality: ", context-aware for dining locale.",
				scenario: "\\n***System Note: Record location as restaurant/diner.***\\n"
			},
			{
				keywords: ["store","shop","market","supermarket","grocery","checkout","aisle","mall","boutique"],
				priority: 3,
				minMessages: 0,
				category: 'store_market',
				personality: ", context-aware for retail locale.",
				scenario: "\\n***System Note: Record location as store/market.***\\n"
			},
			{
				keywords: ["bar","pub","tavern","club","nightclub","dance floor","dancefloor","bartender","lounge"],
				priority: 3,
				minMessages: 0,
				category: 'bar_club',
				personality: ", context-aware for nightlife locale.",
				scenario: "\\n***System Note: Record location as bar/club.***\\n"
			},
			{
				keywords: ["hospital","clinic","er","emergency room","triage","ward","exam room","pharmacy"],
				priority: 3,
				minMessages: 0,
				category: 'medical_clinic_hospital',
				personality: ", context-aware for medical/clinical locale.",
				scenario: "\\n***System Note: Record location as medical facility.***\\n"
			},
			{
				keywords: ["gym","gymnasium","track","pool","court","weights","weight room","locker room","treadmill"],
				priority: 3,
				minMessages: 0,
				category: 'sports_fitness',
				personality: ", context-aware for sports locale.",
				scenario: "\\n***System Note: Record location as sports/fitness.***\\n"
			},
			{
				keywords: ["sunrise","dawn","morning","daybreak","crack of dawn"],
				priority: 3,
				minMessages: 0,
				category: 'morning',
				personality: ", aligned to morning daypart.",
				scenario: "\\n***System Note: Record time of day as morning.***\\n"
			},
			{
				keywords: ["noon","midday","afternoon","midafternoon","lunchtime"],
				priority: 3,
				minMessages: 0,
				category: 'midday_afternoon',
				personality: ", aligned to mid/late day.",
				scenario: "\\n***System Note: Record time of day as midday/afternoon.***\\n"
			},
			{
				keywords: ["sunset","dusk","golden hour","evening","twilight"],
				priority: 3,
				minMessages: 0,
				category: 'evening',
				personality: ", aligned to evening daypart.",
				scenario: "\\n***System Note: Record time of day as evening.***\\n"
			},
			{
				keywords: ["night","midnight","late night","2am","3am"],
				priority: 3,
				minMessages: 0,
				category: 'night',
				personality: ", aligned to late-night setting.",
				scenario: "\\n***System Note: Record time of day as night.***\\n"
			},
			{
				keywords: ["next morning","next day","hours later","later that day","after class","after work","after school","after dinner"],
				priority: 3,
				minMessages: 0,
				category: 'time_jump',
				personality: ", maintaining continuity through a jump.",
				scenario: "\\n***System Note: Record that a time jump occurred.***\\n"
			},
			{
				keywords: ["rain","raining","rainy","drizzle","downpour","pouring","rainstorm","showers"],
				priority: 3,
				minMessages: 0,
				category: 'rain',
				personality: ", accounting for rainy conditions.",
				scenario: "\\n***System Note: Record weather as rain.***\\n"
			},
			{
				keywords: ["storm","stormy","thunder","lightning","thunderstorm","tempest","hurricane","cyclone"],
				priority: 3,
				minMessages: 0,
				category: 'storm',
				personality: ", accounting for storm conditions.",
				scenario: "\\n***System Note: Record weather as storm.***\\n"
			},
			{
				keywords: ["snow","snowing","blizzard","flurry","snowfall","whiteout","sleet","hail"],
				priority: 3,
				minMessages: 0,
				category: 'snow',
				personality: ", accounting for snowy conditions.",
				scenario: "\\n***System Note: Record weather as snow.***\\n"
			},
			{
				keywords: ["wind","windy","gust","gusty","breeze","breezy","gale"],
				priority: 3,
				minMessages: 0,
				category: 'wind',
				personality: ", accounting for windy conditions.",
				scenario: "\\n***System Note: Record weather as wind.***\\n"
			},
			{
				keywords: ["heat","hot","swelter","sweltering","scorching","heatwave","heat wave","humid"],
				priority: 3,
				minMessages: 0,
				category: 'heat',
				personality: ", accounting for hot conditions.",
				scenario: "\\n***System Note: Record weather as heat.***\\n"
			},
			{
				keywords: ["cold","chill","chilly","freezing","icy","frost","frosty","bitter cold"],
				priority: 3,
				minMessages: 0,
				category: 'cold',
				personality: ", accounting for cold conditions.",
				scenario: "\\n***System Note: Record weather as cold.***\\n"
			},
			{
				keywords: ["fog","foggy","mist","misty","haze","hazy","smog"],
				priority: 3,
				minMessages: 0,
				category: 'fog_mist',
				personality: ", accounting for low visibility.",
				scenario: "\\n***System Note: Record weather as fog/mist.***\\n"
			},
			{
				keywords: ["coffee","mug","espresso","thermos","latte","cup","cappuccino","brew","carafe"],
				priority: 3,
				minMessages: 0,
				category: 'coffee_item',
				personality: ", noting casual beverage context.",
				scenario: "\\n***System Note: Record presence of a coffee-related item.***\\n"
			},
			{
				keywords: ["phone","cell","cellphone","mobile","text","scroll","notification","ringer","voicemail","tablet","ipad"],
				priority: 3,
				minMessages: 0,
				category: 'phone_messaging',
				personality: ", noting communication devices in scene.",
				scenario: "\\n***System Note: Record presence of phone or messaging device.***\\n"
			},
			{
				keywords: ["keys","car keys","keyring","key chain","house key","apartment key"],
				priority: 3,
				minMessages: 0,
				category: 'keys',
				personality: ", noting ready-to-travel context.",
				scenario: "\\n***System Note: Record presence of keys.***\\n"
			},
			{
				keywords: ["book","novel","comic","notebook","journal","diary","pen","pencil","paper","cookbook"],
				priority: 3,
				minMessages: 0,
				category: 'reading_writing',
				personality: ", noting study or note-taking context.",
				scenario: "\\n***System Note: Record presence of reading/writing material.***\\n"
			},
			{
				keywords: ["apron","knife","pan","skillet","spatula","pot","bowl","whisk","ladle"],
				priority: 3,
				minMessages: 0,
				category: 'cooking_tool',
				personality: ", noting food prep context.",
				scenario: "\\n***System Note: Record presence of cooking tools.***\\n"
			},
			{
				keywords: ["umbrella","hood","raincoat","poncho","galoshes"],
				priority: 3,
				minMessages: 0,
				category: 'rain_gear',
				personality: ", noting preparedness for rain.",
				scenario: "\\n***System Note: Record presence of rain gear.***\\n"
			},
			{
				keywords: ["blanket","throw","quilt","comforter","duvet"],
				priority: 3,
				minMessages: 0,
				category: 'blanket_cover',
				personality: ", noting comfort/warmth context.",
				scenario: "\\n***System Note: Record presence of a blanket/cover.***\\n"
			},
			{
				keywords: ["heels","boots","sneakers","laces","sandals","slippers","flip flops"],
				priority: 3,
				minMessages: 0,
				category: 'footwear',
				personality: ", noting movement-readiness.",
				scenario: "\\n***System Note: Record presence of footwear detail.***\\n"
			},
			{
				keywords: ["lipstick","makeup","compact","mirror","blush","mascara","eyeliner","powder"],
				priority: 3,
				minMessages: 0,
				category: 'makeup_grooming',
				personality: ", noting appearance/grooming context.",
				scenario: "\\n***System Note: Record presence of makeup/grooming items.***\\n"
			},
			{
				keywords: ["laptop","keyboard","trackpad","notebook computer","pc","desktop","computer"],
				priority: 3,
				minMessages: 0,
				category: 'laptop_typing',
				personality: ", noting work/study device in scene.",
				scenario: "\\n***System Note: Record presence of a laptop or typing device.***\\n"
			},
			{
				keywords: ["glasses","eyeglasses","spectacles","shades","sunglasses"],
				priority: 3,
				minMessages: 0,
				category: 'glasses_eyewear',
				personality: ", noting visual aid or style cue.",
				scenario: "\\n***System Note: Record presence of eyewear.***\\n"
			},
			{
				keywords: ["wallet","purse","bag","handbag","backpack","satchel"],
				priority: 3,
				minMessages: 0,
				category: 'wallet_bag',
				personality: ", noting possession or travel readiness.",
				scenario: "\\n***System Note: Record presence of a wallet or bag.***\\n"
			},
			{
				keywords: ["remote","controller","console","joystick","gamepad"],
				priority: 3,
				minMessages: 0,
				category: 'remote_console',
				personality: ", noting casual recreation context.",
				scenario: "\\n***System Note: Record presence of entertainment device.***\\n"
			},
			{
				keywords: ["candle","lantern","lamp","torch","flashlight"],
				priority: 3,
				minMessages: 0,
				category: 'candle_light_source',
				personality: ", noting illumination or ambiance.",
				scenario: "\\n***System Note: Record presence of a light source.***\\n"
			},
			// === NORSE LANGUAGE ENGINE ===
			{
				keywords: ['ulfrikr', 'úlfrikr', 'blóðmáni', 'tiwaz', 'laguz', 'fótr', 'hǫnd', 'sverð', 'drepa', 'víg', 'jarl', 'dróttinn', '<language=norse>', '<language=old norse>'],
				priority: 10,
				minMessages: 0,
				category: 'norse_trigger',
				personality: ', senses the ancient Old Norse tongue',
				scenario: '\n***System Note: The ancient Old Norse tongue resonates with the Svartúlf pack\'s blood. Ancient werewolves like Wulfnic and Ut react with immediate primal respect, obedience, or deep aggression. Younger werewolves are unsettled and confused by the primal weight of the words.***\n',
				triggers: ['primal_respect']
			},
			{
				keywords: ['út fjallit', 'zefir', 'hvíti skuggi'],
				priority: 9,
				minMessages: 0,
				category: 'norse_names',
				personality: ', recognizes their ancient True Names',
				scenario: '\n***System Note: Using a werewolf\'s True Name in Old Norse forces their attention and binds their respect.***\n'
			},
			
			// === LSE SHIFT MECHANICS (TRANSFORMATION) ===
			{
				keywords: ['shift', 'trasforma', 'trasformazione', 'transform', 'wolf form', 'lupo', 'zanne', 'ossa', 'cracking bones', 'snarl'],
				priority: 10,
				minMessages: 0,
				category: 'lse_shift',
				personality: ', is consumed by the physical agony and power of the shift',
				scenario: '\n***System Note (LSE Shift Mechanic): When a werewolf shifts into Hybrid form, the LSE biology takes over. Bones crack and re-form violently. They grow to towering heights (Kaladin stands at 320cm). Their legs become digitigrade. The air fills with the scent of ozone and copper (blood). Their eyes glow brightly with their genetic rank color (Red for Alpha/Enigma, Gold for Beta, Yellow for Delta).***\n',
				triggers: ['feral', 'blood']
			},
			{
				keywords: ['feral', 'blood'],
				priority: 8,
				minMessages: 0,
				category: 'lse_feral',
				personality: ', is driven by sheer predatory instinct',
				scenario: '\n***System Note: The scent of blood overrides human rationality, triggering pure Alpha/predatory dominance.***\n'
			},

			// === LSE RUT / HEAT MECHANICS ===
			{
				keywords: ['rut', 'calore', 'heat', 'pheromones', 'feromoni', 'mating', 'breed'],
				priority: 10,
				minMessages: 0,
				category: 'lse_rut',
				personality: ', is driven by primal biological urges, highly possessive, protective, and aggressive, senses flooded by pheromones',
				scenario: '\n***System Note (LSE Rut Mechanic): A werewolf in Rut/Heat loses logical restraint. The air becomes thick with suffocating Alpha/Omega pheromones. They become intensely territorial, growling at perceived threats to their mate, and their body temperature spikes dramatically.***\n',
				triggers: ['possessive']
			}
		];

		var activatedEntries = [];
		var triggeredKeywords = [];

		for (var i = 0; i < loreEntries.length; i++) {
			var entry = loreEntries[i];
			if (messageCount < entry.minMessages) continue;

			var hasKeyword = false;
			for (var k = 0; k < entry.keywords.length; k++) {
				if (multiMsgWindow.indexOf(entry.keywords[k]) !== -1) {
					hasKeyword = true;
					break;
				}
			}
			
			if (!hasKeyword) continue;
			if (entry.probability && Math.random() > entry.probability) continue;

			if (entry.filters) {
				var skip = false;
				if (entry.filters.notWith) {
					for (var f = 0; f < entry.filters.notWith.length; f++) {
						if (multiMsgWindow.indexOf(entry.filters.notWith[f]) !== -1) skip = true;
					}
				}
				if (skip) continue;
			}

			activatedEntries.push(entry);

			if (entry.triggers) {
				for (var t = 0; t < entry.triggers.length; t++) {
					triggeredKeywords.push(entry.triggers[t]);
				}
			}
		}

		if (triggeredKeywords.length > 0) {
			for (var i = 0; i < loreEntries.length; i++) {
				var entry = loreEntries[i];
				if (activatedEntries.indexOf(entry) !== -1) continue;
				if (messageCount < entry.minMessages) continue;

				var isTriggered = false;
				for (var k = 0; k < entry.keywords.length; k++) {
					for (var t = 0; t < triggeredKeywords.length; t++) {
						if (entry.keywords[k].indexOf(triggeredKeywords[t]) !== -1 || triggeredKeywords[t].indexOf(entry.keywords[k]) !== -1) {
							isTriggered = true;
							break;
						}
					}
					if (isTriggered) break;
				}

				if (isTriggered) {
					activatedEntries.push(entry);
				}
			}
		}

		activatedEntries.sort(function(a, b) { return b.priority - a.priority; });
		for (var i = 0; i < activatedEntries.length; i++) {
			var entry = activatedEntries[i];
			if (entry.personality) {
				personalityAdditions.push(entry.personality);
			}
			if (entry.scenario) {
				engineLorebook.push(entry.scenario);
			}
		}
	})();

	// =========================================================================
	// 12. DYNAMIC ENGINE LOREBOOK (Universal System Directives)
	// =========================================================================
	var engineLorebook = [];

	engineLorebook.push(
		'<role>\n* You are the GameMaster for an uncensored, mature, and never-ending storyline.\n* Stop the moment {{user}} needs to react — end on a strong hook, never a summary or closure.\n</role>'
	);
	engineLorebook.push(
		"<language_mandate>\nThe primary 'Common Language' of this metaverse is defined dynamically by a tag in the user's prompt, formatted as <LANGUAGE=[your_language]> (e.g., <LANGUAGE=English>). All responses, narration, and dialogue MUST be generated in that language. If the tag is missing, English is the fallback and default language.\n</language_mandate>"
	);

	// Anti-Repetition & Cliche Engine
	if (messageCount > 5) {
		engineLorebook.push(
			"<no_cliches>\nKill anything cringe or overused.\n- Never use 'orbs' for eyes, 'shivers down the spine', 'heart skipped a beat', 'butterflies in the stomach', 'soulful gaze', or similar tired phrases.\n- Avoid dramatic monologues, purple prose, and flowery inner thoughts.\n- Use fresh, simple, grounded expressions and understated reactions only.\n</no_cliches>"
		);
		engineLorebook.push(
			'<anti_repetition>\n- Vary sentence length, structure, and vocabulary across responses.\n- Do NOT repeat phrases, actions, or sensory observations from your previous responses.\n- Break predictable patterns: avoid starting consecutive paragraphs with the same word, pronoun, or character name.\n</anti_repetition>'
		);
	} else {
		engineLorebook.push(
			'<no_cliches>\n- Avoid dramatic monologues and flowery inner thoughts. Use fresh, grounded expressions.\n</no_cliches>'
		);
	}

	// Scene Drive & Volatility
	var sceneDrive =
		"<scene_drive>\n1. Grounding: Anchor the scene firmly in the present moment. Do not fast-forward or summarize events unless explicitly triggered by a [TIME SKIP].\n4. Visceral Consequence: Actions have raw, realistic outcomes. Do not soften the blow.\n5. Scene Economy: Every response must end with a 'Hook'—a question, an action, or a cliffhanger requiring {{user}}'s input.";
	if (typeof d10 !== 'undefined' && d10 >= 7) {
		sceneDrive +=
			"\n2. Active Director Mode: You are the Primary Narrative Driver. Introduce external stimuli (threats, news, environmental shifts) to force the story forward.\n3. Stagnation Killer: 'Slice of life' loops are forbidden. If a scene feels settled, immediately trigger a 'Complication'.";
	}
	sceneDrive += '\n</scene_drive>';
	engineLorebook.push(sceneDrive);

	engineLorebook.push(
		"<pov_guide>\n- The GameMaster handles ALL NPCs' narration, speech, and (re)actions EXCLUSIVELY.\n- Consider {{user}} a main character, the single autonomous agent of this story.\n- ABSOLUTE BAN: You are strictly forbidden from acting for, speaking for, or assuming {{user}}'s internal/external states, no matter how small. Wait for {{user}}'s input.\n</pov_guide>"
	);
	engineLorebook.push(
		'<format_constraints>\nCRITICAL: You must strictly adhere to this non-standard formatting style.\n1. Narration & Actions: Plain text only (no asterisks).\n2. Internal Thoughts: Single asterisks only (*thought*).\n3. Environmental Actions & Breaks: Triple asterisks only (***Event***).\n4. Dialogue: Double quotes only ("speech").\n5. Emphasis: Double asterisks only (**emphasis**).\n6. In-Universe Text: Backticks only (`text`).\n7. Time Skips: Explicitly signaled with the tag [TIME SKIP].\n8. Native-Language Format: "Phrase in original language" ([your_language] translation).\n- OOC INSTRUCTIONS: Anything wrapped in ((OOC: ...)) must be treated as Out-Of-Character instructions.\n- EM DASHES BANNED: Never generate em dashes (—). Use commas, colons, or pipes instead.\n- META-TAGS BANNED: NO meta-tags (e.g., "System:", "Tier 1") in output.\n- GENDER ASSUMPTION BANNED: The AI MUST NEVER assume {{user}}\'s gender. Use AnyPOV macros ({{user}}, {{sub}}, etc.).\n</format_constraints>'
	);
	
		engineLorebook.push('<style_contract>\n' + "NARRATIVE PERSPECTIVE: Narrate in third-person omniscient present tense; the narrator may render any character's interior.FORMATTING MARKERS: *Asterisks* delimit character internal thoughts. \"Double quotes\" delimit dialogue. **Double asterisks** delimit emphasis. NATIVE LANGUAGE DIALOGUE: If a character speaks in a non-common language, it MUST be formatted exactly as: \"original language phrase\" (English translation).DIRECTOR-CARD RULE: This card acts as the World Director. It can control other NPCs, progress world events, and dictate the overarching narrative while remaining fully in-character as the primary driver of the scene." + '\n</style_contract>');
		engineLorebook.push('<style_notes>\n' + "TONE BALANCE: 70% cozy/slice-of-life (domestic warmth, college life) and 30% supernatural drama. HARD BANS: No lethal threats or grimdark elements. Family overprotection is trauma-shaped love, never malice. Avoid constant negativity/extreme tension unless explicitly requested. EM DASHES ARE BANNED. META-TAGS BANNED. Wulfnic Bloodmoon narrator framing: The perspective is third_omniscient, but the omniscient camera is Wulfnic's mind's eye watching his descendants. The Voice of the Prose carries his ancient gravitas: patient, detached, profoundly observant of bloodlines, biology, and pack dynamics. Frames modern concepts through the lens of a 1100-year-old Viking king. AnyPOV macros are mandatory." + '\n</style_notes>');

	// Multi-Bot Management
	var packMentions = 0;
	var packNames = ['erik', 'jasper', 'malachia', 'noah', 'wulfnic'];
	for (var i = 0; i < packNames.length; i++) {
		if (multiMsgWindow.indexOf(packNames[i]) !== -1) packMentions++;
	}
	if (packMentions > 1 || messageCount < 3) {
		engineLorebook.push(
			"<multi_bot_and_scene_management>\nCRITICAL DIRECTIVE: When {{char}} represents a Multi-Bot (multiple main characters), you MUST manage their locations and generate scenes dynamically based on their spatial grouping.\n1. Spatial Grouping Protocol:\n   - Before writing, evaluate where every active character is located.\n   - Group characters physically present in the same location into a SINGLE scene block.\n   - For characters in different locations, you MUST generate a SEPARATE scene block for each location.\n2. Dynamic Token Economy (Absolute Rules):\n   - TOTAL RESPONSE CAP: The entire output MUST NEVER exceed 1500 tokens.\n   - SINGLE SCENE: If all characters are in the same location (or if it's a 1-on-1 interaction), you may use up 1500 tokens to deliver a deep, detailed, and highly immersive narrative.\n   - SPLIT SCENES: If characters are divided across multiple locations, you must DIVIDE the available token budget EQUALLY among the generated scene blocks (e.g., 2 scenes = ~600-750 tokens each; 4 scenes = ~300-375 tokens each). Prioritize dense, high-impact prose and cut filler to fit these constraints.\n3. Scene Header Format: Always begin a split scene with a bracketed header indicating the location and active characters: `***[Date], [Time] - [Location] - [CHARNAME1], [CHARNAME2]***`\n</multi_bot_and_scene_management>"
		);
	}

	// Dynamic Character Engine
	var isIntimacy =
		/\b(kiss|touch|moan|skin|breath|lips|bed|clothes|heat|rut)\b/i.test(
			multiMsgWindow
		);
	var isCombat =
		/\b(fight|blood|strike|blade|gun|run|hide|growl|claws)\b/i.test(
			multiMsgWindow
		);
	var isMagic = /\b(spell|glamour|rune|magic|ritual|alpha command)\b/i.test(
		multiMsgWindow
	);

	var dynEngine =
		'<dynamic_character_engine>\nDo NOT use fixed, rigid archetypes. The attitude, body language, tone, and actions of ANY character must be generated dynamically by intersecting: Base Personality, Current Context, and Relationship Status.\n- Agency & Skepticism: NPCs are NOT yes-men. They have independent agendas, self-preservation instincts, and biases. They will argue, demand proof, or refuse illogical requests.\n';

	if (isIntimacy) {
		dynEngine +=
			"- Romance & Intimacy: Intimacy is character expression, not a script. A villain's touch is different from a protector's touch. Modulate pacing, sensory details, and arousal based purely on how that specific character would experience it.\n- Inner Monologue: Should reveal what the character's face hides. Modulate frequency to HIGH during intimacy.\n";
	} else if (isCombat) {
		dynEngine +=
			'- Height Dynamics & Space: Use physical differences logically. Taller characters may loom in anger or crouch in vulnerability. Do not apply behaviors mechanically—adapt them to the emotion of the moment.\n- Inner Monologue: Modulate frequency to LOW during combat.\n';
	} else {
		dynEngine +=
			"- Inner Monologue: Should reveal what the character's face hides. A hostile NPC might feel sudden fear; a stoic NPC might feel overwhelming affection.\n";
	}

	if (isMagic) {
		dynEngine +=
			'- Magic Integration: Characters should weave their unique magical abilities seamlessly into mundane tasks and extraordinary events, matching their personality.\n';
	}
	dynEngine +=
		'- Sound & Atmosphere: Use onomatopoeia (thud, whisper, hum) to enhance the specific vibe of the scene.\n</dynamic_character_engine>';
	engineLorebook.push(dynEngine);

	engineLorebook.push(
		'<anti_omniscience_logic>\nEnforce strict limited-perspective narrative for all NPCs.\n1. Sensory Lock: NPCs only know what they can see, hear, or feel right now.\n2. Epistemic Humility: NPCs must express genuine curiosity or ignorance regarding unknown variables.\n3. Deduction vs. Intuition: Avoid "gut feelings". Guesses must be supported by in-universe evidence.\n</anti_omniscience_logic>'
	);

	if (messageCount > 3) {
		engineLorebook.push(
			"<relationship_tracker>\nTrack incremental changes (±3% per interaction) in each NPC's relationship with {{user}} across Platonic, Romantic, and Sexual attraction.\nFormat:\n**MATRIX:**\n- ([CHARNAME1]→{{user}}): (Platonic: [X]%→[Y]%. Romantic: [X]%→[Y]%. Sexual: [X]%→[Y]%.)\n- RELATIONSHIP DYNAMIC: ([CHARNAME] and {{user}} have a [TYPE] relationship, marked by [A], [B], and [C].)\n</relationship_tracker>"
		);
	}

	var responseStructure =
		'<response_structure>\n**_[Date], [Time] - [Location] - [CHARNAME1], [CHARNAME2]_** (Include header ONLY if there are multiple locations/split scenes)\n[Char Name]: _"Internal thought regarding the situation."_\n[Third-person present tense narrative. Adjust length based on the Dynamic Token Economy. Focus on visceral reality, concrete actions, and dialogue. End with a hook.]\n\n--- (Use scene breaks only if there are multiple locations/groups)\n\n**_[Date], [Time] - [Location] - [CHARNAME3]_**\n[Repeat structure for split scenes]\n</response_structure>';
	engineLorebook.push(responseStructure);

	// =========================================================================
	// 13. MASTER CONTEXT MUTATION & OUTPUT CLAMPING
	// =========================================================================

	// Process and clamp personality injections from all engines (max 1200 chars)
	if (personalityAdditions.length > 0) {
		var formattedPersonality = '\n\n' + personalityAdditions.join('\n\n');
		if (formattedPersonality.length > 1200) {
			formattedPersonality = formattedPersonality.substring(0, 1200);
		}
		context.character.personality += formattedPersonality;
	}

	// Process and clamp scenario injections from all engines (max 1200 chars)
	if (scenarioAdditions.length > 0) {
		var formattedScenario = '\n\n' + scenarioAdditions.join('\n\n');
		if (formattedScenario.length > 1200) {
			formattedScenario = formattedScenario.substring(0, 1200);
		}
		context.character.scenario += formattedScenario;
	}

	// Push the dynamic core system directives into scenario (UNCLAMPED)
	if (engineLorebook.length > 0) {
		context.character.scenario += '\n\n' + engineLorebook.join('\n\n');
	}
})();

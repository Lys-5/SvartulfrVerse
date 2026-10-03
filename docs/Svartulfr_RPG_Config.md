# Svartúlfr - RPG Simulation Configuration

Questo documento contiene la configurazione ufficiale (bilanciata su PtB 25) per il modulo *Simulation* del World. I valori vanno inseriti nel pannello web di Wyvern.

## 1. Statistiche Base
- **MGT** (Might): Forza fisica, danno corpo a corpo.
- **RES** (Resilience): Resistenza fisica, HP, difesa.
- **AGI** (Agility): Velocità, schivata, mira.
- **WIT** (Wits): Intelligenza, tattica, magia.
- **PRS** (Presence): Carisma, intimidazione, aura.
- **SCT** (Scouting): Percezione, sensi ferini, fortuna.

*(Base value: 1. Point Budget: 25. Max Traits: 10)*

## 2. Species (Razze e Sotto-specie)

**HUMANS**
- **Human (Standard):** 0 mod (Base neutra)
- **Human (Magically Gifted):** WIT +2, MGT -1

**WERES & SHAPESHIFTERS**
- **Werewolf (Pureblood):** MGT +2, RES +1, SCT +1, WIT -1
- **Werewolf (Common):** MGT +1, RES +1, SCT +1, WIT -1
- **Shapeshifter:** AGI +2, SCT +1, RES -1

**DEMI-HUMANS**
- **Demi-Human (Apex Carnivore):** MGT +2, AGI +1, WIT -1
- **Demi-Human (Prey/Herbivore):** AGI +2, SCT +2, MGT -1, RES -1
- **Demi-Human (Avian/Reptilian):** AGI +1, WIT +1, RES -1

**HYBRIDS**
- **Hybrid (Large Brute):** MGT +3, RES +2, AGI -2, SCT -1
- **Hybrid (Serpentine):** MGT +1, AGI +1, PRS +1, RES -1
- **Hybrid (Aquatic):** AGI +1, RES +1, WIT +1, SCT -1

**DEMONS**
- **Demon (Brute / Ifrit):** MGT +2, RES +1, PRS -1
- **Demon (Succubus / Incubus):** PRS +3, AGI +1, RES -1, MGT -1

**FAE**
- **Fae (High/Sidhe/Dryads):** WIT +2, PRS +1, MGT -1
- **Fae (Small/Pixies/Sprites):** AGI +3, SCT +1, MGT -2, RES -1

**VAMPIRES**
- **Vampire (Elite):** PRS +2, AGI +1, MGT +1, RES -1

**UNDEAD**
- **Undead (Corporeal):** RES +3, MGT +1, AGI -2, PRS -1
- **Undead (Spectral):** WIT +2, AGI +1, MGT -2, RES -1


## 3. Occupations (Lavori, Ruoli LSE e Status Gerarchico)

**CIVILI E CORPORATIVI**
- **SUCC Student / Civilian:** PRS +1, WIT +1
- **DCC Security / PMC:** SCT +2, AGI +1
- **Street Scrapper / Rogue:** AGI +2, SCT +1

**GILDA E DUNGEON**
- **Guild Vanguard (DPS):** MGT +1, AGI +1
- **Guild Tank:** RES +2, MGT +1
- **Guild Support (Healer/Mage):** WIT +2, PRS +1

**LSE PACK AUTHORITY (Ruoli Operativi di Branco)**
- **Pack Leader:** PRS +2, WIT +1, SCT -1 *(Comando e visione strategica)*
- **Leader's Mate / Pack Mom:** PRS +2, RES +1, MGT -1 *(Protezione emotiva e organizzazione)*
- **Right Hand (Advisor/Peacekeeper):** WIT +2, PRS +1, MGT -1 *(Tattica, finanza e mediazione)*
- **Left Hand (Enforcer):** MGT +2, AGI +1, PRS -1 *(Protezione fisica ed esecuzione ordini)*
- **Caretaker / Breeder:** RES +2, PRS +1, MGT -1 *(Gestione domestica, cuccioli e prole)*

**LSE PACK ROLES (Funzioni Specifiche)**
- **Hunter / Provider:** AGI +1, SCT +1 *(Logistica e risorse)*
- **Defender:** RES +2 *(Protezione territoriale)*
- **Teacher:** WIT +2 *(Trasmissione della storia e delle abilità)*
- **Diplomat:** PRS +2 *(Relazioni inter-branco ed esterne)*
- **Scout:** SCT +2 *(Esplorazione e raccolta informazioni)*
- **Builder:** MGT +1, WIT +1 *(Mantenimento infrastrutture fisiche ed economiche)*

**HOUSE HIERARCHY (Status Politico)**
- **House Head (Lord/Patriarch):** PRS +2, WIT +1, AGI -1 *(Governa più branchi e domini)*
- **Knight (Sworn Warrior):** MGT +1, RES +1 *(Guerriero giurato o ufficiale)*
- **Citizen:** 0 mod *(Membro riconosciuto protetto dalla Casata)*


## 4. Traits (Tratti biologici e selezionabili)
- **LSE Alpha Biology:** PRS +2, WIT -1 *(Dominante, carismatico ma istintivo)*
- **LSE Beta Biology:** MGT +1, RES +1 *(Bilanciato e resiliente)*
- **LSE Omega Biology:** PRS +2, RES +1, MGT -2 *(Altamente empatico e ricettivo, ma fisicamente sottomesso)*
- **LSE Delta Biology:** SCT +2, PRS -1 *(Sensi ultra-sviluppati, distaccato)*
- **Lupine Senses:** SCT +2 *(Olfatto e udito extra)*
- **Silver Allergy:** RES -2 *(Malus severo passivo)*
- **Dungeon Veteran:** MGT +1, WIT +1 *(Esperienza sul campo)*
- **Feral Blood:** MGT +2, PRS -2 *(Fortissimo ma selvaggio/incontrollabile)*
- **Regenerative Factor:** RES +2 *(Guarigione rapida)*
- **Night Stalker:** AGI +1, SCT +1 *(Predatore notturno)*
- **Tech Savvy:** WIT +2 *(Perfetto per la DCC)*
- **Blood Craze:** MGT +2, RES -1, AGI -1 *(Furia berserker)*


## 5. Extra Occupations & Traits (dalle Schede Personaggio)
*Dall'analisi delle schede di Malachia, Scarlett, Angelo e Marcus.*

**EXTRA OCCUPATIONS:**
- **Pro Athlete / Fighter (es. MMA/Boxe):** MGT +1, AGI +1 *(Fisico al picco della condizione umana/sovrumana)*
- **Academic / PhD Candidate:** WIT +2 *(Ricerca e specializzazione di alto livello)*
- **Patriarch / Coven Leader:** PRS +2, WIT +1, MGT -1 *(Equivalente del Pack Leader per Vampiri e altre congreghe)*
- **Event Organizer / Fixer:** PRS +1, WIT +1 *(Gestione sociale, eventi, contatti)*

**EXTRA TRAITS:**
- **S.R.F. Veteran:** RES +1, WIT +1 *(Veterano della Supernatural Rehabilitation Facility, disciplina tattica e gestione del trauma)*
- **Cyber-Augmented (Sci-Fi / Vanguard):** RES +2, MGT +1, PRS -2 *(Impianti cibernetici che aumentano la resistenza ma riducono l'empatia)*
- **Symbiotic Feeder:** PRS +2, RES -1 *(Tipico di Succubi/Incubi: si nutre di emozioni e lussuria, ma fisicamente più fragile)*
- **Ancient Heritage:** WIT +1, PRS +1 *(Per Vampiri o esseri con secoli di ricordi e ricchezza accumulata)*

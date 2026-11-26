# Canonical Family Trees, Anti-Homonymy Firewall & Italian Shared-Relative Possessive Discipline

**Purpose:** Prevent LLMs from hallucinating false blood/family links between unrelated characters who share surnames or first names (such as `Mac Sanchez-Rogers` vs `Bailey Rogers`) and enforce natural Italian possessive pronouns (`nostro / nostra / nostri` vs `mio / tuo`) when family members discuss shared relatives.

**Synchronized Across:**
- World [`_YpX47fNraQFw2dD7TdycJ`](https://app.wyvern.chat) (`base_instructions`, `system_prompt_override`, `final_instructions`)
- AI Game Master [`simple_assistant_EYQTtcgTQfwh2RH9RG8z3`](file:///e:/repository/SvartulfrVerse/FINAL/assistants/Svartulfr_Game_Master_Assistant.json) & Sidechat `❤️Pack-Family❤️` [`simple_assistant_TqGKMBgr28JNeyRJ69mTN`](file:///e:/repository/SvartulfrVerse/FINAL/assistants/Pack_Family_Assistant.json)
- Prompt Assembly [`pha_kWkWUAfTJTF9q72c2bC98`](file:///e:/repository/SvartulfrVerse/FINAL/prompts/Svartulfr_Master_TTRPG_Prompt_Assembly.json) (including Depth 4% `<anti_drift_guardrails>`) & [`PROMPT_OVERRIDES_WYVERN.md`](file:///e:/repository/SvartulfrVerse/FINAL/PROMPT_OVERRIDES_WYVERN.md)
- World Lexicon [`_4GV6zfBjPE9mcaEy17hPx`](file:///e:/repository/SvartulfrVerse/FINAL/Svartulfr_Lorebook_II.json) (`House Genealogies Summary`) + dedicated `Firewall Omonimie & Non-Parentele (Chi NON e' Imparentato)` entry in World Lexicon and [`Svartulfr_Lorebook_I.json`](file:///e:/repository/SvartulfrVerse/FINAL/Svartulfr_Lorebook_I.json)
- World Characters [`_MbAPCTW3C8hhJ4qct9Mr2`](file:///e:/repository/SvartulfrVerse/FINAL/Svartulfr_Characters.json) (`Naomi Black`, fixed erroneous co-ruler reference from `Harrison Black` to `Cass Harrow`), `Bailey Rogers` (`_FLnMQYPgHKVkjfz7ywLV3`), `Dominic Rogers` (`_QrByAWBBMBAW9qC7WxAwY`), `Mackenzie "Mac" Sanchez-Rogers` (`_RXHKfwRXwhRkBHttHVgqt`) & [`Svartulfr_NPC_Primary.json`](file:///e:/repository/SvartulfrVerse/FINAL/Svartulfr_NPC_Primary.json)
- Standalone Character Cards (`/mine`): `Erik`, `Logan`, `Malachia`, `Noah`, `Jasper`, `Edric`, `Wulfnic`, and `Mac Sanchez-Rogers` (`post_history_instructions` + Mac `description`).

---

## 1. Regola Obbligatoria sui Pronomi Possessivi Italiani (`nostro` vs `mio/tuo`)

Prima di scrivere `mio/mia/tuo/tua` davanti a un nome di parentela (`nonno`, `nonna`, `padre`, `papà`, `madre`, `mamma`, `fratello`, `sorella`, `zio`, `zia`, `cugino`, `cugina`, `nipote`), verificare **entrambi** gli interlocutori (chi parla e chi ascolta):

| Relazione (Parlante -> Ascoltatore) | Persona Menzionata | Forma Obbligatoria | Vietato |
| :--- | :--- | :--- | :--- |
| Tra fratelli **Malachia, Noah, Jasper, Alyssa** | **Wulfnic Bloodmoon** | **`nostro nonno`** / `Nonno Nic` | `tuo nonno`, `mio nonno` |
| Tra fratelli **Malachia, Noah, Jasper, Alyssa** | **Erik Douglas** | **`nostro padre`** / `papà` | `tuo padre`, `mio padre` |
| Tra fratelli **Malachia, Noah, Jasper, Alyssa** | **Nixara Bloodmoon** | **`nostra madre`** / `mamma` | `tua madre`, `mia madre` |
| Tra fratelli **Malachia, Noah, Jasper, Alyssa** | **Magnus / Elizabeth** | **`nostro nonno Magnus`** / **`nostra nonna Elizabeth`** / `i nostri nonni` | `tuo nonno`, `tua nonna` |
| Tra fratelli **Malachia, Noah, Jasper, Alyssa** | **Logan Douglas** | **`nostro zio`** / `Zio Logan` | `tuo zio`, `mio zio` |
| Tra fratelli **Malachia, Noah, Jasper, Alyssa** | **Edric Douglas** | **`nostro cugino`** | `tuo cugino`, `mio cugino` |
| Tra fratelli **Malachia, Noah, Jasper, Alyssa** | Uno degli altri 3 fratelli | **`nostro fratello`** / **`nostra sorella`** | `tuo fratello` |
| Tra **Erik** e **Logan** | **Magnus / Elizabeth / Cornelius** | **`nostro padre`** / **`nostra madre`** / **`nostro nonno`** | `tuo padre`, `tua madre` |
| Cugini (**Malachia/Noah/Jasper/Alyssa <-> Edric**) | **Magnus / Elizabeth** | **`nostro nonno Magnus`** / **`nostra nonna Elizabeth`** | `tuo nonno` |
| **Erik / Logan / Edric -> Alyssa/Jasper/Noah/Malachia** | **Wulfnic Bloodmoon** | **`tuo nonno`** / **`vostro nonno`** / `Nonno Nic` *(NON e' parente di sangue di Erik/Logan/Edric)* | `nostro nonno` |
| **Estranei / Amici** (`Jared`, `Mac`, `Bailey`, `Finn`, `Sierra`, `Scarlett`) | Qualsiasi parente di `{{user}}` | **`tuo ...`** / **`vostro ...`** | `nostro ...` |

---

## 2. Firewall Omonimie & Non-Parentele (Estranei Confermati)

Cognomi o nomi identici o parzialmente sovrapponibili **NON implicano mai** parentela, branco o casata comune se non dichiarati nelle schede:

| Persona A | Persona B | Verdetto | Motivo |
| :--- | :--- | :--- | :--- |
| **Mackenzie "Mac" Sanchez-Rogers & Luisa Sanchez-Rogers** (Werewolves, madre Andrea Sanchez) | **Bailey Rogers & Dominic Wayne Rogers** (Incubi, madre/moglie Lara Rogers) | **ESTRANEI ASSOLUTI (Zero parentela)** | Omonimia casuale sul cognome comune "Rogers" |
| **Mackenzie "Mac" Sanchez-Rogers** (Keyboardist *Grave Mistake*, Oakland/Solarton) | **Roger "Rocky" Mackenzie** (Werewolf scozzese, ex *Lone Howlers*) | **ESTRANEI ASSOLUTI** | Omonimia casuale su "Mackenzie/Mac" |
| **Roman Blackwood** (Wolf Demihuman, SUCC) | **Casata Douglas / Fondatori di Blackwood City** | **ESTRANEI ASSOLUTI** | Omonimia anagrafica |
| **Naomi Black** (Werewolf Beta, co-leader Uptown North con **Cass Harrow**) | **Councilman Harrison Black** (Umano/dio greco, Concilio) / **Miles Black** (Vampiro) | **ESTRANEI ASSOLUTI** | Omonimia sul cognome "Black" *(corretto anche il refuso su scheda NPC Naomi Black)* |
| **Russell "Russ" Sinclair** (Tiger Demihuman, compagno di stanza di Jasper) | **Dr. Arthur Sinclair** (`Sloth`, Mutante/Chimera) | **ESTRANEI ASSOLUTI** | Omonimia sul cognome "Sinclair" |
| **Finnegan "Finn" Novak** (Arctic Wolf Demihuman, figlio unico di Caitlyn & Lee Novak) | **Verena Novak** (Demonkin) / **Kellan Novak** (Dragon) | **ESTRANEI ASSOLUTI** | Omonimia sul cognome "Novak" |
| **Jasper Douglas-Bloodmoon** | **Jasper Rowan** (Ghost, Camp Mystic) | **ESTRANEI ASSOLUTI** | Stesso nome di battesimo |
| **Noah Douglas-Bloodmoon** | **Noah Grant** (Ghost, Camp Mystic) | **ESTRANEI ASSOLUTI** | Stesso nome di battesimo |
| **Erik Douglas** | **Eric** (Fox Demihuman, SUCC) | **ESTRANEI ASSOLUTI** | Nome simile |
| **Fenris** (First Wolf / Divinita') | **Fenrir** (`DDM Contractor #06`) | **ENTITA DISTINTE** | Nessun legame familiare |
| **Dominic Wayne Rogers** (Incubus, Solarton) | **Dominic Chen** (Pureblood Werewolf Alpha) | **ESTRANEI ASSOLUTI** | Stesso nome di battesimo |
| **Marcus Iron Thornfield** (DMHA/DCC) | **Marcus "Mark" O'Connor** (Oldtown) / **Marcus Vale** (Camp Mystic) | **ESTRANEI ASSOLUTI** | Stesso nome di battesimo |
| **Altri cluster di cognomi non imparentati** | `Chase Anderson != Aiden Anderson`; `Harlan Beaumont != Bram Beaumont`; `Angelo Moreno != Asher Moreno`; `Hugh Rivers != Mateo Rivers`; `Darius Vale != Marcus/Elara/Cassian Vale`; `Marlowe Voss != Mara/Nadia/Evan Voss`; `Vespera Thorne != Aris/Silas Thorne`; `Damien Bishop != Naomi Bishop`; `Iris Callow` / `Vesper Callow` (verificare caso per caso, mai inventare legami) | **ZERO PARENTELA SE NON ESPLICITA** | Nessun legame dichiarato in scheda |

---

## 3. Alberi Genealogici Canonici Riepilogativi

1. **Casata Douglas-Bloodmoon (Merged Dynasty):**
   - **Linea Douglas (Pureblood):** Lord Cornelius Douglas (dec.) -> figlio ed erede **Magnus Douglas III** (355, n. 29 dic 1668) + moglie **Elizabeth Duskwood** (House Duskwood, Pureblood Omega, 76, n. 14 lug 1947, presentata 1966) -> figli **Erik Ulfr Douglas** (54/55, n. 31 ott 1969) e **Logan Járn Douglas** (49, n. 12 gen 1975). Figlio di Logan: **Edric Douglas** (13, n. 25 feb 2011; cugino dei 4 figli di Erik, NON nipote di Wulfnic).
   - **Linea Bloodmoon (Divine Blood / Founding Bloodline):** **Wulfnic Báleygr Bloodmoon** (Firstborn, n. 21 dic 824 d.C.; shield-brothers conviventi Ut Berg e Zefir) -> figlia **Nixara Hvít Bloodmoon** (dec., White Moon, 9 giu 1975 – 22 apr 2005).
   - **Figli di Erik Douglas & Nixara Bloodmoon (4 fratelli):** **Malachia** (`Vígit`, Alpha, n. 10 ago 1996), **Noah** (`Loki`, Delta, n. 5 ott 1998), gemelli **Jasper** (`Svartr`, Beta, n. 22 apr 2005) e **Alyssa** (`Hvít`, Fourth White Moon Omega, n. 22 apr 2005).
2. **Altre Famiglie Canoniche Confermate:**
   - **Sanchez-Rogers (Oakland/Solarton):** Madre **Andrea Sanchez**, padre assente (NON Dominic Rogers); figli **Luisa** (27), **Mackenzie "Mac"** (19, discendente inconsapevole di Garmr Kjalki), **Mario**, **James**.
   - **Rogers (Incubi, Louisiana/Solarton):** **Dominic Wayne Rogers** (50) + **Lara Rogers** (umana, dec.) -> figlio unico **Bailey Rogers** (22, SUCC Bulls).
   - **Thompson (Half-Minotaur/Holstaur, Solarton):** **Hank** (51) & **Jasmin** (48) -> 9 figli: **Jared** (22), **Janice** (21), **Jake** (20), gemelli **Jaiden & Jason** (18), **Jeremy** (16), **Jet** (13), **Jerry** (10), **Julie** (6).
   - **Davies (Werewolves, Solarton):** **Stanley Davies Sr.** (50) & **Eris Davies nee Lopez Ortega** -> figlio unico **Stan Davies** (21).
   - **House O'Connor (Oldtown Blackwood):** Alpha **Marcus "Mark" O'Connor** (45), figlia minore **Nicole O'Connor** (22), consanguineo **Liam O'Connor** (27).
   - **Steeltooth Clan (Orc, Solarton):** Patriarca **Nahgigoth** -> figli **Ikkath** e **Larek Steeltooth** (21, SUCC); zio **Morgeth Steeltooth** (42, fabbro Half-Orc/Half-Eadra).
   - **Nargathon Lineage:** **Dr. Airen Nargathon** (72, umano, Project BlackWolf) -> figlio biologico **Commander Kaladin Nargathon** (45, Beta/Alpha militare DCC, nessun sangue Douglas).
   - **House Darkfire (Vax Demons, Horned Skull Clan):** Patriarca **Varg Darkfire** (800) -> figli **Zeera** (137), **Aras** (124), **Karshin** (118), **Boros** (112).
   - **Campbell Vampire Line (Montreal/SUCC):** **Leonard** & **Maria Campbell** -> **Vincent "Vince"** (22), **Andrew "Andy"** (22), **Elice** (19).
   - **DeVille (Humans):** Ex-coniugi **Alistair Ambrose DeVille** & **Amelia DeVille** -> figlio **Charles "Charlie" DeVille** (28).
   - **Locke Brothers (Texas/Blackwood):** Fratelli separati **Adrian Locke** (werewolf) e **Garrett Locke** (vampire).
   - **Novak Household:** **Caitlyn & Lee Novak** -> figlio unico **Finnegan "Finn" Novak** (19).
   - **Convergenza dei Firstborn (7/9 rivelati):** Wulfnic -> Malachia (`Vígit`), Ut Berg -> Thorvald, Zefir -> Zefir, Svartr -> Jasper, Garmr Kjalki -> Mac Sanchez-Rogers, Sigvaldi Blóðöx -> Harald Sigurdsson, Rúnólfr Völundr -> Iordan R. Vess (ramo islandese distante nella famiglia NZ); restano latenti **Brandr Eldstígi** e **Kári Hafgufa**.

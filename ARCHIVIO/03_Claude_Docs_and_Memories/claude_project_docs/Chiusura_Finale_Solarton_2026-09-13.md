# Chiusura finale del roster Solarton (2026-09-13)

Riverifica live di tutti i 46 personaggi della cartella Character "Solarton", per confermare che i buchi sistemici documentati in `Audit_Completezza_SUCC_2026-09-13.md` e presumibilmente chiusi in `Chiusura_Buchi_Sistemici_SUCC_2026-09-13.md` fossero davvero chiusi, prima di passare a Los Angeles e Blackwood come richiesto dall'utente.

## Esito

44 dei 46 personaggi risultavano già completamente a posto: `long_summary`, `display_description`, 5+ outfit con Default impostato, 5 Dialogue Examples, `final_instructions` con la riga di format discipline, `birthdate === start_timeline_position`. Nessuna sorpresa, conferma che il lavoro di ieri e di oggi ha tenuto.

Trovati solo due mismatch birthdate/Start Position, entrambi risolti:

**Barkley Rover**: aveva già `start_timeline_position` (10205376, corrispondente esattamente a 32 anni rispetto all'età odierna del World) ma nessun `birthdate`, e il campo AGE nel `long_summary` era ancora scritto in chiaro ("32") invece che con la macro `{{age}}`. Correzione puramente meccanica, nessuna invenzione: copiato lo stesso valore nel campo `birthdate` e convertita la macro.

**Dullahan**: caso diverso, sottoposto all'utente prima di procedere per via della sua natura di Immortal Contractor DDM (AGE narrativo: "unknown, born in France in the 1700s"). L'utente ha scelto di assegnare una data meccanica nel 1700s senza toccare la prosa, come già fatto per Oskar. Nello scegliere la data è emerso un vincolo interessante: il suo `start_timeline_position` esistente era già impostato al **1724-01-01**, deliberatamente molto presto, quasi certamente per garantire che un Immortal Contractor risulti presente in qualunque scenario del World, inclusi quelli fuori epoca già previsti (viaggio di Wulfnic, scenario piratesco di Cornelius). Un birthdate successivo al 1724 avrebbe reso Dullahan "non ancora nato" nel suo stesso Start Position, quindi la data scelta è il **14 settembre 1710**, prima del suo Start Position e comunque coerente con "born in the 1700s". Verificato che `birthdate < start_timeline_position`. Testo AGE lasciato invariato ("unknown, born in France in the 1700s").

## Stato del roster Solarton

Con questi due fix, tutti e 46 i personaggi della cartella Solarton risultano completi su ogni passo della pipeline §14: `long_summary`/`summary`/`display_description`, 5+ outfit con Default, 5 Dialogue Examples, Attitudes verso almeno Alyssa e Jasper, `final_instructions` con disciplina di formato, `birthdate`/`start_timeline_position` coerenti, Global Character ON. Nessun punto aperto residuo su Solarton.

## Prossimo passo

Su richiesta dell'utente, si passa ora agli NPC ancora da lavorare nelle cartelle **Los Angeles** (21 personaggi) e **Blackwood** (9 personaggi). Non ancora auditate in questa sessione: da fare lo stesso controllo sistematico (long_summary/display_description/outfit/Dialogue Examples/Attitudes/birthdate/format-discipline) prima di iniziare a scrivere.

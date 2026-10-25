import json

path_loc = 'FINAL/Svartulfr_Location.json'
with open(path_loc, 'r', encoding='utf-8') as f:
    data = json.load(f)

entries = data.get('entries', [])
lexicon = data.get('lexicon', [])

print(f"Initial Location counts: entries={len(entries)}, lexicon={len(lexicon)}")

bricklane_update = """Bricklane Mall e un pittoresco centro commerciale all'aperto situato a breve distanza dal cuore pulsante di Solarton e dal perimetro della SUCC, caratterizzato da bassi edifici in mattoni rossi a due piani affacciati su vicoli pedonali lastricati. Nessun grande franchising e presente: vi sorgono boutique indipendenti, botteghe esoteriche e servizi dedicati a una clientela mista. Tra le attivita piu note spicca Medusa's, il salone di acconciatura piu in voga della contea, rinomato per tagliare, pettinare e curare capigliature di ogni tipo (siano esse composte da capelli umani, chiome serpentine viventi, piume arpie o criniere leonine). Poco distante sorge lo Yeti Shack, un frequentatissimo chiosco specializzato in granite termoregolatrici, ghiaccioli arcani e dolci sottozero progettati per consentire a specie a temperatura corporea elevata di affrontare il caldo estivo. Due cortili alberati alberati con jacarande e panchine in ferro battuto offrono spazio per il relax pomeridiano degli studenti tra una lezione e l'altra."""

sidewinders_update = """Sidewinders Bar & Nightclub e uno dei punti di riferimento storici della vita notturna di Solarton. Strutturato su due livelli con pub e bancone in legno scuro al piano terra, e pista da ballo con salette prive di luce naturale e zona VIP schermata al piano superiore, il locale ha segnato una svolta fondamentale nella storia cittadina: fu infatti il primissimo esercizio commerciale di Solarton ad abbattere le storiche leggi discriminatorie e ad aprire ufficialmente le porte alla clientela vampirica dopo la Crisi Notturna del 1999. Benche oggi la clientela studentesca preferisca talvolta i club piu moderni o le feste di confraternita, Sidewinders conserva il suo fascino iconico e alternativo, offrendo drink classici, pozioni energetiche e riserve ematiche sigillate per non-morti."""

highschool_update = """Solarton High School e il liceo pubblico della cittadina, situato in un campus alberato con edifici in mattoni degli anni '70, campi sportivi regolamentari e pista d'atletica. L'istituto e celebre nella regione per il suo prestigioso programma di borse di studio sportive, che ha formato numerosi atleti approdati poi nelle formazioni universitarie dei Bulls e dei Bears della SUCC. Recentemente il complesso ha subito estesi interventi di ristrutturazione architettonica per eliminare ogni barriera e rendere aule, spogliatoi e laboratori accessibili a studenti non-umanoidi, taurini e ibridi alati. Tra i docenti storici della scuola figurano Hank Thompson, che insegna Educazione Fisica e allena le giovanili, e Stanley Davies Senior, che ricopre il ruolo di professore di Matematica."""

for e in entries:
    name = e.get('name', '')
    if name == 'Bricklane Mall':
        e['content'] = bricklane_update
    elif name == 'Sidewinders Bar & Nightclub':
        e['content'] = sidewinders_update
    elif name == 'Solarton High School':
        e['content'] = highschool_update

for l in lexicon:
    name = l.get('name', '')
    if name == 'Bricklane Mall':
        l['content'] = bricklane_update
    elif name == 'Sidewinders Bar & Nightclub':
        l['content'] = sidewinders_update
    elif name == 'Solarton High School':
        l['content'] = highschool_update

with open(path_loc, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated Location: entries={len(entries)}, lexicon={len(lexicon)}")

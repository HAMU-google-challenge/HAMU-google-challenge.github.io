# Verifiche del sito HAMU

Consegna verificata il 1 ottobre 2026 sul nuovo regolamento unificato, con confronto integrale rispetto al PDF precedente e coordinamento con le note del 24 settembre.

| Controllo | Esito |
|---|---|
| Compilazione Jekyll 3.10.0 con Ruby 3.1.3 | Superata |
| Output alla radice del dominio | 3 pagine HTML, 83 riferimenti locali verificati |
| Output in sottocartella `/hamu-demo` | 3 pagine HTML, 83 riferimenti locali verificati |
| URL ricavati dai metadati di Pages | Verificati su una copia tramite lo script del workflow |
| Download, ancore e collegamenti IT/EN | Tutti i riferimenti locali risolti |
| Stato in preparazione con nuovo modulo | Link al modulo richiesto dall’utente e avviso che non accetta risposte, in entrambe le lingue |
| Stato aperto senza informativa | Nessun pulsante di candidatura e nessun collegamento di anteprima del modulo; 85 riferimenti locali verificati |
| Stato aperto con modulo e informativa | Pulsante di candidatura presente in entrambe le lingue; 83 riferimenti locali verificati |
| Stato chiuso | Nessun pulsante di candidatura o anteprima del modulo; 85 riferimenti locali verificati |
| Anteprima e indicizzazione | `noindex` e blocco robots presenti; sitemap vuota |
| Modalità definitiva | Sulle copie di verifica: `noindex` rimosso dalle homepage, sitemap con due URL e robots aggiornato |
| Output pubblico | File di sviluppo, `FONTI.md` e `LOGHI.md` esclusi |
| JavaScript | Controllo sintattico con Node superato |
| Dati comuni | Dieci Atenei, dieci FAQ per lingua e griglia di valutazione da 100 punti |
| Anteprima portabile | 3 pagine HTML, 83 riferimenti locali verificati dopo la conversione |
| Download | Cinque file coincidenti byte per byte con le copie in HAMU e nell’anteprima; PDF ricevuto immutato |
| Differenze nel repository | Controllo degli spazi superato; modifiche preesistenti a `Gemfile.lock` conservate |

Le cinque configurazioni (radice, sottocartella, apertura senza privacy, apertura completa, chiusura) sono state compilate su copie temporanee. La consegna mantiene `preview: true`, `registration.state: planned` e `documents_need_alignment: true`.

## Contenuti e loghi

- Tempi di formazione dei team indicati come da confermare in descrizione, calendario e FAQ: il nuovo PDF mantiene l’anticipo di una settimana, in divergenza con le note del 24 settembre. Nessuna delle due modalità è presentata come confermata sul sito.
- Il 6 novembre riguarda la sede assegnata; i tempi di comunicazione dei temi sono indicati come da precisare.
- Chieti-Pescara confermata come Ateneo ospitante, con aula e indirizzo da comunicare; Politecnica delle Marche preferita e da confermare; Umbria in definizione.
- Avviso sui documenti visibile in entrambe le lingue: spiega la divergenza sui team. Il nuovo PDF è il download principale ed è identico all’allegato; le copie Word IT/EN e l’avviso recepiscono le modifiche dell’articolo 3. La locandina è stata ridisegnata il 1 ottobre con i dieci loghi; non specifica i tempi ancora da chiarire per team e temi.
- Modulo corrente https://forms.gle/fAHHkY52ppsiemvu5, richiesto direttamente dall’utente: risposta HTTP 200, destinazione Google Forms `/closedform`, titolo della Challenge e messaggio che non accetta risposte. Nessun invio effettuato. Il precedente link `MFsfjNUiUNsmnSiy8` è assente dalle pagine pubbliche.
- Sezione Formazione conservata nelle due lingue, con tre argomenti, durata e orario indicativi, attestato previsto e precisazione sui CFU.
- Dieci loghi locali, nomi completi e collegamenti istituzionali, raggruppati 4 + 4 + 2; nessuna modifica ai file grafici. Decodifica e dimensioni controllate; ispezione visiva degli originali già completata nella consegna precedente.
- Nessuna capienza candidata, dotazione o parcheggio presentato come disponibilità prenotata. Nessuna approvazione o modifica dei requisiti dedotta dal solo ordine del giorno.

## Verifica del nuovo regolamento e delle copie modificabili

- Confrontati i 18 articoli del PDF nuovo (14 pagine) e precedente (13 pagine). Cambiamenti sostanziali: termine massimo della finale all’art. 3.3 e nuova esclusione all’art. 3.6. Corretto il titolo dell’art. 12 nel sommario; gli articoli sui team restano invariati.
- Riscontrati nel nuovo PDF tutti i paragrafi del corpo italiano e le celle della griglia (173 blocchi), normalizzando spazi, punteggiatura e legature tipografiche.
- Copie Word IT/EN: 18 articoli, clausola 3.6 inserita con numerazione coerente, griglia da 100 punti conservata; otto pagine ciascuna, tutte renderizzate e ispezionate.
- Avviso: tre pagine renderizzate e ispezionate; aggiornati sia il testo dei requisiti sia il termine della finale nella tabella del calendario.
- PDF nuovo e tre DOCX: identità dei file verificata fra materiali, sorgenti del sito, compilazione e anteprima. I cinque collegamenti ai documenti puntano ai file correnti; il precedente PDF resta conservato, senza essere il download principale.
- Date e requisiti sul sito: finale entro fine 2026 e possibilità di esclusione successiva presenti in entrambe le lingue; settimana del 23 novembre esplicitamente indicativa. I loghi e le sedi già recepite non sono cambiati.

## Nuova locandina del 1 ottobre

- PDF A3 verticale, una pagina da 297 × 420 mm; testi vettoriali con font Rubik incorporati. SVG modificabile con immagini e font incorporati; PNG da 3508 × 4961 pixel a 300 dpi e anteprima leggera.
- Rendering del PDF ispezionato nella pagina completa e nel dettaglio dei loghi. Dieci loghi originali, proporzioni e colori conservati; la risoluzione effettiva dipende dai file già forniti, senza ricostruzioni dei marchi.
- Date, gratuità, tre sedi regionali, masterclass e dimensioni dei team riscontrate nei dati correnti. Finale con data da comunicare; nessun tempo di formazione dei team presentato come confermato.
- La locandina rimanda a `https://hamu-google-challenge.github.io/`: tutti i collegamenti nel PDF e nell’SVG portano al sito, senza link diretti al modulo né QR. Il sito IT/EN mantiene il link `https://forms.gle/fAHHkY52ppsiemvu5`. Nuovo rendering ispezionato; colori, dati, dieci loghi e dicitura «AI tools» conservati.
- Copia PDF aggiornata nei download; nuova compilazione alla radice e anteprima portabile controllate con 83 riferimenti locali per ciascuna. Verificata identità delle copie della locandina in materiali, sorgenti, compilazione e anteprima. Gli archivi di consegna sono stati rigenerati.

## Limiti della verifica

Il workflow GitHub Actions è incluso; non è stato eseguito un push o un deployment remoto durante questo aggiornamento. Le gem native sono state eseguite su macOS. Il lockfile include Ruby, Linux x86_64 e macOS ARM64; non è stata eseguita una compilazione Linux in questa sessione.

La verifica visiva del layout e delle interazioni nel browser resta da completare: il controllo di sicurezza aveva rifiutato l’apertura dell’URL `file://` dell’anteprima. Non sono stati utilizzati aggiramenti. I controlli della struttura HTML e degli asset non equivalgono a una verifica visiva o a un audit di accessibilità.

L’anteprima esportata si apre dal proprio computer tramite `hamu-anteprima/index.html`, conservando tutte le sottocartelle. La verifica dei collegamenti locali non costituisce un monitoraggio della disponibilità dei siti esterni.


La locandina è stata aggiornata su richiesta dell’utente: «Google» nel titolo passa a 76 punti, in lime; in fondo compare «Locandina generata con l’ausilio di AI tools.». PDF, PNG e SVG rigenerati; pagina renderizzata e ispezionata, percorso locandina → sito → modulo verificato, dieci loghi conservati.

## Aggiornamento locandina del 6 ottobre

- Date organizzate in tre riquadri: iscrizioni (scadenza 3 novembre 2026), fase iniziale (13 novembre 2026) e fase finale (data da confermare, Università dell'Aquila).
- PDF A3, PNG per stampa a 300 dpi, anteprima e SVG rigenerati. Rendering completo ispezionato; dieci loghi originali e credit «AI tools» conservati.
- La locandina continua a rimandare al sito GitHub, verificato disponibile. Il sottodominio universitario presenta ancora errori HTTP/TLS; l'analisi è stata effettuata in sola lettura e non costituisce un'attivazione del dominio.
- Nuova compilazione Jekyll e anteprima portabile: tre pagine HTML e 83 riferimenti locali verificati in ciascuna. PDF identico nelle copie materiali, sorgenti, compilazione e anteprima; collegamento al modulo richiesto presente in entrambe le lingue.


## Controlli prima della pubblicazione del 10 ottobre

- Modulo nuovo `https://forms.gle/m8npVRMSNzRwhz2x6`: HTTP 200, titolo della Challenge, campi e pulsante «Invia» visibili. L’utente conferma l’apertura. Nessuna candidatura compilata o inviata. Rilevato e segnalato il segnaposto `@@@@@` per il regolamento; non è stato ricavato un URL di informativa specifica dalla dichiarazione sull’uso dei dati.
- Iscrizioni aperte nel sito IT/EN; due collegamenti al nuovo modulo per lingua, nella testata e nella sezione dedicata. Il collegamento all’informativa è gestito separatamente. Nessun vecchio URL o avviso di modulo chiuso nelle pagine compilate.
- Locandine IT/EN: frase promozionale aggiornata, «Tre sedi / Three venues», dieci loghi originali, tre tappe del calendario e credit «AI tools». La data della finale resta da confermare. Le due versioni sono scaricabili dal sito.
- Due PDF A3 di una pagina, font incorporati, due link HTTPS ciascuno verso il sito nella lingua corrispondente. Nessun QR né link diretto al modulo. Versioni SVG e PNG a 300 dpi (3508 × 4961 pixel) rigenerate. Rendering completi in entrambe le lingue ispezionati; margini e testi nei tre riquadri delle date verificati.
- `https://hamu.univaq.it/` e `/en/` restituiscono HTTP 200 con verifica TLS riuscita. Il repository remoto ha aggiunto `CNAME` dopo l’ultima copia locale: la pubblicazione dell’aggiornamento deve conservare questa configurazione.
- Compilazione Jekyll e anteprima portabile: tre pagine HTML e 83 riferimenti locali verificati per ciascuna. Entrambi i PDF sono identici byte per byte nei materiali, nei sorgenti del sito, nella compilazione e nell’anteprima.

- Tentativo di pubblicazione: il connettore GitHub ha restituito HTTP 403 «Resource not accessible by integration» al primo inserimento di un oggetto. Nessun commit, aggiornamento del ramo o deployment è stato effettuato. Il sito online conserva il vecchio modulo; i file di consegna sono pronti per la pubblicazione.


## Coordinamento grafico con la locandina: 10 ottobre

- Rubik Regular e Bold installati in `assets/fonts/`: identità byte per byte con i file usati per le locandine; licenza SIL OFL 1.1 e attribuzioni incluse. Due font precaricati nella versione web; dati del font incorporati nel CSS dell’anteprima offline.
- Titolo con Google lime, HAMU bianco e anno lime sul blu scuro; stessa frase promozionale e tre forme intrecciate della locandina. Riquadro verde con tre tappe principali, schede e pulsanti arrotondati, blocco iscrizioni coerente. Layout adattato tramite media query per schermi stretti; loghi originali e contenuti operativi conservati.
- Nuova compilazione Jekyll: tre pagine HTML e 89 riferimenti locali verificati; anteprima portabile: tre pagine e 83 riferimenti (i preload dei font sono rimossi perché il CSS li incorpora).
- Due collegamenti al modulo corrente per lingua; tre tappe e testi corretti in IT/EN; font, date e PDF delle locandine coincidenti fra materiali e copie del sito. Controllo delle differenze e sintassi JavaScript superati.
- Il controllo visivo automatico con Chromium non è stato eseguito: l’ambiente ha negato l’avvio del processo con errore MachPortRendezvous, Permission denied (1100), anche dopo l’abilitazione della rete. Non sono state prodotte schermate. Le verifiche della compilazione e dei collegamenti non certificano l’impaginazione visiva né le interazioni su desktop e telefono; è disponibile l’anteprima locale per la revisione manuale.
- Nessun commit o push eseguito: pubblicazione manuale a cura dell’utente, come concordato.

## Sostituzione loghi del 10 ottobre

- UniMC (591 × 251 px), Università di Camerino (2678 × 1066 px) e GSSI (1939 × 871 px): file del sito identici agli allegati, dimensioni HTML aggiornate in IT/EN e dieci loghi totali. I due file con estensione superata sono rimossi dagli asset correnti; copie precedenti conservate nell’area di lavoro.
- Locandine italiana e inglese rigenerate in PDF A3, SVG modificabile e PNG a 300 dpi; entrambe le anteprime complete ispezionate visivamente. I tre nuovi marchi sono presenti nei PDF alla risoluzione originale, con proporzioni conservate. I testi estratti coincidono con quelli precedenti e ciascun PDF mantiene due link al sito nella lingua corretta.
- Compilazione Jekyll: tre pagine e 89 riferimenti locali verificati; anteprima portabile: tre pagine e 83 riferimenti. Due link al modulo corrente per lingua. PDF e nuovi loghi identici fra materiali, sorgenti, compilazione e anteprima.
- I limiti già riportati sulla verifica visiva del sito nel browser restano invariati. Nessun commit, push o deployment eseguito.

## Logo dell’Università d’Annunzio: 12 ottobre

- Sostituito `unich.png` con una copia integrale dell’allegato `logo_UdA.png`, 1689 × 708 px; aggiornate le dimensioni nelle pagine IT/EN. Identità del file verificata in sorgenti, compilazione e anteprima.
- Rigenerate le locandine italiana e inglese in PDF A3, SVG modificabile e PNG a 300 dpi. Entrambe le anteprime complete ispezionate visivamente. Verificati dieci loghi, conservazione dei pixel dell’allegato nell’SVG e risoluzione originale nel PDF; nessuna modifica ai testi e ai collegamenti rispetto alla versione precedente.
- Compilazione Jekyll: tre pagine e 89 riferimenti locali; anteprima: tre pagine e 83 riferimenti. Conservati due collegamenti al modulo corretto per lingua. Copie dei PDF allineate fra materiali, sorgenti, compilazione e anteprima.
- Restano i limiti precedentemente documentati sulla verifica visiva del sito nel browser. Aggiornamento locale pronto per commit e pubblicazione manuali.

## Introduzione e sintesi del regolamento: 12 ottobre

- Apertura IT/EN riscritta per spiegare formazione e sfida collaborativa tra studenti degli atenei HAMU; introduzione e tre passaggi descrivono tema proposto, lavoro in team e presentazione. Conservata la condizione «ove possibile» sulla varietà degli atenei e delle competenze nei team.
- Link diretto al PDF del regolamento nella testata e nella sezione iscrizioni. Nuova sintesi con otto punti elenco, link al PDF e ai documenti, richiamo al testo completo e nota sui tempi dei team. Accesso dalla testata e dal menu; sezione collocata prima dei dettagli sulla formazione.
- Compilazione alla radice e con prefisso `/hamu-demo`: tre pagine e 95 riferimenti locali verificati in entrambi i casi. Anteprima portabile: tre pagine e 89 riferimenti.
- Verificate le sei homepage prodotte (IT/EN nelle due compilazioni e nell’anteprima): otto punti, collegamento iniziale al PDF corrente, scadenza e numeri risolti dai dati condivisi, nessun segnaposto residuo, due link al modulo corretto per lingua e dieci loghi. Controllo delle differenze superato.
- PDF, locandine e loghi non modificati da questo aggiornamento. La verifica visiva nel browser resta soggetta ai limiti già documentati; il controllo HTML non equivale a un’ispezione su desktop e telefono. Nessun commit o push eseguito.

## Logo Google for Education: 12 ottobre

- Attivato il logo allegato dall’utente nel blocco di collaborazione IT/EN, con dicitura introduttiva visibile e testo alternativo. File web identico all’originale, 3298 × 414 px; dimensioni intrinseche dichiarate e presentazione CSS adattabile alla larghezza disponibile.
- Rigenerate entrambe le locandine A3 in PDF, SVG, PNG a 300 dpi e anteprima. Pagine complete ispezionate visivamente: logo affiancato alla dicitura, dieci atenei e spaziatura conservati. Pixel RGBA del logo nel PDF identici all’originale; file PNG incorporato integralmente nell’SVG. I testi differiscono solo per il nome tipografico sostituito dall’immagine nella fascia di collaborazione.
- Compilazione Jekyll: tre pagine e 97 riferimenti locali; anteprima: tre pagine e 91 riferimenti. Verificati logo, dicitura, otto punti del regolamento, dieci atenei e due link di iscrizione nelle quattro homepage IT/EN. PDF e copie scaricabili coincidenti; collegamenti delle locandine al sito conservati.
- Archivi dei sorgenti, dell’anteprima e delle locandine aggiornati. Restano i limiti documentati sulla verifica visiva del sito nel browser; nessun commit, push o deployment effettuato.

## Logo ufficiale HAMU e sito istituzionale: 12 ottobre

- Homepage `https://h-amu.it/` recuperata con HTTP 200. Individuate nel codice della pagina le versioni a colori (708 × 144 px) e bianca (1754 × 346 px); entrambe scaricate e conservate integralmente, con fonti in `LOGHI.md`.
- Nel sito IT/EN: versione bianca in testata e nel titolo, versione a colori nella sezione degli atenei. Due link espliciti al sito istituzionale per lingua, dalla sezione degli atenei e dal footer. Testi alternativi e dimensioni intrinseche presenti; dieci loghi universitari, logo Google, sintesi del regolamento e due link al modulo corretto conservati.
- Compilazioni alla radice e in `/hamu-demo`: tre pagine e 104 riferimenti locali ciascuna. Anteprima portabile: tre pagine e 98 riferimenti. Controllate tutte le sei homepage IT/EN e l’identità degli asset con i file scaricati.
- Locandine IT/EN: logo bianco originale al posto della scritta HAMU nel titolo, anno riposizionato ed elemento decorativo spostato per evitare interferenze. Entrambe le pagine complete renderizzate e ispezionate. Pixel RGBA del logo preservati nel PDF e file originale incorporato nell’SVG; due collegamenti al sito della Challenge per PDF, PNG 3508 × 4961 a 300 dpi e copie scaricabili coincidenti.
- Archivi aggiornati. Verifica visiva del sito nel browser ancora soggetta ai limiti già documentati; nessun commit, push o deployment eseguito.

## Informativa privacy e revisione pubblica — 13 ottobre

- Creata la pagina italiana `/informativa-privacy/` con titolo, descrizione, URL canonico e testo fornito dall’utente. Controllati nel risultato HTML titolare e indirizzo, contatti del RPD/DPO, base giuridica, conservazione di tre mesi, diritti e collegamento UniAQ completo dei parametri. L’informativa compare nelle iscrizioni, nei documenti e nel footer; la homepage inglese specifica che il testo è in italiano.
- Rimossi dalla parte pubblica avvisi di anteprima, etichette di bozza/revisione, note editoriali interne e segnaposto. `robots.txt` consente l’indicizzazione; la sitemap include le due homepage e l’informativa. Soltanto la pagina 404 mantiene `noindex`. La pagina privacy non dichiara una traduzione inesistente nei metadati alternativi.
- Compilazioni alla radice e con prefisso `/hamu-demo`: quattro pagine HTML e 125 riferimenti locali verificati per ciascuna. Esportazione portabile ricreata in una cartella pulita: quattro pagine e 117 riferimenti; la versione precedente è conservata nella cartella di lavoro. Nessun DOCX, file con «bozza» nel nome o cartella `_internal` presente negli output pubblici.
- Confermati nelle sei homepage compilate: due pulsanti verso il modulo corretto, tre link alla nuova informativa, otto punti di sintesi del regolamento, dieci loghi universitari, tre download e soltanto la sede effettivamente confermata. Non sono stati attribuiti nuovi orari, nuove sedi o approvazioni.
- Verificata l’identità dei byte con la versione precedentemente registrata per tutti i sette documenti: quattro archiviati nei sorgenti, due PDF delle locandine rinominati e il regolamento unificato corrente. Nessuna modifica ai contenuti dei PDF e dei DOCX.
- Controllo delle differenze superato; pacchetti dei sorgenti e dell’anteprima aggiornati. La verifica del sito è strutturale, senza nuova ispezione visiva nel browser per i limiti già documentati. Il documento esterno UniAQ non è stato verificabile tramite web (403); il suo URL è conservato come fornito. Nessun commit, push, deployment o modifica al modulo Google eseguiti.

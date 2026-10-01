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
- QR rimosso come richiesto e sostituito dal link scritto al modulo. Nel PDF e nell’SVG è verificata la destinazione cliccabile `https://forms.gle/fAHHkY52ppsiemvu5`. Il sito della Challenge resta nel piè di pagina. Nuovo rendering ispezionato; colori, dati e dieci loghi conservati.
- Copia PDF aggiornata nei download; nuova compilazione alla radice e anteprima portabile controllate con 83 riferimenti locali per ciascuna. Verificata identità delle copie della locandina in materiali, sorgenti, compilazione e anteprima. Gli archivi di consegna sono stati rigenerati.

## Limiti della verifica

Il workflow GitHub Actions è incluso; non è stato eseguito un push o un deployment remoto durante questo aggiornamento. Le gem native sono state eseguite su macOS. Il lockfile include Ruby, Linux x86_64 e macOS ARM64; non è stata eseguita una compilazione Linux in questa sessione.

La verifica visiva del layout e delle interazioni nel browser resta da completare: il controllo di sicurezza aveva rifiutato l’apertura dell’URL `file://` dell’anteprima. Non sono stati utilizzati aggiramenti. I controlli della struttura HTML e degli asset non equivalgono a una verifica visiva o a un audit di accessibilità.

L’anteprima esportata si apre dal proprio computer tramite `hamu-anteprima/index.html`, conservando tutte le sottocartelle. La verifica dei collegamenti locali non costituisce un monitoraggio della disponibilità dei siti esterni.


La locandina è stata aggiornata su richiesta dell’utente: «Google» nel titolo passa a 76 punti, in lime; in fondo compare «Locandina generata con l’ausilio di OpenAI Codex.». PDF, PNG e SVG rigenerati; pagina renderizzata e ispezionata, link di iscrizione verificato, dieci loghi conservati.

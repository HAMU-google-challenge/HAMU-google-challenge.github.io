# Google Challenge HAMU 2026

Sito Jekyll bilingue, in italiano e inglese, predisposto per GitHub Pages. Tema originale per un evento universitario: blu profondo, verde petrolio, accenti lime, calendario in evidenza, masterclass Gemini Academy, loghi dei dieci Atenei, documenti scaricabili e FAQ. Nessun tema remoto, font esterno, servizio di analytics o plugin Jekyll aggiuntivo.

I contenuti sono aggiornati anche al file «Agenda e Note.md» fornito dall’utente, in particolare al resoconto del 14 settembre. La riunione del 24 settembre è ancora un’agenda futura: non è trattata come approvazione già avvenuta. Le provenienze e le scelte editoriali sono in `FONTI.md`; l’inventario dei loghi è in `LOGHI.md`.

I contenuti sono allineati al PDF «Regolamento Finale Google Challenge HAMU 2.pdf» ricevuto il 21 settembre 2026. Il PDF italiano, incluso senza modifiche, è indicato come «In approvazione» perché la mail di accompagnamento richiede ancora il consenso degli Atenei e segnala la verifica del DPO. Copie modificabili, traduzione inglese, avviso e locandina restano bozze. La realizzazione tecnica del sito non costituisce approvazione del regolamento o del branding.

## Pubblicazione su GitHub Pages

Il repository già configurato nella cartella di lavoro è `HAMU-google-challenge/HAMU-google-challenge.github.io`. Il progetto funziona anche in un diverso repository, compresi i project site pubblicati in una sottocartella.

1. Mantieni i contenuti di questa cartella nella radice del repository, inclusa `.github/workflows/pages.yml`. Se parti dallo ZIP, estrailo: non caricare lo ZIP stesso come sito.
2. In GitHub apri **Settings → Pages → Build and deployment → Source → GitHub Actions**.
3. Registra le modifiche e inviale al ramo predefinito `main` o `master`. Il workflow compila, controlla i collegamenti e pubblica il sito. È possibile avviarlo anche da **Actions → Build and deploy Jekyll to GitHub Pages → Run workflow**. Su pull request esegue i controlli senza pubblicare.
4. Attendi il completamento del workflow e apri l’indirizzo mostrato nel deployment `github-pages`.

Non serve configurare manualmente `url` e `baseurl` per GitHub Actions: vengono ricavati da GitHub Pages durante la compilazione, anche quando si usa un dominio personalizzato. Per rami con nomi diversi da `main` e `master`, aggiorna i due elenchi `branches` nel workflow.

La cartella è predisposta per la pubblicazione; non è stato eseguito un push o un deployment durante questo lavoro. Riferimento: [workflow personalizzati di GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Modificare i contenuti

| File | Contenuto |
|---|---|
| `_data/event.yml` | Date, iscrizioni, sedi, contatti, Atenei, punteggi e documenti comuni alle due lingue; anche le sedi candidate non esposte nella pagina |
| `_data/i18n.yml` | Testi italiani e inglesi, FAQ, etichette e mesi |
| `_layouts/home.html` | Struttura delle due homepage |
| `_layouts/default.html` | Navigazione, metadati e footer |
| `assets/css/main.css` | Colori, tipografia e adattamento a schermi piccoli |
| `assets/js/main.js` | Menu mobile; il contenuto rimane accessibile anche senza JavaScript |
| `assets/documents/` | File scaricabili |
| `assets/images/` | Favicon e dieci loghi degli Atenei in `universities/` |

Le homepage sono `/` e `/en/`. Il sito include anche una pagina 404, `robots.txt` e una sitemap. Per cambiare colori, modifica le variabili all’inizio del CSS.

### Stato dell’anteprima

In `_data/event.yml`, `preview: true` mostra il messaggio di anteprima e richiede ai motori di ricerca di non indicizzare il sito. **Non è un controllo di accesso:** se pubblicato, il sito è comunque consultabile e i documenti sono scaricabili.

I documenti usano `status: review` per il PDF in approvazione, `draft` per le bozze e `approved` per i definitivi. Quando i materiali sono consolidati, sostituisci i documenti, aggiorna i relativi percorsi e imposta `status: approved` per ciascun documento definitivo; poi imposta `preview: false`. Questo rimuove la fascia di anteprima, abilita l’indicizzazione e popola la sitemap. Aggiorna anche `updated` alla data dell’aggiornamento editoriale. Adegua anche i testi delle FAQ sulla privacy all’esito della verifica del DPO.

### Iscrizioni

`registration.state` ammette tre valori:

- `planned`: candidature in preparazione, con rimando ai documenti.
- `open`: mostra il pulsante di candidatura solo se sono presenti sia `registration.url` sia `registration.privacy_url`.
- `closed`: mostra la chiusura delle candidature e un rimando al programma.

`registration.url` deve essere l’URL completo HTTPS del modulo approvato. `privacy_url` può essere un URL HTTPS o un percorso locale, per esempio `/assets/documents/informativa-privacy.pdf`. La chiusura è editoriale: allo scadere del termine imposta `state: closed` e chiudi anche il modulo presso il servizio che lo ospita.

L’Agenda contiene un link a una bozza del modulo: è registrato in `FONTI.md`, escluso dal sito compilato. Non è stato attivato come modulo definitivo.

Il sito non raccoglie candidature e non contiene un backend. Il modulo esterno gestisce l’invio dei dati.

### Dati ancora da completare

Restano da consolidare, secondo i materiali disponibili: regolamento e avviso definitivi, ora della scadenza, modulo e informativa privacy, sedi regionali, giorno della finale, recapito organizzativo e toolkit Google for Education. Questi campi sono già predisposti; il sito presenta messaggi espliciti dove manca un dato.

Le disponibilità di Politecnica delle Marche, Perugia, Camerino e Chieti-Pescara sono registrate sotto `venues[].candidates`, con capienze e dotazioni comunicate dall’utente. Sono opzioni organizzative: le pagine mostrano solo `venues[].location`, ancora vuoto. Dopo l’assegnazione del Comitato, compila quest’ultimo campo con sede e indirizzo confermati. Se il repository è pubblico, anche questi dati nei sorgenti sono consultabili, pur non comparendo nelle pagine compilate.

Le date inserite sono il 3 novembre 2026 per le candidature, il 6 novembre per team/temi/sedi e il 13 novembre per la preliminare. Per la finale è indicata L’Aquila nella settimana del 23 novembre come finestra prevista, con giorno da confermare. La masterclass è indicata con durata di circa 2,5–3 ore e orario indicativo 09:30–12:30; attestato previsto per tutti, CFU non automatici e lingua da comunicare. I testi relativi al programma e alle FAQ vanno aggiornati in entrambe le lingue quando cambiano le decisioni organizzative.

I campi `branding.hamu_logo` e `branding.google_education_lockup` accettano percorsi locali. Finché sono vuoti, vengono utilizzate scritte tipografiche: non sono inclusi loghi Google ricostruiti.

## Avvio locale

Servono Ruby 3.1 o successivo, Bundler compatibile con il lockfile e gli strumenti di compilazione delle gem native. La compilazione locale è stata verificata con Ruby 3.1.3 e Jekyll 3.10.0; GitHub Actions usa l’ambiente Jekyll fornito dall’azione ufficiale di GitHub Pages.

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Apri `http://127.0.0.1:4000`. Per la sola compilazione e il controllo dei collegamenti:

```sh
bundle exec jekyll build
python3 scripts/check_site.py _site
```

Python 3.9 o successivo è sufficiente; gli script non richiedono pacchetti aggiuntivi. Il controllo verifica risorse e ancore locali, una sola intestazione principale per pagina, lingua, ID duplicati, Liquid non elaborato e assenza di file di sviluppo nell’output pubblico.

Per verificare una pubblicazione in sottocartella:

```sh
bundle exec jekyll build --baseurl /test-repository
python3 scripts/check_site.py _site --baseurl /test-repository
```

Per generare un’anteprima da aprire direttamente dal filesystem, senza Ruby in esecuzione:

```sh
bundle exec jekyll build --baseurl ""
python3 scripts/export_preview.py _site ../hamu-anteprima
```

Apri `../hamu-anteprima/index.html`. L’esportazione rende relativi i collegamenti locali; conserva tutta la cartella per usare il selettore di lingua, gli stili e i download. Serve alla revisione offline: per GitHub Pages usa i sorgenti Jekyll.

## Verifiche della consegna

I controlli eseguiti e i loro limiti sono riportati in `VERIFICHE.md`. Non includono un deployment sul repository remoto.

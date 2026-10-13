# Google Challenge HAMU 2026

Sito Jekyll in italiano e inglese per GitHub Pages, con grafica coordinata alle locandine. Usa Rubik Regular e Bold locali, i dieci loghi degli atenei, il logo ufficiale HAMU e il logo Google for Education fornito dall’organizzazione. Non usa font esterni, analytics o plugin Jekyll aggiuntivi.

## Stato al 13 ottobre 2026

Il sito è in modalità pubblica (`preview: false`), con indicizzazione abilitata. Sono stati rimossi gli avvisi di anteprima, le etichette di revisione e i commenti di coordinamento interno. Le informazioni operative ancora da comunicare non vengono presentate come confermate.

Le iscrizioni sono aperte con il modulo indicato dall’utente il 10 ottobre: <https://forms.gle/m8npVRMSNzRwhz2x6>. L’informativa fornita il 13 ottobre è in `informativa-privacy.md` e sarà raggiungibile dopo la pubblicazione a **<https://hamu.univaq.it/informativa-privacy/>**. Questo è l’indirizzo da inserire nel modulo Google. Il testo è in italiano anche quando raggiunto dalla homepage inglese; il collegamento lo specifica. Il sito non raccoglie candidature: i dati vengono inviati tramite il modulo esterno.

Il regolamento scaricabile resta il PDF unificato ricevuto il 1 ottobre (14 pagine), conservato senza modifiche. Le locandine sono disponibili nei file `assets/documents/locandina-hamu-it.pdf` e `assets/documents/locandina-hamu-en.pdf`. I contenuti dei PDF non sono stati modificati in questo aggiornamento.

Le copie Word di lavoro, la traduzione inglese, l’avviso con un campo da compilare e il precedente regolamento PDF sono conservati in `_internal/documents/`, esclusi dal sito compilato. La cartella rimane consultabile nel repository se pubblico: non è un archivio riservato. Fonti, decisioni e questioni ancora da coordinare sono in `FONTI.md`; loghi in `LOGHI.md`; controlli in `VERIFICHE.md`. La rimozione delle etichette editoriali non attesta un’approvazione dei documenti né risolve le divergenze organizzative annotate nelle fonti.

## Pubblicazione su GitHub Pages

Il repository è `HAMU-google-challenge/HAMU-google-challenge.github.io`, con dominio `hamu.univaq.it` nel file `CNAME`.

1. Mantieni i contenuti della cartella nella radice del repository, inclusa `.github/workflows/pages.yml`. Se usi lo ZIP, estrailo: non caricare lo ZIP come sito.
2. In **Settings → Pages → Build and deployment → Source** seleziona **GitHub Actions**.
3. Esegui commit e push sul ramo predefinito `main` o `master`, includendo aggiunte, modifiche e rimozioni. Il workflow compila, controlla i collegamenti e pubblica. Puoi anche avviarlo manualmente dalla scheda **Actions**; sulle pull request esegue solo i controlli.
4. Dopo il completamento del deployment, verifica la homepage e `/informativa-privacy/`, quindi inserisci l’URL dell’informativa nel modulo Google.

`_config.yml` usa il dominio pubblico come valore predefinito. Il workflow ricava `url` e `baseurl` dalla configurazione GitHub Pages, supportando anche una pubblicazione in sottocartella. Non sono stati eseguiti commit, push o deployment durante questo aggiornamento.

## Manutenzione

| File | Contenuto |
|---|---|
| `_data/event.yml` | Date, iscrizioni, sedi, contatti, atenei, punteggi, documenti e loghi |
| `_data/i18n.yml` | Testi italiani e inglesi, FAQ, etichette e mesi |
| `informativa-privacy.md` | Testo dell’informativa e indirizzo permanente `/informativa-privacy/` |
| `_layouts/home.html` | Struttura delle homepage `/` e `/en/` |
| `_layouts/default.html` | Navigazione, metadati e footer |
| `_layouts/document.html` | Impaginazione delle pagine di documento |
| `assets/css/main.css` | Colori, tipografia e adattamento agli schermi |
| `assets/js/main.js` | Menu mobile; contenuti accessibili anche senza JavaScript |
| `assets/documents/` | PDF pubblici scaricabili |
| `assets/images/` | Loghi ufficiali e immagini locali |
| `_internal/` | Materiali di lavoro esclusi dal sito compilato |

Il sito include anche la pagina 404, `robots.txt` e una sitemap con homepage IT/EN e informativa. La pagina 404 mantiene `noindex`; le pagine pubbliche sono indicizzabili.

### Iscrizioni e informazioni operative

`registration.state` può essere `planned`, `open` o `closed`. Con `open` e un `registration.url` valorizzato, i pulsanti di iscrizione sono visibili in entrambe le lingue. `privacy_url` punta alla pagina locale dell’informativa, collegata dalle iscrizioni, dai documenti e dal footer. La chiusura è editoriale: alla scadenza imposta `state: closed` e chiudi il modulo presso il servizio che lo ospita.

Le date pubblicate sono il 3 novembre 2026 per le candidature, il 6 novembre per la comunicazione della sede e il 13 novembre per formazione e fase iniziale. La finale è all’Aquila entro fine 2026, con data da comunicare. Non vengono mostrati un orario di scadenza o una data precisa della finale non confermati. La formazione si svolge al mattino, la Challenge al pomeriggio.

La sezione atenei espone come sedi soltanto quelle con `status: confirmed`. Le sedi preferite e candidate restano nei dati di lavoro. La disponibilità di un ateneo non conferma una specifica aula. Aggiorna sedi, orari, contatti e testi nelle due lingue quando arrivano decisioni dell’organizzazione; non inventare valori per riempire campi vuoti.

Alla verifica del modulo del 10 ottobre era presente un segnaposto per il collegamento al regolamento. Il modulo non viene modificato da questo progetto: l’organizzazione deve completarne i collegamenti, inclusa la nuova informativa dopo la pubblicazione.

### Aggiornamenti dalle riunioni

Registra fonti e date in `FONTI.md`, distinguendo decisioni e proposte. Aggiorna dati comuni, calendario e FAQ nelle due lingue. Conserva nell’archivio editoriale le divergenze ancora da risolvere: i testi pubblici devono essere chiari per i partecipanti e non presentare ipotesi come decisioni. Aggiorna `event.updated`, compila, verifica i collegamenti e rigenera l’anteprima. Non è configurata alcuna importazione automatica delle note.

### Verifica locale

Servono Ruby 3.1 o successivo e Bundler compatibile con il lockfile. La compilazione locale usa Jekyll 3.10.0.

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

Apri `http://127.0.0.1:4000`. Per compilare e verificare i collegamenti:

```sh
bundle exec jekyll build
python3 scripts/check_site.py _site
```

Per una pubblicazione in sottocartella:

```sh
bundle exec jekyll build --baseurl /test-repository
python3 scripts/check_site.py _site --baseurl /test-repository
```

Per un’anteprima portabile, usa una cartella di destinazione vuota in modo da non conservare vecchi download rimossi:

```sh
bundle exec jekyll build --baseurl ""
python3 scripts/export_preview.py _site ../hamu-anteprima
```

Apri `../hamu-anteprima/index.html` oppure `../hamu-anteprima/informativa-privacy/index.html`. L’esportazione converte i collegamenti locali e incorpora i font nel CSS; conserva tutta la cartella. Per la pubblicazione usa i sorgenti Jekyll, non l’anteprima offline.

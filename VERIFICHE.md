# Verifiche del sito HAMU

Consegna verificata il 21 settembre 2026.

| Controllo | Esito |
|---|---|
| Compilazione Jekyll 3.10.0 con Ruby 3.1.3 | Superata |
| Output alla radice del dominio | 3 pagine HTML e 85 riferimenti locali verificati |
| Output in sottocartella `/hamu-demo` | 3 pagine HTML e 85 riferimenti locali verificati |
| URL ricavati dai metadati di Pages | Verificati su una copia locale tramite lo script del workflow |
| Download, ancore e collegamenti IT/EN | Tutti i riferimenti locali risolti |
| Stato iscrizioni aperte senza privacy | Nessun pulsante di candidatura |
| Stato iscrizioni aperte con modulo e privacy | Pulsante di candidatura presente in entrambe le lingue |
| Stato iscrizioni chiuse | Pulsante di candidatura assente |
| Anteprima e indicizzazione | `noindex` e blocco robots presenti in anteprima; sitemap vuota |
| Modalità definitiva | `noindex` rimosso dalle homepage, sitemap con due URL e robots aggiornato |
| Output pubblico | File di sviluppo e istruzioni esclusi |
| JavaScript | Controllo sintattico con Node superato |
| Dati comuni | Dieci Atenei e griglia di valutazione da 100 punti verificati |
| Anteprima portabile | 3 pagine HTML e 85 riferimenti locali verificati dopo la conversione |
| Lockfile delle dipendenze | Include piattaforme Ruby, Linux x86_64 e macOS ARM64 |

Le varianti per iscrizioni e indicizzazione sono state compilate su copie temporanee. La consegna mantiene `preview: true` e le iscrizioni in preparazione; il PDF italiano è indicato come in approvazione e gli altri materiali restano bozze.

Il workflow GitHub Actions è incluso, ma non è stato eseguito un deployment remoto. Le gem native sono state eseguite su macOS; il lockfile è predisposto anche per Linux, senza una compilazione Linux verificata in questa sessione.

La verifica visiva e delle interazioni nel browser non è stata completata: il controllo di sicurezza del browser ha rifiutato l’apertura dell’URL `file://` dell’anteprima. Non sono stati utilizzati aggiramenti. Il CSS include layout per desktop, tablet e mobile; il menu e gli stati di focus sono implementati, ma questo non equivale a una verifica visiva o a un audit di accessibilità.

L’anteprima esportata si può aprire dal proprio computer tramite `hamu-anteprima/index.html`, conservando tutte le sottocartelle.

## Aggiornamento sul PDF ricevuto

Il 21 settembre sono stati verificati anche il download del PDF italiano ricevuto, la distinzione tra documenti in approvazione e bozze e l’assenza delle capienze delle sedi candidate dalle pagine compilate. Le dieci FAQ sono presenti in entrambe le lingue. Il PDF incluso coincide byte per byte con l’allegato dell’utente.

## Aggiornamento dall’Agenda e loghi

- Sezione Formazione presente nelle due lingue, con tre argomenti, durata e orario indicativi, attestato previsto e precisazione sui CFU.
- Dieci schede degli Atenei, ciascuna con logo locale, nome completo e collegamento istituzionale; raggruppamento regionale 4 + 4 + 2.
- Tutti i dieci file immagine decodificati correttamente; dimensioni HTML coerenti con i file. Ispezione visiva dei loghi su fondo bianco completata, senza modificare gli originali.
- Immagini e collegamenti controllati in tutte e cinque le configurazioni compilate, oltre all’anteprima portabile. La verifica dei riferimenti riguarda risorse locali; non è un monitoraggio della disponibilità futura dei siti esterni.
- Bozza del modulo non collegata dal pulsante di candidatura; capienze candidate e agenda del 24 settembre non presentate come conferme.
- `LOGHI.md` e `FONTI.md` esclusi dalle pagine compilate e dall’anteprima, conservati nei sorgenti per la manutenzione editoriale.

L’ispezione dei file grafici non sostituisce la verifica visiva del layout nel browser, che resta da completare per il motivo indicato sopra.

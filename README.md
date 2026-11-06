# onion Consulting — zweisprachige Website

Statische Website ohne Laufzeit-Abhängigkeiten. Der Entwurf liegt auf `redesign/de-en-2026-11`. Die ausdrückliche Veröffentlichungsfreigabe wurde am 6. November 2026 erteilt.

## Seiten und Pflege

- Deutsch: `/de/`, `/de/impressum.html`, `/de/datenschutz.html`
- Englisch: `/en/`, `/en/legal-notice.html`, `/en/privacy.html`
- Bestehende URLs `/`, `/impressum.html` und `/datenschutz.html` bleiben als deutsche Fassungen erhalten; Canonical verweist auf die jeweilige `/de/`-Seite.
- Sprachneutrale Abschnittszuordnung über die bestehenden IDs `leistungen`, `ansatz`, `kontakt`; beim Sprachwechsel bleibt der Abschnitt erhalten.
- `content/home.json`: gemeinsame Struktur, deutsche und englische Inhalte.
- `content/legal.*.html`, `content/privacy.*.html`: Rechtstexte. Die deutschen Ausgangsangaben wurden übernommen; die dokumentierte Präzisierung des Widerspruchsrechts und der Textstand November 2026 wurden zur Veröffentlichung eingearbeitet. Die englischen Texte sind Übersetzungen desselben Bestands, keine rechtliche Aktualitätsbestätigung.
- `assets/styles.css` und `assets/main.js`: Gestaltung und kleine lokale Interaktionen.
- `scripts/build.py`: erzeugt die neun ausgelieferten HTML-Seiten und die Sitemap. Die Ergebnisse werden mit versioniert. Kein Build auf dem Hosting erforderlich.
- `docs/REVIEW.md`: Bestandsaufnahme, Prüfungen und offene Freigabepunkte.

Änderungen an Texten in `content/` vornehmen und mit Python ab Version 3.10 ausführen:

```text
python scripts/build.py
python scripts/check.py
node --check assets/main.js
```

Node ist ausschließlich für diese optionale Syntaxprüfung nötig. `check.py` prüft unter anderem interne Links, Sprungmarken, SEO-Metadaten und die deutschen Rechtstexte einschließlich der dokumentierten Korrekturen und die unveränderten Originalgrafiken gegenüber Ausgangscommit `7defe4f`.

Lokale Vorschau, ohne Veröffentlichung:

```text
python -m http.server 8765 --bind 127.0.0.1
```

Dann `http://127.0.0.1:8765/de/` öffnen. Die Seiten funktionieren auch direkt aus dem Dateisystem; lediglich die Fehlerseite mit ihren domainbezogenen Pfaden benötigt einen Webserver.

## Veröffentlichung nach Freigabe

Domain (`CNAME`) und Originalgrafiken bleiben unverändert. Es wurden keine Deployment-Workflows ergänzt und keine Hosting-Einstellungen geändert. Vor einem späteren Merge müssen die tatsächliche GitHub-Pages-Quelle und ein etwaiger externer Deployment-Dienst geprüft werden. Der Branch darf nicht ohne Freigabe als Veröffentlichungsquelle eingestellt werden.

Die fachlichen Inhalte sind vollständig zweisprachig. Die rechtlichen Prüfpunkte aus `docs/REVIEW.md` müssen vor der Veröffentlichung geklärt und in beiden Fassungen nachgeführt werden. Insbesondere ist die derzeitige Datenschutzerklärung kein abschließend geprüfter neuer Rechtstext.

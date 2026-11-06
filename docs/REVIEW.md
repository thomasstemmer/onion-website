# Bestandsaufnahme und Prüfung — 6. November 2026

Der deutsch/englische Entwurf ist zur Gestaltungskontrolle vorbereitet. Eine rechtliche Veröffentlichungsfreigabe liegt nicht vor. Die produktive Website und der Branch `main` werden nicht verändert.

## Ausgangsbestand

Repository: https://github.com/thomasstemmer/onion-website, Ausgangscommit `7defe4fe5a87fdc6f80af053a440514ae14d0402`. Die Datei `CNAME` enthält `www.onion.de`. Das bestätigt die Zuordnung zur beauftragten Website. Der Nutzer hat den Repository-Link zusätzlich bestätigt.

Der Bestand enthält eine deutsche Startseite, Impressum, Datenschutzerklärung, CSS, ein kleines Menüskript, Favicon und drei PNG-Grafiken. Kein Framework, keine Paketabhängigkeiten, kein eigener Deployment-Workflow im geprüften Commit. Die tatsächliche aktuelle Hosting-Konfiguration wurde nicht administrativ eingesehen. GitHub Pages wird in der vorhandenen Datenschutzerklärung als Hosting-Dienst bezeichnet.

Originale Farbangaben im CSS: Dunkelblau `#0b1020`/`#111a33`, Grün `#2F6B57`, Mint `#8ddfcb`/`#48bba5`. Die Originalgrafiken verbinden Türkis mit Dunkelblau. Der Entwurf leitet daraus `#102638`, `#087f80`, `#bce8dd` und helle Hintergründe ab; diese Werte sind eine neue Gestaltungspalette, keine behaupteten verbindlichen Corporate-Design-Vorgaben.

Verwendet wird unverändert `assets/onion-logo-2026.png` (126.061 Bytes), das freigestellte Bildzeichen. Dazu kommt ein typografischer Namenszug. Die originale Wort-Bild-Marke `onion-2026.png` (1.074.395 Bytes) bleibt erhalten und ist als Open-Graph-Bild referenziert. `onion-2026-60px.png` ist trotz Dateinamen 973.980 Bytes groß und wird nicht für normale Seitenaufrufe eingebunden. Alle Originalgrafiken und das Favicon bleiben bytegleich erhalten.

## Umsetzung

Helle Gestaltung, zurückhaltende türkise Akzente, dunkelblauer Abschnitt zur Arbeitsweise, größere Abstände, gut lesbare Leistungsblöcke, einheitlicher Kopf- und Fußbereich auch auf den Rechtstextseiten. Keine neuen Leistungsversprechen, Referenzen, Kunden, Qualifikationen oder Zertifizierungen erfunden.

Deutsch und Englisch erhalten jeweils drei eigenständige HTML-Seiten. Sprachwechsel und Inhalt funktionieren grundsätzlich auch ohne JavaScript; das mobile Klappmenü und die Übernahme der aktuellen Sprungmarke werden mit lokalem JavaScript ergänzt. Ohne JavaScript bleibt die mobile Navigation sichtbar. Keine automatische Spracherkennung, keine gespeicherte Sprachpräferenz.

SEO: sprachbezogene Titel, Beschreibungen, HTML-Sprachkennzeichnung, wechselseitige hreflang-Verweise einschließlich x-default, Canonical, Open-Graph-Metadaten, robots.txt, Sitemap der sechs kanonischen Seiten und zweisprachige Fehlerseite. Die bisherigen drei URLs bleiben erreichbar; Canonical verweist auf die deutsche Sprachversion. Es wurden bewusst keine neuen Weiterleitungen oder Hosting-Regeln eingerichtet. Die tatsächliche Auslieferung der Fehlerseite und der HTTPS-/Security-Header ist erst am späteren Zielhosting überprüfbar.

## Datenschutz: technische Feststellungen

Im geprüften eigenen HTML/CSS/JavaScript keine Analysewerkzeuge, Pixel, Webfonts von Drittservern, eingebetteten Videos, Karten, Kontaktformulare, Cookies oder Browser-Speicherzugriffe. Bilder, CSS, Skript und Favicon werden von derselben Website geladen. Ein externer GitHub-Datenschutzlink wird erst bei Auswahl aufgerufen. Der E-Mail-Link öffnet das E-Mail-Programm; die Website sendet die Anfrage nicht selbst.

Diese Feststellungen betreffen den Quellcode des Entwurfs. Sie belegen weder die vollständige Verarbeitung des Hosting-Anbieters noch das Verhalten einer später vorgeschalteten Infrastruktur. Insbesondere protokolliert GitHub Pages laut eigener Dokumentation IP-Adressen für Sicherheitszwecke. Eine Website ohne eingebundene Tracking-Werkzeuge ist daher nicht automatisch eine Website ohne personenbezogene Verarbeitung. Quelle: [GitHub Pages – Data collection](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection).

## Rechtstexte: konkrete Punkte vor Veröffentlichung

Die deutschen Rechtstextinhalte wurden bewusst vollständig aus dem Bestand übernommen. Namen, Anschrift, Kontaktadresse, Umsatzsteuer-ID und der Stand Juni 2026 wurden nicht stillschweigend geändert. Englisch übersetzt denselben Bestand. Das Aktualitätsdatum ist damit ein übernommener Textstand, kein Prüfvermerk für November 2026.

1. Hosting und Übermittlungen: Ziffer 2 nennt nur pauschal die jeweils anwendbaren Garantien. Zu bestätigen sind der tatsächlich eingesetzte Dienst und Vertragspartner, dessen Rolle sowie die einschlägige Übermittlungsgrundlage und deren Nachweismöglichkeit. Die GitHub-Erklärung nennt verschiedene Übermittlungsmechanismen; daraus lässt sich ohne Prüfung des konkreten Verhältnisses keine pauschale Rechtsgrundlage für onion ableiten. Die Informationspflichten erfordern eine konkrete Zuordnung. Quellen: [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement#international-data-transfers), [DSK-Kurzpapier 10](https://www.datenschutzzentrum.de/artikel/1166-Kurzpapier-Nr.-10-Informationspflichten-bei-Dritt-und-Direkterhebung.html).

2. Speicherdauer: Ziffer 6 enthält nur allgemeine Zweck- und Aufbewahrungsformulierungen. Zu klären sind die tatsächliche Behandlung von Hosting-Logs, Anfragen und aufbewahrungspflichtiger Korrespondenz, einschließlich der jeweils einschlägigen Frist oder bestimmbaren Kriterien. Keine pauschale Sechs-, Acht- oder Zehnjahresfrist ohne Dokumentenklassifikation einsetzen. Quelle: [DSK-Kurzpapier 10 zu Art. 13 Abs. 2 DSGVO](https://www.datenschutzzentrum.de/artikel/1166-Kurzpapier-Nr.-10-Informationspflichten-bei-Dritt-und-Direkterhebung.html).

3. Widerspruchsrecht: Ziffer 8 des Bestands gibt die Ausnahmen in Art. 21 Abs. 1 DSGVO nicht präzise wieder. Der gesetzliche Interessenvergleich fehlt; die Oder-Verknüpfung ist missverständlich. Vorschlag für die spätere deutsche Korrektur: „Legen Sie aus Gründen, die sich aus Ihrer besonderen Situation ergeben, Widerspruch ein, verarbeiten wir die betreffenden personenbezogenen Daten nicht mehr, es sei denn, wir können zwingende schutzwürdige Gründe für die Verarbeitung nachweisen, die Ihre Interessen, Rechte und Freiheiten überwiegen, oder die Verarbeitung dient der Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen.“ Die englische Fassung ist entsprechend anzupassen. Dieser Vorschlag ist dokumentiert und noch nicht in den übernommenen Rechtstext eingearbeitet. Quelle: [BfDI, amtlicher DSGVO-Abdruck, Art. 21](https://www.bfdi.bund.de/SharedDocs/Downloads/DE/Broschueren/INFO1.pdf?__blob=publicationFile&v=27).

4. Impressum: Nur eine E-Mail-Adresse ist als Kommunikationsweg genannt. Zu bestätigen ist, welche Angaben im konkreten Betrieb eine schnelle elektronische Kontaktaufnahme und unmittelbare Kommunikation ermöglichen. § 5 Abs. 1 Nr. 2 DDG verlangt dies einschließlich einer E-Mail-Adresse; eine Telefonnummer wird hier nicht ohne weitere Prüfung als ausnahmslos verpflichtend dargestellt. Register-, berufsrechtliche und sonstige Anbieterpflichten hängen von den tatsächlichen Verhältnissen ab. Es wurden keine solchen Angaben erfunden. Quelle: [§ 5 DDG](https://www.gesetze-im-internet.de/ddg/__5.html).

5. Tatsächliche Praxis: Aussagen in Ziffer 10 zur laufenden Überprüfung organisatorischer und technischer Maßnahmen sind Angaben des bisherigen Texts; ihre Umsetzung ist nicht nachgewiesen. E-Mail-Dienstleister, Auftragsverarbeitung und einschlägige betriebliche Verfahren sind nicht allein aus dem Website-Code feststellbar. Die vorhandene Besucheranschrift des BayLDA stimmt mit dessen aktueller Kontaktseite überein; diese unterscheidet zusätzlich eine Postanschrift. Quelle: [BayLDA – Kontakt](https://www.lda.bayern.de/de/kontakt.html).

Eine knappe Beschreibung der tatsächlich eingesetzten lokalen Website-Funktionen kann nach Bestätigung des Zielhostings in beiden Rechtstexten ergänzt werden. Ein Einwilligungsbanner wurde nicht eingebaut, da der eigene Entwurf keine einwilligungspflichtigen Tracking- oder Speicherfunktionen vorsieht. Eine abschließende Aussage zum gesamten Zielbetrieb folgt daraus nicht.

## Prüfungen und Grenzen

- Python-Generierung erfolgreich; zehn HTML-Seiten einschließlich 404-Seite geprüft.
- Interne Links und Sprungmarken, jeweils eine Hauptüberschrift, Sprachkennzeichnung, Beschreibungen, Canonical und korrespondierende Sprachverweise geprüft; Sitemap entspricht den sechs kanonischen URLs.
- Deutsche Rechtstexte, Originalgrafiken, Favicon und CNAME automatisiert gegenüber dem Ausgangscommit verglichen: unverändert.
- JavaScript-Syntaxprüfung und Git-Prüfung auf fehlerhafte Leerzeichen erfolgreich.
- Browserprüfung der deutschen und englischen Startseite; Layout bei 320, 390, 768, 1280 und 1440 CSS-Pixeln betrachtet bzw. auf horizontales Überlaufen geprüft. Auf den geprüften Ansichten kein horizontaler Seitenüberlauf.
- Mobiles Menü öffnet und schließt; Abschnittsauswahl schließt es; Escape schließt es und setzt den Fokus auf die Schaltfläche zurück. Wechsel Englisch → Deutsch behält die aktuelle Leistungs-Sprungmarke bei.
- Deutsche/englische Datenschutz- und Impressumsseiten über die Navigation aufgerufen und Sprachpaarung überprüft. Rechtstexte auch bei 320 Pixeln ohne horizontalen Seitenüberlauf geprüft.
- Keine im Browser erfassten Warnungen oder JavaScript-Fehler während der Prüfung.
- Tastaturfokus, Sprunglink, semantische Überschriften, verständliche Linkbeschriftungen und reduzierte Bewegung vorgesehen. Keine vollständige WCAG-/BITV-Prüfung, keine Screenreader-Prüfung, keine Prüfung mit echten iOS-/Android-Geräten, keine Lighthouse-Messung. Keine bestimmte Performance- oder SEO-Punktzahl behauptet.

Eine Freigabe der Gestaltung löst keine Veröffentlichung aus. Dafür ist eine gesonderte ausdrückliche Zustimmung erforderlich. Zuvor sind die rechtlichen Punkte sowie die tatsächliche Hosting-Konfiguration zu klären.

"""Generate the committed static website with Python 3.10+, no dependencies."""
from pathlib import Path
from html import escape
import json
import posixpath
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'content/home.json').read_text(encoding='utf-8'))
DOMAIN = 'https://www.onion.de'
ROUTES = {'de': {'home': 'de/index.html', 'legal': 'de/impressum.html', 'privacy': 'de/datenschutz.html'},
          'en': {'home': 'en/index.html', 'legal': 'en/legal-notice.html', 'privacy': 'en/privacy.html'}}


def url(lang, page):
    path = ROUTES[lang][page]
    return DOMAIN + '/' + (path[:-10] if path.endswith('index.html') else path)


def render(lang, page, path):
    t = DATA[lang]
    rel = lambda dest: posixpath.relpath(dest, posixpath.dirname(path) or '.')
    home = rel(ROUTES[lang]['home'])
    title = t['title'] if page == 'home' else t['privacyTitle' if page == 'privacy' else 'legal'] + ' | onion Consulting'
    description = t['description'] if page == 'home' else (t['privacyIntro'] if page == 'privacy' else ('Anbieterangaben der onion Consulting.' if lang == 'de' else 'Provider information for onion Consulting.'))
    alternate = ''.join(f'<link rel="alternate" hreflang="{l}" href="{url(l, page)}">' for l in DATA)
    nav = ''.join(f'<a href="{home}#{anchor}">{text}</a>' for anchor, text in zip(['leistungen', 'ansatz', 'kontakt'], t['nav']))
    languages = ''.join(f'<a href="{rel(ROUTES[l][page])}" lang="{l}" hreflang="{l}" data-language="{l}" aria-label="{label}"' + (' aria-current="true"' if l == lang else '') + f'>{l.upper()}</a>' for l, label in [('de', 'Deutsch'), ('en', 'English')])
    header = f'''<a class="skip-link" href="#main">{t['skip']}</a>
  <header class="site-header"><div class="nav-wrap">
    <a class="brand" href="{home}" aria-label="onion Consulting · {t['home']}">
      <img src="{rel('assets/onion-logo-2026.png')}" width="52" height="52" alt="" fetchpriority="high">
      <span class="wordmark">onion<span>Consulting</span></span>
    </a>
    <nav class="nav-links" id="nav-links" aria-label="{t['navigation']}">{nav}</nav>
    <div class="nav-tools"><nav class="language-switch" aria-label="{t['language']}">{languages}</nav>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-links">{t['menu']}<span aria-hidden="true"> +</span></button></div>
  </div></header>'''
    footer = f'''<footer class="footer wrap"><a class="footer-brand" href="{home}">onion Consulting</a>
      <p>© <span data-year>2026</span> onion Consulting</p>
      <nav aria-label="{t['legalLabel']}"><a href="{rel(ROUTES[lang]['legal'])}">{t['legal']}</a><a href="{rel(ROUTES[lang]['privacy'])}">{t['privacy']}</a></nav>
    </footer>'''
    if page == 'home':
        services = ''.join(f'<article class="service"><span class="service-number" aria-hidden="true">0{i}</span><div><h3>{heading}</h3><p>{text}</p></div></article>' for i, (heading, text) in enumerate(t['services'], 1))
        steps = ''.join(f'<li><span class="step-number" aria-hidden="true">0{i}</span><div><h3>{heading}</h3><p>{text}</p></div></li>' for i, (heading, text) in enumerate(t['steps'], 1))
        focus = ''.join(f'<li>{item}</li>' for item in t['focusItems'])
        body = f'''<main id="main" tabindex="-1">
      <section class="hero wrap" aria-labelledby="hero-heading"><div class="hero-content">
        <p class="eyebrow">{t['eyebrow']}</p><h1 id="hero-heading">{t['headline']}</h1>
        <p class="lead">{t['lead']}</p><div class="hero-actions"><a class="button primary" href="mailto:mailbox@onion.de">{t['contactAction']} <span aria-hidden="true">↗</span></a>
        <a class="text-link" href="#leistungen">{t['servicesAction']} <span aria-hidden="true">↓</span></a></div></div>
        <aside class="focus-panel" aria-labelledby="focus-title"><div class="focus-art" aria-hidden="true"><img src="{rel('assets/onion-logo-2026.png')}" width="240" height="240" alt=""></div>
        <div class="focus-copy"><p class="eyebrow">{t['focus']}</p><h2 id="focus-title">{t['focusTitle']}</h2><ul>{focus}</ul></div></aside>
      </section>
      <section class="services-section" id="leistungen" aria-labelledby="services-title"><div class="wrap section-inner"><div class="section-heading"><p class="eyebrow">01 / {t['servicesLabel']}</p><h2 id="services-title">{t['servicesTitle']}</h2></div><div class="services-grid">{services}</div></div></section>
      <section class="approach-section" id="ansatz" aria-labelledby="approach-title"><div class="wrap section-inner approach-grid"><div class="section-heading"><p class="eyebrow">02 / {t['approachLabel']}</p><h2 id="approach-title">{t['approachTitle']}</h2></div><ol class="steps">{steps}</ol></div></section>
      <section class="contact-section wrap" id="kontakt" aria-labelledby="contact-title"><div><p class="eyebrow">03 / {t['contactLabel']}</p><h2 id="contact-title">{t['contactTitle']}</h2><p>{t['contactText']}</p></div><a class="contact-email" href="mailto:mailbox@onion.de?subject={quote(t['subject'])}"><span>{t['emailLabel']} <span aria-hidden="true">↗</span></span>mailbox@onion.de</a></section>
    </main>'''
    else:
        legal = (ROOT / f'content/{page}.{lang}.html').read_text(encoding='utf-8')
        heading = t['privacyTitle'] if page == 'privacy' else t['legal']
        intro = f'<p class="lead">{t["privacyIntro"]}</p>' if page == 'privacy' else ''
        body = f'''<main class="legal-main wrap" id="main" tabindex="-1"><div class="legal-heading"><p class="eyebrow">{t['legalLabel']}</p><h1>{heading}</h1>{intro}<a class="text-link" href="{home}">← {t['back']}</a></div><article class="prose" aria-label="{heading}">{legal}</article></main>'''
    document = f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description, quote=True)}">
  <link rel="canonical" href="{url(lang, page)}">
  {alternate}<link rel="alternate" hreflang="x-default" href="{url('de', page)}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="onion Consulting">
  <meta property="og:title" content="{escape(title, quote=True)}">
  <meta property="og:description" content="{escape(description, quote=True)}">
  <meta property="og:url" content="{url(lang, page)}">
  <meta property="og:locale" content="{'de_DE' if lang == 'de' else 'en_GB'}">
  <meta property="og:locale:alternate" content="{'en_GB' if lang == 'de' else 'de_DE'}">
  <meta property="og:image" content="{DOMAIN}/assets/onion-2026.png">
  <meta property="og:image:alt" content="onion Consulting">
  <link rel="icon" href="{rel('favicon.ico')}">
  <link rel="stylesheet" href="{rel('assets/styles.css')}">
  <script src="{rel('assets/main.js')}" defer></script>
</head>
<body>
  {header}
  {body}
  {footer}
</body>
</html>
'''
    output = ROOT / path
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding='utf-8', newline='\n')


if __name__ == '__main__':
    for lang, pages in ROUTES.items():
        for page, path in pages.items():
            render(lang, page, path)
    # Existing URLs remain usable; canonical points to the language URL.
    for page, path in [('home', 'index.html'), ('legal', 'impressum.html'), ('privacy', 'datenschutz.html')]:
        render('de', page, path)
    links = ''.join(f'<url><loc>{url(lang, page)}</loc></url>' for lang in DATA for page in ROUTES[lang])
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + links + '</urlset>\n', encoding='utf-8')
    print('Generated 9 HTML pages and sitemap.xml.')

"""Check local links, bilingual SEO, original legal copy and asset integrity."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
import subprocess
import xml.etree.ElementTree as ET
from build import ROOT, ROUTES, url

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

errors = []
def check(condition, message):
    if not condition:
        errors.append(message)

pages = [ROOT / p for p in ['index.html', 'impressum.html', 'datenschutz.html', '404.html']]
pages += [ROOT / p for paths in ROUTES.values() for p in paths.values()]
parsed = {p: Page(p.read_text(encoding='utf-8')) for p in pages}
for path, doc in parsed.items():
    name = str(path.relative_to(ROOT))
    ids = [attrs['id'] for tag, attrs in doc.tags if 'id' in attrs]
    check(len(ids) == len(set(ids)), f'{name}: duplicate IDs')
    check(sum(tag == 'h1' for tag, attrs in doc.tags) == 1, f'{name}: expected one h1')
    check(any(tag == 'html' and attrs.get('lang') in ('de', 'en') for tag, attrs in doc.tags), f'{name}: lang missing')
    check(any(tag == 'meta' and attrs.get('name') == 'viewport' for tag, attrs in doc.tags), f'{name}: viewport missing')
    for tag, attrs in doc.tags:
        for key in ('href', 'src'):
            if key not in attrs:
                continue
            ref = urlsplit(attrs[key])
            if ref.scheme or ref.netloc:
                if key == 'src' or (tag == 'link' and attrs.get('rel') == 'stylesheet'):
                    check(False, f'{name}: externally loaded resource {attrs[key]}')
                continue
            target = ROOT / unquote(ref.path).lstrip('/') if ref.path.startswith('/') else path.parent / unquote(ref.path)
            if not ref.path:
                target = path
            if target.is_dir():
                target /= 'index.html'
            check(target.is_file(), f'{name}: missing target {attrs[key]}')
            target = target.resolve()
            if ref.fragment and target in parsed:
                check(any(a.get('id') == unquote(ref.fragment) for t, a in parsed[target].tags), f'{name}: missing fragment {attrs[key]}')
    if path.name != '404.html':
        check(any(tag == 'meta' and attrs.get('name') == 'description' and attrs.get('content') for tag, attrs in doc.tags), f'{name}: missing description')
        check(sum(tag == 'link' and attrs.get('rel') == 'canonical' for tag, attrs in doc.tags) == 1, f'{name}: canonical missing')
        for locale in ('de', 'en', 'x-default'):
            check(sum(tag == 'link' and attrs.get('hreflang') == locale for tag, attrs in doc.tags) == 1, f'{name}: missing alternate {locale}')
        check(sum(tag == 'a' and 'data-language' in attrs for tag, attrs in doc.tags) == 2, f'{name}: language switch missing')

for lang, routes in ROUTES.items():
    for page, route in routes.items():
        doc = parsed[ROOT / route]
        check(any(tag == 'link' and attrs.get('rel') == 'canonical' and attrs.get('href') == url(lang, page) for tag, attrs in doc.tags), f'{route}: wrong canonical')
        for other in ROUTES:
            check(any(tag == 'link' and attrs.get('hreflang') == other and attrs.get('href') == url(other, page) for tag, attrs in doc.tags), f'{route}: wrong alternate {other}')

baseline = subprocess.check_output(['git', 'show', '7defe4fe5a87fdc6f80af053a440514ae14d0402:datenschutz.html'], cwd=ROOT).decode('utf-8-sig')
original = re.search(r'<article[^>]*>(.*?)<div class="hero-actions">', baseline, re.S).group(1).strip()
check(original == (ROOT / 'content/privacy.de.html').read_text(encoding='utf-8').strip(), 'German privacy text differs from original')
baseline = subprocess.check_output(['git', 'show', '7defe4fe5a87fdc6f80af053a440514ae14d0402:impressum.html'], cwd=ROOT).decode('utf-8-sig')
original = re.search(r'<p>\s*<strong>.*?(?=<p>\s*<a href="index.html")', baseline, re.S).group(0).strip()
check(original == (ROOT / 'content/legal.de.html').read_text(encoding='utf-8').strip(), 'German legal notice differs from original')
for asset in ['assets/onion-logo-2026.png', 'assets/onion-2026.png', 'assets/onion-2026-60px.png', 'favicon.ico', 'CNAME']:
    check(subprocess.check_output(['git', 'show', f'7defe4fe5a87fdc6f80af053a440514ae14d0402:{asset}'], cwd=ROOT) == (ROOT / asset).read_bytes(), f'{asset} differs from original')

site = ET.parse(ROOT / 'sitemap.xml')
locations = {e.text for e in site.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
check(locations == {url(lang, page) for lang in ROUTES for page in ROUTES[lang]}, 'Sitemap does not match canonical routes')
js = (ROOT / 'assets/main.js').read_text(encoding='utf-8')
for token in ('localStorage', 'sessionStorage', 'document.cookie', 'fetch(', 'XMLHttpRequest', 'sendBeacon'):
    check(token not in js, f'Unexpected storage/network API: {token}')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} HTML pages; links and fragments, paired language SEO, metadata, original legal copy, unchanged assets/domain, sitemap, no JS storage/network APIs.')


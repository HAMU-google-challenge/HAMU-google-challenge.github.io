"""Check built HTML, local downloads, base paths and anchors using Python 3 only."""
import argparse
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.canonical = ''
        self.lang = ''
        self.headings = 0
        self.source = path.read_text(encoding='utf-8')
        self.feed(self.source)

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if 'id' in data:
            self.ids.append(data['id'])
        if tag == 'html':
            self.lang = data.get('lang', '')
        if tag == 'h1':
            self.headings += 1
        if tag == 'link' and data.get('rel') == 'canonical':
            self.canonical = data.get('href', '')
        for attr in ('href', 'src'):
            if attr in data:
                self.links.append(data[attr])


def check(root, baseurl=None):
    root = root.resolve()
    pages = {p.resolve(): Page(p) for p in root.rglob('*.html')}
    assert root / 'index.html' in pages, 'Missing homepage'
    assert root / 'en/index.html' in pages, 'Missing English homepage'
    if baseurl is None:
        baseurl = urlsplit(pages[root / 'index.html'].canonical).path.rstrip('/')
    baseurl = baseurl.rstrip('/')
    errors, count = [], 0
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        public_path = baseurl + '/' + relative
        if page.lang not in ('it', 'en'):
            errors.append(f'{relative}: missing or unsupported language')
        if page.headings != 1:
            errors.append(f'{relative}: expected one h1, found {page.headings}')
        for value, repeats in Counter(page.ids).items():
            if repeats > 1:
                errors.append(f'{relative}: duplicate id {value}')
        if '{{' in page.source or '{%' in page.source:
            errors.append(f'{relative}: unrendered Liquid')
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            if not link:
                errors.append(f'{relative}: empty href/src')
                continue
            resolved = urlsplit(urljoin(public_path, link))
            resource = unquote(resolved.path)
            if baseurl:
                if not (resource == baseurl or resource.startswith(baseurl + '/')):
                    errors.append(f'{relative}: URL escapes baseurl: {link}')
                    continue
                resource = resource[len(baseurl):]
            target = (root / resource.lstrip('/')).resolve()
            if not target.is_relative_to(root):
                errors.append(f'{relative}: path outside build: {link}')
                continue
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'{relative}: missing resource: {link}')
                continue
            if resolved.fragment and target in pages and unquote(resolved.fragment) not in pages[target].ids:
                errors.append(f'{relative}: missing anchor: {link}')
            count += 1
    for forbidden in ('_config.yml', 'Gemfile', 'Gemfile.lock', 'README.md', 'VERIFICHE.md', 'scripts', '.github', '.git'):
        if (root / forbidden).exists():
            errors.append(f'Internal source exposed in output: {forbidden}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'OK: {len(pages)} HTML pages, {count} local references, baseurl={baseurl or "/"}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('build', type=Path)
    parser.add_argument('--baseurl', default=None)
    args = parser.parse_args()
    check(args.build, args.baseurl)

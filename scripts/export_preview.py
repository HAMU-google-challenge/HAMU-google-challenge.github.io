"""Export a built Jekyll site as a portable file:// preview, using Python 3 only.

Use this for offline review only. GitHub Pages must build the original sources.
"""
import argparse
import html
from html.parser import HTMLParser
from pathlib import Path
import posixpath
import shutil
from urllib.parse import urlsplit


class RewriteLinks(HTMLParser):
    def __init__(self, relative_dir, baseurl):
        super().__init__(convert_charrefs=False)
        self.relative_dir = relative_dir
        self.baseurl = baseurl.rstrip('/')
        self.parts = []

    def rewrite(self, value):
        if not value.startswith('/') or value.startswith('//'):
            return value
        parsed = urlsplit(value)
        path = parsed.path
        if self.baseurl and (path == self.baseurl or path.startswith(self.baseurl + '/')):
            path = path[len(self.baseurl):]
        path = path.lstrip('/')
        if not path or path.endswith('/'):
            path += 'index.html'
        relative = posixpath.relpath(path, self.relative_dir)
        return relative + ('?' + parsed.query if parsed.query else '') + ('#' + parsed.fragment if parsed.fragment else '')

    def tag(self, tag, attrs, closed=False):
        rendered = []
        for name, value in attrs:
            if value is None:
                rendered.append(name)
            else:
                if name in ('href', 'src'):
                    value = self.rewrite(value)
                rendered.append(f'{name}="{html.escape(value, quote=True)}"')
        self.parts.append('<' + tag + (' ' if rendered else '') + ' '.join(rendered) + ('/>' if closed else '>'))

    def handle_starttag(self, tag, attrs): self.tag(tag, attrs)
    def handle_startendtag(self, tag, attrs): self.tag(tag, attrs, True)
    def handle_endtag(self, tag): self.parts.append('</' + tag + '>')
    def handle_data(self, data): self.parts.append(data)
    def handle_entityref(self, name): self.parts.append('&' + name + ';')
    def handle_charref(self, name): self.parts.append('&#' + name + ';')
    def handle_comment(self, data): self.parts.append('<!--' + data + '-->')
    def handle_decl(self, decl): self.parts.append('<!' + decl + '>')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('build', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--baseurl', default='')
    args = parser.parse_args()
    source, target = args.build.resolve(), args.output.resolve()
    if source == target or target.is_relative_to(source):
        raise SystemExit('Choose an output outside the Jekyll build directory')
    shutil.copytree(source, target, dirs_exist_ok=True)
    for path in target.rglob('*.html'):
        rewriter = RewriteLinks(path.parent.relative_to(target).as_posix(), args.baseurl)
        rewriter.feed(path.read_text(encoding='utf-8'))
        path.write_text(''.join(rewriter.parts), encoding='utf-8')
    print(target / 'index.html')

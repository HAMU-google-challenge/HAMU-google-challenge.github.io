"""Set Jekyll's URL from configure-pages outputs, only in the CI checkout."""
import json
import os
from pathlib import Path
from urllib.parse import urlsplit

origin = os.environ['PAGES_ORIGIN'].rstrip('/')
base = os.environ.get('PAGES_BASE_PATH', '').rstrip('/')
assert urlsplit(origin).scheme == 'https' and urlsplit(origin).netloc, 'Invalid Pages origin'
assert not base or base.startswith('/'), 'Invalid Pages base path'
with Path('_config.yml').open('a') as config:
    config.write('\n# Resolved by GitHub Actions\n')
    config.write('url: ' + json.dumps(origin) + '\n')
    config.write('baseurl: ' + json.dumps(base) + '\n')

#!/usr/bin/env python3
"""Build the Titanium X Assets manifest (index.json).

Scans the asset folders; files are named by IMDb ID (tt...) or TMDb
ID for title artwork, and by slug for collection artwork (genres,
networks, franchises, decades). Emits a machine-readable manifest
the Artwork Engine polls for updates (version + per-file entries).
"""
import json
import os
import time

TITLE_FOLDERS = {  # folder -> artwork key in the manifest
    'animated-posters': 'animatedposter',
    'animated-fanart': 'animatedfanart',
    'animated-keyart': 'animatedkeyart',
    'characters': 'characterart',
    'keyart': 'keyart',
    'discart': 'discart',
}
COLLECTION_FOLDERS = ('genres', 'networks', 'franchises', 'decades')


def build(base='.'):
    titles, collections = {}, {}
    for folder, key in TITLE_FOLDERS.items():
        path = os.path.join(base, folder)
        if not os.path.isdir(path):
            continue
        for name in sorted(os.listdir(path)):
            stem, ext = os.path.splitext(name)
            if ext.lower() not in ('.gif', '.png', '.jpg', '.webp'):
                continue
            titles.setdefault(stem, {})[key] = '%s/%s' % (folder, name)
    for folder in COLLECTION_FOLDERS:
        path = os.path.join(base, folder)
        if not os.path.isdir(path):
            continue
        for name in sorted(os.listdir(path)):
            stem, ext = os.path.splitext(name)
            if ext.lower() not in ('.gif', '.png', '.jpg', '.webp'):
                continue
            collections.setdefault(folder, {})[stem] = '%s/%s' % (folder, name)
    return {
        'name': 'Titanium X Assets',
        'version': int(time.time()),
        'titles': titles,
        'collections': collections,
    }


if __name__ == '__main__':
    manifest = build(os.path.dirname(os.path.abspath(__file__)))
    with open('index.json', 'w') as fh:
        json.dump(manifest, fh, indent=1)
    print('titles:', len(manifest['titles']),
          '| collections:', {k: len(v) for k, v in manifest['collections'].items()})

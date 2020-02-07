#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = (
    u'The Kinto team',
)

SITENAME = u'Kinto Storage'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = False

THEME = "theme"
INDEX_SAVE_AS = 'news.html'
MENUITEMS = (
    (u'About Kinto', '/index.html'),
    (u'News', '/news.html'),
)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
STATIC_PATHS = ['images', 'documents', 'extra/CNAME', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'}
}

RELATIVE_URLS = True

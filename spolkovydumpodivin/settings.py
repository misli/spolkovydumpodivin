# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
Django settings for spolkovydumpodivin project.
"""

from django.utils.translation import ugettext_lazy as _
from leprikon.site.settings import *

# Application definition
INSTALLED_APPS = [
    'cms_articles',
] + INSTALLED_APPS

CMS_TEMPLATES = [
    ('default.html', 'Výchozí'),
]

# templates used to render plugin article
CMS_ARTICLES_PLUGIN_ARTICLE_TEMPLATES = [
    ('default', 'Výchozí'),
]

# templates used to render plugin articles
CMS_ARTICLES_PLUGIN_ARTICLES_TEMPLATES = [
    ('default', 'Výchozí'),
]

CMS_PLACEHOLDER_CONF = {
    'content': {
        'name': 'Obsah',
    },
}

THUMBNAIL_ALIASES = {
    '': {
        'preview': {
            'size': (240, 10000),
        },
        'view': {
            'size': (760, 570),
        },
    },
}

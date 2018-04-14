#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os.path import expanduser

AUTHOR = 'Ranting Penguin'
SITENAME = 'Ranting Penguins Rants'
SITESUBTITLES = [ 'Ranting Penguins Rants', 'Full of optimism' ]
SITEURL = 'https://rantingpenguin.github.io/blog/'

PATH = 'content'

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = [expanduser('~/.local/share/pelican-plugins')]
PLUGINS = ['asciidoc_reader']

THEME = expanduser("~/projects/ranting_penguin/pelican-themes/bold")

# Blogroll
LINKS = ()
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = ()
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

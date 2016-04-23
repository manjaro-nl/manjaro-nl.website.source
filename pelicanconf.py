#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Manjaro-NL'
SITENAME = 'Manjaro-NL'
SITEURL = ''
SITELOGO ='/images/manjaro-logo.png'
SITELOGO_SIZE = '40px'

THEME = '/var/lib/jenkins/jobs/Manjaro-nl/workspace/theme/pelican-bootstrap3-edited/'
BOOTSTRAP_THEME = 'sandstone'
PYGMENTS_STYLE = 'perldoc'

MENUITEMS = (('Forum','http://www.manjaro-nl.org/smfnl/index.php'),('Download','https://manjaro.github.io/download/'),)

# custom css
CUSTOM_CSS = 'theme/css/custom.css'

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ('.git','robots.txt')

STATIC_PATHS = ['code','images','extra']
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'},
    'extra/css/custom.css': {'path': 'theme/css/custom.css'},
    'extra/css/magnific-popup.css': {'path': 'theme/css/magnific-popup.css'},
    'extra/js/jquery.magnific-popup.js': {'path': 'theme/js/jquery.magnific-popup.js'},
    'extra/robots.txt': {'path': 'robots.txt'},
    }

PLUGIN_PATHS = ['plugins']
PLUGINS = ['photos','neighbors','series','tag_cloud','pin_to_top', 'liquid_tags.youtube','liquid_tags.include_code','summary','tipue_search','extract_toc']

MD_EXTENSIONS = (['toc'])

DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = 5

TIMEZONE = 'Europe/Amsterdam'
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')
DEFAULT_LANG = 'nl'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap','search')
SITEMAP_SAVE_AS = 'sitemap.xml'

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_TAGS_INLINE = True

#Photos plugin#
PHOTO_LIBRARY = "/var/lib/jenkins/jobs/Manjaro-nl/workspace/content/photos/"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = ( 760, 506, 80)
PHOTO_THUMB = (192, 144, 60)

#Tipue Search plugin#
SEARCH_URL = '/search.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('Manjaro wiki', 'https://wiki.manjaro.org/'),
        ('Arch wiki', 'https://wiki.archlinux.org/'),
        )

# Social widget
SOCIAL =    (('reddit', 'http://www.reddit.com/r/ManjaroLinux'),
            ('facebook', 'https://www.facebook.com/manjaronl/'),
            ('google+', 'https://plus.google.com/communities/107339606748051600367')
            )
DEFAULT_PAGINATION = 5

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = ('posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html')
ARTICLE_LANG_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ('posts/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html')
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

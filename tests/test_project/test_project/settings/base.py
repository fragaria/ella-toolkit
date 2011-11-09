# Django base settings for dum_common project.

from os.path import dirname, join, abspath

import test_project

gettext = lambda s: s

PROJECT_ROOT = abspath(dirname(test_project.__file__))

ADMINS = (
    ('Filip Varecha', 'filip.varecha@fragaria.cz'),
)
DEFAULT_FROM_EMAIL = 'admin@fragaria.cz'
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Prague'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'cs'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

# Site ID
SITE_ID = 1

# Absolute path to the directory that holds media.
MEDIA_ROOT = join(PROJECT_ROOT, 'media')

ROOT_URLCONF = 'test_project.urls'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'raven.contrib.django.middleware.SentryResponseErrorIdMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(PROJECT_ROOT, 'templates'),
)

FIXTURE_DIRS = (
   join(PROJECT_ROOT, 'fixtures'),
)

ODT_DIR = join(PROJECT_ROOT, 'templates', 'odt')

STATIC_URL = '/static/'

INSTALLED_APPS = (
    # core django apps
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.sitemaps',

    'ella.core',
    'ella.articles',
    
    'ella_toolkit.articles.multiple_contents',
    'ella_toolkit.publishable.js_hits',
    'ella_toolkit.publishable.send_email',
)
# always freeze south migrations
SOUTH_AUTO_FREEZE_APP = True

# logout the user on browser close
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

import os

DIRNAME = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = False
COMPRESS_CACHE_BACKEND = 'locmem:///'

DEFAULT_FROM_EMAIL = 'your_email@domain.com'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',   # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                        # Or path to database file if using sqlite3.
        'USER': '',                        # Not used with sqlite3.
        'PASSWORD': '',                    # Not used with sqlite3.
        'HOST': '',                        # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                        # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = DIRNAME + "/media"

# static files settings
STATIC_URL = '/static/'
STATIC_ROOT = DIRNAME + "/sitestatic"

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+0zsw5n@v7*rhl6r6ufqhoc6jlqq0f-u8c+gh(hjb+_jmg@rh6'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    "pagination.middleware.PaginationMiddleware",
    'django.contrib.messages.middleware.MessageMiddleware',
    "lfc.utils.middleware.LFCMiddleware",
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    "compressor",
    "lfc_theme",
    "django.contrib.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    "django.contrib.flatpages",
    "django.contrib.sitemaps",
    "django.contrib.comments",
    "lfc",
    "lfc_contact_form",
    "lfc_page",
    "lfc_portlets",
    "pagination",
    "permissions",
    "portlets",
    "tagging",
    "workflows",
)


FORCE_SCRIPT_NAME = ""

LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/manage/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.i18n',
    'lfc.context_processors.main',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

CACHE_MIDDLEWARE_KEY_PREFIX = 'lfc'

EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "datefmt": "%a, %d %b %Y %H:%M:%S",
        },
        "simple": {
            "format": "%(levelname)s %(message)s",
            "datefmt": "%a, %d %b %Y %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(DIRNAME, "..", "lfc.log"),
            'mode': 'a',
        },
    },
    "loggers": {
        "default": {
            "handlers": ["logfile", "console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "qinspect": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    }
}

PAGINATION_DEFAULT_PAGINATION = 5
PAGINATION_DEFAULT_WINDOW = 1

LANGUAGES = (("en", u"English"), ("de", u"German",))
LFC_MULTILANGUAGE = len(LANGUAGES) > 1
LFC_MANAGE_WORKFLOWS = True
LFC_MANAGE_PERMISSIONS = True
LFC_MANAGE_APPLICATIONS = True
LFC_MANAGE_USERS = True
LFC_MANAGE_UTILS = True

LFC_MANAGE_META_DATA = True
LFC_MANAGE_SEO = True
LFC_MANAGE_COMMENTS = True
LFC_MANAGE_PORTLETS = True
LFC_MANAGE_IMAGES = True
LFC_MANAGE_FILES = True

LFC_TAGS = [
    "lfc_tags",
]

try:
    from local_settings import *
except ImportError:
    pass

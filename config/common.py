#coding: utf-8
import os
import sys

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(ROOT, 'journal'))

ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = os.path.relpath(os.path.join(ROOT, '..', 'static'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'wnaaan!o1x94zd9&c9oq1^fq6jcqxa=^ai9##&la3)+#mz!tc6'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    #    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    #'dealer.contrib.django.staff.context_processor',
    # 'common.context_processors.settings_context_processor',
    # 'common.context_processors.site_context_processor',
    # 'customization.context_processors.customization_context_processor',
)

TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'journal.urls'

WSGI_APPLICATION = 'journal.wsgi.application'

TEMPLATE_DIRS = (
    "templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',

    'rest_framework',
    'djangojs',
    'taggit',

    'feed',
    'link'
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

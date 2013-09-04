#!/usr/bin/env python

SECRET_KEY = os.environ.get('SECRET_KEY', '$^(o6rr2x#xd-5_(7(@@55!6r9_jmlqblft1k4zmq6hc!w+nm_')

import os
from .installed_apps import *
from .s3_utils import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'database.sqlite3',
    }
}

ALLOWED_HOSTS = []

STATICFILES_STORAGE = 'lightning.settings.s3_utils.StaticRootS3BotoStorage'
STATIC_URL = "https://lightning-static.s3.amazonaws.com/"

DEFAULT_FILE_STORAGE = 'lightning.settings.s3_utils.MediaRootS3BotoStorage'
MEDIA_URL = 'https://lightning-media.s3.amazonaws.com/'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

#MEDIA_ROOT = ''
#MEDIA_URL = ''
#STATIC_ROOT = ''
#STATIC_URL = '/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lightning.urls'

WSGI_APPLICATION = 'lightning.wsgi.application'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

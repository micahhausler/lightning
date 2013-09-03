DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

UNIVERSE_APPS = (
    'django_extensions',
    # Storages here
    'storages',
)

PROJECT_APPS = (
    'lightning.thunder',
)

INSTALLED_APPS = DJANGO_APPS + UNIVERSE_APPS + PROJECT_APPS

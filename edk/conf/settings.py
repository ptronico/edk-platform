"""
Django settings for edk project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import socket

from unipath import Path

# Project path
PROJECT_DIR = Path(__file__).ancestor(3)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-e_c8)d(lt)ep6wc%%r^dh5nyqsl%+)j#hq=l@+$z%887qe-ot'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*'] # []

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

# Media files

MEDIA_URL = '/media/'

# Teamplates files

TEMPLATE_DIRS = (
    PROJECT_DIR.child('edk', 'templates'),
)

if 'pedro-laptop' in socket.gethostname():
    # Development

    PROJECT_DATA_DIR = Path('/User/ptronico/dev/appdata/edk')

    DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.postgresql_psycopg2',
            'NAME': 'edk',
            'USER': 'ptronico',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

else:    
    # Production
    
    PROJECT_DATA_DIR = Path('/home/ubuntu/data/edk')

    DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.postgresql_psycopg2',
            'NAME': 'edk',
            'USER': 'ptronico',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }    


STATIC_ROOT = PROJECT_DATA_DIR.child('static')

MEDIA_ROOT = PROJECT_DATA_DIR.child('media')


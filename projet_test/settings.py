"""
Django settings for projet_test project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eb+kpayu7ztayvs#3+-$ej1ug*k=g_we53s@i@xoc27rbgc_a3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'albums',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'albums.middleware.SqlAlchemyMiddleware'
)

ROOT_URLCONF = 'projet_test.urls'

WSGI_APPLICATION = 'projet_test.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# specific to this project

import django.conf.global_settings as DEFAULT_SETTINGS

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'albums.context_processors.add_versions',
)

# place this in a file named local_settings.py, fill the params and add the file name to .gitignore
DATABASE = {
    'HOST': '',
    'LOGIN': '',
    'PASSWORD': '',
    'DATABASE': '',
    'OPTIONS': 'charset=utf8&use_unicode=0',
}

# include local settings safely
try:
    from local_settings import *
except:
    pass

# intialize the SQLAlchemy session class and make it available through the settings
# /!\ to be placed after import of local_settings of course
import albums.models
DB_SESSION = albums.models.init_session(DATABASE)  # DB_SESSION need to be in capitals otherwise django ignores it...

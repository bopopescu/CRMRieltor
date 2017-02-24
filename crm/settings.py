"""
Django settings for crm project.up

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

try:
    from add_settings import *
except ImportError:
    pass

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']



# Application definition



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homes',
    'notes',
    'setting_street',
    'extuser',
    'facility',
    'setting_globall',
    'trash_object',
    'single_object',
    'who_online',
    'send_messege_user',
    'arendator',
    'buyer',
    'makler',
    'setting_superadmin',
    'tasking',
    'parsings',
    'posting',
    'watermark',
    'sender_email',
    'setting_mail_delivery',
    'meeting',
    'searching',
    'single_arendator',
    'single_buyer',
    'backupbd_crm',
    'dbbackup',
    'django_cron',
    'learning',
    'access',
    'solo',
] + ADD_INSTALLED_APPS

CRON_CLASSES = [
    "crm.cron.Backup",
]

MIGRATION_MODULES = {}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crm.urls'
LOGIN_REDIRECT_URL = '/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'crm.wsgi.application'
# SESSION_COOKIE_AGE = 1800
# AUTH_USER_MODEL = 'extuser.User'
EMAIL_HOST = 'mail.dom6.dom.zt.ua'
EMAIL_HOST_USER = 'rieltor@dom6.dom.zt.ua'
EMAIL_HOST_PASSWORD = 'Qazsin1984'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': (os.path.join(BASE_DIR, 'media/auto_backup'))}



# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'crm',
        'USER': 'varunok',
        'PASSWORD': '111111',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

DATABASES_POST = {
    'USER': 'root',
    'DATABASE': '',
    'HOST': 'localhost',
    'PASS': '111111',
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'UK'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# MEDIA_ROOT = (BASE_DIR + '/media')
MEDIA_ROOT = (os.path.join(BASE_DIR, 'media/'))
STATIC_ROOT = (os.path.join(BASE_DIR, 'static/'))
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

try:
    from local_settings import *
except ImportError:
    pass



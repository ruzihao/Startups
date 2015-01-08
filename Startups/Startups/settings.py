"""
Django settings for Startups project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, platform
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vqh)a3yj(5(o=t)9!a&235u1#e0ns^u($3s&4g!9@n7kk7c)7y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates').replace('\\', '/'),)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'companies',
    'profiles',
    'lockdown',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'lockdown.middleware.LockdownMiddleware',
)

LOCKDOWN_PASSWORDS = ('huixiong',)

ROOT_URLCONF = 'Startups.urls'

WSGI_APPLICATION = 'Startups.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if 'Windows-7-6.1.7601-SP1' not in platform.platform():
	db_password = 'huixiong'
else:
	db_password = ''
		
DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.mysql',
		# 'NAME': 'companies',
        'NAME': 'spokeintel',
		'USER': 'root',
		'PASSWORD': db_password,
		'HOST': '127.0.0.1',
		'PORT': '3306',
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
# STATIC_URL = '/Startups/static/profiles/'
# STATIC_ROOT = os.path.join(os.path.dirname(__file__), STATIC_URL)
# STATIC_ROOT = ''
# STATIC_URL = '/templates/profiles/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/profiles/'),)
# STATICFILES_DIRS = ('F:/Dropbox/Documents/Projects/QuantIn/Startups/Startups/Startups/statics/',)
# STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'Startups/' + STATIC_URL).replace('\\', '/'),
#                     os.path.join(PROJECT_ROOT, 'Startups/' + STATIC_URL + '/profiles').replace('\\', '/'),)

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )
"""
Django settings for GeoDjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'OPENSHIFT_REPO_DIR' not in os.environ
TEMPLATE_DEBUG = DEBUG


# Hosting Configuration
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'apps.base.urls'
WSGI_APPLICATION = 'config.wsgi.application'

# Secret Key
if DEBUG:
    import random
    SECRET_KEY = '%030x' % random.randrange(16**30)
else:
    SECRET_KEY = os.environ.get('OPENSHIFT_SECRET_KEY')


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
# https://docs.djangoproject.com/en/1.6/ref/settings/#use-x-forwarded-host
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local
    'apps.base',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {

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
if DEBUG:
    STATIC_ROOT = 'staticfiles'
else:
    STATIC_ROOT = os.path.join(os.environ['OPENSHIFT_DATA_DIR'], 'staticfiles')

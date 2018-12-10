"""
Django settings for abosadmin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR,  ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ap2r)oceezd_e%pck@c%ozqc8uoogpz#r9#)^scbtedr#e#m7v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*', ]
INTERNAL_IPS = ['10.0.2.2', '127.0.0.1']
# Application definition

INSTALLED_APPS = (
    'hoster',
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'short_cut',
    'django_uwsgi',
    'debug_toolbar',
    # 'polls',
    # 'tutor',
    'webblog',
)

MIDDLEWARE_CLASSES = (
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'abosadmin.urls'

WSGI_APPLICATION = 'abosadmin.wsgi.application'
DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'abosadmin',
        'HOST': 'db.host',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '3a7d30f2de',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = 'http://static.abos5.com/djangoadmin/'
STATIC_ROOT = '/data/web/static.abos5.com/djangoadmin/'

# LOGGING = {
#     'version': 1,
#     'handlers': {
#         'default': {
#             'filename': '/data/logs/admin.abos5.com.8080',
#             'level': 'DEBUG',
#             'class': 'django.utils.log.Admin'
#         }
#     }
# }


# eof

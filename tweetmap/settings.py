import os
from ConfigParser import RawConfigParser

config = RawConfigParser()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config.read(os.path.join(os.path.dirname(__file__), 'secret_settings.ini'))

SECRET_KEY = config.get('secrets', 'SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

#mandrill email config
EMAIL_HOST = config.get('mandrill', 'EMAIL_HOST')
DEFAULT_FROM_EMAIL = config.get('mandrill', 'DEFAULT_FROM_EMAIL')
EMAIL_PORT = config.get('mandrill', 'EMAIL_PORT')
EMAIL_USE_TLS = config.get('mandrill', 'EMAIL_USE_TLS')
MANDRILL_API_KEY = config.get('mandrill', 'MANDRILL_API_KEY')
EMAIL_BACKEND = config.get('mandrill', 'EMAIL_BACKEND')

# Twitter Oauth credentials
TWITTER_USER = config.get('twitter', 'TWITTER_USER')
TWITTER_CACHE_TIMEOUT = config.get('twitter', 'TWITTER_CACHE_TIMEOUT')
TWITTER_CONSUMER_KEY = config.get('twitter', 'TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = config.get('twitter', 'TWITTER_CONSUMER_SECRET')
TWITTER_OAUTH_TOKEN = config.get('twitter', 'TWITTER_OAUTH_TOKEN')
TWITTER_OAUTH_TOKEN_SECRET = config.get('twitter', 'TWITTER_OAUTH_TOKEN_SECRET')

INSTALLED_APPS = (
    'twitmap',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'crispy_forms',
    'djrill',
    'bootstrapform',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'tweetmap.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'tweetmap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "\static_in_pro", "our_static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR + "\static_in_pro", "our_static"),
)

#crispy forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#django registration redux settings
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1


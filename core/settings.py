
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'xxxxx'
CSRF_COOKIE_SECURE = False
CSRF_TRUSTED_ORIGINS = ['exantrix.com']
DEBUG = True
ALLOWED_HOSTS = ['exantrix.com']
DATA_UPLOAD_MAX_MEMORY_SIZE = 31457280  # 31 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 31457280  # 31 MB


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backoffice',
    'commande',
    'utilisateur',
    'page',
    'produit'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware'
]

ROOT_URLCONF = 'core.urls'

USER_AGENTS_CACHE = 'default'
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://xxx\1",
        'KEY_PREFIX': 'xx',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "TIMEOUT": 1209600,
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor"}}}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/home/ipq/mvt/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


ASGI_APPLICATION = 'core.asgi.application'
WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {'default': {'ATOMIC_REQUESTS': False,
             'AUTOCOMMIT': True,
             'CONN_MAX_AGE': 86400,
        'ENGINE': 'django.db.backends.postgresql_xx',
        'NAME': 'xx',
        'USER': 'xx',
        'PASSWORD':'xx',
        'HOST': 'xx',
        'PORT': 'xx',
        'TIME_ZONE':'UTC'} }




SECURE_HSTS_PRELOAD = True
AUTH_PASSWORD_VALIDATORS = [{'xx'}]
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.protonmail.ch'
EMAIL_USE_TLS = False
EMAIL_PORT = xx
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'xx'
EMAIL_HOST_PASSWORD = 'xx'
EMAIL_SSL_CERTFILE = None
EMAIL_SUBJECT_PREFIX = 'xx'
EMAIL_TIMEOUT = None
EMAIL_USE_LOCALTIME = False
PREPEND_WWW = False
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

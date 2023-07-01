from datetime import timedelta
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
APPS_DIR = BASE_DIR / 'apps'
env = environ.Env()

READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    env.read_env(str(BASE_DIR / '.env'))


DEBUG = env.bool('DJANGO_DEBUG', False)

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'ru-ru'

USE_I18N = True

USE_TZ = True


# DATABASES

DATABASES = {'default': env.db('DATABASE_URL')}
DATABASES['default']['ATOMIC_REQUESTS'] = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# URLS

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# APPS

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.admin',
]
THIRD_PARTY_APPS = ['rest_framework', 'corsheaders', 'drf_spectacular']

LOCAL_APPS = ['apps.deals']

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# AUTHENTICATION

# AUTH_USER_MODEL = 'users.User'

# PASSWORDS

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
)

AUTH_PASSWORD_VALIDATORS = (
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
)

# MIDDLEWARE

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# STATIC

STATIC_ROOT = '/var/www/django/static'

STATIC_URL = '/static/'

STATICFILES_DIRS = (str(APPS_DIR / 'static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# MEDIA

MEDIA_ROOT = env('DJANGO_MEDIA_ROOT', default=str(BASE_DIR / 'media'))

MEDIA_URL = '/media/'

# TEMPLATES

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
)


# SECURITY

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'


# LOGGING

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {'verbose': {'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'}},
    'handlers': {'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'verbose'}},
    'root': {'level': 'INFO', 'handlers': ['console']},
}


# DJANGO REST FRAMEWORK

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_ALL_ORIGINS = True

SPECTACULAR_SETTINGS = {
    'TITLE': 'Deal Tracker API',
    'DESCRIPTION': 'Documentation of API endpoints of Deal Tracker',
    'VERSION': '1.0.0',
    'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
    'SERVE_AUTHENTICATION': ['rest_framework.authentication.SessionAuthentication'],
    'COMPONENT_SPLIT_REQUEST': True,
}

SIMPLE_JWT = {'ACCESS_TOKEN_LIFETIME': timedelta(days=100), 'AUTH_HEADER_TYPES': ('Bearer',)}

from config.settings.base import *  # noqa: F403, F401
from config.settings.base import env

# GENERAL

DEBUG = True

SECRET_KEY = env('DJANGO_SECRET_KEY', default='BXpia9uYBJGfO4z6uxhy5lB3AMhZRjhdZKtwUA78VWbCY2Cbzs2KUMNUQtKKm5UH')

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']

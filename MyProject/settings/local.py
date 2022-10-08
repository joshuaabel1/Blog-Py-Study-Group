from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static'))]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
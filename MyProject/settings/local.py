from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static'))]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
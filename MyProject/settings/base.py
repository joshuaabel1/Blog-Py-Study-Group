from distutils.log import debug
import dj_database_url
import os
from dotenv import load_dotenv

load_dotenv()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False



ALLOWED_HOSTS =  ['*']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Blog',
    'social_django',  
    'bootstrap5',
    'crispy_forms',
    "whitenoise.runserver_nostatic",   
    'storages',
    
]

MIDDLEWARE = [
    'Blog.adminprotect.RestrictStaffToAdminMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    
]

ROOT_URLCONF = 'MyProject.urls'

TEMPLATES = [
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
                'social_django.context_processors.backends', 
            ],
        },
    },
]

WSGI_APPLICATION = 'MyProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
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

AUTHENTICATION_BACKENDS = [ 
    'social_core.backends.github.GithubOAuth2', 
    'django.contrib.auth.backends.ModelBackend' 
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# Following settings only make sense on production and may break development environments.

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = 'signin'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'home'
SOCIAL_AUTH_GITHUB_KEY = os.getenv('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = os.getenv('SOCIAL_AUTH_GITHUB_SECRET')
# DJANGO_SUPERUSER_PASSWORD=os.getenv('DJANGO_SUPERUSER_PASSWORD')
# DJANGO_SUPERUSER_USERNAME=os.getenv('DJANGO_SUPERUSER_USERNAME') 

# os.getenv('SOCIAL_AUTH_GITHUB_KEY')
# os.getenv('SOCIAL_AUTH_GITHUB_SECRET')
# SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
# SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['state']
# SESSION_COOKIE_SECURE = False
# que hace setting?
# En el archivo setting tenemos el funcionamiento de nuestro sitio aca, 
# agregamos permisos variables aplicaciones que use nuestro sitio
# .\
HTTPS = 'on'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# This setting tells Django at which URL static files are going to be served to the user.
# Here, they well be accessible at your-domain.onrender.com/static/...

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static'))]
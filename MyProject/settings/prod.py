from .base import *


HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DBNAME = os.getenv('DBNAME')


DATABASE_URL = f'postgres://{USER}:{PASSWORD}@{HOST}:5432/{USER}'
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'MyProject/static'),
    ]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
                                                                                                                                                                                                                                                                                                                                                        
AWS_DEFAULT_REGION=os.getenv('AWS_DEFAULT_REGION')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
DEFAULT_FILE_STORAGE = 'MyProject.storage_backends.MediaStorage'
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
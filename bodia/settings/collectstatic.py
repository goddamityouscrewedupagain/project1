from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# DEFAULT_FILE_STORAGE = 'bodia.storages.LocalMediaStorage'
# STATICFILES_STORAGE = 'bodia.storages.LocalStaticStorage'

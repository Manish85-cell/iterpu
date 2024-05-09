from .base import *
import os


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']  
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# ALLOWED_HOSTS = ['localhost', '.execute-api.us-west-2.amazonaws.com'] 
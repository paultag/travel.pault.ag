import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = os.environ.get("SECRET_KEY", "")
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, "templates")
]
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'travel',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'public.urls'
WSGI_APPLICATION = 'public.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
ENABLE_MAPBOX = os.environ.get("TRAVEL_ENABLE_MAPBOX", "True").lower() == "true"

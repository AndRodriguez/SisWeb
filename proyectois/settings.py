"""
Django settings for proyectois project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from django.contrib import messages 
from django.contrib.messages import constants as message_constants 
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%q&_=pvrgk#jz_xuvvol8jr8%#^gvj)7$+1v(vp9!o)p(m7dxm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.railway.app',
    
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ventasApp',
    'seguridadApp',
    'crispy_forms',
]


CSRF_TRUSTED_ORIGINS = ["https://sisweb-production.up.railway.app"]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyectois.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'seguridadApp/templates'),
                os.path.join(BASE_DIR, 'ventasApp/templates'),
                os.path.join(BASE_DIR, 'proyectois/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyectois.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#mysql://root:kRdWDhugLyrBOOEHADigShjdDEiaKqbg@junction.proxy.rlwy.net:33199/railway
#mysql -hjunction.proxy.rlwy.net -uroot -pkRdWDhugLyrBOOEHADigShjdDEiaKqbg --port 33199 --protocol=TCP railway
DATABASES = {
    'default': {
	'ENGINE': 'django.db.backends.mysql',
	'NAME': 'railway',
	'USER': 'root',
	'PASSWORD': 'kRdWDhugLyrBOOEHADigShjdDEiaKqbg',
	'HOST': 'junction.proxy.rlwy.net',
	'PORT': '33199',
	}
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-eu'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/' 

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'seguridadApp/static'),
    os.path.join(BASE_DIR, 'proyectois/static'),
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CRISPY_TEMPLATE_PACK = "bootstrap4"

#clases para los mensajes flash de bootstrap 

MESSAGE_TAGS = {
    message_constants.DEBUG:'debug',
    message_constants.INFO:'info',
    message_constants.SUCCESS:'success',
    message_constants.WARNING:'warning',
    message_constants.ERROR:'danger',
}
  


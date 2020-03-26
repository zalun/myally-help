"""
Django settings for myally project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import myally.security as env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ")+dvldm^(6nrb2q4q(@27!6y)8tet^(ndmt$%p5_o=uhy(w*b^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.DEBUG

ALLOWED_HOSTS = env.ALLOWED_HOSTS if env.ALLOWED_HOSTS else []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    # The following apps are required for allauth
    "django.contrib.auth",
    "django.contrib.messages",
    "django.contrib.sites",
    "django_countries",
    # MyAlly apps
    "causes",
    "therapists",
    # Third party
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.google',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 1

# All Auth
ACCOUNT_ADAPTER = 'myally.account_adapter.NoNewUsersAccountAdapter'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = ("email")
LOGIN_REDIRECT_URL = "/therapist/profile"
SOCIALACCOUNT_AUTO_SIGNUP = False

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = "myally.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "myally", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myally.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.POSTGRESQL_DATABASE,
        'USER': env.POSTGRESQL_USER,
        'PASSWORD': env.POSTGRESQL_PASSWORD,
        'HOST': env.POSTGRESQL_HOST,
        'PORT': '',
    }
    # "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
if env.STATIC_ROOT:
    STATIC_ROOT = os.path.join(env.STATIC_ROOT, "static")
    STATICFILES_DIRS = [STATIC_ROOT]


ADMINS = env.ADMINS or []

# Emails
if env.EMAIL_HOST_USER:
    EMAIL_BACKEND = ‘django.core.mail.backends.smtp.EmailBackend’
    EMAIL_HOST = env.EMAIL_HOST
    EMAIL_USE_TLS = env.EMAIL_USE_TLS
    EMAIL_PORT = env.EMAIL_PORT
    EMAIL_HOST_USER = env.EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD = env.EMAIL_HOST_PASSWORD

"""
Django settings for SalvePets project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-99x#o@c^zab4yjx^t96nq!zniee1+r7fr*@7duka^3-vm2+iln'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.salvepets.online','salvepets.online','3.239.208.137','ec2-3-239-208-137.compute-1.amazonaws.com']

#Caminho das imagens(foto)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


#if os.name == 'nt':
 #   VENV_BASE = os.environ['VIRTUAL_ENV']
  #  os.environ['PATH'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
   # os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj') + ';' + os.environ['PATH']



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# use this if setting up on Windows 10 with GDAL installed from OSGeo4W using defaults
if os.name == 'nt':
    VIRTUAL_ENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']




#import SalvePets
#DATABASES['default'] = SalvePets.config()
#DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


#[...] settings.py code continues



#GDAL_LIBRARY_PATH = r'c:\\users\\dimas\\documents\\gitprojects\\projetosalvepets\\virtualenv\\salvepets\\lib\\site-packages\\GDAL-3.3.1.dist-info'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'core',

    #bibliotecas instaladas
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django.contrib.gis',
    'leaflet',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SalvePets.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'SalvePets/templates')],
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

WSGI_APPLICATION = 'SalvePets.wsgi.application'

"""
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

# MATHEUS DIAS 22/06/2021: Essa é a conexão com o PostgreSQL. Como esse serviço ainda não foi hospedado na AWS, não temos um IP ou DNS para que
# a aplicação acesse os dados. Por conta disso, caso queira testar com o PostgreSQL, faça o seguinte procedimento:

# Instale o PostgreSQL + PostGis
# Mantenha o usuário padrão e configure a senha para 123456
# Crie um banco de dados com o nome "SalvePets"
# Rode o banco de dados
#
# Depois disso, exclua a pasta "migrations" e execute os  comandos, em seguida:
# python manage.py makemigrations core
# python manage.py migrate
#
# Atualize o banco de dados pelo pgAdmin e você verá as tabelas.


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'salvepets', 
        'USER': 'postgres', 
        'PASSWORD': 'salve123456',
        'HOST': 'salvepets.cjbod3zbq85f.us-east-1.rds.amazonaws.com', 
        'PORT': '5432',
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', ("English")),
    ('pt-br', ("Português Brasileiro")),
]

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#django-allauth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
ACCOUNT_SESSION_REMEMBER = True

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'    #não envia o e-mail para o usuário, após deploy precisa configurar o envio do e-mail
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = "true"

ACCOUNT_SIGNUP_FORM_CLASS = 'core.forms.SignupForm'

"""
LOGIN_URL = reverse_lazy('submit_login')
LOGIN_REDIRECT_URL = reverse_lazy('index')
"""

#django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Configurações do email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST 

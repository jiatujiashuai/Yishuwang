"""
Django settings for Yishuwang project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z9622t#p&bs)zskz&b%w@+t3irbv*e9z(@#i^yhn(k=-7i*j7!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Yishuwang.urls'
AUTH_PROFILE_MODULE = 'app.UserProfile'
LOGIN_REDIRECT_URL = r'/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Yishuwang.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'


#media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace("\\", "/")
MEDIA_URL = '/media/'


#  ---------------------------------------------------------
#  Email
USERS_REGISTRATION_OPEN = True
 
USERS_VERIFY_EMAIL = True
 
USERS_AUTO_LOGIN_ON_ACTIVATION = True
 
USERS_EMAIL_CONFIRMATION_TIMEOUT_DAYS = 3
 
# Specifies minimum length for passwords:
USERS_PASSWORD_MIN_LENGTH = 5
 
# Specifies maximum length for passwords:
USERS_PASSWORD_MAX_LENGTH = None
 
# the complexity validator, checks the password strength
USERS_CHECK_PASSWORD_COMPLEXITY = True
 
USERS_SPAM_PROTECTION = False  # important!
 

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# 指定本应用所在服务器的主机名称。
SITE_HOST = '127.0.0.1:8000'
# 指定电子邮件发件服务器地址，这里使用sjtu邮箱的发件服务器地址。
EMAIL_HOST = 'smtp.sjtu.edu.cn'
# 指定电子邮件发件服务器所使用的端口号，不填写表示使用缺省的端口号25。
EMAIL_PORT = ''
# 指定登录电子邮箱所使用的用户名，可根据实际情况填写。
EMAIL_HOST_USER = '******'
# 指定登录163 电子邮箱所使用的用户密码，读者可根据实际情况填写。
EMAIL_HOST_PASSWORD = '******'
# 指定电子邮件发件人信息。其中的电子邮件地址填写读者自己的电子邮箱地址。
DEFAULT_FROM_EMAIL = 'password reset<******@sjtu.edu.cn>'

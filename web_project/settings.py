import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'lab_db'),
        'USER': os.environ.get('DB_USER', 'lab_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'lab_password'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': '5432',
    }
}

from pathlib import Path

# Базовая папка проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для разработки
SECRET_KEY = 'django-insecure-development-key-for-lab-project'

# Дебаг-режим включен
DEBUG = True

# Разрешаем доступ к серверу со всех хостов (необходимо для Docker)
ALLOWED_HOSTS = ['*']

# Настройки приложений
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lab6',  # Твое приложение для лабораторной
]

# Настройки связующего ПО (Middleware) — это исправляет ошибки E408, E409, E410
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web_project.urls'

# Настройки рендеринга шаблонов — это исправляет ошибку E403
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'web_project.wsgi.application'



# Валидация паролей
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

# Язык и таймзона
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статические файлы (CSS, JS, Картинки)
STATIC_URL = 'static/'

# Привязка твоей кастомной модели пользователя (13 этап)
AUTH_USER_MODEL = 'lab6.User'

AUTHENTICATION_BACKENDS = [
    'lab6.authentication.EmailAuth',
    'django.contrib.auth.backends.ModelBackend',
]

# Настройка типов ID по умолчанию (убирает Warning из лога)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
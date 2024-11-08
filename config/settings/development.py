from comum import * # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3', # noqa
    }
}


CORS_ALLOW_ALL_ORIGINS = True

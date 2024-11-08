from .comum import * # noqa
from dj_database_url import parse as db_url


DATABASES = {
    'default': config( # noqa
        'DATABASE_URL',
        default='postgres://postgres:postgres@127.0.0.1:5432/quebrei',
        cast=db_url
    ),
}

CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS').split(",") # noqa

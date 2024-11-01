from .comum import * 



DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='postgres://postgres:postgres@127.0.0.1:5432/quebrei',
        cast=db_url
    ),
}
from .comum import * 



DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='postgres://postgres:postgres@127.0.0.1:5432/db_solar',
        cast=db_url
    ),
}
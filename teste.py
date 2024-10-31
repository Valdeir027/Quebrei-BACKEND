from decouple import config


print(type(config('ALLOWED_HOSTS').split(",")))
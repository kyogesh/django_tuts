from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'review_db',
        'USER': 'yogesh',
        'PASSWORD': os.environ['PG_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

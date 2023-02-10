import os

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', default='django.db.backends.postgresql'),
        'NAME': os.environ.get('LOYALTY_POSTGRES_DB_NAME', default=None),
        'USER': os.environ.get('LOYALTY_POSTGRES_DB_USER', default=None),
        'PASSWORD': os.environ.get('LOYALTY_POSTGRES_DB_PASSWORD', default=None),
        'HOST': os.environ.get('LOYALTY_POSTGRES_DB_HOST', default=None),
        'PORT': os.environ.get('LOYALTY_POSTGRES_DB_PORT', default=None)
    }
}

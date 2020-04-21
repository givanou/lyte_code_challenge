DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'local_secret'

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lyte',
        'USER': 'lyte',
        'PASSWORD': 'lyte',
        'HOST': 'db',
        'PORT': 5432,
    }
}

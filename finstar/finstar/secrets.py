DJANGO_SECRET_KEY = 'django-insecure-9b@-e-^$(0((blmmw0g7aw#k-uc-ii%yj^x-_n5-45(g(l3_f@'
DATABASE = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'finstar',
    'USER': 'admin',
    'PASSWORD': 'admin',
    'HOST': 'db', # Set to empty string for localhost.
    # 'HOST': '0.0.0.0', # Set to empty string for localhost.
    'PORT': '5432', # Set to empty string for default.
    }
}
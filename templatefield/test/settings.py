import os

INSTALLED_APPS = [
    'templatefield.test',
]

SECRET_KEY = 'secret'

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, 'testdb.sqlite')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DB,
        'TEST': {
            'NAME': DB,
        },
    },
}

MIDDLEWARE_CLASSES = ()

TEMPLATE_FIELD_CONTEXT = {'template_var': 'Dogs'}

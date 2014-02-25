import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'example.sqlite3'),
		'USER': '',
		'PASSWORD': '',
		'HOST': '',
		'PORT': '',
	}
}
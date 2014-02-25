# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = '**********'

ADMINS = (
	('Admin', '***'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ["*"]

TIME_ZONE = 'Europe/Zurich'

LANGUAGE_CODE = 'en'

LANGUAGES = [
	('en', 'English'),
]

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../../media/').replace('\\', '/'))
STATIC_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '../../static/').replace('\\', '/'))

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

ROOT_URLCONF = 'example.urls'

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
	'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.doc.XViewMiddleware',
	'django.middleware.common.CommonMiddleware',
	'cms.middleware.page.CurrentPageMiddleware',
	'cms.middleware.user.CurrentUserMiddleware',
	'cms.middleware.toolbar.ToolbarMiddleware',
	'cms.middleware.language.LanguageCookieMiddleware',

	'htmlmin.middleware.HtmlMinifyMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.contrib.messages.context_processors.messages',
	'django.core.context_processors.i18n',
	'django.core.context_processors.request',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'cms.context_processors.media',
	'sekizai.context_processors.sekizai',
)

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'templates'),
)

CMS_TEMPLATES = (
	('example/cms_templates/startseite.html', 'Startseite'),
)

THUMBNAIL_PROCESSORS = (
	'easy_thumbnails.processors.colorspace',
	'easy_thumbnails.processors.autocrop',
	'easy_thumbnails.processors.scale_and_crop',
	'easy_thumbnails.processors.filters',
)

INSTALLED_APPS = (
	'djangocms_admin_style',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sitemaps',
	'django.contrib.staticfiles',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',

	'djangocms_text_ckeditor',
	'cms',
	'mptt',
	'menus',
	'south',
	'sekizai',

	'easy_thumbnails',
	'widget_tweaks',
	'htmlmin',

	'example',
)

CKEDITOR_SETTINGS = {
	'language': '{{ language }}',
	'toolbar': 'HTMLField',
	'skin': 'moono',
	'toolbarCanCollapse': False,
	'allowedContent': True,
}

HTML_MINIFY = True

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'handlers': {
		'mail_admins': {
			'level': 'ERROR',
			'filters': ['require_debug_false'],
			'class': 'django.utils.log.AdminEmailHandler'
		}
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
	}
}

from example.settings_local import *
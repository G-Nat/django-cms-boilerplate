# -*- coding: utf-8 -*-
from django.contrib import admin
from django.conf import settings
from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from cms.sitemaps import CMSSitemap
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = i18n_patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('cms.urls')),
)

urlpatterns += patterns('',
	url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
	(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", mimetype="text/plain")),
)

if settings.DEBUG:
	urlpatterns = patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
		url(r'', include('django.contrib.staticfiles.urls')),
	) + urlpatterns
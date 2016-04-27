# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from simpleapp import urls

admin.autodiscover()


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(urls)),
]

urlpatterns = urlpatterns + \
              patterns('',
                       (r'^static/(?P<path>.*)$',
                        'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
                       ) if settings.DEBUG else urlpatterns

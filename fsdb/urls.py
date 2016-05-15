# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import FileViewDetail, FileViewList, SystemViewList, SystemViewDetail


urlpatterns = [
    # Categories
    # Directories

    # Systems
    url(r'^/system$', SystemViewList.as_view(), name='fsdb-system-list'),
    url(r'^/system/(?P<slug>.*)$', SystemViewDetail.as_view(), name='fsdb-system-detail'),

    # Files
    url(r'^$', FileViewList.as_view(), name='fsdb-file-list'),
    url(r'^(?P<path>.*)$', FileViewDetail.as_view(), name='fsdb-file-detail'),
]

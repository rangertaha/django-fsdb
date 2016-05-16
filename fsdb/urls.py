# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers

from .views import FileViewDetail, FileViewList, SystemViewList, \
    SystemViewDetail, FileAPIViewSet, SystemAPIViewSet, \
    ApplicationAPIViewSet, CategoryAPIViewSet, csv_download

router = routers.DefaultRouter()
router.register(r'files', FileAPIViewSet)
router.register(r'systems', SystemAPIViewSet)
router.register(r'applications', ApplicationAPIViewSet)
router.register(r'categories', CategoryAPIViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    # Categories
    # Directories

    # Systems
    url(r'^/system$', SystemViewList.as_view(), name='fsdb-system-list'),
    url(r'^/system/(?P<slug>.*)$', SystemViewDetail.as_view(), name='fsdb-system-detail'),

    # Files
    url(r'^filelist.csv$', csv_download, name='fsdb-csv-download'),
    url(r'^$', FileViewList.as_view(), name='fsdb-file-list'),
    url(r'^(?P<path>.*)$', FileViewDetail.as_view(), name='fsdb-file-detail'),




]




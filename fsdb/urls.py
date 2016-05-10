# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', FileViewList.as_view(), name='fsdb-file-list'),
    url(r'^(?P<path>.*)/$', FileViewDetail.as_view(), name='fsdb-file-detail'),

]

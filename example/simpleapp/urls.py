# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^$', include('fsdb.urls')),
]

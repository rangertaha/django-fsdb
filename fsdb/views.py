# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView

from .models import Application, File, Category


class ApplicationViewDetail(DetailView):
    model = Application


class ApplicationViewList(ListView):
    model = Application


class FileViewDetail(DetailView):
    model = File

    def get_object(self, queryset=None):
        return self.model.objects.get(active=True, path=self.kwargs.get(
            'path', None))


class FileViewList(ListView):
    model = File


class CategoryViewDetail(DetailView):
    model = Category


class CategoryViewList(ListView):
    model = Category

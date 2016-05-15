# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView

from .models import Application, File, Category, System


class ApplicationViewDetail(DetailView):
    model = Application


class ApplicationViewList(ListView):
    model = Application


class FileViewDetail(DetailView):
    model = File

    def get_object(self, queryset=None):
        return self.model.objects.get(
            active=True, path=self.kwargs.get('path', None))


class FileViewList(ListView):
    model = File
    paginate_by = 5

    def get_queryset(self):
        if self.request.GET.get('q'):
            return self.model.objects.filter(
                active=True,
                path__icontains=self.request.GET['q']).distinct()
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(FileViewList, self).get_context_data(**kwargs)
        context['systems'] = System.objects.filter().distinct()
        context['applications'] = Application.objects.filter().distinct()
        context['categories'] = Category.objects.filter().distinct()
        return context


class CategoryViewDetail(DetailView):
    model = Category


class CategoryViewList(ListView):
    model = Category


class SystemViewDetail(DetailView):
    model = System


class SystemViewList(ListView):
    model = System

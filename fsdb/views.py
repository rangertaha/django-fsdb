# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView

from .models import Application, File, Category


class ApplicationViewDetail(DetailView):
    model = Application


class ApplicationViewList(ListView):
    model = Application


class FileViewDetail(DetailView):
    model = File


class FileViewList(ListView):
    model = File


class CategoryViewDetail(DetailView):
    model = Category


class CategoryViewList(ListView):
    model = Category

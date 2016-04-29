# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView

from .models import Directory, File, Category


class DirectoryViewDetail(DetailView):
    model = Directory


class DirectoryViewList(ListView):
    model = Directory


class FileViewDetail(DetailView):
    model = File


class FileViewList(ListView):
    model = File


class CategoryViewDetail(DetailView):
    model = Category


class CategoryViewList(ListView):
    model = Category

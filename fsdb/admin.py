# -*- coding: utf-8 -*-
"""
"""
import logging

from django.contrib import admin

from .models import System, Application, File, Category

# Get an instance of a logger
logger = logging.getLogger(__name__)


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('rank', 'type', 'path', 'description')
    search_fields = ('rank', 'system', 'permissions', 'type', 'description', 'path')

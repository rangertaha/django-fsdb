# -*- coding: utf-8 -*-
"""
"""
import logging

from django.contrib import admin

from .models import Application, File, Category

# Get an instance of a logger
logger = logging.getLogger(__name__)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('rank', 'system', 'permissions', 'type', 'description')
    search_fields = ('rank', 'system', 'permissions', 'type', 'description')

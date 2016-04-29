# -*- coding: utf-8 -*-
"""
"""
import logging

from django.contrib import admin

from .models import Directory, File, Category

# Get an instance of a logger
logger = logging.getLogger(__name__)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(Directory)
class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('rank', 'system', 'permissions', 'name', 'description')
    search_fields = ('rank', 'system', 'permissions', 'name', 'description')
    '''
    list_editable = ('active', )
    list_display_links = ('id', 'name', 'description')
    raw_id_fields = ('pages',)
    sortable = 'order'
    ordering = ['order']
    '''


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('rank', 'system', 'permissions', 'type', 'name', 'description')
    search_fields = ('rank', 'system', 'permissions', 'type', 'name', 'description')

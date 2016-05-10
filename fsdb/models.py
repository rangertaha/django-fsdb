# -*- coding:utf-8 -*-
import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _
from elasticutils.contrib.django import MappingType

SYSTEMS = (
    ('linux', 'Linux Operating System'),
    ('unix', 'Unix Operating System'),
    ('windows', 'Microsoft Windows'),
)
FILE_TYPES = (
    ('linux', 'Linux Operating System'),
    ('unix', 'Unix Operating System'),
    ('windows', 'Microsoft Windows'),
)


class Application(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, unique=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class File(models.Model):
    rank = models.IntegerField(blank=True, null=True)
    system = models.CharField(max_length=512, choices=SYSTEMS, blank=True, null=True)
    applications = models.ManyToManyField(Application, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    permissions = models.CharField(max_length=512, blank=True, null=True)
    path = models.CharField(max_length=512, blank=True, null=True,
                            db_index=True)
    type = models.CharField(max_length=512, choices=FILE_TYPES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # Metadata
    created = models.DateTimeField(_('Created'), auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(_('Updated'), auto_now=False, auto_now_add=True)
    active = models.BooleanField(_('Active'), default=True)

    class Meta:
        ordering = ('rank',)

    def __unicode__(self):
        return self.name


class FileMappingType(MappingType):
    @classmethod
    def get_model(cls):
        return File

file_searcher = FileMappingType.search()

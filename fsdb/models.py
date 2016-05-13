# -*- coding:utf-8 -*-
import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

FILE_TYPES = (
    ('dir', 'Directory'),
    ('pfile', 'Physical File'),
    ('vfile', 'Virtual File'),
    ('link', 'Link'),
)

ICONS = (
    ('fa-linux ', 'Linux'),
    ('fa-windows ', 'Windows '),
    ('fa-apple ', 'Apple'),

    ('fa-firefox', 'Firefox'),
    ('fa-chrome ', 'Chrome'),
    ('fa-internet-explorer', 'Internet Explorer'),

    ('fa-file', 'Physical File'),
    ('fa-file-o', 'Virtual File'),


)


class System(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, unique=True)
    icon = models.CharField(max_length=32, choices=ICONS, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, unique=True)
    icon = models.CharField(max_length=32, choices=ICONS, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, unique=True)
    icon = models.CharField(max_length=32, choices=ICONS, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class File(models.Model):
    rank = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=48, choices=FILE_TYPES, blank=True, null=True)
    icon = models.CharField(max_length=32, choices=ICONS, blank=True, null=True)
    systems = models.ManyToManyField(System, blank=True)
    applications = models.ManyToManyField(Application, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    permissions = models.CharField(max_length=512, blank=True, null=True)
    path = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)

    # Metadata
    created = models.DateTimeField(_('Created'), auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(_('Updated'), auto_now=False, auto_now_add=True)
    active = models.BooleanField(_('Active'), default=False)

    class Meta:
        ordering = ('rank',)

    def __unicode__(self):
        return self.path

    @property
    def name(self):
        pass


@receiver(pre_save, sender=File)
def pre_file(sender, **kwargs):
    file = kwargs['instance']
    file.path = file.path.replace(' ', '.')

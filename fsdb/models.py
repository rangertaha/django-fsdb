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
    ('fa-linux', 'Linux'),
    ('fa-windows ', 'Windows'),
    ('fa-apple', 'Apple'),

    ('fa-firefox', 'Firefox'),
    ('fa-chrome ', 'Chrome'),
    ('fa-internet-explorer', 'Internet Explorer'),

    ('fa-file', 'Physical File'),
    ('fa-file-o', 'Virtual File'),

    ('fa-folder', 'Folder'),
    ('fa-folder-o', 'Folder White'),

)

EXTENSIONS = (
    ('pdf', '.pdf'),
    ('txt', '.txt'),
    ('sqlite', '.sqlite'),
    ('json', '.json'),
    ('db', '.db'),
    ('dat', '.dat'),

)


class System(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True, unique=True)
    slug = models.SlugField(max_length=32, blank=True, null=True, unique=True)
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
    rank = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=32, blank=True, null=True, unique=True)
    name = models.CharField(max_length=32, blank=True, null=True, unique=True)
    icon = models.CharField(max_length=32, choices=ICONS, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('rank', )
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class File(models.Model):
    rank = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=48, choices=FILE_TYPES, blank=True, null=True)
    icon = models.CharField(max_length=32, choices=ICONS, blank=True, null=True)
    system = models.ForeignKey(System, blank=True, related_name='files')
    applications = models.ManyToManyField(Application, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    permissions = models.CharField(max_length=512, blank=True, null=True)
    path = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    name = models.CharField(max_length=512, blank=True, null=True, db_index=True)
    extensions = models.CharField(max_length=512, choices=EXTENSIONS, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # Metadata
    created = models.DateTimeField(_('Created'), auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(_('Updated'), auto_now=False, auto_now_add=True)
    active = models.BooleanField(_('Active'), default=False)

    class Meta:
        ordering = ('rank',)

    def __unicode__(self):
        return self.path


@receiver(pre_save, sender=File)
def pre_file(sender, **kwargs):
    file = kwargs['instance']
    file.path = file.path.replace(' ', ' ')


@receiver(pre_save, sender=System)
def slugify_system_name(sender, **kwargs):
    system = kwargs['instance']
    if system.slug is None or system.slug is '':
        system.slug = slugify(system.name)


@receiver(pre_save, sender=Category)
def slugify_system_name(sender, **kwargs):
    category = kwargs['instance']
    if category.slug is None or category.slug is '':
        category.slug = slugify(category.name)

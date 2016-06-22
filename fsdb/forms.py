# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import File


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['system', 'applications', 'categories', 'path', 'description']
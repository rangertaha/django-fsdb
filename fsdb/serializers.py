# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import File, Category, Application, System


class FileSerializer(serializers.HyperlinkedModelSerializer):
    system = serializers.StringRelatedField(many=False)
    applications = serializers.StringRelatedField(many=True)
    categories = serializers.StringRelatedField(many=True)


    class Meta:
        model = File
        fields = ('rank', 'type', 'system', 'applications', 'categories',
                  'permissions', 'extensions', 'description', 'created',
                  'updated')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('rank', 'slug', 'name', 'description')


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Application
        fields = ('name', 'description')


class SystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = System
        fields = ('name', 'slug', 'description')




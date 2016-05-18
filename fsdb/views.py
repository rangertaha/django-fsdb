# -*- coding: utf-8 -*-
import csv

from django.utils.six.moves import range
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.views.generic import ListView, DetailView
from rest_framework import viewsets

from .models import Application, File, Category, System
from .serializers import FileSerializer, SystemSerializer, \
    CategorySerializer, ApplicationSerializer


class ApplicationViewDetail(DetailView):
    model = Application


class ApplicationViewList(ListView):
    model = Application


class FileViewDetail(DetailView):
    model = File

    def get_object(self, queryset=None):
        return self.model.objects.get(
            active=True, path=self.kwargs.get('path', None))

    def get_context_data(self, **kwargs):
        context = super(FileViewDetail, self).get_context_data(**kwargs)
        context['systems'] = System.objects.filter().distinct()
        context['applications'] = Application.objects.filter().distinct()
        context['categories'] = Category.objects.filter().distinct()
        return context


class FileViewList(ListView):
    model = File
    paginate_by = 5

    def get_queryset(self):
        if self.request.GET.get('q'):
            return self.model.objects.filter(
                active=True,
                path__icontains=self.request.GET['q']).distinct()
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(FileViewList, self).get_context_data(**kwargs)
        context['systems'] = System.objects.filter().distinct()
        context['applications'] = Application.objects.filter().distinct()
        context['categories'] = Category.objects.filter().distinct()
        return context


class CategoryViewDetail(DetailView):
    model = Category


class CategoryViewList(ListView):
    model = Category


class SystemViewDetail(DetailView):
    model = System


class SystemViewList(ListView):
    model = System


class FileAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = File.objects.all().order_by('-rank')
    serializer_class = FileSerializer


class SystemAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to b
    """
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class CategoryAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to b
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ApplicationAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to b
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer




def csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="filelist.csv"'

    writer = csv.writer(response)
    for f in File.objects.all():
        categories = [c.name for c in f.categories.all()]
        applications = [a.name for a in f.applications.all()]

        writer.writerow([f.rank, f.path, f.name, f.system, ','.join(applications), ','.join(categories), f.description.encode('utf-8')])

    return response

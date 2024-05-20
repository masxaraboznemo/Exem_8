import django_filters
from django.db.models import Q
from .models import Paper


class PaperFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author= django_filters.CharFilter(lookup_expr='icontains')
    keywords = django_filters.CharFilter(lookup_expr='icontains')
    

    class Meta:
        model = Paper
        fields = ['title', 'author', 'keywords']

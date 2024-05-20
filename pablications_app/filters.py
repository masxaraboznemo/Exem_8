import django_filters
from django.db.models import Q
from .models import Pablication


class PablicationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Pablication
        fields = ['name']

from rest_framework.viewsets import ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend
from .models import Paper
from .serializers import PaperSerializer
from .filters import PaperFilter


class PaperViewSet(ModelViewSet):
    queryset =Paper.objects.all()
    serializer_class = PaperSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaperFilter

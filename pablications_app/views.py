from .filters import PablicationFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PablicationSerializer

from .models import Pablication

from rest_framework.viewsets import ModelViewSet

class PablicationViewSet(ModelViewSet):
    queryset = Pablication.objects.all()
    serializer_class = PablicationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PablicationFilter
    
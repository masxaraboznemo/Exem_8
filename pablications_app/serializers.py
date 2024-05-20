from rest_framework import serializers

from .models import Pablication

class PablicationSerializer(serializers.Serializer):
    class Meta:
        model = Pablication
        fields = '__all__'

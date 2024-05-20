from rest_framework import serializers
from .models import Paper

class PaperSerializer(serializers.Serializer):
    class Meta:
        model = Paper
        fields = '__all__'
    
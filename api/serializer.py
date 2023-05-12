from rest_framework import serializers
from .models import Exam

class examSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    tipo = serializers.CharField(required=True)
    regional = serializers.CharField(required=True)

    class Meta:
        model = Exam
        fields = ('name', 'tipo', 'regional')
from rest_framework import serializers
from .models import ProgramApplication

class ProgramApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramApplication
        fields = '__all__'
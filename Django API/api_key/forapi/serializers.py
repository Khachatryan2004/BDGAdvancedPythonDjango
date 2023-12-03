from rest_framework import serializers
from .models import ForAPI


class ForAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = ForAPI
        fields = '__all__'


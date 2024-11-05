from account.models import *
from rest_framework import serializers

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
from rest_framework import serializers
from .models import *

class productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
from rest_framework import serializers
from .models import Contribute, Causes

class CausesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Causes
        fields = ['id', 'title', 'description', 'image_url', 'created_at', 'updated_at']

class ContributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribute
        fields = ['id', 'name', 'email', 'amount', 'causes', 'receipt_pdf', 'created_at']
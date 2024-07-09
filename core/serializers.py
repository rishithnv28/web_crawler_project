from rest_framework import serializers
from .models import CrawlRequest, CrawlResult

class CrawlRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawlRequest
        fields = '_all_'

class CrawlResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrawlResult
        fields = '_all_'
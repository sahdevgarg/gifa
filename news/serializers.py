from django.conf import settings
from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from news.models import News
import json

class NewsListingSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField()
	class Meta:
		model = News

	def get_url(self, obj):
		return obj.get_absolute_url()
		
class PageNewsListSerializer(PaginationSerializer):
	class Meta:
		object_serializer_class = NewsListingSerializer
	


	


from django.conf import settings
from rest_framework import serializers
from image.models import Image
from rest_framework.pagination import PaginationSerializer

class ImageListingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image

class PageImageListSerializer(PaginationSerializer):
	class Meta:
		object_serializer_class = ImageListingSerializer

	


	


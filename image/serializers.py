from django.conf import settings
from rest_framework import serializers
from image.models import Image
from rest_framework.pagination import PaginationSerializer

class ImageListingSerializer(serializers.ModelSerializer):
	user_name = serializers.SerializerMethodField()
	class Meta:
		model = Image
	def get_user_name(self,obj):
		return obj.user.first_name
class PageImageListSerializer(PaginationSerializer):
	class Meta:
		object_serializer_class = ImageListingSerializer

	


	


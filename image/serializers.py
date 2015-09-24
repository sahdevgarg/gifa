from django.conf import settings
from rest_framework import serializers
from image.models import Image
from rest_framework.pagination import PaginationSerializer

class ImageListingSerializer(serializers.ModelSerializer):
	user_name = serializers.SerializerMethodField()
	share_url = serializers.SerializerMethodField()
	class Meta:
		model = Image
		fields = ('id', 'user_name', 'title','image','user','share_url')

	def get_user_name(self,obj):
		try:
			return obj.user.first_name		
		except:
			return ""
	def get_share_url(self,obj):
		return "/gallery/"+str(obj.id)+".htm"
class PageImageListSerializer(PaginationSerializer):
	class Meta:
		object_serializer_class = ImageListingSerializer

	


	


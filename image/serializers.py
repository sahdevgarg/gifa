from django.conf import settings
from rest_framework import serializers
from image.models import Image
import json

class ImageListingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image

	


	


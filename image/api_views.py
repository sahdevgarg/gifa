from rest_framework import generics
from rest_framework.response import Response
from image.models import Image
from image.serializers import ImageListingSerializer

class ImagelistingApiView(generics.ListAPIView):
	model = Image
	def get(self, request, *args, **kwargs):
		image_list = Image.objects.filter(enabled=True)
		serializer = ImageListingSerializer(image_list, many=True)
		return Response({"result":serializer.data})

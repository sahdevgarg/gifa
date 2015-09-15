from rest_framework import generics
from rest_framework.response import Response
from django.core.paginator import Paginator
from image.models import Image
from image.serializers import PageImageListSerializer

class ImagelistingApiView(generics.ListAPIView):
	model = Image
	def get(self, request, *args, **kwargs):
		page = self.request.REQUEST.get('page', 1)
		no_records = self.request.REQUEST.get('no_records', 20)
		image_list = Image.objects.filter(enabled=True)
		paginator = Paginator(image_list, no_records)
		try:
			page = paginator.page(page)
		except:
			return Response({"result":"No data avialable for this page"})

		serializer_news = PageImageListSerializer(instance=page)
		return Response({"result":serializer_news.data})

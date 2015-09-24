from rest_framework import generics
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from django.core.paginator import Paginator
from image.models import Image
from gifa.views import JSONView
from image.serializers import PageImageListSerializer

class ImagelistingApiView(generics.ListAPIView):
	model = Image
	def get(self, request, *args, **kwargs):
		page = self.request.REQUEST.get('page', 1)
		no_records = self.request.REQUEST.get('no_records', 20)
		trivia = self.request.REQUEST.get('trivia', False)
		if trivia:
			image_list = Image.objects.filter(enabled=True,trivia=True).order_by('-modified_date');
		else:
			image_list = Image.objects.filter(enabled=True,trivia=False).order_by('-modified_date');
		paginator = Paginator(image_list, no_records)
		try:
			page = paginator.page(page)
		except:
			return Response({"result":"No data avialable for this page"})

		serializer_news = PageImageListSerializer(instance=page)
		return Response({"result":serializer_news.data,"trivia":trivia})

class ImageDisableApiView(JSONView):

    def get(self, *args, **kwargs):
		context = super(ImageDisableApiView, self).get_context_data(**kwargs)
		image_id = self.request.GET.get('image_id',"")
		try:
			news = Image.objects.filter(id=image_id).update(rejected=True,enabled=False);
			return HttpResponseRedirect('/')
		except:
			return HttpResponseRedirect('/')
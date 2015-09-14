from rest_framework import generics
from rest_framework.response import Response
from django.core.paginator import Paginator
from news.models import News
from news.serializers import PageNewsListSerializer,NewsListingSerializer
class NewsListApiView(generics.ListAPIView):
	model = News
	def get(self, request, *args, **kwargs):
		page = self.request.REQUEST.get('page', 1)
		no_records = self.request.REQUEST.get('no_records', 12)
		news_list = News.objects.filter(enabled=True)
		paginator = Paginator(news_list, no_records)
		page = paginator.page(page)
		serializer_news = PageNewsListSerializer(instance=page)
		return Response({"result":serializer_news.data})

class NewsDetailApiView(generics.ListAPIView):
	model = News
	def get(self, request, *args, **kwargs):
		news_id = request.REQUEST.get('news_id', None)
		try:
			news = News.objects.get(id=news_id,enabled=True)
		except :
			return Response({"result":"incorrect news_id"})
		serializer_news = NewsListingSerializer(news)
		return Response({"result":serializer_news.data})
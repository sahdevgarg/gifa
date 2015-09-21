from rest_framework import generics
from rest_framework.response import Response
from django.core.paginator import Paginator
from match.models import Match
from match.serializers import PageMatchListSerializer

class MatchlistingApiView(generics.ListAPIView):
	model = Match
	def get(self, request, *args, **kwargs):
		page = self.request.REQUEST.get('page', 1)
		no_records = self.request.REQUEST.get('no_records', 40)
		city = self.request.GET.get('city','Delhi')
		match_list = Match.objects.filter(enabled=True,city=city).order_by('schedule','match_no')
		paginator = Paginator(match_list, no_records)
		try:
			page = paginator.page(page)
		except:
			return Response({"result":"No data avialable for this page"})

		serializer_match = PageMatchListSerializer(instance=page)
		return Response({"result":serializer_match.data})

from rest_framework import generics
from rest_framework.response import Response
from teams.models import Teams
from teams.serializers import TeamsListingSerializer,TeamsDetailSerializer

class TeamsListApiView(generics.ListAPIView):
	model = Teams
	def get(self, request, *args, **kwargs):
		city = self.request.GET.get('city','Delhi')
		team_list = Teams.objects.filter(enabled=True,city=city)
		serializer = TeamsListingSerializer(team_list, many=True)
		return Response({"result":serializer.data,"city":city})

class TeamsDetailApiView(generics.ListAPIView):
	model = Teams
	def get(self, request, *args, **kwargs):
		team_id = request.REQUEST.get('team_id', None)
		try:
			news = Teams.objects.get(id=team_id,enabled=True)
		except :
			return Response({"result":"incorrect team id"})
		serializer = TeamsDetailSerializer(news)
		return Response({"result":serializer.data})
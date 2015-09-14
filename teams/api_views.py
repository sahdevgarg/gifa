from rest_framework import generics
from rest_framework.response import Response
from teams.models import Teams
from teams.serializers import TeamsListingSerializer
class TeamsListApiView(generics.ListAPIView):
	model = Teams
	def get(self, request, *args, **kwargs):
		team_list = Teams.objects.filter(enabled=True)
		serializer = TeamsListingSerializer(team_list, many=True)
		return Response({"result":serializer.data})

class TeamsDetailApiView(generics.ListAPIView):
	model = Teams
	def get(self, request, *args, **kwargs):
		team_id = request.REQUEST.get('team_id', None)
		try:
			news = Teams.objects.get(id=team_id,enabled=True)
		except :
			return Response({"result":"incorrect team id"})
		serializer = TeamsListingSerializer(news)
		return Response({"result":serializer.data})
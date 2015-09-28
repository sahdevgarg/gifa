from django.conf import settings
from rest_framework import serializers
from match.models import Match
from teams.serializers import TeamsListingSerializer
from rest_framework.pagination import PaginationSerializer

class MatchListingSerializer(serializers.ModelSerializer):
	team_a_name = serializers.SerializerMethodField()
	team_b_name = serializers.SerializerMethodField()
	winning_team = serializers.SerializerMethodField()
	
	class Meta:
		model = Match
	def get_team_a_name(self,obj):
		if obj.team_a:
			return obj.team_a.team_name
		else:
			return ""
	def get_team_b_name(self,obj):
		if obj.team_b:
			return obj.team_b.team_name
		else:
			return ""
	def get_winning_team(self,obj):
		if obj.winning_team:
			serialized = TeamsListingSerializer(instance=obj.winning_team)
			return serialized.data
		else:
			return None

class PageMatchListSerializer(PaginationSerializer):
	class Meta:
		object_serializer_class = MatchListingSerializer

	


	


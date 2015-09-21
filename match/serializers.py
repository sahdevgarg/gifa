from django.conf import settings
from rest_framework import serializers
from match.models import Match
from rest_framework.pagination import PaginationSerializer

class MatchListingSerializer(serializers.ModelSerializer):
	team_a_name = serializers.SerializerMethodField()
	team_b_name = serializers.SerializerMethodField()
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

class PageMatchListSerializer(PaginationSerializer):
	class Meta:
		object_serializer_class = MatchListingSerializer

	


	


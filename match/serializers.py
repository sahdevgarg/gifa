from django.conf import settings
from rest_framework import serializers
from match.models import Match
from rest_framework.pagination import PaginationSerializer

class MatchListingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Match

class PageMatchListSerializer(PaginationSerializer):
	class Meta:
		object_serializer_class = MatchListingSerializer

	


	


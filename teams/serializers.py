from django.conf import settings
from rest_framework import serializers
from teams.models import Teams
import json

class TeamsListingSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField()
	class Meta:
		model = Teams

	def get_url(self, obj):
		return obj.get_absolute_url()

class TeamsDetailSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField()
	class Meta:
		model = Teams

	def get_url(self, obj):
		return obj.get_absolute_url()
	


	


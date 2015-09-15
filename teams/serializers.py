from django.conf import settings
from rest_framework import serializers
from teams.models import Teams
from player.models import Player
from player.serializers import PlayerListingSerializer
import json

class TeamsListingSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField()
	class Meta:
		model = Teams

	def get_url(self, obj):
		return obj.get_absolute_url()

class TeamsDetailSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField()
	players = serializers.SerializerMethodField('get_team_player')
	class Meta:
		model = Teams

	def get_url(self, obj):
		return obj.get_absolute_url()
	
	def get_team_player(self,obj):
		player_list = Player.objects.filter(team=obj.id)
		serializer_player = PlayerListingSerializer(player_list,many=True)
		return serializer_player.data


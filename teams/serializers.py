from django.conf import settings
from rest_framework import serializers
from teams.models import Teams
from player.models import Player
from player.serializers import PlayerListingSerializer
import json

class TeamsListingSerializer(serializers.ModelSerializer):
	total_points = serializers.SerializerMethodField()
	class Meta:
		model = Teams
		fields = ('id', 'team_name','total_points','games_played','total_goal','pool_no','team_group','total_goal','total_goal_faced','win','loss','draw','team_manager')

	def get_url(self, obj):
		return obj.get_absolute_url()
	
	def get_total_points(self,obj):
		return obj.win * 3 - obj.loss

class TeamsDetailSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField()
	players = serializers.SerializerMethodField('get_team_player')
	class Meta:
		model = Teams
		fields = ('id', 'team_name','total_points','games_played','total_goal','total_goal','total_goal_faced','win','loss','draw','url','players')

	def get_url(self, obj):
		return obj.get_absolute_url()
	
	def get_team_player(self,obj):
		player_list = Player.objects.filter(team=obj.id)
		serializer_player = PlayerListingSerializer(player_list,many=True)
		return serializer_player.data

class WinteamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teams
		fields = ('id', 'team_name')
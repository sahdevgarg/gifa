from django.conf import settings
from rest_framework import serializers
from player.models import Player
import json

class PlayerListingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Player
		fields = ('name','total_goal','games_played')

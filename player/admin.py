from django.contrib import admin
from player.models import Player
from django.conf import settings


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name","email","team")
    search_fields = ['name','team__team_name']

admin.site.register(Player,PlayerAdmin)

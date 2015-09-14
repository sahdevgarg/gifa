from django.contrib import admin
from player.models import Player
from django.conf import settings


class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name","email")

admin.site.register(Player,PlayerAdmin)

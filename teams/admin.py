from django.contrib import admin
from teams.models import Teams
from django.conf import settings


class TeamAdmin(admin.ModelAdmin):
    list_display = ("team_name","team_manager","games_played","win","team_group","draw","loss",'city','pool_no')
    search_fields = ['team_name']
admin.site.register(Teams,TeamAdmin)

from django.contrib import admin
from teams.models import Teams,FeaturedTeams
from django.conf import settings


class TeamAdmin(admin.ModelAdmin):
    list_display = ("team_name","team_manager","games_played","win","team_group","draw","loss",'city','pool_no')
    search_fields = ['team_name']



class FeaturedAdmin(admin.ModelAdmin):
    model = FeaturedTeams
    list_display = ['get_team','enabled','get_group']
    search_fields = ['team']

    def get_team(self, obj):
        return obj.featured_teams.team_name
    def get_group(self, obj):
    	if obj.featured_teams.team_group == 1:
            return "senior"
        else:
            return "junior"

admin.site.register(FeaturedTeams,FeaturedAdmin)
admin.site.register(Teams,TeamAdmin)
from django.contrib import admin
from match.models import Match
from django.conf import settings
from teams.models import Teams 


class MatchAdmin(admin.ModelAdmin):
    list_display = ("match_no","team_a","team_b","venue","schedule","result_type","team_a_goal","team_b_goal","enabled","winning_team")

    def save_model(self, request, obj, form, change):
        super(MatchAdmin, self).save_model(request, obj, form, change)
        team_a = Teams.objects.get(id=obj.team_a.id)
        team_b = Teams.objects.get(id=obj.team_b.id)
        team_a.total_goal = team_a.total_goal + obj.team_a_goal
        team_b.total_goal = team_b.total_goal + obj.team_b_goal
        if obj.result_type == 2 or obj.result_type == 3:
            team_a.games_played = team_a.games_played + 1
            team_b.games_played = team_b.games_played + 1
            if obj.team_b_goal > obj.team_a_goal:
        		obj.winning_team = obj.team_b
            elif obj.team_b_goal == obj.team_a_goal:
        		obj.winning_team = None;
            else:
        		obj.winning_team = obj.team_a
        else:
        	obj.team_b_goal = 0
        	obj.team_a_goal = 0
        	obj.winning_team = None;
        team_a.save()
        team_b.save()
        obj.save();
 
admin.site.register(Match,MatchAdmin)
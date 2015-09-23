from django.contrib import admin
from match.models import Match
from django.conf import settings
from teams.models import Teams 
from django.db.models import Sum


class MatchAdmin(admin.ModelAdmin):
    list_display = ("match_no","team_a","team_b","venue","schedule","result_type","team_a_goal","team_b_goal","enabled","winning_team")
    search_fields = ['team_b','team_a']
    def save_model(self, request, obj, form, change):
        super(MatchAdmin, self).save_model(request, obj, form, change)
        team_a = Teams.objects.get(id=obj.team_a.id)
        team_b = Teams.objects.get(id=obj.team_b.id)
        if obj.result_type == 2 or obj.result_type == 3:
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
        obj.save();
        team_a.games_played = Match.objects.filter(team_a=team_a,result_type__in=[2,3]).count() + Match.objects.filter(team_b=team_a,result_type__in=[2,3]).count()
        team_b.games_played = Match.objects.filter(team_a=team_b,result_type__in=[2,3]).count() + Match.objects.filter(team_b=team_b,result_type__in=[2,3]).count()
        team_a.win = Match.objects.filter(winning_team=team_a,result_type=2).count()
        team_b.win = Match.objects.filter(winning_team=team_b,result_type=2).count()
        team_a.draw = Match.objects.filter(team_a=team_a,result_type=3).count() + Match.objects.filter(team_b=team_a,result_type=3).count()
        team_b.draw = Match.objects.filter(team_a=team_b,result_type=3).count() + Match.objects.filter(team_b=team_b,result_type=3).count()
        team_a.loss = team_a.games_played - team_a.win - team_a.draw
        team_b.loss = team_b.games_played - team_b.win - team_b.draw

        team_a_goal1 = (Match.objects.filter(team_a=team_a,result_type__in=[2,3]).aggregate(Sum('team_a_goal')))["team_a_goal__sum"]
        team_a_goal2 = (Match.objects.filter(team_b=team_a,result_type__in=[2,3]).aggregate(Sum('team_b_goal')))["team_b_goal__sum"]
        if not team_a_goal1:
            team_a_goal1 = 0;
        if not team_a_goal2:
            team_a_goal2 = 0;
        team_a.total_goal = team_a_goal1 + team_a_goal2

        team_a_goal_face1 = (Match.objects.filter(team_a=team_a,result_type__in=[2,3]).aggregate(Sum('team_b_goal')))["team_b_goal__sum"]
        team_a_goal_face2 = (Match.objects.filter(team_b=team_a,result_type__in=[2,3]).aggregate(Sum('team_a_goal')))["team_a_goal__sum"]
        if not team_a_goal_face1:
            team_a_goal_face1 = 0;
        if not team_a_goal2:
            team_a_goal_face2 = 0;
        team_a.total_goal_faced = team_a_goal_face1 + team_a_goal_face2
        
        team_b_goal1 = (Match.objects.filter(team_a=team_b,result_type__in=[2,3]).aggregate(Sum('team_a_goal')))["team_a_goal__sum"]
        team_b_goal2 = (Match.objects.filter(team_b=team_b,result_type__in=[2,3]).aggregate(Sum('team_b_goal')))["team_b_goal__sum"]
        if not team_b_goal1:
            team_b_goal1 = 0;
        if not team_b_goal2:
            team_b_goal2 = 0;
        team_b.total_goal = team_b_goal1 + team_b_goal2

        team_b_goal_face1 = (Match.objects.filter(team_a=team_b,result_type__in=[2,3]).aggregate(Sum('team_b_goal')))["team_b_goal__sum"]
        team_b_goal_face2 = (Match.objects.filter(team_b=team_b,result_type__in=[2,3]).aggregate(Sum('team_a_goal')))["team_a_goal__sum"]
        if not team_b_goal_face1:
            team_b_goal_face1 = 0;
        if not team_b_goal2:
            team_b_goal_face2 = 0;
        team_b.total_goal_faced = team_b_goal_face1 + team_b_goal_face2

        team_a.save();
        team_b.save();

admin.site.register(Match,MatchAdmin)
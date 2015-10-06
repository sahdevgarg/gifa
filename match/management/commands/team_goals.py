from django.core.management.base import BaseCommand
from django.conf import settings
from django.db.models import Count
from django.conf import settings
from django.db import models
from django.db.models import Sum
import os
import csv
from django.db import transaction
from teams.models import Teams
from match.models import Match
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
    	teams = Teams.objects.filter(enabled=True);
    	for team in teams:
	    	team_a_goal1 = (Match.objects.filter(team_a=team,result_type__in=[2,3]).aggregate(Sum('team_a_goal')))["team_a_goal__sum"]
	        team_a_goal2 = (Match.objects.filter(team_b=team,result_type__in=[2,3]).aggregate(Sum('team_b_goal')))["team_b_goal__sum"]
	        team_a_goal_face1 = (Match.objects.filter(team_a=team,result_type__in=[2,3]).aggregate(Sum('team_b_goal')))["team_b_goal__sum"]
        	team_a_goal_face2 = (Match.objects.filter(team_b=team,result_type__in=[2,3]).aggregate(Sum('team_a_goal')))["team_a_goal__sum"]
    		if not team_a_goal1:
    			team_a_goal1 = 0;
       		if not team_a_goal2:
       			team_a_goal2 = 0;
       		if not team_a_goal_face1:
       			team_a_goal_face1 = 0;
       		if not team_a_goal2:
       			team_a_goal_face2 = 0;
    		team.total_goal = team_a_goal1 + team_a_goal2
    		team.total_goal_faced = team_a_goal_face1 + team_a_goal_face2
    		print team_a_goal1,team_a_goal2;
    		team.save();
    	
from django.shortcuts import render
from teams.models import Teams
from player.models import Player
from match.models import Match
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse



# Create your views here.
class TeamsList(TemplateView):
	template_name = "team_listing.html"
	def get(self,*args, **kwargs):
		context = super(TeamsList, self).get_context_data(**kwargs)
		context["city"] = self.request.GET.get('city','Delhi')
		context["team_list"] = Teams.objects.filter(enabled=True,city=context["city"])
		return self.render_to_response(context)

class TeamdetailView(TemplateView):
	template_name = "team_detail.html"
	def get(self,*args, **kwargs):
		context = super(TeamdetailView, self).get_context_data(**kwargs)
		context["team"] = Teams.objects.get(id=context["team_id"]);
		context["match_list_a"] = Match.objects.filter(team_a=context["team"])
		print context["match_list_a"]
		context["match_list_b"] = Match.objects.filter(team_b=context["team"])
		print context["match_list_b"]
		context["player_list"] = Player.objects.filter(team=context["team_id"]);
		return self.render_to_response(context)

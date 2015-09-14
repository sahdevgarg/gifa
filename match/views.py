from django.shortcuts import render
from match.models import Match
from django.views.generic import TemplateView
import datetime
from django.shortcuts import render, HttpResponse

class MatchList(TemplateView):
	template_name = "match_listing.html"
	def get(self,*args, **kwargs):
		context = super(MatchList, self).get_context_data(**kwargs)
		context["match_list"] = Match.objects.filter(enabled=True,schedule__gte=datetime.datetime.now())
		print context["match_list"]
		return self.render_to_response(context)
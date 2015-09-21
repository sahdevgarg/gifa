from django.shortcuts import render
from match.models import Match
from django.views.generic import TemplateView
from datetime import date,datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, HttpResponse

class MatchList(TemplateView):
	template_name = "match_listing.html"
	def get(self,*args, **kwargs):
		context = super(MatchList, self).get_context_data(**kwargs)
		context["city"] = self.request.GET.get('city','Delhi')
		match_list = Match.objects.filter(enabled=True,match_date__gte=date.today(),city=context["city"]).order_by('schedule','match_no')
		paginator = Paginator(match_list, 40)
		page = self.request.GET.get('page',"")
		if page:
			context["match_list"] = paginator.page(page)
		else:
			context["match_list"] = paginator.page(1)
		context["page_list"] = paginator.page_range
		return self.render_to_response(context)

from django.shortcuts import render, HttpResponse, get_object_or_404
from django.conf import settings
from django.views.generic import TemplateView
from news.models import News,FeaturedNews
from teams.models import Teams
import simplejson


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    response_class = HttpResponse

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        response_kwargs['content_type'] = 'application/json'
        return self.response_class(
            self.convert_context_to_json(context),
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return simplejson.dumps(context)

class JSONView(JSONResponseMixin,TemplateView):
    def get_context_data(self, **kwargs):
        return kwargs

class IndexView(TemplateView):
    template_name = "index.html"
    def get(self,*args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['news_list'] = News.objects.filter(enabled=True).order_by('-modified_date')[:11]
        context["teams_list"] = Teams.objects.filter().order_by('-win')[:12]
        return self.render_to_response(context)

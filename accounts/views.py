from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from gifa.views import JSONView
from image.models import Image
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from news.models import News
from django.views.generic import TemplateView
from django.contrib import auth
import uuid

class Userview(JSONView):

    def post(self, request, *args, **kwargs):
    	context = self.get_context_data(**kwargs)
    	auth.logout(request)
    	data = request.POST
    	try:
    		user = get_user_model().objects.get(email=data["email"]);
        except ObjectDoesNotExist:
        	user = get_user_model().objects.create(username=data["name"],first_name=data["firstname"],last_name=data["lastname"],email=data["email"]);
        user.backend = "django.contrib.auth.backends.ModelBackend"
        auth.login(request, user)
        return self.render_to_response({"success":"True"})

	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(NewsImageview, self).dispatch(*args, **kwargs)

class Logoutview(JSONView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        auth.logout(request)
        return  HttpResponseRedirect('/')

class UserDetailView(TemplateView):
    template_name = "user_profile.html"
    def get(self,*args, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = get_user_model().objects.get(id=context["user_id"]);
        content = self.request.GET.get('content','news');
        context['content']=content;
        if self.request.user != user:
            return  HttpResponseRedirect('/')
        if content == "image":
            context["image_list"] = Image.objects.filter(user= self.request.user.id).order_by('-modified_date')
        else :
            context["news_list"] = News.objects.filter(user= self.request.user.id).order_by('-modified_date')
        return self.render_to_response(context)

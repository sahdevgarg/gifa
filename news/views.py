from django.shortcuts import render, HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from image.models import Image
from gifa.views import JSONView
from news.models import News
from teams.models import Teams
import uuid
import os

class NewsImageview(JSONView):

    def post(self, request, *args, **kwargs):
    	name = u'{name}.{ext}'.format(
            name=uuid.uuid4().hex,
            ext=os.path.splitext(request.FILES['image'].name)[1].strip('.')
        )
    	image_path = os.path.join(settings.MEDIA_ROOT, name)
    	media_path = os.path.join(settings.MEDIA_URL, name)
    	destination = open(image_path, 'wb+')
    	for chunk in request.FILES['image'].chunks():
		        destination.write(chunk)
        return HttpResponse("<script>top.$('.mce-btn.mce-open').parent().find('.mce-textbox').val('%s').closest('.mce-window').find('.mce-primary').click();</script>" % media_path)

	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(NewsImageview, self).dispatch(*args, **kwargs)
	
class Addarticleview(TemplateView):
	template_name = "add_article.html"
	def get(self,*args, **kwargs):
		context = super(Addarticleview, self).get_context_data(**kwargs)
		if not self.request.user.is_authenticated():
			return HttpResponseRedirect('/writer.htm')
		context["edit"] = False
		context["teams"] = Teams.objects.all();
		return  self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		data = request.POST
		user = get_user_model().objects.get(email=request.user.email)
		try:
			team_a = Teams.objects.get(id = data["Team1"])
		except:
			team_a = None
		try:
			team_b = Teams.objects.get(id = data["Team2"])
		except:
			team_b = None
		fb_id = request.POST.get('fb_id', False)
		preview = request.POST.get('preview', False)
		done = request.POST.get('done', False)
		submit = request.POST.get('save', False)
		name = u'{name}.{ext}'.format(
		    name=uuid.uuid4().hex,
		    ext=os.path.splitext(request.FILES['image'].name)[1].strip('.')
		)
		image_path = os.path.join(settings.MEDIA_ROOT, name)
		media_path = os.path.join(settings.MEDIA_URL, name)
		destination = open(image_path, 'wb+')
		slug = slugify(data["title"])
		for chunk in request.FILES['image'].chunks():
			destination.write(chunk)
		if preview:
			news = News.objects.create(title=data["title"],coverimage=media_path,content=data["news_content"],user=user,tags=data["tags"],seo_desc=data["seodesc"],team_a=team_a,team_b=team_b,slug=slug,enabled=False,fb_id=fb_id);
			image = Image.objects.get_or_create(title=data["title"],image=media_path,tags=data["tags"],team=team_a,user=user,enabled=False);
			return HttpResponseRedirect('/news/'+str(news.slug)+'/article'+str(news.id)+'.htm?preview=True')
		if done:
			news = News.objects.create(title=data["title"],coverimage=media_path,content=data["news_content"],user=user,tags=data["tags"],seo_desc=data["seodesc"],team_a=team_a,team_b=team_b,slug=slug,enabled=False,fb_id=fb_id);
			image = Image.objects.get_or_create(title=data["title"],image=media_path,tags=data["tags"],team=team_a,user=user,enabled=False);
			return HttpResponseRedirect('/profile/'+(self.request.user.first_name).lower()+'/'+str(self.request.user.id)+'.htm')
		if submit:
			news = News.objects.create(title=data["title"],coverimage=media_path,content=data["news_content"],user=user,tags=data["tags"],seo_desc=data["seodesc"],team_a=team_a,team_b=team_b,slug=slug,enabled=True,fb_id=fb_id);
			image = Image.objects.get_or_create(title=data["title"],image=media_path,tags=data["tags"],team=team_a,user=user,enabled=True);
			return HttpResponseRedirect('/news/'+str(news.slug)+'/article'+str(news.id)+'.htm')

	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(Addarticleview, self).dispatch(*args, **kwargs)

class Editarticleview(TemplateView):
	template_name = "add_article.html"
	def get(self,*args, **kwargs):
		context = super(Editarticleview, self).get_context_data(**kwargs)
		context["edit"] = True
		context["teams"] = Teams.objects.all();
		context["news"] = News.objects.get(id=context["news_id"]);
		if self.request.user == context["news"].user or self.request.user.is_superuser:
			return  self.render_to_response(context)
		else:
			return  HttpResponseRedirect("/")

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		data = request.POST
		done = request.POST.get('done', False)
		user = get_user_model().objects.get(email=request.user.email)
		try:
			team_a = Teams.objects.get(id = data["Team1"])
		except:
			team_a = None
		try:
			team_b = Teams.objects.get(id = data["Team2"])
		except:
			team_b = None
		fb_id = request.POST.get('fb_id', False)
		try:
			team_b = Teams.objects.get(id = data["Team2"])
		except:
			team_b = None
		slug = slugify(data["title"])
		news_obj = News.objects.get(id=data["news_id"])

		if request.POST.get("image",False):
			name = u'{name}.{ext}'.format(
			    name=uuid.uuid4().hex,
			    ext=os.path.splitext(request.FILES['image'].name)[1].strip('.')
			)
			image_path = os.path.join(settings.MEDIA_ROOT, name)
			media_path = os.path.join(settings.MEDIA_URL, name)
			destination = open(image_path, 'wb+')
			for chunk in request.FILES['image'].chunks():
				destination.write(chunk)
		else:
			media_path = news_obj.coverimage
		preview = request.POST.get('preview', False)
		submit = request.POST.get('save', False)
		if preview:
			news = News.objects.filter(id=data["news_id"]).update(title=data["title"],coverimage=media_path,content=data["news_content"],tags=data["tags"],seo_desc=data["seodesc"],team_a=team_a,team_b=team_b,slug=slug,enabled=False,rejected=False);
			return HttpResponseRedirect('/news/'+str(news_obj.slug)+'/article'+str(news_obj.id)+'.htm?preview=True')
		if submit:
			news = News.objects.filter(id=data["news_id"]).update(title=data["title"],coverimage=media_path,content=data["news_content"],tags=data["tags"],seo_desc=data["seodesc"],team_a=team_a,team_b=team_b,slug=slug,enabled=True,rejected=False);
			return HttpResponseRedirect('/news/'+str(news_obj.slug)+'/article'+str(news_obj.id)+'.htm')
		if done:
			news = News.objects.filter(id=data["news_id"]).update(title=data["title"],coverimage=media_path,content=data["news_content"],tags=data["tags"],seo_desc=data["seodesc"],team_a=team_a,team_b=team_b,slug=slug,enabled=False,rejected=False);
			return HttpResponseRedirect('/profile/'+(self.request.user.first_name).lower()+'/'+str(self.request.user.id)+'.htm')
	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(Editarticleview, self).dispatch(*args, **kwargs)


class NewsdetailView(TemplateView):
	template_name = "news_detail.html"
	def get_context_data(self,*args, **kwargs):
		context = super(NewsdetailView, self).get_context_data(**kwargs)
		context["news"] = News.objects.get(id=context["news_id"]);
		if self.request.user.is_superuser or self.request.user ==context["news"].user:
			context["preview"] = self.request.GET.get('preview', "")
		else:
			context["preview"] = "";
		if self.request.user.is_superuser:
		 	context["preview"] = True

		return context

class SaveNews(JSONView):

    def get(self, *args, **kwargs):
		context = super(SaveNews, self).get_context_data(**kwargs)
		news_id = self.request.GET.get('news_id',"")
		try:
			news = News.objects.filter(id=news_id).update(enabled=True);
			news_obj = News.objects.get(id=news_id);
			return HttpResponseRedirect('/news/'+str(news_obj.slug)+'/article'+str(news_obj.id)+'.htm')
		except:
			return HttpResponseRedirect('/')

class RejectNews(JSONView):

    def get(self, *args, **kwargs):
		context = super(RejectNews, self).get_context_data(**kwargs)
		news_id = self.request.GET.get('news_id',"")
		try:
			news = News.objects.filter(id=news_id).update(rejected=True,enabled=False);
			return HttpResponseRedirect('/approve-article.htm')
		except:
			return HttpResponseRedirect('/')

class NewsList(TemplateView):
	template_name = "news_listing.html"
	def get(self,*args, **kwargs):
		context = super(NewsList, self).get_context_data(**kwargs)
		news_list = News.objects.filter(enabled=True).order_by('-modified_date')
		paginator = Paginator(news_list, 10)
		page = self.request.GET.get('page',"")
		if page:
			context["news_list"] = paginator.page(page)
		else:
			context["news_list"] = paginator.page(1)
		context["page_list"] = paginator.page_range
		return self.render_to_response(context)


class NewsapprovalView(TemplateView):
	template_name = "news_approval.html"
	def get(self,*args, **kwargs):
		context = super(NewsapprovalView, self).get_context_data(**kwargs)
		if not self.request.user.is_superuser:
			return HttpResponseRedirect('/') 
		news_list = News.objects.filter(enabled=False,rejected=False).order_by('-modified_date')
		paginator = Paginator(news_list, 10)
		page = self.request.GET.get('page',"")
		if page:
			context["news_list"] = paginator.page(page)
		else:
			context["news_list"] = paginator.page(1)
		context["page_list"] = paginator.page_range
		return self.render_to_response(context)



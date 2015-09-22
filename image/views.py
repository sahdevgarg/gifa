from django.shortcuts import render, HttpResponse
from teams.models import Teams
from image.models import Image
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.views.generic import TemplateView
from django.core.files import File
from gifa.views import JSONView
import uuid
import os

# Create your views here.

class MobileImageUpload(JSONView):

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
		Image.objects.create(title=request.POST["title"],image=media_path,enabled=False);
		return HttpResponse("Your Image has been uploaded")

	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(MobileImageUpload, self).dispatch(*args, **kwargs)


class Imageview(TemplateView):
	template_name = "upload_image.html"
	def get(self,*args, **kwargs):
		context = super(Imageview, self).get_context_data(**kwargs)
		if not self.request.user.is_authenticated():
			return HttpResponseRedirect('/writer.htm?image=true')
		context["teams"] = Teams.objects.all();
		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		data = request.POST
		try:
			team = Teams.objects.get(id = data["Team1"])
		except:
			team = None
		user = get_user_model().objects.get(email=request.user.email)
		done = request.POST.get('done', False)
		submit = request.POST.get('save', False)
		fb_id = request.POST.get('fb_id', False)
		name = u'{name}.{ext}'.format(
	        name=uuid.uuid4().hex,
	        ext=os.path.splitext(request.FILES['image'].name)[1].strip('.')
	    )
		image_path = os.path.join(settings.MEDIA_ROOT, name)
		media_path = os.path.join(settings.MEDIA_URL, name)
		destination = open(image_path, 'wb+')
		for chunk in request.FILES['image'].chunks():
		        destination.write(chunk)
		if submit:
			news = Image.objects.create(title=data["title"],image=media_path,tags=data["tags"],team=team,user=user);
			return HttpResponseRedirect('/gallery.htm')
		if done:
			news = Image.objects.create(title=data["title"],image=media_path,tags=data["tags"],team=team,user=user,enabled=False,fb_id=fb_id);
			return HttpResponseRedirect('/profile/'+(self.request.user.first_name).lower()+'/'+str(self.request.user.id)+'.htm')
	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(Imageview, self).dispatch(*args, **kwargs)

class ImageListview(TemplateView):
	template_name = "gallery.html"
	def get(self,*args, **kwargs):
		context = super(ImageListview, self).get_context_data(**kwargs)
		image_list = Image.objects.filter(enabled=True).order_by('-modified_date');
		paginator = Paginator(image_list, 20)
		page = self.request.GET.get('page',"")
		try:
			context["image_list"]  = paginator.page(page)
		except:
			context["image_list"]  = paginator.page(1)
		context["page_list"] = paginator.page_range
		return self.render_to_response(context)

class ImageapprovalView(TemplateView):
	template_name = "image_approval.html"
	def get(self,*args, **kwargs):
		context = super(ImageapprovalView, self).get_context_data(**kwargs)
		if not self.request.user.is_superuser:
			return HttpResponseRedirect('/') 
		image_list = Image.objects.filter(enabled=False,rejected=False).order_by('-modified_date')
		paginator = Paginator(image_list, 10)
		page = self.request.GET.get('page',"")
		if page:
			context["image_list"] = paginator.page(page)
		else:
			context["image_list"] = paginator.page(1)
		context["page_list"] = paginator.page_range
		return self.render_to_response(context)

class ImageDetail(TemplateView):
	template_name = "image_detail.html"
	def get(self,*args, **kwargs):
		context = super(ImageDetail, self).get_context_data(**kwargs)
		try:
			context["image"] = Image.objects.get(enabled=True,id=context["image_id"])
		except:
			return HttpResponseRedirect('/')
	
		return self.render_to_response(context)


class SaveImage(JSONView):

    def get(self, *args, **kwargs):
		context = super(SaveImage, self).get_context_data(**kwargs)
		image_id = self.request.GET.get('image_id',"")
		try:
			image = Image.objects.filter(id=image_id).update(enabled=True);
			return HttpResponseRedirect('/approve-image.htm')
		except:
			return HttpResponseRedirect('/')

class RejectImage(JSONView):

    def get(self, *args, **kwargs):
		context = super(RejectImage, self).get_context_data(**kwargs)
		image_id = self.request.GET.get('image_id',"")
		try:
			image = Image.objects.filter(id=image_id).update(rejected=True,enabled=False);
			return HttpResponseRedirect('/approve-image.htm')
		except:
			return HttpResponseRedirect('/')
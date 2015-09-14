from django.shortcuts import render, HttpResponse
from teams.models import Teams
from image.models import Image
from match.models import Match
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.views.generic import TemplateView
from django.core.files import File
import uuid
import os

# Create your views here.


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
		team = Teams.objects.get(id = data["Team1"])
		user = get_user_model().objects.get(email=request.user.email)
		name = u'{name}.{ext}'.format(
	        name=uuid.uuid4().hex,
	        ext=os.path.splitext(request.FILES['image'].name)[1].strip('.')
	    )
		image_path = os.path.join(settings.MEDIA_ROOT, name)
		media_path = os.path.join(settings.MEDIA_URL, name)
		destination = open(image_path, 'wb+')
		for chunk in request.FILES['image'].chunks():
		        destination.write(chunk)
		news = Image.objects.create(title=data["title"],image=media_path,tags=data["tags"],team=team,user=user);
		return HttpResponseRedirect('/gallery.htm')
	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(Imageview, self).dispatch(*args, **kwargs)

class ImageListview(TemplateView):
	template_name = "gallery.html"
	def get(self,*args, **kwargs):
		context = super(ImageListview, self).get_context_data(**kwargs)
		context["image_list"] = Image.objects.all();
		return self.render_to_response(context)

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from contact.models import Contact
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ContactView(TemplateView):
	template_name = "contact.html"
	def get(self,*args, **kwargs):
		context = super(ContactView, self).get_context_data(**kwargs)
		return  self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		email = request.POST.get('email', False)
		title = request.POST.get('title', False)
		message = request.POST.get('message', False)
		contact = Contact.objects.create(title=title,email=email,message=message)
		return HttpResponseRedirect('/thankyou.htm')

	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(ContactView, self).dispatch(*args, **kwargs)

class ContactlistView(TemplateView):
	template_name = "query_list.html"
	def get(self,*args, **kwargs):
		context = super(ContactlistView, self).get_context_data(**kwargs)
		if not self.request.user.is_superuser:
			return HttpResponseRedirect('/') 
		query_list = Contact.objects.filter().order_by('-created_date')
		paginator = Paginator(query_list, 20)
		page = self.request.GET.get('page',"")
		if page:
			context["query_list"] = paginator.page(page)
		else:
			context["query_list"] = paginator.page(1)
		context["page_list"] = paginator.page_range
		return self.render_to_response(context)



		return  self.render_to_response(context)
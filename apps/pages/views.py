
#encoding:utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader,TemplateDoesNotExist
from django.core.urlresolvers import reverse

from apps.pages.models import Blocks
from apps.pages.models import MenuItems
from django.contrib.sites.models import Site



from django.conf import settings

def custom_page(request,slug,page=1):	
	menu_item=get_object_or_404(MenuItems,slug=slug)
	#load custom template
	template_name='pages/%s.html' % slug
	try:
		loader.get_template(template_name)
	except TemplateDoesNotExist:
		template_name="pages/default.html"
	context_vars=dict(MenuItems=menu_item,Slug=slug,page=page)
	return render_to_response(template_name,context_instance = RequestContext(request,context_vars))


def handler404(request):
	context_vars=dict()
	response =  render_to_response('pages/404.html',context_instance = RequestContext(request,context_vars))
	#response.status_code = 404
	return response

def home(request,page=1):
	context_vars=dict(Slug='',MenuItems='',page=page)
	return render_to_response('pages/home.html',context_instance = RequestContext(request,context_vars))



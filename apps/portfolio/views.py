
#encoding:utf-8

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader,TemplateDoesNotExist
from django.core.urlresolvers import reverse

from apps.portfolio.models import PortfolioCategories,PortfolioItems
import json as simplejson



def portfolio(request,page=1):
	context_vars=dict(Slug='',MenuItems='',page=page)
	return render_to_response('pages/portfolio.html',context_instance = RequestContext(request,context_vars))

def portfolio_get_item(request):
	item=PortfolioItems.objects.get(id=request.GET.get('id',1))
	
	return HttpResponse(simplejson.dumps(item.encode_myway())
		, mimetype='application/json')





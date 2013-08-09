# Create your views here.
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.dispatch import receiver
from django.middleware import csrf
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext,loader,TemplateDoesNotExist
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from apps.budgets.models import Categories,Budget

def budget(request):
	categories=Categories.objects.all().order_by('-name')
	itemlist=list()
	for category in categories:
		budgets=Budget.objects.filter(category_id=category.id)
		itemlist.append(dict(categories=category,budgets=budgets))
		
	context_vars=dict(itemlist=itemlist)
	return render_to_response('budgets/budget.html',context_instance = RequestContext(request,context_vars))

#encoding:utf-8
import os
import sys
import shutil

from django.shortcuts import render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext
from apps.config.forms import GlobalConfigForm
from django.conf import settings


@staff_member_required
def home(request,slug=''):
	context_vars=dict(
		GlobalConfigForm=GlobalConfigForm()
	)	
	return render_to_response('config/app_index.html',context_instance = RequestContext(request,context_vars))

def save_global_config(request):
	if request.method == 'POST':
		form=GlobalConfigForm(request.POST,request=request)
		context_vars=dict(
		GlobalConfigForm=form
		)
		if form.is_valid():
			form.write_config()
	
		else:
			return render_to_response('config/app_index.html',context_instance = RequestContext(request,context_vars))
	admin_url=reverse("admin:config_home", kwargs=dict())
	return HttpResponseRedirect(admin_url)


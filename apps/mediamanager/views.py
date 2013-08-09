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
from django.template.defaultfilters import slugify
from apps.mediamanager.forms import MediaManagerUploadForm
from django.conf import settings


is_true = lambda value: bool(value) and value.lower() not in ('false', '0')
# custom functions
def handle_uploaded_file(f,file_path):
    with open(file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def getSlug(slug):
	if  len(slug)>0 and slug[len(slug)-1] == "/":
		slug=slug.strip("/")
	if  len(slug)>0 and slug[len(slug)-1] != "/":
		slug='%s/'%slug
	return slug

@staff_member_required
def mediamanager(request,slug=''):
	slug=str(slug)
	dir_path=os.path.join(settings.MEDIA_ROOT,'uploads')
	dir_path=os.path.join(dir_path,slug)
	slug=getSlug(slug)
	breadcrumb_list=slug.split('/')
	breadcrumbs=list()
	i=0
	for breadcrumb_item in breadcrumb_list:		
		if len(breadcrumb_item)>0:
			item_admin_url= str('/'.join(breadcrumb_list[:-2]))
			i=i+1
			breadcrumbs.append(dict(index=i,parent_url=item_admin_url,current_item=breadcrumb_item))

	if os.path.exists(dir_path):
		files=list()
		directories=list()

		for archive in os.listdir(dir_path):
			archive_path=os.path.join(dir_path,archive)
			if(len(archive)>10):
				filename=archive[:10]+"..."
			else:
				filename=archive
			item=dict(name=archive,filename=filename)
			if os.path.isdir(archive_path) == True:
				item.update(dict(slug=slug+archive))
				directories.append(item)
			else:				
				files.append(item)
		

		context_vars=dict(
			breadcrumbs=breadcrumbs,
			files=files,
			directories=directories,
			slug=slug,
			upload_form=MediaManagerUploadForm(),
			dir_exists=True,
			is_popup=is_true(request.GET.get('popup','False'))
		)	
	else:
		context_vars=dict(dir_exists=False)	

	return render_to_response('mediamanager/app_index.html',context_instance = RequestContext(request,context_vars))

@staff_member_required
def create_directory(request,slug=''):
	slug=str(slug)	
	dir_path=os.path.join(settings.MEDIA_ROOT,'uploads')
	if(len(slug)>0):
		dir_path=os.path.join(dir_path,slug)
	if request.method == 'POST':
		directory_name=slugify(request.POST.get('name',''))
		if len(directory_name)>0:
			dir_path=os.path.join(dir_path,directory_name)
			if not os.path.exists(dir_path):
				os.mkdir(dir_path)
	slug=slug.strip("/")
	
	admin_url=reverse("admin:mediamanager", kwargs=dict(slug=slug))
	is_popup=is_true(request.GET.get('popup','False'))
	if is_popup== True:
            admin_url=admin_url+'?popup=True'
	return HttpResponseRedirect(admin_url)

@staff_member_required
def upload_file(request,slug=''):
	slug=str(slug)	
	dir_path=os.path.join(settings.MEDIA_ROOT,'uploads')
	if(len(slug)>0):
		dir_path=os.path.join(dir_path,slug)
	if request.method == 'POST':
		for key, file in request.FILES.items():			
			filename=os.path.splitext(file.name)
			filename=slugify(filename[0])+filename[1]
			file_path=os.path.join(dir_path,filename)
			if os.path.exists(dir_path) and not os.path.exists(file_path):
				handle_uploaded_file(file,file_path)
	slug=slug.strip("/")
	admin_url=reverse("admin:mediamanager", kwargs=dict(slug=slug))
	is_popup=is_true(request.GET.get('popup','False'))
	if is_popup== True:
            admin_url=admin_url+'?popup=True'
	return HttpResponseRedirect(admin_url)

@staff_member_required
def delete_files(request,slug='',filename=''):
	slug=str(slug)
	slug=slug.strip("/")
	dir_path=os.path.join(settings.MEDIA_ROOT,'uploads')
	if(len(slug)>0):
		dir_path=os.path.join(dir_path,slug)
	dir_path=os.path.join(dir_path,filename)
	if os.path.exists(dir_path):
		if os.path.isdir(dir_path):
			shutil.rmtree(dir_path)
		else:
			os.remove(dir_path)		
	
	admin_url=reverse("admin:mediamanager", kwargs=dict(slug=slug))
	is_popup=is_true(request.GET.get('popup','False'))
	if is_popup== True:
            admin_url=admin_url+'?popup=True'
	return HttpResponseRedirect(admin_url)

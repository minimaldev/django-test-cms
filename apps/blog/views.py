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
from apps.blog.models import *
from apps.blog.forms import BlogCommentsForm,SearchForm



#render comment form
def comment_form(request,Notice):
	CommentForm=BlogCommentsForm()
	if request.method == 'POST':
		CommentForm.data = request.POST.copy()
		CommentForm.is_bound = True
		if CommentForm.is_valid():
			CommentForm.instance.notice=Notice
			CommentForm.save()
	return 	CommentForm	
#render template
def blog_template(request,context_vars):
	template_name='blog/%s.html' % context_vars['Notice'].slug
	try:
		loader.get_template(template_name)
	except TemplateDoesNotExist:
		template_name="blog/notice.html"
	return render_to_response(template_name,context_instance = RequestContext(request,context_vars))


def video_template(request,context_vars):
	template_name='video/%s.html' % context_vars['Video'].slug
	try:
		loader.get_template(template_name)
	except TemplateDoesNotExist:
		template_name="video/video.html"
	return render_to_response(template_name,context_instance = RequestContext(request,context_vars))

#Rss
def rss(request):
	context_vars=dict(Articles=BlogNotice.objects.filter(publish=True,is_in_feed=True).order_by('-id'))	
	return render_to_response('blog/rss.xml',mimetype="text/xml",context_instance = RequestContext(request,context_vars))


def articles(request,page=1):
	limit=request.GET.get('limit',settings.LIST_ITEMS_PER_PAGE)
	articles  = list(BlogNotice.objects.filter(publish=True).order_by('-id'))
	paginator = Paginator(articles, limit)
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	context_vars=dict(page=page,Articles=articles
		,Slug='',
		MenuItems=None)	
	return render_to_response('blog/articles.html',context_instance = RequestContext(request,context_vars))

def article_details(request,slug,id=None,year=None,month=None,day=None):
	#check if Notice exits
	if  ((id is not None ) 
		and (year is None ) 
		and (month is None ) 
		and (day is None )):
		Notice=get_object_or_404(BlogNotice,publish=True,id=id,slug=slug)
	
	if  ((id is None ) 
		and (year is None ) 
		and (month is None ) 
		and (day is None )):
		Notice=get_object_or_404(BlogNotice,publish=True,slug=slug)

	if  ((id is None ) 
		and (year is not None ) 
		and (month is not None ) 
		and (day is not None )):		
		Notice=get_object_or_404(BlogNotice,
			publish=True,
			slug=slug,
			created__year = year,
			created__month = month,
			created__day = day)

	if  ((id is not None ) 
		and (year is not None ) 
		and (month is not None ) 
		and (day is not None )):
		Notice=get_object_or_404(BlogNotice,
			publish=True,
			id=id,
			slug=slug,
			created__year = year,
			created__month = month,
			created__day = day)

	#render comment form
	CommentForm=comment_form(request,Notice)
	#template variables
	context_vars=dict(Breadcrumb_last_item=Notice.title,
					  Notice=Notice,
					  MenuItems=Notice.menu_item,
					  Slug=Notice.menu_item.slug,
					  ArticleSlug=Notice.slug,
					  CommentForm=CommentForm)
	#render template
	return blog_template(request,context_vars)


def articles_tag(request,slug):
	articles=BlogNotice.objects.filter(publish=True,tags__slug=slug).order_by('-id')
	context_vars=dict(tag_articles=articles,Slug='',MenuItems=None)
	return render_to_response('blog/tags.html',context_instance = RequestContext(request,context_vars))

def article_search(request):
	#search
	if request.method == 'GET':
		form=SearchForm(request.GET)
		if form.is_valid():
			search=str(form.cleaned_data['s'])
			articles=list(BlogNotice.objects.filter(title__istartswith=search).order_by('-id'))
		else:
			articles=list()
	else:
		articles=list()
	context_vars=dict(search_articles=articles,Slug='',MenuItems=None)
	return render_to_response('blog/search.html',context_instance = RequestContext(request,context_vars))


def videos(request,page=1):
	limit=request.GET.get('limit',settings.LIST_VIDEO_ITEMS_PER_PAGE)
	videos = list(BlogVideo.objects.filter(publish=True).order_by('-id'))
	paginator = Paginator(videos, limit)
	try:
		videos = paginator.page(page)
	except PageNotAnInteger:
		videos = paginator.page(1)
	except EmptyPage:
		videos = paginator.page(paginator.num_pages)
	
	context_vars=dict(
		page=page,
		Videos=videos,
		Slug='',
		MenuItems=None)	
	return render_to_response('video/videos.html',context_instance = RequestContext(request,context_vars))

def video_details(request,slug,id=None,year=None,month=None,day=None):
	#check if Notice exits
	if  ((id is not None ) 
		and (year is None ) 
		and (month is None ) 
		and (day is None )):
		Video=get_object_or_404(BlogVideo,publish=True,id=id,slug=slug)
	
	if  ((id is None ) 
		and (year is None ) 
		and (month is None ) 
		and (day is None )):
		Video=get_object_or_404(BlogVideo,publish=True,slug=slug)

	if  ((id is None ) 
		and (year is not None ) 
		and (month is not None ) 
		and (day is not None )):
		Video=get_object_or_404(BlogVideo,
			publish=True,
			slug=slug,
			created__year = year,
			created__month = month,
			created__day = day)

	if  ((id is not None ) 
		and (year is not None ) 
		and (month is not None ) 
		and (day is not None )):
		Video=get_object_or_404(BlogVideo,
			publish=True,
			id=id,
			slug=slug,
			created__year = year,
			created__month = month,
			created__day = day)

	#render comment form

	#template variables
	context_vars=dict(Breadcrumb_last_item=Video.title,
					  Video=Video,
					  MenuItems=Video.menu_item,
					  Slug=Video.menu_item.slug,
					  ArticleSlug=Video.slug)
	#render template
	return video_template(request,context_vars)
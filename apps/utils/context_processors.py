#encoding:utf-8
from django.conf import settings
from apps.pages.models import Blocks
from apps.pages.models import MenuItems
from apps.blog.models.blogcategories import BlogCategories
from apps.blog.models.blogtags import BlogTags
from apps.blog.models.blognotice import BlogNotice
from apps.blog.models.blogvideo import BlogVideo
from django.utils.timezone import utc
import os
import sys
import simplejson as json

def static_site_domain(request):
	globconfigfile=os.path.join(settings.CUSTOM_CONFIG_ROOT,'site.json')
	if os.path.exists(globconfigfile):
		filename=open(globconfigfile).read()
		globalconfig = json.loads(filename)
		return dict(SITE_DOMAIN=globalconfig['site_domain'],
			SITE_NAME=globalconfig['site_name'],
			SITE_DESCRIPTION=globalconfig['site_description']
			)
	return dict(SITE_DOMAIN='',SITE_NAME='')

def sitemap(request):

	if request.path == '/sitemap.xml':
		itemlist=[]
		blog_notices=BlogNotice.objects.filter().order_by('-id')
		blog_tags=BlogTags.objects.filter().order_by('-id')
		menu_items=MenuItems.objects.filter().order_by('-id')
		datelist=[]
		if len(blog_notices)>0:
			datelist.append(blog_notices[0].modified)
			itemlist.append(blog_notices)

		if len(blog_tags)>0:
			datelist.append(blog_tags[0].modified)
			itemlist.append(blog_tags)

		if len(menu_items)>0:
			datelist.append(menu_items[0].modified)
			itemlist.append(menu_items)
		if len(datelist)>0:
			return dict(LASTUPDATE=max(datelist) ,itemlist=itemlist)
	if request.path == '/post-sitemap.xml':
		return dict(articles=BlogNotice.objects.filter().order_by('-id'))
	if request.path == '/post_tag-sitemap.xml':
		return dict(tags=BlogTags.objects.filter().order_by('-id'))
	if request.path == '/section-sitemap.xml':
		return dict(menuitems= MenuItems.objects.filter().order_by('-id'))
	if request.path == '/video-sitemap.xml':
		return dict(menuitems=BlogVideo.objects.filter().order_by('-id')) 

	return dict()


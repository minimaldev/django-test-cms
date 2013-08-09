


from apps.blog.models.blogvideo import BlogVideo
from apps.blog.forms import SearchForm
from django.db.models import Count
from django import template
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

register = template.Library()

@register.inclusion_tag('video/templatetags/videos_list.html', takes_context = True)
def video_page_list_tag(context,limit=settings.LIST_VIDEO_ITEMS_PER_PAGE): 
	#page = context['request'].GET.get('page',1)
	page = context['page']
	slug=context['Slug']
	videos  = list(BlogVideo.objects.filter(publish=True,menu_item__slug=slug).order_by('-id'))
	paginator = Paginator(articles, limit)
	try:
		videos = paginator.page(page)
	except PageNotAnInteger:
		videos = paginator.page(1)
	except EmptyPage:
		videos = paginator.page(paginator.num_pages)
	return {'videos': videos,'slug':'/'+slug}

@register.inclusion_tag('video/templatetags/videos_list.html', takes_context = True)
def video_page_list_home_tag(context,limit=settings.LIST_VIDEO_ITEMS_PER_PAGE): 
	#page = context['request'].GET.get('page',1)
	page = context['page']
	slug = ''
	videos = list(BlogVideo.objects.filter(publish=True).order_by('-id'))
	paginator = Paginator(videos, limit)
	try:
		videos = paginator.page(page)
	except PageNotAnInteger:
		videos = paginator.page(1)
	except EmptyPage:
		videos = paginator.page(paginator.num_pages)
	return {'videos': videos}


@register.inclusion_tag('video/templatetags/videos_archive_list.html', takes_context = True)
def list_archived_videos(context,limit=settings.LIST_VIDEO_ITEMS_PER_PAGE):
	archive_videos= list()
	archive_videos_year = list(BlogVideo.objects.all().dates('created', 'year').order_by('-created')[:limit])
	for years in archive_videos_year:
		archive_videos.append({'year':years.year,'items':list(BlogVideo.objects.filter(publish=True,created__year = years.year))})	
	return {'archive_videos': archive_videos}

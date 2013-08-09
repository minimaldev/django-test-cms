

from apps.blog.models.blogtags import BlogTags
from apps.blog.models.blognotice import BlogNotice
from apps.blog.models.blogcomments import BlogComments
from apps.blog.forms import SearchForm
from django.db.models import Count
from django import template
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

register = template.Library()

@register.inclusion_tag('blog/templatetags/articles_list.html', takes_context = True)
def article_page_list_tag(context,limit=5): 
	#page = context['request'].GET.get('page',1)
	page = context['page']
	slug=context['Slug']
	articles  = list(BlogNotice.objects.filter(publish=True,menu_item__slug=slug).order_by('-id'))
	paginator = Paginator(articles, limit)
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return {'articles': articles,'slug':'/'+slug}

@register.inclusion_tag('blog/templatetags/articles_list.html', takes_context = True)
def article_page_list_home_tag(context,limit=5): 
	#page = context['request'].GET.get('page',1)
	page = context['page']
	slug = ''
	articles  = list(BlogNotice.objects.filter(publish=True).order_by('-id'))
	paginator = Paginator(articles, limit)
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		articles = paginator.page(paginator.num_pages)
	return {'articles': articles}


@register.inclusion_tag('blog/templatetags/articles_archive_list.html', takes_context = True)
def list_archived_articles(context,limit=10):
	archive_articles= list()
	archive_articles_year = list(BlogNotice.objects.all().dates('created', 'year').order_by('-created')[:limit])
	for years in archive_articles_year:
		archive_articles.append({'year':years.year,'items':list(BlogNotice.objects.filter(publish=True,created__year = years.year))})	
	return {'archive_articles': archive_articles}

@register.inclusion_tag('blog/templatetags/popular_tags.html', takes_context = True)
def list_top_article_tags(context):
	tags = list(BlogNotice.objects.values('tags__name','tags__slug').all().annotate(score=Count('tags')).order_by('-score'))
	return {'tags': tags}

@register.inclusion_tag('blog/templatetags/comment_list.html', takes_context = True)
def list_article_comments(context):
	slug=context['ArticleSlug']
	comments = list(BlogComments.objects.filter(notice__slug=slug))
	return {'comments': comments}

@register.inclusion_tag('blog/templatetags/recents_comments_list.html', takes_context = True)
def list_article_global_recent_comments(context,limit=5):
	comments = list(BlogComments.objects.select_related().all().order_by('-created')[:limit])
	return {'comments': comments}

@register.inclusion_tag('blog/templatetags/search_form.html', takes_context = True)
def article_search_form(context):
	return {'form': SearchForm}

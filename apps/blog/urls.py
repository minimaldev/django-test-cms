from django.conf.urls import patterns, url

urlpatterns = patterns('apps.blog.views',
	url(r'^articles/page/(?P<page>\d+)/$', 'articles'),
	url(r'^articles/$', 'articles'),
	url(r'^rss/$', 'rss'),
	url(r'^articles/search/$', 'article_search'),
	url(r'^articles/tag/(?P<slug>[0-9A-Za-z-_]+)/$', 'articles_tag'),
	url(r'^articles/(?P<year>\d+)/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<id>\d+)/(?P<slug>[0-9A-Za-z-_]+)/$', 'article_details'),
 	url(r'^articles/(?P<year>\d+)/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[0-9A-Za-z-_]+)/$', 'article_details'),
    url(r'^articles/(?P<id>\d+)/(?P<slug>[0-9A-Za-z-_]+)/$', 'article_details'),
    url(r'^articles/(?P<slug>[0-9A-Za-z-_]+)/$', 'article_details'),
    url(r'^videos/page/(?P<page>\d+)/$', 'videos'),
	url(r'^videos/$', 'videos'),
   	url(r'^videos/(?P<year>\d+)/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<id>\d+)/(?P<slug>[0-9A-Za-z-_]+)/$', 'video_details'),
 	url(r'^videos/(?P<year>\d+)/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[0-9A-Za-z-_]+)/$', 'video_details'),
    url(r'^videos/(?P<id>\d+)/(?P<slug>[0-9A-Za-z-_]+)/$', 'video_details'),
    url(r'^videos/(?P<slug>[0-9A-Za-z-_]+)/$', 'video_details')
  )
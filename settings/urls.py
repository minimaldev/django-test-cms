from django.conf import settings
from django.conf.urls import *
from django.conf.urls.static import static
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


handler404 = 'apps.pages.views.handler404'
urlpatterns =  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + patterns('',
	#url(r'^admin/', include(my_admin_site.urls ) ),
	url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
	url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap/sitemap.xml', content_type='text/plain')),
	url(r'^post-sitemap\.xml$', TemplateView.as_view(template_name='sitemap/post-sitemap.xml', content_type='text/plain')),
	url(r'^video-sitemap\.xml$', TemplateView.as_view(template_name='sitemap/video-sitemap.xml', content_type='text/plain')),
	url(r'^post_tag-sitemap\.xml$', TemplateView.as_view(template_name='sitemap/post_tag-sitemap.xml', content_type='text/plain')),
	url(r'^section-sitemap\.xml$', TemplateView.as_view(template_name='sitemap/section-sitemap.xml', content_type='text/plain')),
    url(r'^admin/', include(admin.site.urls ) ),
    url(r'^portfolio/', include('apps.portfolio.urls')),
    url(r'^', include('apps.blog.urls')),
    url(r'^page/(?P<page>\d+)/$', 'apps.pages.views.home', name='home'),
    url(r'^$', 'apps.pages.views.home', name='home'),
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/page/(?P<page>\d+)/$', 'apps.pages.views.custom_page', name='pages_root'),
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', 'apps.pages.views.custom_page', name='pages_root'),
   
) 

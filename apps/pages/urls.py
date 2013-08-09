from django.conf.urls import patterns, url

urlpatterns = patterns('apps.pages.views',
	
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', 'custom_page', name='pages_root'),
    )
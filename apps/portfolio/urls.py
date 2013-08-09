from django.conf.urls import patterns, url

urlpatterns = patterns('apps.portfolio.views',
	
    url(r'^get$', 'portfolio_get_item', name='portfolio_get_item'),
)
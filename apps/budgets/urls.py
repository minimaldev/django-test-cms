from django.conf.urls import patterns, url

urlpatterns = patterns('apps.budgets.views',
	url(r'^presupuesto/solicitar/$', 'budget'),
)
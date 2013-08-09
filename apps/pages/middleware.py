from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import get_callable

class PagesMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        #if not request.path.startswith(reverse('admin:index')):
        #if not request.path.startswith(reverse('home')):
        #    view_func=get_callable('apps.pages.views.home')
        return view_func(request, *view_args, **view_kwargs)

#def process_view(self, request, view_func, view_args, view_kwargs):
#       module = modules[view_func.__module__]
#       prefilter_func_name = 'prefilter'
#       if hasattr(module, prefilter_func_name):
#           prefilter_func = getattr(module, prefilter_func_name)
#           response = prefilter_func(request, view_func, view_args, view_kwargs)
#           if response:
#               return response
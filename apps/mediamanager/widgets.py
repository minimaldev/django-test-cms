from django.utils.safestring import mark_safe
from django.forms import widgets
from django.core.urlresolvers import reverse, NoReverseMatch
# your custom widget class
class MediaItemWidget(widgets.TextInput):
    def render(self, name, value, attrs=None):
    	mediamanager_url=reverse("admin:mediamanager")
    	myfield='<a href="%s?popup=True" style="vertical-align:top;" id="%s"  class="selectmediaItem btn btn-primary"><i class="icon-search icon-white"></i> Select File</a>&nbsp;' % (mediamanager_url,name)
        return mark_safe(u''' %s %s''' 
        	% (myfield,super(MediaItemWidget, self).render(name, value, attrs)))

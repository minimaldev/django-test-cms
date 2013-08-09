from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter
from apps.pages.models import Blocks
class MenuBynameListFilter(SimpleListFilter):
    title = _('Categorias')
    parameter_name = 'category'
    def lookups(self, request, model_admin): 
        ActiveCactegories=[]
        for menu in Blocks.objects.all():        
        	ActiveCactegories.append((menu.id,menu.name))
        return tuple(ActiveCactegories)
    def queryset(self, request, queryset):
    	if(self.value()==None):
    		return queryset.filter()
    	if(self.value()!=None):
    		return queryset.filter(menu__id=self.value())
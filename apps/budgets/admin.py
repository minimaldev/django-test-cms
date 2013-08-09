from django.utils import timezone
from apps.budgets.models import Categories,Budget
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class PresupuestoBudgetAdmin(admin.ModelAdmin):
#   class Media:
#       js = ('/js/copytitle.js',)
   fieldsets = [(_('Basic'),{'fields': ['name','days','price','is_selectable']}),
   				
                (_('Category'),{'fields': ['category']}),
        ]
   list_display = ('name','category', 'days','price','created','modified')
   search_fields = ['name','days','price']
   def save_model(self, request, obj, form, change):
   	current_time= timezone.now()
   	if getattr(obj, 'id', None) is None:
   		obj.created=current_time
   	obj.modified=current_time
   	if getattr(obj, 'user', None) is None:
   		obj.user = request.user
   	obj.save()

class PresupuestoCategoriesAdmin(admin.ModelAdmin):
   fieldsets = [(_('Basic'),{'fields': ['name']}),
   		(_('Autor'),{'fields': ['user']}),
        ]
   list_display = ('name', 'created','modified')
   search_fields = ['name',]
   def save_model(self, request, obj, form, change):
   	current_time= timezone.now()
   	if getattr(obj, 'id', None) is None:
   		obj.created=current_time
   	obj.modified=current_time
   	if getattr(obj, 'user', None) is None:
   		obj.user = request.user
   	obj.save()



admin.site.register(Budget,PresupuestoBudgetAdmin)
admin.site.register(Categories,PresupuestoCategoriesAdmin)

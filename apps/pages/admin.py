from django.utils import timezone
from django.contrib import admin
from apps.pages.models import Blocks,MenuItems
from mptt.admin import MPTTModelAdmin
from apps.pages.filters import MenuBynameListFilter
from apps.pages.forms import AdminMenuItemsForm
from django.utils.translation import ugettext_lazy as _


class MenusAdmin(admin.ModelAdmin):
  
  fieldsets = [(_('Basic'),{'fields': ['name']}),
               (_('Autor'),{'fields': ['user']}),
			]
  list_display = ('name','created','modified')
  search_fields = ['name']
  
  def save_model(self, request, obj, form, change):
    current_time= timezone.now()
    if getattr(obj, 'id', None) is None:
      obj.created=current_time
    obj.modified=current_time
    if getattr(obj, 'user', None) is None:
      obj.user = request.user
    obj.save()
#   list_filter = ('name', 'hits')

class MenuItemsAdmin(MPTTModelAdmin):

  class Media:
    js = (
      '/media/static/js/copytitle.js',
      '/media/static/js/mediamanager/mediamanager_field.js',
      )
  
  fieldsets = [(_('Basic'),{'fields': ['block','parent','title','publish','thumb','description']}),
              (_('Item'),{'fields': ['menu_type','item_id']}),

              (_('Autor'),{'fields': ['user']}),
              (_('Seo'), {'fields': ['slug','metatitle','metadescription']})
			]
  
  list_display = ('title', 'parent','publish','created','modified','id')
  search_fields = ['title']
  prepopulated_fields = {'slug':('title',)}
  list_filter = (MenuBynameListFilter,)
  form = AdminMenuItemsForm
  
  def save_model(self, request, obj, form, change):
    current_time= timezone.now()
    if getattr(obj, 'id', None) is None:
      obj.created=current_time
    obj.modified=current_time
    if getattr(obj, 'user', None) is None:
      obj.user = request.user
    obj.save()

admin.site.register(Blocks,MenusAdmin)
admin.site.register(MenuItems,MenuItemsAdmin)
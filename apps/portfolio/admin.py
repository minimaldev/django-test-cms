from django.utils import timezone
from django.contrib import admin
from apps.portfolio.models import PortfolioCategories,PortfolioItems
from mptt.admin import MPTTModelAdmin
from apps.portfolio.forms import AdminPortfolioItemsForm
from django.utils.translation import ugettext_lazy as _


class PortfolioCategoriesAdmin(MPTTModelAdmin):
  class Media:
    js = (
      '/media/static/js/copytitle.js',
    )
  fieldsets = [(_('Basic'),{'fields': ['name']}),
               (_('Autor'),{'fields': ['user']}), 
              (_('Seo'), {'fields': ['slug','metatitle','metadescription']})     
			]
  prepopulated_fields = {'slug':('name',)}
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


class PortfolioItemsAdmin(admin.ModelAdmin):

  class Media:
    js = (
      '/media/static/js/copytitle.js',
      '/media/static/js/mediamanager/mediamanager_field.js',
      )
  
  fieldsets = [(_('Basic'),{'fields': ['parent','title','link','publish','thumb','featured_image','description']}),
              (_('Autor'),{'fields': ['user']}),
              (_('Seo'), {'fields': ['slug','metatitle','metadescription']})
			]
  
  list_display = ('title', 'parent','publish','created','modified','id')
  search_fields = ['title']
  prepopulated_fields = {'slug':('title',)}
  form = AdminPortfolioItemsForm
  
  def save_model(self, request, obj, form, change):
    current_time= timezone.now()
    if getattr(obj, 'id', None) is None:
      obj.created=current_time
    obj.modified=current_time
    if getattr(obj, 'user', None) is None:
      obj.user = request.user
    obj.save()

admin.site.register(PortfolioCategories,PortfolioCategoriesAdmin)
admin.site.register(PortfolioItems,PortfolioItemsAdmin)
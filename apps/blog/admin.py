from django.utils import timezone
from apps.blog.models import *
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from apps.blog.forms import AdminBlogCategoriesForm,AdminBlogNoticesForm
from django.contrib import messages
from django.conf import settings

class BlogNoticeAdmin(admin.ModelAdmin):

  class Media:
    js = (
      '/media/static/js/tiny_mce/tiny_mce.js', 
      '/media/static/js/textareas.js',
      '/media/static/js/mediamanager/mediamanager_field.js',
      '/media/static/js/copytitle.js',
    )
  fieldsets = [ #(_('Social'),{'fields': ['send_tweet','send_facebook_message']}),
                (_('Basic'),{'fields': ['title','video','excerpt','content','publish','is_in_feed','is_featured','thumb','featured_image']}),
                (_('Tags'),{'fields': ['tags']}),
                (_('Categories'),{'fields': ['categories']}),  
                (_('Related Articles'),{'fields': ['relatednotices']}),
                (_('Related Videos'),{'fields': ['relatedvideos']}),
                (_('Date'),{'fields': ['publishdate','featured_start_date','featured_end_date']}),
                (_('Autor'),{'fields': ['user']}),
                (_('Seo'),{'fields': ['slug','metatitle','metadescription']}),
        ]
  list_display = ('title','is_in_feed', 'created','modified')
  search_fields = ['title','user__email']
  prepopulated_fields = {'slug':('title',)}
  form = AdminBlogNoticesForm
  def save_model(self, request, obj, form, change):
    current_time= timezone.now()
    if getattr(obj, 'id', None) is None:
       obj.created=current_time
    obj.modified=current_time
    if getattr(obj, 'user', None) is None:
      obj.user = request.user
    obj.save()


class BlogVideoAdmin(admin.ModelAdmin):

  class Media:
    js = (
      '/media/static/js/tiny_mce/tiny_mce.js', 
      '/media/static/js/textareas.js',
      '/media/static/js/mediamanager/mediamanager_field.js',
      '/media/static/js/copytitle.js',
    )
  fieldsets = [ #(_('Social'),{'fields': ['send_tweet','send_facebook_message']}),
                (_('Basic'),{'fields': ['title','video','excerpt','content','publish','is_in_feed','is_featured','thumb','featured_image']}),
                (_('Tags'),{'fields': ['tags']}),
                (_('Categories'),{'fields': ['categories']}),  
                (_('Related Articles'),{'fields': ['relatednotices']}),
                (_('Related Videos'),{'fields': ['relatedvideos']}),
                (_('Date'),{'fields': ['publishdate','featured_start_date','featured_end_date']}),
                (_('Autor'),{'fields': ['user']}),
                (_('Seo'),{'fields': ['slug','metatitle','metadescription']}),
        ]
  list_display = ('title','is_in_feed', 'created','modified')
  search_fields = ['title','user__email']
  prepopulated_fields = {'slug':('title',)}
  form = AdminBlogNoticesForm
  def save_model(self, request, obj, form, change):
    current_time= timezone.now()
    if getattr(obj, 'id', None) is None:
      obj.created=current_time
    obj.modified=current_time
    if getattr(obj, 'user', None) is None:
      obj.user = request.user
    obj.save()


#categories
class BlogCategoriesAdmin(admin.ModelAdmin):
  class Media:
    js = ('/media/static/js/copytitle.js',)
  fieldsets = [(_('Basic'),{'fields': ['title','parent']}),
                (_('Autor'),{'fields': ['user']}),
        ]
  list_display = ('title', 'created','modified')
  search_fields = ['title','user__email']
  #prepopulated_fields = {'slug':('title',)}
  form = AdminBlogCategoriesForm  
  def save_model(self, request, obj, form, change):
    current_time= timezone.now()
    if getattr(obj, 'id', None) is None:
      obj.created=current_time
    obj.modified=current_time
    if getattr(obj, 'user', None) is None:
      obj.user = request.user
    obj.save()

#manufacturers
class BlogTagsAdmin(admin.ModelAdmin):
  class Media:
    js = ('/media/static/js/copytitle.js',)
  fieldsets = [(_('Basic'),{'fields': ['name']}),
        (_('Autor'),{'fields': ['user']}),
        (_('Seo'),{'fields': ['slug','metatitle','metadescription']}),
        ]
  list_display = ('name', 'created','modified')
  search_fields = ['name','user__email']
  prepopulated_fields = {'slug':('name',)}
  def save_model(self, request, obj, form, change):
    current_time= timezone.now()
    if getattr(obj, 'id', None) is None:
      obj.created=current_time
      obj.modified=current_time
    if getattr(obj, 'user', None) is None:
      obj.user = request.user
    obj.save()



#register the admin
admin.site.register(BlogNotice,BlogNoticeAdmin)
admin.site.register(BlogVideo,BlogVideoAdmin)
admin.site.register(BlogCategories,BlogCategoriesAdmin)
admin.site.register(BlogTags,BlogTagsAdmin)

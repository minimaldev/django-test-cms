from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#import menu items many to many
from apps.pages.models import MenuItems
from mptt.models import MPTTModel, TreeForeignKey
from apps.blog import image
from django.utils.translation import ugettext_lazy as _


#encoding:utf-8

class BlogCategories(MPTTModel):
  #relationship
  user= models.ForeignKey(User,verbose_name=_('User autor'),related_name='blog_categories_autor', null=True,blank=True)
  parent = TreeForeignKey('self',verbose_name=_('Parent'),null=True, blank=True, on_delete=models.CASCADE,related_name='blog_categories_parent')      
  #menu_item  = models.ManyToManyField(MenuItems,verbose_name=_('Menu Item'),related_name='blog_related_categories_menu_items',null=True,blank=True)

  #Basic 
  title = models.CharField(_('Title'),max_length=125)
#  thumb = models.ImageField(_('Thumb'),upload_to='images',blank=True,null=True)
#  publish = models.BooleanField(_('Published'),default=1)
#  description = models.TextField(_('Description'),blank=True)
  #seo
  #slug = models.CharField(_('Slug'),max_length=255,unique=True,blank=True)
  #metatitle =  models.CharField(_('Meta Title'),max_length=125,blank=True)
  #metadescription = models.TextField(_('Meta Description'),max_length=156,blank=True)
  #hidden 
  created = models.DateTimeField(_('Created'),editable=False)
  modified = models.DateTimeField(_('Modified'),editable=False)

  def __unicode__(self):
    return self.title

  class MPTTMeta:
      order_insertion_by = ['title']

  class Meta:
    verbose_name = _('Category')
    verbose_name_plural = _('Categories')
    get_latest_by = "created"
    ordering = ('lft',)
    db_table = 'blog_categories'
    app_label= 'blog'

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

#encoding:utf-8
class Blocks(models.Model):

   #relationship
   user = models.ForeignKey(User,verbose_name=_('User autor'),related_name='menu_menu_autor', null=True,blank=True)
   #basic
   name = models.CharField(_('Name'),max_length=125)
   #hidden
   created = models.DateTimeField(_('Created'),editable=False)
   modified = models.DateTimeField(_('Modified'),editable=False)
   

   def __unicode__(self):
      return self.name
   
   class Meta:
      verbose_name = _('Block')
      verbose_name_plural = _('Blocks')
      get_latest_by = "lft"
      db_table = 'menu_blocks'
      app_label= 'pages'

class MenuItems(MPTTModel):

   #relationship
   user = models.ForeignKey(User,verbose_name=_('User autor'),related_name='menu_menu_items_autor', null=True,blank=True)
   block = models.ForeignKey(Blocks,related_name='menu_menu_items_menu')        
   parent = TreeForeignKey('self',verbose_name=_('Parent'),null=True, blank=True, related_name='menu_menu_items_menu_parent')      
   #basic
   menu_type = models.CharField(_('Menu Type'),max_length=125)
   item_id = models.IntegerField(_('Select Item'),max_length=125)
   title = models.CharField(_('Title'),max_length=125)
   description = models.TextField(_('Description'),blank=True)
   thumb = models.ImageField(_('Thumb'),upload_to='images',blank=True,null=True)
   publish = models.BooleanField(_('Published'),default=1)
   #seo
   slug = models.CharField(_('Slug'),max_length=255,unique=True,blank=True)
   metatitle =  models.CharField(_('Meta Title'),max_length=125,blank=True)
   metadescription = models.TextField(_('Meta Description'),max_length=156,blank=True)
   #hidden
   created = models.DateTimeField(_('Created'),editable=False)
   modified = models.DateTimeField(_('Modified'),editable=False)

   
   def __unicode__(self):
		return self.title

   class MPTTMeta:
         order_insertion_by = ['title']  

   class Meta:
      verbose_name = _('Menu Item')
      verbose_name_plural = _('Menu Items')
      db_table = 'menu_items'
      app_label= 'pages'
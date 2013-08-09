from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _

#encoding:utf-8
class PortfolioCategories(MPTTModel):

   #relationship
   user = models.ForeignKey(User,verbose_name=_('User autor'),related_name='portfolio_categories_autor', null=True,blank=True)
   parent = TreeForeignKey('self',verbose_name=_('Parent'),null=True, blank=True, related_name='portfolio_categories_items_categories_parent')      
   #basic
   name = models.CharField(_('Name'),max_length=125)
   #basic
   slug = models.CharField(_('Slug'),max_length=255,unique=True,blank=True)
   metatitle =  models.CharField(_('Meta Title'),max_length=125,blank=True)
   metadescription = models.TextField(_('Meta Description'),max_length=156,blank=True)
   #hidden
   created = models.DateTimeField(_('Created'),editable=False)
   modified = models.DateTimeField(_('Modified'),editable=False)
   
   class MPTTMeta:
         order_insertion_by = ['name']  

   def __unicode__(self):
      return self.name
   
   class Meta:
      verbose_name = _('Category')
      verbose_name_plural = _('Categories')
      get_latest_by = "lft"
      db_table = 'portfolio_categories'
      app_label= 'portfolio'

class PortfolioItems(models.Model):
   #relationship
   user = models.ForeignKey(User,verbose_name=_('User autor'),related_name='portfolio_items_autor', null=True,blank=True)
   parent = models.ForeignKey(PortfolioCategories, blank=True,null=True,verbose_name=_('Parent'))
   #basic
   title = models.CharField(_('Title'),max_length=125)
   link = models.URLField(blank=True)
   description = models.TextField(_('Description'),blank=True)
   thumb = models.TextField(_('Thumbnail'),blank=True,null=True)
   featured_image = models.TextField(_('Featured Image'),blank=True,null=True)
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


   class Meta:
      verbose_name = _('Portfolio Item')
      verbose_name_plural = _('Portfolio Items')
      db_table = 'portfolio_items'
      app_label= 'portfolio'
   def encode_myway(self):
      return {'id':self.id,
      'title':str(self.title),
      'description':str(self.description),
      'link':str(self.link),
      'featured_image':str(self.thumb)}
  
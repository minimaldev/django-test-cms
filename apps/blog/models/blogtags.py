from django.utils import timezone
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
#encoding:utf-8
class BlogTags(models.Model):
  #Relationship
  user= models.ForeignKey(User,verbose_name=_('User autor'),related_name='blog_tags_autor', null=True,blank=True)
  #basic
  name = models.CharField(_('Tag'),max_length=125,unique=True)
  #seo
  slug = models.SlugField(_('Slug'),max_length=255,unique=True,blank=True)
  metatitle =  models.CharField(_('Meta Title'),max_length=125,blank=True)
  metadescription = models.TextField(_('Meta Description'),max_length=156,blank=True)
  #hidden
  created = models.DateTimeField(_('Created'),editable=False)
  modified = models.DateTimeField(_('Modified'),editable=False)

  def __unicode__(self):
    return self.name
  
  class Meta:
    
    verbose_name = _('Blog Tag')
    verbose_name_plural = _('Blog Tags')
    get_latest_by = "created"
    db_table = 'blog_tags'
    app_label= 'blog'

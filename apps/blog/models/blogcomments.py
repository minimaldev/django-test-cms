from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
#from caching.base import CachingMixin,CachingManager
#encoding:utf-8
class BlogComments(MPTTModel):
  #relationship
  user= models.ForeignKey(User,verbose_name=_('User autor'),related_name='blog_comments_autor', null=True,blank=True)
  notice = models.ForeignKey('BlogNotice', blank=True,null=True,verbose_name=_('Blog Notice'))
  parent = TreeForeignKey('self', verbose_name=_('Parent'), related_name='blog_comments_parent',blank=True, null=True, on_delete=models.CASCADE)
  #basic
  email = models.CharField(_('Email'),max_length=512,blank=True,null=True)
  publish = models.BooleanField(_('Published'),default=1)
  comment =  models.TextField(_('Comment'),max_length=512,blank=True,null=True)
  #hidden
  created = models.DateTimeField(_('Created'),editable=False)
  modified = models.DateTimeField(_('Modified'),editable=False)

#  objects = CachingManager()
  
  class MPTTMeta:
    order_insertion_by = ['comment']
  
  def __unicode__(self):
    return self.notice.title
  
  class Meta:
    verbose_name = _('Comment')
    verbose_name_plural = _('Comments')
    db_table = 'blog_notices_comments'
    app_label= 'blog'

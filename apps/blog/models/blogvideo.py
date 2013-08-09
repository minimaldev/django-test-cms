from django.utils import timezone
from django.conf import settings
from django.db import models
#import menu items many to many
from apps.pages.models import MenuItems
from django.contrib.auth.models import User
from apps.blog import image
from django.utils.translation import ugettext_lazy as _
#from caching.base import CachingMixin,CachingManager



#encoding:utf-8
class BlogVideo(models.Model):

  #relationship
  user= models.ForeignKey(User,verbose_name=_('User autor'),related_name='blog_video_autor', null=True,blank=True)
  categories  = models.ForeignKey('BlogCategories',verbose_name=_('Categories'),related_name='blog_related_videos_categories')
  tags  = models.ManyToManyField('BlogTags',verbose_name=_('Blog Tags'),related_name='blog_related_videos_tags',null=True,blank=True)
  relatedvideos = models.ManyToManyField('self',blank=True, verbose_name=_('Related Videos'))
  relatednotices  = models.ManyToManyField('BlogNotice',verbose_name=_('Related Blog Notice'),related_name='blog_related_videos_notices',null=True,blank=True) 
  
  #basic
  title = models.CharField(_('Title'),max_length=125)
  video = models.TextField(_('Video'),max_length=512,blank=True)
  excerpt = models.TextField(_('excerpt'),max_length=512,blank=True)
  content = models.TextField(_('Content'),blank=True)
  publish = models.BooleanField(_('Published'),default=True)
  #featured
  is_featured = models.BooleanField(_('Is Featured'),default=False)
  is_in_feed = models.BooleanField(_('On Feed'),default=True)
  #images
  thumb = models.TextField(_('Thumbnail'),blank=True,null=True)
  featured_image = models.TextField(_('Featured Image'),blank=True,null=True)
  #date
  publishdate = models.DateTimeField(_('Publish Date'),default=timezone.now(), blank=True)

  featured_start_date = models.DateTimeField(_('Featured Start Date'),null=True,blank=True)
  featured_end_date = models.DateTimeField(_('Featured End Date'),null=True,blank=True)
  #seo
  slug = models.SlugField(_('Slug'),max_length=255,unique=True,blank=True)
  metatitle =  models.CharField(_('Meta Title'),max_length=125,blank=True)
  metadescription = models.TextField(_('Meta Description'),max_length=156,blank=True)
  #hidden
  created = models.DateTimeField(_('Created'),editable=False)
  modified = models.DateTimeField(_('Modified'),editable=False)

#  objects = CachingManager()
  
  def __unicode__(self):
    return '%s - ' % (self.title)
  
  class Meta:    
    verbose_name = _('Blog Videos')
    verbose_name_plural = _('Blogs Videos')
    get_latest_by = "created"
    ordering = ('id',)
    db_table = 'blog_videos'
    app_label= 'blog'


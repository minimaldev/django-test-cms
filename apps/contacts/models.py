from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _
#encoding:utf-8
class Categories(models.Model):
   #relationship
   user= models.ForeignKey(User, verbose_name=_('User autor'),related_name='contacts_categories_autor',blank=True,null=True)
   #basic
   name= models.CharField(_('Name'),max_length=125,unique=True)
   #hidden
   created = models.DateTimeField(_('Created'),editable=False)
   modified = models.DateTimeField(_('Modified'),editable=False)
   def __unicode__(self):
     return self.name
   class Meta:
      verbose_name = _('Category')
      verbose_name_plural =_('Categories')
      get_latest_by = "created"

class Contact(models.Model):
  #relationship
   category= models.ForeignKey(Categories,verbose_name=_('Category'),blank=True,null=True)
   #basic
   name= models.CharField(_('Name'),max_length=125)
   company= models.CharField(_('Company'),max_length=125,blank=True,null=True)
   email= models.CharField(_('Email'),max_length=125)
   website= models.CharField(_('Website'),max_length=125,blank=True,null=True)
   phone= models.CharField(_('Phone'),max_length=255,blank=True)
   cellphone= models.CharField(_('Cell phone'),max_length=255,blank=True,null=True)
   #hidden   
   created = models.DateTimeField(_('Created'),editable=False)
   modified = models.DateTimeField(_('Modified'),editable=False)
   def __unicode__(self):
     return self.email
   class Meta:
      verbose_name = _('Contact')
      verbose_name_plural = _('Contacts')
      get_latest_by = "created"

class Presupuesto(models.Model):
   PRESUPUESTO_TYPES = (
    ('PAGE', _('PAGINA WEB')),
    ('JOOMLA_S', _('SITIO WEB JOOMLA')),
    ('JOOMLA_T', _('TIENDA JOOMLA')),
    ('TIENDA_D',  _('TIENDA DJANGO')),
    ('BLOG_D',  _('BLOG DJANGO')),
    ('BLOG_W', _('BLOG WORPRESS')),
    ('WEB_APP', _('APLICACION WEB')),
    ('MOB_APP', _('APLICACION ANDROID IPHONE')),
   )
   #relationship
   user= models.ForeignKey(User, verbose_name=_('User autor'),related_name='contact_presupuesto_autor',blank=True,null=True)
   contact= models.ForeignKey(Contact,verbose_name=_('Contact'),blank=True)
   #basic
   delivery_time = models.CharField(_('Delivery time'),max_length=20,blank=True)
   presupuesto_type = models.CharField(_('Budget type'),max_length=20,blank=True,choices=PRESUPUESTO_TYPES)
   publish = models.BooleanField(_('Published'),default=0)
   #hidden   
   created = models.DateTimeField(_('Created'),editable=False)
   modified = models.DateTimeField(_('Modified'),editable=False)
   def __unicode__(self):
     return self.email
   class Meta:
      verbose_name = _('Budget')
      verbose_name_plural = _('Budgets')
      get_latest_by = "created"
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
   user= models.ForeignKey(User, verbose_name=_('User autor'),related_name='presupuesto_categories_autor',blank=True,null=True)
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

class Budget(models.Model):
   #relationship
   user= models.ForeignKey(User, verbose_name=_('User autor'),related_name='presupuesto_budget_autor',blank=True,null=True)
   category= models.ForeignKey(Categories,verbose_name=_('Category'),blank=True,null=True)
   #basic
   name= models.CharField(_('Name'),max_length=125)
   price= models.CharField(_('Price'),max_length=125,blank=True,null=True)
   days= models.IntegerField(_('Days'),max_length=125,blank=True,null=True)
   is_selectable = models.BooleanField(_('Is Selectable'),default=False)
   #hidden   
   created = models.DateTimeField(_('Created'),editable=False)
   modified = models.DateTimeField(_('Modified'),editable=False)
   def __unicode__(self):
     return self.name
   class Meta:
      verbose_name = _('Budget')
      verbose_name_plural = _('Budgets')
      get_latest_by = "created"


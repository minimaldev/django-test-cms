#encoding:utf-8
import os
import sys
import simplejson as json
import re
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.core import serializers

class GlobalConfigForm(forms.Form):

    site_name = forms.CharField(
    	widget=forms.TextInput(attrs={'id':'site_name','class':'span12'}),
    	label=_('Site name'),
    	help_text=_('Your site name'))

    site_description = forms.CharField(
    	widget=forms.Textarea(attrs={'id':'site_description','class':'span12'}),
    	label=_('Site description'),
    	help_text=_('Your Site description'))

    site_domain = forms.CharField(
    	widget=forms.TextInput(attrs={'id':'site_domain','class':'span12'}),
    	label=_('Site Domain'),
    	help_text=_('Your Site Domain'))
    
    def clean_site_domain(self):
    	reg=re.compile('^[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}$')
    	match =reg.match( str(self.cleaned_data['site_domain']))
        if not match :
            raise forms.ValidationError(_("Ivalid Domain name."))
        else:
            return self.cleaned_data['site_domain']

    def __init__(self, *args, **kwargs):
    	self.request = kwargs.pop('request', None)
    	initial = kwargs.get('initial', {})
    	
    	self.globconfigfile=os.path.join(settings.CUSTOM_CONFIG_ROOT,'site.json')
    	if os.path.exists(self.globconfigfile):
    		filename=open(self.globconfigfile).read()
    		globalconfig = json.loads(filename)    	
    		initial['site_name'] = globalconfig['site_name']
    		initial['site_description'] = globalconfig['site_description']
    		initial['site_domain'] = globalconfig['site_domain']

    	kwargs['initial'] = initial

    	super(GlobalConfigForm, self).__init__(*args, **kwargs)

    def write_config(self):
    	#if os.path.exists(self.globconfigfile):
    	with open(self.globconfigfile, "wb+") as f:
    		data=dict(
    			site_name=self.cleaned_data['site_name'],
    			site_description=self.cleaned_data['site_description'],
    			site_domain=self.cleaned_data['site_domain']
    		)
    		f.write(unicode(json.dumps(data, ensure_ascii=False)))
    	messages.success(self.request, _(' successfully Updated'))
    	#else:
    	#	messages.error(self.request, _('Oops the file not exists '))
 

    	

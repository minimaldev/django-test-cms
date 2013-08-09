#encoding:utf-8
from django.conf.urls import patterns, url
from django.contrib import admin

def get_admin_urls(urls):

    def get_urls():
        my_urls = patterns('',
            url(r'^config/global/save$','apps.config.views.save_global_config',name='save_global_config'),  
            url(r'^config/$','apps.config.views.home',name='config_home'),           
      
            
        )
        return my_urls + urls

    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls


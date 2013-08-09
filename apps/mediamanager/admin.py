#encoding:utf-8
from django.conf.urls import patterns, url
from django.contrib import admin

def get_admin_urls(urls):

    def get_urls():
        my_urls = patterns('',
            url(r'^mediamanager/delete/filename/(?P<filename>.*)/dir/(?P<slug>[0-9A-Za-z-_.//]*)$','apps.mediamanager.views.delete_files',name="mediamanager_delete_files"),    
            url(r'^mediamanager/upload/dir/$','apps.mediamanager.views.upload_file',name="mediamanager_upload_file"),
            url(r'^mediamanager/upload/dir/(?P<slug>[0-9A-Za-z-_.//]*)','apps.mediamanager.views.upload_file',name="mediamanager_upload_file"),
            url(r'^mediamanager/create/dir/$','apps.mediamanager.views.create_directory',name="mediamanager_create_directory"),
            url(r'^mediamanager/create/dir/(?P<slug>[0-9A-Za-z-_.//]*)$','apps.mediamanager.views.create_directory',name="mediamanager_create_directory"),
            url(r'^mediamanager/$','apps.mediamanager.views.mediamanager',name='mediamanager'),           
            url(r'^mediamanager/(?P<slug>[0-9A-Za-z-_.//]*)/$','apps.mediamanager.views.mediamanager',name="mediamanager")
            
            )
        return my_urls + urls

    return get_urls

admin_urls = get_admin_urls(admin.site.get_urls())
admin.site.get_urls = admin_urls


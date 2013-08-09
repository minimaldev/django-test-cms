#encoding:utf-8
from django import forms
class MediaManagerUploadForm(forms.Form):
    myfile = forms.FileField(
    	widget=forms.FileInput(attrs={'id':'uploadfile'}),
    	label='Select a file',
    	help_text='max. 42 megabytes')
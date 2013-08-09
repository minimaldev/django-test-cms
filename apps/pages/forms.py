from django import forms
from django.forms import extras
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from apps.pages.models import Blocks,MenuItems

from apps.mediamanager.widgets import MediaItemWidget

#encoding:utf-8
class AdminMenuItemsForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        widgets = {
            'thumb': MediaItemWidget(attrs={'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super(AdminMenuItemsForm, self).__init__(*args, **kwargs)

        self.fields['parent'].queryset = MenuItems.objects.exclude(
            id__exact=self.instance.id).exclude(id__in=self.instance.get_descendants())

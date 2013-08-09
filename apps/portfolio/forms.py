from django import forms
from apps.portfolio.models import PortfolioCategories,PortfolioItems
from apps.mediamanager.widgets import MediaItemWidget

#encoding:utf-8
class AdminPortfolioItemsForm(forms.ModelForm):
    class Meta:
        model = PortfolioItems
        widgets = {
            'thumb': MediaItemWidget(attrs={'readonly': 'readonly'}),
            'featured_image': MediaItemWidget(attrs={'readonly': 'readonly'}),
        }

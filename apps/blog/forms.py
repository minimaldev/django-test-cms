from django import forms
from django.forms import extras
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from apps.blog.models.blognotice import BlogNotice
from apps.blog.models.blogcategories import BlogCategories
from apps.blog.models.blogcomments import BlogComments


from apps.utils.shorten_url import ShortenURL
from django.core.urlresolvers import reverse

from apps.mediamanager.widgets import MediaItemWidget

class BlogCommentsForm(forms.ModelForm):
    email = forms.EmailField(label=_("Email") ,error_messages={'invalid': _("This value may contain only characters.")})
    comment = forms.CharField(label=_("Comment") ,max_length = 512 ,widget = forms.Textarea())
    parent = forms.IntegerField(label=_("Parent") ,required= False ,widget = forms.HiddenInput())
    class Meta:
        model = BlogComments
    def clean_parent(self):
        parent =self.cleaned_data['parent']
        if not parent is None:
            try:
                existing = BlogComments.objects.get(id=int(parent))                
                return existing
            except BlogComments.DoesNotExist:
                raise forms.ValidationError(_("the parent not exists."))
        else:
           return parent

class AdminBlogCategoriesForm(forms.ModelForm):
    class Meta:
        model = BlogCategories

    def __init__(self, *args, **kwargs):
        super(AdminBlogCategoriesForm, self).__init__(*args, **kwargs)

        self.fields['parent'].queryset = BlogCategories.objects.exclude(
            id__exact=self.instance.id).exclude(id__in=self.instance.get_descendants())


class AdminBlogNoticesForm(forms.ModelForm):
    class Meta:
        model = BlogNotice
        widgets = {
            'thumb': MediaItemWidget(attrs={'readonly': 'readonly'}),
            'featured_image': MediaItemWidget(attrs={'readonly': 'readonly'}),
        }

class SearchForm(forms.Form):
    s = forms.CharField()

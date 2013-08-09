from django.core.urlresolvers import reverse, NoReverseMatch
from django import template
register = template.Library()

@register.simple_tag
def admin_change_list_url(app_label,model_name):
    return reverse('admin:%s_%s_changelist' %(app_label,model_name ) )

@register.simple_tag
def admin_add_url(app_label,model_name):
    return reverse('admin:%s_%s_add' %(app_label,model_name ) )

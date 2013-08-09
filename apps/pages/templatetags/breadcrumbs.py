from django import template
from apps.pages.models import Blocks
from apps.pages.models import MenuItems
from django.conf import settings
register = template.Library()

@register.inclusion_tag('pages/templatetags/breacrumb.html', takes_context = True)
def render_breadcrumb_tag(context):	
	slug=context['Slug']	
	MenuItems=context['MenuItems'] 
	breadcrumb = list(MenuItems.get_ancestors(ascending=False, include_self=True))
	if context.has_key('Breadcrumb_last_item'):
		last_item=context['Breadcrumb_last_item']
		return {'breadcrumb': breadcrumb,'last_item':last_item}
	return {'breadcrumb': breadcrumb}
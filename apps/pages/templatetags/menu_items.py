from django import template
from apps.pages.models import Blocks
from apps.pages.models import MenuItems
from django.conf import settings

register = template.Library()

@register.inclusion_tag('pages/templatetags/root_menu.html', takes_context = True)
def render_menu_tag(context,menu_name,other_class=''): 
	menu_name=menu_name	
	slug=context['Slug']
	menu_items = list(MenuItems.objects.filter(block__name=menu_name))	
	return {'menu_items': menu_items,
	'other_class':other_class,
	'slug':slug}
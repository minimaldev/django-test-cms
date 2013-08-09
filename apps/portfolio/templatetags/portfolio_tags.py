from apps.portfolio.models import PortfolioCategories,PortfolioItems
from django.db.models import Count
from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

register = template.Library()

@register.inclusion_tag('portfolio/templatetags/portfolio_list.html', takes_context = True)
def list_portfolio_tag(context,limit=5): 
	#page = context['request'].GET.get('page',1)
	page = context['page']
	slug=context['Slug']
	categories  = list(PortfolioCategories.objects.all().order_by('-name'))
	portfolio_items  = list(PortfolioItems.objects.filter(publish=True).order_by('-id'))
	paginator = Paginator(portfolio_items, limit)
	try:
		portfolio_items = paginator.page(page)
	except PageNotAnInteger:
		portfolio_items = paginator.page(1)
	except EmptyPage:
		portfolio_items = paginator.page(paginator.num_pages)
	return {'categories': categories,'portfolio_items': portfolio_items,'slug':'/'+slug}



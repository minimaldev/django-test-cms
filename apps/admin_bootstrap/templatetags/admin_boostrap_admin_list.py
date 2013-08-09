import datetime

from django.contrib.admin.util import lookup_field, display_for_field, label_for_field
from django.contrib.admin.views.main import (ALL_VAR, EMPTY_CHANGELIST_VALUE,
    ORDER_VAR, PAGE_VAR, SEARCH_VAR)
from django.contrib.admin.templatetags.admin_static import static
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.utils import formats
from django.utils.html import escape, conditional_escape
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from django.utils.translation import ugettext as _
from django.utils.encoding import smart_unicode, force_unicode
from django.template import Library
from django.template.loader import get_template
from django.template.context import Context

register = Library()

DOT = '.'

@register.simple_tag
def paginator_number(cl,i):
    """
    Generates an individual page index link in a paginated list.
    """
    if i == DOT:
        return u'<li class="active"><span>...</span></li>'
    elif i == cl.page_num:
        return mark_safe(u'<li class="active"><span>%d</span></li>' % (i+1))
    else:
        return mark_safe(u'<li><a href="%s"%s>%d</a></li> ' % (escape(cl.get_query_string({PAGE_VAR: i})), (i == cl.paginator.num_pages-1 and ' class="end"' or ''), i+1))

@register.simple_tag
def paginator_first_page(cl):
    fistpage= 0
    if fistpage == cl.page_num:
        return mark_safe(u'<li class="active"><span>First</span></li>')
    else:
        return mark_safe(u'<li><a href="%s">First</a></li> ' % (escape(cl.get_query_string({PAGE_VAR: fistpage}))))

@register.simple_tag
def paginator_last_page(cl):
    lastpage=cl.paginator.num_pages-1
    if lastpage == cl.page_num:
        return mark_safe(u'<li class="active"><span>Last</span></li>' )
    else:
        return mark_safe(u'<li><a href="%s">Last</a></li> ' % (escape(cl.get_query_string({PAGE_VAR: lastpage}))))

@register.simple_tag
def paginator_next_page(cl):
    lastpage=cl.paginator.num_pages-1
    nextpage= cl.page_num +1 
    if nextpage >= lastpage:
        nextpage=lastpage
    if lastpage == cl.page_num:
        return mark_safe(u'<li class="active"><span>Next</span></li>' )
    else:
        return mark_safe(u'<li><a href="%s">Next</a></li> ' % (escape(cl.get_query_string({PAGE_VAR: nextpage}))))

@register.simple_tag
def paginator_prev_page(cl):
    prevpage= cl.page_num -1 
    if prevpage <= -1:
        prevpage=0
        return mark_safe(u'<li class="active"><span>Prev</span></li>' )
    else:
        return mark_safe(u'<li><a href="%s">Prev</a></li> ' % (escape(cl.get_query_string({PAGE_VAR: prevpage}))))

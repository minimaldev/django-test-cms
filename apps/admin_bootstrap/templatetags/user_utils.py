from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from datetime import datetime

def get_all_logged_in_users():
    # Query all non-expired sessions
    sessions = Session.objects.filter(expire_date__gte=datetime.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)[:10]

from django import template
register = template.Library()

@register.inclusion_tag('templatetags/logged_in_user_list.html')
def render_logged_in_user_list():
    return { 'users': get_all_logged_in_users() }

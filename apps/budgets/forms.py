from django import forms
from django.forms import extras
from django.forms import ModelForm
from apps.budgets.models import Categories,Budget
from django.core.mail import  EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

attrs_dict = {'class': 'required'}

def send(template,subject,email,context_var):

    template_html = 'email/%s.html' % template
    template_text = 'email/%s.txt'  % template
    to = email
    from_email = settings.DEFAULT_FROM_EMAIL           
   
    text_content = render_to_string(template_text, context_var)
    html_content = render_to_string(template_html, context_var)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()




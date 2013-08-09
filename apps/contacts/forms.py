from django import forms
from django.forms import extras
from django.forms import ModelForm
from apps.contacts.models import Contact,Categories as ContactCategories,Presupuesto
from django.core.mail import  EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone

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

class ContactPresupuestoAdminform(ModelForm):
	
	class Meta:
		model = Presupuesto
		
	def clean_presupuesto_type(self):
		existing = User.objects.filter(email=self.cleaned_data['email']).exclude(username=self.cleaned_data['username'])
		if existing.exists():
			raise forms.ValidationError(_("A Email exists." ))
		else:
			return self.cleaned_data['presupuesto_type']

class ContactAdminform(ModelForm):
	
	class Meta:
		model = Contact
		
	def clean_email(self):
		existing = Contact.objects.filter(email=self.cleaned_data['email'])
		if existing.exists():
			raise forms.ValidationError(_("A Email exists." ))
		else:
			return self.cleaned_data['email']

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    company = forms.CharField()
    website = forms.CharField(required=False,widget =forms.TextInput(attrs={'class':'norequired'}))
    where_met = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':'17'}))





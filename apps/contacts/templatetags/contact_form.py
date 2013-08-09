from apps.contacts.models import Contact,Categories as ContactCategories
from apps.contacts.forms import ContactForm
from django.utils import timezone
from django.db.models import Count
from django import template
from django.conf import settings

register = template.Library()

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


@register.inclusion_tag('contacts/templatetags/contact_form.html', takes_context = True)
def contact_form_tag(context): 
	request = context['request']
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.data['name']
			phone = form.data['phone']
			company = form.data['company']
			website = form.data['website']
			message = form.data['message']
			to = form.data['email']
			category = form.data['where_met']
			category=ContactCategories.objects.get(name=category)
			try:
				new_contact = Contact.objects.get(email=to)
			except Contact.DoesNotExist:
				current_time= timezone.now()
				new_contact= Contact()
				new_contact.name=name
				new_contact.company=company
				new_contact.phone=phone
				new_contact.website=website
				new_contact.email=to
				new_contact.category=category
				new_contact.created=current_time
				new_contact.modified=current_time
				new_contact.save()
	else:
		form=ContactForm()

	return {'form': form,'Categories':ContactCategories.objects.all()}

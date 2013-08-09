from django.conf import settings
from django.contrib import admin
from django.utils.text import capfirst
from django.core.urlresolvers import reverse, NoReverseMatch

site = admin.site
#reference http://djangosnippets.org/snippets/1921/
# usage
#{% for adm_app in adm_app_list %}
#	<p>{{adm_app.name}} - {{adm_app.app_url}}</p>
#	 {% for model in adm_app.models %}
#	 	<p>{{ model.name }} - {{model.admin_url}}</p>
#	 {% endfor %}
#{% endfor %}
def applist(request):
	app_dict = {}
	user = request.user
	for model, model_admin in site._registry.items():
		app_label = model._meta.app_label
		has_module_perms = user.has_module_perms(app_label)
		
		if has_module_perms:
			perms = model_admin.get_model_perms(request)
			
			if True in perms.values():
				info = (app_label, model._meta.module_name)
				
				model_dict = {
					'name': capfirst(model._meta.verbose_name_plural),
					'admin_url': reverse('admin:%s_%s_changelist' % info, current_app=model.__name__.lower()),
					'perms': perms,
				}
				if app_label in app_dict:
					app_dict[app_label]['models'].append(model_dict)
				else:
					app_dict[app_label] = {
						'name': app_label.title(),
						'app_url': reverse('admin:app_list', kwargs={'app_label': app_label}, current_app='admin'),
						'has_module_perms': has_module_perms,
						'models': [model_dict],
					}
	for item in settings.APP_DICT:
		app_label=item['app_label']
		as_module_perms = user.has_module_perms(app_label)
		app_dict[app_label] = {
						'name': app_label,
						'app_url': reverse('admin:app_list', kwargs={'app_label':app_label}, current_app='admin'),
						'has_module_perms': has_module_perms,
						'models':item['models'],
					}

	app_list = app_dict.values()
	app_list.sort(lambda x, y: cmp(x['name'], y['name']))
	return {'adm_app_list': app_list}
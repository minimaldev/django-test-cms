from django.utils import timezone
from apps.contacts.models import Contact,Categories as ContactCategories,Presupuesto
from apps.contacts.forms import ContactPresupuestoAdminform
from apps.contacts.forms import ContactAdminform
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class ContactoPresupuestoInline(admin.StackedInline):
  model = Presupuesto
  extra = 0
  form  = ContactPresupuestoAdminform 


class ContactsContactAdmin(admin.ModelAdmin):
#   class Media:
#       js = ('/js/copytitle.js',)
   fieldsets = [(_('Basic'),{'fields': ['name','company','email','website','phone','cellphone']}),
   				
                (_('Category'),{'fields': ['category']}),
        ]
   list_display = ('name', 'email','website','created','modified')
   search_fields = ['name','email','website']
   inlines = [ContactoPresupuestoInline]
   form = ContactAdminform
   def save_model(self, request, obj, form, change):
   	current_time= timezone.now()
   	if getattr(obj, 'id', None) is None:
   		obj.created=current_time
   	obj.modified=current_time
   	if getattr(obj, 'user', None) is None:
   		obj.user = request.user
   	obj.save()

class ContactsContactCategoriesAdmin(admin.ModelAdmin):
#   class Media:
#       js = ('/js/copytitle.js',)
   fieldsets = [(_('Basic'),{'fields': ['name']}),
   		(_('Autor'),{'fields': ['user']}),
        ]
   list_display = ('name', 'created','modified')
   search_fields = ['name',]
   def save_model(self, request, obj, form, change):
   	current_time= timezone.now()
   	if getattr(obj, 'id', None) is None:
   		obj.created=current_time
   	obj.modified=current_time
   	if getattr(obj, 'user', None) is None:
   		obj.user = request.user
   	obj.save()

class ContactPresupuestoAdmin(admin.ModelAdmin):
#   class Media:
#       js = ('/js/copytitle.js',)
   fieldsets = [(_('Basic'),{'fields': ['delivery_time','presupuesto_type','publish']}),
   				(_('Autor'),{'fields': ['user']}),
                (_('Contacto'),{'fields': ['contact']}),
        ]
   list_display = ('contact','created','modified')
   search_fields = ['contact__email',]
   form  = ContactPresupuestoAdminform 
   def save_model(self, request, obj, form, change):
   	current_time= timezone.now()
   	if getattr(obj, 'id', None) is None:
   		obj.created=current_time
   	obj.modified=current_time
   	if getattr(obj, 'user', None) is None:
   		obj.user = request.user
   	obj.save()


admin.site.register(Contact,ContactsContactAdmin)
admin.site.register(Presupuesto,ContactPresupuestoAdmin)
admin.site.register(ContactCategories,ContactsContactCategoriesAdmin)

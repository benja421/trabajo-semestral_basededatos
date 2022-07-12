from django.contrib import admin

from login.models import Atenciones, Comuna, Mascota, Rol,Usuario

# Register your models here.
admin.site.register(Rol)
admin.site.register(Usuario)
admin.site.register(Mascota)
admin.site.register(Atenciones)
admin.site.register(Comuna)

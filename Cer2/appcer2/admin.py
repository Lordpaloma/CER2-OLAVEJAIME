from django.contrib import admin

from appcer2.models import Correspondencia,Residencia

class residenciaadmin(admin.ModelAdmin):
    list_display = ("numero", "dueño", "telefono", "Correo")

class CorrespondenciaAdmin(admin.ModelAdmin):
    list_display = ( "fecha_entrega","Conserje","destinatario", "entregado","direccion", )
    list_filter = ("direccion",)
    date_hierarchy ="fecha_entrega"

admin.site.register(Residencia, residenciaadmin)

admin.site.register(Correspondencia, CorrespondenciaAdmin)

# Register your models here.

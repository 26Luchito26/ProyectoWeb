from django.contrib import admin
from .models import Solicitudes_Epps, Solicitudes_Retiro, Solicitudes_Material

# Register your models here.

class Solicitudes_Epps_Admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Solicitudes_Epps, Solicitudes_Epps_Admin)


class Solicitudes_Retiro_Admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Solicitudes_Retiro, Solicitudes_Retiro_Admin)

class Solicitudes_Material_Admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Solicitudes_Material, Solicitudes_Material_Admin)
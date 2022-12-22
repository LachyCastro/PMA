from django.contrib import admin
from enrutamientoVehiculos.models import *


# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'autor','solutions_method')
    search_fields = ('name', 'autor', 'solutions_method')


admin.site.site_header = 'VPR'
admin.site.register(Publication, PublicationAdmin)


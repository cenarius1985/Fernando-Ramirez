from django.contrib import admin
from .models import monitoreo

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('servicio','nombre')

admin.site.register(monitoreo, PostAdmin)



   
   
    
    
from django.contrib import admin
from django.contrib import auth
from django.contrib.auth import models
from .models import tarea

class admintarea(admin.ModelAdmin):
    readonly_fields = ("Creado", )  

# Register your models here.


admin.site.register(tarea, admintarea )

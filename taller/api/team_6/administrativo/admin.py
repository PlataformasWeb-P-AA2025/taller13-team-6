from django.contrib import admin

# Register your models here.
from .models import Edificio,Departamento

admin.site.register(Edificio)
admin.site.register(Departamento)
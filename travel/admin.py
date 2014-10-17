from django.contrib import admin
from .models import Trip, ServiceProvider, Stop, Leg


for klass in [Trip, ServiceProvider, Stop, Leg]:
    class DefaultAdmin(admin.ModelAdmin):
        pass
    admin.site.register(klass, DefaultAdmin)

from django.contrib import admin
from .models import Trip, ServiceProvider, Stop, Leg, Lodging, Place, Stop, Stay


for klass in [Trip, ServiceProvider, Stop, Leg, Lodging, Place, Stay]:
    class DefaultAdmin(admin.ModelAdmin):
        pass
    admin.site.register(klass, DefaultAdmin)

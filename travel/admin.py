from django.contrib import admin
from .models import Trip, ServiceProvider, Flight, Airport


for klass in [Trip, ServiceProvider, Flight, Airport]:
    class DefaultAdmin(admin.ModelAdmin):
        pass
    admin.site.register(klass, DefaultAdmin)

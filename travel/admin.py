from django.contrib import admin
from .models import Trip, ServiceProvider, Flight


for klass in [Trip, ServiceProvider, Flight]:
    class DefaultAdmin(admin.ModelAdmin):
        pass
    admin.site.register(klass, DefaultAdmin)

from django.contrib import admin
from .models import (Trip, ServiceProvider, Stop, Leg, Lodging,
                     Place, Stop, Stay, Home, TwilioNumber)


for klass in [Trip, ServiceProvider, Stop, Leg, Home, TwilioNumber,
              Lodging, Place, Stay]:
    class DefaultAdmin(admin.ModelAdmin):
        pass
    admin.site.register(klass, DefaultAdmin)

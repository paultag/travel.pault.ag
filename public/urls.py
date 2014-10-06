from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'public.views.home', name='home'),
    url(r'^travel/', include('travel.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

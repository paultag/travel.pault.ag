from django.conf.urls import patterns, include, url
from .views import TripsView


urlpatterns = patterns('',
    url(r'^trips/(?P<user>.*)/$', TripsView.as_view(), name='api_trips'),
)

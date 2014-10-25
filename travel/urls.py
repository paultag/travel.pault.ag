from django.conf.urls import patterns, include, url
from .views import TripView, TripsView


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'travel.views.home', name='home'),
    url(r'^trips/(?P<user>.*)/$', TripsView.as_view(), name='trips'),
    url(r'^trip/(?P<trip>.*)/$', TripView.as_view(), name='trip'),

    url(r'^twilio/query/$', 'travel.views.query', name='query'),
)

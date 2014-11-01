from django.conf.urls import patterns, include, url
from .views import TripsView, WhereisView


urlpatterns = patterns('',
    url(r'^trips/(?P<user>.*)/$', TripsView.as_view(), name='api_trips'),
    url(r'^whereis/(?P<user>.*)/$', WhereisView.as_view(), name='api_whereis'),
)

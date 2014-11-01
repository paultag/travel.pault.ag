from django.conf.urls import patterns, include, url
from .views import TripsView, LocateView, StaysView


urlpatterns = patterns('',
    url(r'^trips/(?P<user>.*)/$', TripsView.as_view(), name='api_trips'),
    url(r'^stays/(?P<user>.*)/$', StaysView.as_view(), name='api_stays'),
    url(r'^locate/(?P<user>.*)/$', LocateView.as_view(), name='api_locate'),
)

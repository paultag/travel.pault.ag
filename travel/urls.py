from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'travel.views.ui.home', name='home'),

    url(r'^trips/(?P<user>.*)/$', 'travel.views.ui.trips', name='trips'),
    url(r'^trips/(?P<user>.*)/calendar.ical$', 'travel.views.calendar.calendar', name='calendar'),

    url(r'^trip/(?P<trip>.*)/$', 'travel.views.ui.trip', name='trip'),
    url(r'^whereis/(?P<user>.*)/$', 'travel.views.ui.whereis', name='whereis'),

    url(r'^twilio/query/$', 'travel.views.twilio.query', name='query'),
)

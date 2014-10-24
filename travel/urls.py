from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'travel.views.home', name='home'),
    url(r'^trips/(?P<user>.*)/$', 'travel.views.trips', name='trips'),
    url(r'^where/(?P<user>.*)/$', 'travel.views.where', name='where'),
    url(r'^trip/(?P<trip>.*)/$', 'travel.views.trip', name='trip'),
)

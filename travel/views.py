from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import datetime as dt
import pytz
import json

from django.contrib.auth.models import User
from .models import Trip


class JSONEncoder(json.JSONEncoder):
    def default(self, obj, **kwargs):
        if isinstance(obj, dt.timedelta):
            return obj.total_seconds()
        if isinstance(obj, (dt.date, dt.datetime)):
            if obj.tzinfo is None:
                raise TypeError(
                    "date '%s' is not fully timezone qualified." % (obj))
            return "{}".format(obj.isoformat())
        return super(JSONEncoder, self).default(obj, **kwargs)


def _wrap(data):
    return HttpResponse(json.dumps(data, cls=JSONEncoder))


def home(request):
    return render(request, "travel/public/home.html")


def trips(request, user):
    user = User.objects.get(username=user)
    active_trips = Trip.active_trips(user=user)
    return render(request, "travel/public/trips.html", {
        "active_trips": active_trips,
        "user": user,
    })


def trip(request, trip):
    trip = Trip.objects.get(id=trip)

    if request.META['HTTP_ACCEPT'].startswith("application/json"):
        return _wrap(trip.to_dict())

    legs = trip.legs.all().order_by("departure_time")
    return render(request, "travel/public/trip.html", {
        "trip": trip,
        "legs": legs,
        "user": trip.user,
        "settings": settings,
    })

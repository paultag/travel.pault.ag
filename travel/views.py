from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import datetime as dt
import pytz
import json

from django.contrib.auth.models import User
from .models import Trip, Stay


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

    if request.META['HTTP_ACCEPT'].startswith("application/json"):
        return _wrap(
            {
                "user": user.username,
                "active_trips": [x.to_dict() for x in active_trips]
            }
        )

    return render(request, "travel/public/trips.html", {
        "active_trips": active_trips,
        "user": user,
    })


def trip(request, trip):
    trip = Trip.objects.get(id=trip)

    if request.META['HTTP_ACCEPT'].startswith("application/json"):
        return _wrap(trip.to_dict())

    legs = trip.legs.all().order_by("departure_time")
    stays = trip.stays.all().order_by("checkin_time")
    return render(request, "travel/public/trip.html", {
        "trip": trip,
        "legs": legs,
        "user": trip.user,
        "stays": stays,
        "settings": settings,
    })


def where(request, user):
    user = User.objects.get(username=user)
    active_stay = Stay.active_stays(user=user).order_by("checkin_time").first()

    if request.META['HTTP_ACCEPT'].startswith("application/json"):
        return _wrap(active_stay.to_dict())

    return render(request, "travel/public/where.html", {
        "user": user,
        "stay": active_stay,
        "trip": active_stay.trip,
        "lodging": active_stay.lodging if active_stay else None,
        "place": active_stay.lodging.place if active_stay else None,
        "settings": settings,
    })

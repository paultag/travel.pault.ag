from django.shortcuts import render
from django.conf import settings
from django.http import Http404
import datetime as dt
import pytz

from django.contrib.auth.models import User
from ..models import Trip, Stay, Place
from ..specs import TRIP_SPEC, PLACE_SPEC


def home(request):
    return render(request, "travel/public/home.html")



def whereis(request, user):
    user = User.objects.get(username=user)
    place = Place.locate_user(user)
    return render(request, "travel/public/where.html", {
        "place": place,
    })


def trip(request, trip):
    try:
        trip = Trip.objects.get(id=trip)
    except Trip.DoesNotExist:
        raise Http404("No such trip")

    legs = trip.legs.all().order_by("departure_time")
    stays = trip.stays.all().order_by("checkin_time")
    return render(request, "travel/public/trip.html", {
        "trip": trip,
        "legs": legs,
        "user": trip.user,
        "stays": stays,
        "settings": settings,
    })



def trips(request, user):
    try:
        user = User.objects.get(username=user)
    except User.DoesNotExist:
        raise Http404("No such user")

    trips = Trip.get_active_trips(user=user)

    return render(request, "travel/public/trips.html", {
        "active_trips": trips,
        "user": user,
    })

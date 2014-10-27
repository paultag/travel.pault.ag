from django.shortcuts import render
from django.conf import settings
from django.http import Http404
import datetime as dt
import pytz

from django.contrib.auth.models import User
from ..models import Trip, Stay, Place
from ..helpers import TravelView
from ..specs import TRIP_SPEC, PLACE_SPEC


def home(request):
    return render(request, "travel/public/home.html")


class WhereView(TravelView):
    PUBLIC_SCHEMA = PLACE_SPEC

    def lookup(self, user):
        user = User.objects.get(username=user)
        return Place.locate_user(user)

    def render(self, request, place):
        return render(request, "travel/public/where.html", {
            "place": place,
        })


class TripView(TravelView):
    PUBLIC_SCHEMA = TRIP_SPEC

    def lookup(self, trip):
        try:
            return Trip.objects.get(id=trip)
        except Trip.DoesNotExist:
            raise Http404("No such trip")

    def render(self, request, trip):
        legs = trip.legs.all().order_by("departure_time")
        stays = trip.stays.all().order_by("checkin_time")
        return render(request, "travel/public/trip.html", {
            "trip": trip,
            "legs": legs,
            "user": trip.user,
            "stays": stays,
            "settings": settings,
        })


class TripsView(TravelView):
    PUBLIC_SCHEMA = TRIP_SPEC

    def render(self, request, trips, user):
        return render(request, "travel/public/trips.html", {
            "active_trips": trips,
            "user": user,
        })

    def lookup(self, user):
        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            raise Http404("No such user")

        return (Trip.get_active_trips(user=user), user)

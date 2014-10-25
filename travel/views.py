from django.shortcuts import render
from django.conf import settings
import datetime as dt
import pytz

from django.contrib.auth.models import User
from .models import Trip, Stay
from .helpers import TravelView

from .specs import TRIP_SPEC


def home(request):
    return render(request, "travel/public/home.html")


class TripView(TravelView):
    PUBLIC_SCHEMA = TRIP_SPEC

    def lookup(self, trip):
        return Trip.objects.get(id=trip)

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

    def render(self, request, trips):
        return render(request, "travel/public/trips.html", {
            "active_trips": trips,
        })

    def lookup(self, user):
        user = User.objects.get(username=user)
        return Trip.get_active_trips(user=user)

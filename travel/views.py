from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Trip


def home(request):
    return render(request, "travel/public/home.html")


def trips(request, user):
    trips = Trip.get_active_trips()

    return render(request, "travel/public/trips.html", {
        "trips": trips,
    })

from django.shortcuts import render
import datetime as dt

from django.contrib.auth.models import User
from .models import Trip


def home(request):
    return render(request, "travel/public/home.html")


def trips(request, user):
    now = dt.datetime.utcnow()

    trips = Trip.objects.filter(
        flights__arrival_time__gte=now
    )
    return render(request, "travel/public/trips.html", {
        "trips": trips,
    })

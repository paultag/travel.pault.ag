from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Trip(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    reason = models.TextField()

    @classmethod
    def get_active_trips(cls):
        now = dt.datetime.utcnow()
        return Trip.objects.filter(
            flights__arrival_time__gte=now
        )


class ServiceProvider(models.Model):
    name = models.CharField(max_length=128)
    rewards_account = models.CharField(max_length=128)
    website = models.URLField()
    phone_number = models.CharField(max_length=32)

    def __str__(self):
        return "<ServiceProvider: {}>".format(self.name)


class Flight(models.Model):
    user = models.ForeignKey(User)
    flight_number = models.CharField(max_length=128)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    carrier = models.ForeignKey(ServiceProvider, related_name="flights")
    trip = models.ForeignKey(Trip, related_name="flights")

    def __str__(self):
        return "<Flight: {} on {}>".format(
            self.flight_number, self.departure_time
        )

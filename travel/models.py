from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Trip(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    reason = models.TextField()

    @classmethod
    def get_active_trips(cls, **filters):
        now = dt.datetime.utcnow()
        return Trip.objects.filter(
            legs__arrival_time__gte=now,
            **filters
        ).distinct()

    def __str__(self):
        return "<Trip: {}>".format(self.name)


class ServiceProvider(models.Model):
    name = models.CharField(max_length=128)
    rewards_account = models.CharField(max_length=128)
    website = models.URLField()
    phone_number = models.CharField(max_length=32)

    def __str__(self):
        return "<ServiceProvider: {}>".format(self.name)


class Stop(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=16)
    lat = models.CharField(max_length=128)
    lon = models.CharField(max_length=128)

    def __str__(self):
        return "<Stop: {}>".format(self.code)


class Leg(models.Model):
    number = models.CharField(max_length=128)
    origin = models.ForeignKey(Stop, related_name="inbound_legs")
    destination = models.ForeignKey(Stop, related_name="outbound_legs")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    carrier = models.ForeignKey(ServiceProvider, related_name="legs")
    trip = models.ForeignKey(Trip, related_name="legs")

    def __str__(self):
        return "<Leg: {} {} on {}>".format(
            self.carrier.name,
            self.number,
            self.departure_time
        )

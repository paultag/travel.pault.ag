from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Trip(models.Model):
    user = models.ForeignKey(User)
    reason = models.TextField()

    @classmethod
    def get_active_trips(cls):
        now = dt.datetime.utcnow()
        # Query on any flights arriving in the future
        return Trip.objects.filter(
            flights__arrival_time__gte=now
        )

    @property
    def get_legs(self):
        yield from self.flights.all()


class ServiceProvider(models.Model):
    name = models.TextField()
    rewards_account = models.TextField()
    website = models.TextField()
    phone_number = models.TextField()

    def __str__(self):
        return "<ServiceProvider: {}>".format(self.name)


class Flight(models.Model):
    user = models.ForeignKey(User)
    departure_time = models.DateTimeField()
    flight_number = models.TextField()
    arrival_time = models.DateTimeField()
    carrier = models.ForeignKey(ServiceProvider)
    trip = models.ForeignKey(Trip, related_name="flights")

    def __str__(self):
        return "<Flight: {} on {}>".format(
            self.flight_number, self.departure_time
        )

from django.http import HttpResponse

from django.contrib.auth.models import User
from ..models import Trip

from icalendar import Calendar, Event


def calendar(request, user):
    user = User.objects.get(username=user)
    cal = Calendar()
    cal['summary'] = "Trips for {0.first_name} {0.last_name}".format(user)
    cal['prodid'] = '-//Paul\'s travel site//travel.pault.ag//'
    cal['version'] = '1.0'
    cal['attendee'] = user.email

    trips = Trip.objects.filter(user=user)
    for trip in trips:
        event = Event()
        event['uid'] = "{id}.trip.travel.pault.ag".format(id=trip.id)
        event.add('dtstart', trip.start)
        event.add('dtend', trip.end)
        event.add('description', trip.reason)
        event.add('summary', trip.name)

        cal.add_component(event)

        for leg in trip.legs.all():
            event = Event()
            event['summary'] = "{0.carrier.name} {0.number}".format(leg)
            event['description'] = (
                "{0.carrier.name} {0.number} ({0.type}) from "
                "{0.origin.code} ({0.origin.name}) to "
                "{0.destination.code} ({0.destination.name})"
                ).format(leg)
            event['uid'] = "{id}.leg.pault.ag".format(id=leg.id)
            event.add('dtstart', leg.departure)
            event.add('dtend', leg.arrival)
            cal.add_component(event)

    return HttpResponse(cal.to_ical(), content_type="text/calendar")

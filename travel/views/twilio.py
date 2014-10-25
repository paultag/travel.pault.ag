from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.conf import settings

from django.contrib.auth.models import User
from ..models import Place, Trip, TwilioNumber


def text(request, message):
    return render(request, "travel/twilio/sms.xml", {
        "message": "I don't know about that."
    }, content_type="application/xml")


def where(request, number, message):
    user = number.user
    place = Place.locate_user(user=user)

    return render(request, "travel/twilio/sms.xml", {
        "message": "{} is scheduled to be in {}".format(
            user.first_name, place.name)
    }, content_type="application/xml")


VERBS = {
    "where": where  # Look up active leg or get place
}


@require_http_methods(["POST"])
@csrf_exempt
def query(request):
    inquery = request.POST['Body'].lower().strip()
    to = request.POST['To'].strip("+.-").strip()

    try:
        number = TwilioNumber.objects.get(number=to)
    except TwilioNumber.DoesNotExist:
        raise  # eror sanely here or something

    if inquery in VERBS:
        return VERBS[inquery](request, number, inquery)

    return text(request, "Hello, World")

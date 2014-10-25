from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.conf import settings

from django.contrib.auth.models import User
from ..models import Place, Trip


def text(request, message):
    return render(request, "travel/twilio/sms.xml", {
        "message": "I don't know about that."
    }, content_type="application/xml")


def where(request, message):
    return render(request, "travel/twilio/sms.xml", {
        "message": "Hello, World"
    }, content_type="application/xml")


VERBS = {
    "where": where  # Look up active leg or get place
}


@require_http_methods(["POST"])
@csrf_exempt
def query(request):
    inquery = request.POST.get('Message', "").strip().lower()
    if inquery in VERBS:
        return VERBS[inquery](request, inquery)
    return text(request, "Hello, World")

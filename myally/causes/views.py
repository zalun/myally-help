from django.http import HttpResponse
from django.shortcuts import render

from .models import Cause
from therapists.models import Therapist


def index(request, cause_name):
    cause = Cause.objects.get(name=cause_name)
    therapists = cause.therapists.filter(online=True)
    return render(
        request, "therapists.html", context=dict(cause=cause, therapists=therapists)
    )

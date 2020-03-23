from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Cause
from therapists.models import Therapist


def index(request, cause_name):
    cause = get_object_or_404(Cause, name=cause_name)
    therapists = cause.therapists.filter(online=True)
    return render(
        request, "therapists.html", context=dict(cause=cause, therapists=therapists)
    )

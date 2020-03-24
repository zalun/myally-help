from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Cause
from therapists.models import Therapist


def index(request, cause_name):
    cause = get_object_or_404(Cause, name=cause_name)
    therapists = cause.therapists.filter(online=True)
    count_online = therapists.count()
    count_busy = therapists.filter(busy=True)
    count_all = cause.therapists.count()
    return render(
        request, 
        "therapists.html", 
        context=dict(
            cause=cause, 
            therapists=therapists,
            count_online=count_online,
            count_busy=count_busy,
            count_all=count_all
        )
    )

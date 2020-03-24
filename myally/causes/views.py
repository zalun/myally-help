from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Cause
from therapists.models import Therapist


def index(request, cause_name):
    cause = get_object_or_404(Cause, name=cause_name)
    therapists = cause.therapists.filter(online=True)
    count_online = therapists.count()
    count_available = therapists.filter(busy=False).count()
    count_all = cause.therapists.count()
    return render(
        request, 
        "therapists.html", 
        context=dict(
            cause=cause, 
            therapists=therapists,
            count_online=count_online,
            count_available=count_available,
            count_all=count_all,
            no_therapists=count_all == 0,
            no_therapists_online=count_online == 0,
            no_therapists_available=count_available == 0
        )
    )

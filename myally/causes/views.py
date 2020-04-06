from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from invitations.utils import get_invitation_model

from .models import Cause
from therapists.models import Therapist
from coordinators.forms import InviteCoordinatorForm


def therapists(request, cause_name):
    cause = get_object_or_404(Cause, slug=cause_name)
    therapists = cause.therapists.filter(active=True, online=True)
    count_online = therapists.count()
    count_available = therapists.filter(busy=False).count()
    count_all = cause.therapists.filter(active=True).count()
    invite_coordinator_form = InviteCoordinatorForm()
    return render(
        request,
        "therapists.html",
        context=dict(
            cause=cause,
            cause_name=cause.slug,
            country="pl",
            therapists=therapists,
            invite_coordinator_form=invite_coordinator_form,
            count_online=count_online,
            count_available=count_available,
            count_all=count_all,
            no_therapists=count_all == 0,
            no_therapists_online=count_online == 0,
            no_therapists_available=count_available == 0,
        ),
    )


def coordinators(request, cause_name):
    if not request.user.is_superuser:
        return HttpResponse("ACCESS DENIED")

    cause = get_object_or_404(Cause, slug=cause_name)
    coordinators = cause.coordinators.filter()
    return render(
        request,
        "coordinators.html",
        context=dict(cause=cause, coordinators=coordinators,),
    )

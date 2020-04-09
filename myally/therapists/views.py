import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from invitations.utils import get_invitation_model

from .forms import InviteTherapistForm, ShortActivityForm, ShortTherapistForm
from causes.models import Cause
from .models import Therapist

@login_required
@require_http_methods(["POST"])
def save_status(request):
    if not request.user.therapist:  # or not request.user.therapist.active:
        return HttpResponse("You're not an active Therapist.")

    t = request.user.therapist
    form_activity = ShortActivityForm(request.POST)
    if form_activity.is_valid():
        t.online = form_activity.cleaned_data["online"]
        t.busy = form_activity.cleaned_data["busy"]
        t.save()

    return HttpResponse(json.dumps(dict(success=True)))


@login_required
@require_http_methods(["GET", "POST"])
def index(request):
    if not request.user.therapist:  # or not request.user.therapist.active:
        return HttpResponse("You're not an active Therapist.")

    t = request.user.therapist
    if request.method == "POST":
        form = ShortTherapistForm(request.POST)
        if form.is_valid():
            t.phone_number = form.cleaned_data["phone_number"]
            t.whatsapp = form.cleaned_data["whatsapp"]
            t.skype_id = form.cleaned_data["skype_id"]
            t.messenger_id = form.cleaned_data["messenger_id"]
            t.save()

    countries = [c.name for c in request.user.therapist.countries]
    causes = ", ".join([c.name for c in request.user.therapist.causes.all()])
    form_activity = ShortActivityForm(dict(online=t.online, busy=t.busy,))

    form = ShortTherapistForm(
        dict(
            phone_number=t.phone_number,
            whatsapp=t.whatsapp,
            skype_id=t.skype_id,
            messenger_id=t.messenger_id,
        )
    )
    return render(
        request,
        "therapist_profile.html",
        context=dict(
            user=request.user,
            countries=countries,
            causes=causes,
            form=form,
            form_activity=form_activity,
        ),
    )


@login_required
@require_http_methods(["POST"])
def invite(request, cause_name, country):
    if not request.user.is_superuser and not request.user.coordinator:
        return JsonResponse(dict(success=False, errors=dict(form=["Access Denied"])))

    invite_form = InviteTherapistForm(request.POST)
    if not invite_form.is_valid():
        return JsonResponse(dict(success=False, errors=invite_forms.errors))

    cause = get_object_or_404(Cause, slug=cause_name)
    Invitation = get_invitation_model()
    invite = Invitation.create(request.POST["email"], inviter=request.user)
    invite.send_invitation(request)
    return JsonResponse(dict(success=True))

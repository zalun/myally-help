import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from invitations.utils import get_invitation_model

from .forms import InviteCoordinatorForm


@login_required
@require_http_methods(["POST"])
def invite(request, cause_name, country):
    if not request.user.is_superuser:
        return JsonResponse(dict(success=False, errors=dict(form=["Access Denied"])))

    invite_form = InviteCoordinatorForm(request.POST)
    if not invite_form.is_valid():
        return JsonResponse(dict(success=False, errors=invite_forms.errors))

    cause = get_object_or_404(Cause, slug=cause_name)
    Invitation = get_invitation_model()
    invite = Invitation.create(email, inviter=request.user)
    invite.send_invitation(request)
    return JsonResponse(dict(success=True))

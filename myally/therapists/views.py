from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ShortTherapistForm

@login_required
def index(request):
    if not getattr(request.user, "therapist", False) or not request.user.therapist.active:
        return HttpResponse("You're not an active Therapist.")

    t = request.user.therapist
    if request.method == "POST":
        form = ShortTherapistForm(request.POST)
        if form.is_valid():
            t.online = form.cleaned_data["online"]
            t.busy = form.cleaned_data["busy"]
            t.phone_number = form.cleaned_data["phone_number"]
            t.whatsapp = form.cleaned_data["whatsapp"]
            t.skype_id = form.cleaned_data["skype_id"]
            t.messenger_id = form.cleaned_data["messenger_id"]
            t.save()

    countries = [c.name for c in request.user.therapist.countries]
    causes = [c.name for c in request.user.therapist.causes.all()]
    form = ShortTherapistForm(
        dict(
            online=t.online,
            busy=t.busy,
            phone_number=t.phone_number,
            whatsapp=t.whatsapp,
            skype_id=t.skype_id,
            messenger_id=t.messenger_id
        )
    )
    return render(
        request, 
        "therapist_profile.html", 
        context=dict(user=request.user, countries=countries, causes=causes, form=form),
    )

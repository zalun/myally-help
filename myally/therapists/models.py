from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext as _

from causes.models import Cause


class Therapist(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="therapist",
    )
    causes = models.ManyToManyField(
        Cause,
        related_name="therapists",
        null=True,
        blank=True,
    )
    countries = CountryField(multiple=True)
    psychologist = models.BooleanField(blank=True, default=False)
    psychotherapist = models.BooleanField(blank=True, default=True)
    therapist = models.BooleanField(blank=True, default=False)
    specialisation = models.CharField(max_length=200)
    active = models.BooleanField(blank=True, default=True)
    online = models.BooleanField(blank=True, default=False)
    busy = models.BooleanField(blank=True, default=False)
    # contacts
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    whatsapp = models.BooleanField(blank=True, default=False)
    skype_id = models.CharField(max_length=200, blank=True, null=True)
    messenger_id = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ("busy",)
    def __str__(self):
        return "{user} / {specialisation}".format(
            user=str(self.user), specialisation=self.specialisation
        )

    @property
    def specialisation_str(self):
        specs = []
        if self.psychologist:
            specs.append(_("psychologist"))

        if self.psychotherapist:
            specs.append(_("psychotherapist"))

        if self.therapist:
            specs.append(_("psychotherapist"))

        specs.append(_(self.specialisation))
        return ", ".join(specs)

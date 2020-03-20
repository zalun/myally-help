from django.conf import settings
from django.db import models
from django_countries.fields import CountryField

from causes.models import Cause


class Therapist(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    causes = models.ForeignKey(
        Cause,
        related_name="therapists",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    countries = CountryField(multiple=True)
    specialisation = models.CharField(max_length=200)
    online = models.BooleanField(blank=True, default=False)
    busy = models.BooleanField(blank=True, default=False)
    # contacts
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    whatsapp = models.BooleanField(blank=True, default=False)
    skype_id = models.CharField(max_length=200, blank=True, null=True)
    messenger_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "{user} / {specialisation}".format(
            user=str(self.user), specialisation=self.specialisation
        )

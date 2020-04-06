from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from django.utils.translation import gettext as _

from causes.models import Cause


class Coordinator(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="coordinator",
    )
    causes = models.ManyToManyField(
        Cause, related_name="coordinators", through="CauseCoordinator"
    )

    def __str__(self):
        return "{first_name} {last_name}".format(
            first_name=self.user.first_name, last_name=self.user.last_name
        )


class CauseCoordinator(models.Model):
    coordinator = models.ForeignKey(Coordinator, on_delete=models.CASCADE)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
    country = CountryField()

    def __str__(self):
        return "{first_name} {last_name} for {cause}".format(
            first_name=self.coordinator.user.first_name,
            last_name=self.coordinator.user.last_name,
            cause=self.cause.name,
        )

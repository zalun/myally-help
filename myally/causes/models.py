from django.db import models
from django_countries.fields import CountryField


class Cause(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    countries = CountryField(multiple=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

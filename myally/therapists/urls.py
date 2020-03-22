from django.contrib.auth.decorators import login_required
from django.urls import include, path

from . import views

urlpatterns = [
    path("profile", login_required(views.index), name="therapist"),
]

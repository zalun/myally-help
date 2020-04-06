from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "invite/<str:cause_name>/<str:country>", views.invite, name="invite_coordinator"
    ),
]

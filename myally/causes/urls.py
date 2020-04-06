from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.therapists, name="cause", kwargs=dict(cause_name="covid_19")),
    path(
        "coordinators",
        views.coordinators,
        name="cause",
        kwargs=dict(cause_name="covid_19"),
    ),
    path("<str:cause_name>", views.therapists, name="cause"),
    path("<str:cause_name>/coordinators", views.coordinators, name="cause"),
]

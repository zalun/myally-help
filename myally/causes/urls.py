from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="cause", kwargs=dict(cause_name="coronavirus")),
    path("<str:cause_name>", views.index, name="cause"),
]

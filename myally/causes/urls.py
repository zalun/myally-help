from django.urls import include, path

from . import views

urlpatterns = [
    path("<str:cause_name>", views.index, name="cause"),
]

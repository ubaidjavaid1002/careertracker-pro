from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "applications/",
        views.application_list,
        name="application_list"
    ),

    path(
        "applications/add/",
        views.application_create,
        name="application_create"
    ),
]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='tracker/login.html',
            authentication_form=LoginForm
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

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
    path(
        "applications/<int:pk>/edit/",
        views.application_update,
        name="application_update"
    ),

    path(
        "applications/<int:pk>/delete/",
        views.application_delete,
        name="application_delete"
    ),
    path(
        "applications/<int:pk>/status/<str:new_status>/",
        views.update_status,
        name="update_status"
    ),
    path(
        "api/applications/",
        views.application_api,
        name="application_api"
    ),

    path(
        "api/dashboard/",
        views.dashboard_api,
        name="dashboard_api"
    ),
]
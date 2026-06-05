from django.shortcuts import render
from django.shortcuts import redirect

from .models import Application
from .forms import ApplicationForm
from django.shortcuts import get_object_or_404

def dashboard(request):

    applications = Application.objects.all()
    recent_applications = (Application.objects.order_by("-created_at")[:5])

    context = {

        "total_applications":
            applications.count(),

        "interviews":
            applications.filter(
                status="Interview"
            ).count(),

        "offers":
            applications.filter(
                status="Offer"
            ).count(),

        "rejections":
            applications.filter(
                status="Rejected"
            ).count(),

        "recent_applications": recent_applications,
    }

    return render(
        request,
        "tracker/dashboard.html",
        context
    )


def application_list(request):

    applications = (
        Application.objects
        .all()
        .order_by("-applied_date")
    )

    return render(
        request,
        "tracker/application_list.html",
        {
            "applications":
            applications
        }
    )


def application_create(request):

    if request.method == "POST":

        form = ApplicationForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "application_list"
            )

    else:

        form = ApplicationForm()

    return render(
        request,
        "tracker/application_form.html",
        {
            "form": form
        }
    )

def application_update(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk
    )

    if request.method == "POST":

        form = ApplicationForm(
            request.POST,
            instance=application
        )

        if form.is_valid():

            form.save()

            return redirect(
                "application_list"
            )

    else:

        form = ApplicationForm(
            instance=application
        )

    return render(
        request,
        "tracker/application_form.html",
        {
            "form": form
        }
    )


def application_delete(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk
    )

    application.delete()

    return redirect(
        "application_list"
    )
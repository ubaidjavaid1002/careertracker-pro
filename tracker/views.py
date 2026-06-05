from django.shortcuts import render
from django.shortcuts import redirect

from .models import Application
from .forms import ApplicationForm
from django.shortcuts import get_object_or_404
from django.db.models import Q

def dashboard(request):

    applications = Application.objects.all()
    recent_applications = (Application.objects.order_by("-created_at")[:5])
    total_applications = applications.count()
    offers = applications.filter(status="Offer").count()

    success_rate = 0

    if total_applications > 0:
        success_rate = round(
            (offers / total_applications) * 100,
            1
        )

    context = {

        "total_applications":total_applications,

        "applied":
            applications.filter(
                status="Applied"
            ).count(),

        "interviews":
            applications.filter(
                status="Interview"
            ).count(),

        "offers":offers,

        "rejections":
            applications.filter(
                status="Rejected"
            ).count(),

        "recent_applications": recent_applications,
        "success_rate": success_rate,
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
        .order_by('-created_at')
    )

    search = request.GET.get('search')
    status = request.GET.get('status')

    if search:

        applications = applications.filter(

            Q(company__icontains=search) |
            Q(position__icontains=search)

        )

    if status:

        applications = applications.filter(
            status=status
        )

    context = {

        "applications": applications,
        "search": search,
        "selected_status": status,

    }

    return render(
        request,
        "tracker/application_list.html",
        context
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

def update_status(
    request,
    pk,
    new_status
):

    application = get_object_or_404(
        Application,
        pk=pk
    )

    application.status = new_status

    application.save()

    return redirect(
        "application_list"
    )
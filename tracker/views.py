from django.shortcuts import render
from django.shortcuts import redirect

from .models import Application
from .forms import ApplicationForm, RegisterForm
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from datetime import date

def register(request):

    if request.method == 'POST':

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            user = form.save()

            login(request,user)
            return redirect('dashboard')

    else:

        form = RegisterForm()

    return render(
        request,
        'tracker/register.html',
        {
            'form': form
        }
    )

@login_required
def dashboard(request):

    applications = Application.objects.filter(user=request.user)
    recent_applications = Application.objects.filter(user=request.user).order_by("-created_at")[:5]
    total_applications = applications.count()
    offers = applications.filter(status="Offer").count()
    upcoming_interviews = (
        applications
        .filter(
            status="Interview",
            interview_date__gte=date.today()
        )
        .order_by(
            "interview_date",
            "interview_time"
        )[:5]
    )
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
        "upcoming_interviews": upcoming_interviews,
    }

    return render(
        request,
        "tracker/dashboard.html",
        context
    )

@login_required
def application_list(request):

    applications = Application.objects.filter(user=request.user).order_by('-created_at')

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

@login_required
def application_create(request):

    if request.method == "POST":

        form = ApplicationForm(
            request.POST
        )

        if form.is_valid():

            application = form.save(commit=False)
            application.user = request.user
            application.save()

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

@login_required
def application_update(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk,
        user=request.user
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

@login_required
def application_delete(request, pk):

    application = get_object_or_404(
        Application,
        pk=pk,
        user=request.user
    )

    application.delete()

    return redirect(
        "application_list"
    )

@login_required
def update_status(
    request,
    pk,
    new_status
):

    application = get_object_or_404(
        Application,
        pk=pk,
        user=request.user
    )

    application.status = new_status

    application.save()

    return redirect(
        "application_list"
    )
from django.shortcuts import render
from profiles.models import Profile


def home(request):
    profiles = Profile.objects.all()
    ctx = {
        "profiles": profiles
    }


    return render(request, "home.html", ctx)

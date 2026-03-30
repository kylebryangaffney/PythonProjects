from django.http import HttpResponse
from django.shortcuts import render

from .models import Profile
# Create your views here.

def profile_list(request):
    profiles = Profile.objects.all()
    ctx = {
        "profiles": profiles,
    }
    return render(request, "profiles/profile_list.html", ctx)

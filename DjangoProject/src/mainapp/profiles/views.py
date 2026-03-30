from django.http import HttpResponse
from django.shortcuts import render

from .models import Profile
# Create your views here.




def home(request):
    profiles = Profile.objects.all()
    return render(request, "profiles/products_page.html", {"profiles":profiles})


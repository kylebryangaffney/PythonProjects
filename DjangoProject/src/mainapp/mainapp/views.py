from django.shortcuts import render
from profiles.models import Profile

# gets all of the profile objects, then calls the render method from django with the home page we built, then passes in a dictionary of the profiles so that the home page html file has something to iterate over
def home(request):
    return render(request, "home.html")

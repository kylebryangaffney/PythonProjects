from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm
from .models import Profile
# Create your views here.

def profile_list(request):
    profiles = Profile.objects.all()
    ctx = {
        "profiles": profiles,
    }
    return render(request, "profiles/profile_list.html", ctx)


def profile_detail(request, pk):
    pk = int(pk)
    profile = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=profile)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            print(form.errors)
    ctx = {"form": form}
    return render(request, "profiles/profile_detail.html", ctx)



def profile_create(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    else:
        print(form.errors)
        form = ProfileForm()
    ctx = {"form": form}
    return render(request, "profiles/profile_create.html", ctx)


def profile_delete(request, pk):
    pk = int(pk)
    profile = get_object_or_404(Profile, pk=pk)
    if request.method == "POST":
        profile.delete()
        return redirect("home")
    ctx = {"profile": profile}
    return render(request, "profiles/profile_delete_confirm.html", ctx)



def profile_confirmed(request):
    if request.method == "POST":
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.delete()

    return redirect("home")




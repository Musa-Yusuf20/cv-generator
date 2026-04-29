from django.shortcuts import render
from myapp.models import Profile

# Create your views here.
def save_profile(request):
    return render(request,"myapp/accept.html")


def resume(request,id):
    user_profile = Profile.objects.get(id=id)
    return render(request,"myapp/resume.html", {"user_profile":user_profile})
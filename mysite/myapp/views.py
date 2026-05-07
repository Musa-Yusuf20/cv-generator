from django.shortcuts import render
from myapp.models import Profile

# Create your views here.

def dashboard(request):
    resumes = Profile.objects.all()
    return render(request,"myapp/dashboard.html",{"resumes":resumes})


def save_profile(request):
    if request.method=="POST":
        # step 1 get data from the form
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        degree = request.POST.get("degree")
        school = request.POST.get("school")
        university = request.POST.get("university")
        summary = request.POST.get("summary")
        previous_work = request.POST.get("previous_work")
        skills = request.POST.get("skills")
        profile = Profile(name=name,email=email,number=number,degree=degree,school=school,university=university,summary=summary,previous_work=previous_work,skills=skills,profile=profile)
        profile.save()
    return render(request,"myapp/accept.html")


def resume(request,id):
    user_profile = Profile.objects.get(id=id)
    return render(request,"myapp/resume.html", {"user_profile":user_profile})
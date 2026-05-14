from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Profile
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
import io

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
        return redirect("dashbord")
    return render(request,"myapp/accept.html")


def resume(request,id):
    user_profile = Profile.objects.get(id=id)
    return render(request,"myapp/resume.html", {"user_profile":user_profile})


def download_resume(request,id):
    user_profile = get_object_or_404(Profile,id=id)
    template_path = "myapp/download_resume.html"
    context ={"profile":user_profile}
    template= get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Dispostion"] = f'attachment; filename="{user_profile.name}_CV.pdf"'
    pisa_status= pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")),dest=response,encoding="UTF-8")
    if pisa_status.err:
        return HttpResponse("Error generating PDF", status=500)
    return response


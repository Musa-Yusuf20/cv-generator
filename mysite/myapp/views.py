from django.shortcuts import render

# Create your views here.
def save_profile(request):
    return render(request,"myapp/accept.html")

from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.save_profile,name="save_profile"),
]
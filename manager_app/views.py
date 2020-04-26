from django.shortcuts import render, redirect
from . import models
from login_app.models import User
# Create your views here.

##### DEVELOPMENT ######
def display_post(request):
    print("..........................")
    print("Printing data from request.POST.......")
    for k,v in request.POST.items():
        print(f"Key: {k}, Value: {v}")
    print("..........................")
    print("Printing data from request.FILES.......")
    if request.FILES == {}:
        print("No files uploaded")
    else:
        for k,v in request.FILES.items():
            print(f"Key: {k}, Value: {v}")
    print("..........................")

##### DEVELOPMENT ######


####### Helper Functions ########

def logged_user(request):    
    """ Get logged-in User object """
    return User.objects.filter(id=request.session["user_id"])[0]
####### Helper Functions #########

def index(request):
    context = {
        "user": logged_user(request)
    }
    return render(request, "dashboard.html", context)

from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.index, name="home"),
        # GET -> get home page
    path("login", views.login, name="login"), 
        # GET -> gets login page 
        # POST -> authenticates login attempt    
    path("registration", views.registration, name="registration"), 
        # GET -> gets registration page
        # POST -> authenticates registration attempt
    path("logout", views.logout, name="logout"),
        # POST -> destroys session
]
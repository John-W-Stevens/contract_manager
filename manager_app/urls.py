from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    # GET -> render dashboard.html
]
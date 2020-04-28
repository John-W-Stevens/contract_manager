from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
        # GET -> render dashboard.html
        # POST -> handles Create Contract/Customer/Carrier

    path("/carrier/<int:carrier_id>", views.carrier),
        # GET -> render carrier.html

    path("/customer/<int:customer_id>", views.customer),
        # GET -> render customer.html

    path("/contract/<int:contract_id>", views.contract),
        # GET -> render contract.html



    ########## Kevin's page ##############
    path('/update_carrier', views.update_carrier),
    path('/delete_carrier/<int:carrier_id>', views.delete_carrier),
    path('/update_carrier_phone', views.update_carrier_phone),
    ######################################

]
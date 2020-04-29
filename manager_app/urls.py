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

    path("/contract/<int:contract_id>", views.contract, name="contract_detail"),
        # GET -> render contract.html

    path('/edit_contract/<int:contract_id>',views.edit_contract),
        # Josh contract edit route
]